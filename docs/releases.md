---
hide:
  - footer
---

# `releases`

The releases array is necessarily complex to enable new functionality. At its simplest, it
can seem quite straightforward:

```json
"releases": [
  {
    "name": "Some Video Game (Japan)",
    "build": "Production",
    "is_demo": false,
    "published": true,
    "regions": ["Japan"],
    "languages": {
      "audio": ["Ja", "En"],
      "interface": [["En"]],
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
```

* **`name`** (string): _Required_. The name of the title, in UTF-8. This is used for the
  name of the archive or folder. Names can't end with a period or space, or use the
  following invalid characters:

    ```
    :<>"|?*
    ```

    These invalid characters are found with the following regular expression:

    ```
    ^[^:<>\"|?*].*[^. :<>\"|?*]$
    ```

    Non-UTF-8 characters are found with the following regular expressions:

    ```
    [\xC0-\xC1]
    [\xF5-\xFF]
    \xE0[\x80-\x9F]
    \xF0[\x80-\x8F]
    [\xC2-\xDF](?![\x80-\xBF])
    [\xE0-\xEF](?![\x80-\xBF]{2})
    [\xF0-\xF4](?![\x80-\xBF]{3})
    (?<=[\x00-\x7F\xF5-\xFF])[\x80-\xBF]
    (?<![\xC2-\xDF]|[\xE0-\xEF]|[\xE0-\xEF][\x80-\xBF]|[\xF0-\xF4]|[\xF0-\xF4][\x80-\xBF]|[\xF0-\xF4][\x80-\xBF]{2})[\x80-\xBF]
    (?<=[\xE0-\xEF])[\x80-\xBF](?![\x80-\xBF])
    (?<=[\xF0-\xF4])[\x80-\xBF](?![\x80-\xBF]{2})
    (?<=[\xF0-\xF4][\x80-\xBF])[\x80-\xBF](?![\x80-\xBF])
    ```

* **`build`** (enum): _Required_. When in the
  [software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
  the title was released. Must be one of the following values, in order of maturity
  and specificity:

    * `Production`: What reaches store shelves or internet distribution systems. This
      includes release to manufacturing (RTM) releases.

    * `Release candidate`: There are often multiple release candidates, of which one is
      chosen to go to production. Release candidates are feature complete, and only
      significant bugs force another release candidate to be issued.

    * `Beta`: A largely feature-complete version of a title, that still has bugs and
      performance issues to squash.

    * `Alpha`: An in-development version of a title that isn't feature complete, and isn't
      thoroughly tested. Likely to be highly buggy.

    * `Pre-alpha`: This includes early development releases and prototypes.

    * `Review`: A version of the title sent to reviewers. This can be production code,
      preproduction code, or have code in it that's unique to the reviewer copy.

    * `Preproduction`: A generic catch-all for a title that is at an unspecified
      development stage, but isn't the production version. Wherever possible, don't use
      this.

* **`is_demo`** (bool): _Required_: Whether the title is a demo.

* **`regions`** (enum array): _Required_: Which regions the title was released in. Must be
  one or more of the following regions:

    /// tab | Region groups
    These regional groups are largely cultural or geopolitical in nature. Be aware that
    individual regions might belong to multiple groups.

    * `Global`: Wherever on Earth it was made available, this version of the release was
      used.

    * `Africa`: This title was released in three or more African countries.

    * `Asia`: This title was released in three or more Asian countries.

    * `Europe`: This title was released in three or more European countries.

    * `Latin America`: This title was released in three or more Latin American countries.

    * `Middle East`: This title was released in three or more Middle-Eastern countries.

    * `Nordics`: This title was released in three or more Nordic countries.

    * `Oceania`: This title was released in three or more Oceanic countries.
    ///

    /// tab | Individual regions
    This list does not include all individual countries or regions in the world. It is
    based off known releases available in the Redump and No-Intro databases. New regions
    are added as new releases are indexed from those regions.

    <div class="grid" markdown>

    <div>

    * `Albania`

    * `Argentina`

    * `Asia`

    * `Australia`

    * `Austria`

    * `Belgium`

    * `Brazil`

    * `Bulgaria`

    * `Canada`

    * `China`

    * `Croatia`

    * `Czechia`

    * `Denmark`

    * `Estonia`

    * `Finland`

    * `France`

    * `Germany`

    * `Greece`

    * `Hong Kong`

    * `Hungary`

    * `Iceland`

    * `India`

    * `Indonesia`

    * `Ireland`

    * `Israel`

    * `Italy`

    * `Japan`

    </div>
    <div>

    * `Korea`

    * `Latvia`

    * `Lithuania`

    * `Macedonia`

    * `Mexico`

    * `Netherlands`

    * `New Zealand`

    * `Norway`

    * `Poland`

    * `Portugal`

    * `Romania`

    * `Russia`

    * `Serbia`

    * `Singapore`

    * `Slovakia`

    * `Slovenia`

    * `South Africa`

    * `Spain`

    * `Sweden`

    * `Switzerland`

    * `Taiwan`

    * `Thailand`

    * `Turkey`

    * `United Kingdom`

    * `Ukraine`

    * `United Arab Emirates`

    * `USA`

    </div>
    </div>
    ///

    If you don't know where a region is from, use `Unknown` as the only item in the array.

    /// note | Retiring regions
    `Global` succeeds the less-specific `World` region used by datting groups, which
    depending on the naming standard either encompassed any title released in three or
    more regions, or spanned USA, Europe, and Japan.

    `Nordics` succeeds the more restrictive `Scandinavian`, as it includes more countries.
    ///

---

* **`size`** (integer): _Required_. The size of the file, in bytes.

* **`digests`** (string): _Required_. This object contains the digests of different hash functions. It must have at
  least one digest. The following hash functions are accepted:

    * **`crc32`** (string):

### Interpreting releases data

Observe the following rules in the releases array:

* Unless otherwise specified, empty values are permitted for keys. This means that the
  property exists for the release, but the value is _unknown_.

* Omitted optional keys means the the property is _irrelevant_ to the release.

* To indicate that a title doesn't support a property, use `null` as the value.

For example, the following code sample describes a title where the audio and subtitle
languages aren't known:

```json
"languages": {
  "audio": [],
  "subtitles": []
}
```

In the following code sample, it's known that there are no audio languages and no
subtitles:

```json
"languages": {
  "audio": [null],
  "subtitles": [null]
}
```

---

At its most complex with all the optional data though, it can seem daunting:

```json
"releases": [
  {
    "name": "Some Video Game (Japan)",
    "db_id": "123456789",
    "build": "Production",
    "is_demo": false,
    "serial": null,
    "source": ["3.5\" floppy"],
    "local_names": {
      "japanese": "別のビデオゲーム"
    },
    "regions": ["Japan"],
    "languages": {
      "audio": ["Ja", "En"],
      "subtitles": ["En"]
    },
    "developer": "Some Developer",
    "publisher": "Some Publisher",
    "type": "Game",
    "genre": "",
    "release_date": "1993-10-12",
    "inputs": ["Keyboard", "Mouse"],
    "sets": {
      "chd": [
        {
          "container": null,
          "files": [
            {
              "name": "file.chd",
              "size": 45,
              "digests": {
                "crc32": "3b5bd0a9",
                "md5": "76aab21e473b127684e1ad06208ba168",
                "sha1": "a413ce3fedd2e0755acd3a82362bac32893df47f",
                "sha256": "a9cf7f0b767bc07e6c652bbdd5dd5763a1bfb7ba444aa08ffcc95e45fcec8e7f",
                "xxh3_128": "79b5665946dae6fbb9fee66b2ba2417a",
                "blake3": "0694036dbd769e2861c9ce504acc000aa57ff3da757d72671466fb8cbac62ead"
              },
              "date_created": "2024-03-05 17:53:22.395706",
              "date_modified": "2024-02-08 09:07:35.636984",
              "win_attributes": "a",
              "nix_attributes": "rw-rw-rw-"
            }
          ]
        },
      ],
      "files": [
        {
          "container": "auto",
          "files": [
            {
              "name" : "file.asd",
              "size": 98,
              "digests": {
                "crc32": "29edd0e3",
                "md5": "cb26b7c023fe00ea12dcc49202f67eb0",
                "sha1": "cef9b8c7205552d0d259ac02839707ba03fa1aff",
                "sha256": "46a6e399b1fb2dc6050f7c9f775d9ccee1101a7b46657ff3d992ec5f2900dee1",
                "xxh3_128": "1a2bf3bb0a4cd3aa94bf08b1c269423e",
                "blake3": "c32da642c108dd42bc169dbe4094b96d4f638d2c7388fb18132429347955c7ec"
              },
              "date_created": "2024-03-05 17:53:22.395706",
              "date_modified": "2024-02-08 09:07:35.636984",
              "win_attributes": "a",
              "nix_attributes": "rw-rw-rw-"
            }
          ]
        }
      ]
    },
    "updates": [
      {
        "name": "Some Video Game - Update 5 (Japan)",
        "requires": ["Some Video Game - Update 4 (Japan)"]
      },
      {
        "name": "Some Video Game - Update 4 (Japan)"
      }
    ],
    "addons": [
      {...}
    ]
  },
  {
    "name": "Some Video Game (Europe)",
    "db_id": "987654321",
    ...
  },
  {
    "name": "Some Video Game (USA)",
    "db_id": "123459876",
    ...
  }
]
```

## Full DAT file example

```json
{
  "dat_info": {
    "name": "Sony - Playstation",
    "source": "Redump",
    "source_url": "http://www.redump.org",
    "version": "1.1.1",
    "date": "2025-12-30 13:23:54",
    "contributors": ["Contributor 1", "Contributor 2", "Contributor 3"]
  },
  "collection": [
    {
      "group": "Doom",
      "releases": [
        {
          "name": "Doom (USA)",
          "db_id": "123456789",
          "build": "Production",
          "source": ["3.5\" floppy"],
          "local_names": {},
          "regions": ["USA"],
          "languages": {
            "audio": [],
            "subtitles": ["En"]
          },
          "developer": "iD Software",
          "publisher": "GT Interactive",
          "type": "Game",
          "genre": "",
          "release_date": "1993-10-12",
          "inputs": ["Keyboard"],
          "container": "Auto",
          "files": [
            {...}
          ],
          "updates": [
            {...}
          ],
          "addons": [
            {...}
          ]
        },
        {
          "name": "Doom (Europe)",
          "db_id": "987654321",
          ...
        },
        {
          "name": "Doom (Japan)",
          "db_id": "123459876",
          ...
        }
      ]
    }
  ]
}
```