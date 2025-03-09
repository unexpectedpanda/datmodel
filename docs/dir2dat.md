---
hide:
  - footer
---

# DIR2DAT

You could generate a DIR2DAT in groups with the following folder structure:

```json
● DAT root folder
├ Some Video Game // (1)!
│ ├ Some Video Game (Japan).zip // (2)!
│ └ Some Video Game (USA).zip
└ Some Video Game, Other
  └ Some Video Game, Other (USA).zip
```

1.  Top level folder names get populated as the `group`.
2.  This can be an archive of the title, or a folder containing files.

This would produce the following output:

```json
{
  "datInfo": {
    "schema": "https://www.github.com/unexpectedpanda/datmodel",
    "name": "Company - Console",
    "source": "Release group",
    "date": "2025-12-30 13:30:47"
  },
  "collection": [
    {
      "group": "Some Video Game",
      "titles": [
        {
          "name": "Some Video Game (Japan)",
          "regions": [],
          "languages": {
            "audio": [],
            "interface": [],
            "subtitles": []
          },
          "type": "Game",
          "sets": [
            {
              "set": [
                {
                  "files": [
                    {
                      "name" : "file.asd",
                      "size": 123,
                      "digests": {
                        "blake3": "c32da642c108dd42bc169dbe4094b96d4f638d2c7388fb18132429347955c7ec"
                      }
                    }
                  ]
                }
              ]
            }
          ]
        },
        {
          "name": "Some Video Game (USA)",
          "regions": [],
          "languages": {
            "audio": [],
            "interface": [],
            "subtitles": []
          },
          "type": "Game",
          "sets": [
            {
              "set": [
                {
                  "files": [
                    {
                      "name" : "file.asd",
                      "size": 98,
                      "digests": {
                        "blake3": "d6a38bd711fbfd1065c2f7907c631590ac56249613972199a19713d7c6f10b4d"
                      }
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "group": "Some Video Game, Other",
      "titles": [
        {
          "name": "Some Video Game, Other (USA)",
          "regions": [],
          "languages": {
            "audio": [],
            "interface": [],
            "subtitles": []
          },
          "type": "Game",
          "sets": [
            {
              "set": [
                {
                  "files": [
                    {
                      "name" : "file.asd",
                      "size": 456,
                      "digests": {
                        "blake3": "9261749c950815ea3657f11b60c1388f5e021297c25de546001a632bdfad441d"
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

Alternatively, you could pass a `--nogroups` flag to the DIR2DAT program, and use the
following folder structure to not use groups at all:

```txt
● DAT root folder
├ Some Video Game (Japan).zip
├ Some Video Game (USA).zip
└ Some Video Game, Other (USA).zip
```

This results in the following DAT file:

```json
{
  "datInfo": {
    "schema": "https://www.github.com/unexpectedpanda/datmodel",
    "name": "Company - Console",
    "source": "Release group",
    "date": "2025-12-30 13:30:47"
  },
  "collection": [
    {
      "group": "dir2dat",
      "titles": [
        {
          "name": "Some Video Game (Japan)",
          "regions": [],
          "languages": {
            "audio": [],
            "interface": [],
            "subtitles": []
          },
          "type": "Game",
          "sets": [
            {
              "set": [
                {
                  "files": [
                    {
                      "name" : "file.asd",
                      "size": 123,
                      "digests": {
                        "blake3": "c32da642c108dd42bc169dbe4094b96d4f638d2c7388fb18132429347955c7ec"
                      }
                    }
                  ]
                }
              ]
            }
          ]
        },
        {
          "name": "Some Video Game (USA)",
          "regions": [],
          "languages": {
            "audio": [],
            "interface": [],
            "subtitles": []
          },
          "type": "Game",
          "sets": [
            {
              "set": [
                {
                  "files": [
                    {
                      "name" : "file.asd",
                      "size": 98,
                      "digests": {
                        "blake3": "d6a38bd711fbfd1065c2f7907c631590ac56249613972199a19713d7c6f10b4d"
                      }
                    }
                  ]
                }
              ]
            }
          ]
        },
        {
          "name": "Some Video Game, Other (USA)",
          "regions": [],
          "languages": {
            "audio": [],
            "interface": [],
            "subtitles": []
          },
          "type": "Game",
          "sets": [
            {
              "set": [
                {
                  "files": [
                    {
                      "name" : "file.asd",
                      "size": 456,
                      "digests": {
                        "blake3": "9261749c950815ea3657f11b60c1388f5e021297c25de546001a632bdfad441d"
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
