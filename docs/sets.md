---
hide:
  - footer
---

# `sets`

The `sets` array contains objects that represent different file sets within a
[`title`](titles.md). For example, you might have a file set which describes both the
BIN+CUE version of a title, _and_ the CHD version.

In the following example, required properties are highlighted. The values are for example
only.

``` {.json .copy hl_lines="8-10"}
"sets": [
  {
    "name": "bin",
    "container": "auto",
    "id": "654321",
    "comments": "Something relevant about the set",
    "retroachievements": true,
    "files": [
      ...
    ]
  },
  {
    "name": "chd",
    "files": [
        ...
    ]
  }
]
```

There must be a minimum of one file set in the `sets` array. If there is more than one
file set, then DAT applications should let the user choose which file set or file sets
they want to keep based on the [`name`](#name), and let them assign different output paths
per file set.

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

* **`files`{ #files .toc-code }** `object array`{ .toc-def } `required`{ .toc-req }

    The files in the set and their properties.

    You must use either the `files` array at this level, or the `fileset` array, not both.

    [Read more about the `files` array](files-set.md).

* **`fileset`{ #fileset .toc-code }** `object array`{ .toc-def } `required`{ .toc-req }

    Multiple groups of `files` and their properties. Useful for bundling together separate
    parts of a title. For example, multiple discs in a single release.

    You must use either the `files` array at this level, or the `fileset` array, not both.

    [Read more about the `fileset` array](fileset.md).

</div>

## Optional properties

<div class="definition-list" markdown>

* **`comments`{ #comments .toc-code }** `string`{ .toc-def } `optional`{ .toc-opt }

    Comments related to the set.

* **`container`{ #container .toc-code }** `string`{ .toc-def } `optional`{ .toc-opt }

    The container that the DAT application should use for the file set. Must be one of the
    following values:

    * `auto`: Store the files in whatever container the user chooses in the DAT
      application. For example, a ZIP file, a 7Z file, a folder, or no container. The base
      file name of the container matches the title [`name`](titles.md#name).

    * `folder`: Store the files in a folder named after the title
      [`name`](titles.md#name).

    * `null`: Don't store the files in any container. Useful for keeping files by
      themselves, or for treating archives as files.

    {# * `archive`: Store the files in a specific archive type, named after the
      title [`name`](titles.md#name). #}

    If this property isn't present, the DAT application assumes the value is `auto`.

    /// details | Expand for developer details
    A `container` at the `sets` level with an `auto` value likely has a different behavior
    depending on whether or not it applies to a [`files`](sets.md#files) or
    [`fileset`](sets.md#fileset) array.

    For example, when dealing with a `files` array, `auto` might correlate with a `null`
    value, meaning you get raw files. When dealing with a `fileset` array, `auto` might
    correlate with a folder. This means the following scenario can be supported, where
    multidisc titles are put in a subfolder, but single disc titles are kept in a root
    folder:

    ```json
    ● [folder] Root folder
        ├ [file] Some Video Game (USA).iso
        ├ [file] Some Video Game, Other (Japan).iso
        ├ [folder] Some Video Game, The Sequel (USA)
        │   ├ [file] Some Video Game, The Sequel (USA) (Disc 1).iso
        │   └ [file] Some Video Game, The Sequel (USA) (Disc 2).iso
        └ [file] Yet Another Video game (USA).iso
    ```
    ///

* **`id`{ #id .toc-code }** `string`{ .toc-def } `optional`{ .toc-opt }

    A globally unique ID for the set item. Usually a database ID to ease lookups for DAT
    file maintainers.

* **`name`{ #name .toc-code }** `string`{ .toc-def } `optional`{ .toc-opt }

    The name of the set. Only required if there is more than one set.

    Can be any non-empty string, although generally you should use lowercase container
    format names. For example:

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

* **`retroachievements`{ #retroachievements .toc-code }** `boolean`{ .toc-def } `optional`{ .toc-opt }

    Whether or not retroachievements are supported on the title.

    If this property isn't present, the DAT application assumes the value is `false`.

</div>
