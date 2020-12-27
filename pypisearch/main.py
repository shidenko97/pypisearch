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
        default=1,
        metavar="page",
        type=int,
        help="search page (default 1)",
    )
    args = arg_parser.parse_args()

    # Parse search url and print result table
    search = Search(query=args.q, page=args.page)
    print(search.tabulated_result)


if __name__ == "__main__":
    main()
