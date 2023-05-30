"""
=====
Utils
=====

:Author: Joshua Rose
:Version: 2.0.0 of 2023/05/28
:License: `Apache 2.0 <https://gh-syn.github.io/urban-cli/license.html>`_
:File: urban_utils.py

This file contains utility functions and helper methods.
It is responsible for the following functions.

Data Manipulation
-----------------
When a request object is received, it needs to be formatted in a way that Python can understand
The beautifulsoup library helps beautifully ✨ with this. It parses html data in a way that can be
read and manipulated very easily.

I/O handling
------------
The argparse library can be thought of as boilerplate level code in addition to a few extra classes
that greatly help building a command line interface. It removes most of the argument logic and lets the
developer focus on what's important. Argparse is used in this file for showing and receiving data.

Common Data Structures
-----------------------
Common data structures such as a date, definition struct, lives in this file.
"""

from typing_extensions import deprecated

from bs4 import BeautifulSoup
import bs4
import requests
import rich

from urban_definition import Definition


def show_does_not_exit_error(word: str):
    """
    Show does not exist error when invalid word is queried.

    A type error is not raised as data type is checked in `send_phrase_request` function.

    :param word: The invalid word that apparently doesn't exist.
    """

    rich.print("The word %s doesn't exist yet." % word, end=" ")
    rich.print(
        "You can change that by submitting a definition on the {link}".format(
            link="[link url='https://urbandictionary.com/']Urban Dictionary website.[/link]"
        )
    )


@deprecated("Removed in favour of indexing")
def _get_num_of_definitions(result_set: bs4.ResultSet) -> int:  # pyright: ignore
    """
    Returns the number of definitions found for a given word

    :param result_set: A list of tags, defined as a result set object.

    :return: Number of definitions for a given word as an `int`.
    """

    return len(result_set)


def make_soup_from_response(response: requests.Response):
    """
    When life gives you ~~lemons~~ a `response` object... make soup?

    Take a requests.response and extract response from it - thus returning a soup object.

    :param response: Response object assumedly containing one or more definition(s).
    :return: ~~lemonade~~ A beautiful soup 🍜
    """

    response_content: bytes = response.content

    response_soup = BeautifulSoup(response_content, "lxml")

    return response_soup


@deprecated("Indexed tag used in favour of stringifying `definition_tag`.")
def stringify_definition_tag(definition_tag: bs4.Tag) -> str:
    """
    Convert a definition tag into a string.

    This function assumes it's known with 100% certainty that `definition_tag`
    is indeed a *definition* tag, which this function will 'stringify'.

    :param definition_tag: Definition tag that is 100% known to contain a definition
    :return: `stringified` definition
    """

    return str(definition_tag.strings)


def format_wotd_content(soup: BeautifulSoup) -> Definition:
    """
    Format word of the day content response from a soup into a definition.

    :param soup: Content received from the word of the day site
    :return: Definition object formatted from content and parsed using bs4
    """

    _definition = Definition(soup=soup)

    return _definition


def author_hyperlink_reference(href: str):
    """
    Return author from hyperlink reference.

    This function takes a hyperlink reference.
    For example, a reference that looks like this:

    <div class="contributor font-bold">
        by <a class=
            "text-denim dark:text-fluorescent hover:text-limon-lime"
            href="/author.php?author=CynderFanclub">CynderFanclub</a>
        April 14, 2020
    </div>

    will extract the author by:
      a) making a soup from the reference
      b) using the soup to get the value inside of the <a> tags like this </a>

    :param href: Hyperlink reference as a string containing a valid author and link tag.
    :raises Exception: if the string doesn't contain a valid tag.
    :return: Extracted author value from href.
    """

    soup = BeautifulSoup(href, "lxml")

    a_tag = soup.select_one("a")

    if a_tag is None:
        raise Exception("String / `soup` does not contain <a>")

    return a_tag.value


def get_facebook_link(soup: BeautifulSoup):
    """
    Get facebook link from soup object.

    The link pertains to the specific definition value.

    :return: facebook link as a string value from a given definition.
    """
