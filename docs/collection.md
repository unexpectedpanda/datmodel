---
hide:
  - footer
---

# `collection`

The `collection` array lists all the titles in the DAT file. Related releases are grouped
together in a single object by naming a `group` and listing its `releases`. For example,
the group `Some Video Game` might contain the following releases:

* `Some Video Game (USA)`
* `Some Video Game (USA) (v1.1)`
* `Some Video Game (Europe)`
* `Some Video Game (Japan)`

Grouping in this way helps with 1G1R calculations, and replaces the parent/clone
relationships found in LogiqX DAT files.

At its most basic, the collection array looks something like the following example:

``` {.json .copy}
"collection": [
  {
    "group": "Some Video Game",
    "releases": [
      {
        ...
      }
    ]
  }
]
```

## Definitions

<div class="definition-list" markdown>
* **`group`{ #group .toc-code }** `string`{ .toc-def } `required`{ .toc-req }

    The name of the group of related releases.

* **`releases`{ #releases .toc-code }** `object array`{ .toc-def } `required`{ .toc-req }.

    Contains objects that describe the details about each release that is associated with
    a group. [Read more about the releases array](releases.md).
</div>
