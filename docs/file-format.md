---
hide:
  - footer
---

# File formats and extensions

## File format

The new datafile format uses JSON. This is to be paired with a publicly available JSON
schema.

### Unsuitable formats

* JSONC and JSON5 offer useful extensions to the format (such as comments, trailing
  commas, and unquoted keys). However, standard JSON's ubiquity, speed, and availability
  of libraries is too hard to ignore.

* XML is capable, however, to mimic data structures like arrays and objects is incredibly
  verbose in terms of syntax, adding to file size. Although machines are doing almost all
  of the work here, JSON is arguably more human-readable.

* YAML becomes needlessly complex with large data structures, and is a
  [pain to parse](https://web.archive.org/web/20250121023136/https://ruudvanasseldonk.com/2023/01/11/the-yaml-document-from-hell).

* TOML gets unwieldy with deeply nested data.

## File extension

ROM managers already have to deal with multiple formats that use the extension `.dat`, and
the nomenclature of "DATs" or "DAT files" is widespread. The file extension remains `.dat`
for the new model.