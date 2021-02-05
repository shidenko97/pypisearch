import requests

import tabulate

from pypisearch import re_constants as const
from pypisearch.result_item import ResultItem


class Search:
    """Main search process instance."""

    def __init__(self, query: str, page: int = 1) -> None:
        self.search_url = f"https://pypi.org/search/?q={query}&page={page}"

    @property
    def get_page_data(self) -> str:
        """Returns page's HTML code."""

        return requests.get(url=self.search_url).text

    @property
    def plain_items(self) -> list:
        """Returns plain result items."""

        return const.ITEM_RE.split(self.get_page_data)

    @property
    def result(self) -> list:
        """Returns list of result instances."""

        return list(
            filter(
                lambda result_item: not result_item.is_empty,
                map(
                    lambda plain_item: ResultItem(plain_text=plain_item),
                    self.plain_items,
                ),
            )
        )

    @property
    def tabulated_result(self) -> str:
        """Returns tabulated list of results."""

        return (
            tabulate.tabulate(
                [
                    [
                        f"{item.name} ({item.version})",
                        f"{item.installed_description}{item.description}",
                    ]
                    for item in self.result
                ],
                tablefmt="plain",
            )
            or "Sorry, we haven't results by your query"
        )
