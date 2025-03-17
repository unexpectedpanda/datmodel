---
hide:
  - footer
---

# `titles`

The `titles` array contains objects that describe the details about each title that is
associated with a group.

While many of the properties in the `titles` array are optional, the more that are
included, the more that a DAT application is able to filter on.

In the following example, required properties are highlighted. The values are for example
only.

``` {.json .copy hl_lines="3 21-26 38-40" }
"titles": [
  {
    "name": "Some Video Game (USA)",
    "id": "123456",
    "build": "Production",
    "published": true,
    "type": "Game",
    "subtype": "Educational",
    "releaseDate": "1993-10-12",
    "version": "Rev 1",
    "versionInternal": 1,
    "serial": "SLUS-000000",
    "isAlternate": false,
    "isCompilation": false,
    "isDemo": false,
    "isMIA": false,
    "isPirate": false,
    "isSuperset": false,
    "isUnlicensed": false,
    "contains": [],
    "regions": ["US"],
    "languages": {
      "audio": ["en", "ja"],
      "interface": ["en"],
      "subtitles": ["en"]
    },
    "localNames": [
      "en": "Some Video Game",
      "ja": "別のビデオゲーム"
    ],
    "developer": "That Game Dev",
    "publisher": "That Game Publisher",
    "source": ["3.5\" Floppy Disk"],
    "peripherals": ["Keyboard", "Mouse"],
    "players": 4,
    "playModes": ["Single Player", "Competitive (Online Free-for-all)"],
    "videoStandards": ["NTSC"],
    "sets": [
      ...
    ]
  }
]
```

## Required properties

<div class="definition-list" markdown>

* **`name`{ #name .toc-code }** `pattern string`{ .toc-def } `required`{ .toc-req }

    The name of the title, in UTF-8. Must be globally unique. This is used for the name of
    the archive or folder of the contained [sets](#sets), under the following conditions:

    * The [`container`](sets.md#container) of the set isn't set to `null`.

    * The [`containerName`](sets.md#containerName) of the set isn't defined.

    Names can't end with a period or space, start with a path separator, or use the
    following invalid path characters:

    ```
    :<>"|?*\
    ```

    Path separators are represented Linux-style, with `/` instead of `\`. Don't use
    absolute paths, paths are relative to a path the user sets.

    /// details | Expand for developer details
    Invalid path characters are found with the following regular expression:

    ``` {.text .copy}
    ^[^:<>\"\\|?*].*[^. :<>\"\\|?*]$
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

* **`regions`{ #regions .toc-code }** `enum array`{ .toc-def } `required`{ .toc-req }

    Which regions the title was released in. Valid individual region codes are two
    characters long, and are described in
    [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). Grouped
    regions are three characters long, and defined entirely by this standard.

    The following general rules apply:

    * If you don't know where a title is from, use an empty array:

        ```json
        "regions": []
        ```

    * If you do know where a title is from, prefer listing individual regions over grouped
      regions where possible for better granularity.

    * Region codes should always be listed in alphabetical order.

    For grouped regions, keep the following rules in mind:

    * Only use grouped regions by themselves when a title is clearly intended for release
      in that broad area. For example, titles have often been released for Europe due to
      the PAL video standard, some other form of region locking, or because of the
      [level of English comprehension of the continent](https://europa.eu/eurobarometer/surveys/detail/2979).
      Digitally-distributed titles often have only one global version.

    * When using grouped regions, be aware that each can contain several individual
      regions that have vastly different languages, even _within_ those individual
      regions. It's not good enough to have a grouped region listed without its languages
      &mdash; just `ASI` (Asia) by itself tells us nothing about who the target audience
      is. Be extra diligent in adding all the supported languages for the title, even if
      this means testing to find out.

    * If you have more than two individual regions listed that belong to a grouped region,
      also add that grouped region. For example, if a title was released in France and
      Germany, it's also worth adding Europe: `["FR", "DE", "EUR"]`. Be aware that
      individual regions can be part of multiple grouped regions. For example, Türkiye is
      a melting pot of cultures at the intersection of Asia, Europe, and the Middle East.
      Mexico is part of North America, but also Latin America.

    The valid regions are as follows:

    /// tab | Individual regions

    <input type="text" id="language-filter" class="filter input" placeholder="Filter the list" title="Filter the list">

    <ul class="filter">
      <li><code>AF</code> - Afghanistan</li>
      <li><code>AX</code> - Åland Islands</li>
      <li><code>AL</code> - Albania</li>
      <li><code>DZ</code> - Algeria</li>
      <li><code>AS</code> - American Samoa</li>
      <li><code>AD</code> - Andorra</li>
      <li><code>AO</code> - Angola</li>
      <li><code>AI</code> - Anguilla</li>
      <li><code>AQ</code> - Antarctica</li>
      <li><code>AG</code> - Antigua and Barbuda</li>
      <li><code>AR</code> - Argentina</li>
      <li><code>AM</code> - Armenia</li>
      <li><code>AW</code> - Aruba</li>
      <li><code>AU</code> - Australia</li>
      <li><code>AT</code> - Austria</li>
      <li><code>AZ</code> - Azerbaijan</li>
      <li><code>BS</code> - Bahamas</li>
      <li><code>BH</code> - Bahrain</li>
      <li><code>BD</code> - Bangladesh</li>
      <li><code>BB</code> - Barbados</li>
      <li><code>BY</code> - Belarus</li>
      <li><code>BE</code> - Belgium</li>
      <li><code>BZ</code> - Belize</li>
      <li><code>BJ</code> - Benin</li>
      <li><code>BM</code> - Bermuda</li>
      <li><code>BT</code> - Bhutan</li>
      <li><code>BO</code> - Bolivia</li>
      <li><code>BQ</code> - Bonaire, Sint Eustatius and Saba</li>
      <li><code>BA</code> - Bosnia and Herzegovina</li>
      <li><code>BW</code> - Botswana</li>
      <li><code>BV</code> - Bouvet Island</li>
      <li><code>BR</code> - Brazil</li>
      <li><code>IO</code> - British Indian Ocean Territory</li>
      <li><code>BN</code> - Brunei  Darussalam</li>
      <li><code>BG</code> - Bulgaria</li>
      <li><code>BF</code> - Burkina Faso</li>
      <li><code>BI</code> - Burundi</li>
      <li><code>CV</code> - Cabo Verde</li>
      <li><code>KH</code> - Cambodia</li>
      <li><code>CM</code> - Cameroon</li>
      <li><code>CA</code> - Canada</li>
      <li><code>KY</code> - Cayman Islands</li>
      <li><code>CF</code> - Central African Republic</li>
      <li><code>TD</code> - Chad</li>
      <li><code>CL</code> - Chile</li>
      <li><code>CN</code> - China</li>
      <li><code>CX</code> - Christmas Island</li>
      <li><code>CC</code> - Cocos (Keeling) Islands</li>
      <li><code>CO</code> - Colombia</li>
      <li><code>KM</code> - Comoros</li>
      <li><code>CG</code> - Congo</li>
      <li><code>CD</code> - Congo, Democratic Republic of the</li>
      <li><code>CK</code> - Cook Islands</li>
      <li><code>CR</code> - Costa Rica</li>
      <li><code>CI</code> - Côte d'Ivoire</li>
      <li><code>HR</code> - Croatia</li>
      <li><code>CU</code> - Cuba</li>
      <li><code>CW</code> - Curaçao</li>
      <li><code>CY</code> - Cyprus</li>
      <li><code>CZ</code> - Czechia</li>
      <li><code>DK</code> - Denmark</li>
      <li><code>DJ</code> - Djibouti</li>
      <li><code>DM</code> - Dominica</li>
      <li><code>DO</code> - Dominican Republic</li>
      <li><code>EC</code> - Ecuador</li>
      <li><code>EG</code> - Egypt</li>
      <li><code>SV</code> - El Salvador</li>
      <li><code>GQ</code> - Equatorial Guinea</li>
      <li><code>ER</code> - Eritrea</li>
      <li><code>EE</code> - Estonia</li>
      <li><code>SZ</code> - Eswatini</li>
      <li><code>ET</code> - Ethiopia</li>
      <li><code>FK</code> - Falkland Islands</li>
      <li><code>FO</code> - Faroe Islands</li>
      <li><code>FJ</code> - Fiji</li>
      <li><code>FI</code> - Finland</li>
      <li><code>FR</code> - France</li>
      <li><code>GF</code> - French Guiana</li>
      <li><code>PF</code> - French Polynesia</li>
      <li><code>TF</code> - French Southern Territories</li>
      <li><code>GA</code> - Gabon</li>
      <li><code>GM</code> - Gambia</li>
      <li><code>GE</code> - Georgia</li>
      <li><code>DE</code> - Germany</li>
      <li><code>GH</code> - Ghana</li>
      <li><code>GI</code> - Gibraltar</li>
      <li><code>GR</code> - Greece</li>
      <li><code>GL</code> - Greenland</li>
      <li><code>GD</code> - Grenada</li>
      <li><code>GP</code> - Guadeloupe</li>
      <li><code>GU</code> - Guam</li>
      <li><code>GT</code> - Guatemala</li>
      <li><code>GG</code> - Guernsey</li>
      <li><code>GN</code> - Guinea</li>
      <li><code>GW</code> - Guinea-Bissau</li>
      <li><code>GY</code> - Guyana</li>
      <li><code>HT</code> - Haiti</li>
      <li><code>HM</code> - Heard Island and McDonald Islands</li>
      <li><code>VA</code> - Holy-See</li>
      <li><code>HN</code> - Honduras</li>
      <li><code>HK</code> - Hong Kong</li>
      <li><code>HU</code> - Hungary</li>
      <li><code>IS</code> - Iceland</li>
      <li><code>IN</code> - India</li>
      <li><code>ID</code> - Indonesia</li>
      <li><code>IR</code> - Iran, Islamic Republic of</li>
      <li><code>IQ</code> - Iraq</li>
      <li><code>IE</code> - Ireland</li>
      <li><code>IM</code> - Isle of Man</li>
      <li><code>IL</code> - Israel</li>
      <li><code>IT</code> - Italy</li>
      <li><code>JM</code> - Jamaica</li>
      <li><code>JP</code> - Japan</li>
      <li><code>JE</code> - Jersey</li>
      <li><code>JO</code> - Jordan</li>
      <li><code>KZ</code> - Kazakhstan</li>
      <li><code>KE</code> - Kenya</li>
      <li><code>KI</code> - Kiribati</li>
      <li><code>KP</code> - Korea, Democratic People's Republic of (North Korea)</li>
      <li><code>KR</code> - Korea, Republic of (South Korea)</li>
      <li><code>KW</code> - Kuwait</li>
      <li><code>KG</code> - Kyrgyzstan</li>
      <li><code>LA</code> - Lao People's Democratic Republic (Laos)</li>
      <li><code>LV</code> - Latvia</li>
      <li><code>LB</code> - Lebanon</li>
      <li><code>LS</code> - Lesotho</li>
      <li><code>LR</code> - Liberia</li>
      <li><code>LY</code> - Libya</li>
      <li><code>LI</code> - Liechtenstein</li>
      <li><code>LT</code> - Lithuania</li>
      <li><code>LU</code> - Luxembourg</li>
      <li><code>MO</code> - Macao</li>
      <li><code>MG</code> - Madagascar</li>
      <li><code>MW</code> - Malawi</li>
      <li><code>MY</code> - Malaysia</li>
      <li><code>MV</code> - Maldives</li>
      <li><code>ML</code> - Mali</li>
      <li><code>MT</code> - Malta</li>
      <li><code>MH</code> - Marshall Islands</li>
      <li><code>MQ</code> - Martinique</li>
      <li><code>MR</code> - Mauritania</li>
      <li><code>MU</code> - Mauritius</li>
      <li><code>YT</code> - Mayotte</li>
      <li><code>MX</code> - Mexico</li>
      <li><code>FM</code> - Micronesia, Federated States of</li>
      <li><code>MD</code> - Moldova, Republic of</li>
      <li><code>MC</code> - Monaco</li>
      <li><code>MN</code> - Mongolia</li>
      <li><code>ME</code> - Montenegro</li>
      <li><code>MS</code> - Montserrat</li>
      <li><code>MA</code> - Morocco</li>
      <li><code>MZ</code> - Mozambique</li>
      <li><code>MM</code> - Myanmar</li>
      <li><code>NA</code> - Namibia</li>
      <li><code>NR</code> - Nauru</li>
      <li><code>NP</code> - Nepal</li>
      <li><code>NL</code> - Netherlands, Kingdom of the</li>
      <li><code>NC</code> - New Caledonia</li>
      <li><code>NZ</code> - New Zealand</li>
      <li><code>NI</code> - Nicaragua</li>
      <li><code>NE</code> - Niger</li>
      <li><code>NG</code> - Nigeria</li>
      <li><code>NU</code> - Niue</li>
      <li><code>NF</code> - Norfolk Island</li>
      <li><code>MK</code> - North Macedonia</li>
      <li><code>MP</code> - Northern Mariana Islands</li>
      <li><code>NO</code> - Norway</li>
      <li><code>OM</code> - Oman</li>
      <li><code>PK</code> - Pakistan</li>
      <li><code>PW</code> - Palau</li>
      <li><code>PS</code> - Palestine, Sate of</li>
      <li><code>PA</code> - Panama</li>
      <li><code>PG</code> - Papua New Guinea</li>
      <li><code>PY</code> - Paraguay</li>
      <li><code>PE</code> - Peru</li>
      <li><code>PH</code> - Philippines</li>
      <li><code>PN</code> - Pitcairn</li>
      <li><code>PL</code> - Poland</li>
      <li><code>PT</code> - Portugal</li>
      <li><code>PR</code> - Puerto Rico</li>
      <li><code>QA</code> - Qatar</li>
      <li><code>RE</code> - Réunion</li>
      <li><code>RO</code> - Romania</li>
      <li><code>RU</code> - Russian Federation (Russia)</li>
      <li><code>RW</code> - Rwanda</li>
      <li><code>BL</code> - Saint Barthélemy</li>
      <li><code>SH</code> - Saint Helena, Ascension and Tristan da Cunha</li>
      <li><code>KN</code> - Saint Kitts & Nevis</li>
      <li><code>LC</code> - Saint Lucia</li>
      <li><code>PM</code> - Saint Pierre & Miquelon</li>
      <li><code>VC</code> - Saint Vincent and the Grenadines</li>
      <li><code>WS</code> - Samoa</li>
      <li><code>SM</code> - San Marino</li>
      <li><code>ST</code> - Sao Tome & Principe</li>
      <li><code>SA</code> - Saudi Arabia</li>
      <li><code>SN</code> - Senegal</li>
      <li><code>RS</code> - Serbia</li>
      <li><code>SC</code> - Seychelles</li>
      <li><code>SL</code> - Sierra Leone</li>
      <li><code>SG</code> - Singapore</li>
      <li><code>SX</code> - Sint Maarten (Dutch)</li>
      <li><code>MF</code> - Sint Maarten (French)</li>
      <li><code>SK</code> - Slovakia</li>
      <li><code>SI</code> - Slovenia</li>
      <li><code>SB</code> - Solomon Islands</li>
      <li><code>SO</code> - Somalia</li>
      <li><code>ZA</code> - South Africa</li>
      <li><code>GS</code> - South Georgia and the South Sandwich Islands</li>
      <li><code>SS</code> - South Sudan</li>
      <li><code>ES</code> - Spain</li>
      <li><code>LK</code> - Sri Lanka</li>
      <li><code>SD</code> - Sudan</li>
      <li><code>SR</code> - Suriname</li>
      <li><code>SJ</code> - Svalbard and Jan Mayen</li>
      <li><code>SE</code> - Sweden</li>
      <li><code>CH</code> - Switzerland</li>
      <li><code>SY</code> - Syrian Arab Republic (Syria)</li>
      <li><code>TW</code> - Taiwan, Province of China</li>
      <li><code>TJ</code> - Tajikstan</li>
      <li><code>TZ</code> - Tanzania, United Republic of</li>
      <li><code>TH</code> - Thailand</li>
      <li><code>TL</code> - Timor-Leste</li>
      <li><code>TG</code> - Togo</li>
      <li><code>TK</code> - Tokelau</li>
      <li><code>TO</code> - Tonga</li>
      <li><code>TT</code> - Trinidad and Tobago</li>
      <li><code>TN</code> - Tunisia</li>
      <li><code>TR</code> - Türkiye</li>
      <li><code>TM</code> - Turkmenistan</li>
      <li><code>TC</code> - Turks and Caicos Islands</li>
      <li><code>TV</code> - Tuvalu</li>
      <li><code>UG</code> - Uganda</li>
      <li><code>UA</code> - Ukraine</li>
      <li><code>AE</code> - United Arab Emirates</li>
      <li><code>GB</code> - United Kingdom of Great Britain and Northern Ireland</li>
      <li><code>UM</code> - United States Minor Outlying Islands</li>
      <li><code>US</code> - United States of America</li>
      <li><code>UY</code> - Uruguay</li>
      <li><code>UZ</code> - Uzbekistan</li>
      <li><code>VU</code> - Vanuatu</li>
      <li><code>VE</code> - Venezuela, Bolivarian Republic of</li>
      <li><code>VN</code> - Viet Nam (Vietnam)</li>
      <li><code>VG</code> - Virgin Islands (British)</li>
      <li><code>VI</code> - Virgin Islands (U.S.)</li>
      <li><code>WF</code> - Wallis and Futuna</li>
      <li><code>EH</code> - Western Sahara</li>
      <li><code>YE</code> - Yemen</li>
      <li><code>ZM</code> - Zambia</li>
      <li><code>ZW</code> - Zimbabwe</li>
    </ul>

    ///
    /// tab | Grouped regions
    * `GLO` - Global

    * `AFR` - Africa

    * `ASI` - Asia

    * `EUR` - Europe

    * `LAM` - Latin America

    * `MDE` - Middle East

    * `NAM` - North America

    * `NOR` - Nordics

    * `OCE` - Oceania

    * `SAM` - South America
    ///

    /// warning | Regions in graphical user interfaces
    These region codes are intended to keep the character count of the `regions` array,
    and therefore the file size, down. When building graphical user interfaces, opt to use
    full region names to keep it more accessible to users.
    ///

* **`languages`{ #languages .toc-code }** `object`{ .toc-def } `required`{ .toc-req }

    The supported languages for the title's `audio`, `interface`, and `subtitles`. If
    there are no audio, interface, or subtitle languages, add a singular `null` item to
    the relevant arrays:

    ``` {.json .copy}
    "languages": {
      "audio": [null],
      "interface": ["en"],
      "subtitles": [null]
    }
    ```

    If you don't know what languages are supported and aren't able to test to find out,
    leave the arrays empty. **This isn't recommended**. A sincere effort to catalog
    supported languages should be made &mdash; more data helps us all.

    ``` {.json .copy}
    "languages": {
      "audio": [],
      "interface": [],
      "subtitles": []
    }
    ```

    <h4>Constructing language codes</h4>

    Valid language codes are listed in the
    [IANA language subtag registry](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry).
    You can search for and validate a language code at
    [BCP47 language subtag lookup](https://r12a.github.io/app-subtags/). Here are some
    example codes:

    * `en` - English

    * `en-US` - English (United States of America)

    * `zh-Hant` - Chinese (Traditional) [written]

    * `cmn` - Chinese (Mandarin) [spoken]

    There are well over 9,000 subtags that can be combined in different ways to create a
    language code, so for page performance they're not listed here. It's also not sensible
    to include that much data in the schema validation, so validation needs to be done by
    the code generating the DAT file.

    To learn more about language codes, see the following pages:

    * [Language tags in HTML and XML](https://www.w3.org/International/articles/language-tags/)

    * [Choosing a language tag](https://www.w3.org/International/questions/qa-choosing-language-tags)

    * [Simplified vs. Traditional Chinese, and the Spoken Dialects](https://localization.blog/2022/10/10/simplified-vs-traditional-chinese-and-the-spoken-dialects/)
        (Chinese language codes differ for spoken vs written)

    <h4>Choosing languages</h4>

    In all circumstances, consider the intended audience of the medium when selecting
    language codes. For example, if a video is largely in English and is intended for
    English-speaking audiences, but has a short scene in which people speak Japanese, you
    set the `audio` as `["en"]`, _not_ `["en", "ja"]`.

    <h4>Order</h4>

    Language codes should always be listed in alphabetical order.

    <h4>Examples</h4>

    `Metal Gear Solid Integral (Japan)` on PlayStation has English audio, selectable
    English or Japanese subtitles, and a mix of English _and_ Japanese for the
    interface&mdash;where Japanese is used for weapon and item descriptions, and English
    for everything else. It's a weird mix, but it's definitely intended for Japanese
    audiences, so it's represented as follows:

    ``` {.json .copy}
    "languages": {
      "audio": ["en"],
      "interface": ["ja"],
      "subtitles": ["en", "ja"]
    }
    ```

    `Ghost in the Shell (France)` on PlayStation has cutscenes where the audio is in French,
    but the interface is in English, and there are no subtitles. This is represented as
    follows:

    ``` {.json .copy}
    "languages": {
      "audio": ["fr"],
      "interface": ["en"],
      "subtitles": [null]
    }
    ```

    /// details | Expand for developer details
    Certain combinations of language types tell us useful things. For example, a Japanese
    title with the following properties is completely playable by English speakers:

    ``` {.json .copy}
    "languages": {
      "audio": [null],
      "interface": ["en"],
      "subtitles": [null]
    }
    ```

    Consider these scenarios when building filters for DAT files.
    ///

    /// warning | Languages in graphical user interfaces
    These language codes are intended to keep the character count of the `languages`
    arrays, and therefore the file size, down. When building graphical user interfaces,
    opt to use full language names to keep it more accessible to users.
    ///

* **`sets`{ #sets .toc-code }** `object array`{ .toc-def } `required`{ .toc-req }

    Defines the different file sets within the title.
    [Read more about the `sets` array](sets.md).

</div>

## Optional properties

<div class="definition-list" markdown>

* **`build`{ #build .toc-code }** `enum`{ .toc-def } `optional`{ .toc-opt }

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

    * `Pre-alpha`: This includes early development titles and prototypes.

    * `Review`: A version of the title sent to reviewers. This can be production code,
      preproduction code, or have code in it that's unique to the reviewer copy.

    * `Preproduction`: A generic catch-all for a title that is at an unspecified
      development stage, but isn't the production version. Wherever possible, don't use
      this.

    If this property isn't present, the DAT application assumes the value is `Production`.

* **`contains`{ #contains .toc-code }** `object array`{ .toc-def } `optional`{ .toc-opt }

    Lists the content that this title contains. Useful for identifying the following:

    * The individual titles that make up a compilation.
    * The individual parts that go into game of the year or special editions.
    * The multiple CDs that are superceded by a DVD rerelease of the same title.

    <h4>Compilations</h4>

    The `contains` array must be paired with
    [`isCompilation: true`](titles.md#isCompilation) when describing compilations.

    Given the following compilation:

    ```text
    Some Video Game A + Some Video Game B + Some Video Game C (USA)
    ```

    The `contains` array might look like this:

    ``` {.json .copy}
    "contains": [
      {
        "name": "Some Video Game A (USA)",
        "groupId": "654321",
        "languages": {
          "audio": ["en"],
          "interface": ["en"],
          "subtitles": ["en"]
        },
        "version": "1.1",
        "versionInternal": "1"
      },
      {
        "name": "Some Video Game B (USA)",
        "groupId": "654322",
        "languages": {
          "audio": ["en"],
          "interface": ["en"],
          "subtitles": ["en"]
        },
        "version": "1.3",
        "versionInternal": "1"
      },
      {
        "name": "Some Video Game C (USA)",
        "languages": {
          "audio": ["en"],
          "interface": ["en"],
          "subtitles": ["en"]
        },
        "version": "1.0",
        "versionInternal": "1"
      }
    ]
    ```

    Each `contains` title has its own [`languages`](titles.md#languages) object, as
    individual titles within a compilation often have different language support.

    The `groupId` property links the constituent title in a compilation to the relevant
    group of standalone titles it belongs to, via its globally unique
    [`id`](collection.md#id). At comparison time during a 1G1R operation, a compilation is
    broken down into its constituent titles and compared against standalone titles. The
    title that's ultimately selected is up to user preference, whether that be to always
    keep the most recent version of a title, only keep compilations if they have unique
    titles, or otherwise.

    Where possible, the `version` and `internalVersion` properties should be consistent
    with the versioning of standalone titles. In this circumstance, it is okay to reuse a
    `versionInternal` value that has been used by an standalone title. For example, here's
    the `Some Video Game A (USA)` part of the `contains` array:

    ``` {.json .copy hl_lines="3"}
    {
      "name": "Some Video Game A (USA)",
      "groupId": "654321",
      "languages": {
        "audio": ["en"],
        "interface": ["en"],
        "subtitles": ["en"]
      },
      "version": "1.1",
      "versionInternal": "1"
    }
    ```

    And here's the relevant part of the standalone `Some Video Game A (USA)` entry in the
    DAT file:

    ``` {.json .copy hl_lines="3"}
    {
      "group": "Some Video Game",
      "id": "654321",
      "titles": [
        {
          "name": "Some Video Game A (USA)",
          "regions": ["US"],
          "languages": {
            "audio": ["en"],
            "interface": ["en"],
            "subtitles": ["en"]
          },
          "version": "1.1",
          "versionInternal": "1",
          ...
        }
      ]
    }
    ```

    Notice how the `version` and `versionInternal` fields match &mdash; this way we know
    the variant inside the compilation is exactly the same as the standalone title, and
    the DAT application will need to do more work to figure out what title to select
    during a 1G1R operation.

    The lack of `groupId` property for `Some Video Game C (USA)` indicates that this
    title is only found in the compilation. It's important to include these titles in
    the `contains` array, as it helps DAT applications to determine whether they should
    keep a compilation for its unique titles during 1G1R operations.

    <h4>Supersets</h4>

    The `contains` array must be paired with [`isSuperset: true`](titles.md#isSuperset)
    when describing supersets.

    Given the following superset:

    ```
    Some Video Game - Game of the Year Edition (USA)
    ```

    The `contains` array might look like this:

    ``` {.json .copy}
    "contains": [
      {
        "name": "Some Video Game (USA)",
        "includesIds": ["123456", "234567"]
      },
      {
        "name": "Add-ons",
        "includesIds": ["345678", "456789", "987654"],
      },
      {
        "name": "Updates",
        "includesIds": ["012345", "543210"]
      },
      {
        "name": "Extra content",
        "comments": ""
      }
    ]
    ```

    Where the original title, its DLC, and its updates are listed. Content that isn't
    found in an individual title is added as a `comment` to the `Extra content` object.

    The `includesIds` array lists the individual IDs of the titles, add-ons, and updates
    that are included in the superset. This includes all older versions of the title,
    add-ons, and updates that are no longer required because of this version.

    <h4>DVD releases</h4>


* **`developer`{ #developer .toc-code }** `string`{ .toc-def } `optional`{ .toc-opt }

    The developer of the title.

* **`id`{ #id .toc-code }** `string`{ .toc-def } `optional`{ .toc-opt }

    A globally unique ID for the title. Usually a database ID to ease lookups for DAT file
    maintainers. Might be referenced by a DAT application when finding dependencies for
    add-ons or updates, or when present in a [`containsId`](titles.md#containsId)
    property.

* **`isAlternate`{ #isAlternate .toc-code }** `boolean`{ .toc-def } `optional`{ .toc-opt }

    Whether the title is an alternate variant of a release.

    Where possible, don't use this. This is a generic property that doesn't tell the user
    what's different about a title compared to the original. Instead, classify the title
    with a property that provides more detail.

    If this property isn't present, the DAT application assumes the value is `false`.

* **`isCompilation`{ #isCompilation .toc-code }** `boolean`{ .toc-def } `optional`{ .toc-opt }

    Whether the title is a compilation. When used in combination with
    [`contains`](titles.md#contains), can be used by DAT applications to follow user
    preferences around keeping individual titles in preference of compilations, unless the
    compilation contains a unique title.

    Compilations live in their own groups, and shouldn't be grouped with their consituent
    titles.

    If this property isn't present, the DAT application assumes the value is `false`.

* **`isDemo`{ #isDemo .toc-code }** `boolean`{ .toc-def } `optional`{ .toc-opt }

    Whether the title is a demo.

    If this property isn't present, the DAT application assumes the value is `false`.

* **`isLicensed`{ #isLicensed .toc-code }** `boolean`{ .toc-def } `optional`{ .toc-opt }

    Whether the title was sanctioned for release by a platform manufacturer, assuming
    there was an approval process in place.

    If this property isn't present, the DAT application assumes the value is `true`.

* **`isMIA`{ #isMIA .toc-code }** `boolean`{ .toc-def } `optional`{ .toc-opt }

    Whether the title's digests have been verified by more than one person. If not, set
    the value to `true`.

    If this property isn't present, the DAT application assumes the value is `false`.

* **`isPirate`{ #isPirate .toc-code }** `boolean`{ .toc-def } `optional`{ .toc-opt }

    Whether the title contains stolen assets. Often a hack of an existing game that uses
    intellectual property from other games.

    If the value is `true`, [`islicensed`](titles.md#isUnlicensed) is considered `false`,
    regardless of its value in the DAT file.

    If this property isn't present, the DAT application assumes the value is `false`.

* **`isSuperset`{ #isSuperset .toc-code }** `boolean`{ .toc-def } `optional`{ .toc-opt }

    Whether the title contains more content than the original title, or for some reason
    is superior to another version. For example, game of the year editions, a regional
    variant with uncensored content, or a DVD version of a title previously released on
    multiple CDs.

    In 1G1R choices, supersets are selected above normal titles, so long as they fit the
    user's language priorities. Superset selection is _cross-regional_, meaning the
    following situation can arise:

    * The user preferences USA over Europe, and wants English only titles.

    * There are three titles available to choose from:

        * `Some Video Game (USA)`

        * `Some Video Game (Europe)`

        * `Some Video Game - Game of the Year Edition (Europe)`

    * Because `Some Video Game - Game of the Year Edition (Europe)` is in English, and is
      a superset, it gets selected even though the user preferenced USA titles over
      Europe.

    If this property isn't present, the DAT application assumes the value is `false`.

* **`localNames`{ #localNames .toc-code }** `object`{ .toc-def } `optional`{ .toc-opt }

    Local names given to the title, defined by language. Often titles are recorded in
    databases using their romanized form instead of their original name to aid with
    searching for the title. Other times a title can have multiple names, and what is
    displayed depends on the region of the machine on which it's running.

    The `localNames` object is where these names can be kept in their original form. DAT
    applications can then use this data to rename files according to a user's regional
    preferences.

    Keys should follow the language codes found in the
    [IANA language subtag registry](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry).
    See [`languages`](#languages) for more details about selecting a language code.

    The following is an example of the `localNames` array:

    ``` {.json .copy}
    "localNames": {
      "en": "Altered Beast",
      "ja": "獣王記"
    }
    ```

    Only use the title's name &mdash; don't include additional information like tags found
    in naming systems.

    If a title can show more than one name depending on the region, and the title
    [`name`](#name) is already in English, you should still include the English name in
    the `localNames` array. This is because client applications have no idea what language
    the title `name` is in, and so can't safely select it as the English name if someone
    sets that as a preference.

* **`peripherals`{ #peripherals .toc-code }** `enum array`{ .toc-def } `optional`{ .toc-opt }

    Contains inputs used to control the title, or devices that show output from the title.

    Names are as generic as possible, with a focus on mentioning if specialist devices are
    required for an ideal emulation experience.

    For example, trying to play _Guitar Hero_ with a standard controller is asking for a
    bad time, so it would be set to the following:

    ``` {.json .copy}
    "peripherals": [
      "Guitar"
    ]
    ```

    But playing almost any GameCube game with almost any controller through an emulator is
    perfectly fine, so they would generally be set to the following:

    ``` {.json .copy}
    "peripherals": [
      "Controller"
    ]
    ```

    For scenarios where titles are optimized for multiple inputs (for example, a racing
    game might be great with both controllers _and_ a steering wheel), add both:

    ``` {.json .copy}
    "peripherals": [
      "Controller",
      "Pedals",
      "Steering Wheel (Lock-to-lock)/Paddle"
    ]
    ```

    Valid values are the following:

    * `Controller`

    * `Controller with Touchpad`

    * `Controller with Trackball`

    * `Analog Joystick`

    * `Dance Pad`

    * `Digital Joystick`

    * `Digital Twin Sticks`

    * `Drums`

    * `EyeToy`

    * `Flight Stick`

    * `Guitar`

    * `HOTAS`

    * `Keyboard`

    * `Light Gun`

    * `Magnavox Odyssey Controller`

    * `Microphone`

    * `Microsoft Kinect`

    * `Microsoft Xbox Live Vision`

    * `Mouse`

    * `Nintendo Joy-Con`

    * `Nintendo Wii Balance Board`

    * `Nintendo Wii Remote`

    * `Nintendo Wii Remote and Nunchuk`

    * `Nintendo Power Glove`

    * `Pedals`

    * `Sega Dreamcast VMU`

    * `Sony EyeToy`

    * `Sony PlayStation Eye`

    * `Sony PlayStation Move`

    * `Sony Sixaxis`

    * `Spinner`

    * `Steering Wheel (Lock-to-lock)/Paddle`

    * `Steering Wheel (360°)`

    * `Touchscreen`

    * `Trackball`

    * `VR Headset`

    * `VR Headset and Controls`

* **`players`{ #players .toc-code }** `int`{ .toc-def } `optional`{ .toc-opt }

    The number of players the title supports. Might be paired with
    [`playModes`](#playModes).

* **`playModes`{ #playModes .toc-code }** `enum array`{ .toc-def } `optional`{ .toc-opt }

    The play modes the title supports. Valid values are the following:

    * `Single player`

    * `Co-op (Split-screen)`

    * `Co-op (Local)`

    * `Co-op (Remote)`

    * `Competitive (Split-screen Free-for-all)`

    * `Competitive (Split-screen Team)`

    * `Competitive (Local Free-for-all)`

    * `Competitive (Local Team)`

    * `Competitive (Remote Free-for-all)`

    * `Competitive (Remote Team)`

* **`published`{ #published .toc-code }** `bool`{ .toc-def } `optional`{ .toc-opt }

    Whether the title was published. Unpublished titles that didn't have an official
    release should be set to `false`.

    If this property isn't present, the DAT application assumes the value is `true`.

* **`publisher`{ #publisher .toc-code }** `string`{ .toc-def } `optional`{ .toc-opt }

    The publisher of the title.

* **`releaseDate`{ #releaseDate .toc-code }** `pattern string`{ .toc-def } `optional`{ .toc-opt }

    The date the title was released. Must be an
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) extended format date, without the
    time zone. Valid formats include the following:

    * `YYYY-MM-DD hh:mm:ss`

    * `YYYY-MM-DD hh:mm`

    * `YYYY-MM-DD`

    * `YYYY-MM`

    * `YYYY`

    /// details | Expand for developer details
    Valid dates are found with the following regular expressions:

    ``` {.text .copy}
    ^[1-9][0-9]{3,3}-(?:(?:0[469]|11)-(?:0[1-9]|1[0-9]|2[0-9]|30)|02-(?:0[1-9]|1[0-9]|2[0-9])|(?:0[13578]|10|12)-(?:0[1-9]|1[0-9]|2[0-9]|3[01])) (?:0[0-9]|1[0-9]|2[0-3]):(?:[0-5][0-9]:?){1,2}(?<!:)$
    ^[1-9][0-9]{3,3}-(?:(?:0[469]|11)-(?:0[1-9]|1[0-9]|2[0-9]|30)|02-(?:0[1-9]|1[0-9]|2[0-9])|(?:0[13578]|10|12)-(?:0[1-9]|1[0-9]|2[0-9]|3[01])) (?:0[0-9]|1[0-9]|2[0-3]):(?:[0-5][0-9])$
    ^[1-9][0-9]{3,3}-(?:(?:0[469]|11)-(?:0[1-9]|1[0-9]|2[0-9]|30)|02-(?:0[1-9]|1[0-9]|2[0-9])|(?:0[13578]|10|12)-(?:0[1-9]|1[0-9]|2[0-9]|3[01]))$
    ^[1-9][0-9]{3,3}-(?:0[1-9]|1[0-2])$
    ^[1-9][0-9]{3,3}$
    ```

    There's a lower year bound of 1000, and an upper year bound of 9999. The regular
    expressions also constrain month and date pairs appropriately, although it's possible
    to have February 29 on a non-leap year. It's assumed that systems generating the DAT
    file will generate valid dates to avoid this. The schema validation just enforces the
    format to enable easier programmatic comparisons when determining if one title is
    newer than another.
    ///

* **`serial`{ #serial .toc-code }** `string`{ .toc-def } `optional`{ .toc-opt }

    A manufacturer identifier for the title. Might be a cartridge serial, disc ring
    code, or otherwise.

* **`source`{ #source .toc-code }** `enum array`{ .toc-def } `optional`{ .toc-opt }

    The title's origin. Valid sources are:

    * `3.5\" floppy disk`

    * `5.25\" floppy disk`

    * `BD-ROM`

    * `BD-ROM (Ultra HD)`

    * `Cassette tape`

    * `CD-ROM`

    * `Device`

    * `Digital`

    * `DVD-ROM`

    * `Famicom Disk`

    * `GameCube Game Disc`

    * `Game Card`

    * `GD-ROM`

    * `Hard Drive`

    * `HD-DVD`

    * `HuCard`

    * `LaserDisc`

    * `Memory Card`

    * `ROM Card`

    * `ROM Cartridge`

    * `UMD`

    * `VHS`

    * `Wii Optical Disc`

    * `Wii U Optical Disc`

* **`subtype`{ #subtype .toc-code }** `enum`{ .toc-def } `optional`{ .toc-opt }

    The subtype of the title. Must be paired with a valid [`type`](#type).

    * `Add-on` - Valid with the `Application` and `Game` types.

    * `Audio` - Valid with the `Application` and `Game` types.

    * `Children` - Valid with the `Application`, `Audio`, `Game`, `Multimedia`, and `Video` types.

    * `Educational` - Valid with the `Application`, `Audio`, `Game`, `Multimedia`, and `Video` types.

    * `Manual` - Valid with the `Application`, `Device`, and `Game` types.

    * `Update` - Valid with the `Application` and `Game` types.

    * `Video` - Valid with the `Application` and `Game` types.

    For example:

    ``` {.json .copy}
    "type": "Game",
    "subtype": "Add-on"
    ```

* **`type`{ #type .toc-code }** `enum`{ .toc-def } `optional`{ .toc-opt }

    The type of the title. Must be one of the following:

    * `Application`

    * `Audio`

    * `BIOS`

    * `Chip`

    * `Coverdisc`

    * `Device`

    * `Firmware`

    * `Game`

    * `Magazine`

    * `Multimedia`

    * `Video`

    These can be paired with a [`subtype`](#subtype).

* **`version`{ #version .toc-code }** `string`{ .toc-def } `optional`{ .toc-opt }

    The version as reported by the title or media it came on. Don't include prefixes like
    `v`, or `Rev`, only include the version string itself.

    For example, don't use `Rev 1`, instead use `1`. Don't use `v1.1a`, instead use
    `1.1a`.

* **`versionInternal`{ #versionInternal .toc-code }** `int`{ .toc-def } `optional`{ .toc-opt }

    An integer-based version assigned by the DAT maintainer, so DAT applications don't
    have to parse multiple different versioning systems when making 1G1R decisions. This
    can also help fill the gap in 1G1R selection when the title's
    [`releaseDate`](titles.md#releaseDate) is unknown.

    The earliest release is set to `1`, with later releases increasing in value.

    The following rules apply:

    * The `versionInternal` is regional. That is, it only applies to, and is only compared
      against titles in the same region.

    * Don't assign the same number to multiple releases within the one region.

    * Numbering should start from the earliest available release, including preproduction.

    * If you don't know the release order, make your best guess. It's not ideal, but it
      means a 1G1R selection can actually happen.

    For example:

    ``` { .json .copy }
    ...
    "name": "Some Video Game (USA)",
    "versionInternal": 1,
    ...
    "name": "Some Video Game (USA) (v1.1)",
    "versionInternal": 2,
    ...
    "name": "Some Video Game (USA) (v1.2)",
    "versionInternal": 3,
    ...
    "name": "Some Video Game (Europe) (Beta)",
    "versionInternal": 1,
    ...
    "name": "Some Video Game (Europe)",
    "versionInternal": 2,
    ...
    "name": "Some Video Game - Game of the Year (Europe)",
    "versionInternal": 3,
    ...
    ```

    /// details | Expand for developer details
    This is an attempt to partially recreate how
    [Retool](https://unexpectedpanda.github.io/retool) sets up clone lists, while removing
    the need to write logic that figures out which titles are the oldest or newest. See
    [1G1R calculations](1g1r.md).
    ///

* **`videoStandards`{ #videoStandards .toc-code }** `enum array`{ .toc-def } `optional`{ .toc-opt }

    The video standard supported by the title. This describes a title's fixed output
    in both color and resolution, as opposed to any monitor standard that might be
    receiving the output.

    Use `RGB` for any title that supports higher resolutions than SVGA, and allows for
    flexible resolution output.

    Valid standards are:

    * `4K Ultra HD`

    * `8K Ultra HD`

    * `AX-VGA`

    * `CGA`

    * `EGA`

    * `EVGA`

    * `HGC`

    * `HDTV (720i)`

    * `HDTV (720p)`

    * `Full HDTV (1080i)`

    * `Full HDTV (1080p)`

    * `JEGA`

    * `MCGA`

    * `MDA`

    * `MPAL`

    * `NTSC`

    * `NTSC (DV) (480i)`

    * `NTSC (DV) (480p)`

    * `PAL`

    * `PAL (DV) (576i)`

    * `PAL (DV) (576p)`

    * `PAL 60Hz`

    * `PGC`

    * `Plantronics`

    * `Quadcolor`

    * `RGB`

    * `SECAM`

    * `SVGA`

    * `Tandy`

    * `TIGA`

    * `VGA`

    * `XGA`

</div>
