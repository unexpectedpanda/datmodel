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
      "interface": ["En"],
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

## Definitions

<div class="definition-list" markdown>
* **`name`{:#name .toc-code}** `string`{:.toc-def} `required`{:.toc-req}

    The name of the title, in UTF-8. This is used for the name of the archive or folder.
    Names can't end with a period or space, or use the following invalid characters:

    ``` {.text .copy}
    :<>"|?*
    ```

    /// details | Expand for developer details
    Invalid path characters are found with the following regular expression:

    ``` {.text .copy}
    ^[^:<>\"|?*].*[^. :<>\"|?*]$
    ```

    Non-UTF-8 characters are found with the following regular expressions:

    ``` {.text .copy}
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
    ///

* **`build`{:#build .toc-code}** `enum`{:.toc-def} `required`{:.toc-req}

    When in the
    [software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
    the title was released. Must be one of the following values, in order of maturity and
    specificity:

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

* **`is_demo`{:#is_demo .toc-code}** `bool`{:.toc-def} `required`{:.toc-req}

    Whether the title is a demo.

* **`was_published`{:#was_published .toc-code}** `bool`{:.toc-def} `required`{:.toc-req}

    Whether the title was published. Unreleased titles should be set to `false`.

* **`regions`{:#regions .toc-code}** `enum array`{:.toc-def} `required`{:.toc-req}

    Which regions the title was released in. This is not intended to match the regional
    naming standards of DAT groups, as these differ. File names can remain unaltered to
    follow those regional naming standards.

    If you don't know where a release is from, use `Unknown` as the only item in the
    array.

    If you do know where the release is from, prefer listing individual regions where
    possible for better granularity.

    For grouped regions, keep the following rules in mind:

    * Only use grouped regions by themselves when a title is clearly intended for release
      in that broad area. For example, titles have often been released for `Europe` due to
      the PAL video standard, another form of region locking, or because of the
      [level of English comprehension of the continent](https://europa.eu/eurobarometer/surveys/detail/2979).
      Digitally-distributed titles often have only one `Global` version.

    * When using grouped regions, be aware that each can contain several individual
      regions that have vastly different languages, even _within_ those individual
      regions. It's not good enough to have a grouped region listed without its languages
      &mdash; just `Asia` by itself tells us nothing about who the target audience is. Be
      extra diligent in adding all the supported languages for the title, even if this
      means testing to find out.

    * If you have more than two individual regions listed that belong to a grouped region,
      also add that grouped region. For example: `["France", "Germany", "Europe"]`. Just
      be aware that individual regions can be part of multiple grouped regions. For
      example, Türkiye is a melting pot of cultures at the intersection of Asia, Europe,
      and the Middle East. Mexico is part of North America, but also Latin America.

    The valid regions are as follows:

    /// tab | Individual regions

    * `Afghanistan`

    * `Albania`

    * `Algeria`

    * `American Samoa`

    * `Andorra`

    * `Angola`

    * `Anguilla`

    * `Antigua and Barbuda`

    * `Argentina`

    * `Armenia`

    * `Aruba`

    * `Australia`

    * `Austria`

    * `Azerbaijan`

    * `Bahamas`

    * `Bahrain`

    * `Bangladesh`

    * `Barbados`

    * `Belarus`

    * `Belgium`

    * `Belize`

    * `Benin`

    * `Bermuda`

    * `Bhutan`

    * `Bolivia`

    * `Bosnia and Herzegovina`

    * `Botswana`

    * `Brazil`

    * `British Virgin Islands`

    * `Brunei`

    * `Bulgaria`

    * `Burkina Faso`

    * `Burundi`

    * `Cabo Verde`

    * `Cambodia`

    * `Cameroon`

    * `Canada`

    * `Caribbean Netherlands`

    * `Cayman Islands`

    * `Central African Republic`

    * `Chad`

    * `Chil`

    * `China`

    * `Colombia`

    * `Comoros`

    * `Congo`

    * `Cook Islands`

    * `Costa Rica`

    * `Croatia`

    * `Cuba`

    * `Curaçao`

    * `Cyprus`

    * `Czechia`

    * `Côte d'Ivoire`

    * `Denmark`

    * `Djibouti`

    * `Dominica`

    * `Dominican Republic`

    * `DR Congo`

    * `Ecuador`

    * `Egypt`

    * `El Salvador`

    * `Equatorial Guinea`

    * `Eritrea`

    * `Estonia`

    * `Eswatini`

    * `Ethiopia`

    * `Faeroe Islands`

    * `Falkland Islands`

    * `Fiji`

    * `Finland`

    * `France`

    * `French Guiana`

    * `French Polynesia`

    * `Gabon`

    * `Gambia`

    * `Georgia`

    * `Germany`

    * `Ghana`

    * `Gibraltar`

    * `Greece`

    * `Greenland`

    * `Grenada`

    * `Guadeloupe`

    * `Guam`

    * `Guatemala`

    * `Guinea`

    * `Guinea-Bissau`

    * `Guyana`

    * `Haiti`

    * `Holy-See`

    * `Honduras`

    * `Hong Kong`

    * `Hungary`

    * `Iceland`

    * `India`

    * `Indonesia`

    * `Iran`

    * `Iraq`

    * `Ireland`

    * `Isle of Man`

    * `Israel`

    * `Italy`

    * `Jamaica`

    * `Japan`

    * `Jordan`

    * `Kazakhstan`

    * `Kenya`

    * `Kiribati`

    * `Kuwait`

    * `Kyrgyzstan`

    * `Laos`

    * `Latvia`

    * `Lebanon`

    * `Lesotho`

    * `Liberia`

    * `Libya`

    * `Liechtenstein`

    * `Lithuania`

    * `Luxembourg`

    * `Macao`

    * `Madagascar`

    * `Malawai`

    * `Malaysia`

    * `Maldives`

    * `Mali`

    * `Malta`

    * `Marshall Islands`

    * `Martinique`

    * `Mauritania`

    * `Mauritius`

    * `Macedonia`

    * `Mayotte`

    * `Mexico`

    * `Micronesia`

    * `Moldova`

    * `Monaco`

    * `Mongolia`

    * `Montenegro`

    * `Montserrat`

    * `Morocco`

    * `Mozambique`

    * `Myanmar`

    * `Namibia`

    * `Nauru`

    * `Nepal`

    * `Netherlands`

    * `New Caledonia`

    * `New Zealand`

    * `Nicaragua`

    * `Niue`

    * `Niger`

    * `Nigeria`

    * `North Korea`

    * `North Macedonia`

    * `Northern Mariana Islands`

    * `Norway`

    * `Oman`

    * `Pakistan`

    * `Palau`

    * `Panama`

    * `Papua New Guinea`

    * `Paraguay`

    * `Peru`

    * `Philippines`

    * `Poland`

    * `Portugal`

    * `Puerto Rico`

    * `Qatar`

    * `Réunion`

    * `Romania`

    * `Russia`

    * `Rwanda`

    * `Saint Barthelemy`

    * `Saint Helena`

    * `Saint Kitts & Nevis`

    * `Saint Lucia`

    * `Saint Pierre & Miquelon`

    * `Samoa`

    * `San Marino`

    * `Sao Tome & Principe`

    * `Saudi Arabia`

    * `Senegal`

    * `Serbia`

    * `Seychelles`

    * `Sierra Leone`

    * `Singapore`

    * `Sint Maarten`

    * `Slovakia`

    * `Slovenia`

    * `Solomon Islands`

    * `South Africa`

    * `South Korea`

    * `South Sudan`

    * `Spain`

    * `Sri Lanka`

    * `St. Vincent & Grenadines`

    * `State of Palestine`

    * `Sudan`

    * `Suriname`

    * `Sweden`

    * `Switzerland`

    * `Syria`

    * `Taiwan`

    * `Tajikstan`

    * `Tanzania`

    * `Thailand`

    * `Timor-Lest`

    * `Togo`

    * `Tokelau`

    * `Tonga`

    * `Trinidad and Tobag`

    * `Tunisia`

    * `Türkiye`

    * `Turks and Caicos`

    * `Turkmenistan`

    * `Tuvalu`

    * `U.S. Virgin Islands`

    * `Uganda`

    * `Ukraine`

    * `United Arab Emirates`

    * `United Kingdom`

    * `United State`

    * `Unknown`

    * `Uruguay`

    * `Uzbekistan`

    * `Vanuatu`

    * `Venezuela`

    * `Vietnam`

    * `Wallis & Futuna`

    * `Western Sahara`

    * `Yemen`

    * `Zambia`

    * `Zimbabwe`
    ///
    /// tab | Grouped regions
    * `Global`

    * `Africa`

    * `Asia`

    * `Europe`

    * `Latin America`

    * `Middle East`

    * `North America`

    * `Nordics`

    * `Oceania`

    * `South America`
    ///

    /// warning | Regions in graphical user interfaces
    These region codes are intended to keep the character count of the `regions` array,
    and therefore the file size, down. When building graphical user interfaces, opt to use
    full region names to keep it more accessible to users.
    ///

* **`languages`{:#languages .toc-code}** `object`{:.toc-def} `required`{:.toc-req}

    The supported languages for audio, the title's interface, and its subtitles.

    Languages are split up into `audio`, `interface`, and `subtitles` to handle odd
    language scenarios. For example, `Metal Gear Solid Integral (Japan)` on PlayStation
    has English audio, selectable English or Japanese subtitles, and a mix of English
    _and_ Japanese for the interface&mdash;where Japanese is used for weapon and item
    descriptions, and English for everything else. It's a weird mix, but it's definitely
    intended for Japanese audiences, so is represented as follows:

    ```json
    "languages": {
      "audio": ["En"],
      "interface": ["Ja"],
      "subtitles": ["En", "Ja"]
    }
    ```

    `Ghost in the Shell (France)` on PlayStation has cutscenes where the audio is in French,
    but the interface is in English, and there are no subtitles. This is represented as
    follows:

    ```json
    "languages": {
      "audio": ["Fr"],
      "interface": ["En"],
      "subtitles": [null]
    }
    ```

    If there are no audio, interface, or subtitle languages, add a singular `null` item to
    the relevant arrays.

    Certain combinations of language types tell us useful things. For example, a Japanese
    game with the following properties is completely playable by English speakers:

    ```json
    "languages": {
      "audio": [null],
      "interface": ["En"],
      "subtitles": [null]
    }
    ```

    Valid language codes are listed in the
    [IANA language subtag registry](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry).
    You can search for a language subtag at
    [BCP47 language subtag lookup](https://r12a.github.io/app-subtags/).

    There are well over 9,000 valid languages, so for page performance they're not listed
    here. It's also not sensible to include them in the schema validation, so validation
    needs to be done by the code generating the DAT file.

    When choosing a language code, follow the guidelines laid out in the following pages:

    * [Language tags in HTML and XML](https://www.w3.org/International/articles/language-tags/)
    * [Choosing a language tag](https://www.w3.org/International/questions/qa-choosing-language-tags)
    * [Simplified vs. Traditional Chinese, and the Spoken Dialects](https://web.archive.org/web/20250216094012/https://localization.blog/2022/10/10/simplified-vs-traditional-chinese-and-the-spoken-dialects/) (Chinese language codes differ for spoken vs written)

    /// warning | Languages in graphical user interfaces
    These language codes are intended to keep the character count of the `languages`
    arrays, and therefore the file size, down. When building graphical user interfaces,
    opt to use full language names to keep it more accessible to users.
    ///
</div>


---

* **`size`** (integer): _Required_. The size of the file, in bytes.

* **`digests`** (string): _Required_. This object contains the digests of different hash functions. It must have at
  least one digest. The following hash functions are accepted:

    * **`crc32`** (string):

## Interpreting releases data

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