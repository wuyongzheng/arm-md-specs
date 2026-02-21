## 5.3 L1CD, Level 1 Context Descriptor

The L1CD characteristics are:

Configures the base address of a second level CD table for a range of SubstreamIDs.

L1CD is a 8-byte structure.

## Field descriptions

<!-- image -->

When stage 1 is enabled and substreams are enabled and two-level Context Descriptor tables are in use (STE.S1Fmt != 0b00 ), the stage 1 context pointer indicates an array of Level 1 Context Descriptors which contain pointers to Level 2 CD tables.

## V, bit [0]

## Bits [11:1]

## Purpose

## Attributes

Valid.

| V   | Meaning                                                        |
|-----|----------------------------------------------------------------|
| 0b0 | L2Ptr invalid                                                  |
| 0b1 | L2Ptr valid - CDs are indexed through to the next level table. |

Reserved, RES0.

## L2Ptr, bits [55:12]

Pointer to next-level table.

Bits above the implemented OA size, reported in SMMU\_IDR5.OAS, are RES0.

Address bits above and below the field range are treated as zero.

The programmed value must be in the range of the IAS if stage 2 is enabled for the stream causing a CD fetch through this descriptor, or in the range of the OAS if stage 2 is not enabled for the stream.

See section 3.4.3 Address sizes of SMMU-originated accesses for behavior of addresses beyond IPA or PA address range.

## Bits [63:56]

Reserved, RES0.

## 5.3.1 General properties of the L1CD

If a CD fetch for a transaction with SubstreamID encounters an L1CD with V == 0, L2Ptr is IGNORED, the transaction is terminated with abort and a C\_BAD\_SUBSTREAMID event is recorded.

See the invalidation examples for L1STD in section 5.1 Level 1 Stream Table Descriptor. When an L1CD is changed, the non-leaf form of CMD\_CFGI\_CD is the minimum scope of invalidation command required to invalidate SMMU caches of the L1CD entry. Depending on the change, other CD invalidations might be required, for example:

- Changing an inactive L1CD with V == 0 to an active V == 1 form (introducing a new section of level-2 CD table) requires an invalidation of the L1CD only. Because no CDs were reachable for SubstreamIDs within the span, none require invalidation. A CMD\_CFGI\_CD can be used with Leaf == 0 and any SubstreamID that matches the L1CD entry.
- Changing an active L1CD with V == 1 to an inactive L1CD (decommissioning a span of SubstreamIDs) requires an invalidation of the L1CD as well as invalidation of cached CDs from the affected span. Either multiple non-leaf CMD\_CFGI\_CD commands, or a wider scope such as CMD\_CFGI\_CD\_ALL, CMD\_CFGI\_STE or CMD\_CFGI\_ALL is required.

See also the CD notes in Section 5.4.1 CD notes . An L1CD can be cached multiple times for the same reason as a single CD can be cached multiple times if accessed through multiple StreamIDs. This situation requires an invalidation procedure covering multiple StreamIDs.