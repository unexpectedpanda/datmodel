---
hide:
  - footer
---

# `dat_info`

The `dat_info` object contains information related to the DAT file and those who created
it. It functions like a header for the file.

```json
"dat_info": {
  "schema": "https://www.github.com/unexpectedpanda/datmodel",
  "name": "Company - Console",
  "source": "Release group",
  "source_url": "https://www.example.com",
  "version": "1.1.1",
  "date": "2025-12-30 13:23:54",
  "contributors": ["Contributor 1", "Contributor 2", "Contributor 3"],
  "comments": "Created with magic DAT generator 2.3.1"
}
```

The `dat_info` object contains the following elements:

* **`name`** (string): _Required_. The name of the DAT file. This is usually something
  that describes the scope of content covered by the file. For example, a platform
  (`Sony - PlayStation`), a curated collection (`ExoDOS`), a theme (`Adventure games`), or
  otherwise. This name is shown in client software to tell the end user what file they're
  working with, and to manage updates to the file.

* **`source`** (string): _Required_. The origin of the DAT file, whether that be a group
  or individual.

* **`source_url`** (string): _Optional_. The website of the source. For example,
  `https://www.example.com`.

* **`version`** (pattern string): _Optional_. The version of the DAT file. For example,
  `1.1.1`. The version must be a [semantic version](https://semver.org/).

    Validated with the following regular expression:

    ```
    ^(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)(?:-((?:0|[1-9][0-9]*|[0-9]*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9][0-9]*|[0-9]*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?:[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$
    ```

* **`date`** (pattern string): _Required_. When the DAT file was created. Must be an
  [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) extended format date, without the
  time zone (`YYYY-MM-DD hh:mm:ss`). For example: `2025-12-30 23:01:05`.
    * Time uses 24-hour syntax.
    * Hours, minutes, and seconds are always double digit, and use leading zeros where
      appropiate.

    Validated with the following regular expression:

    ```
    ^[2-9][0-9]{3,3}-(?:(?:0[469]|11)-(?:0[1-9]|1[0-9]|2[0-9]|30)|02-(?:0[1-9]|1[0-9]|2[0-9])|(?:0[13578]|10|12)-(?:0[1-9]|1[0-9]|2[0-9]|3[01])) (?:0[0-9]|1[0-9]|2[0-3]):(?:[0-5][0-9]:?){1,2}(?<!:)$
    ```

    There's a lower year bound of 2000, and an upper year bound of 9999. The regular
    expression also constrains month and date pairs appropriately, although it's possible
    to have February 29 on a non-leap year. It's assumed that systems generating the DAT
    file will generate valid dates to avoid this. The validation just enforces the format
    to enable easier programmatic comparisons when determining if one DAT file is newer
    than another.

* **`contributors`** (string array): _Optional_. When multiple individuals or groups have
  contributed to the data contained in the DAT file, they are listed here.

* **`comments`**: (string): _Optional_. Relevant comments about the DAT file. For example,
  compression settings used, or other things users should know about.

/// note | ROM manager flags
Unlike the LogiqX DAT standard, flags for specific ROM managers aren't required. Relevant
metadata to implement that functionality is provided at the `releases` level.
///