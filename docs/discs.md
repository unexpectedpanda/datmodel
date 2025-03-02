---
hide:
  - footer
---

# Multiple discs in a single set

The examples on this page show how to handle bundling together discs into a single set
within a release. This is so DAT managers know to keep these files together when
filtering.

## Bundle discs together

The following example demonstrates how to keep together multiple discs in a single
release.

``` {.json .copy}
{
  "dat_info": {
    "schema": "https://www.github.com/unexpectedpanda/datmodel",
    "name": "Multiple discs",
    "source": "Data model 2025",
    "date": "2025-12-30 13:23:54"
  },
  "collection": [
    {
      "group": "Some Video Game",
      "releases": [
        {
          "name": "Some Video Game (USA)",
          "build": "Production",
          "published": true,
          "type": "Game",
          "release_date": "1993-10-12",
          "regions": ["US"],
          "languages": {
            "audio": [null],
            "interface": ["en"],
            "subtitles": [null]
          },
          "sets": [
            {
              "name": "bin",
              "set": [
                {
                  "container_name": "Some Video Game (USA) (Disc 1)",
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
                  "container_name": "Some Video Game (USA) (Disc 2)",
                  "container": "auto",
                  "files": [
                    {
                      "name": "Some Video Game (USA) (Disc 2) (Track 1).bin",
                      "size": 10000,
                      "digests": {
                        "crc32": "150cc86c",
                        "xxh3_128": "562ab7b9c5d8c3697d0b7641f389e946",
                        "blake3": "aa70c31c05bd6a4c5200599b2ee211005f5ce5fe67a3d1ac14e1f7f02bb8553a"
                      }
                    },
                    {
                      "name": "Some Video Game (USA) (Disc 2) (Track 2).bin",
                      "size": 1000,
                      "digests": {
                        "crc32": "da785795",
                        "xxh3_128": "301fc055404b959b28c3d197eba6b1bb",
                        "blake3": "37987e3bafd8e0a1f1436d2f9c25b2e79cf0337f7f0ce8b3f6c85c37dd5fa6ad"
                      }
                    },
                    {
                      "name": "Some Video Game (USA) (Disc 2).cue",
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
        }
      ]
    }
  ]
}
```

## Reference discs in other sets

The following example shows how to reference a disc that is shared between sets in a release.

``` {.json .copy}
{
  "dat_info": {
    "schema": "https://www.github.com/unexpectedpanda/datmodel",
    "name": "Multiple discs",
    "source": "Data model 2025",
    "date": "2025-12-30 13:23:54"
  },
  "collection": [
    {
      "group": "Some Video Game",
      "releases": [
        {
          "name": "Some Video Game (USA)",
          "build": "Production",
          "published": true,
          "type": "Game",
          "release_date": "1993-10-12",
          "regions": ["US"],
          "languages": {
            "audio": [null],
            "interface": ["en"],
            "subtitles": [null]
          },
          "sets": [
            {
              "name": "bin",
              "set": [
                {
                  "container_name": "Some Video Game (USA) (Disc 1)",
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
                  "container_name": "Some Video Game (USA, Europe) (Disc 2)",
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
          "build": "Production",
          "published": true,
          "type": "Game",
          "release_date": "1993-10-12",
          "regions": ["EUR"],
          "languages": {
            "audio": [null],
            "interface": ["en"],
            "subtitles": [null]
          },
          "sets": [
            {
              "name": "bin",
              "set": [
                {
                  "container_name": "Some Video Game (Europe) (Disc 1)",
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
                  "container_name": "Some Video Game (USA, Europe) (Disc 2)",
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