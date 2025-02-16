---
hide:
  - footer
---

# `collection`

The `collection` array lists all the titles in the DAT file. Related releases are grouped
together in a single object by naming a `group` and listing its `releases`. For example,
the group `Doom` might contain the releases `Doom (USA)`, `Doom (Europe)`, and `Doom
(Japan)`, along with their different versions. This helps with 1G1R calculations, and
replaces the antiquated parent/clone relationship in LogiqX DAT files.

At its most basic, the collection array looks something like the following example:

```json
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

The `collection` array contains one or more objects with the following elements:

* **`group`** (str): _Required_. The name of the group of related titles.

* [**`releases`**](releases.md) (array): _Required_. Contains objects that describe the
  details about each title that is associated with the group.