---
hide:
  - footer
---

# Schema

You can test validating against this schema with
[JSON Schema Lint](https://jsonschemalint.com/#!/version/draft-07/markup/json), with the
`$schema` and `$id` lines removed.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id":"https://www.github.com/unexpectedpanda/datmodel",
  "title": "DAT file specification",
  "description": "File that contains metadata for managing files on a hard drive.",
  "version": "2025-02-13 13:23:54",
  "type": "object",
  "required": ["dat_info", "collection"],
  "additionalProperties": false,
  "properties": {
    "$schema": {
      "description": "A public link to this JSON schema.",
      "$ref": "#/$defs/nonEmptyString"
    },
    "dat_info": {
      "description": "Content that describes the DAT file and its origin.",
      "type": "object",
      "required": ["schema", "name", "source", "date"],
      "additionalProperties": false,
      "properties": {
        "schema": {
          "description": "A link to the DAT schema used for the file.",
          "$ref": "#/$defs/nonEmptyString"
        },
        "name": {
          "description": "The scope of content covered by the DAT file. This might be a platform, curated collection, a theme, or otherwise.",
          "$ref": "#/$defs/nonEmptyString"
        },
        "source": {
          "description": "The origin of the DAT file, whether that be a group or individual.",
          "$ref": "#/$defs/nonEmptyString"
        },
        "source_url": {
          "description": "The website of the source.",
          "$ref": "#/$defs/nonEmptyString"
        },
        "version": {
          "description": "The version of the DAT file, following semantic versioning.",
          "$ref": "#/$defs/nonEmptyString",
          "pattern": "^(?:0|[1-9][0-9]*)\\.(?:0|[1-9][0-9]*)\\.(?:0|[1-9][0-9]*)(?:-((?:0|[1-9][0-9]*|[0-9]*[a-zA-Z-][0-9a-zA-Z-]*)(?:\\.(?:0|[1-9][0-9]*|[0-9]*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\\+(?:[0-9a-zA-Z-]+(?:\\.[0-9a-zA-Z-]+)*))?$"
        },
        "date": {
          "description": "When the DAT file was created, in extended ISO 8601 format, without the time zone. For example: YYYY-MM-DD hh:mm:ss",
          "$ref": "#/$defs/nonEmptyString",
          "pattern": "^[2-9][0-9]{3,3}-(?:(?:0[469]|11)-(?:0[1-9]|1[0-9]|2[0-9]|30)|02-(?:0[1-9]|1[0-9]|2[0-9])|(?:0[13578]|10|12)-(?:0[1-9]|1[0-9]|2[0-9]|3[01])) (?:0[0-9]|1[0-9]|2[0-3]):(?:[0-5][0-9]:?){1,2}(?<!:)$"
        },
        "contributors": {
          "description": "When multiple people have contributed to the data contained in the DAT file, they are listed here.",
          "type": "array",
          "items": {
            "$ref": "#/$defs/nonEmptyString"
          }
        },
        "comments": {
          "description": "Relevant comments about the DAT file. For example, compression settings used, or other things users should know about.",
          "$ref": "#/$defs/nonEmptyString"
        }
      }
    },
    "collection": {
      "description": "Content that describes titles in the collection.",
      "type": "array",
      "minProperties": 1,
      "contains": {
        "type": "object",
        "required": ["group", "releases"],
        "additionalProperties": false,
        "properties": {
          "group": {
            "description": "The name for the group that contains related titles, in UTF-8. For example, the 'Doom' group might contain 'Doom (USA)', 'Doom (Europe)', and 'Doom (Japan)', along with their various different versions.",
            "$ref": "#/$defs/nonEmptyString"
          },
          "releases": {
            "description": "Contains objects that describe the details about each title that is associated with the group.",
            "type": "array",
            "minProperties": 1,
            "contains": {
              "type": "object",
              "required": ["name", "regions", "languages", "release_date", "build" ,"is_demo", "was_published", "sets"],
              "additionalProperties": false,
              "properties": {
                "name": {
                  "description": "The name of the title, in UTF-8. This is used for the name of the archive or folder. Path separators are valid (both forward and back slashes). Names can't end with a period or space.",
                  "$ref": "#/$defs/nonEmptyString",
                  "pattern": "^[^:<>\"|?*].*[^. :<>\"|?*]$",
                  "not": {
                    "description": "Regular expressions to exclude non-UTF-8 characters.",
                    "anyOf": [
                      {
                        "pattern": "[\\xC0-\\xC1]"
                      },
                      {
                        "pattern": "[\\xF5-\\xFF]"
                      },
                      {
                        "pattern": "\\xE0[\\x80-\\x9F]"
                      },
                      {
                        "pattern": "\\xF0[\\x80-\\x8F]"
                      },
                      {
                        "pattern": "[\\xC2-\\xDF](?![\\x80-\\xBF])"
                      },
                      {
                        "pattern": "[\\xE0-\\xEF](?![\\x80-\\xBF]{2})"
                      },
                      {
                        "pattern": "[\\xF0-\\xF4](?![\\x80-\\xBF]{3})"
                      },
                      {
                        "pattern": "(?<=[\\x00-\\x7F\\xF5-\\xFF])[\\x80-\\xBF]"
                      },
                      {
                        "pattern": "(?<![\\xC2-\\xDF]|[\\xE0-\\xEF]|[\\xE0-\\xEF][\\x80-\\xBF]|[\\xF0-\\xF4]|[\\xF0-\\xF4][\\x80-\\xBF]|[\\xF0-\\xF4][\\x80-\\xBF]{2})[\\x80-\\xBF]"
                      },
                      {
                        "pattern": "(?<=[\\xE0-\\xEF])[\\x80-\\xBF](?![\\x80-\\xBF])"
                      },
                      {
                        "pattern": "(?<=[\\xF0-\\xF4])[\\x80-\\xBF](?![\\x80-\\xBF]{2})"
                      },
                      {
                        "pattern": "(?<=[\\xF0-\\xF4][\\x80-\\xBF])[\\x80-\\xBF](?![\\x80-\\xBF])"
                      }
                    ]
                  }
                },
                "db_id": {
                  "$ref": "#/$defs/nonEmptyString"
                },
                "build": {
                  "enum": [
                    "Production",
                    "Preproduction",
                    "Release candidate",
                    "Beta",
                    "Alpha",
                    "Prototype",
                    "Development",
                    "Debug",
                    "Review"
                  ]
                },
                "is_demo": {
                  "type": "boolean"
                },
                "was_published": {
                  "type": "boolean"
                },
                "serial": {
                  "$ref": "#/$defs/stringnull"
                },
                "regions": {
                  "description": "The regions the title was released in.",
                  "type": "array",
                  "items": {
                    "anyOf": [
                      {
                        "$ref": "#/$defs/regionsGroup"
                      },
                      {
                        "$ref": "#/$defs/regionsIndividual"
                      }
                    ]
                  }
                },
                "subregions": {
                  "description": "If a group region is used, define the subregions.",
                  "type": "array"
                },
                "languages": {
                  "description": "The languages the title supports.",
                  "type": "object",
                  "required": ["audio", "subtitles"],
                  "additionalProperties": false,
                  "properties": {
                    "audio": {
                      "type": "array",
                      "items": {
                        "$ref": "#/$defs/stringnull"
                      }
                    },
                    "subtitles": {
                      "type": "array",
                      "items": {
                        "$ref": "#/$defs/stringnull"
                      }
                    }
                  }
                },
                "type": {
                  "$ref": "#/$defs/nonEmptyString"
                },
                "release_date": {
                  "description": "The date the title was released, in extended ISO 8601 format, without the time zone. Acceptable formats are YYYY-MM-DD hh:mm:ss, YYYY-MM-DD hh:mm, YYYY-MM-DD, YYYY-MM, YYYY, and null for an unknown date.",
                  "$ref": "#/$defs/nonEmptyString",
                  "anyOf" : [
                    {
                      "description": "YYYY-MM-DD hh:mm:ss",
                      "pattern": "^[1-9][0-9]{3,3}-(?:(?:0[469]|11)-(?:0[1-9]|1[0-9]|2[0-9]|30)|02-(?:0[1-9]|1[0-9]|2[0-9])|(?:0[13578]|10|12)-(?:0[1-9]|1[0-9]|2[0-9]|3[01])) (?:0[0-9]|1[0-9]|2[0-3]):(?:[0-5][0-9]:?){1,2}(?<!:)$"
                    },
                    {
                      "description": "YYYY-MM-DD hh:mm",
                      "pattern": "^[1-9][0-9]{3,3}-(?:(?:0[469]|11)-(?:0[1-9]|1[0-9]|2[0-9]|30)|02-(?:0[1-9]|1[0-9]|2[0-9])|(?:0[13578]|10|12)-(?:0[1-9]|1[0-9]|2[0-9]|3[01])) (?:0[0-9]|1[0-9]|2[0-3]):(?:[0-5][0-9])$"
                    },
                    {
                      "description": "YYYY-MM-DD",
                      "pattern": "^[1-9][0-9]{3,3}-(?:(?:0[469]|11)-(?:0[1-9]|1[0-9]|2[0-9]|30)|02-(?:0[1-9]|1[0-9]|2[0-9])|(?:0[13578]|10|12)-(?:0[1-9]|1[0-9]|2[0-9]|3[01]))$"
                    },
                    {
                      "description": "YYYY-MM",
                      "pattern": "^[1-9][0-9]{3,3}-(?:0[1-9]|1[0-2])$"
                    },
                    {
                      "description": "YYYY",
                      "pattern": "^[1-9][0-9]{3,3}$"
                    },
                    {
                      "type": "null"
                    }
                  ]
                },
                "sets": {
                  "type": "object",
                  "minProperties": 1,
                  "properties": {
                    "files": {
                      "type": "array",
                      "contains": {
                        "type": "object",
                        "properties": {
                          "container": {
                            "$ref": "#/$defs/stringnull"
                          },
                          "files": {
                            "description": "The file properties.",
                            "type": "array",
                            "minProperties": 1,
                            "contains": {
                              "type": "object",
                              "required": ["name", "size", "digests"],
                              "additionalProperties": false,
                              "properties": {
                                "name": {
                                  "type": "string"
                                },
                                "size": {
                                  "type": "integer"
                                },
                                "digests": {
                                  "type": "object"
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              },
              "if": {
                "properties": {
                  "regions": {
                    "anyOf": [
                      {
                        "const": ["Africa"]
                      },
                      {
                        "const": ["Asia"]
                      },
                      {
                        "const": ["Europe"]
                      },
                      {
                        "const": ["Latin America"]
                      },
                      {
                        "const": ["Middle East"]
                      },
                      {
                        "const": ["Nordics"]
                      },
                      {
                        "const": ["Oceania"]
                      }
                    ]
                  }
                }
              },
              "then": {
                "required": ["subregions"]
              }
            }
          }
        }
      }
    }
  },
  "$defs": {
    "nonEmptyString": {
      "type": "string",
      "minLength": 1,
      "not": {
        "anyOf": [
          {
            "pattern": "^\\s+$"
          },
          {
            "pattern": "^\\s+.*$"
          },
          {
            "pattern": "\\s+$"
          }
        ]
      }
    },
    "stringnull": {
      "anyOf": [
        {
          "$ref": "#/$defs/nonEmptyString"
        },
        {
          "type": "null"
        }
      ]
    },
    "languages": {
      "enum": [
        "Abkhazain",
        "Afar",
        "Afrikaans",
        "Akan",
        "Albanian",
        "Amharic",
        "Arabic",
        "Arabic (Algeria)",
        "Arabic (Bahrain)",
        "Arabic (Egypt)",
        "Arabic (Iraq)",
        "Arabic (Jordan)",
        "Arabic (Kuwait)",
        "Arabic (Lebanon)",
        "Arabic (Libya)",
        "Arabic (Morocco)",
        "Arabic (Oman)",
        "Arabic (Qatar)",
        "Arabic (Saudi Arabia)",
        "Arabic (Syria)",
        "Arabic (Tunisia)",
        "Arabic (UAE)",
        "Arabic (Yemen)",
        "Aragonese",
        "Armenian",
        "Assamese",
        "Avaric",
        "Aymara",
        "Azerbaijani",
        "Bambara",
        "Bashkir",
        "Basque",
        "Belarusian",
        "Bengali",
        "Bislama",
        "Bosnian",
        "Breton",
        "Bulgarian",
        "Burmese",
        "Catalan",
        "Chamorro",
        "Chechen",
        "Chichewa",
        "Chinese (Cantonese)"
        "Chinese (Mandarin)",
        "Chinese (Simplified)",
        "Chinese (Traditional)",
        "Chuvash",
        "Cornish",
        "Corsican",
        "Cree",
        "Croatian",
        "Czech",
        "Danish",
        "Divehi",
        "Dutch",
        "Dzongkha",
        "English",
        "English (Australia)",
        "English (Belize)",
        "English (Canada)",
        "English (Ireland)",
        "English (Jamaica)",
        "English (New Zealand)",
        "English (South Africa)",
        "English (Trinidad)",
        "English (United States)"
        "Estonian",
        "Ewe",
        "Faroese",
        "Fijian",
        "Finnish",
        "French",
        "French (Belgium)",
        "French (Canada)",
        "French (Luxembourg)",
        "French (Standard)",
        "French (Switzerland)",
        "Frisian",
        "Fulah",
        "Gaelic (Scotland)",
        "Galician",
        "Ganda",
        "Georgian",
        "German",
        "German (Austria)",
        "German (Liechtenstein)",
        "German (Luxembourg)",
        "German (Switzerland)",
        "Greek",
        "kalaallisut",
        "Guarani",
        "Gujarati",
        "Haitian",
        "Hausa",
        "Hebrew",
        "Herero",
        "Hindi",
        "Hiri Motu",
        "Hungarian",
        "Icelandic",
        "Igbo",
        "Indonesian",
        "Inukitut",
        "Inupiaq",
        "Irish",
        "Italian",
        "Italian (Switzerland)",
        "Japanese",
        "Javanese",
        "Kannada",
        "Kanuri",
        "Kashmiri",
        "Kazakh",
        "Khmer",
        "Kikuyu",
        "Kinyarwanda",
        "Kyrgyz",
        "Komi",
        "Kongo",
        "Korean",
        "Kuanyama",
        "Kurdish",
        "Lao",
        "Latvian",
        "Limburgan",
        "Lingala",
        "Lithuanian",
        "Luba-Katanga",
        "Luxembourgish",
        "Macedonian",
        "Malagasy",
        "Malay",
        "Malayalam",
        "Maltese",
        "Manx",
        "Maori",
        "Marathi",
        "Marshallese",
        "Mongolian",
        "Nauru",
        "Navajo",
        "Ndebele (North)",
        "Ndebele (South)",
        "Ndonga",
        "Nepali",
        "Norwegian",
        "Norwegian (Bokmål)",
        "Norwegian (Nynorsk)",
        "Occitan",
        "Ojibwa",
        "Oriya",
        "Oromo",
        "Ossetian",
        "Pashto",
        "Persian",
        "Polish",
        "Portuguese"
        "Portuguese (Brazil)",
        "Portuguese (Portugal)",
        "Punjabi",
        "Quechua",
        "Romanian",
        "Romanian (Romania)",
        "Romanian (Republic of Moldova)",
        "Romansh",
        "Rundi",
        "Russian",
        "Russian (Republic of Moldova)",
        "Sami (Northern)",
        "Samoan",
        "Sango",
        "Sardinian",
        "Serbian",
        "Shona",
        "Sindhi",
        "Sinhala",
        "Slovak",
        "Slovenian",
        "Somali",
        "Sotho (Southern)",
        "Spanish",
        "Spanish (Argentina)",
        "Spanish (Bolivia)",
        "Spanish (Chile)",
        "Spanish (Colombia)",
        "Spanish (Costa Rica)",
        "Spanish (Dominican Republic)",
        "Spanish (Ecuador)",
        "Spanish (El Salvador)",
        "Spanish (Guatemala)",
        "Spanish (Honduras)",
        "Spanish (Latin America)",
        "Spanish (Mexico)",
        "Spanish (Nicaragua)",
        "Spanish (Panama)",
        "Spanish (Paraguay)",
        "Spanish (Peru)",
        "Spanish (Puerto Rico)",
        "Spanish (Uruguay)",
        "Spanish (Venezuela)",
        "Sundanese",
        "Swahili",
        "Swati",
        "Swedish",
        "Swedish (Finland)",
        "Swedish (Sweden)",
        "Tagalog",
        "Tahitian",
        "Tajik",
        "Tamil",
        "Tatar",
        "Telugu",
        "Thai",
        "Tibetan",
        "Tigrinya",
        "Tonga",
        "Tswana",
        "Turkish",
        "Turkmen",
        "Twi",
        "Uighur",
        "Ukrainian",
        "Urdu",
        "Uzbek",
        "Venda",
        "Vietnamese",
        "Walloon",
        "Welsh",
        "Wolof",
        "Xhosa",
        "Yi (Sichuan)",
        "Yiddish",
        "Yoruba",
        "Zhuang",
        "Zulu"
      ]
    },
    "regionsGroup": {
      "enum": [
        "Global",
        "Africa",
        "Asia",
        "Europe",
        "Latin America",
        "Middle East",
        "North America",
        "Nordics",
        "Oceania",
        "South America"
      ]
    },
    "regionsIndividual": {
      "enum": [
        "Afghanistan",
        "Albania",
        "Algeria",
        "American Samoa",
        "Andorra",
        "Angola",
        "Anguilla",
        "Antigua and Barbuda",
        "Argentina",
        "Armenia",
        "Aruba",
        "Australia",
        "Austria",
        "Azerbaijan",
        "Bahamas",
        "Bahrain",
        "Bangladesh",
        "Barbados",
        "Belarus",
        "Belgium",
        "Belize",
        "Benin",
        "Bermuda",
        "Bhutan",
        "Bolivia",
        "Bosnia and Herzegovina",
        "Botswana",
        "Brazil",
        "British Virgin Islands",
        "Brunei",
        "Bulgaria",
        "Burkina Faso",
        "Burundi",
        "Cabo Verde",
        "Cambodia",
        "Cameroon",
        "Canada",
        "Caribbean Netherlands",
        "Cayman Islands",
        "Central African Republic",
        "Chad",
        "Chile"
        "China",
        "Colombia",
        "Comoros",
        "Congo",
        "Cook Islands",
        "Costa Rica",
        "Croatia",
        "Cuba",
        "Curaçao",
        "Cyprus",
        "Czechia",
        "Côte d'Ivoire",
        "Denmark",
        "Djibouti",
        "Dominica",
        "Dominican Republic",
        "DR Congo",
        "Ecuador",
        "Egypt",
        "El Salvador",
        "Equatorial Guinea",
        "Eritrea",
        "Estonia",
        "Eswatini",
        "Ethiopia",
        "Faeroe Islands",
        "Falkland Islands",
        "Fiji",
        "Finland",
        "France",
        "French Guiana",
        "French Polynesia",
        "Gabon",
        "Gambia",
        "Georgia",
        "Germany",
        "Ghana",
        "Gibraltar",
        "Greece",
        "Greenland",
        "Grenada",
        "Guadeloupe",
        "Guam",
        "Guatemala",
        "Guinea",
        "Guinea-Bissau",
        "Guyana",
        "Haiti",
        "Holy-See",
        "Honduras",
        "Hong Kong",
        "Hungary",
        "Iceland",
        "India",
        "Indonesia",
        "Iran",
        "Iraq",
        "Ireland",
        "Isle of Man",
        "Israel",
        "Italy",
        "Jamaica",
        "Japan",
        "Jordan",
        "Kazakhstan",
        "Kenya",
        "Kiribati",
        "Kuwait",
        "Kyrgyzstan",
        "Laos",
        "Latvia",
        "Lebanon",
        "Lesotho",
        "Liberia",
        "Libya",
        "Liechtenstein",
        "Lithuania",
        "Luxembourg",
        "Macao",
        "Madagascar",
        "Malawai",
        "Malaysia",
        "Maldives",
        "Mali",
        "Malta",
        "Marshall Islands",
        "Martinique",
        "Mauritania",
        "Mauritius",
        "Macedonia",
        "Mayotte",
        "Mexico",
        "Micronesia",
        "Moldova",
        "Monaco",
        "Mongolia",
        "Montenegro",
        "Montserrat",
        "Morocco",
        "Mozambique",
        "Myanmar",
        "Namibia",
        "Nauru",
        "Nepal",
        "Netherlands",
        "New Caledonia",
        "New Zealand",
        "Nicaragua",
        "Niue",
        "Niger",
        "Nigeria",
        "North Korea",
        "North Macedonia",
        "Northern Mariana Islands",
        "Norway",
        "Oman",
        "Pakistan",
        "Palau",
        "Panama",
        "Papua New Guinea".
        "Paraguay",
        "Peru",
        "Philippines",
        "Poland",
        "Portugal",
        "Puerto Rico",
        "Qatar",
        "Réunion",
        "Romania",
        "Russia",
        "Rwanda",
        "Saint Barthelemy",
        "Saint Helena",
        "Saint Kitts & Nevis",
        "Saint Lucia",
        "Saint Pierre & Miquelon",
        "Samoa",
        "San Marino",
        "Sao Tome & Principe",
        "Saudi Arabia",
        "Senegal",
        "Serbia",
        "Seychelles",
        "Sierra Leone",
        "Singapore",
        "Sint Maarten",
        "Slovakia",
        "Slovenia",
        "Solomon Islands",
        "South Africa",
        "South Korea",
        "South Sudan",
        "Spain",
        "Sri Lanka",
        "St. Vincent & Grenadines",
        "State of Palestine",
        "Sudan",
        "Suriname",
        "Sweden",
        "Switzerland",
        "Syria",
        "Taiwan",
        "Tajikstan",
        "Tanzania",
        "Thailand",
        "Timor-Leste"
        "Togo",
        "Tokelau",
        "Tonga",
        "Trinidad and Tobago"
        "Tunisia",
        "Türkiye",
        "Turks and Caicos",
        "Turkmenistan",
        "Tuvalu",
        "U.S. Virgin Islands",
        "Uganda",
        "Ukraine",
        "United Arab Emirates",
        "United Kingdom",
        "United States"
        "Unknown",
        "Uruguay",
        "Uzbekistan",
        "Vanuatu",
        "Venezuela",
        "Vietnam",
        "Wallis & Futuna",
        "Western Sahara",
        "Yemen",
        "Zambia",
        "Zimbabwe"
      ]
    }
  }
}
```
