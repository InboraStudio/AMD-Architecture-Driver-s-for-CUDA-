"""Utility functions."""


from typing import Optional


def get_yn_input(prompt: str, force_result: Optional[bool] = None, default: str = "n") -> bool:
    """Prompt a user and get a yes/no answer."""
    if force_result is not None:
        return force_result
    response = ""
    while not response.lower() in ["y", "n", "yes", "no"]:
        try:
            response = input(prompt + " [(y)es/(n)o] ")
        except EOFError:
            return default in ["y", "Y"]
    return response[0] in ["y", "Y"]
