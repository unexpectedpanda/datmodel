---
hide:
  - footer
---

# Goals, non-goals, and risks

## Goals

* A data format that provides enough metadata for enhanced functionality in the client
  software that processes it.

* A shift away from ROM nomenclature towards general file management language.

* Improvements in data validation, which take into account the following:

    * More rigid enforcement of standards, to make data comparison easier.

    * Expansion and changes to standards to take into account world changes, technology
      changes, changes to how titles are distributed, and more accurate definitions.

* After the new DAT standard is complete, publish its schema in a public repository,
  alongside an updated version of this documentation.

## Non-goals

* This proposal doesn't cover MAME, which continues to be a special case due to its unique
  needs.

* This proposal doesn't seek to alter file naming standards put in place by DAT groups,
  but it does standardize and validate fields that they might have set as free text, or
  have not considered, which in turn might impact naming decisions.

* Metadata that can't be used to manage files isn't included in the standard. Managing
  this metadata is up to the individuals or groups that release DAT files. They might
  choose, for example, to export an expanded DAT format that includes all of their
  additional fields for the sake of open data, however these expanded fields aren't
  covered by the schema.

* It's tempting to define a standard that can enable client software to handle complex
  nested containers, and container conversion. For example:

    * Build a RAR archive from constituent files, then place that RAR inside a ZIP
      archive, and then along with other files and predefined partitions build everything
      into the final ISO file.

    * Convert an ISO file to CHD and vice versa.

    This capability is particularly appealing to those who seek to maximise available disk
    space, minimize file duplication, and enable virtual file systems that can
    transparently construct final containers when required. It's a nifty idea.

    However, image file formats often have origin-specific configurations despite
    identical file extensions, compressed containers can be non-deterministic, and even
    deterministic containers can change their output between version and setting changes.
    It requires a huge amount of data to be recorded and handled.

    Adding this functionality is too much burden on those creating the DAT files, and the
    developers who need to support them. This functionality is therefore considered out of
    scope, and is more appropriately left to an external party who reverse-engineers the
    expansion of the final containers detailed in DAT files.

## Risks

* The necessary complexity required to enable new functionality might prevent client
  software authors and database maintainers into adopting the new format.