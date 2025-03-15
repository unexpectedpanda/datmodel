---
hide:
  - footer
---

# Basic example

The following example represents a valid DAT file, with only the mandatory parameters
supplied.

It doesn't include all available keys or demonstrate all valid values. For that, see the
DAT file structures section.

```json
{
  "datInfo": {
    "schema": "https://www.github.com/unexpectedpanda/datmodel",
    "name": "Company - Console",
    "source": "Release group",
    "date": "2025-12-30"
  },
  "collection": [
    {
      "group": "Some Video Game",
      "titles": [
        {
          "name": "Some Video Game (Japan)",
          "regions": ["JP"],
          "languages": {
            "audio": ["ja", "en"],
            "interface": ["ja", "en"],
            "subtitles": ["en"]
          },
          "type": "Game",
          "sets": [
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
        },
        {
          "name": "Some Video Game (USA)",
          "regions": ["US"],
          "languages": {
            "audio": ["en"],
            "interface": ["en"],
            "subtitles": ["en"]
          },
          "type": "Game",
          "sets": [
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
}
```
