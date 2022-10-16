import argparse

from pypisearch.search import Search


def main() -> None:
    """Main program entrypoint."""

    # Get command arguments
    arg_parser = argparse.ArgumentParser(
        description="Custom pip-search utility by pypi search line"
    )
    arg_parser.add_argument(
        "q", metavar="query", type=str, help="query for search"
    )
    arg_parser.add_argument(
        "-p",
        "--page",
        default="1",
        metavar="page",
        type=str,
        help="search page (default 1, could be range of pages like 1-5)",
    )
    args = arg_parser.parse_args()

    page = args.page

    if "-" in page:
        page_from, page_to = args.page.split("-")
        if page_from > page_to:
            raise ValueError("Page from shouldn't be greater then page to")
    else:
        page_from = page
        page_to = None

    # Parse search url and print result table
    search = Search(query=args.q, page_from=page_from, page_to=page_to)
    print(search.tabulated_result or "No results")


if __name__ == "__main__":
    main()
