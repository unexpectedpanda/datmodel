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

* **`is_demo`** (bool): _Required_. Whether the title is a demo.

* **`regions`** (enum array): _Required_. Which regions the title was released in. This is
    not intended to match the regional naming standards of DAT groups, as these differ.
    File names can remain unaltered to follow those regional naming standards.

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
    <div class="grid" markdown>
    <div>

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

    </div>
    <div>

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

    </div>
    </div>

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

* **`languages`** (object): _Required_. The supported languages for audio, the title's
  interface, and its subtitles. Languages are listed in
  [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) format, with
  appended two letter country codes where relevant. Some spoken or signed languages use
  [ISO 639-3](https://en.wikipedia.org/wiki/List_of_ISO_639-3_codes) codes.

    Languages are split up into audio, interface, and subtitles to handle odd
    language-selection scenarios.

    If there are no audio, interface, or subtitle languages, add a singular `null` item to
    the relevant arrays.

    The valid languages are as follows:

    <input type="text" id="language-filter" class="filter input" placeholder="Filter the list" title="Filter the list">

    <div class="grid filter" markdown>
      <div>
        <ul>
          <li><code>ab</code> - Abkhazain</li>
          <li><code>aa</code> - Afar</li>
          <li><code>af</code> - Afrikaans</li>
          <li><code>ak</code> - Akan</li>
          <li><code>sq</code> - Albanian</li>
          <li><code>am</code> - Amharic</li>
          <li><code>ase</code> - American Sign Language</li>
          <li><code>ar</code> - Arabic</li>
          <li><code>ar-DZ</code> - Arabic (Algeria)</li>
          <li><code>ar-BH</code> - Arabic (Bahrain)</li>
          <li><code>ar-EG</code> - Arabic (Egypt)</li>
          <li><code>ar-IQ</code> - Arabic (Iraq)</li>
          <li><code>ar-JO</code> - Arabic (Jordan)</li>
          <li><code>ar-KW</code> - Arabic (Kuwait)</li>
          <li><code>ar-LB</code> - Arabic (Lebanon)</li>
          <li><code>ar-LY</code> - Arabic (Libya)</li>
          <li><code>ar-MA</code> - Arabic (Morocco)</li>
          <li><code>ar-OM</code> - Arabic (Oman)</li>
          <li><code>ar-QA</code> - Arabic (Qatar)</li>
          <li><code>ar-SA</code> - Arabic (Saudi Arabia)</li>
          <li><code>ar-SY</code>- Arabic (Syria)</li>
          <li><code>ar-TN</code> - Arabic (Tunisia)</li>
          <li><code>ar-AE</code> - Arabic (UAE)</li>
          <li><code>ar-YE</code> - Arabic (Yemen)</li>
          <li><code>an</code>- Aragonese</li>
          <li><code>hy</code> - Armenian</li>
          <li><code>as</code> - Assamese</li>
          <li><code>asf</code> - Auslan, Australian Sign Language</li>
          <li><code>av</code> - Avaric</li>
          <li><code>ae</code> - Avestan</li>
          <li><code>ay</code> - Aymara</li>
          <li><code>az</code> - Azerbaijani</li>
          <li><code>bm</code> - Bambara</li>
          <li><code>ba</code> - Bashkir</li>
          <li><code>eu</code> - Basque</li>
          <li><code>be</code> - Belarusian</li>
          <li><code>bn</code> - Bengali</li>
          <li><code>bi</code> - Bislama</li>
          <li><code>bs</code> - Bosnian</li>
          <li><code>br</code> - Breton</li>
          <li><code>bg</code> - Bulgarian</li>
          <li><code>my</code> - Burmese</li>
          <li><code>ca</code> - Catalan</li>
          <li><code>ch</code> - Chamorro</li>
          <li><code>ce</code> - Chechen</li>
          <li><code>ny</code> - Chichewa</li>
          <li><code>yue</code> - Chinese (Cantonese)</li>
          <li><code>cmn</code> - Chinese (Mandarin)</li>
          <li><code>zh-Hans</code> - Chinese (Simplified)</li>
          <li><code>zh-Hant</code> - Chinese (Traditional)</code></li>
          <li><code>cv</code> - Chuvash</li>
          <li><code>kw</code> - Cornish</li>
          <li><code>co</code> - Corsican</li>
          <li><code>cr</code> - Cree</li>
          <li><code>hr</code> - Croatian</li>
          <li><code>cs</code> - Czech</li>
          <li><code>da</code> - Danish</li>
          <li><code>dv</code> - Divehi</li>
          <li><code>nl</code> - Dutch, Flemish</li>
          <li><code>dz</code> - Dzongkha</li>
          <li><code>en</code> - English</li>
          <li><code>en-AU</code> - English (Australia)</li>
          <li><code>en-BZ</code> - English (Belize)</li>
          <li><code>en-CA</code> - English (Canada)</li>
          <li><code>en-IE</code> - English (Ireland)</li>
          <li><code>en-JM</code> - English (Jamaica)</li>
          <li><code>en-NZ</code> - English (New Zealand)</li>
          <li><code>en-ZA</code> - English (South Africa)</li>
          <li><code>en-TT</code> - English (Trinidad)</li>
          <li><code>en-GB</code> - English (United Kingdom)</li>
          <li><code>en-US</code> - English (United States)</li>
          <li><code>eo</code> - Esperanto</li>
          <li><code>et</code> - Estonian</code></li>
          <li><code>ee</code> - Ewe</li>
          <li><code>fo</code> - Faroese</li>
          <li><code>fj</code> - Fijian</li>
          <li><code>fi</code> - Finnish</li>
          <li><code>fr</code> - French</li>
          <li><code>fr-BE</code> - French (Belgium)</li>
          <li><code>fr-CA</code> - French (Canada)</li>
          <li><code>fr-LU</code> - French (Luxembourg)</li>
          <li><code>fr-ch</code> - French (Switzerland)</li>
          <li><code>fy</code> - Frisian (Western)</li>
          <li><code>ff</code> - Fulah</li>
          <li><code>gd</code> - Gaelic (Scotland)</li>
          <li><code>gl</code> - Galician</li>
          <li><code>lg</code> - Ganda</li>
          <li><code>ka</code> - Georgian</li>
          <li><code>de</code> - German</li>
          <li><code>de-AT</code> - German (Austria)</li>
          <li><code>de-LI</code> - German (Liechtenstein)</li>
          <li><code>de-LU</code> - German (Luxembourg)</li>
          <li><code>de-CH</code> - German (Switzerland)</li>
          <li><code>el</code> - Greek</li>
          <li><code>kl</code> - Kalaallisut</li>
          <li><code>gn</code> - Guarani</li>
          <li><code>gu</code> - Gujarati</li>
          <li><code>hn</code> - Haitian</li>
          <li><code>ha</code> - Hausa</li>
          <li><code>he</code> - Hebrew</li>
          <li><code>hz</code> - Herero</li>
          <li><code>hi</code> - Hindi</li>
          <li><code>ho</code> - Hiri Motu</li>
          <li><code>hu</code> - Hungarian</li>
          <li><code>is</code> - Icelandic</li>
          <li><code>ig</code> - Igbo</li>
          <li><code>id</code> - Indonesian</li>
          <li><code>iu</code> - Inukitut</li>
          <li><code>ik</code> - Inupiaq</li>
          <li><code>ga</code> - Irish</li>
          <li><code>it</code> - Italian</li>
          <li><code>it-CH</code> - Italian (Switzerland)</li>
          <li><code>ja</code> - Japanese</li>
          <li><code>jv</code> - Javanese</li>
          <li><code>kn</code> - Kannada</li>
          <li><code>kr</code> - Kanuri</li>
          <li><code>ks</code> - Kashmiri</li>
          <li><code>kk</code> - Kazakh</li>
          <li><code>km</code> - Khmer (Central)</li>
          <li><code>ki</code> - Kikuyu</li>
        </ul>
      </div>
      <div>
        <ul class="filter-languages">
          <li><code>rw</code> - Kinyarwanda</li>
          <li><code>ky</code> - Kyrgyz</li>
          <li><code>kv</code> - Komi</li>
          <li><code>kg</code> - Kongo</li>
          <li><code>ko</code> - Korean</li>
          <li><code>kj</code> - Kuanyama</li>
          <li><code>ku</code> - Kurdish</li>
          <li><code>lo</code> - Lao</li>
          <li><code>la</code> - Latin</li>
          <li><code>lv</code> - Latvian</li>
          <li><code>li</code> - Limburgan</li>
          <li><code>ln</code> - Lingala</li>
          <li><code>lt</code> - Lithuanian</li>
          <li><code>lu</code> - Luba-Katanga</li>
          <li><code>lb</code> - Luxembourgish</li>
          <li><code>mk</code> - Macedonian</li>
          <li><code>mg</code> - Malagasy</li>
          <li><code>ms</code> - Malay</li>
          <li><code>ml</code> - Malayalam</li>
          <li><code>mt</code> - Maltese</li>
          <li><code>gv</code> - Manx</li>
          <li><code>mi</code> - Maori</li>
          <li><code>mr</code> - Marathi</li>
          <li><code>mh</code> - Marshallese</li>
          <li><code>mn</code> - Mongolian</li>
          <li><code>na</code> - Nauru</li>
          <li><code>nv</code> - Navajo</li>
          <li><code>nd</code> - Ndebele (North)</li>
          <li><code>nr</code> - Ndebele (South)</li>
          <li><code>ng</code> - Ndonga</li>
          <li><code>ne</code> - Nepali</li>
          <li><code>no</code> - Norwegian</li>
          <li><code>nb</code> - Norwegian (Bokmål)</li>
          <li><code>nn</code> - Norwegian (Nynorsk)</li>
          <li><code>oc</code> - Occitan</li>
          <li><code>oj</code> - Ojibwa</li>
          <li><code>or</code> - Oriya</li>
          <li><code>om</code> - Oromo</li>
          <li><code>os</code> - Ossetian</li>
          <li><code>pi</code> - Pali</li>
          <li><code>ps</code> - Pashto</li>
          <li><code>fa</code> - Persian, Farsi</li>
          <li><code>pl</code> - Polish</li>
          <li><code>pt</code> - Portuguese</li>
          <li><code>pt-BR</code> - Portuguese (Brazil)</li>
          <li><code>pa</code> - Punjabi</li>
          <li><code>qu</code> - Quechua</li>
          <li><code>ro</code> - Romanian</li>
          <li><code>rm</code> - Romansh</li>
          <li><code>rn</code>- Rundi</li>
          <li><code>ru</code> - Russian</li>
          <li><code>se</code> - Sami (Northern)</li>
          <li><code>sm</code> - Samoan</li>
          <li><code>sg</code> - Sango</li>
          <li><code>sa</code> - Sanskrit</li>
          <li><code>sc</code> - Sardinian</li>
          <li><code>sr</code> - Serbian</li>
          <li><code>sn</code> - Shona</li>
          <li><code>sd</code> - Sindhi</li>
          <li><code>si</code> - Sinhala</li>
          <li><code>sk</code> - Slovak</li>
          <li><code>sl</code> - Slovenian</li>
          <li><code>so</code> - Somali</li>
          <li><code>st</code> - Sotho (Southern)</li>
          <li><code>es</code> - Spanish</li>
          <li><code>es-AR</code> - Spanish (Argentina)</li>
          <li><code>es-BO</code> - Spanish (Bolivia)</li>
          <li><code>es-CL</code> - Spanish (Chile)</li>
          <li><code>es-CO</code> - Spanish (Colombia)</li>
          <li><code>es-CR</code> - Spanish (Costa Rica)</li>
          <li><code>es-DO</code> - Spanish (Dominican Republic)</li>
          <li><code>es-EC</code> - Spanish (Ecuador)</li>
          <li><code>es-SV</code> - Spanish (El Salvador)</li>
          <li><code>es-GT</code> - Spanish (Guatemala)</li>
          <li><code>es-HN</code> - Spanish (Honduras)</li>
          <li><code>es-XL</code> - Spanish (Latin America)</li>
          <li><code>es-MX</code> - Spanish (Mexico)</li>
          <li><code>es-NI</code> - Spanish (Nicaragua)</li>
          <li><code>es-PA</code> - Spanish (Panama)</li>
          <li><code>es-PY</code> - Spanish (Paraguay)</li>
          <li><code>es-PE</code> - Spanish (Peru)</li>
          <li><code>es-PR</code> - Spanish (Puerto Rico)</li>
          <li><code>es-UY</code> - Spanish (Uruguay)</li>
          <li><code>es-VE</code> - Spanish (Venezuela)</li>
          <li><code>su</code> - Sundanese</li>
          <li><code>sw</code> - Swahili</li>
          <li><code>ss</code> - Swati</li>
          <li><code>sv</code> - Swedish</li>
          <li><code>sv-FI</code> - Swedish (Finland)</code></li>
          <li><code>tl</code> - Tagalog</li>
          <li><code>ty</code> - Tahitian</li>
          <li><code>tg</code> - Tajik</li>
          <li><code>ta</code> - Tamil</li>
          <li><code>tt</code> - Tatar</li>
          <li><code>te</code> - Telugu</li>
          <li><code>th</code> - Thai</li>
          <li><code>bo</code> - Tibetan</li>
          <li><code>ti</code> - Tigrinya</li>
          <li><code>to</code> - Tonga</li>
          <li><code>tn</code> - Tswana</li>
          <li><code>tr</code> - Turkish</li>
          <li><code>tk</code> - Turkmen</li>
          <li><code>tw</code> - Twi</li>
          <li><code>ug</code> - Uighur</li>
          <li><code>uk</code> - Ukrainian</li>
          <li><code>ur</code> - Urdu</li>
          <li><code>uz</code> - Uzbek</li>
          <li><code>ve</code> - Venda</li>
          <li><code>vi</code> - Vietnamese</li>
          <li><code>wa</code> - Walloon</li>
          <li><code>cy</code> - Welsh</li>
          <li><code>wo</code> - Wolof</li>
          <li><code>xh</code> - Xhosa</li>
          <li><code>ii</code> - Yi (Sichuan)</li>
          <li><code>yi</code> - Yiddish</li>
          <li><code>yo</code> - Yoruba</li>
          <li><code>za</code> - Zhuang</li>
          <li><code>zu</code> - Zulu</li>
        </ul>
      </div>
    </div>


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