---
hide:
  - footer
---

# Dense format

The following example represents a more dense way of presenting the DAT file JSON. Mostly
it collapses select objects to move the data horizontally.

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
          "regions": ["JP"],
          "languages": {"audio": ["en", "ja"], "interface": ["ja"], "subtitles": ["en"]},
          "type": "Game",
          "sets": [
            {
              "files": [
                {"name" : "file.asd", "size": 123, "digests": {"blake3": "c32da642c108dd42bc169dbe4094b96d4f638d2c7388fb18132429347955c7ec"}}
              ]
            }
          ]
        },
        {
          "name": "Some Video Game (USA)",
          "regions": ["US"],
          "languages": {"audio": ["en"], "interface": ["en"], "subtitles": ["en"]},
          "type": "Game",
          "sets": [
            {
              "files": [
                {"name" : "file.asd", "size": 98, "digests": { "blake3": "d6a38bd711fbfd1065c2f7907c631590ac56249613972199a19713d7c6f10b4d"}}
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
          "regions": ["US"],
          "languages": {"audio": ["en"], "interface": ["en"], "subtitles": ["en"]},
          "type": "Game",
          "sets": [
            {
              "files": [
                {"name" : "file.asd", "size": 456, "digests": {"blake3": "9261749c950815ea3657f11b60c1388f5e021297c25de546001a632bdfad441d"}}
              ]
            }
          ]
        }
      ]
    }
  ]
}
```