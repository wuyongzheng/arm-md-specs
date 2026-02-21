## 5.1 L1STD, Level 1 Stream Table Descriptor

The L1STD characteristics are:

Configures the base address and size of a second level Stream table for a range of StreamIDs.

L1STD is a 8-byte structure.

## Field descriptions

<!-- image -->

## Span, bits [4:0]

Size of Level 2 array and validity of L1STD.L2Ptr.

| Span   | Meaning                                                                         |
|--------|---------------------------------------------------------------------------------|
| 0      | L1STD.L2Ptr is invalid. The StreamIDs matching this descriptor are all invalid. |
| 1-11   | Level 2 array contains 2 (Span-1) STEs (1) .                                    |
| 12-31  | Reserved, behaves as 0.                                                         |

## Bit [5]

## Purpose

## Attributes

Reserved, RES0.

## L2Ptr, bits [55:6]

Pointer to the start of the Level-2 array.

Bits above the implemented OA size, reported in SMMU\_IDR5.OAS, are RES0.

Address bits above and below the field range are treated as 0.

Bits L2Ptr[N:0] are treated as 0 by the SMMU, where N == 5 + (Span -1) .

Note: The Level 2 array is therefore aligned to its size by the SMMU.

See section 3.4.3 Address sizes of SMMU-originated accesses for behavior of addresses beyond the OAS or physical address range.

5.1.

## Bits [63:56]

Reserved, RES0.

## 5.1.1 General properties of the L1STD

Incoming StreamIDs that select a descriptor with Span == 0, or a Span set to a Reserved value, or a Span set to an out of bounds value given the split point, or those that select a valid Level 1 descriptor but are outside of the level 2 range described by Span, are deemed invalid. A transaction causing a Stream table lookup that does not reach a valid STE is terminated with an abort to the client device and optionally records an event, see SMMU\_(*\_)CR2.RECINVSID and C\_BAD\_STREAMID.

When an L1STD is changed, the non-leaf form of CMD\_CFGI\_STE is the minimum scope of invalidation command required to invalidate SMMU caches of the L1STD entry. Depending on the change, other STE invalidations might be required, for example:

- Changing an inactive L1STD with Span == 0 to a non-zero active Span (introducing a new section of level-2 Stream table) requires an invalidation of the L1STD only. As no STEs were reachable for StreamIDs within the span, none require invalidation.
- Changing an active L1STD with Span != 0 to an inactive L1STD (decommissioning a span of Stream table) requires an invalidation of the L1STD as well as invalidation of cached STEs from the affected span. Either multiple non-leaf CMD\_CFGI\_STE commands, or a wider scope such as CMD\_CFGI\_STE\_RANGE or CMD\_CFGI\_ALL is required.