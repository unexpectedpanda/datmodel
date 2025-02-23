---
hide:
  - footer
---

# Top level

A DAT file at the top level looks like the following example:

``` {.json .copy}
{
  "dat_info": {
    ...
  },
  "collection": [
    ...
  ]
}
```

## Definitions

<div class="definition-list" markdown>
* **`dat_info`{ #dat_info .toc-code }** `object`{ .toc-def } `required`{ .toc-req }

    Contains information related to the DAT file and those who created it. It functions
    like a header for the file. [Read more about the `dat_info` object](dat_info.md).

* **`collection`{ #collection .toc-code }** `array`{ .toc-def } `required`{ .toc-req }

    Lists all the titles in the DAT file.
    [Read more about the `collection` array](collection.md)
</div>
