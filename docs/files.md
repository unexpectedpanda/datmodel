---
hide:
  - footer
---

# `files`

The `files` array contains objects that describe the files in a file set.

``` {.json .copy}
"files": [
  {
    "name": "Some Video Game (USA) (Track 1).bin",
    "size": 10000,
    "digests": {
      "crc32": "29edd0e3",
      "xxh3_128": "1a2bf3bb0a4cd3aa94bf08b1c269423e",
      "blake3": "c32da642c108dd42bc169dbe4094b96d4f638d2c7388fb18132429347955c7ec"
    }
  },
  {
    "name": "Some Video Game (USA) (Track 2).bin",
    "size": 1000,
    "digests": {
      "crc32": "872f5343",
      "xxh3_128": "b993a0619f896a101e786850967b3d90",
      "blake3": "74277af46089c2b15aea5b193bdecdd58a2992e47b00956c678a6c070225cb18"
    }
  },
  {
    "name": "Some Video Game (USA).cue",
    "size": 100,
    "digests": {
      "crc32": "987150b7",
      "xxh3_128": "b7bb3254808cfc06d899854a1b58bab0",
      "blake3": "fcbc02c56a9a5157255febeac2009a988ccd08863ff648d290fe973dffe7f88c"
    }
  }
]
```

## Definitions

<div class="definition-list" markdown>
* **`name`{ #name .toc-code }** `pattern string`{ .toc-def } `required`{ .toc-req }

    The name of the file, in UTF-8. Names can't end with a period or space, start with a
    path separator, or use the following invalid path characters:

    ```
    :<>"|?*\
    ```

    Path separators are represented Linux-style, with `/` instead of `\`. Don't use
    absolute paths, paths are relative to a path the user sets.

    /// details | Expand for developer details
    Invalid path characters are found with the following regular expression:

    ``` {.text .copy}
    ^[^:<>\"\\\\|?*].*[^. :<>\"\\\\|?*]$
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

* **`size`{ #size .toc-code }** `int`{ .toc-def } `required`{ .toc-req }

    The size of the file, in bytes.

* **`digests`{ #size .toc-code }** `object`{ .toc-def } `required`{ .toc-req }

    The digests of different hash functions. The object must contain at least one digest.
    The following hash functions are preferred:

    * **`crc32`** (pattern string): Still useful, as many container formats like ZIP
      record the CRC32 of their internal files without them needing to be extracted. This
      should only ever be used for initial validation of a file inside an archive, to see
      if it's worth extracting. The extracted file should still be tested with a more
      reliable hashing function to verify that it's the correct file. See the developer
      details for more information.

        /// details | Expand for developer details
        Valid CRC32 digests are found with the following regular expression:

        ```
        ^[a-fA-F0-9]{8,8}$
        ```

        Don't fall into the trap of thinking CRC32 + file size is enough to verify a file
        is the correct one. Here are four different files from the one archive,
        `segasp.zip`, in MAME:

        ```json hl_lines="2 4 12 14 22 24 32 34"
        "name": "fpr-24208a.ic72",
        "size": 2097152,
        "digests": {
          "crc32": "a738ea1c",
          "md5": "81abd9705b6ae17bd232b9fe96f12de8",
          "sha1": "3c32ddfb3c40be66b9fb2ba35fbfd5b534bb3da0",
          "sha256": "db9470c83a4b17cc7441b6fe6d824a1a6e299964a4a79bf8e5e6229fd542c120",
          "xxh3_128": "8c65f0bc5c3889a0f10d59de5125db4b",
          "blake3": "a850810cc35294c32c970870495d8f63a1328b8ea4d0c0ddef5c56daf76255c0"
        },
        "name": "fpr-24329.ic72",
        "size": 2097152,
        "digests": {
          "crc32": "a738ea1c",
          "md5": "7cf5e46dd564d3a88b4f7e24a1d57362",
          "sha1": "d0d062a4089a2d3404df45eb015faaf7eee9b8c2",
          "sha256": "85af02e76cde08f8ed4e02c7736af7c920157dbb7e7c5cf10606d457ae97b71c",
          "xxh3_128": "5b8d6afb1cc5d965bad5d626c760174c",
          "blake3": "109d5884b004dd828cf2f65be422ab75464a85847c92f74f43f3812e59fee340"
        },
        "name": "fpr-24407.ic72",
        "size": 2097152,
        "digests": {
          "crc32": "a738ea1c",
          "md5": "ec790069699b0312d3e374b17d1b7e20",
          "sha1": "fbcc3d119b47a6da4d194e3fe4a98126c7049edf",
          "sha256": "8fb1dadbc7e2a599cbcf30338c3a6e97ef24955cc0f2ceae781169ad8223cb59",
          "xxh3_128": "45bb3c0d4298a2472e94031d88318286",
          "blake3": "260827d650c68f62eccf207528f6f88bfa1be0088983ea1897bb3ac02c7883f0"
        },
        "name": "fpr-24407_123.ic72",
        "size": 2097152,
        "digests": {
          "crc32": "a738ea1c",
          "md5": "369b9634d187fd5cd28f09397a99359a",
          "sha1": "3f5a2fb03bbb1bd9af9fe32ad76a224c97aa9b7a",
          "sha256": "1979ae53d47e6bb52448623fb772d86ef997d8514b11955c41de6a09ee1913cb",
          "xxh3_128": "dae252a24f23999208cd945aded75f11",
          "blake3": "699a9cb452239bc4d678664a78351bb90a1a007a71c2a6974a77e09db2da5446"
        }
        ```
        ///

    * **`sha256`** (pattern string): Can be used for verifying untrusted files. SHA256
      should only be used by client applications if the user's processor supports hardware
      acceleration of the hashing function, or if no other digests are supplied.

        /// details | Expand for developer details
        Valid SHA256 digests are found with the following regular expression:

        ```
        ^[a-fA-F0-9]{64,64}$
        ```
        ///

    * **`xxh3_128`** (pattern string): Can be used for checksumming trusted files.

        /// details | Expand for developer details
        Valid XXH3 128 digests are found with the following regular expression:

        ```
        ^[a-fA-F0-9]{32,32}$
        ```
        ///

    * **`blake3`** (pattern string): Can be used for verifying untrusted files.

        /// details | Expand for developer details
        Valid BLAKE3 digests are found with the following regular expression:

        ```
        ^[a-fA-F0-9]{64,64}$
        ```
        ///

    The following hash functions should only be used in specific circumstances:

    * **`md5`** (pattern string): Legacy hashing function. Wherever possible, don't use
      this. The only permissable situation is if you're converting old DAT files that
      don't contain more reliable hashes, and don't possess the files yourself to rehash
      them with something better. Otherwise, replace with prejudice.

        /// details | Expand for developer details
        Valid MD5 digests are found with the following regular expression:

        ```
        ^[a-fA-F0-9]{32,32}$
        ```
        ///

    * **`sha1`** (pattern string): Can be used for verifying untrusted files, but prefer
      SHA256 or BLAKE3 where possible. SHA1 should only be used by client applications if
      the user's processor supports hardware acceleration of the hashing function, or if
      no other digests are supplied.

        /// details | Expand for developer details
        Valid SHA1 digests are found with the following regular expression:

        ```
        ^[a-fA-F0-9]{40,40}$
        ```
        ///

    * **`sha1_internal`** (pattern string): The internal SHA-1 used only for CHD files.

        /// details | Expand for developer details
        Valid SHA1 digests are found with the following regular expression:

        ```
        ^[a-fA-F0-9]{40,40}$
        ```
        ///

</div>
