---
hide:
  - footer
---

# `addOns`

The `addOns` array contains objects that represent add-ons, like downloadable content
(DLC) for a [`title`](titles.md). You can bundle add-ons together, and assign them to
specific sets.

In the following example, required properties are highlighted. The values are for example
only.

``` {.json .copy hl_lines="3 8-10"}
"addOns": [
  {
    "name": "Some Video Game - DLC 2 (USA) (v1.2)",
    "container": "auto",
    "requiresId": ["123456", "456122"],
    "id": "456123",
    "comments": "Something relevant about the add-on",
    "files": [
      ...
    ]
  },
  {
    "name": "Some Video Game - DLC 1 (USA)",
    "container": "auto",
    "requiresId": ["123456"],
    "id": "456122",
    "comments": "Something relevant about the add-on",
    "files": [
      ...
    ]
  },
  {
    "name": "Some Video Game - DLC 2 (USA) (v1.1)",
    "container": "auto",
    "requiresId": ["123456"],
    "superseded": true,
    "id": "456121",
    "comments": "Something relevant about the add-on",
    "files": [
      ...
    ]
  }
]
```

## Required properties

<div class="definition-list" markdown>

* **`name`{ #name .toc-code }** `pattern string`{ .toc-def } `required`{ .toc-req }

    The name of the add-on, in UTF-8. This is used for the name of the archive or folder
    of the contained add-on:

    Names can't end with a period or space, start with a path separator, or use the
    following invalid path characters:

    ```
    :<>"|?*\
    ```

    Path separators are represented Linux-style, with `/` instead of `\`. Don't use
    absolute paths, paths are relative to a path the user sets.

    /// details | Expand for developer details
    Invalid path characters are found with the following regular expression:

    ``` {.text .copy}
    ^[^:<>\"\\|?*].*[^. :<>\"\\|?*]$
    ```

    Non-UTF-8 characters are found with the following regular expressions:

    ``` {.text .copy}
    [\xC0-\xC1]
    [\xF5-\xFF]
    \xE0[\x80-\x9F]
    \xF0[\x80-\x8F]
    [\xC2-\xDF](?![\x80-\xBF])
    [\xE0-\xEF](?![\x80-\xBF]{2})
    [\xF0-\xF4](?![\x80-\xBF]{3})
    (?<=[\x00-\x7F\xF5-\xFF])[\x80-\xBF]
    (?<![\xC2-\xDF]|[\xE0-\xEF]|[\xE0-\xEF][\x80-\xBF]|[\xF0-\xF4]|[\xF0-\xF4][\x80-\xBF]|[\xF0-\xF4][\x80-\xBF]{2})[\x80-\xBF]
    (?<=[\xE0-\xEF])[\x80-\xBF](?![\x80-\xBF])
    (?<=[\xF0-\xF4])[\x80-\xBF](?![\x80-\xBF]{2})
    (?<=[\xF0-\xF4][\x80-\xBF])[\x80-\xBF](?![\x80-\xBF])
    ```
    ///

* **`files`{ #files .toc-code }** `object array`{ .toc-def } `required`{ .toc-req }

    The files in the add-on and their properties.
    [Read more about the `files` array](files-addOns.md).

</div>

## Optional properties

<div class="definition-list" markdown>

* **`comments`{ #comments .toc-code }** `string`{ .toc-def } `optional`{ .toc-opt }

    Comments related to the add-on.

* **`container`{ #container .toc-code }** `string`{ .toc-def } `optional`{ .toc-opt }

    The container that the DAT application should use for the file set. Must be one of the
    following values:

    * `auto`: Store the files in whatever container the user chooses in the DAT
      application. For example, a ZIP file, a 7Z file, a folder, or no container. The base
      file name of the container matches the add-on [`name`](addOns.md#name).

    * `folder`: Store the files in a folder named after the add-on
      [`name`](addOns.md#name).

    * `null`: Don't store the files in any container. Useful for keeping files by
      themselves, or for treating archives as files.

    {# * `archive`: Store the files in a specific archive type, named after the
      add-on [`name`](addOns.md#name). #}

    If this property isn't present, the DAT application assumes the value is `auto`.

* **`id`{ #id .toc-code }** `string`{ .toc-def } `optional`{ .toc-opt }

    A gobally unique ID for the add-on. Usually a database ID to ease lookups for DAT file
    maintainers. Might be referenced by a DAT application when finding dependencies for
    other add-ons, or when present in a [`containsId`](titles.md#containsId) property.

* **`requiresId`{ #requiresId .toc-code }** `string`{ .toc-def } `optional`{ .toc-opt }

    Which titles and updates the specific add-on requires to function, as identified by
    their globally unique IDs.

    This way if a title gets selected during filtering, its relevant add-ons can be
    selected too. Conversely, if a title gets filtered out, there's an opportunity to
    remove its add-ons as well.

    Add-ons are considered to be valid for all [`sets`](sets.md).

    /// details | Expand for developer details
    The most optimal behavior here is likely first walking the `addOns` array for the
    required ID, and then on a miss going up one level to `collections`, and walking the
    `titles` array for the required ID.
    ///

* **`superceded`{ #superseded .toc-code }** `boolean`{ .toc-def } `optional`{ .toc-opt }

    Add-ons kept for archival purposes, that are no longer required to update a title to
    its latest version.

    If this property isn't present, the DAT application assumes the value is `false`.

</div>
