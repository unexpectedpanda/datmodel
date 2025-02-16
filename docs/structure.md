---
hide:
  - footer
---

# Overview

The following sections include examples of DAT file structures. They are presented
piecemeal to help ease understanding. For a complete example of a valid DAT file, see
[Complete DAT file example](complete_example.md).

In code samples, `...` is used where data has been omitted for brevity and ease of
understanding. This omitted data might contain required information to validate
successfully against the [schema](schema.md).


The string `...` is not valid JSON and should not be
included in DAT files.

## Global rules

When creating DAT files, keep the following rules in mind:

* DAT files must be valid JSON.

* String values can't have leading or trailing whitespace.

## Top-level data

A DAT file at the top level looks like the following example:

```json
{
  "dat_info": {
    ...
  },
  "collection": [
    ...
  ]
}
```

The DAT file at the top level contains the following elements:

* **[`dat_info`](dat_info.md)** (object): _Required_: Contains information related to the
  DAT file and those who created it. It functions like a header for the file.

* **[`collection`](collection.md)** (array): _Required_: Lists all the titles in the DAT
  file.
