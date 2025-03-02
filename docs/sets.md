---
hide:
  - footer
---

# `sets`

The `sets` array contains objects that represent different file sets within a
[`release`](releases.md). For example, you might have a file set which describes both the
BIN+CUE version of a release, _and_ the CHD version.

``` {.json .copy}
"sets": [
  {
    "name": "bin",
    "set": [
      {
        "container": "auto",
        "files": [
          ...
        ]
      }
    ]
  },
  {
    "name": "chd",
    "set": [
      {
        "container": null,
        "files": [
          ...
        ]
      }
    ]
  }
]
```

There must be a minimum of one file set in the `sets` array. If there is more than one
file set, then applications that process DAT files should let the user choose which file
set or file sets they want to keep, and let them assign different output paths per file
set.

This capability means a single DAT file can cover multiple formats. For example, a disc
image in ISO, CHD, _and_ RVZ formats. Or a ROM in encrypted _and_ decrypted formats. A
user can keep one file set or many, routing the output for each to different paths if they
want.

/// details | Expand for developer details
Don't allow different sets to be assigned to the same folder, or you could end up with
naming clashes.
///

## Required properties

<div class="definition-list" markdown>

* **`name`{ #name .toc-code }** `string`{ .toc-def } `required`{ .toc-req }

    The name of the set. Can be any non-empty string, although generally you should use
    lowercase container format names. For example:

    * `bin`

    * `chd`

    * `ciso`

    * `gdi`

    * `iso`

    * `rvz`

    * `xiso`

    Use the following for decrypted and encrypted content:

    * `decrypted`

    * `encrypted`

    Use the following for files that shouldn't be stored in a container:

    * `files`

* **`set`{ #set .toc-code }** `object array`{ .toc-def } `required`{ .toc-req }

    The file set contents. For more information, see [The `set` array](#set-array)

</div>

## The `set` array { #set-array }

Contains objects that each describe an individual set.

### Required properties

<div class="definition-list" markdown>

* **`container`{ #container .toc-code }** `string`{ .toc-def } `optional`{ .toc-opt }

    The container that the application managing the DAT file should use for the file set.
    Must be one of the following values:

    * `auto`: Store the files in whatever container the user chooses in the
      application that's managing the DAT file. For example, a ZIP file, a 7Z file,
      a folder, or no container. The base file name of the container matches the
      [release name](releases.md#name).

    * `folder`: Store the files in a folder named after the
      [release name](releases.md#name).

    * `null`: Don't store the files in any container. Useful for keeping files by
      themselves, or for treating archives as files.

    {# * `archive`: Store the files in a specific archive type, named after the
      [release name](releases.md#name). #}

* **`files`{ #files .toc-code }** `object array`{ .toc-def } `optional`{ .toc-opt }

    The files in the set and their properties.
    [Read more about the `files` array](files.md).

</div>

### Optional properties

<div class="definition-list" markdown>

* **`container_name`{ #container_name .toc-code }** `pattern string`{ .toc-def } `optional`{ .toc-opt }

    Overrides the release [`name`](releases.md#name) key to become the archive or folder
    name used for the set. Generally only used when
    [bundling together multiple discs](discs.md) from the same set to avoid name clashes.

    Can only be used if the `container` isn't set to `null`.

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

* **`comments`{ #comments .toc-code }** `string`{ .toc-def } `optional`{ .toc-opt }

    Comments related to the set.

* **`retroachievements`{ #retroachievements .toc-code }** `boolean`{ .toc-def } `optional`{ .toc-opt }

    Whether or not retroachievements are supported on the title.
