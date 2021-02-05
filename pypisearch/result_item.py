from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as pkg_version

import pypisearch.re_constants as const


class ResultItem:
    """Result item instance of search."""

    def __init__(self, plain_text: str) -> None:
        self.plain_text = plain_text

    @property
    def is_empty(self) -> bool:
        """Check is current instance empty."""

        return not all([self.name, self.version, self.description])

    @property
    def name(self) -> str:
        """Returns item name."""

        name = const.NAME_RE.findall(self.plain_text)
        return name[0] if name else ""

    @property
    def version(self) -> str:
        """Returns item version."""

        version = const.VERSION_RE.findall(self.plain_text)
        return version[0] if version else ""

    @property
    def description(self) -> str:
        """Returns item description."""

        description = const.DESCRIPTION_RE.findall(self.plain_text)
        return description[0] if description else ""

    @property
    def is_installed(self) -> bool:
        try:
            pkg_version(self.name)
        except PackageNotFoundError:
            return False
        else:
            return True

    @property
    def get_installed_version(self) -> str:
        return pkg_version(self.name) if self.is_installed else ""

    @property
    def installed_description(self) -> str:
        return (
            f"[installed {self.get_installed_version}] "
            if self.is_installed
            else ""
        )
