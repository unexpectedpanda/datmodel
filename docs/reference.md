---
hide:
  - footer
---

# Reference file sets in other titles

Sometimes there are file sets that are shared between titles. For example, you might have
the following set of discs that make up the USA variant of a title:

* `Some Video Game (USA) (Disc 1)`
* `Some Video Game (USA, Europe) (Disc 2)`

And the following set of discs that make up the Europe variant of a title:

* `Some Video Game (Europe) (Disc 1)`
* `Some Video Game (USA, Europe) (Disc 2)`

Where `Some Video Game (USA, Europe) (Disc 2)` is identical between the two variants. You
can link those two file sets together in a DAT file via a reference, and the DAT
application can choose the following behavior for those filesets:

* If the file set is stored in the same folder, ignore the reference, the file is already
  available.
* If the file set is stored in different folders:

    * Create a symbolic link to the reference file set.

    * Create a copy of the file.

The following example shows how to reference the files that are in another title. This
only links to a specific `files` array, it doesn't link to individual files.

``` {.json .copy}
{
  "datInfo": {
    "schema": "https://www.github.com/unexpectedpanda/datmodel",
    "name": "Multiple discs",
    "source": "Data model 2025",
    "date": "2025-12-30 13:23:54"
  },
  "collection": [
    {
      "group": "Some Video Game",
      "titles": [
        {
          "name": "Some Video Game (USA)",
          "type": "Game",
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
                  "container": "auto",
                  "files": [
                    {
                      "name": "Some Video Game (USA) (Disc 1) (Track 1).bin",
                      "size": 10000,
                      "digests": {
                        "crc32": "29edd0e3",
                        "xxh3_128": "1a2bf3bb0a4cd3aa94bf08b1c269423e",
                        "blake3": "c32da642c108dd42bc169dbe4094b96d4f638d2c7388fb18132429347955c7ec"
                      }
                    },
                    {
                      "name": "Some Video Game (USA) (Disc 1) (Track 2).bin",
                      "size": 1000,
                      "digests": {
                        "crc32": "872f5343",
                        "xxh3_128": "b993a0619f896a101e786850967b3d90",
                        "blake3": "74277af46089c2b15aea5b193bdecdd58a2992e47b00956c678a6c070225cb18"
                      }
                    },
                    {
                      "name": "Some Video Game (USA) (Disc 1).cue",
                      "size": 100,
                      "digests": {
                        "crc32": "987150b7",
                        "xxh3_128": "b7bb3254808cfc06d899854a1b58bab0",
                        "blake3": "fcbc02c56a9a5157255febeac2009a988ccd08863ff648d290fe973dffe7f88c"
                      }
                    }
                  ]
                },
                {
                  "name": "Some Video Game (USA, Europe) (Disc 2)",
                  "container": "auto",
                  "files": [
                    {
                      "name": "Some Video Game (USA, Europe) (Disc 2) (Track 1).bin",
                      "size": 10000,
                      "digests": {
                        "crc32": "150cc86c",
                        "xxh3_128": "562ab7b9c5d8c3697d0b7641f389e946",
                        "blake3": "aa70c31c05bd6a4c5200599b2ee211005f5ce5fe67a3d1ac14e1f7f02bb8553a"
                      }
                    },
                    {
                      "name": "Some Video Game (USA, Europe) (Disc 2) (Track 2).bin",
                      "size": 1000,
                      "digests": {
                        "crc32": "da785795",
                        "xxh3_128": "301fc055404b959b28c3d197eba6b1bb",
                        "blake3": "37987e3bafd8e0a1f1436d2f9c25b2e79cf0337f7f0ce8b3f6c85c37dd5fa6ad"
                      }
                    },
                    {
                      "name": "Some Video Game (USA, Europe) (Disc 2).cue",
                      "size": 100,
                      "digests": {
                        "crc32": "0a8850bc",
                        "xxh3_128": "8272cdb90bf9197105edec3ee8956844",
                        "blake3": "e685486d29de13f3215c969764b462b3f479e1873fab8f995fb083900fb58406"
                      }
                    }
                  ]
                }
              ]
            }
          ]
        },
        {
          "name": "Some Video Game (Europe)",
          "type": "Game",
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
                  "container": "auto",
                  "files": [
                    {
                      "name": "Some Video Game (Europe) (Disc 1) (Track 1).bin",
                      "size": 10000,
                      "digests": {
                        "crc32": "29edd0e3",
                        "xxh3_128": "1a2bf3bb0a4cd3aa94bf08b1c269423e",
                        "blake3": "c32da642c108dd42bc169dbe4094b96d4f638d2c7388fb18132429347955c7ec"
                      }
                    },
                    {
                      "name": "Some Video Game (Europe) (Disc 1) (Track 2).bin",
                      "size": 1000,
                      "digests": {
                        "crc32": "872f5343",
                        "xxh3_128": "b993a0619f896a101e786850967b3d90",
                        "blake3": "74277af46089c2b15aea5b193bdecdd58a2992e47b00956c678a6c070225cb18"
                      }
                    },
                    {
                      "name": "Some Video Game (Europe) (Disc 1).cue",
                      "size": 100,
                      "digests": {
                        "crc32": "987150b7",
                        "xxh3_128": "b7bb3254808cfc06d899854a1b58bab0",
                        "blake3": "fcbc02c56a9a5157255febeac2009a988ccd08863ff648d290fe973dffe7f88c"
                      }
                    }
                  ]
                },
                {
                  "name": "Some Video Game (USA, Europe) (Disc 2)",
                  "container": "auto",
                  "files": [
                    {
                      "$ref": "#/collection/Some Video Game/Some Video Game (USA)/Some Video Game (USA) (Disc 2) (Track 1).bin"
                    },
                    {
                      "$ref": "#/collection/Some Video Game/Some Video Game (USA)/Some Video Game (USA) (Disc 2) (Track 2).bin"
                    },
                    {
                      "$ref": "#/collection/Some Video Game/Some Video Game (USA)/Some Video Game (USA) (Disc 2).cue"
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