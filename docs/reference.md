---
hide:
  - footer
---

# Reference other file sets

Sometimes there are file sets that are shared between titles. For example, you might have
the following set of discs that make up the USA variant of a title:

* `Some Video Game (USA) (Disc 1)`
* `Some Video Game (USA, Europe) (Disc 2)`

And the following set of discs that make up the Europe variant of a title:

* `Some Video Game (Europe) (Disc 1)`
* `Some Video Game (USA, Europe) (Disc 2)`

Where `Some Video Game (USA, Europe) (Disc 2)` is identical between the two variants.

Instead of listing both entries, you can list the USA variant as the source, and then
_reference_ it inside the Europe variant. A DAT application can then treat the referenced
file set differently to the source to save disk space,
[depending on the situation and user preference](reference.md#file-storage-behavior).

The following example shows creating a reference using the `refId` property. The parts of
the code that represent the reference are highlighted.

``` {.json .copy hl_lines="39 71-85"}
{
  "datInfo": {
    "schema": "https://www.github.com/unexpectedpanda/datmodel",
    "name": "Reference ID example",
    "source": "Data model 2025",
    "date": "2025-12-30 13:23:54"
  },
  "collection": [
    {
      "group": "Some Video Game",
      "titles": [
        {
          "name": "Some Video Game (Europe)",
          "regions": ["EUR"],
          "languages": {
            "audio": [null],
            "interface": ["en"],
            "subtitles": [null]
          },
          "sets": [
            {
              "fileset": [
                {
                  "name": "Some Video Game (Europe) (Disc 1)",
                  "id": "123458",
                  "files": [
                    {
                      "name": "Some Video Game (Europe) (Disc 1).iso",
                      "size": 10000,
                      "digests": {
                        "crc32": "29edd0e3",
                        "xxh3_128": "1a2bf3bb0a4cd3aa94bf08b1c269423e",
                        "blake3": "c32da642c108dd42bc169dbe4094b96d4f638d2c7388fb18132429347955c7ec"
                      }
                    }
                  ]
                },
                {
                  "refId": "123457"
                }
              ]
            }
          ]
        },
        {
          "name": "Some Video Game (USA)",
          "regions": ["US"],
          "languages": {
            "audio": [null],
            "interface": ["en"],
            "subtitles": [null]
          },
          "sets": [
            {
              "fileset": [
                {
                  "name": "Some Video Game (USA) (Disc 1)",
                  "id": "123456",
                  "files": [
                    {
                      "name": "Some Video Game (USA) (Disc 1).iso",
                      "size": 10000,
                      "digests": {
                        "crc32": "29edd0e3",
                        "xxh3_128": "1a2bf3bb0a4cd3aa94bf08b1c269423e",
                        "blake3": "c32da642c108dd42bc169dbe4094b96d4f638d2c7388fb18132429347955c7ec"
                      }
                    }
                  ]
                },
                {
                  "name": "Some Video Game (USA, Europe) (Disc 2)",
                  "id": "123457",
                  "files": [
                    {
                      "name": "Some Video Game (USA, Europe) (Disc 2).iso",
                      "size": 10000,
                      "digests": {
                        "crc32": "150cc86c",
                        "xxh3_128": "562ab7b9c5d8c3697d0b7641f389e946",
                        "blake3": "aa70c31c05bd6a4c5200599b2ee211005f5ce5fe67a3d1ac14e1f7f02bb8553a"
                      }
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

In the previous example, a DAT application sees the `refId` to the unique global
identifier `123457`. It then scours the DAT file at the `sets` and `fileset` level for a
matching `id`, and imports any properties that aren't defined locally &mdash; in this case
`name`, `files`, and all the `files` subproperties. The `id` property is not imported.

Therefore the following code sample:

``` {.json .copy}
{
  "refId": "123457"
}
```

Is effectively interpreted as follows:

``` {.json .copy}
{
  "refId": "123457",
  "name": "Some Video Game (USA, Europe) (Disc 2)",
  "files": [
    {
      "name": "Some Video Game (USA, Europe) (Disc 2).iso",
      "size": 10000,
      "digests": {
        "crc32": "150cc86c",
        "xxh3_128": "562ab7b9c5d8c3697d0b7641f389e946",
        "blake3": "aa70c31c05bd6a4c5200599b2ee211005f5ce5fe67a3d1ac14e1f7f02bb8553a"
      }
    }
  ]
}
```

Properties that are defined locally are treated as overrides, and are preferenced over
imported properties. For example, the following code sample:

``` {.json .copy}
{
  "name": "Some Video Game (Europe) (Disc 2)",
  "refId": "123457"
}
```

Is effectively interpreted as follows:

``` {.json .copy}
{
  "refId": "123457",
  "name": "Some Video Game (Europe) (Disc 2)",
  "files": [
    {
      "name": "Some Video Game (USA, Europe) (Disc 2).iso",
      "size": 10000,
      "digests": {
        "crc32": "150cc86c",
        "xxh3_128": "562ab7b9c5d8c3697d0b7641f389e946",
        "blake3": "aa70c31c05bd6a4c5200599b2ee211005f5ce5fe67a3d1ac14e1f7f02bb8553a"
      }
    }
  ]
}
```

You can only reference an entire top-levl object in the `sets` or `fileset` arrays. This
means you can't reference individual files, or set a local `name` for individual files.

## File storage behavior

A DAT application can then choose the following behavior for referenced filesets, based on
situation and user preference:

* If the container is stored in the same destination folder and imports the `name`
  property, ignore the reference, the file is already available.

  * If the container is stored in a different destination folder than the original, do
  one of the following:

    * Create a symbolic link to the reference container.

    * Create a copy of the reference container.

* If the container sets a local `name` property, do one of the following:

    * Create a symbolic link to the reference container, but use the local `name`
      property as the file name.

    * Create a copy of the reference container, renaming it with the local `name`
      property.

The following example shows how to reference the files that are in another title. This
only links to a specific `files` array, it doesn't link to individual files.
