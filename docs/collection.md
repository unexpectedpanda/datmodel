---
hide:
  - footer
---

# `collection`

The `collection` array contains all of the titles in the DAT file.

In the following example, required properties are highlighted. The values are for example
only.

``` {.json .copy hl_lines="3 5-8"}
"collection": [
  {
    "group": "Some Video Game",
    "id": "654321",
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
    "supersets": [
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

* `Some Video Game (Europe)`
* `Some Video Game (Japan)`
* `Some Video Game (USA)`
* `Some Video Game (USA) (v1.1)`

The following updates:

* `Some Video Game (Europe) (Update v1.2)`
* `Some Video Game (Japan) (Update v1.1)`

The following add-ons:

* `Some Video Game - Expansion Pack (USA, Europe)`
* `Some Video Game - Expansion Pack (Japan)`

And the following superset:

* `Some Video Game - Game of the Year Edition (USA)`

Grouping in this way helps with 1G1R calculations, and replaces the parent/clone
relationships found in LogiqX DAT files.

## Required properties

<div class="definition-list" markdown>
* **`group`{ #group .toc-code }** `string`{ .toc-def } `required`{ .toc-req }

    The name of the group of related titles.

* **`titles`{ #titles .toc-code }** `object array`{ .toc-def } `required`{ .toc-req }.

    Contains objects that describe the details about each title that is associated with
    a group. [Read more about the `titles` array](titles.md).
</div>

## Optional properties

<div class="definition-list" markdown>

* **`addOns`{ #addOns .toc-code }** `object array`{ .toc-def } `optional`{ .toc-opt }

    The add-ons associated with titles. This includes DLC. Add-ons are at this level of
    the structure as they might be compatible with many variants of the `titles`.
    [Read more about the `addOns` array](addOns.md).

* **`id`{ #id .toc-code }** `string`{ .toc-def } `optional`{ .toc-opt }

    A globally unique ID for the group. Usually a database ID to ease lookups for DAT file
    maintainers. Might be referenced by a DAT application when matching compilations
    against individual titles using the [`contains`](titles.md#contains) array.

* **`supersets`{ #updates .toc-code }** `object array`{ .toc-def } `optional`{ .toc-opt }

    Contains objects that describe the details about supersets in the group. Supersets are
    variants of titles that contain more content, or for some reason are superior to
    another version. This might include, for example, a Game of the Year edition, an
    all-in-one pack that bundles a game and all its DLC, or a DVD version of a title
    previously released on multiple CDs.

    [Read more about the `supersets` array](supersets.md).

* **`updates`{ #updates .toc-code }** `object array`{ .toc-def } `optional`{ .toc-opt }

    The updates associated with titles. Updates are at this level of the structure as they
    might be compatible with many variants of the `titles`.
    [Read more about the `updates` array](updates.md).

</div>
