import re


DESCRIPTION_RE = re.compile(
    r".*<p class=\"package-snippet__description\">(.+)</p>"
)
ITEM_RE = re.compile(r"<a class=\"package-snippet\".*>")
NAME_RE = re.compile(r"<span class=\"package-snippet__name\">(.+)</span>")
VERSION_RE = re.compile(
    r".*<span class=\"package-snippet__version\">(.+)</span>"
)
