from collections import defaultdict
import re
from typing import Callable, Dict, Optional
from packaging.version import parse as vparse

from util.release_data import ReleaseLib
from util.util import get_yn_input


def template_factory():
    """A dictionary for changelog regexes by library, with default."""
    return (
        r"""## \[?(?:\((?:Unr|R)eleased\) (?:- )?|(?:Unr|R)eleased (?:- )?)?"""
        r"""(?P<lib_name>[a-zA-Z-]+)[\s-](?P<lib_version>\d+\.\d+(?:\.\d+)?(?:-\d+)?)"""
        r"""(?P<for_rocm> for ROCm )?"""
        r"""(?P<rocm_version>(?(for_rocm)\d+\.\d+(?:\.\d+)?|.*))?"""
        r"""\]?\n"""
        r"""(?P<body>(?:(?!## ).*(?:(?!\n## )\n|(?=\n## )))*)"""
    )


def processor_factory():
    """A dictionary for regex processors by library, with default."""

    def default_processor(
        data: ReleaseLib, template: str, unchanged: Optional[bool] = None, ignore_unreleased = False
    ) -> bool:
        # Get the changelog for the provided library release.
        changelog = data.repo.get_contents("CHANGELOG.md", data.commit)
        changelog = changelog.decoded_content.decode()

        pattern = re.compile(template)
        latest_match: Optional[re.Match] = None
        for match in pattern.finditer(changelog):
            lib_name     = match["lib_name"]
            lib_version  = match["lib_version"]
            rocm_version = match["rocm_version"]

            if not rocm_version:
                print(match[0])
                if ignore_unreleased:
                    continue
                if not get_yn_input(
                    f"ROCm version not detected, release these ({lib_name}-"
                    f"{lib_version}) changes for ROCm {data.full_version}?"
                ):
                    continue
            elif vparse(match["rocm_version"]) > vparse(data.full_version):
                continue
            elif vparse(match["rocm_version"]) < vparse(data.full_version):
                latest_match = match

            data.message = (
                f"{match['lib_name']} {match['lib_version']} for ROCm"
                f" {data.full_version}"
            )
            data.notes = match["body"]
            data.lib_version = lib_version

            change_pattern = re.compile(
                r"^#+ +(?P<type>[^\n]+)$\n*(?P<change>(^(?!#).*\n*)*)",
                re.RegexFlag.MULTILINE
            )
            
            for match in change_pattern.finditer(data.notes):
                data.data.changes[match["type"]] = match["change"]
            return True

        is_previous = False
        for tag in data.repo.get_tags():
            if tag.commit.sha == data.commit:
                is_previous = True
                break
        latest_match = (
            pattern.search(changelog) if latest_match is None else latest_match
        )
        if is_previous or get_yn_input(
            "Could not find a valid changelog. Perform this release noting no"
            " changes?",
            unchanged,
        ):
            data.message = (
                f"{data.name} {latest_match['lib_version']} for ROCm"
                f" {data.full_version}"
            )
            data.notes = (
                f"{latest_match['lib_name']} code for ROCm"
                f" {data.rocm_version} did not change. The library was rebuilt"
                f" for the updated ROCm {data.rocm_version} stack."
            )
            return True
        return False

    return default_processor


TEMPLATES: Dict[str, str] = defaultdict(template_factory)
PROCESSORS: Dict[
    str, Callable[[ReleaseLib, str, Optional[bool]], bool]
] = defaultdict(processor_factory)
