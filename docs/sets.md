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

``` {.json .copy hl_lines="4-8"}
"sets": [
  {
    "name": "bin",
    "set": [
      {
        ...
      }
    ]
  },
  {
    "name": "chd",
    "set": [
      {
        ...
      }
    ]
  }
]
```

There must be a minimum of one file set in the `sets` array. If there is more than one
file set, then DAT managers should let the user choose which file set or file sets they
want to keep based on the [`name`](#name), and let them assign different output paths per
file set.

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

* **`set`{ #set .toc-code }** `object array`{ .toc-def } `required`{ .toc-req }

    Describes an individual file set. [Read more about the `set` array](set.md).

</div>

## Optional properties

<div class="definition-list" markdown>

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

</div>
