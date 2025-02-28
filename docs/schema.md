---
hide:
  - footer
---

# Schema

You can test validating against this schema with
[JSON Schema Validator](https://www.jsonschemavalidator.net/).

``` {.json .copy}
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id":"https://www.github.com/unexpectedpanda/datmodel",
  "title": "DAT file specification",
  "description": "2025-02-13 13:23:54",
  "type": "object",
  "required": ["dat_info", "collection"],
  "additionalProperties": false,
  "properties": {
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
            "description": "The name for the group that contains related titles, in UTF-8. For example, the 'Some Video Game ' group might contain 'Some Video Game (USA)', 'Some Video Game (USA) (v1.1)', 'Some Video Game  (Europe)', and 'Some Video Game  (Japan)'.",
            "$ref": "#/$defs/nonEmptyString"
          },
          "releases": {
            "description": "Contains objects that describe the details about each title that is associated with the group.",
            "type": "array",
            "minProperties": 1,
            "contains": {
              "type": "object",
              "required": ["name", "regions", "languages", "release_date", "build", "published", "sets"],
              "dependentRequired": {
                "subtype": ["type"]
              },
              "additionalProperties": false,
              "allOf": [
                {
                  "description": "The rules that manage what types that subtypes require",
                  "if": {
                    "properties": {
                      "subtype": {
                        "pattern": "^(?:Add-on|Audio|Demo|Update|Video)$"
                      }
                    }
                  },
                  "then": {
                    "properties": {
                      "type": {
                        "pattern": "^(?:Application|Game)$"
                      }
                    }
                  }
                },
                {
                  "if": {
                    "properties": {
                      "subtype": {
                        "const": "Manual"
                      }
                    }
                  },
                  "then": {
                    "properties": {
                      "type": {
                        "pattern": "^(?:Application|Device|Game)$"
                      }
                    }
                  }
                }
              ],
              "properties": {
                "name": {
                  "description": "The name of the title, in UTF-8. This is used for the name of the archive or folder. Must use / for path separators. Names can't end with a period or space.",
                  "$ref": "#/$defs/stringFile"
                },
                "build": {
                  "description": "",
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
                "published": {
                  "type": "boolean"
                },
                "type": {
                  "enum": [
                    "Application",
                    "Audio",
                    "BIOS",
                    "Chip",
                    "Coverdisc",
                    "Device",
                    "Prototype",
                    "Firmware",
                    "Game",
                    "Magazine",
                    "Multimedia",
                    "Video"
                  ]
                },
                "release_date": {
                  "description": "The date the title was released, in extended ISO 8601 format, without the time zone. Valid formats are YYYY-MM-DD hh:mm:ss, YYYY-MM-DD hh:mm, YYYY-MM-DD, YYYY-MM, YYYY, and null for an unknown date.",
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
                      "description": "Empty string",
                      "pattern": "^$"
                    }
                  ]
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
                "languages": {
                  "description": "The languages the title supports.",
                  "type": "object",
                  "required": ["audio", "interface", "subtitles"],
                  "additionalProperties": false,
                  "properties": {
                    "audio": {
                      "type": "array",
                      "items": {
                        "type": "string"
                      }
                    },
                    "interface": {
                      "type": "array",
                      "items": {
                        "type": "string"
                      }
                    },
                    "subtitles": {
                      "type": "array",
                      "items": {
                        "type": "string"
                      }
                    }
                  }
                },
                "id": {
                  "description": "A unique ID for the release. Usually a database ID.",
                  "$ref": "#/$defs/nonEmptyString"
                },
                "local_names": {
                  "type": "object",
                  "minProperties": 1,
                  "patternProperties": {
                    "^[a-zA-Z0-9-]+$": {
                      "$ref": "#/$defs/nonEmptyString"
                    }
                  }
                },
                "serial": {
                  "$ref": "#/$defs/stringnull"
                },
                "source": {
                  "type": "array",
                  "minItems": 1,
                  "items": {
                    "$ref": "#/$defs/media"
                  }
                },
                "subtype": {
                  "description": "The subtype of the release. Must be paired with a valid type.",
                  "enum": [
                    "Add-on",
                    "Audio",
                    "Demo",
                    "Manual",
                    "Update",
                    "Video"
                  ]
                },
                "sets": {
                  "type": "array",
                  "minProperties": 1,
                  "contains": {
                    "type": "object",
                    "required": ["name", "set"],
                    "additionalProperties": false,
                    "properties": {
                      "name": {
                        "description": "The name of the file set, in UTF-8. Can be any non-empty string, although generally you should use lowercase container format names. For example: bin, chd, iso. Use a null value for raw files without a container.",
                        "$ref": "#/$defs/stringnull"
                      },
                      "set": {
                        "type": "array",
                        "minProperties": 1,
                        "contains": {
                          "type": "object",
                          "required": ["container", "files"],
                          "additionalProperties": false,
                          "properties": {
                            "container": {
                              "description": "The container that the application managing the DAT file should use for the file set. Must be one of the following values: auto, folder, or null.",
                              "$ref": "#/$defs/stringnull"
                            },
                            "files": {
                              "type": "array",
                              "contains": {
                                "type": "object",
                                "required": ["name", "size", "digests"],
                                "additionalProperties": false,
                                "properties": {
                                  "name": {
                                    "description": "The name of the file, in UTF-8. Must use / for path separators. Names can't end with a period or space.",
                                    "$ref": "#/$defs/stringnull"
                                  },
                                  "size": {
                                    "description": "The size of the file, in bytes.",
                                    "type": "integer"
                                  },
                                  "digests": {
                                    "description": "The digests of different hash functions. The following hash functions are preferred: crc32, sha256, xxh3_128, blake3.",
                                    "$ref": "#/$defs/digests"
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
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
    "stringFile": {
      "allOf": [
        {
          "$ref": "#/$defs/nonEmptyString"
        },
        {
          "pattern": "^[^:<>\"\\\\|?*].*[^. :<>\"\\\\|?*]$",
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
        }
      ]
    },
    "digests": {
      "type": "object",
      "minProperties": 1,
      "properties": {
        "crc32": {
          "type": "string",
          "pattern": "^[a-fA-F0-9]{8,8}$"
        },
        "md5": {
          "type": "string",
          "pattern": "^[a-fA-F0-9]{32,32}$"
        },
        "sha1": {
          "type": "string",
          "pattern": "^[a-fA-F0-9]{40,40}$"
        },
        "sha1_internal": {
          "type": "string",
          "pattern": "^[a-fA-F0-9]{40,40}$"
        },
        "sha256": {
          "type": "string",
          "pattern": "^[a-fA-F0-9]{64,64}$"
        },
        "xxh3_128": {
          "type": "string",
          "pattern": "^[a-fA-F0-9]{32,32}$"
        },
        "blake3": {
          "type": "string",
          "pattern": "^[a-fA-F0-9]{64,64}$"
        }
      }
    },
    "media": {
      "enum": [
        "3.5\" floppy disk",
        "5.25\" floppy disk",
        "BD-ROM",
        "BD-ROM (Ultra HD)",
        "Cassette tape",
        "CD-ROM",
        "Device",
        "Digital",
        "DVD-ROM",
        "Famicom Disk",
        "GameCube Game Disc",
        "Game Card",
        "GD-ROM",
        "Hard Drive",
        "HD-DVD",
        "HuCard",
        "LaserDisc",
        "Memory Card",
        "ROM Card",
        "ROM Cartridge",
        "UMD",
        "VHS",
        "Wii Optical Disc",
        "Wii U Optical Disc"
      ]
    },
    "regionsGroup": {
      "enum": [
        "AFR",
        "ASI",
        "EUR",
        "GLO",
        "LAM",
        "MDE",
        "NAM",
        "NOR",
        "OCE",
        "SAM"
      ]
    },
    "regionsIndividual": {
      "enum": [
        "AD",
        "AE",
        "AF",
        "AG",
        "AI",
        "AL",
        "AM",
        "AO",
        "AQ",
        "AR",
        "AS",
        "AT",
        "AU",
        "AW",
        "AX",
        "AZ",
        "BA",
        "BB",
        "BD",
        "BE",
        "BF",
        "BG",
        "BH",
        "BI",
        "BJ",
        "BL",
        "BM",
        "BN",
        "BO",
        "BQ",
        "BR",
        "BS",
        "BT",
        "BV",
        "BW",
        "BY",
        "BZ",
        "CA",
        "CC",
        "CD",
        "CF",
        "CG",
        "CH",
        "CI",
        "CK",
        "CL",
        "CM",
        "CN",
        "CO",
        "CR",
        "CU",
        "CV",
        "CW",
        "CX",
        "CY",
        "CZ",
        "DE",
        "DJ",
        "DK",
        "DM",
        "DO",
        "DZ",
        "EC",
        "EE",
        "EG",
        "EH",
        "ER",
        "ES",
        "ET",
        "FI",
        "FJ",
        "FK",
        "FM",
        "FO",
        "FR",
        "GA",
        "GB",
        "GD",
        "GE",
        "GF",
        "GG",
        "GH",
        "GI",
        "GL",
        "GM",
        "GN",
        "GP",
        "GQ",
        "GR",
        "GS",
        "GT",
        "GU",
        "GW",
        "GY",
        "HK",
        "HM",
        "HN",
        "HR",
        "HT",
        "HU",
        "ID",
        "IE",
        "IL",
        "IM",
        "IN",
        "IO",
        "IQ",
        "IR",
        "IS",
        "IT",
        "JE",
        "JM",
        "JO",
        "JP",
        "KE",
        "KG",
        "KH",
        "KI",
        "KM",
        "KN",
        "KP",
        "KR",
        "KW",
        "KY",
        "KZ",
        "LA",
        "LB",
        "LC",
        "LI",
        "LK",
        "LR",
        "LS",
        "LT",
        "LU",
        "LV",
        "LY",
        "MA",
        "MC",
        "MD",
        "ME",
        "MF",
        "MG",
        "MH",
        "MK",
        "ML",
        "MM",
        "MN",
        "MO",
        "MP",
        "MQ",
        "MR",
        "MS",
        "MT",
        "MU",
        "MV",
        "MW",
        "MX",
        "MY",
        "MZ",
        "NA",
        "NC",
        "NE",
        "NF",
        "NG",
        "NI",
        "NL",
        "NO",
        "NP",
        "NR",
        "NU",
        "NZ",
        "OM",
        "PA",
        "PE",
        "PF",
        "PG",
        "PH",
        "PK",
        "PL",
        "PM",
        "PN",
        "PR",
        "PS",
        "PT",
        "PW",
        "PY",
        "QA",
        "RE",
        "RO",
        "RS",
        "RU",
        "RW",
        "SA",
        "SB",
        "SC",
        "SD",
        "SE",
        "SG",
        "SH",
        "SI",
        "SJ",
        "SK",
        "SL",
        "SM",
        "SN",
        "SO",
        "SR",
        "SS",
        "ST",
        "SV",
        "SX",
        "SY",
        "SZ",
        "TC",
        "TD",
        "TF",
        "TG",
        "TH",
        "TJ",
        "TK",
        "TL",
        "TM",
        "TN",
        "TO",
        "TR",
        "TT",
        "TV",
        "TW",
        "TZ",
        "UA",
        "UG",
        "UM",
        "US",
        "UY",
        "UZ",
        "VA",
        "VC",
        "VE",
        "VG",
        "VI",
        "VN",
        "VU",
        "WF",
        "WS",
        "YE",
        "YT",
        "ZA",
        "ZM",
        "ZW"
      ]
    }
  }
}
```
