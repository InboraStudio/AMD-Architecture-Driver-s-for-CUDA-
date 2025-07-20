from collections import defaultdict
from typing import Dict, List, TextIO, Tuple
from jinja2 import Environment, FileSystemLoader
from util.release_data import ReleaseBundle
from packaging.version import Version

class Changelog():
    releases: List[Tuple[str, ReleaseBundle]]
    """List of release bundles by version, ordered by latest first."""

    rocm_ver_by_lib_ver: Dict[str, Dict[str, str]]
    """Dictionary that maps per library, a library version to the releasing rocm version."""

    prev_lib_ver: Dict[str, Dict[str, str]]
    """Dictionary that maps per library a library version to the previous library version."""

    def __init__(self, releases: Dict[str, ReleaseBundle]):
        self.releases = list(releases.items())
        # self.releases.sort(key=lambda x: Version(x[0]), reverse=True)

        # For each library find the earliest ROCm release where it updated.
        rocm_ver_by_lib_ver: Dict[str, Dict[str, str]] = defaultdict(dict)
        for rocm_version, release in releases.items():
            for lib_name, lib in release.libraries.items():
                lib_version = lib.lib_version
                if lib_version not in rocm_ver_by_lib_ver[lib_name]:
                    # New lib version in this rocm_release.
                    rocm_ver_by_lib_ver[lib_name][lib_version] = rocm_version
                elif Version(rocm_version) < Version(rocm_ver_by_lib_ver[lib_name][lib_version]):
                    # Same lib version but updated in earlier ROCm release.
                    rocm_ver_by_lib_ver[lib_name][lib_version] = rocm_version

        self.rocm_ver_by_lib_ver = rocm_ver_by_lib_ver

        # For each library version find the previous library.
        prev_lib_ver: Dict[str, Dict[str, str]] = defaultdict(dict)
        for name, lib_versions in rocm_ver_by_lib_ver.items():
            prev_version = None
            for lib_version in lib_versions:
                if prev_version:
                    prev_lib_ver[name][lib_version] = prev_version
                prev_version = lib_version
        self.prev_lib_ver = prev_lib_ver

    def write_to_file(self, output: TextIO):
        """Writes the changelog to a text file."""
        env = Environment(loader=FileSystemLoader("templates/"))
        template = env.get_template("changelog.jinja")

        content = template.render(
            releases=self.releases,
            rocm_ver_by_lib_ver=self.rocm_ver_by_lib_ver,
            prev_lib_ver=self.prev_lib_ver
        )

        output.write(content)
