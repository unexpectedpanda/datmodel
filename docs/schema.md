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
  "description": "2025-03-03 10:38",
  "type": "object",
  "required": ["datInfo", "collection"],
  "additionalProperties": false,
  "properties": {
    "datInfo": {
      "description": "Content that describes the DAT file and its origin.",
      "type": "object",
      "required": ["schema", "name", "source", "date"],
      "additionalProperties": false,
      "properties": {
        "comments": {
          "description": "Relevant comments about the DAT file. For example, compression settings used, or other things users should know about.",
          "$ref": "#/$defs/nonEmptyString"
        },
        "contributors": {
          "description": "When multiple people have contributed to the data contained in the DAT file, they are listed here.",
          "type": "array",
          "items": {
            "$ref": "#/$defs/nonEmptyString"
          }
        },
        "date": {
          "description": "When the DAT file was created, in extended ISO 8601 format, without the time zone. For example: YYYY-MM-DD hh:mm:ss",
          "$ref": "#/$defs/nonEmptyString",
          "pattern": "^[2-9][0-9]{3,3}-(?:(?:0[469]|11)-(?:0[1-9]|1[0-9]|2[0-9]|30)|02-(?:0[1-9]|1[0-9]|2[0-9])|(?:0[13578]|10|12)-(?:0[1-9]|1[0-9]|2[0-9]|3[01])) (?:0[0-9]|1[0-9]|2[0-3]):(?:[0-5][0-9]:?){1,2}(?<!:)$"
        },
        "name": {
          "description": "The scope of content covered by the DAT file. This might be a platform, curated collection, a theme, or otherwise.",
          "$ref": "#/$defs/nonEmptyString"
        },
        "schema": {
          "description": "A link to the DAT schema used for the file.",
          "$ref": "#/$defs/nonEmptyString"
        },
        "source": {
          "description": "The origin of the DAT file, whether that be a group or individual.",
          "$ref": "#/$defs/nonEmptyString"
        },
        "sourceUrl": {
          "description": "The website of the source.",
          "$ref": "#/$defs/nonEmptyString"
        },
        "version": {
          "description": "The version of the DAT file, following semantic versioning.",
          "$ref": "#/$defs/nonEmptyString",
          "pattern": "^(?:0|[1-9][0-9]*)\\.(?:0|[1-9][0-9]*)\\.(?:0|[1-9][0-9]*)(?:-((?:0|[1-9][0-9]*|[0-9]*[a-zA-Z-][0-9a-zA-Z-]*)(?:\\.(?:0|[1-9][0-9]*|[0-9]*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\\+(?:[0-9a-zA-Z-]+(?:\\.[0-9a-zA-Z-]+)*))?$"
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
              "required": ["build", "languages", "name", "regions", "releaseOrder", "sets"],
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
                        "pattern": "^(?:Add-on|Audio|Update|Video)$"
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
                        "pattern": "^(?:Children|Educational)$"
                      }
                    }
                  },
                  "then": {
                    "properties": {
                      "type": {
                        "pattern": "^(?:Application|Audio|Game|Multimedia|Video)$"
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
                "build": {
                  "description": "When in the software release life cycle the title was released.",
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
                "developer": {
                  "description": "The developer of the title.",
                  "$ref": "#/$defs/nonEmptyString"
                },
                "id": {
                  "description": "A unique ID for the release. Usually a database ID.",
                  "$ref": "#/$defs/nonEmptyString"
                },
                "isDemo": {
                  "description": "Whether the title is a demo.",
                  "type": "boolean"
                },
                "isMIA": {
                  "description": "Whether the title's digests have been verified by more than one person. If not, set the value to true.",
                  "type": "boolean"
                },
                "isSuperset": {
                  "description": "Whether the title contains more content than the original release, or for some reason is superior to another version. For example, game of the year editions, a regional variant with uncensored content, or a DVD version of a title previously released on multiple CDs.",
                  "type": "boolean"
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
                "localNames": {
                  "description": "Local names given to the title, defined by language.",
                  "type": "object",
                  "minProperties": 1,
                  "patternProperties": {
                    "^[a-zA-Z0-9-]+$": {
                      "$ref": "#/$defs/nonEmptyString"
                    }
                  }
                },
                "name": {
                  "description": "The name of the title, in UTF-8. This is used for the name of the archive or folder. Must use / for path separators. Names can't end with a period or space.",
                  "$ref": "#/$defs/stringFile"
                },
                "peripherals": {
                  "description": "Contains inputs used to control the title, or devices that show output from the title.",
                  "type": "array",
                  "minItems": 1,
                  "items": {
                    "$ref": "#/$defs/peripherals"
                  }
                },
                "players": {
                  "decsription": "The number of players the title supports.",
                  "type": "integer"
                },
                "playModes": {
                  "decsription": "The number of players the title supports.",
                  "type": "array",
                  "minitems": 1,
                  "items": {
                    "$ref": "#/$defs/playModes"
                  }
                },
                "published": {
                  "description": "Whether the title was published. Unpublished titles that didn't have an official release should be set to false.",
                  "type": "boolean"
                },
                "publisher": {
                  "description": "The publisher of the title.",
                  "$ref": "#/$defs/nonEmptyString"
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
                "releaseDate": {
                  "description": "The date the title was released, in extended ISO 8601 format, without the time zone. Valid formats are YYYY-MM-DD hh:mm:ss, YYYY-MM-DD hh:mm, YYYY-MM-DD, YYYY-MM, YYYY, and null for an unknown date.",
                  "anyOf": [
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
                    }
                  ]
                },
                "releaseOrder": {
                  "description": "An integer-based version assigned internally by the DAT maintainer, where 1 is the earliest release of the title, and higher numbers were released later. This helps with 1G1R decisions by removing the need to compare multiple different versioning systems, and can stand in for when release dates are unknown.",
                  "type": "integer"
                },
                "serial": {
                  "description": "A manufacturer identifier for the release. Might be a cartridge serial, disc ring code, or otherwise.",
                  "$ref": "#/$defs/stringnull"
                },
                "sets": {
                  "description": "Defines the different file sets within the release.",
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
                        "description": "Describes an individual file set.",
                        "type": "array",
                        "minProperties": 1,
                        "contains": {
                          "type": "object",
                          "required": ["files"],
                          "additionalProperties": false,
                          "properties": {
                            "addOns": {
                              "description": "The add-ons associated with the set. This includes DLC.",
                              "type": "array",
                              "contains": {
                                "type": "object"
                              }
                            },
                            "comments": {
                              "description": "A description of the set.",
                              "$ref": "#/$defs/nonEmptyString"
                            },
                            "container": {
                              "description": "The container that the application managing the DAT file should use for the file set. Must be one of the following values: auto, folder, or null.",
                              "$ref": "#/$defs/stringnull"
                            },
                            "name": {
                              "description": "Overrides the release name key to become the archive or folder name used for the set.",
                              "$ref": "#/$defs/stringFile"
                            },
                            "files": {
                              "description": "The files in the set and their properties.",
                              "type": "array",
                              "contains": {
                                "type": "object",
                                "required": ["digests", "name", "size"],
                                "additionalProperties": false,
                                "properties": {
                                  "dateModified": {
                                    "description": "The last modified date that should be applied by the client application that's parsing the DAT file and operating on related files. Because FAT file systems have a time resolution of 2 seconds on last modified dates, you can only use even numbers for the seconds.",
                                    "type": "string",
                                    "pattern": "^[1-9][0-9]{3,3}-(?:(?:0[469]|11)-(?:0[1-9]|1[0-9]|2[0-9]|30)|02-(?:0[1-9]|1[0-9]|2[0-9])|(?:0[13578]|10|12)-(?:0[1-9]|1[0-9]|2[0-9]|3[01])) (?:0[0-9]|1[0-9]|2[0-3]):(?:[0-5][0-9]):(?:[0-5][02468])(?<!:)$"
                                  },
                                  "digests": {
                                    "description": "The digests of different hash functions. The following hash functions are preferred: crc32, sha256, xxh3_128, blake3.",
                                    "$ref": "#/$defs/digests"
                                  },
                                  "header": {
                                    "description": " The header for a ROM, in hex. Aids with addition of the header to a headerless ROM, or removal from a headered ROM.",
                                    "$ref": "#/$defs/stringnull"
                                  },
                                  "name": {
                                    "description": "The name of the file, in UTF-8. Must use / for path separators. Names can't end with a period or space.",
                                    "$ref": "#/$defs/stringnull"
                                  },
                                  "size": {
                                    "description": "The size of the file, in bytes.",
                                    "type": "integer"
                                  }
                                }
                              }
                            },
                            "id": {
                              "description": "A unique ID for the set. Usually a database ID.",
                              "$ref": "#/$defs/nonEmptyString"
                            },
                            "retroachievements": {
                              "description": "Whether retroachievements are support on the title.",
                              "type": "boolean"
                            },
                            "updates": {
                              "description": "The updates associated with the set.",
                              "type": "array",
                              "contains": {
                                "type": "object"
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                },
                "source": {
                  "description": "The release's origin.",
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
                    "Children",
                    "Educational",
                    "Manual",
                    "Update",
                    "Video"
                  ]
                },
                "type": {
                  "description": "The type of release.",
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
                "version": {
                  "description": "The version as reported by the title or media it came on. For example, Rev 1.",
                  "$ref": "#/$defs/stringnull"
                },
                "videoStandards": {
                  "description": "The video standard supported by the release. This describes a release's fixed output in both color and resolution, as opposed to any monitor standard that might be receiving the output. Use RGB for any release that supports higher resolutions than SVGA, and allows for flexible resolution output.",
                  "$ref": "#/$defs/videoStandards"
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
        "sha1Internal": {
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
    "peripherals": {
      "enum": [
        "Controller",
        "Controller with Touchpad",
        "Controller with Trackball",
        "Analog Joystick",
        "Dance Pad",
        "Digital Joystick",
        "Digital Twin Sticks",
        "Drums",
        "EyeToy",
        "Flight Stick",
        "Guitar",
        "HOTAS",
        "Keyboard",
        "Light Gun",
        "Magnavox Odyssey Controller",
        "Microphone",
        "Microsoft Kinect",
        "Microsoft Xbox Live Vision",
        "Mouse",
        "Nintendo Joy-Con",
        "Nintendo Wii Balance Board",
        "Nintendo Wii Remote",
        "Nintendo Wii Remote and Nunchuk",
        "Nintendo Power Glove",
        "Pedals",
        "Sega Dreamcast VMU",
        "Sony EyeToy",
        "Sony PlayStation Eye",
        "Sony PlayStation Move",
        "Sony Sixaxis",
        "Spinner",
        "Steering Wheel (Lock-to-lock)/Paddle",
        "Steering Wheel (360°)",
        "Touchscreen",
        "Trackball",
        "VR Headset",
        "VR Headset and Controls"
      ]
    },
    "playModes": {
      "enum": [
        "Single Player",
        "Co-op (Split-screen)",
        "Co-op (Local)",
        "Co-op (Online)",
        "Competitive (Split-screen Free-for-all)",
        "Competitive (Split-screen Team)",
        "Competitive (Local Free-for-all)",
        "Competitive (Local Team)",
        "Competitive (Online Free-for-all)",
        "Competitive (Online Team)"
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
    },
    "videoStandards": {
      "enum": [
        "4K Ultra HD",
        "8K Ultra HD",
        "AX-VGA",
        "CGA",
        "EGA",
        "EVGA",
        "HGC",
        "HDTV (720i)",
        "HDTV (720p)",
        "Full HDTV (1080i)",
        "Full HDTV (1080p)",
        "JEGA",
        "MCGA",
        "MDA",
        "MPAL",
        "NTSC",
        "NTSC (DV) (480i)",
        "NTSC (DV) (480p)",
        "PAL",
        "PAL (DV) (576i)",
        "PAL (DV) (576p)",
        "PAL 60Hz",
        "PGC",
        "Plantronics",
        "Quadcolor",
        "RGB",
        "SECAM",
        "SVGA",
        "Tandy",
        "TIGA",
        "VGA",
        "XGA"
      ]
    }
  }
}
```
