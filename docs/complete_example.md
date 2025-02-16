---
hide:
  - footer
---

# Complete DAT file example

The following example represents a complete, valid DAT file.

It doesn't include all available keys or demonstrate all valid values. For that, see the
DAT file structures section.

```json
{
  "dat_info": {
    "schema": "https://www.github.com/unexpectedpanda/datmodel",
    "name": "Company - Console",
    "source": "Release group",
    "source_url": "https://www.example.com",
    "version": "1.1.1",
    "date": "2025-12-30 13:23:54",
    "contributors": ["Contributor 1", "Contributor 2", "Contributor 3"]
  },
  "collection": [
    {
      "group": "Some Video Game",
      "releases": [
        {
          "name": "Some Video Game (Japan)",
          "build": "Production",
          "is_demo": false,
          "regions": ["Japan"],
          "languages": {
            "audio": ["Ja", "En"],
            "subtitles": ["En"]
          },
          "type": "Game",
          "release_date": "1993-10-12",
          "sets": {
            "files": [
              {
                "container": "auto",
                "files": [
                  {
                    "name" : "file.asd",
                    "size": 98,
                    "digests": {
                      "xxh3_128": "1a2bf3bb0a4cd3aa94bf08b1c269423e",
                      "blake3": "c32da642c108dd42bc169dbe4094b96d4f638d2c7388fb18132429347955c7ec"
                    }
                  }
                ]
              }
            ]
          }
        }
      ]
    }
  ]
}
```
