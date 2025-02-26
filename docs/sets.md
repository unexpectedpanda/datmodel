---
hide:
  - footer
---

# `sets`

The `sets` array contains objects (known as _sets_) that represent different file sets
within a [`release`](#releases.md). The example that follows is a simple one, however the
`sets` array can get much more complex to support extended use cases.

``` {.json .copy}
"sets": [
  {
    "name": "bin",
    "set": [
      {
        "container": "auto",
        "files": [
          {
            "name": "Some Video Game (USA) (Track 1).bin",
            "size": 10000,
            "digests": {
                "crc32": "29edd0e3",
                "xxh3_128": "1a2bf3bb0a4cd3aa94bf08b1c269423e",
                "blake3": "c32da642c108dd42bc169dbe4094b96d4f638d2c7388fb18132429347955c7ec"
            }
          },
          {
            "name": "Some Video Game (USA) (Track 2).bin",
            "size": 1000,
            "digests": {
                "crc32": "872f5343",
                "xxh3_128": "b993a0619f896a101e786850967b3d90",
                "blake3": "74277af46089c2b15aea5b193bdecdd58a2992e47b00956c678a6c070225cb18"
            }
          },
          {
            "name": "Some Video Game (USA).cue",
            "size": 100,
            "digests": {
                "crc32": "987150b7",
                "xxh3_128": "b7bb3254808cfc06d899854a1b58bab0",
                "blake3": "fcbc02c56a9a5157255febeac2009a988ccd08863ff648d290fe973dffe7f88c"
            }
          }
        ]
      }
    ]
  }
]
```

There must be a minimum of one set in the `sets` array. If there is more than one set,
then applications that process DAT files should let the user choose which set or sets they
want to keep, and let them assign different output paths per set.

This means a single DAT file can cover multiple formats &mdash; for example, a CD image in
ISO, CHD, _and_ RVZ formats. Or a ROM in encrypted _and_ decrypted formats. A user can
keep one fileset or many, routing the output to multiple different paths if they want.

## Definitions

<div class="definition-list" markdown>
* **`name`{ #name .toc-code }** `string`{ .toc-def } `required`{ .toc-req }

    The name of the set.

    The following values should be used where possible. However, you can use any value
    here &mdash; it's up to the application processing the DAT as to how it interprets it.

    * `archive`
    * `bin`
    * `chd`
    * `ciso`
    * `cso`
    * `cso2`
    * `decrypted`
    * `encrypted`
    * `files`
    * `gdi`
    * `iso`
    * `rvz`
    * `wbfs`
    * `wud`
    * `wux`
    * `xiso`
    * `zso`


* **`set`{ #build .toc-code }** `enum`{ .toc-def } `required`{ .toc-req }

</div>