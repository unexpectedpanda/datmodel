---
hide:
  - footer
---

# `fileset`

The `fileset` array is a way to bundle together multiple groups of files and their
properties. For example, you might want to bundle multiple discs from a single title
together, so DAT applications know to keep those files together when filtering.

``` {.json .copy hl_lines="3 7-9 21"}
"fileset": [
  {
    "name": "Some Video Game (USA) (Disc 1)",
    "container": "auto",
    "id": "654319",
    "comments": "Something relevant about the set",
    "files": [
      ...
    ]
  },
  {
    "name": "Some Video Game (USA) (Disc 2)",
    "container": "auto",
    "id": "654320",
    "comments": "Something relevant about the set",
    "files": [
      ...
    ]
  },
  {
    "refId": "123456"
  }
]
```

## Required properties

<div class="definition-list" markdown>

* **`files`{ #files .toc-code }** `object array`{ .toc-def } `required`{ .toc-req }

    The files in the set and their properties.
    [Read more about the `files` array](files-set.md).

    {# Condition: Required when [`refId`](fileset.md#refId) isn't used. Not compatible with
    `refId`. #}

* **`name`{ #name .toc-code }** `pattern string`{ .toc-def } `condtionally required`{ .toc-req }

    Overrides the title [`name`](titles.md#name) key to become the archive or folder
    name used for the set.

    Names can't end with a period or space, start with a path separator, or use the
    following invalid path characters:

    ```
    :<>"|?*\
    ```

    Path separators are represented Linux-style, with `/` instead of `\`. Don't use
    absolute paths, paths are relative to a path the user sets.

    Condition: Required when the [`container`](#container) property isn't set to `null`.
    Optional when it is.

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

{#
* **`refId`{ #refId .toc-code }** `string`{ .toc-def } `conditonally required`{ .toc-req }

    Any properties not specified in the fileset are imported from the referenced
    [`sets`](sets.md) or `fileset` object, except for `id`. For more details, see
    [Reference other file sets](reference.md).

    Condition: Because it imports properties from other sets, an object with `refId` in it
    requires no other properties. Not compatible with `files`.
#}
</div>

## Optional properties

<div class="definition-list" markdown>

* **`comments`{ #comments .toc-code }** `string`{ .toc-def } `optional`{ .toc-opt }

    Comments related to the fileset.

* **`container`{ #container .toc-code }** `string`{ .toc-def } `optional`{ .toc-opt }

    The container that the DAT application should use for the file set. Must be one of the
    following values:

    * `auto`: Store the files in whatever container the user chooses in the DAT
      application. For example, a ZIP file, a 7Z file, a folder, or no container. The base
      file name of the container matches the [`name`](#name).

    * `folder`: Store the files in a folder named after the
      [`name`](#name).

    * `null`: Don't store the files in any container. Useful for keeping files by
      themselves, or for treating archives as files.

    {# * `archive`: Store the files in a specific archive type, named after the
      [`name`](#name). #}

    If this property isn't present, the DAT application assumes the value is `auto`.
    Unless the `container` is set to `null`, you must supply a [`name`](fileset.md#name).

* **`id`{ #id .toc-code }** `string`{ .toc-def } `optional`{ .toc-opt }

    A globally unique ID for the fileset item. Usually a database ID to ease lookups for
    DAT file maintainers.

</div>