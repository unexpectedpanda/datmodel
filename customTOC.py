# Inspired by https://github.com/mh166/mkdocs-custom-anchors/blob/main/customAnchors.py
#
# Looks for user-specified HTML tags with a specific class in an mkdocs page, and adds
# those tags to the TOC, so long as they also provide an id.
#
# For example, if you use the following settings:
#
# user_specified_html_tag = 'code'
# user_specified_class = 'toc-code'
# include_html_in_toc = True
#
# And this is in the body of your mkdocs page:
#
# `Add me to the TOC!`{ #addme .toc-code }
#
# Or this:
#
# <code id="addme" class="toc-code">Add me to the TOC!</code>
#
# Then "Add me to the TOC!" will be added to the TOC, along with the HTML formatting
# given to the text by the <code> tags.

import re
from copy import deepcopy
from typing import TYPE_CHECKING, Any

from bs4 import BeautifulSoup
from mkdocs.structure.pages import Page
from mkdocs.structure.toc import AnchorLink

if TYPE_CHECKING:
    from bs4 import element

# Set the following variables to the HTML element and class you want to use to identify
# fragments to add to the TOC.
user_specified_html_tag: str = "code"
user_specified_class: str = "toc-code"

# Set the following variable to False to render the TOC entries as plain text. Otherwise
# all HTML used in the identified fragment is also used in the TOC.
include_html_in_toc: bool = True


def add_to_toc(link: AnchorLink, page_html: str) -> None:
    """Goes through the HTML in an mkdocs page, finds a user-specified HTML tag, and adds
    it to the TOC.

    Args:
        link (AnchorLink): The top level H1 entry of the page.
        page_html (str): The HTML content of the page.
    """

    # Parse the HTML from the page
    soup = BeautifulSoup(page_html, "lxml")

    # Get the user-specified tags we want to add to the TOC
    toc_tags: element.ResultSet[Any] = soup.find_all(
        user_specified_html_tag, class_=user_specified_class
    )

    if toc_tags:
        # Get the closest heading to each of the user-specified tags, and then pair it
        # with the tag in a tuple and add it to a list
        toc_placement: list[tuple[Any, Any]] = []

        for tag in toc_tags:
            closest_tag: element.tag = tag.find_previous(re.compile("^h[1-3]$"))
            toc_placement.append((closest_tag, tag))

        for item in reversed(toc_placement):
            # Add the user-specified tag as a child to the appropriate heading
            if "id" in item[0].attrs and "id" in item[1].attrs:
                add_children(link, item)


def add_children(link: AnchorLink, item: tuple[Any, Any]) -> None:
    """Traverse down the children in a TOC entry, looking for the appropriate heading to
    add a user-specified TOC entry to as a child.

    Args:
        link (AnchorLink): The TOC entry to check if a child entry should be added to it.
        item (tuple[Any, Any]): A tuple containing the ID to match against in the TOC
          entry, and the child to add to it.
    """
    search_for_heading = item[0].attrs["id"]

    if link.id == search_for_heading:
        if include_html_in_toc:
            # Strip the ID from the tag being added to the TOC
            toc_entry = deepcopy(item[1])
            del toc_entry["id"]
            # Add the TOC entry with surrounding HTML code
            link.children.insert(
                0, AnchorLink(toc_entry, item[1].attrs["id"], link.level + 1)
            )
        else:
            # Add the TOC entry as just text
            link.children.insert(
                0,
                AnchorLink(
                    str(item[1].get_text()), item[1].attrs["id"], link.level + 1
                ),
            )
    else:
        if link.children:
            for child in link.children:
                add_children(child, item)


def on_page_content(page_html: str, page: Page, **kwargs: Any) -> None:
    """Automatically runs on pages in your doc set.

    Iterates through the links already added to the TOC, and passes them to
    custom_headings().

    Args:
        page_html (str): The HTML content of the page.
        page (Page): The mkdocs page properties.
    """

    for link in page.toc:
        add_to_toc(link, page_html)

    # Uncomment the following lines for debug output based on a specific page
    # if page.file.src_uri == 'releases.md':
    #     dump_links(link)


def dump_links(link: AnchorLink, depth: int = 0) -> None:
    padding = " " * 2 * (depth + 1)
    print(f"{padding}- [{link.level}] {link.title} => {link.url}")
    if len(link.children) > 0:
        print(f"{padding}  -> {len(link.children)} children")
        for child in link.children:
            dump_links(child, depth + 1)
