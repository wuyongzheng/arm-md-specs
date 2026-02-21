## 5.2 STE, Stream Table Entry

The STE characteristics are:

## Purpose

## Attributes

Configuration structure for each stream, including:

- Whether traffic from the device is permitted.
- Whether it is subject to stage 1 translation.
- Whether it is subject to stage 2 translation, and the relevant translation tables.
- Which data structures locate translation tables for stage 1.

STE is a 64-byte structure.

## Field descriptions

<!-- image -->

## V, bit [0]

STE fields follow the convention of an S1 prefix for fields related to stage 1 translation, an S2 prefix for fields relating to stage 2 translation, and neither for fields unrelated to a specific translation stage.

In a valid STE, that is where STE.V == 1:

- All fields with an S2 prefix (with the exception of S2VMID) are IGNORED when stage 2 bypasses translation STE.Config == 0b10x .
- All fields with an S1 prefix are IGNORED when stage 1 bypasses translation (STE.Config == 0b1x0 ).

The validity conditions in field descriptions are written with the assumption that the field is not IGNORED because of a disabled stage of translation.

Note: Additionally, the validity check of STE.EATS might assert that STE.S2S == 0 even if stage 2 is in bypass. That is STE.S2S is not IGNORED.

All undefined fields, and some defined fields where explicitly noted, are permitted to take RAZ/WI behavior in an Embedded Implementation (EI) providing internal storage for Stream Table Entries, see section 3.16 Embedded Implementations . Permitted differences for such an embedded implementation that does not store STEs in regular memory are marked EI in this section.

Note: This allows such implementations to avoid storing bits that do not affect the SMMU behavior.

Invalid or contradictory configurations are marked ILLEGAL in field descriptions. Use of an ILLEGAL STE behaves as described for STE.V == 0.

## STE Valid.

| V   | Meaning                                                             |
|-----|---------------------------------------------------------------------|
| 0b0 | Structure contents are invalid. Other STE fields are IGNORED.       |
| 0b1 | Structure contents are valid. Other STE fields behave as described. |

Care must be taken when updating an STE when this field is 1 as updates might race against SMMU fetching the structure, see section 3.21 Structure access rules and update procedures .

Device transactions that select an STE with this field configured to 0 are terminated with an abort reported back to the device and a C\_BAD\_STE event is recorded.

ATS Translation Requests that select an STE with this field configured to 0 are immediately completed with CA status. No event is recorded.

If SMMU\_CR0.ATSCHK == 1, ATS Translated transactions are checked against STE configuration. Those selecting an invalid STE (with ILLEGAL configuration, or this field configured to 0) are terminated with an abort reported back to the device. No event is recorded. See 3.9 Support for PCI Express, PASIDs, PRI, and ATS for more information on ATS-related transactions.

## Config, bits [3:1]

Stream configuration.

| Value   | Traffic can pass?   | Stage 1   | Stage 2   | Notes                                      |
|---------|---------------------|-----------|-----------|--------------------------------------------|
| 0b000   | No                  | -         | -         | Report abort to device, no event recorded. |
| 0b0xx   | No                  | -         | -         | Reserved (behaves as 0b000 )               |
| 0b100   | Yes                 | Bypass    | Bypass    | STE.EATS value effectively 0b00            |

| Value   | Traffic can pass?   | Stage 1   | Stage 2   | Notes              |
|---------|---------------------|-----------|-----------|--------------------|
| 0b101   | Yes                 | Translate | Bypass    | S1* valid          |
| 0b110   | Yes                 | Bypass    | Translate | S2* valid          |
| 0b111   | Yes                 | Translate | Translate | S1* and S2* valid. |

If stage 1 is not implemented (SMMU\_IDR0.S1P == 0), it is ILLEGAL to set STE.Config == 0b1x1 .

If stage 2 is not implemented (SMMU\_IDR0.S2P == 0), it is ILLEGAL to set STE.Config == 0b11x .

If stage 2 is implemented, and Secure stage 2 is not supported (SMMU\_S\_IDR1.SEL2 == 0), and the STE is reached from the Secure Stream table, it is ILLEGAL to set STE.Config == 0b11x .

It is ILLEGAL to configure a Secure STE with STE.Config == 0b11x , and STE.S2AA64 selects VMSAv8-32 LPAE.

Note: When stage 1 is configured to translate, see the descriptions for STE.S1DSS and STE.S1Fmt for substream configuration.

In an EI, STE.Config[0] is permitted to be RAZ/WI if stage 1 is not implemented and STE.Config[1] is permitted to be RAZ/WI if stage 2 is not implemented.

When no translation stages are enabled ( 0b100 ), ATS Translation Requests (and Translated traffic, if SMMU\_CR0.ATSCHK == 1) are denied as though STE.EATS == 0b00 ; the actual value of the STE.EATS field is IGNORED. Such a Translation Request causes F\_BAD\_ATS\_TREQ and Translated traffic causes F\_TRANSL\_FORBIDDEN.

When STE.Config == 0b000 , an ATS Translation Request is denied with UR status and no event is recorded. When STE.Config == 0b000 and SMMU\_CR0.ATSCHK == 1, ATS Translated transactions are terminated with an abort and no event is recorded.

## S1Fmt, bits [5:4]

Stage 1 Format.

If STE.S1CDMax == 0 (substreams disabled) or SMMU\_IDR1.SSIDSIZE == 0 (substreams unsupported), this field is IGNORED and STE.S1ContextPtr points to one CD.

Otherwise STE.S1ContextPtr points to:

| S1Fmt   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00    | Two or more Context descriptors in a linear table indexed by SubstreamID[STE.S1CDMax - 1:0]. The table is aligned to its size. S1ContextPtr[STE.S1CDMax + 5:6] are RES0.                                                                                                                                                                                                                                                                                                                                                   |
| 0b01    | 2-level table with 4KB L2 leaf tables. L1 table contains 1-16384 L1CD pointers (128KB maximum) to 4KB tables of 64 CDs. If STE.S1CDMax <= 6, only index #0 of the L1 table is used. Otherwise, the L1 table is indexed by SubstreamID[STE.S1CDMax - 1:6]. The L2 table is indexed by SubstreamID[5:0]. L2 tables are 4KB-aligned: L1CD.L2Ptr[11:0] are taken to be zero by the SMMU. L1 tables are aligned to their size, or 64 bytes, whichever is greater. If STE.S1CDMax > 9, S1ContextPtr[STE.S1CDMax - 4:6] are RES0. |

| S1Fmt   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b10    | 2-level table with 64KB L2 leaf tables. L1 table contains 1-1024 L1CD pointers (8KB maximum) to 64KB tables of 1024 CDs. If STE.S1CDMax<=10, only index #0 of the L1 table is used. Otherwise, the L1 table is indexed by SubstreamID[STE.S1CDMax - 1:10]. The L2 table is indexed by SubstreamID[9:0]. L2 tables are 64KB-aligned: L1CD.L2Ptr[15:12] are RES0 and L1CD.L2Ptr[11:0] are taken to be zero by the SMMU. L1 tables are aligned to their size, or 64 bytes, whichever is greater. If STE.S1CDMax > 13, S1ContextPtr[STE.S1CDMax - 8:6] are RES0. |
| 0b11    | Reserved (behaves as 0b00 )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

Bits of STE.S1ContextPtr that are RES0 because of the configuration of STE.S1CDMax must be programmed to zero by software. If they are not programmed to zero, it is CONSTRAINED UNPREDICTABLE which of the following behaviors applies:

- The SMMU treats the bits as zero.
- If this field is 0b00 , the SMMU fetches any CD in the table.
- If this field is 0b01 or 0b10 , the SMMU fetches any L1CD in the level 1 CD table.

When multiple substreams are supported and enabled, the supported range is 2-1024K substreams in all table layouts.

If STE.Config == 0b1x0 (stage 1 disabled), this field is IGNORED and the supply of a SubstreamID with a transaction causes the transaction to be terminated with an abort, recording C\_BAD\_SUBSTREAMID. This is the case for full stream bypass (STE.Config == 0b100 ), or stage 2-only translation (STE.Config == 0b110 ).

If STE.S1CDMax == 0 (substreams disabled) or SMMU\_IDR1.SSIDSIZE == 0 (substreams unsupported), this field is IGNORED and STE.S1ContextPtr points to one CD.

If substreams are supported and enabled and stage 1 is enabled and SMMU\_IDR0.CD2L == 0, it is ILLEGAL to set this field != 0b00 (as two-stage tables are not supported).

In an EI, this field is permitted to be RAZ/WI if stage 1 is not implemented or substreams are unsupported or SMMU\_IDR0.CD2L == 0.

Note: If stage 2 is configured, STE.S1ContextPtr is an IPA. If this field indicates a 2-level table, the pointers in the first-level table are also IPAs. Otherwise, the pointers are PAs.

Note: If this field is 0b00 , it can be used for a single CD, or to support multiple CDs for substreams. A 4KB page will hold 64 CDs, and a 64KB page will hold 1024 CDs.

Note: Arm expects that the effective number of CDs in simultaneous use is practically limited to the number of distinct address spaces which is limited by the number of ASIDs. If this field is 0b01 , 64KB CDs can be accommodated with an 8KB L1 table and multiple 4KB L2 tables.

## S1ContextPtr, bits [55:6]

Pointer to the Stage 1 Context descriptor.

Bits above the implemented OA size, reported in SMMU\_IDR5.OAS, are RES0.

Bits above and below the range of the field are implied as zero in CD address calculations.

If STE.Config == 0b1x0 (stage 1 disabled), this field is IGNORED.

In an EI, this field is permitted to be RAZ/WI if stage 1 is not implemented.

If STE.Config == 0b11x (stage 2 enabled), this pointer is an IPA translated by stage 2 and the programmed value must be within the range of the IAS. Otherwise, this pointer is a PA, is not translated, and must be within the range of the OAS. See 3.4.3 Address sizes of SMMU-originated accesses for allowed behavior of an out-of-range value in this field.

In a Realm STE:

- If stage 1 and stage 2 translation are enabled, this field is treated as a Realm IPA.
- If stage 1 translation is enabled and stage 2 translation is disabled, this field is treated as a Realm physical address.

## Bits [58:56]

Reserved, RES0.

## S1CDMax, bits [63:59]

Log2 of the number of CDs pointed to by STE.S1ContextPtr.

The number of CDs pointed to by STE.S1ContextPtr is 2 STE.S1CDMax .

If SMMU\_IDR1.SSIDSIZE == 0, this field is IGNORED. A transaction is not permitted to supply a SubstreamID. If a transaction does so, it will be terminated and a C\_BAD\_SUBSTREAMID event recorded.

In an EI, this field is permitted to be RAZ/WI if stage 1 is not implemented or if SMMU\_IDR1.SSIDSIZE == 0.

If STE.Config == 0b1x0 (stage 1 disabled), this field is IGNORED.

If this field is 0, then all of the following apply:

- STE.S1ContextPtr points at one CD.
- Substreams are disabled.
- Any transaction using this STE that is presented with SSV=1 is terminated with an abort, and a C\_BAD\_SUBSTREAMID event is generated.

If this field is greater than 0, all of the following apply:

- STE.S1ContextPtr points at more than one CD.
- Transactions with SSV=1 and a SubstreamID that is less than 2 STE.S1CDMax use the CD for that SubstreamID.
- Transactions with SSV=1 and a SubstreamID that is greater than or equal to 2 STE.S1CDMax are terminated with an abort, and a C\_BAD\_SUBSTREAMID event is generated.

The allowable range is 0 to SMMU\_IDR1.SSIDSIZE inclusive. Other values are ILLEGAL.

The behavior of a transaction without a SubstreamID when STE.S1CDMax &gt; 0 is governed by the STE.S1DSS field.

## S1DSS, bits [65:64]

Default Substream.

When substreams are enabled (STE.S1CDMax != 0), this field determines the behavior of a transaction or translation request that arrives without an associated substream:

| S1DSS   | Meaning                                                                                    |
|---------|--------------------------------------------------------------------------------------------|
| 0b00    | Terminate. An abort is reported to the device and the F_STREAM_DISABLED event is recorded. |

| S1DSS   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b01    | Bypass stage 1 as though STE.Config == 0b1x0 The transaction can cause a stage 1 Address Size fault if the input address size exceeds the IAS, see section 3.4 Address sizes for details. If the configuration enables stage 2 translation, the address is then translated as an IPA if a stage 1 Address Size fault did not occur. Note: This behavior is identical to a transaction through an STE with STE.Config == 0b1x0 . Note: Such a transaction does not fetch a CD, and therefore does not report F_CD_FETCH, C_BAD_CD or a stage 2 Translation-related fault with CLASS == CD. |
| 0b10    | Transactions that do not include a substream are translated using the CD associated with Substream 0, which becomes unavailable for use by transactions that include a substream. Transactions that include a substream and select Substream 0 are terminated. An abort is reported to the device and the F_STREAM_DISABLED event is recorded. System software must associate traffic with non-zero substreams because Substream 0 is not available for use.                                                                                                                              |
| 0b11    | Reserved (behaves as 0b00 )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

If STE.Config == 0b1x0 (stage 1 disabled) or STE.S1CDMax == 0 (substreams disabled) or SMMU\_IDR1.SSIDSIZE == 0 (substreams unsupported), this field is IGNORED.

In an EI, this field is permitted to be RAZ/WI if stage 1 is not implemented or if SMMU\_IDR1.SSIDSIZE == 0.

Note: PCIe traffic might include a PASID TLP prefix, or might be issued without it. Consequently, it is possible for some transactions to supply a substream while others from the same endpoint do not.

Note: This field affects ATS Translation Requests, which can be caused to skip stages of translation as described in section 13.6.3 Split-stage (STE.EATS == 0b10 ) ATS behavior and responses and 13.6.4 Full ATS skipping stage 1 . See section 3.9.2 Changing ATS configuration for information on changing configuration that affects ATS translations that could be cached in an Endpoint.

For ATS Translation Requests, if the cases described in 0b00 and 0b10 lead to termination, the Translation Request is terminated with a CA and no event is recorded.

## S1CIR, bits [67:66]

STE.S1ContextPtr memory Inner Region attribute.

| S1CIR   | Meaning                                        |
|---------|------------------------------------------------|
| 0b00    | Normal, non-cacheable                          |
| 0b01    | Normal, Write-Back cacheable, Read-Allocate    |
| 0b10    | Normal, Write-Through cacheable, Read-Allocate |
| 0b11    | Normal, Write-Back cacheable, no Read-Allocate |

Note: Read allocation is a hint in the same way as in the A-profile architecture, and it is IMPLEMENTATION DEFINED whether it has any effect.

Note: Because CDs are read-only there is no configuration for cache allocation on write. The value of the write-allocation hint provided for a CD read is IMPLEMENTATION DEFINED.

This field, STE.S1COR and STE.S1CSH set the memory access attributes that access the Context descriptor (and Level-1 CD table pointers, if relevant) through STE.S1ContextPtr. If STE.Config == 0b11x (stage 2 enabled), the CD is loaded from IPA space and the attributes are combined with those from the stage 2 translation descriptor of the page mapping the accessed IPA, otherwise, these attributes are used directly.

In an EI, this field, STE.S1COR and STE.S1CSH are permitted to be RAZ/WI if stage 1 is not implemented.

## S1COR, bits [69:68]

STE.S1ContextPtr memory Outer Region attribute.

| S1COR   | Meaning                                        |
|---------|------------------------------------------------|
| 0b00    | Normal, Non-cacheable                          |
| 0b01    | Normal, Write-Back cacheable, Read-Allocate    |
| 0b10    | Normal, Write-Through cacheable, Read-Allocate |
| 0b11    | Normal, Write-Back cacheable, no Read-Allocate |

## S1CSH, bits [71:70]

STE.S1ContextPtr memory Shareability attribute.

| S1CSH   | Meaning                     |
|---------|-----------------------------|
| 0b00    | Non-shareable               |
| 0b01    | Reserved (behaves as 0b00 ) |
| 0b10    | Outer Shareable             |
| 0b11    | Inner Shareable             |

Note: If both STE.S1CIR and STE.S1COR == 0b00 , selecting normal Non-cacheable access, the Shareability of access to CDs is taken to be Outer Shareable regardless of the value of this field.

## S2HWU59, bit [72]

If SMMU\_IDR3.PBHA == 1, this field controls the interpretation of bit [59] of the stage 2 translation table final-level (page or block) descriptor.

| S2HWU59   | Meaning                                                                        |
|-----------|--------------------------------------------------------------------------------|
| 0b0       | Bit [59] is not interpreted by hardware for an IMPLEMENTATION DEFINED purpose. |
| 0b1       | Bit [59] has IMPLEMENTATION DEFINED hardware use.                              |

This field is IGNORED if PBHA are not supported (SMMU\_IDR3.PBHA == 0).

If STE.S2AA64 selects VMSAv9-128, this field is RES0.

In SMMUv3.0 this field is RES0.

Note: Stage 2 translations do not have the Hierarchical Attribute Disable (HAD) control present for stage 1 and the stage 2 HWU bits therefore do not have a relation to HAD in the same way as for stage 1.

## S2HWU60, bit [73]

Similar to STE.S2HWU59, but affecting descriptor bit [60].

## S2HWU61, bit [74]

Similar to STE.S2HWU59, but affecting descriptor bit [61].

## S2HWU62, bit [75]

Similar to STE.S2HWU59, but affecting descriptor bit [62].

## DRE, bit [76]

Destructive Read Enable.

Some implementations might support transactions with data-destructive effects which intentionally cause cache lines to be invalidated, without writeback even if they are dirty, such as destructive reads or cache invalidation operations, see section 3.22 Destructive reads and directed cache prefetch transactions .

Note: The invalidation side-effect is not required for correctness of this class of transaction, but if performed might cause stale data to be made visible.

| DRE   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | A device request to consume data using a read and invalidate transaction is transformed to a read without a data-destructive side-effect. An Invalidate Cache Maintenance Operation is transformed to a CleanInvalidate operation.                                                                                                                                                                           |
| 0b1   | A device request to consume data using a read and invalidate transaction is permitted to destructively read the requested location. An Invalidate Cache Maintenance Operation is permitted without transformation. Both of these behaviors are dependent on the correct page permissions as described in sections 3.22.2 Permissions model and 16.7.2.2 Permissions model for Cache Maintenance Operations . |

This field is IGNORED on implementations that do not support this class of transactions. Otherwise, this field is applied for the following transactions:

- Transactions that go through at least one stage of translation (if STE.S1DSS configuration or STE.Config == 0b100 causes all stages to be bypassed, a read and invalidate or Invalidate Cache Maintenance Operation is permitted regardless of the value of this field). This includes ATS Translated transactions where Split-stage ATS is enabled.
- ATS Translated transactions if SMMU\_CR0.ATSCHK == 1 and one of the following conditions is met:
- -STE.EATS selects Full ATS and SMMU\_IDR3.DPT == 1. If SMMU\_IDR3.DPT == 0 then it is IMPLEMENTATION DEFINED whether this bit is applied.
- -STE.EATS selects Full ATS with DPT checks.

In SMMUv3.0 this field is RES0.

## CONT, bits [80:77]

Contiguous Hint.

This field provides a hint to SMMU caching structures that a fetched STE is identical to its neighbours within a particular span of StreamIDs, and that a cache of the STE might be matched for any future lookup of StreamID for translation purposes within this span. The field is a 4-bit unsigned value specifying the span size. This field does not affect configuration invalidation. Software must ensure every STE in the required range is targeted by appropriate CMD\_CFGI\_* commands, regardless of the value of the field.

When CONT == 0, the STE is an individual STE bordered by STEs not considered identical. Otherwise, the span is defined as a contiguous block of 2 CONT STEs starting at a StreamID for which StreamID[CONT-1:0]=0.

All defined fields, except for CONT, in all STEs within the stated span must be identical, otherwise the result of an STE lookup has one of the following CONSTRAINED UNPREDICTABLE behaviors:

- The requested STE is used as it is represented in the Stream table.
- A neighbouring STE within the CONT span is used.
- An F\_CFG\_CONFLICT event is reported and the transaction or translation request that led to the STE lookup is aborted.

Note: During the process of marking STEs as members of a contiguous span (or taking away such hints), the STEs might differ by their CONT field values.

Note: Arm expects that the CONT value is changed in valid STEs and that the STEs in the span are not made invalid before changing CONT. This ensures that the STEs in the span remain identical.

A span greater than the size of the Stream table is capped by the SMMU by the size of the Stream table, and does not allow StreamIDs beyond the Stream table span to match an STE.

For a given valid STE in a 2-level Stream table, if STE.CONT is configured to a range greater than the number of entries in the level 2 array that locates that STE, use of StreamIDs within the range of that STE.CONT is CONSTRAINED UNPREDICTABLE. Either one of these behaviors is permitted:

- The transaction is terminated and a C\_BAD\_STREAMID error is raised, if the StreamID is outside of the range represented by the Span of the corresponding L1STD. Note: This is the expected behavior when using a StreamID outside of an L1STD.Span range.
- The transaction uses any STE from the same Security state as the stream.

In an EI, this field is permitted to be RAZ/WI.

## DCP, bit [81]

Directed Cache Prefetch.

Some implementations might support directed cache prefetch hint operations which are a standalone hint transaction, or a read/write transaction with hint side-effect, that changes the cache allocation in a part of the cache hierarchy that is not on the direct path to memory. This class of operation does not include those with data-destructive side-effects, see section 3.22 Destructive reads and directed cache prefetch transactions .

| DCP   | Meaning                                                                                                                                                                                                 |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Directed cache prefetch operations are inhibited. A transaction input with hint side-effect is stripped of the hint. A standalone hint operation completes successfully having no effect on the system. |

| DCP   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1   | A directed cache prefetch operation is permitted as follows: • A transaction with hint side-effect is performed if the final translation permissions permit the transaction. - Note: This permits a write with side-effect to progress if permissions grant write access, otherwise a Permission fault occurs. • A standalone hint operation is performed if the final permissions grant either read or write or execute permission for the requested address, otherwise the hint completes successfully having no effect on the system. |

This field is IGNORED on implementations that do not support this class of transactions. Otherwise, this field is applied for the following transactions:

- Transactions that go through at least one stage of translation (if STE.S1DSS configuration or STE.Config == 0b100 causes all stages to be bypassed, a directed cache prefetch is permitted regardless of the value of this field). This includes ATS Translated transactions where Split-stage ATS is enabled.
- ATS Translated transactions if SMMU\_CR0.ATSCHK == 1 and one of the following conditions is met:
- -STE.EATS selects Full ATS and SMMU\_IDR3.DPT == 1. If SMMU\_IDR3.DPT == 0 then it is IMPLEMENTATION DEFINED whether this bit is applied.
- -STE.EATS selects Full ATS with DPT checks.

In SMMUv3.0 this field is RES0.

## PPAR, bit [82]

PRI Page request Auto Responses.

| PPAR   | Meaning                                                                                 |
|--------|-----------------------------------------------------------------------------------------|
| 0b0    | Auto-generated responses on PRI queue overflow do not include a PASID TLP prefix.       |
| 0b1    | Auto-generated responses on PRI queue overflow include a PASID TLP prefix if permitted. |

See sections 8.1 PRI queue overflow and 8.2 Miscellaneous for the conditions that permit a PASID TLP prefix to be used on an auto-generated response.

If SMMU\_IDR0.PRI == 0 or SMMU\_IDR1.SSIDSIZE == 0, this field is RES0.

If SMMU\_IDR3.PPS == 1, this field is IGNORED and the behavior of an auto-generated response is the same as described for PPAR == 1.

## MEV, bit [83]

Merge Events arising from terminated transactions from this stream.

| MEV   | Meaning                                   |
|-------|-------------------------------------------|
| 0b0   | Do not merge similar fault records        |
| 0b1   | Permit similar fault records to be merged |

The SMMU might be able to reduce the usage of the Event queue by coalescing fault records that share the same page granule of address, access type and SubstreamID.

Setting MEV == 1 does not guarantee that faults will be coalesced.

Setting MEV == 0 causes a physical SMMU to prevent coalescing of fault records, however, a hypervisor might not honour this setting if it deems a guest to be too verbose.

Note: Software must expect, and be able to deal with, coalesced fault records even when MEV == 0.

In an EI, this field is permitted to be RAZ/WI if the implementation does not merge events.

See section 7.3.1 Event record merging for details on event merging.

## SW\_RESERVED, bits [87:84]

Reserved for software use.

This field is IGNORED by the SMMU.

In an EI, storage must be provided for this field.

## S1PIE, bit [88]

Stage 1 permission indirection enable.

| S1PIE   | Meaning                                                                |
|---------|------------------------------------------------------------------------|
| 0b0     | CDs fetched via this STE cannot enable stage 1 permission indirection. |
| 0b1     | CDs fetched via this STE can enable stage 1 permission indirection.    |

If SMMU\_IDR3.S1PI == 0 this field is RES0.

## S2FWB, bit [89]

Stage 2 control of attributes.

| S2FWB   | Meaning                                                                                                                                                                                       |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | Attribute calculation behaves as described in Chapter 13 Attribute Transformation .                                                                                                           |
| 0b1     | Output attribute calculation and the behavior of the stage 2 page or block descriptor bits [4:2] are affected as described in the VMSA in the A-profile architecture[2] for HCR_EL2.FWB == 1. |

Note: The VMSA FWB behavior allows the stage 2 memory type to be output directly instead of being combined with that of the stage 1 translation, redefining bit [4] of a stage 2 page or block descriptor to do so.

This field applies when both stage 1 and stage 2 translation is performed or when stage 2-only translation is performed. This field is IGNORED when stage 2 translation is not performed.

Otherwise, when stage 2 translation is performed, it is ILLEGAL to set this field to 1 when STE.S2AA64 selects VMSAv8-32 LPAE.

If SMMU\_IDR3.MTEPERM == 1, the effects of this field on the interpretation of memory attributes change. See 3.23 Memory Tagging Extension .

Prior to SMMUv3.2 this field is RES0.

## S1MPAM, bit [90]

Enable stage 1 control of MPAM.

| S1MPAM   | Meaning                                                                                                                                                                                                      |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | The PARTID and PMG for transactions and SMMU-originated requests relating to this stream are assigned by STE.PARTID and STE.PMG.                                                                             |
| 0b1      | The PARTID and PMG for transactions are assigned by the CD.PARTID and CD.PMG fields, which might be translated using the PARTID_MAP. See section 17.2 Assignment of PARTID and PMG for client transactions . |

Prior to SMMUv3.2, and if MPAM is not supported in the corresponding Security state, this field is RES0. Otherwise, when MPAM is supported in the corresponding Security state then:

- When stage 1 translation is performed, this field controls whether the MPAM IDs are given by the CD or the STE. This applies to stage 1-only and nested configurations. In a nested configuration that has this field configured to 1, CD.PARTID is translated using VMS.PARTID\_MAP as described in section 17.2 Assignment of PARTID and PMG for client transactions .
- When stage 1 translation is not performed, this field is IGNORED and the STE.PARTID and STE.PMG fields are used.
- -This applies to STE.Config == 0b1x0 and to scenarios where STE.S1DSS causes stage 1 to bypass.

## S1STALLD, bit [91]

Stage 1 Stall Disable.

| S1STALLD   | Meaning                                                                     |
|------------|-----------------------------------------------------------------------------|
| 0b0        | Allow stalling fault model for stage 1 (configured in CD)                   |
| 0b1        | Disallow stalls to be configured for Stage 1 (faults terminate immediately) |

If stage 1 is not implemented (SMMU\_IDR0.S1P == 0), this field is RES0.

If stage 1 is not enabled (STE.Config == 0b1x0 ), this field is IGNORED.

Otherwise, if stage 1 is enabled and SMMU\_(*\_)IDR0.STALL\_MODEL is not 0b00 , it is ILLEGAL to set this field to 1 because the Stall model is not supported or not configurable.

When the Stall model is configurable, this field must be set for StreamIDs associated with stall-unsafe system topologies or for PCIe clients.

## EATS, bits [93:92]

Enable PCIe ATS translation and traffic.

This field enables responses to ATS Translation Requests, and if SMMU\_CR0.ATSCHK == 1, controls whether ATS Translated traffic can pass into the system.

| EATS   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00   | ATS Translation Requests are returned unsuccessful or aborted (UR) and F_BAD_ATS_TREQ is recorded. Additionally, if SMMU_CR0.ATSCHK == 1, Translated traffic associated with the StreamID of the STE is prevented from bypassing the SMMU. Such traffic is terminated with an abort and a F_TRANSL_FORBIDDEN event is recorded.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 0b01   | Full ATS: ATS Translation Requests are serviced by translating at all enabled stages of translation. Translated traffic from the StreamID of the STE is allowed to bypass (regardless of SMMU_CR0.ATSCHK). In implementations of SMMUv3.1 and later, this configuration is ILLEGAL if this field is not IGNORED and STE.Config == 0b11x and STE.S2S == 1. In SMMUv3.0 implementations, this configuration is ILLEGAL if this field is not IGNORED and STE.S2S == 1. It is CONSTRAINED UNPREDICTABLE whether or not this check of STE.S2S occurs when STE.Config == 0b10x . Arm recommends that STE.S2S == 1 causes STE.EATS == 0b01 to be ILLEGAL only when STE.Config == 0b11x . This condition is represented by CONSTR_UNPRED_EATS_S2S in the pseudocode description.                                                                                                                                                                                                              |
| 0b10   | Split-stage ATS: ATS Translation responses return the IPA output of stage 1 translation to the Endpoint or ATC. Subsequent Translated transactions are generated by the Endpoint with IPAs and these undergo stage 2 translation in the SMMU, see section 13.6.3 Split-stage (STE.EATS == 0b10 ) ATS behavior and responses for details. This configuration must only be used when: • The stream has both stage 1 and stage 2 translation (STE.Config == 0b111 ) • STE.S2S == 0 • SMMU_IDR0.NS1ATS == 0 • SMMU_CR0.ATSCHK == 1 If any of the following hold, the STE is ILLEGAL (if it is not IGNORED): • STE.Config != 0b111 • STE.S2S == 1. • SMMU_IDR0.NS1ATS == 1. If STE.Config == 0b111 and STE.S2S == 0 and SMMU_IDR0.NS1ATS == 0, but SMMU_CR0.ATSCHK == 0 then STE.EATS == 0b10 configuration behaves as 0b00 . Note: See section 13.6.3 Split-stage (STE.EATS == 0b10 ) ATS behavior and responses and 13.6.4 Full ATS skipping stage 1 which describes interaction of this |

| EATS   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b11   | Enable Full ATS with DPT checks: If SMMU_R_IDR3.DPT == 0, then this encoding is Reserved for Realm STEs and behaves as 0b00 . If SMMU_IDR3.DPT == 0, then this encoding is Reserved for Non-secure STEs and behaves as 0b00 . If the corresponding SMMU_(R_)IDR3.DPT == 1 and StreamWorld is not EL1, this encoding is ILLEGAL and results in C_BAD_STE. For a Non-secure STE, if this encoding is not ILLEGAL and SMMU_CR0.ATSCHK == 0, then this encoding is treated as 0b00 . This configuration is ILLEGAL if this field is not IGNORED and STE.Config == 0b11x and STE.S2S == 1. Otherwise: Same as encoding 0b01 but additionally enables per-granule checking of ATS-translated transactions. See also 3.24.1 DPT check . |

If the STE is Secure, this field is RES0 and has an effective value of 0b00 .

This field is IGNORED if any of the following hold:

- SMMU\_IDR0.ATS == 0
- -ATS is not supported by the SMMU implementation. No ATS requests can be made, nor Translated traffic passed.
- STE.Config[1:0] == 0b00
- -When STE.Config == 0b100 , the effective value of this field is 0b00 .The responses and events recorded for Translation Requests and Translated transactions are as described in this table for STE.EATS == 0b00 .
- -When STE.Config == 0b000 , Translation Requests are silently terminated with UR and, if SMMU\_CR0.ATSCHK == 1, Translated transactions are silently aborted.

Incoming PCIe traffic marked Translated is only checked against the effective value of STE.EATS if SMMU\_CR0.ATSCHK == 1, otherwise traffic marked Translated bypasses the SMMU.

Incoming ATS Translation Requests are always checked against the effective value of STE.EATS.

The behavior when STE.EATS == 0b10 or 0b11 is dependent on SMMU\_CR0.ATSCHK; see section 3.9.2 Changing ATS configuration for details on changing ATS configuration. An implementation is permitted to cache ATSCHK in configuration caches, so if ATSCHK is changed while STEs exist with STE.EATS == 0b10 or 0b11 it is UNPREDICTABLE as to whether the behavior on receipt of new requests related to those STEs is as though this field is configured to 0b00 or 0b10 .

In an EI, this field is permitted to be RAZ/WI if SMMU\_IDR0.ATS == 0.

Note: There is no dependency between this field being non-zero and the ability for a CD to select the stall fault model with CD.S == 1. Arm expects that the Stall model is not enabled for PCIe-related streams both at stage 2 (STE.S2S == 0) and at stage 1 (CD.S == 0) and that STE.S1STALLD == 1 is used if necessary to ensure that a CD cannot use CD.S == 1 when the CD configuration is not managed the highest-privilege entity in the system. This expectation is present regardless of whether the stream uses ATS or not. If STE.S1STALLD == 0 and CD.S == 1, the Stall model might (if supported) cause PCIe traffic to stall upon fault.

## STRW, bits [95:94]

StreamWorld control.

Selects the translation regime and associated Exception level controlling this stream, in conjunction with the Security state of the STE as defined by being fetched using the Stream table associated with that Security state, when stage 1 translation is used.

If stage 1 is not implemented (SMMU\_IDR0.S1P == 0), this field is RES0. In this case, the effective StreamWorld is determined by STE.Config[1].

If SMMU\_IDR0.Hyp == 0 and the STE is in the Non-secure Stream table this field is RES0.

If STE.Config == 0b11x (stage 2 translation enabled) and the STE is Non-secure, STRW is IGNORED (if it is not already RES0) and the effective StreamWorld is NS-EL1.

If STE.Config == 0b11x and the STE is Secure and Secure stage 2 is supported, then STRW is IGNORED (if it is not already RES0) and the effective StreamWorld is Secure.

If STE.Config == 0b10x (stage 2 bypass) and STE.Config == 0b1x0 (stage 1 bypass), STRW is IGNORED (if it is not already RES0) as no translations are performed.

Note: The STRW field is not the same as the StreamWorld, which is an attribute whose Effective value might be influenced by STRW in some configurations, but not in others. See section 3.3.3 Configuration and Translation lookup for a definition of StreamWorld.

If Config == 0b101 (stage 1 only), then StreamWorld is determined from the Security state of the Stream table, STRW and SMMU\_(*\_)CR2.E2H as described below.

For STEs reached using the Non-secure Stream table, if STRW is not RES0 or IGNORED then StreamWorld is determined from STRW and SMMU\_CR2.E2H as follows:

| STRW   | E2H   | Resulting StreamWorld   |
|--------|-------|-------------------------|
| 0b00   | X     | NS-EL1                  |
| 0b10   | 0     | NS-EL2                  |
| 0b10   | 1     | NS-EL2-E2H              |
| 0bx1   | X     | Reserved, ILLEGAL       |

For STEs reached using the Realm Stream table, if STRW is not RES0 or IGNORED, then StreamWorld is determined from STRW and SMMU\_R\_CR2.E2H as follows:

| STE.Config   | STE.STRW   | Mode              | Properties                                                                                                                 |
|--------------|------------|-------------------|----------------------------------------------------------------------------------------------------------------------------|
| 0b0xx        | 0bxx       | Stream disabled   | See 3.10.3.2 Realm stream disabled .                                                                                       |
| 0b100        | 0bxx       | Stream bypass     | See 3.10.3.3 Realm stream bypass .                                                                                         |
| 0b101        | 0b00       | EL1 stage 1 only  | Realm EL1&0 stage 1 translation, with stage 2 translation disabled.                                                        |
| 0b111        | 0b00       | EL1 stage 1 and 2 | Realm EL1&0 stage 1 translation, with stage 2 translation enabled.                                                         |
| 0b110        | 0b00       | EL1 stage 2 only  | Realm EL1&0 stage 1 translation disabled, with stage 2 translation enabled.                                                |
| 0b101        | 0b10       | EL2 or EL2-E2H    | If SMMU_R_CR2.E2H=0 then Realm EL2 stage 1 stage 1 translation. If SMMU_R_CR2.E2H=1, then Realm EL2&0 stage 1 translation. |

For STEs reached using the Secure Stream table, if STRW is not RES0 or IGNORED then StreamWorld is determined from STRW and SMMU\_S\_CR2.E2H as follows:

| STRW   | E2H   | Resulting StreamWorld   | ILLEGAL when            |
|--------|-------|-------------------------|-------------------------|
| 0b00   | X     | Secure                  | -                       |
| 0b10   | 0     | S-EL2                   | SMMU_S_IDR1.SEL2 == 0   |
| 0b10   | 1     | S-EL2-E2H               | SMMU_S_IDR1.SEL2 == 0   |
| 0b01   | X     | EL3                     | SMMU_IDR0.RME_IMPL == 1 |
| 0b11   | X     | Reserved, ILLEGAL       | Always                  |

The behaviors of these StreamWorlds are as follows:

- Secure tags TLB entries as Secure with an ASID and Arm expects this StreamWorld to be selected for Secure streams used by:
- -Secure software on an Armv7-A host PE, or Armv8-A host PE whose EL3 runs in AArch32.
- -Secure-EL1 software on an Armv8-A host PE whose EL3 runs in AArch64.
- When Secure stage 2 is supported, that is SMMU\_S\_IDR1.SEL2 == 1, the Secure StreamWorld additionally tags TLB entries a VMID.
- S-EL2 tags TLB entries as Secure EL2 without an ASID.
- S-EL2-E2H tags TLB entries as Secure EL2 with an ASID, using E2H mode.
- EL3 tags TLB entries as Secure EL3, without an ASID.
- The tagging of resulting TLB entries, that is the translation regime, and ASID or VMID.
- The number of translation tables used in the CD for stage 1.
- The Permissions model used in stage 1 translation table

Note: The StreamWorld affects three things:

## See also:

- 3.3.3 Configuration and Translation lookup .
- 3.3.4 Transaction attributes: incoming, two-stage translation and overrides .

## MemAttr, bits [99:96]

Memory Attribute override value.

If MTCFG == 1, MemAttr provides memory type override for incoming transactions. The encoding matches the VMSAv8-64 stage 2 MemAttr[3:0] field as described in the A-profile architecture[2], except that the following encodings are Reserved (not UNPREDICTABLE) and behave as Device-nGnRnE:

- 0b0100
- 0b1000
- 0b1100

Note: In the A-profile architecture[2], FEAT\_MTE\_PERM introduces the encoding 0b0100 for the stage 2 MemAttr[3:0] field. This behavior is implemented in the SMMU if SMMU\_IDR3.MTEPERM == 1. For STE.MemAttr this encoding remains Reserved and behaves as Device-nGnRnE. See section 3.23.1 SMMU support for FEAT\_MTE\_PERM .

Note: This encoding matches the encoding of the stage 2 translation table descriptor MemAttr field that is used when S2FWB == 0. The S2FWB field only affects the stage 2 translation table descriptor MemAttr field, and does not affect the encoding of this field.

If MTCFG == 0 or SMMU\_IDR1.ATTR\_TYPES\_OVR == 0, this field is RES0.

## MTCFG, bit [100]

Memory Type configuration.

| MTCFG   | Meaning                                                                  |
|---------|--------------------------------------------------------------------------|
| 0b0     | Use incoming type or Cacheability                                        |
| 0b1     | Replace incoming type or Cacheability with that defined by MemAttr field |

If SMMU\_IDR1.ATTR\_TYPES\_OVR == 0, this field is RES0 and the incoming Memory Type is used.

It is IMPLEMENTATION DEFINED whether MTCFG applies to streams associated with PCIe devices or whether the incoming Memory Type is used for such streams regardless of the field value.

## ALLOCCFG, bits [104:101]

Allocation hints override.

- 0b0xxx : Use incoming RA, WA, TR hints
- 0b1RWT : Hints are overridden to given values:
- -Read Allocate == R
- -Write Allocate == W
- -Transient == T

When overridden by this field, for each of RA/WA and TR, both inner and outer hints are set to the same value. Because it is not architecturally possible to express hints for types that are any-Device or Normal-Non-cacheable, this field has no effect on memory types that are not Normal-WB or Normal-WT, whether such types are provided with transaction from the client device or overridden using MTCFG/MemAttr.

Note: A value of 0b1001 encodes Transient with no-allocate. When the SMMU ensures output attribute consistency (see section 13.1.7 Ensuring consistent output attributes ), no-allocate is considered to be non-transient. As there is no value of stage 1/stage 2 attribute with which Transient-no-allocate could combine to cause an allocating Transient attribute to be output, 0b1001 is functionally equivalent to 0b1000 (non-Transient, no-allocate).

If SMMU\_IDR1.ATTR\_TYPES\_OVR == 0, this field is RES0 and the incoming Allocation hints are used.

It is IMPLEMENTATION DEFINED whether ALLOCCFG applies to streams associated with PCIe devices or whether the incoming allocation hints are used for such streams regardless of the field value.

If STE.MTCFG is 0, it is CONSTRAINED UNPREDICTABLE whether ALLOCCFG has any effect on the allocation hints for the cacheability domains of a transaction.

## Bits [107:105]

Reserved, RES0.

## SHCFG, bits [109:108]

Shareability configuration.

| SHCFG   | Meaning                             |
|---------|-------------------------------------|
| 0b00    | Non-shareable                       |
| 0b01    | Use incoming Shareability attribute |
| 0b10    | Outer shareable                     |
| 0b11    | Inner shareable                     |

Architecturally, any-Device and Normal-iNC-oNC are OSH and Shareability is only variable where cacheable types are used. This field has no effect on memory types that do not contain Normal-{i,o}WB or Normal-{i,o}WT, whether such types are provided with transaction from the client device or overridden using MTCFG/MemAttr.

If SMMU\_IDR1.ATTR\_TYPES\_OVR == 0, this field is RES0 and the incoming Shareability attribute is used.

It is IMPLEMENTATION DEFINED whether SHCFG applies to streams associated with PCIe devices or whether the incoming Shareability attribute is used for such streams regardless of the field value.

## NSCFG, bits [111:110]

Non-secure attribute configuration.

For a Secure stream, NSCFG is interpreted as follows:

| NSCFG   | Meaning                     |
|---------|-----------------------------|
| 0b00    | Use incoming NS attribute   |
| 0b01    | Reserved, behaves as 0b00 . |
| 0b10    | Secure                      |
| 0b11    | Non-secure                  |

NSCFG is IGNORED when the STE is in the Non-secure Stream table.

NSCFG is IGNORED when the STE is in the Secure Stream table and stage 1 translation is enabled. In this case the final NS attribute is determined entirely by the translation process (see CD.NSCFGx, the TTD.NSTable and TTD.NS bits). The input NS attribute and this field are not used. If Secure stage 2 is enabled, the output IPA space determined from the stage 1 translation is input into stage 2. See section 3.10.2.2 Secure EL2 and support for Secure stage 2 translation .

Otherwise, when the STE is in the Secure Stream table and stage 1 translation is disabled (STE.Config == 0b1x0 ):

- If SMMU\_IDR1.ATTR\_PERMS\_OVR == 0, this field is RES0 and the incoming NS attribute is output from stage 1 directly. If Secure stage 2 is enabled, the NS attribute is input into stage 2 and selects between the Secure and Non-secure IPA spaces.
- If SMMU\_IDR1.ATTR\_PERMS\_OVR == 1, this field determines the target IPA or PA space of transactions that bypass stage 1 translation and this value is output from stage 1 as the target IPA or PA space.
- -Note: Arm recommends that SMMU\_IDR1.ATTR\_PERMS\_OVR == 1 if an implementation might be used in a system where the input NS attribute from a client device on a Secure stream is not accurate, and is required to be overridden by the SMMU configuration.
- If Secure stage 2 is enabled, the resulting NS attribute is input into stage 2. See section 3.10.2.2 Secure EL2 and support for Secure stage 2 translation .

Note: The function of this field is not related to the CD.NSCFG{0,1} fields (whose purpose is to affect the NS property of the translation table walk).

For a Realm stream, NSCFG is interpreted as follows:

| Value   | Meaning                                                                                                            |
|---------|--------------------------------------------------------------------------------------------------------------------|
| 0b00    | Use incoming NS attribute.                                                                                         |
| 0b01    | If SMMU_R_IDR3.XT == 0, then Reserved, behaves as 0b00 . If SMMU_R_IDR3.XT == 1, then Check incoming NS attribute. |
| 0b10    | Override to Realm.                                                                                                 |
| 0b11    | Override to Non-secure.                                                                                            |

Note: If the Realm client device does not provide an input NS attribute, the input NS attribute defaults to Realm.

Note: NSCFG is supported for Realm streams regardless of the value of SMMU\_IDR1.ATTR\_PERMS\_OVR.

## PRIVCFG, bits [113:112]

User/privileged attribute configuration.

| PRIVCFG   | Meaning                     |
|-----------|-----------------------------|
| 0b00      | Use incoming PRIV attribute |
| 0b01      | Reserved, behaves as 0b00 . |
| 0b10      | Unprivileged                |
| 0b11      | Privileged                  |

If SMMU\_IDR1.ATTR\_PERMS\_OVR == 0, this field is RES0 and the incoming PRIV attribute is used.

## INSTCFG, bits [115:114]

Inst/Data attribute configuration.

| INSTCFG   | Meaning                     |
|-----------|-----------------------------|
| 0b00      | Use incoming INST attribute |
| 0b01      | Reserved, behaves as 0b00 . |
| 0b10      | Data                        |
| 0b11      | Instruction                 |

If SMMU\_IDR1.ATTR\_PERMS\_OVR == 0, this field is RES0 and the incoming INST attribute is used.

INSTCFG only affects translations for reads, the SMMU considers incoming writes to be Data regardless of this field. See section 13.1.2 Attribute support .

## IMPLEMENTATION DEFINED, bits [127:116]

IMPLEMENTATION DEFINED per-stream configuration. (For example, QoS overrides for configuration access, data streams.)

## S2VMID, bits [143:128]

Virtual Machine Identifier

Marks TLB entries inserted because of translations located through this STE, differentiating them from translations belonging to different virtual machines.

For a Non-secure STE when stage 2 is implemented (SMMU\_IDR0.S2P == 1) translations resulting from a StreamWorld == NS-EL1 configuration are VMID-tagged with STE.S2VMID when either of stage 1 (STE.Config == 0b1x1 ) or stage 2 (STE.Config == 0b11x ) provide translation.

For a Secure STE when Secure stage 2 is implemented, that is SMMU\_S\_IDR1.SEL2 == 1, and when StreamWorld == Secure:

- Translations are VMID-tagged with STE.S2VMID when stage 2 is enabled (STE.Config == 0b11x ), including nested configuration.
- When only stage 1 is enabled, this field is IGNORED and translations are tagged with VMID 0.

Note: Secure VMIDs and Non-secure VMIDs are different namespaces. See section 3.10.2.2 Secure EL2 and support for Secure stage 2 translation .

When an implementation supports only 8-bit VMIDs, that is when SMMU\_IDR0.VMID16 == 0, it is ILLEGAL for bits STE.S2VMID[15:8] to be non-zero unless this field is IGNORED.

STE.S2VMID[15:0] is IGNORED and no VMID tagging occurs when any of the following are true:

- Stage 2 is not implemented in the Security state corresponding to the STE.
- STE.Config[1:0] == 0b00 . Note: In this case, no TLB entries are inserted as translation is bypassed.
- A Non-secure STE StreamWorld is not NS-EL1.
- A Secure STE has a StreamWorld other than 'Secure'.
- A Realm STE StreamWorld is not Realm-EL1.

Note: If SMMU\_IDR0.S2P == 0, then for broadcast TLB maintenance, the SMMU is only required to invalidate Non-secure EL1 or Secure StreamWorld TLB entries if VMID is 0 in the broadcast TLB maintenance operation. See 3.17 TLB tagging, VMIDs, ASIDs and participation in broadcast TLB maintenance .

In an EI, this field is permitted to be RAZ/WI if stage 2 is not implemented. In an EI implementing stage 2 with 8-bit VMIDs, STE.S2VMID[15:8] are permitted to be RAZ/WI.

If 16-bit VMIDs are supported by an implementation, the full VMID[15:0] value is used regardless of STE.S2AA64. Arm expects that legacy and AArch32 hypervisor software using 8-bit VMIDs will write zero-extended 8-bit values in the VMID field in this case.

See section 3.17 TLB tagging, VMIDs, ASIDs and participation in broadcast TLB maintenance for more information on ASID and VMID TLB tagging.

Changes to the STE.S2VMID field of an STE are not automatically reflected in cached translations, which must be subjected to separate TLB maintenance.

Note: This field might be supplied by an implementation in transactions to the memory system for IMPLEMENTATION DEFINED purposes.

## IMPLEMENTATION DEFINED, bits [159:144]

IMPLEMENTATION DEFINED.

## S2T0SZ, bits [165:160]

Size of IPA input region covered by stage 2 translation table.

This field is equivalent to VTCR\_EL2.T0SZ in the A-profile architecture[2].

This field is 4 bits ([3:0]) and bits [5:4] are IGNORED when stage 2 translation is VMSAv8-32 LPAE, as indicated by STE.S2AA64. The input region size is calculated the same as in the A-profile architecture[2]. When STE.S2AA64 selects VMSAv8-64 or VMSAv9-128, this field is 6 bits and the region size is calculated the same as for VTCR\_EL2 in the A-profile architecture[2].

If stage 2 translation is enabled (STE.Config == 0b11x ), legal values of STE.S2SL0 and STE.S2TG relate to this field as defined by the Translation system in the A-profile architecture[2], in section D5.2.3, 'Controlling Address translation stages'.

Note: This field is IGNORED when stage 2 is implemented but not enabled (STE.Config == 0b10x ).

When STE.S2AA64 selects VMSAv8-64:

- If SMMU\_IDR3.STT == 0, the maximum valid value is 39.
- If SMMU\_IDR3.STT == 1, the maximum valid value is:
- -48, when STE.S2TG selects a 4KB or 16KB granule
- -47, when STE.S2TG selects a 64KB granule.
- In SMMUv3.0, the minimum valid value for this field is (64-IAS).
- In architectures after SMMUv3.0:
- -If STE.S2TG selects a 4KB or 16KB granule and STE.S2DS == 0, the minimum valid value for this field is MAX(16, 64-IAS).
- Otherwise, the minimum valid value for this field is MAX(12, 64-IAS).

Note: If AArch32 is implemented, IAS == MAX(40, OAS), otherwise IAS == OAS, see section 3.4 Address sizes .

When STE.S2AA64 selects VMSAv9-128:

- The maximum valid value is:
- -48, when STE.S2TG selects a 4KB or 16KB granule.
- -47, when STE.S2TG selects a 64KB granule.
- The minimum valid value is MAX(8, 64-IAS).

When STE.S2AA64 selects VMSAv8-32 LPAE, this field encodes a value from -8 to 7 as defined by the Translation system in the A-profile architecture[2].

Note: When STE.S2AA64 selects VMSAv8-32 LPAE all 4-bit values are valid, therefore it is not possible to use a value outside the valid range but it is still possible for this field to be inconsistent with STE.S2SL0.

In SMMUv3.0 implementations, the use of a value out of range of these maximum and minimum valid values is CONSTRAINED UNPREDICTABLE and has one of the following behaviors:

- The STE becomes ILLEGAL.
- The STE is not ILLEGAL and the effective value used by the translation is the maximum permitted value (if the programmed value is greater than the maximum permitted value) or the minimum permitted value (if the programmed value is less than the minimum permitted value).

Note: This condition is represented by constr\_unpred\_S2T0SZ\_oor\_ILLEGAL in the pseudocode description.

In implementations of SMMUv3.1 and later, an STE is treated as ILLEGAL if it contains a STE.S2T0SZ value out of range of these maximum and minimum values.

The usable range of values is further constrained by a function of the starting level set by STE.S2SL0 and, if STE.S2AA64 selects VMSAv8-64 or VMSAv8-32 LPAE, granule size set by STE.S2TG as described by the translation system in the A-profile architecture[2]. Use of a value of STE.S2T0SZ that is inconsistent with the permitted range (given STE.S2SL0 and STE.S2TG) is ILLEGAL.

Note: The SMMU behavior differs from the Translation system in the A-profile architecture[2], in which the legal range of VTCR\_EL2.T0SZ values can also depend on whether EL1&amp;0 stage 1 uses VMSAv8-32 LPAE or VMSAv8-64.

If stage 2 is not implemented, that is if SMMU\_IDR0.S2P == 0, this field is RES0.

## S2SL0, bits [167:166]

Starting level of stage 2 translation table walk.

If STE.S2DS == 1 and STE.S2TG selects 4KB, this field is considered in combination with the STE.S2SL0\_2 field.

The stage 2 walk start level is a function of STE.{S2SL0\_2, S2SL0} and the value of STE.S2TG.

When STE.S2AA64 selects VMSAv8-64, the encoding of STE.{S2SL0\_2, S2SL0} is the same as for the VTCR\_EL2.{SL2, SL0} fields in the A-profile architecture[2].

When STE.S2AA64 selects VMSAv8-32 LPAE, the encoding of this field is the same as for the VTCR.SL0 field in the A-profile architecture[2].

If stage 2 is not implemented, that is if SMMU\_IDR0.S2P == 0, this field is RES0.

If stage 2 translation is enabled (STE.Config == 0b11x ), it is ILLEGAL for the configuration of STE.{S2SL0\_2, S2SL0} to be inconsistent with STE.S2T0SZ and STE.S2TG.

If STE.S2AA64 selects VMSAv9-128, this field is RES0.

## S2IR0, bits [169:168]

Inner region Cacheability for stage 2 translation table access.

| S2IR0   | Meaning                                                |
|---------|--------------------------------------------------------|
| 0b00    | Non-cacheable                                          |
| 0b01    | Write-back Cacheable, Read-Allocate, Write-Allocate    |
| 0b10    | Write-through cacheable, Read-Allocate                 |
| 0b11    | Write-back cacheable, Read-Allocate, no Write-Allocate |

The only time that translation table entries are written by the SMMU is when HTTU is in use, and because the read effect of the atomic update might cause read allocation of the affected translation table entry into a data cache, it is IMPLEMENTATION DEFINED as to whether 0b01 and 0b11 differ.

Many memory systems might require use of Normal Write-back Cacheable memory for the atomic updates of translation table entries to occur correctly.

If HTTU is enabled and this field is configured to 0b00 or 0b10 , then it is IMPLEMENTATION DEFINED which of the following behaviors occurs for hardware updates of Access flag and dirty state:

- The hardware update occurs correctly as an atomic read-modify-write operation.
- The hardware update occurs, but the read-modify-write operation is not guaranteed to be atomic.
- The hardware update is attempted but fails and generates an F\_WALK\_EABT event.

Arm recommends that software uses 0b01 or 0b11 when HTTU is enabled for this translation table unless the behavior of an implementation is otherwise known.

If stage 2 is not implemented, that is if SMMU\_IDR0.S2P == 0, this field is RES0.

## S2OR0, bits [171:170]

Outer region Cacheability for stage 2 translation table access.

Same as for S2IR0.

## S2SH0, bits [173:172]

Shareability for stage 2 translation table access.

| S2SH0   | Meaning                     |
|---------|-----------------------------|
| 0b00    | Non-shareable               |
| 0b01    | Reserved, behaves as 0b00 . |
| 0b10    | Outer Shareable             |
| 0b11    | Inner Shareable             |

Note: If both S2IR0 and S2OR0 == 0b00 , selecting normal Non-cacheable access, the Shareability of translation table access is taken to be OSH regardless of the value of this field.

If stage 2 is not implemented, that is if SMMU\_IDR0.S2P == 0, this field is RES0.

## S2TG, bits [175:174]

Stage 2 Translation Granule size.

| S2TG   | Meaning   |
|--------|-----------|
| 0b00   | 4KB       |
| 0b01   | 64KB      |
| 0b10   | 16KB      |
| 0b11   | Reserved  |

If stage 2 is not implemented, that is when SMMU\_IDR0.S2P == 0, this field is RES0.

Otherwise, if stage 2 translation is disabled (STE.Config == 0b10x ), this field is IGNORED.

Otherwise, if stage 2 translation is enabled (STE.Config == 0b11x ),

- If STE.S2AA64 selects VMSAv8-32 LPAE, this field is RES0 and the effective value of this field is 4KB.
- If STE.S2AA64 selects VMSAv8-64 or VMSAv9-128, this field must only select a granule supported by the SMMU, as described in SMMU\_IDR5, and use of an unsupported size or Reserved value is ILLEGAL.
- It is ILLEGAL for STE.S2T0SZ and STE.S2SL0 to be inconsistent with the value of this field, as described in the A-profile architecture[2].

## S2PS, bits [178:176]

Physical address Size.

This field is equivalent to VTCR\_EL2.PS in the A-profile architecture[2].

| S2PS   | Meaning                                                                                                                                                                       |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b000  | 32 bits                                                                                                                                                                       |
| 0b001  | 36 bits                                                                                                                                                                       |
| 0b010  | 40 bits                                                                                                                                                                       |
| 0b011  | 42 bits                                                                                                                                                                       |
| 0b100  | 44 bits                                                                                                                                                                       |
| 0b101  | 48 bits                                                                                                                                                                       |
| 0b110  | 52 bits In SMMUv3.0 implementations, this value is Reserved and behaves as 0b101 .                                                                                            |
| 0b111  | 56 bits. In SMMUv3.0 implementations, this value is Reserved and behaves as 0b101 . In implementations of SMMUv3.1 to SMMUv3.3, this value is Reserved and behaves as 0b110 . |

Software must not rely on the behavior of Reserved values.

This field determines the Physical address size for the purpose of Address Size fault checking the output of stage 2 translation, see section 3.4 Address sizes .

If stage 2 is not implemented, that is when SMMU\_IDR0.S2P == 0, this field is RES0.

If STE.S2AA64 selects VMSAv8-32 LPAE, this field is IGNORED and the effective stage 2 output address size is taken as 40 bits.

If STE.S2AA64 selects VMSAv8-64 or VMSAv9-128, the effective stage 2 output address size is given by:

eff\_S2PS = MIN(S2PS, SMMU\_IDR5.OAS);

The effective value of this field is capped to the OAS.

When STE.S2AA64 selects VMSAv8-64 or VMSAv9-128, setting this field to any value greater than the cap defined here behaves as though this field equals the cap size. Software must not rely on this behavior.

Note: This includes use of a Reserved value.

An Address Size fault occurs if stage 2 translation outputs an address that has non-zero bits above eff\_S2PS .

If STE.S2AA64 selects VMSAv8-64, an address of 52 bits in size can be output from stage 2 when eff\_S2PS is 52 and either:

- 64KB granule is in use for that translation table.
- STE.S2DS == 1.

An address of 56 bits in size can be output from stage 2 when STE.S2AA64 selects VMSAv9-128.

Note: In configurations where eff\_S2PS is larger than the address output from the stage 2 descriptor, output bits above the address are treated as zero and no Address Size fault can occur.

In SMMUv3.0 addresses are limited to 48 bits.

## S2AA64, bit [179]

Stage 2 translation table format for S2TTB0, and S\_S2TTB0 if appropriate.

| S2AA64   | Meaning                                | Applies when          |
|----------|----------------------------------------|-----------------------|
| 0b0      | Use VMSAv8-32 LPAE descriptor formats. | SMMU_IDR0.TTF[0] == 1 |
| 0b0      | Use VMSAv9-128 descriptor formats.     | SMMU_IDR5.D128 == 1   |
| 0b1      | Use VMSAv8-64 descriptor formats.      |                       |

If stage 2 is not implemented, that is when SMMU\_IDR0.S2P == 0, this field is RES0.

If SMMU\_IDR5.D128 == 0 and stage 2 translation is enabled (STE.Config == 0b11x ), it is ILLEGAL to select:

- VMSAv8-32 LPAE tables when VMSAv8-32 LPAE tables are not supported (SMMU\_IDR0.TTF[0] == 0).
- VMSAv8-64 tables when VMSAv8-64 tables are not supported (SMMU\_IDR0.TTF[1] == 0).

If an STE is in the Secure stream table and STE.Config == 0b11x , it is ILLEGAL to select VMSAv8-32 LPAE.

If this field selects VMSAv9-128, then STE.{S2SL0, S2SL0\_2, S\_S2SL0, S\_S2SL0\_2} fields are all RES0. If SMMU\_IDR5.D128 == 1, the behavior of this field is equivalent to VTCR\_EL2.D128 in the A-profile architecture[2], with reversed polarity.

Note: The stage 2 translation table permissions are interpreted slightly differently between VMSAv8-64 and VMSAv8-32 LPAE format tables, for example, a VMSAv8-64 stage 2 table can encode an execute-only page permission whereas a VMSAv8-32 LPAE stage 2 table cannot, see the A-profile architecture[2] for more information.

This field is permitted to be cached in a TLB.

## S2ENDI, bit [180]

Stage 2 translation table endianness.

| S2ENDI   | Meaning       |
|----------|---------------|
| 0b0      | Little Endian |
| 0b1      | Big Endian    |

If Stage 2 translation is enabled (STE.Config == 0b11x ), it is ILLEGAL for this field to select an unimplemented endianness (as indicated by SMMU\_IDR0.TTENDIAN).

If stage 2 is not implemented, that is when SMMU\_IDR0.S2P == 0, this field is RES0.

## S2AFFD, bit [181]

Stage 2 Access Flag Fault Disable.

When HTTU is not in use at stage 2 because (STE.S2HA == 0 or HTTU is not supported, this flag determines the behavior on access of a stage 2 page whose descriptor has AF == 0:

| S2AFFD   | Meaning                                                                       |
|----------|-------------------------------------------------------------------------------|
| 0b0      | An Access flag fault occurs (behavior controlled by STE.S2R and STE.S2S bits) |

| S2AFFD   | Meaning                                                                         |
|----------|---------------------------------------------------------------------------------|
| 0b1      | An Access flag fault never occurs; the TTD.AF bit is considered to be always 1. |

When (STE.S2HA == 1, this flag is IGNORED.

If stage 2 is not implemented, that is if SMMU\_IDR0.S2P == 0, this field is RES0.

## S2PTW, bit [182]

Protected Table Walk.

For an STE configured for translation at both stages, a stage 1 translation table walk access or CD fetch access made to a stage 2 page with any Device type is terminated and recorded as a stage 2 Permission fault if this field is set.

Note: This might provide early indication of a programming error.

| S2PTW   | Meaning                                                                                                                                                                                                                                                    |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | If SMMU_IDR3.PTWNNC == 0: CD fetch and stage 1 translation table walks allowed to any valid stage 2 address. If SMMU_IDR3.PTWNNC == 1: A translation table access or CD fetch mapped as any Device type occurs as if it is to Normal Non-cacheable memory. |
| 0b1     | CD fetch or Stage 1 translation table walks to stage 2 addresses mapped as any Device are terminated. A stage 2 Permission fault is recorded.                                                                                                              |

If STE.Config[1:0] != 0b11 , this field is IGNORED.

If stage 2 is not implemented, that is if SMMU\_IDR0.S2P == 0, this field is RES0.

## S2HD, bit [183]

Hardware Translation Table Update of stage 2 Dirty flags.

See definition of S2HA.

## S2HA, bit [184]

Hardware Translation Table Update of stage 2 Access flags.

When combined with STE.S2HD as {STE.S2HA, STE.S2HD}:

- 0b00 : HTTU disabled
- 0b10 : Update of Access flag enabled
- 0b01 : Reserved. If STE.S2HD == 1 is not ILLEGAL, behaves as (STE.S2HA == 0 and STE.S2HD == 0).
- 0b11 : Update of Access flag and dirty state of the page enabled

If stage 2 translation is enabled (STE.Config == 0b11x ),

- It is ILLEGAL to set STE.S2HA or (STE.S2HD if STE.S2AA64 selects VMSAv8-32 LPAE.
- It is ILLEGAL to set STE.S2HA if SMMU\_IDR0.HTTU == 0b00 .
- It is ILLEGAL to set STE.S2HD if SMMU\_IDR0.HTTU == 0b00 or 0b01 .

These fields are RES0 if stage 2 is not implemented. In an EI, this field is permitted to be RAZ/WI if stage 2 is not implemented or SMMU\_IDR0.HTTU == 0b00 . In an EI, STE.S2HD is permitted to be RAZ/WI if stage 2 is not implemented or SMMU\_IDR0.HTTU == 0b0x .

Note: If HTTU is enabled when S2OR0 or S2IR0 indicate Non-cacheable memory, behavior is IMPLEMENTATION DEFINED, see 3.15 Coherency considerations and memory access types . A system might only be able to perform atomic updates using cacheable normal memory, or might implement other means for doing so.

## S2S, bit [185]

Stage 2 fault behavior - Stall.

See section 5.5 Fault configuration (A, R, S bits) for a description of fault configuration.

When STE.Config == 0b10x (Stage 2 disabled), {S2R, S2S} are IGNORED.

If stage 2 is not implemented, that is when SMMU\_IDR0.S2P == 0, this field is RES0.

## S2R, bit [186]

Stage 2 fault behavior - Record.

See section 5.5 Fault configuration (A, R, S bits) for a description of fault configuration.

When STE.Config == 0b10x (Stage 2 disabled), {S2R, S2S} are IGNORED.

If stage 2 is not implemented, that is when SMMU\_IDR0.S2P == 0, this field is RES0.

## S2HAFT, bit [187]

Enable hardware update of Access flag in Table descriptors.

| S2HAFT   | Meaning                |
|----------|------------------------|
| 0b0      | Stage 2 HAFT disabled. |
| 0b1      | Stage 2 HAFT enabled.  |

If STE.S2HA is 0 and not IGNORED, it is ILLEGAL to set this field to 1 and this results in C\_BAD\_STE.

This field is permitted to be cached in a TLB.

If SMMU\_IDR0.HTTU != 0b11 this field is RES0.

## S2PIE, bit [188]

Stage 2 permissions indirection enable.

This field is equivalent to VCTR\_EL2.S2PIE in the A-profile architecture[2].

| S2PIE   | Meaning                                                  |
|---------|----------------------------------------------------------|
| 0b0     | Stage 2 translations use the Direct Permission Scheme.   |
| 0b1     | Stage 2 translations use the Indirect Permission Scheme. |

Note: For each Security state, this field must be configured consistently for all STEs that have the same value of STE.S2VMID.

If STE.S2AA64 selects VMSAv9-128, this field is RES0 and stage 2 translations use the Indirect Permission Scheme.

If SMMU\_IDR3.S2PI == 0 or STE.S2AA64 selects VMSAv8-32 this field is RES0.

This field is permitted to be cached in a TLB.

## S2POE, bit [189]

Stage 2 permission overlay enable.

This field is similar to VCTR\_EL2.S2POE in the A-profile architecture[2].

| S2POE   | Meaning                                   |
|---------|-------------------------------------------|
| 0b0     | Do not apply stage 2 overlay permissions. |
| 0b1     | Apply stage 2 overlay permissions.        |

If stage 2 translations use the Direct Permission Scheme, it is ILLEGAL to set this field to 1 and this results in C\_BAD\_STE.

If any of STE.{S2HWU62, S2HWU61, S2HWU60, S2HWU59} are 1, it is ILLEGAL to set this field to 1 and this results in C\_BAD\_STE.

This field is permitted to be cached in a TLB.

Note: In the A-profile architecture[2], the equivalent bit is not permitted to be cached in a TLB, because it is expected to be updated in a manner that is synchronous relative to accesses made in the EL1&amp;0 translation regime. However, this is not possible in the SMMU, as a device might make accesses at any time, so this field is permitted to be cached in a TLB.

If SMMU\_IDR3.S2PO == 0 this field is RES0.

## DPT\_VMATCH, bits [191:190]

VMID matching requirement for DPT checks.

If SMMU\_(R\_)IDR3.DPT == 0 or STE.EATS != 0b11 , then this field is RES0.

For a Non-secure STE with STE.EATS == 0b11 , the encoding is:

| DPT_VMATCH   | Meaning                                                                                  |
|--------------|------------------------------------------------------------------------------------------|
| 0b00         | STE.S2VMID is required to match or the DPT entry is required to have AC = 0b10 .         |
| 0b01         | STE.S2VMID is required to match or the DPT entry is required to have AC = 0b01 or 0b10 . |
| 0b10         | S2VMID not required to match.                                                            |
| 0b11         | Reserved, behaves as 0b00 .                                                              |

For a Realm STE with STE.EATS == 0b11 , then all of the following apply:

- The only permitted value is encoding 0b00 , and this behaves as described for Non-secure STEs.
- It is ILLEGAL to program this field to any value other than 0b00 .

Note: If DPT\_VMATCH is not consistently configured for all STEs with the same STE.S2VMID field, it is possible that accesses are checked according to the most-permissive DPT\_VMATCH field for that group of STEs.

This field is not permitted to be cached in a TLB.

See also:

· 3.24.1 DPT check .

## S2NSW, bit [192]

This field gives the NS bit used for all stage 2 translation table walks for the Secure stream Non-secure IPA space, that is, made through STE.S2TTB.

When the STE is not in the Secure Stream table then this field is RES0.

If SMMU\_S\_IDR1.SEL2 == 0 then this field is RES0.

If SMMU\_S\_IDR1.SEL2 == 1, this field is IGNORED in a Secure STE that has STE.Config == 0b10x .

## S2NSA, bit [193]

This field gives the NS bit that is output for all stage 2 Secure stream Non-secure IPA translations.

When the STE is not in the Secure Stream table then this field is RES0.

If SMMU\_S\_IDR1.SEL2 == 0 then this field is RES0.

If SMMU\_S\_IDR1.SEL2 == 1, this field is IGNORED in a Secure STE that has STE.Config == 0b10x .

Otherwise, when STE.S2NSW == 1 or the effective value of STE.S2SA is 1, this field is IGNORED and the stage 2 Secure stream Non-secure IPA translation results in the target Non-secure PA space.

Note: The effective value of the STE.S2SA field is treated as being 1 when the STE.S2SW field is 1.

## S2SL0\_2, bit [194]

Bit [2] of STE.S2SL0.

See the definition of STE.S2SL0.

This field is IGNORED if stage 2 is implemented but not enabled.

If STE.S2AA64 selects VMSAv9-128, then this field is RES0.

If SMMU\_IDR5.DS == 0 this field is RES0.

If STE.S2AA64 selects VMSAv8-32 LPAE then this field is RES0.

## S2DS, bit [195]

Enable 52-bit input and output address size when using 4KB and 16KB granules.

| S2DS   | Meaning                                                         |
|--------|-----------------------------------------------------------------|
| 0b0    | 52-bit address sizes when using 4KB and 16KB granules disabled. |
| 0b1    | 52-bit address sizes when using 4KB and 16KB granules enabled.  |

The effect of this field on the interpretation of stage 2 translation table descriptors is the same as for the VTCR\_EL2.DS bit as specified in FEAT\_LPA2 in the A-profile architecture[2].

The effect of this field on the determination of whether the STE.{S2T0SZ, S2SL0, S\_S2T0SZ, S\_S2SL0} fields are configured inconsistently is the same as for the effect of the VTCR\_EL2.DS bit on V(S)TCR\_EL2.{T0SZ, SL0, SL2} specified in FEAT\_LPA2 in the A-profile architecture[2].

If this field is 1, the Shareability attribute for a Cacheable location translated by tables pointed to by STE.S2TTB is taken from STE.S2SH0.

For a stream with Secure stage 2 translation enabled, if this field is 1, the Shareability attribute for a cacheable location translated by tables pointed to by STE.S\_S2TTB is taken from STE.S2SH0.

This field is IGNORED if stage 2 is implemented but not enabled.

This field is RES0 if any of the following are true:

- STE.S2AA64 selects VMSAv9-128.
- STE.S2AA64 selects VMSAv8-32 LPAE.
- STE.S2TG selects 64KB.
- For a Secure stream, if STE.S\_S2TG selects 64KB.

If SMMU\_IDR5.DS == 0 this field is RES0.

## S2TTB, bits [247:196]

In SMMUv3.1 and later, if STE.S2AA64 selects VMSAv9-128, then bits[247:196] represent the address of Stage 2 Translation Table base, bits[55:4]. Otherwise:

- In SMMUv3.1 and later:
- -Bits[243:196] represent the address of Stage 2 Translation Table base, bits[51:4].
- -Bits[247:244] are RES0.
- In SMMUv3.0:
- -Bits[239:196] represent the address of Stage 2 Translation Table base, bits[47:4].
- -Bits[247:240] are RES0.

Address bits above and below the field range are treated as zero.

Bits [(x-1):0] are treated as if all the bits are zero, where x is defined by the required alignment of the translation table as given in the A-profile architecture[2].

Note: The SMMU effectively aligns the value in this field before use.

For VMSAv8-64 a 64-byte minimum alignment on starting-level translation table addresses is imposed when the effective STE.S2PS value indicates 52-bit output. In this case bits [5:0] are treated as zero.

For VMSAv9-128 a 32-byte minimum alignment on starting-level translation table addresses is imposed regardless of the effective STE.S2PS value. In this case bits [4:0] are treated as zero.

If Stage 2 translation is enabled (STE.Config[1]=1), it is ILLEGAL for the address in this field to be outside the range described by the effective STE.S2PS value. It is ILLEGAL for the address in this field to be outside of a 48-bit range when STE.S2AA64 selects VMSAv8-64 and STE.S2TG selects a granule smaller than 64KB and STE.S2DS == 0.

If stage 2 is not implemented, that is if SMMU\_IDR0.S2P == 0, this field is RES0.

In an EI, the high-order bits of TTB outside of the PA size (SMMU\_IDR5.OAS) are permitted to be RAZ/WI. If these bits are not implemented as RAZ/WI, they must store the full address field and correctly support the ILLEGAL address range-check described above.

In a Realm STE, STE.S2TTB, if required, is treated as being a Realm physical address.

## Bits [252:248]

Reserved, RES0.

## S2SKL, bits [254:253]

Skip Level configuration for initial lookup for stage 2 translations using STE.S2TTB.

This field is equivalent to VTTBR\_EL2.SKL in the A-profile architecture[2].

| S2SKL   | Meaning        |
|---------|----------------|
| 0b00    | Skip 0 levels. |
| 0b01    | Skip 1 level.  |
| 0b10    | Skip 2 levels. |
| 0b11    | Skip 3 levels. |

If STE.S2AA64 selects VMSAv9-128, this field is interpreted as the Skip Level for the initial lookup for stage 2 translations that use STE.S2TTB.

If STE.S2AA64 selects VMSAv8-64, then this field is RES0.

If SMMU\_IDR5.D128 == 0 this field is RES0.

This field is permitted to be cached in a TLB.

Reserved, RES0.

## IMPLEMENTATION DEFINED, bits [271:256]

IMPLEMENTATION DEFINED.

## PARTID, bits [287:272]

MPAM partition ID assigned to accesses related to this StreamID.

If MPAM is not supported in the corresponding Security state, then this field is RES0.

This field is interpreted as having an UNKNOWN value if it is configured with a value greater than the corresponding SMMU\_(*\_)MPAMIDR.PARTID\_MAX.

The corresponding SMMU\_(*\_)MPAMIDR.PARTID\_MAX is chosen as follows:

- For a Non-secure Stream, then SMMU\_MPAMIDR.PARTID\_MAX.
- For a Secure Stream, if SMMU\_S\_MPAMIDR.HAS\_MPAM\_NS == 0 or STE.MPAM\_NS == 0, then SMMU\_S\_MPAMIDR.PARTID\_MAX.
- For a Secure Stream, if SMMU\_S\_MPAMIDR.HAS\_MPAM\_NS == 1 and STE.MPAM\_NS == 1, then SMMU\_MPAMIDR.PARTID\_MAX.

Prior to SMMUv3.2 this field is RES0.

See Chapter 17 Memory System Resource Partitioning and Monitoring for more information on use of this field.

## S\_S2T0SZ, bits [293:288]

Size of Secure IPA input region covered by stage 2 translation table.

This field is equivalent to VSTCR\_EL2.T0SZ in the A-profile architecture[2].

This field is encoded the same as, and has the same validity requirements as STE.S2T0SZ.

## Bit [255]

Note: This field is not used with a stage 2 translation table for which STE.S2AA64 selects VMSAv8-32 LPAE, as this configuration is not permitted.

If SMMU\_S\_IDR1.SEL2 == 0 this field is RES0. If SMMU\_S\_IDR1.SEL2 == 1, this field is IGNORED in a Secure STE that has STE.Config == 0b10x . When the STE is not in the Secure Stream table this field is RES0.

## S\_S2SL0, bits [295:294]

Secure stage 2 translation starting level for STE.S\_S2TTB.

If STE.S2DS == 1 and STE.S\_S2TG selects 4KB, this field is considered in combination with the STE.S\_S2SL0\_2 field.

STE.{S\_S2SL0\_2, S\_S2SL0} are encoded the same as, and have the same validity requirements as STE.{S2SL0\_2, S2SL0}.

When any of the following are true this field is RES0:

- SMMU\_S\_IDR1.SEL2 == 0.
- The STE is not fetched for Secure state.
- STE.S2AA64 selects VMSAv9-128.

If SMMU\_S\_IDR1.SEL2 == 1, this field is IGNORED in a Secure STE that has STE.Config == 0b10x .

If stage 2 is not implemented, that is if SMMU\_IDR0.S2P == 0, this field is RES0.

## Bits [301:296]

Reserved, RES0.

## S\_S2TG, bits [303:302]

Secure stage 2 translation granule for STE.S\_S2TTB.

This field is encoded the same as, and has the same validity requirements, as STE.S2TG.

This field is equivalent to VSTCR\_EL2.TG0 in the A-profile architecture[2].

If SMMU\_S\_IDR1.SEL2 == 0 this field is RES0. If SMMU\_S\_IDR1.SEL2 == 1, this field is IGNORED in a Secure STE that has STE.Config == 0b10x . When the STE is not in the Secure Stream table this field is RES0.

## MECID, bits [319:304]

MECID for SMMU-originated and client-orientated accesses related to this StreamID.

The MECID value is used for all of the following accesses:

- Stage 1 and stage 2 translation table accesses for this stream, including the stage 2 translation of addresses used in L1CD and CD fetches.
- Fetches of L1CD and CD structures for this stream.
- Client-originated accesses to Realm PA space for this stream.

For STEs fetched for Non-secure or Secure streams this field is RES0.

If SMMU\_R\_IDR3.MEC == 0, this field is RES0.

For a Realm stream with STE.Config[2] == 0, this field is IGNORED.

Bits above the supported MECID size are RES0. The supported MECID size is indicated in SMMU\_R\_MECIDR.MECIDSIZE. If SMMU\_R\_MECIDR.MECIDSIZE is less than 0xf , the SMMU treats bits [15:MECIDSIZE+1] of this field as 0.

This field is permitted to be cached in a configuration cache.

Note: If multiple agents can access the same location with mismatched MECID values, the location can become UNKNOWN, as described in the FEAT\_MEC specification in the A-profile architecture[2]. Arm expects all Realm STEs with matching STE.S2VMID values also have matching MECID values.

## PMG, bits [327:320]

MPAM PMG assigned to accesses related to this StreamID.

If MPAM is not supported in the corresponding Security state this field is RES0.

For a Non-secure StreamID, this field is interpreted as having an UNKNOWN value if it is configured with a value greater than SMMU\_MPAMIDR.PMG\_MAX.

For a Secure StreamID if SMMU\_S\_MPAMIDR.HAS\_MPAM\_NS == 0 or STE.MPAM\_NS == 0, this field is interpreted as having an UNKNOWN value if it is configured with a value greater than SMMU\_S\_MPAMIDR.PMG\_MAX.

For a Secure StreamID if SMMU\_S\_MPAMIDR.HAS\_MPAM\_NS == 1 and STE.MPAM\_NS == 1, this field is interpreted as having an UNKNOWN value if it is configured with a value greater than SMMU\_MPAMIDR.PMG\_MAX.

Prior to SMMUv3.2 this field is RES0.

See Chapter 17 Memory System Resource Partitioning and Monitoring for more information on use of this field.

## MPAM\_NS, bit [328]

PARTID space value for accesses related to this StreamID.

| MPAM_NS   | Meaning                                                                                                        |
|-----------|----------------------------------------------------------------------------------------------------------------|
| 0b0       | Accesses for structures reached from this STE use the PARTID space corresponding to the Security state of STE. |
| 0b1       | Accesses for structures reached from this STE use the Non-secure PARTID space.                                 |

For a Non-secure STE this field is RES0.

For a Secure STE if SMMU\_S\_MPAMIDR.HAS\_MPAM\_NS == 0, this field is RES0.

for a Realm STE if SMMU\_R\_MPAMIDR.HAS\_MPAM\_NS == 0, this field is RES0.

If this field is 1, then accesses using MPAM information derived from information in this STE use Non-secure PARTID space. This STE.MPAM\_NS field affects the PARTID space used for:

- CD fetches
- Stage 1 translation table walks
- Stage 2 translation table walks
- Client transactions

Note: This field does not affect the PARTID space used for VMS fetches. See 17.7 Determination of PARTID space values .

## AssuredOnly, bit [329]

Stage 2 AssuredOnly behavior enable.

This field is equivalent to VTCR\_EL2.AssuredOnly in the A-profile architecture[2], but with an additional requirement that CDs are fetched from AssuredOnly memory in order to permit a stage 1 translation to have the Assured Translation property.

| AssuredOnly   | Meaning                                     |
|---------------|---------------------------------------------|
| 0b0           | AssuredOnly permission checks are disabled. |
| 0b1           | AssuredOnly permission checks are enabled.  |

If STE.S2AA64 selects VMSAv9-128, this field is RES0 and AssuredOnly permission checks are enabled.

If SMMU\_IDR3.THE == 0, this field is RES0.

This field is permitted to be cached in a TLB.

## TL0, bit [330]

Stage 2 TopLevel 0 check enable.

This field is equivalent to VTCR\_EL2.TL0 in the A-profile architecture[2].

If SMMU\_IDR3.THE == 0 this field is RES0.

This field is permitted to be cached in a TLB.

## TL1, bit [331]

Stage 2 TopLevel 1 check enable.

This field is equivalent to VTCR\_EL2.TL1 in the A-profile architecture[2].

If SMMU\_IDR3.THE == 0 this field is RES0.

This field is permitted to be cached in a TLB.

## VMSPtr, bits [375:332]

VMS pointer.

Bits above the implemented OA size, reported in SMMU\_IDR5.OAS, are RES0.

Physical address pointer to the VMS structure associated with the stream. For an STE in the Non-secure Stream Table, this address belongs to Non-secure PA space. For an STE in the Secure Stream Table, this address belongs to Secure PA space.

For an STE in the Realm Stream table, this address belongs to the Realm PA space.

Prior to SMMUv3.2 and when the VMS is not supported, this field is RES0. See section Virtual Machine Structure for information on the VMS and when it is supported.

When the VMS is supported in the corresponding Security state:

- The VMSPtr is enabled if all of the following are true:
- -STE.Config == 0b111 and STE.S1MPAM == 1.
- -STE.MPAM\_NS selects a PARTID space for which SMMU\_(*\_)MPAMIDR.PARTID\_MAX is non-zero.
- If the VMSPtr is enabled, then an address greater than the OAS leads to a C\_BAD\_STE error.

Note: This refers to the OAS from SMMU\_IDR5.OAS, not STE.S2PS.

- If the VMSPtr is not enabled, then VMSPtr is IGNORED.

Note: These rules may change if other facilities are added to the VMS.

Address bits [11:0] and [63:55] are taken as zero.

## Bits [383:376]

Reserved, RES0.

## S2SW, bit [384]

This field gives the NS bit used for all stage 2 translation table walks for Secure IPA space, that is, made through STE.S\_S2TTB.

When the STE is not in the Secure Stream table this field is RES0.

In a Secure STE if SMMU\_S\_IDR1.SEL2 == 0 this field is RES0.

If SMMU\_S\_IDR1.SEL2 == 1, this field is IGNORED in a Secure STE that has STE.Config == 0b10x .

## S2SA, bit [385]

This field gives the NS bit that is output for all stage 2 Secure IPA translations.

When the STE is not in the Secure Stream table this field is RES0. In a Secure STE if SMMU\_S\_IDR1.SEL2 == 0, this field is RES0.

If SMMU\_S\_IDR1.SEL2 == 1, this field is IGNORED in a Secure STE that has STE.Config == 0b10x .

Otherwise, when STE.S2SW == 1, this field is IGNORED and the effective STE.S2SA value is treated as being 1.

Note: When this field is 1, both the stage 2 Non-secure IPA and the stage 2 Secure IPA translations target Non-secure PA space. See STE.S2NSA.

## S\_S2SL0\_2, bit [386]

Bit [2] of STE.S\_S2SL0.

See the definition of STE.S\_S2SL0.

This field is IGNORED if stage 2 is implemented but not enabled.

If STE.S2AA64 selects VMSAv9-128 then this field is RES0.

If STE.S2AA64 selects VMSAv8-32 LPAE then this field is RES0.

If SMMU\_IDR5.DS == 0 this field is RES0.

Reserved, RES0.

## S\_S2TTB, bits [439:388]

In SMMUv3.1 and later, if STE.S2AA64 selects VMSAv9-128, then bits[439:388] represent the address of Secure Stage 2 Translation Table base, bits[55:4]. Otherwise:

- In SMMUv3.1 and later:
- -Bits[435:388] represent the address of Secure Stage 2 Translation Table base, bits[51:4].
- -Bits[439:436] are RES0.
- In SMMUv3.0:
- -Bits[431:388] represent the address of Secure Stage 2 Translation Table base, bits[47:4].
- -Bits[439:432] are RES0.

This field is encoded the same, and has the same validity requirements, as STE.S2TTB.

The STE.S\_S2TTB translation table is configured using the same STE.S2* fields as STE.S2TTB, with the exception of the following fields which are specific to STE.S\_S2TTB:

## Bit [387]

## Bit [447]

- STE.S\_S2SL0.
- STE.S\_S2TG.
- STE.S\_S2T0SZ.
- STE.S2SW.
- STE.S2SA.

If SMMU\_S\_IDR1.SEL2 == 0 this field is RES0. If SMMU\_S\_IDR1.SEL2 == 1, this field is IGNORED in a Secure STE that has STE.Config == 0b10x . When the STE is not in the Secure Stream table this field is RES0.

## Bits [444:440]

Reserved, RES0.

## S\_S2SKL, bits [446:445]

Skip Level configuration for initial lookup for stage 2 translations using STE.S\_S2TTB.

If STE.S2AA64 selects VMSAv9-128, this field is interpreted as the Skip Level for the initial lookup for stage 2 translations that use STE.S\_S2TTB.

This field is equivalent to VSTTBR\_EL2.SKL in the A-profile architecture[2].

| S_S2SKL   | Meaning        |
|-----------|----------------|
| 0b00      | Skip 0 levels. |
| 0b01      | Skip 1 level.  |
| 0b10      | Skip 2 levels. |
| 0b11      | Skip 3 levels. |

This field is RES0 if any of the following are true:

- STE.S2AA64 selects VMSAv8-64.
- SMMU\_IDR5.D128 == 0.
- The STE is not in the Secure Stream table.

This field is permitted to be cached in a TLB.

Reserved, RES0.

## S2POI&lt;p&gt; , bits [4p+451:4p+448], for p = 15 to 0

Stage 2 permission overlay interpretation.

This field is equivalent to S2POR\_EL1 in the A-profile architecture[2].

The set of 16 stage 2 permission overlay interpretations for this stream.

This field is indexed by the POIndex value derived from the translation table descriptor, as STE.S2POI[4*POIndex+3:4*POIndex].

| S2POI<p>   | Meaning                         |
|------------|---------------------------------|
| 0b0000     | No Access                       |
| 0b0001     | Reserved, treated as C_BAD_STE. |
| 0b0010     | MRO                             |
| 0b0011     | MRO-TL1                         |
| 0b0100     | WO                              |
| 0b0101     | Reserved, treated as C_BAD_STE. |
| 0b0110     | MRO-TL0                         |
| 0b0111     | MRO-TL01                        |
| 0b1000     | RO                              |
| 0b1001     | RO+uX                           |
| 0b1010     | RO+pX                           |
| 0b1011     | RO+puX                          |
| 0b1100     | RW                              |
| 0b1101     | RW+uX                           |
| 0b1110     | RW+pX                           |
| 0b1111     | RW+puX                          |

This field is RES0 if any of the following are true:

- SMMU\_IDR3.S2PO is 0.
- STE.S2POE is 0.
- Stage 2 permission indirection is not enabled. Note: This can be configured in STE.S2PIE, but if STE.S2AA64 selects VMSAv9-128 then stage 2 permission indirection is implicitly enabled.
- STE.S2AA64 selects VMSAv8-32 LPAE.

This field is IGNORED if stage 2 translation is disabled.

The effect of this field on the stage 2 translation of an output address from stage 1 is not permitted to be cached in a TLB.

The effect of this field on the stage 2 translation of a stage 1 translation table walk is permitted to be cached in a TLB.

If SMMU\_IDR3.S2PO == 0 this field is RES0.

## 5.2.1 General properties of the STE

If V == 1 and Config == 0b100 (Stream Bypass), the S1* and S2* fields are IGNORED. The following fields are used to apply attributes to the Bypass transactions:

- MTCFG/MemAttr, ALLOCCFG, SHCFG.
- NSCFG (Ignored unless STE is selected from Secure Stream table).
- PRIVCFG, INSTCFG.

If V == 1 and Config == 0b000 (disabled), the CONT field is permitted to be obeyed. The remaining fields contain no relevant configuration and are IGNORED. Transactions selecting such an STE will be silently terminated with an abort.

For more details on the memory attribute and permissions overrides (MTCFG, ALLOCCFG, SHCFG, NSCFG, PRIVCFG, INSTCFG), see Chapter 13 Attribute Transformation .

An STE or L1STD that is successfully fetched might be cached by the SMMU in any state, therefore any modification, commissioning or decommissioning of an STE must be followed by a CMD\_CFGI\_STE command. A failed fetch (F\_STE\_FETCH) does not cause an STE or L1STD to be cached.

When cached, an STE is uniquely identified by SEC\_SID and StreamID.

Note: An STE from one Stream table index X is unrelated to the STE at index X of the Stream table of the other Security state.

If an implementation supports bypass transactions (because STE.Config == 0b100 ) by creating 'identity-mapped' TLB entries, the presence of these entries is not visible to software. Changing STE.Config does not require explicit TLB invalidation.

Note: STE configuration invalidation is required for any alteration to an STE.

Note: StreamWorld (as determined from the STRW field, SMMU\_CR2.E2H, SMMU\_S\_CR2.E2H, Config[1:0] and the Security state of the Stream table that fetches the STE) controls the tagging of TLB entries, so a change of the StreamWorld of a stream makes lookups performed for the stream fail to match TLB entries of a prior StreamWorld or translation regime. Software must consider the possibility of such TLB entries still being present if a prior StreamWorld configuration is returned to, unless explicit invalidation has occurred. Arm recommends that TLB entries that are made unreachable by a change in StreamWorld are invalidated after the change to avoid their unanticipated use by a future configuration that happens to match the old StreamWorld, ASID and VMID (if appropriate).

Note: The following STE properties affect the interpretation of a CD located through the STE:

- StreamWorld.
- S1STALLD.
- VMSAv8-32 LPAE stage 2 translation (STE.Config == 0b11x and STE.S2AA64 selects VMSAv8-32 LPAE).

When stage 2 translation is enabled (STE.Config == 0b11x ), the correct setting of the stage 2 table walk starting level, S2SL0, is dependent on the granule size, S2TG, and the required IPA address size (S2T0SZ). All three fields must be set in a manner consistent with the equivalent Armv8-A fields. A mismatch causes the STE to be considered ILLEGAL. When Secure stage 2 is supported and enabled, the same requirement also applies to S\_S2SL0, S\_S2TG0 and S\_S2T0SZ.

Note: In Armv8-A, an inconsistency between SL0, TG and T0SZ is reported as a Translation fault.

In addition, a S2TTB base address outside the range indicated by the effective STE.S2PS value makes the STE ILLEGAL. When Secure stage 2 is enabled, this rule also applies to S\_S2TTB.

Note: In Armv8-A, an inconsistency between TTBR and PS is reported as an Address Size fault.

The following STE fields are permitted to be cached as part of a translation or TLB entry and, when altered, software must perform explicit invalidation of any TLB entry that might have cached these fields, after performing STE structure cache invalidation:

- S2TTB.
- S2PTW.
- S2VMID.
- S2T0SZ.
- S2IR0.
- S2OR0.
- S2SH0.
- S2SL0.
- S2TG.
- S2PS.
- S2AFFD.
- S2HA.

- S2HD.
- S2ENDI.
- S2AA64.
- S\_S2TTB.
- S2NSW.
- S2NSA.
- S2SW.
- S2SA.
- S\_S2SL0.
- S\_S2TG0.
- S\_S2T0SZ.
- S2FWB.
- TL1.
- TL0.
- AssuredOnly.
- S2PIE.
- S2POE.
- S2POI.
- S2SKL.
- S\_S2SKL.
- S2HAFT.

All other STE fields are not permitted to be cached as part of a translation or TLB entry, which means that alterations to all other STE fields do not require invalidation of TLB entries. IMPLEMENTATION DEFINED STE fields might have IMPLEMENTATION DEFINED invalidation requirements.

Note: Invalidation of an STE also implicitly invalidates cached CDs fetched through the STE.

For a given Security state, stage 2 configuration from STEs with the same S2VMID is considered interchangeable by the SMMU.

Note: Software must ensure that all STEs containing the same S2VMID value are identical for non- IGNORED fields permitted to be cacheable as part of a TLB entry, in the list in this section. Fields that are IGNORED because of a stage 2 bypass (STE.Config == 0b10x ) are not covered by this rule.

Note: As the properties of TLB or translation cache entries inserted from an STE depend on the fields listed here, a difference would cause TLB entries to be cached with different properties. It would be UNPREDICTABLE as to whether a TLB entry was cached using a particular STE sharing an S2VMID value, therefore the properties returned by a general TLB lookup under the given VMID become UNPREDICTABLE.

## 5.2.2 Validity of STE

The following pseudocode indicates whether an STE is considered valid or ILLEGAL, for the purposes of determining a configuration error (C\_BAD\_STE). Further checks are required (for example, on the extent of an incoming SubstreamID with respect to STE.S1CDMax) after an STE is discovered to be valid.

```
// IgnoreSTESTRW() // =============== // Returns TRUE if STE.STRW is unused // Returns FALSE otherwise boolean IgnoreSTESTRW( bits (3) Config, SecurityState sec_sid) // Stage 1 not implemented if SMMU_IDR0.S1P == '0' then return TRUE; // Non-Secure AND Hyp not supported if sec_sid == SS_NonSecure && SMMU_IDR0.Hyp == '0' then return TRUE; // Stage 2 translation enabled if Config == '11x' then return TRUE; // Bypass, no translations
```

```
if Config == '100' then return TRUE; // STRW is used return FALSE; // IgnoreSTES2VMID() // ================= // Returns TRUE if STE.S2VMID is ignored // Returns FALSE otherwise boolean IgnoreSTES2VMID( bits (3) Config, bits (2) STRW, SecurityState sec_sid) if Config == '0xx' then // Translation is disabled return TRUE; if sec_sid == SS_NonSecure && SMMU_IDR0.S2P == '0' then // STE is NS and NS stage 2 is not implemented return TRUE; if sec_sid == SS_Secure && SMMU_S_IDR1.SEL2 == '0' then // STE is Secure and S-stage 2 not implemented return TRUE; if Config == '100' then // Bypass, no translations return TRUE; if STRW != '00' && !IgnoreSTESTRW(Config, sec_sid) then // Not using an EL1 streamworld return TRUE; if sec_sid == SS_Secure && Config == '101' then // Secure, only Stage 1 return TRUE; // S2VMID is not ignored return FALSE; // Assuming SMMU_S_IDR1.SECURE_IMPL == 1, NSSTALLD may affect // the Non-secure STALL_MODEL: See section 3.12. bits (2) EffectiveSMMU_IDR0_STALL_MODEL() return SMMU_S_IDR0.STALL_MODEL == 0b00 ? (SMMU_S_CR0.NSSTALLD == 0 ? 0b00 : 0b01) : SMMU_S_IDR0.STALL_MODEL; // SteIllegal() // ============ // Returns TRUE if STE is considered ILLEGAL // Returns FALSE otherwise boolean SteIllegal(STE_t STE, bits (2) SEC_SID) // Intermediate Values SecurityState sec_sid = DecodeSecSid(SEC_SID); integer pa_range = CalcPARange(STE.S2PS, STE.S2AA64); boolean strw_unused = IgnoreSTESTRW(STE.Config, sec_sid); boolean s2vmid_ignored = IgnoreSTES2VMID(STE.Config, STE.STRW, sec_sid); bits (2) eff_idr0_stall_model = EffectiveSMMU_IDR0_STALL_MODEL(); TGSize s2tg = TG0(STE.S2TG); TGSize s_s2tg = TG0(STE.S_S2TG); boolean using_vmsa32 = SMMU_IDR5.D128 == '0' && STE.S2AA64 == '0'; boolean using_vmsa64 = STE.S2AA64 == '1'; boolean using_vmsa128 = SMMU_IDR5.D128 == '1' && STE.S2AA64 == '0'; // See the definition of the STE.EATS field in section 5.2 boolean constr_unpred_EATS_S2S; // See the definition of the STE.S2T0SZ field in section 5.2 boolean constr_unpred_S2T0SZ_oor_ILLEGAL; if SMMU_AIDR.ArchMajorRev == '0000' && SMMU_AIDR.ArchMinorRev == '0000' then constr_unpred_EATS_S2S = ConstrainUnpredictableBool(); constr_unpred_S2T0SZ_oor_ILLEGAL = ConstrainUnpredictableBool(); else // In SMMUv3.1 and later, these cases are always ILLEGAL constr_unpred_EATS_S2S = FALSE; constr_unpred_S2T0SZ_oor_ILLEGAL = TRUE;
```

```
// Check if Valid if STE.V == '0' then return TRUE; // Check if performing Translation if STE.Config == '0xx' then return FALSE; // Check STE.Config[0] if STE.Config == '1x1' && SMMU_IDR0.S1P == '0' then // Stage 1 enabled but not supported return TRUE; // Check for cases where stage 2 translation is enabled but not supported if STE.Config == '11x' then if SMMU_IDR0.S2P == '0' then // Stage 2 not supported return TRUE; if SMMU_IDR0.S2P == '1' && sec_sid == SS_Secure && SMMU_S_IDR1.SEL2 == '0' then // Secure stage 2 not supported return TRUE; if using_vmsa32 && sec_sid != SS_NonSecure then // Cannot use Secure or Realm stage 2 in VMSAv8-32 LPAE return TRUE; // Check ATS configuration if ((sec_sid == SS_NonSecure && SMMU_IDR0.ATS == '1') || (sec_sid == SS_Realm && SMMU_R_IDR0.ATS == '1')) && STE.Config != 'x00' then // Needs to be NS/Realm, ATS enabled, and not Bypass if STE.EATS == '10' then // Split-stage ATS mode if STE.Config != '111' || STE.S2S == '1' || SMMU_IDR0.NS1ATS == '1' then // Either STE not configured for split-stage ATS // or it's not supported return TRUE; if STE.EATS == '01' && STE.S2S == '1' then // Full ATS mode if STE.Config == '11x' || constr_unpred_EATS_S2S then // if stage 2 enabled or CONSTRAINED UNPREDICTABLE for SMMUv3.0 return TRUE; if STE.EATS == '11' then if ((sec_sid == SS_Realm && SMMU_R_IDR3.DPT == 1) || (sec_sid == SS_NonSecure && SMMU_IDR3.DPT == 1)) && !strw_unused && STE.STRW != '00' then // StreamWorld other than EL1 is ILLEGAL for DPT use return TRUE; if sec_sid == SS_Realm && SMMU_R_IDR3.DPT == 1 && STE.DPT_VMATCH != '00' then // For Realm, the only permitted DPT_VMATCH is 0b00 return TRUE; // Check STE.STRW if sec_sid != SS_Secure && !strw_unused && STE.STRW == 'x1' then // Reserved NS & R STRW values are ILLEGAL if STRW is used return TRUE; if sec_sid == SS_Secure && !strw_unused && STE.STRW == '11' then // Reserved S STRW value is ILLEGAL if STRW used return TRUE;
```

```
if sec_sid == SS_Secure && !strw_unused && STE.STRW == '01' && SMMU_IDR0.RME_IMPL == '1' then // EL3 is not supported if RME is supported return TRUE; if sec_sid == SS_Secure && SMMU_S_IDR1.SEL2 == '0' && STE.STRW == '10' && STE.Config == '101' then // Secure EL2(-E2H) but Secure EL2 not supported return TRUE; // Stage 1 Translation if STE.Config == '1x1' then // Check STE.S1STALLD if STE.S1STALLD == '1' then if sec_sid == SS_NonSecure && eff_idr0_stall_model != '00' then // NS Stall Model != Stall and Terminate return TRUE; if sec_sid == SS_Secure && SMMU_S_IDR0.STALL_MODEL != '00' then // S Stall Model != Stall and Terminate return TRUE; if sec_sid == SS_Realm && SMMU_R_IDR0.STALL_MODEL == '01' then // R Stall model does not support stalling return TRUE; // Check STE.S1CDMax // 2^S1CDMax - Number of CDs pointed to by S1ContextPtr. // The allowable range is 0 to SMMU_IDR1.SSIDSIZE if SMMU_IDR1.SSIDSIZE != '00000' then if UInt(STE.S1CDMax) > UInt(SMMU_IDR1.SSIDSIZE) then return TRUE; // Check STE.S1Fmt if substreams are supported if SMMU_IDR1.SSIDSIZE != '00000' && STE.S1CDMax != '00000' && // and 2-level CD table not supported. SMMU_IDR0.CD2L == '0' && // it is ILLEGAL to set S1Fmt != 00 (11 behaves as 00) (STE.S1Fmt == '01' || STE.S1Fmt == '10') then return TRUE; // Check STE.S1ContextPtr // by checking if PA/IPA is out of range if STES1ContextPtrOutOfRange(STE.Config, STE.S1ContextPtr) then return TRUE; // Stage 2 Translation - SMMU_IDR0.S2P already checked above if STE.Config == '11x' then // Check STE.S2FWB if using_vmsa32 && SMMU_IDR3.FWB == '1' && STE.S2FWB == '1' then // Cannot use FWB in VMSAv8-32 LPAE return TRUE; // Check STE.S2S if STE.S2S == '1' then if eff_idr0_stall_model == '01' then // stall_model doesn't support stalls, but S2S == 1 return TRUE; if sec_sid == SS_Realm && SMMU_R_IDR0.STALL_MODEL == '01' then // Realm state does not support stall return TRUE; if eff_idr0_stall_model == '10' && STE.S2S == '0' then // stall_model forcing stall, but S2S == 0 return TRUE;
```

```
// Check STE.S2AA64 if using_vmsa32 && SMMU_IDR0.TTF == 'x0' then // STE is VMSAv8-32 LPAE but not supported return TRUE; if using_vmsa64 && SMMU_IDR0.TTF == '0x' then // STE is VMSAv8-64 but not supported return TRUE; // Check STE HW Translation Table Update of stage 2 Access flag and Dirty state if (STE.S2HA == '1' || STE.S2HD == '1') && (using_vmsa32 || SMMU_IDR0.HTTU == '00') then // No flag updates supported by the system // or STE is VMSAv8-32 LPAE at stage 2 // yet S2HA OR S2HD set return TRUE; if STE.S2HD == '1' && SMMU_IDR0.HTTU == '01' then // SMMU only supports Access flag update, not Dirty state return TRUE; if STE.S2HAFT == '1' && STE.S2HA == '0' && SMMU_IDR0.HTTU == '11' then // Stage 2 hardware update of Access flag in Table descriptors is enabled, // but hardware update of Access flag is not return TRUE; // Check STE.S2TG if !using_vmsa32 && !GranuleSupported(s2tg) then // unsupported granule size, or Reserved value return TRUE; // Check STE.S2TTB if STES2TTBOutOfRange(using_vmsa128, STE.S2DS, STE.S2TTB, s2tg, pa_range) then return TRUE; // Check STE.S2T0SZ if !using_vmsa32 && STES2T0SZInvalid(using_vmsa128, STE.S2DS, STE.S2T0SZ, s2tg) && constr_unpred_S2T0SZ_oor_ILLEGAL then return TRUE; // Check consistency of S2 Translation fields if ((using_vmsa32 && STEWalkConfigInconsistentAA32(STE.S2T0SZ, STE.S2SL0)) || (using_vmsa64 && STEWalkConfigInconsistentAA64(STE.S2T0SZ, STE.S2DS, STE.<S2SL0_2,S2SL0>, s2tg)) || (using_vmsa128 && STEWalkConfigInconsistentD128(STE.S2T0SZ, STE.S2SKL, s2tg))) then return TRUE; // Secure version of above 4 cases if sec_sid == SS_Secure then // Check STE.S_S2TG if !GranuleSupported(s_s2tg) then return TRUE; // Check STE.S_S2TTB if STES2TTBOutOfRange(using_vmsa128, STE.S2DS, STE.S_S2TTB, s_s2tg, pa_range) then return TRUE; // Check STE.S_S2T0SZ if STES2T0SZInvalid(using_vmsa128, STE.S2DS, STE.S_S2T0SZ, s_s2tg) then return TRUE; // Check consistency of S2 Translation fields // A Secure STE with stage 2 translation enabled is not permitted to use VMSAv8-32. if ((using_vmsa64 && STEWalkConfigInconsistentAA64(STE.S_S2T0SZ, STE.S2DS, STE.<S_S2SL0_2,S_S2SL0>, s_s2tg)) || (using_vmsa128 &&
```

```
STEWalkConfigInconsistentD128(STE.S_S2T0SZ, STE.S_S2SKL, s_s2tg))) then return TRUE; // Check Endianness if SMMU_IDR0.TTENDIAN == '10' && STE.S2ENDI == '1' then // Only little-endian supported, but STE configures big-endian return TRUE; if SMMU_IDR0.TTENDIAN == '11' && STE.S2ENDI == '0' then // Only big-endian supported, but STE configures little-endian return TRUE; // Check STE.S2PIE if SMMU_IDR3.S2PI == '1' && STE.S2PIE == '1' && using_vmsa32 then // Stage 2 permission indirection is enabled, but Stage 2 uses VMSAv8-32 return TRUE; // Check STE.S2POE if SMMU_IDR3.S2PO == '1' && STE.S2POE == '1' then if STE.S2PIE == '0' && !using_vmsa128 then // Stage 2 Overlay is enabled, but Stage 2 Indirect permissions is not return TRUE; if SMMU_IDR3.PBHA == '1' && STE.<S2HWU62,S2HWU61,S2HWU60,S2HWU59> != '0000' then // Stage 2 Overlay is enabled, but STE bits corresponding to PBHA are not ZERO return TRUE; // Check STE.S2POI for i = 0 to 15 if STE.S2POI<(i*4)+:4> IN { '0001', '0101' } then // Stage 2 Overlay is enabled, but S2POI contains a Reserved encoding return TRUE; // Check STE.S2VMID if !s2vmid_ignored && SMMU_IDR0.VMID16 == '0' && STE.S2VMID<15:8> != '00000000' then // Implementation only supports 8-bit VMIDs // but STE VMID > 8-bits and STE.S2VMID isn't ignored return TRUE; // Check STE.VMSPtr if STE.Config == '111' && STE.S1MPAM == '1' && STEVMSPtrOutOfRange(STE.VMSPtr) then // The VMSPtr is enabled, and is out of range return TRUE; // No ILLEGAL conditions met return FALSE; // Non-secure and Realm states must support the same PARTID_MAX effective_MPAM_PARTID_MAX(IS_SECURE) = IS_SECURE ? SMMU_S_MPAMIDR.PARTID_MAX : SMMU_MPAMIDR.PARTID_MAX; // STES2T0SZInvalid() // ================== // Returns TRUE if (S_)S2T0SZ value is outside the range that // is valid when stage 2 is implemented and is VMSAv8-64 or VMSAv9-128 // Returns FALSE otherwise boolean STES2T0SZInvalid( boolean using_vmsa128, bit DS, bits (6) S2T0SZ, TGSize S2TG) integer txsz_min, txsz_max; integer s2t0sz = UInt(S2T0SZ); integer ias = IAS(); // find txsz_max // Small translation table supported if SMMU_IDR3.STT == '1' && S2TG IN {TGSize_4KB, TGSize_16KB} then txsz_max = 48;
```

```
// Small translation table supported and S2TG not IN {4KB, 16KB} elsif SMMU_IDR3.STT == '1' then txsz_max = 47; // Small translation table not supported else txsz_max = 39; // find txsz_min // SMMUv3.0 if SMMU_AIDR.ArchMajorRev == '0000' && SMMU_AIDR.ArchMinorRev == '0000' then txsz_min = 64-ias; // SMMUv3.1 onwards elsif using_vmsa128 then txsz_min = MAX(8, 64-ias); elsif S2TG == TGx_64KB || (SMMU_IDR5.DS == '1' && DS == '1') then txsz_min = Max(12, 64-ias); else // S2TG is 4KB or 16KB and 52-bit or larger not supported txsz_min = Max(16, 64 - ias); return (s2t0sz < txsz_min || s2t0sz > txsz_max);
```