import requests
from typing import List, Optional

import tabulate

from pypisearch import re_constants as const
from pypisearch.result_item import ResultItem


class Search:
    """Main search process instance."""

    pypi_search_url = "https://pypi.org/search/?q={query}&page={page}"

    def __init__(
        self,
        query: str,
        page_from: str = "",
        page_to: Optional[str] = None,
    ) -> None:
        page_from, page_to = int(page_from), int(page_to) if page_to else None
        self.result = []

        if page_to is None:
            self.result = self.download_data(query=query, page=page_from)
        else:
            for page in range(page_from, page_to + 1):
                result = self.download_data(query=query, page=page)

                if not result:
                    break

                self.result.extend(result)

    def download_data(self, *, query: str, page: int) -> List[ResultItem]:
        url = self.pypi_search_url.format(query=query, page=page)
        page_data = requests.get(url=url).text
        items = const.ITEM_RE.split(page_data)
        result = list(
            filter(
                lambda result_item: not result_item.is_empty,
                map(
                    lambda plain_item: ResultItem(plain_text=plain_item),
                    items,
                ),
            )
        )

        return result

    @property
    def tabulated_result(self) -> str:
        """Returns tabulated list of results."""

        return tabulate.tabulate(
            [
                [
                    f"{item.name} ({item.version})",
                    f"{item.installed_description}{item.description}",
                ]
                for item in self.result
            ],
            tablefmt="plain",
        )
