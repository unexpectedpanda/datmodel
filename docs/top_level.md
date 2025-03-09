---
hide:
  - footer
---

# Top level

A DAT file at the top level has minimal properties.

In the following example, required properties are highlighted.

``` {.json .copy hl_lines="2-7"}
{
  "datInfo": {
    ...
  },
  "collection": [
    ...
  ]
}
```

## Required properties

<div class="definition-list" markdown>
* **`datInfo`{ #datInfo .toc-code }** `object`{ .toc-def } `required`{ .toc-req }

    Contains information related to the DAT file and those who created it. It functions
    like a header for the file. [Read more about the `datInfo` object](datInfo.md).

* **`collection`{ #collection .toc-code }** `object array`{ .toc-def } `required`{ .toc-req }

    Lists all the titles in the DAT file.
    [Read more about the `collection` array](collection.md).
</div>
