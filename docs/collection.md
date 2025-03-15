---
hide:
  - footer
---

# `collection`

The `collection` array contains all of the titles in the DAT file.

In the following example, required properties are highlighted. The values are for example
only.

``` {.json .copy hl_lines="3-7"}
"collection": [
  {
    "group": "Some Video Game",
    "titles": [
      {
        ...
      }
    ],
    "addOns": [
      {
        ...
      }
    ],
    "updates": [
      {
        ...
      }
    ]
  }
]
```

Related titles are grouped together in a single object by naming a `group` and listing
its `titles`. For example, the group `Some Video Game` might contain the following
titles:

* `Some Video Game (USA)`
* `Some Video Game (USA) (v1.1)`
* `Some Video Game (Europe)`
* `Some Video Game (Japan)`

Grouping in this way helps with 1G1R calculations, and replaces the parent/clone
relationships found in LogiqX DAT files.

## Required properties

<div class="definition-list" markdown>
* **`group`{ #group .toc-code }** `string`{ .toc-def } `required`{ .toc-req }

    The name of the group of related titles.

* **`titles`{ #titles .toc-code }** `object array`{ .toc-def } `required`{ .toc-req }.

    Contains objects that describe the details about each title that is associated with
    a group. [Read more about the titles array](titles.md).
</div>

## Optional properties

<div class="definition-list" markdown>

* **`addOns`{ #addOns .toc-code }** `object array`{ .toc-def } `optional`{ .toc-opt }

    The add-ons associated with titles. This includes DLC. Add-ons are at this level of
    the structure as they might be compatible with many variants of the `titles`.
    [Read more about the `addOns` array](addOns.md).

* **`updates`{ #updates .toc-code }** `object array`{ .toc-def } `optional`{ .toc-opt }

    The updates associated with titles. Updates are at this level of the structure as they
    might be compatible with many variants of the `titles`.
    [Read more about the `updates` array](updates.md).

</div>
