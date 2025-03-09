---
hide:
  - footer
---

# `updates`

The `updates` array contains objects that represent different updates for a
[`title`](titles.md). You can bundle updates and their dependent updates together, and
assign updates to specific sets.

In the following example, required properties are highlighted. The values are for example
only.

``` {.json .copy hl_lines="3 5 10-12"}
"updates": [
  {
    "latest": [
      {
        "name": "Some Video Game (USA) (Update v1.2)",
        "container": "auto",
        "matchSet": "bin",
        "id": "321654",
        "comments": "Something relevant about the update",
        "files": [
          ...
        ]
      },
      {
        "name": "Some Video Game (USA) (Update v1.1)",
        "container": "auto",
        "matchSet": "bin",
        "id": "321654",
        "comments": "Something relevant about the update",
        "files": [
          ...
        ]
      }
    ],
    "archived": [
      {
        "name": "Some Video Game (USA) (Update v1.01)",
        "container": "auto",
        "matchSet": "bin",
        "id": "321654",
        "comments": "Something relevant about the update",
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

    Contains the latest update for the title, and its dependency updates.

* **`name`{ #name .toc-code }** `pattern string`{ .toc-def } `required`{ .toc-req }

    The name of the update, in UTF-8. This is used for the name of the archive or folder
    of the contained update:

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

    The files in the update and their properties.
    [Read more about the `files` array](files-updates.md).

</div>

## Optional properties

<div class="definition-list" markdown>

* **`archived`{ #comments .toc-code }** `object array`{ .toc-def } `optional`{ .toc-opt }

    Updates that are no longer required to update a title to its latest version.

* **`comments`{ #comments .toc-code }** `string`{ .toc-def } `optional`{ .toc-opt }

    Comments related to the update.

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

    A unique ID for the update. Usually a database ID to ease lookups for DAT file
    maintainers.

* **`matchSet`{ #id .toc-code }** `string`{ .toc-def } `optional`{ .toc-opt }

    Updates are considered to be valid for all [`sets`](sets.md) by default.

    If the update only works with a particular set, add its [`name`](sets.md#name) here.
    For example:

    ``` {.json .copy}
    "matchset": "bin"
    ```

    This way if a title gets filtered out by a user, its updates do too.

</div>
