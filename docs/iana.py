import json
import pathlib
import requests
import sys

from bs4 import BeautifulSoup as bs
from typing import Any


def main() -> None:
    # Download the language subtags and their description
    iana_languages: requests.Response = requests.get(
        "https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry"
    )

    # Filter for pairs of subtags and descriptions, and add them to a list
    languages: list[dict[str, Any]] = []
    code: str = ""
    description: list[str] = []
    deprecated: bool = False
    preferred_code: str = ''


    for line in iana_languages.text.split("\n"):
        if line.startswith("Subtag"):
            code = line[8:]

        if line.startswith("Description"):
            description.append(line[13:])

        if line.startswith("Deprecated"):
            deprecated = True

        if line.startswith("Preferred-Value"):
            preferred_code = line[17:]

        if line == "%%":
            if code and description:
                if deprecated and preferred_code:
                    languages.append({"code": code, "description": description, "deprecated": deprecated, "use": preferred_code})
                elif deprecated:
                    languages.append({"code": code, "description": description, "deprecated": deprecated})
                else:
                    languages.append({"code": code, "description": description})
            code = ""
            description = []
            deprecated = False
            preferred_code = ''


    # Order the languages list by description
    languages.sort(key=lambda d: d["description"])

    # Add the languages list to a dictionary
    languages_dict: dict[str, list[dict[str, Any]]] = {
        "languages": languages
    }

    # Write to the appropriate file depending on the user-provided argument
    if len(sys.argv) > 1:
        if sys.argv[1] == "json":
            write_to_json(languages_dict)
        elif sys.argv[1] == "html":
            html_list: list[str] = ['<ul>']

            for language in languages:
                if 'deprecated' in language:
                    if 'use' in language:
                        html_list.append(f'<li class="deprecated"><code><s>{language['code']}</s></code> - {', '.join(language['description'])} (deprecated, use <code>{language['use']}</code>)</li>')
                    else:
                        html_list.append(f'<li class="deprecated"><code><s>{language['code']}</s></code> - {', '.join(language['description'])} (deprecated, no replacement code yet)</li>')
                else:
                    html_list.append(f'<li><code>{language['code']}</code> - {', '.join(language['description'])}</li>')

            html_list.append('</ul>')

            soup = bs(''.join(html_list), features='html.parser', preserve_whitespace_tags=['code', 'li'])

            with open(pathlib.Path("languages.html"), "w", encoding="utf-8") as file:
                file.write(str(soup.prettify()))

    else:
        write_to_json(languages_dict)


def write_to_json(languages_dict: dict[str, list[dict[str, Any]]]) -> None:
    """ Write to a valid UTF-8 JSON file, languages.json

    Args:
        languages_dict (dict[str, list[dict[str, Any]]]): The languages dictionary.
    """
    with open(pathlib.Path("languages.json"), "w", encoding="utf-8") as file:
        json.dump(languages_dict, file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
