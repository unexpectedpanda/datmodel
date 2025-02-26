---
hide:
  - footer
---

# `releases`

The `releases` array contains objects that describe the details about each release that is
associated with a group.

``` {.json .copy}
"releases": [
  {
    "name": "Some Video Game (USA)",
    "build": "Production",
    "published": true,
    "type": "Game",
    "release_date": "1993-10-12",
    "regions": ["JP"],
    "languages": {
      "audio": ["ja", "en"],
      "interface": ["en"],
      "subtitles": ["en"]
    },
    "sets": [
      ...
    ]
  }
]
```

## Definitions

<div class="definition-list" markdown>
* **`name`{ #name .toc-code }** `string`{ .toc-def } `required`{ .toc-req }

    The name of the title, in UTF-8. This is used for the name of the archive or folder.
    Names can't end with a period or space, or use the following invalid path characters:

    ```
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

* **`build`{ #build .toc-code }** `enum`{ .toc-def } `required`{ .toc-req }

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

* **`published`{ #published .toc-code }** `bool`{ .toc-def } `required`{ .toc-req }

    Whether the title was published. Unpublished titles that didn't have an official
    release should be set to `false`.

* **`type`{ #type .toc-code }** `enum`{ .toc-def } `required`{ .toc-req }

    The type of release. Must be one of the following:

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

* **`release_date`{ #release_date .toc-code }** `pattern string`{ .toc-def } `required`{ .toc-req }

    The date the title was released. Must be an
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) extended format date, without the
    time zone. Valid formats include the following:

    * `YYYY-MM-DD hh:mm:ss`
    * `YYYY-MM-DD hh:mm`
    * `YYYY-MM-DD`
    * `YYYY-MM`
    * `YYYY`

    Leave the field empty for an unknown date:

    ```json
    "release_date": ""
    ```

    /// details | Expand for developer details
    Valid dates are found with the following regular expressions:

    ``` {.text .copy}
    ^[1-9][0-9]{3,3}-(?:(?:0[469]|11)-(?:0[1-9]|1[0-9]|2[0-9]|30)|02-(?:0[1-9]|1[0-9]|2[0-9])|(?:0[13578]|10|12)-(?:0[1-9]|1[0-9]|2[0-9]|3[01])) (?:0[0-9]|1[0-9]|2[0-3]):(?:[0-5][0-9]:?){1,2}(?<!:)$
    ^[1-9][0-9]{3,3}-(?:(?:0[469]|11)-(?:0[1-9]|1[0-9]|2[0-9]|30)|02-(?:0[1-9]|1[0-9]|2[0-9])|(?:0[13578]|10|12)-(?:0[1-9]|1[0-9]|2[0-9]|3[01])) (?:0[0-9]|1[0-9]|2[0-3]):(?:[0-5][0-9])$
    ^[1-9][0-9]{3,3}-(?:(?:0[469]|11)-(?:0[1-9]|1[0-9]|2[0-9]|30)|02-(?:0[1-9]|1[0-9]|2[0-9])|(?:0[13578]|10|12)-(?:0[1-9]|1[0-9]|2[0-9]|3[01]))$
    ^[1-9][0-9]{3,3}-(?:0[1-9]|1[0-2])$
    ^[1-9][0-9]{3,3}$
    ^$
    ```

    There's a lower year bound of 1000, and an upper year bound of 9999. The regular
    expressions also constrain month and date pairs appropriately, although it's possible
    to have February 29 on a non-leap year. It's assumed that systems generating the DAT
    file will generate valid dates to avoid this. The schema validation just enforces the
    format to enable easier programmatic comparisons when determining if one release is
    newer than another.
    ///

* **`regions`{ #regions .toc-code }** `enum array`{ .toc-def } `required`{ .toc-req }

    Which regions the title was released in. Valid individual region codes are two
    characters long, and are described in
    [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). Grouped
    regions are three characters long, and defined entirely by this standard.

    The following general rules apply:

    * If you don't know where a release is from, use an empty array:

        ```json
        "regions": []
        ```

    * If you do know where a release is from, prefer listing individual regions over
      grouped regions where possible for better granularity.

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

    Defines the different file sets within the release.

    For a more detailed explanation of how the `sets` array works, see [`sets`](sets.md).

</div>

## Optional parameters

<div class="definition-list" markdown>
* **`subtype`{ #subtype .toc-code }** `enum`{ .toc-def } `optional`{ .toc-opt }

    The subtype of the release. Must be paired with a valid [`type`](#type).

    * `Add-on` - Valid with the `Game` and `Application` types.

    * `Audio` - Valid with the `Game` and `Application` types.

    * `Demo` - Valid with the `Game` and `Application` types.

    * `Manual` - Valid with the `Device`, `Game`, and `Application` types.

    * `Update` - Valid with the `Game`, and `Application` types.

    * `Video` - Valid with the `Game` and `Application` types.

    For example:

    ``` {.json .copy}
    "type": "Game",
    "subtype": "Add-on"
    ```
</div>

---

* **`size`** (integer): _Required_. The size of the file, in bytes.

* **`digests`** (string): _Required_. This object contains the digests of different hash functions. It must have at
  least one digest. The following hash functions are accepted:

    * **`crc32`** (string):

---

At its most complex with all the optional data though, it can seem daunting:

```json
"releases": [
  {
    "name": "Some Video Game (Japan)",
    "db_id": "123456789",
    "build": "Production",
    "serial": null,
    "source": ["3.5\" floppy"],
    "local_names": {
      "ja": "別のビデオゲーム"
    },
    "regions": ["Japan"],
    "languages": {
      "audio": ["ja", "en"],
      "subtitles": ["en"]
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
            "subtitles": ["en"]
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
