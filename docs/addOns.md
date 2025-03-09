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

``` {.json .copy hl_lines="3 5 10-12"}
"addOns": [
  {
    "latest": [
      {
        "name": "Some Video Game - DLC 2 (USA) (v1.2)",
        "container": "auto",
        "matchSet": "bin",
        "id": "456123",
        "comments": "Something relevant about the add-on",
        "files": [
          ...
        ]
      },
      {
        "name": "Some Video Game - DLC 1 (USA)",
        "container": "auto",
        "matchSet": "bin",
        "id": "456123",
        "comments": "Something relevant about the add-on",
        "files": [
          ...
        ]
      },
    ],
    "archived": [
      {
        "name": "Some Video Game - DLC 2 (USA) (v1.1)",
        "container": "auto",
        "matchSet": "bin",
        "id": "456123",
        "comments": "Something relevant about the add-on",
        "files": [
          ...
        ]
      }
    ]
  }
]
```

## Required properties

<div class="definition-list" markdown>

* **`latest`{ #latest .toc-code }** `object array`{ .toc-def } `required`{ .toc-req }

    Contains the latest add-ons for the title, and other add-ons it should be bundled
    with. The latest versions of all add-ons should be added here, along with any
    dependencies.

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

* **`archived`{ #comments .toc-code }** `object array`{ .toc-def } `optional`{ .toc-opt }

    Add-ons that are no longer required to provide the latest content to a title.

* **`comments`{ #comments .toc-code }** `string`{ .toc-def } `optional`{ .toc-opt }

    Comments related to the add-on.

* **`container`{ #container .toc-code }** `string`{ .toc-def } `optional`{ .toc-opt }

    The container that the DAT manager should use for the file set. Must be one of the
    following values:

    * `auto`: Store the files in whatever container the user chooses in the
      application that's managing the DAT file. For example, a ZIP file, a 7Z file,
      a folder, or no container. The base file name of the container matches the
      [title name](titles.md#name).

    * `folder`: Store the files in a folder named after the [title name](titles.md#name).

    * `null`: Don't store the files in any container. Useful for keeping files by
      themselves, or for treating archives as files.

    {# * `archive`: Store the files in a specific archive type, named after the
      [title name](titles.md#name). #}

    If this property isn't present, the DAT manager assumes the value is `auto`.

* **`id`{ #id .toc-code }** `string`{ .toc-def } `optional`{ .toc-opt }

    A unique ID for the add-on. Usually a database ID to ease lookups for DAT file
    maintainers.

* **`matchSet`{ #id .toc-code }** `string`{ .toc-def } `optional`{ .toc-opt }

    Add-ons are considered to be valid for all [`sets`](sets.md) by default.

    If the add-on only works with a particular set, add its [`name`](sets.md#name) here.
    For example:

    ``` {.json .copy}
    "matchset": "bin"
    ```

    This way if a title gets filtered out by a user, its add-ons do too.

</div>
