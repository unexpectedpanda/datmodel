---
hide:
  - footer
---

# Goals, non-goals, and risks

## Goals

* A data format that provides additional metadata for enhanced functionality in the client
  software that processes it. This functionality includes:

    * Improved filtering and 1G1R processing.

    * Grouping multiple discs together that belong to the same release.

    * Linking common discs between different releases.

    * Grouping updates and addons (including DLC) with the releases they can be validly
      applied to.

* A shift away from ROM nomenclature towards general file management language.

* Improvements in data validation, which take into account the following:

    * More rigid enforcement of standards, to make data comparison easier.

    * Updates to standards due to world and technology changes, and a need for higher
      accuracy.

* A completed schema published in a public repository, alongside an updated version of
  this documentation to account for changes during the development process.

## Non-goals

* This proposal doesn't cover MAME, which continues to run its own race.

* This proposal doesn't seek to alter file naming standards put in place by DAT groups.
  However, its validation might be looser or more restrictive than a given naming standard
  depending on the particular field. For example, the ancient [No-Intro
  guidelines](https://datomatic.no-intro.org/stuff/The%20Official%20No-Intro%20Convention%20(20071030).pdf)
  insist on 7&#8209;bit ASCII in file names, while this DAT schema allows for the now
  ubiquitous UTF&#8209;8.

* Metadata that can't be used to manage or filter files, for example primary volume
  descriptors, isn't included in the standard. Managing this sort of metadata is up to the
  individuals or groups that release DAT files to store and distribute how they choose.

* It's tempting to define a standard that can enable client software to handle complex
  nested containers, and container conversion. For example:

    * Build a RAR archive from constituent files, then place that RAR inside a ZIP
      archive, and then along with other files and predefined partitions build everything
      into the final ISO file.

    * Convert an ISO file to CHD and vice versa.

    This capability is particularly appealing to those who seek to maximise available disk
    space, minimize file duplication, and enable virtual file systems that can
    transparently construct final containers when required.

    However, image file formats often have origin-specific configurations despite
    identical file extensions, compressed containers can be non-deterministic, and even
    deterministic containers can change their output between version and setting changes.
    There's also a dearth of cross-language libraries available for developers to
    integrate into their own DAT management software, whether that be parsing or
    creating DAT files.

    This functionality is therefore considered out of scope, and is more appropriately
    left to an external party who reverse-engineers the extraction of containers listed
    in a DAT file into their own, more detailed DAT files.

## Risks

* The complexity of the new format requires significant work in terms of the following:

    * Building appropriate interfaces to input data, paired with appropriate validation to
      ensure the output matches the schema.

    * Writing code to generate, parse, and make use of the data in the DAT files.

    Due to the organic nature of how the existing standard arose over time, it's likely
    that inertia in retaining the old format will be difficult to overcome.
