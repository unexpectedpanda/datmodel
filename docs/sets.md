---
hide:
  - footer
---

# `sets`

The `sets` array contains objects that represent different file sets within a
[`release`](#releases.md). For example, you might have a file set which describes both the
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

<span style="color:red">There's a potential clash here with container names if someone
tries to create more than one file set in the same folder. This needs to be resolved.</span>

## Definitions

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

    Use a `null` value for raw files without a container:

    ``` {.json .copy}
    "container": null
    ```

* **`set`{ #set .toc-code }** `object array`{ .toc-def } `required`{ .toc-req }

    The file set contents. Must include the following keys:

    * `container` (string): The container that the application managing the DAT file should use for
      the file set. Must be one of the following values:

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

    * `files` (object array): The files in the set and their properties.
      [Read more about the `files` array](files.md).

</div>
