---
hide:
  - footer
---

# `set`

The `set` array contains objects that each describe an individual file set.

In the following example, required properties are highlighted. The values are for example
only.

``` {.json .copy hl_lines="8-10"}
"set": [
  {
    "name": "Some Video Game (USA)",
    "container": "auto",
    "id": "654321",
    "comments": "Something relevant about the set",
    "retroachievements": True,
    "files": [
        ...
    ]
  }
]
```

## Required properties

<div class="definition-list" markdown>

* **`files`{ #files .toc-code }** `object array`{ .toc-def } `required`{ .toc-req }

    The files in the set and their properties.
    [Read more about the `files` array](files-set.md).

</div>

## Optional properties

<div class="definition-list" markdown>

* **`comments`{ #comments .toc-code }** `string`{ .toc-def } `optional`{ .toc-opt }

    Comments related to the set.

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

    A unique ID for the set. Usually a database ID to ease lookups for DAT file
    maintainers.

* **`name`{ #name .toc-code }** `pattern string`{ .toc-def } `optional`{ .toc-opt }

    Overrides the title [`name`](titles.md#name) key to become the archive or folder
    name used for the set. Generally only used when
    [bundling together multiple discs](discs.md) from the same set to avoid name clashes.

    Can only be used if the [`container`](#container) isn't set to `null`.

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

* **`retroachievements`{ #retroachievements .toc-code }** `boolean`{ .toc-def } `optional`{ .toc-opt }

    Whether or not retroachievements are supported on the title.

</div>