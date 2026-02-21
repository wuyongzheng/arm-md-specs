## 3.24 Device Permission Table

The Device Permission Table and associated behavior provides a mechanism to enforce the association between granules of physical address space and the memory footprint of virtual machines.

Use of the DPT is only supported for StreamIDs that are configured to use StreamWorld EL1, and otherwise results in C\_BAD\_STE.

The architecture supports an independent DPT for each of Non-secure and Realm states.

A DPT is an in-memory structure that describes the accessibility of each granule of configured physical address space as one of the following:

- No access is permitted to the granule.
- The granule is accessible for accesses associated with some specific VMIDs.
- The granule is accessible regardless of VMID association.

DPT configuration is not required for StreamIDs where ATS is disabled or configured for Split-stage operation.

See 3.9.1 ATS Interface and STE.EATS.

The Device Permission Table, DPT, is independently optional for each of the Non-secure and Realm programming interfaces:

- Support for DPT in the Non-secure state is indicated in SMMU\_IDR3.DPT.
- Support for DPT in the Realm state is indicated in SMMU\_R\_IDR3.DPT.

## 3.24.1 DPT check

A successful DPT lookup resolves to the following information for a granule or contiguous region:

- A No Access indication. This indicates that an access to the region is not permitted and that the SMMU is not permitted to create a DPT TLB entry for the lookup. See: 3.24.2 DPT caching behavior .
- Whether an access is permitted according to the Access Control (AC), W and VMID fields returned by the lookup.

The DPT check includes all of the following:

- If the address input into the DPT check is outside the address range configured in SMMU\_(R\_)DPT\_BASE\_CFG.DPTPS, this indicates No Access, and the DPT check fails as a Device Access fault.
- If a DPT descriptor indicates No Access, the DPT check fails as a Device Access fault. There are two ways for a descriptor to indicate No Access:
- -A Level 0 No Access entry.
- -The encoding of the A[1:0] field in a Level 1 descriptor indicates No Access.
- If the region is marked as W = 0 and the incoming transaction is a write access, the DPT check fails as a Device Access fault.

Note: In certain coherency protocol implementations, if the DPT grants a fully-coherent client with access to a page, it is not possible to enforce separate read and write permissions. In this case, the DPT W bit is ignored (that is, treated as 1) when processing fully-coherent translated transactions. The method by which system software discovers if write permission can be enforced for each fully-coherent client is system-specific.

- The AC and VMID fields from the DPT are checked against the STE.{DPT\_VMATCH, S2VMID} fields for the StreamID of the access that is being checked. This table indicates whether the VMID in the DPT entry is required to match the STE.S2VMID field for the access in order for the access to be permitted:

| STE.DPT_VMATCH   | AC= 0b00   | AC= 0b01   | AC= 0b10   |
|------------------|------------|------------|------------|
| 0b00             | Yes        | Yes        | No         |
| 0b01             | Yes        | No         | No         |
| 0b10             | No         | No         | No         |

Note: For Realm STEs, DPT\_VMATCH is always 0b00 .

If VMID is required to match and does not match, the DPT check fails as a Device Access fault.

Note: The DPT check might generate a Device Access fault only if DPT configuration did not lead to a DPT lookup fault. See section: 3.24.4 DPT lookup errors .

Note: In the absence of correct DPT TLB maintenance, the DPT check might be made using stale information cached in the DPT TLB.

The output PA space of the region is determined as follows:

- For the Non-secure DPT, the output PA space is Non-secure.
- For the Realm DPT the output PA space is determined from AC:
- -If AC is 0b01 or 0b10 , the output PA space is Non-secure.
- -Otherwise, the output PA space is Realm.

Note: The STE.DPT\_VMATCH field has no effect on the output PA space for the access.

## 3.24.2 DPT caching behavior

For a StreamID with STE.EATS == 0b11 , there are two situations in which the result of a lookup is permitted to be cached in a DPT TLB:

- When an ATS Translation Request results in a successful ATS Translation Completion with any permissions other than R == W == 0, the SMMU is permitted to create a DPT TLB entry based on either of:
- -The final enabled stage of translation that the request was subject to.
- -All enabled stages of translation that the request was subject to.

In both cases, this is only permitted within the bounds specified later in this subsection.

If the ATS Translation Request did not result in a successful ATS Translation Completion only because of a GPC fault on the output address, then the SMMU is still permitted to create a DPT TLB entry for it in a DPT TLB that does not cache GPT information.

Note: If hardware update of the Access flag or dirty state is enabled, the SMMU still follows the existing rules for performing the updates both speculatively and in response to an ATS translation request. See 3.13.7 ATS, PRI and translation table flag update .

DPT TLB entries are never created from the result of ATS Translation Requests that bypass all stages of translation. This includes the case where STE.S1DSS configuration means that Translation Requests with SSV=0 effectively bypass stage 1, on a stream where stage 2 is configured for bypass.

- When a walk of the DPT does not result in a DPT lookup fault, and the DPT information returned by the walk does not indicate No Access, the SMMU is permitted to create a DPT TLB entry based on the result of the DPT lookup.

This property applies both for DPT walks caused by an incoming transaction, and DPT walks that are performed speculatively by the SMMU.

Note: This means software must ensure consistent configuration of the DPT and the final enabled stage of translation.

The properties of a DPT TLB are:

- It is indexed by SEC\_SID and the final Output Address of the translation.
- Entries are permitted to cover an address region up to the effective size of the translation, as determined by the level of the translation result and the Contiguous bit for a translation table walk, or the level of the DPT lookup and the Contig field for a DPT walk.
- If the result of an ATS Translation request covers an address region smaller than the configured region size in SMMU\_(R\_)DPT\_BASE\_CFG.DPTGS, the SMMU is permitted to use either region size.
- The entries distinguish whether access to the region is read-only, or has read and write permissions.
- The entries determine the Output physical address space of the translation. For Realm state, this is either Realm or Non-secure PA space. For Non-secure state, this is always Non-secure PA space.
- The entries determine whether accesses to a region must be associated with a specific VMID or not. If the region is associated with a specific VMID, the VMID is also part of the entry.
- Entries inserted based on the result of an ATS Translation Completion might contain less information than can be determined from the result of a DPT walk.

Note: The DPT format cannot express permission for a write-only region of memory and therefore write-only permission is instead treated as read and write permission by the DPT and DPT checks.

Implementations are permitted to combine DPT and GPT information in TLBs. In an implementation that combines DPT and GPT information in a TLB, all of the following apply:

- The SMMU removes entries as part of both CMD\_DPTI\_* operations and TLBI *PA* operations that match the properties of the entries.
- Any use of a DPT TLB entry cannot allow an access to bypass the requirements of Granule Protection Checks.

When a DPT TLB entry is created because of a successful ATS Translation Completion, it is permitted to be cached according to all enabled stages of translation or the final enabled stage of translation that was used to service the ATS Translation Request, in a manner consistent with observing the following values from a DPT walk for the PA returned in the ATS Translation Completion:

| DPT Field   | Value                                                                                                                                                                                                                                                                                                                                                                        |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A[x]        | Implicitly grants access to the appropriate granule or contiguous region if the ATS Translation Completion indicated any access permission.                                                                                                                                                                                                                                  |
| W           | The write permission returned by the combined or final stage of translation that was used to generate the ATS Translation Completion. For translation stages using hardware update of dirty state then a writable-clean translation does not count as granting write access, unless the ATS Translation Request also caused the translation to transition to writable-dirty. |
| AC          | For a Non-secure stream, 0b00 . For a Realm stream: - If the output PA space was Non-secure, 0b01 . - If the output PA space was Realm, 0b00 .                                                                                                                                                                                                                               |
| VMID        | STE.S2VMID value for the StreamID for which the ATS Translation Request was performed.                                                                                                                                                                                                                                                                                       |

| DPT Field   | Value                                                                                                                                                                                                                                                                                                         |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Contig      | The region size returned by the combined or final stage of translation that was used to generate the ATS Translation Completion, but the SMMUlimits the size to never exceed the level 0 DPT size configured in SMMU_(R_)DPT_BASE_CFG.L0DPTSZ, or a size of 1GB if L0DPTSZ is programmed to a Reserved value. |

The configuration of STE.DPT\_VMATCH does not affect the attributes of any DPT TLB entry.

See also 4.6 DPT maintenance .

## 3.24.2.1 DPT TLB caching and Device Access faults

The SMMU is only permitted to generate a Device Access fault directly from information cached in a DPT TLB entry in the following situation:

- The DPT TLB entry was created from the result of a DPT walk that did not result in a DPT lookup fault and the information returned by the DPT lookup did not indicate No Access.

The SMMU is not permitted to generate a Device Access fault directly from information cached in a DPT TLB entry in the following situation:

- The DPT TLB entry was created from the result of the translation table walk performed as part of responding to an ATS Translation Request.

In the case where the SMMU is not permitted to generate a Device Access fault based on an existing DPT TLB entry, the SMMU is required to perform a DPT walk in order to correctly perform the DPT check.

The SMMU is permitted to not generate a Device Access fault in any situation where an existing DPT TLB entry grants access for the ATS Translated transaction being checked.

## 3.24.2.2 Changing the DPT structure for a region of memory

If the configuration of the DPT expresses a consistent set of attributes for a region of memory, and the configuration of the DPT is changed such that the attributes for that region of memory remain the same and consistent, then DPT checks continue to be performed correctly even in the absence of DPT TLB maintenance operations. This includes the following example cases:

- Replacing a set of Level 1 entries that have the Contig field set to zero with a set of Level 1 entries that have the Contig field configured to the size of the region.
- Replacing a single Level 0 Block entry with a Level 0 Table entry that points to a level 1 table containing Level 1 entries.
- Replacing a Level 0 Table entry that points to a level 1 table containing Level 1 entries with a single Level 0 Block entry.

In this case, the SMMU might still fetch from the level 1 table until completion of a DPT TLB maintenance operation that removes the Level 0 Table entry from the DPT TLB.

## 3.24.3 DPT format and lookup process

The DPT has two levels, level 0 and level 1.

All descriptors are 8 bytes in length, and are little-endian.

All tables are aligned to their size in memory.

DPT lookups are made with the memory attributes configured in SMMU\_(R\_)CR1.{TABLE\_IC, TABLE\_OC, TABLE\_SH}, and the Read-allocate hint in SMMU\_(R\_)DPT\_BASE.RA.

DPT lookups are made with the MPAM STE.{PARTID, PMG} values configured in the STE for the StreamID for which the lookup is performed. The MPAM PARTID space is the same as the space that would be used to fetch stage 2 translation tables for that StreamID.

DPT lookups are made with behavior consistent with PBHA being disabled or not implemented.

Note: If SMMU\_R\_IDR3.MEC is 1, DPT lookups for Realm state are performed with the MECID value configured in SMMU\_R\_GMECID.

The L0DPT base address, and next-level table base addresses for L1DPT tables, are aligned by the hardware.

The input PA is interpreted as described in Table 3.35.

In Table 3.35, the placeholder values are:

- oas is the decoded value of SMMU\_IDR5.OAS as a bit width.
- dptps is the decoded value of SMMU\_(R\_)DPT\_BASE\_CFG.DPTPS as a bit width.
- l0dptsz is the decoded value of SMMU\_(R\_)DPT\_BASE\_CFG.L0DPTSZ as a bit width.
- dptgs is the decoded value of SMMU\_(R\_)DPT\_BASE\_CFG.DPTGS as a bit width.

Table 3.35: Input PA interpretation for DPT lookups

| PA bits                 | Usage                           |
|-------------------------|---------------------------------|
| [ oas -1: dptps ]       | Device Access fault if non-zero |
| [ dptps -1: l0dptsz ]   | L0DPT index                     |
| [ l0dptsz -1: dptgs +1] | L1DPT index                     |
| [ dptgs ]               | Level 1 page descriptor index   |
| [ dptgs -1:0]           | IGNORED                         |

Note: Bits [63: oas ] of the input PA are processed according to the general requirements for handling of addresses in ATS-related transactions.

The algorithm for the DPT walk process is as follows:

1. The SMMU\_(R\_)DPT\_BASE register points at the base of the level 0 table.
2. The SMMU uses bits [ dptps -1: l0dptsz ] of the input PA as the index into the level 0 table.

Note: Each level 0 entry is 8 bytes, so the offset into the level 0 table is (level 0 index) * (8 bytes).

Note: There is one level 0 table. Every entry in the level 0 table is one of the three level 0 descriptors, or Invalid.

The size of the level 0 table is determined by (number of entries) * (8 bytes), where (number of entries) is DPTPS / L0DPTSZ.

3. If the level 0 entry is a No Access, Block or invalid entry, then the DPT walk is complete. Otherwise, the level 0 entry is a level 0 Table entry and it contains a pointer to the base of a level 1 table.

Note: There are many level 1 tables. The size of all the level 1 tables is the same, and determined by (number of entries) * (8 bytes), where (number of entries) is (L0DPTSZ / DPTGS) / 2.

4. The SMMU uses bits [ l0dptsz -1: dptgs +1] of the input PA as the index into the level 1 table determined in the previous step.

Note: Every entry in a level 1 table is a level 1 descriptor.

Note: Every entry in a level 1 table is 8 bytes, so the offset into a level 1 table is (level 1 index) * (8 bytes).

5. The SMMU decodes the level 1 entry according to the rules for a level 1 descriptor. Bit [ dptgs ] of the input PA might be used to select between the upper and lower half of the descriptor, depending on the value of A[1:0] in the descriptor.

The DPT walk is now complete.

Note: Depending on PMCG configuration, DPT lookups are counted in PMCG events.

## 3.24.3.1 DPT descriptor formats

There are four DPT descriptor formats:

1. Level 0 No Access entry: Indicates that a region of size L0DPTSZ is not accessible.
2. Level 0 Block entry: Indicates that a region of size L0DPTSZ is accessible with some constraints on Access Control and VMID.
3. Level 0 Table entry: Includes a pointer to a Level 1 entry.
4. Level 1 entry: Indicates either No Access, or Access Control and VMID information, for either two granules or a contiguous region.

An entry that does not match any of the formats at the appropriate level is invalid.

## 3.24.3.1.1 Level 0 No Access entry

Figure 3.10: Level 0 No Access entry

<!-- image -->

Note: In all cases, if a bit described as RES0 is non-zero, or a field is configured to a Reserved value, the descriptor is Invalid. See section 3.24.4 DPT lookup errors .

At level 0, a descriptor with bits [1:0] set to 0b00 indicates No Access.

A level 0 No Access entry is not permitted to be cached in a DPT TLB.

## 3.24.3.1.2 Level 0 Block entry

Figure 3.11: Level 0 Block entry

<!-- image -->

Note: In all cases, if a bit described as RES0 is non-zero, or a field is configured to a Reserved value, the descriptor is Invalid. See section 3.24.4 DPT lookup errors .

At level 0, a descriptor with bits [1:0] set to 0b01 indicates a Block descriptor.

The AC and W fields are valid.

The encoding of the W field is:

The encoding of the AC field is:

| Value   | Meaning                     |
|---------|-----------------------------|
| 0b0     | Write access not permitted. |
| 0b1     | Write access permitted.     |

| Value   | Meaning                                                                    |
|---------|----------------------------------------------------------------------------|
| 0b00    | VMID field is valid and is checked unless STE.DPT_VMATCH is 0b10 .         |
| 0b01    | VMID field is valid and is checked unless STE.DPT_VMATCH is 0b01 or 0b10 . |
| 0b10    | VMID field is RES0.                                                        |
| 0b11    | Reserved, invalid.                                                         |

Note: For a Realm STE, DPT\_VMATCH is always 0b00 and therefore VMID is always checked when AC is 0b00 or 0b01 .

Note: For the Realm DPT, the value of AC determines the output PA space.

If SMMU\_IDR0.VMID16 is 0, then VMID[15:8] are RES0 regardless of the value of AC.

A level 0 DPT Block entry that does not generate a DPT lookup fault is permitted to be cached in a TLB as though the Block is a contiguous region of granules each of the size configured in SMMU\_(R\_)DPT\_BASE\_CFG.DPTGS.

## 3.24.3.1.3 Level 0 Table entry

Figure 3.12: Level 0 Table entry

<!-- image -->

|    | 56   | 63   | 55             |                | 32   |
|----|------|------|----------------|----------------|------|
|    | MBZ  |      |                | Address[55:12] |      |
| 31 |      |      |                | 12 11          | 1 0  |
|    |      |      | Address[55:12] |                | 0b11 |

Note: In all cases, if a bit described as RES0 is non-zero, or a field is configured to a Reserved value, the descriptor is Invalid. See section 3.24.4 DPT lookup errors .

At level 0, a descriptor with bits [1:0] set to 0b11 indicates a Table descriptor.

The Address field indicates the next-level base address of a level 1 table.

The address is aligned by the hardware to the size of the level 1 table.

Bits above the implemented physical address size, indicated in SMMU\_IDR5.OAS, are RES0.

A level 0 DPT Table entry that does not generate a DPT lookup fault is permitted to be cached in a TLB.

## 3.24.3.1.4 Level 1 entry

Figure 3.13: Level 1 entry

<!-- image -->

| 63    | 48 47   |        |     | 37   | 36 35   | 34   | 33 32   |
|-------|---------|--------|-----|------|---------|------|---------|
| VMID1 |         | MBZ    |     | W1   |         | AC1  | MBZ     |
| 31    | 16 15   | 12 11  | 8 7 | 5    | 4       | 3 2  | 1 0     |
| VMID0 | MBZ     | Contig | MBZ | W0   | AC0     |      | A[1:0]  |

Note: In all cases, if a bit described as RES0 is non-zero, or a field is configured to a Reserved value, the descriptor is Invalid. See section 3.24.4 DPT lookup errors .

A level 1 entry represents either:

- The attributes for two adjacent granules, which might have different values.
- The attributes for a naturally-aligned contiguous region, as indicated in the Contig field.

The encoding of the A[1:0] field is as follows, and affects the interpretation of the Contig field:

| A[1]   | A[0]   | Contig   | Behavior                                                                                        |
|--------|--------|----------|-------------------------------------------------------------------------------------------------|
| 0b0    | 0b0    | RES0     | No Access to upper or lower granule.                                                            |
| 0b0    | 0b1    | RES0     | No Access to upper granule. Lower granule controlled by AC0, W0, and VMID0.                     |
| 0b1    | 0b0    | RES0     | Upper granule controlled by AC1, W1, and VMID1. No Access to lower granule.                     |
| 0b1    | 0b1    | Zero     | Upper granule controlled by AC1, W1, and VMID1. Lower granule controlled by AC0, W0, and VMID0. |
| 0b1    | 0b1    | Non-zero | Contiguous region controlled by AC0, W0, and VMID0.                                             |

The encoding of the Contig field is as follows:

If A is 0b00 , all other fields in the descriptor are RES0.

If A is 0b01 or 0b10 , then Contig is RES0 and the descriptor describes the properties for two granules.

If A is 0b11 and Contig is zero, then the descriptor describes the properties for two granules.

If the descriptor describes the properties for two granules, then:

- Access to the upper granule is governed by A[1], AC1, W1 and VMID1. If A[1] is 0, then the AC1, W1 and VMID1 fields are RES0.
- Access to the lower granule is governed by A[0], AC0, W0 and VMID0. If A[0] is 0, then the AC0, W0 and VMID0 fields are RES0.

If A is 0b11 and Contig is non-zero, the AC1, W1 and VMID1 fields are RES0 and only the AC0, W0 and VMID0 fields are considered. The value of Contig indicates the size of the contiguous region.

If Contig is not RES0, then encodings of Contig that select a region size greater than L0DPTSZ are Reserved.

If Contig selects a Reserved encoding, the descriptor is invalid.

If SMMU\_IDR0.VMID16 is 0, then VMID0[15:8] and VMID1[15:8] are RES0 regardless of the values of ACx.

The encoding and meaning of the ACx and Wx fields is the same as for the AC and W fields in a Level 0 Block entry.

It is possible that contiguous regions are inconsistently configured in the DPT:

- In the case where a region is composed of descriptors that provide the same attributes, and differ only by the value of the Contig field, the DPT check is correctly applied.
- In the case where a region is composed of descriptors that provide different attributes, and the values of the Contig fields produce overlapping regions, the SMMU might use any of the configured attributes in the overlapping regions.

If the lookup of a level 1 DPT entry does not generate a DPT lookup fault, then:

- If Contig is 0, each half of the entry that does not indicate No Access is permitted to be cached in a TLB.
- If Contig is not RES0 and is non-zero, the entry is permitted to be cached in a TLB as a naturally-aligned contiguous region of granules, each of the size configured in SMMU\_(R\_)DPT\_BASE\_CFG.DPTGS.

| Value     | Meaning                          |
|-----------|----------------------------------|
| 0b0000    | No contiguity                    |
| 0b0001    | 64KB. Reserved if DPTGS is 64KB. |
| 0b0010    | 2MB                              |
| 0b0011    | 32MB                             |
| 0b0100    | 512MB                            |
| 0b0101    | 1GB                              |
| 0b0110    | 16GB                             |
| 0b0111    | 64GB                             |
| Otherwise | Reserved                         |

## 3.24.4 DPT lookup errors

In the DPT check, there are two classes of fault that can occur:

- The DPT lookup process succeeds, but does not grant access for the transaction being checked. This is referred to as a Device Access fault, and is reported as F\_TRANSL\_FORBIDDEN. The criteria for generating a Device Access Fault are specified in 3.24.1 DPT check and section 3.24.2.1 DPT TLB caching and Device Access faults .
- The DPT lookup process fails. This is referred to as a DPT lookup fault, and is reported both in SMMU\_(R\_)DPT\_CFG\_FAR and as F\_TRANSL\_FORBIDDEN. See 7.3.8 F\_TRANSL\_FORBIDDEN .

The fault reporting priority for DPT lookup faults is as follows:

|   Priority | Reason                             | Reported as    |   Level |
|------------|------------------------------------|----------------|---------|
|          1 | DPT_WALK_EN = 0                    | DPT_DISABLED   |       0 |
|          2 | Invalid DPT register configuration | DPT_WALK_FAULT |       0 |
|          3 | GPC fault on level 0 fetch         | DPT_GPC_FAULT  |       0 |
|          4 | External abort on level 0 fetch    | DPT_EABT       |       0 |
|          5 | Invalid level 0 descriptor         | DPT_WALK_FAULT |       0 |
|          6 | GPC fault on level 1 fetch         | DPT_GPC_FAULT  |       1 |
|          7 | External abort on level 1 fetch    | DPT_EABT       |       1 |
|          8 | Invalid level 1 descriptor         | DPT_WALK_FAULT |       1 |

If the SMMU encounters any of these faults while performing a DPT lookup, and SMMU\_(R\_)DPT\_CFG\_FAR.FAULT = 0, the SMMU reports the information in SMMU\_(R\_)DPT\_CFG\_FAR and sets the FAULT bit to 1. If the FAULT bit is already 1, the fault is not reported in SMMU\_(R\_)DPT\_CFG\_FAR.

When the SMMU makes a fault active in SMMU\_(R\_)DPT\_CFG\_FAR, it additionally makes the corresponding SMMU\_(R\_)GERROR.DPT\_ERR active, if the value of SMMU\_(R\_)GERROR(N).DPT\_ERR does not already indicate an active fault. If a fault is observable in SMMU\_(R\_)GERROR.DPT\_ERR, then it has already been made observable in SMMU\_(R\_)DPT\_CFG\_FAR.

If a client-originated access generates a DPT lookup fault, and the abort response arising from this is visible to the device, then the corresponding update of SMMU\_(R\_)GERROR.DPT\_ERR is also observable.

If a DPT lookup fault is observable in SMMU\_(R\_)GERROR.DPT\_ERR, or the abort arising from that fault is visible to the client device then completion of a CMD\_SYNC on an appropriate Command queue for the Security state guarantees observability of the corresponding F\_TRANSL\_FORBIDDEN in the Event queue, or that the F\_TRANSL\_FORBIDDEN has been discarded if the Event queue is unwritable, consistent with the existing rules for Event queue observability.

If the F\_TRANSL\_FORBIDDEN event arising from a DPT lookup fault is observable, then the corresponding update of SMMU\_(R\_)GERROR.DPT\_ERR is also observable.

The SMMU is not required to report any of these faults if a DPT check can be resolved by a successful DPT TLB lookup.

The following configurations are treated as Invalid DPT register configuration:

- Reserved value 0b111 , or a value exceeding SMMU\_IDR5.OAS, for DPTPS.
- Invalid or Reserved encoding of DPTGS.
- Invalid or Reserved encoding of L0DPTSZ.

- Configuration of L0DPTSZ to an address size that exceeds the address sizes in SMMU\_IDR5.OAS or DPTPS.

A DPT entry is treated as invalid if any of the following apply:

- The entry does not match one of the descriptor formats for the given level of lookup.
- The entry matches one of the formats for the given level of lookup, but has any RES0 bit set to 1 in the descriptor.
- The entry contains a field that is not RES0 and is configured to a Reserved encoding.

If a DPT\_GPC\_FAULT is reported then the corresponding GPC fault information is reported in the appropriate SMMU\_ROOT\_GPT\_CFG\_FAR or SMMU\_ROOT\_GPF\_FAR register, with REASON = TRANSLATION and FAULTCODE = GPF\_WALK\_EABT.

If a DPT\_EABT is reported as the result of a RAS error, then the corresponding RAS information is reported in RAS syndrome registers, if implemented. See 12.2 Error consumption visible through the SMMU programming interface .

## 3.24.5 DPT maintenance operations

The DPT maintenance commands remove cached DPT information from DPT TLBs regardless of whether the entry was inserted as the result of a successful ATS translation request or a walk of the DPT.

The CMD\_DPTI\_ALL and CMD\_DPTI\_PA commands have the same consumption and completion behavior as for CMD\_TLBI\_* commands, in that:

- Consumption of the command does not provide any guarantees.
- Consumption of a subsequent CMD\_SYNC on the same Command queue for which the CMD\_DPTI\_* command was issued guarantees that the appropriate invalidation has been performed, all Events and faults relating to the invalidated entries have been reported, and all client transactions using the invalidated entries have completed.

Note: Within a given security state, DPT maintenance behaves as follows:

- CMD\_DPTI\_ALL is always sufficient to invalidate all cached DPT information.
- To invalidate cached copies of a Level 0 Table descriptor, a CMD\_DPTI\_PA with Leaf as 0 and an address anywhere in the region covered by that descriptor is sufficient.
- To invalidate cached copies of a Level 0 Table descriptor as well as any Level 1 entries in the table pointed to by the Level 0 Table descriptor, a CMD\_DPTI\_PA with Leaf as 0 and SIZE matching the size of the region pointed to by the Level 0 Table descriptor and address aligned to the size of the region is sufficient.
- To invalidate cached copies of a Level 0 Block descriptor or Level 1 entries for a contiguous region, a CMD\_DPTI\_PA with Leaf as 1, SIZE matching the size of the region and an address aligned to the size of the region is sufficient.
- To invalidate cached copies of the DPT information in one granule of a non-contiguous Level 1 entry, a CMD\_DPTI\_PA with Leaf=1 and the address of the granule is sufficient.

Note: CMD\_TLBI\_* Commands and broadcast TLBI operations for stage 1 and stage 2 are not required to invalidate any DPT TLB entries. If an implementation combines GPT and DPT information in DPT TLB entries, TLBI by PA operations remove DPT TLB entries according to the requirements for TLBI by PA operations. Otherwise, TLBI by PA operations are not required to invalidate any DPT TLB entries.

The DPT maintenance operations can be found in 4.6 DPT maintenance .

## 3.24.6 Software guidance

The DPT is expected, in the general case, to be used to partition physical address space between different EL1 contexts. The statements in this section therefore generally apply to stage 2 translation configuration.

However, it is possible that future use cases might include use of the EL2-E2H StreamWorld, and in that case the statements in this section would apply to stage 1 translation configuration.

## 3.24.6.1 Access permissions considerations

The DPT configuration for a memory region should be configured to represent the most-permissive access permissions for that memory region, for the final enabled stage of translation. This means that the DPT should grant access for a given granule if any of the following are true for the final enabled stage of translation:

- The descriptor has AF = 1.
- The descriptor has AF = 0 and hardware update of the Access Flag is enabled.

This also means that the DPT should grant write access for a given granule if any of the following are true for the final enabled stage of translation:

- The descriptor grants write access. This includes the case where the descriptor is writable-dirty.
- The descriptor is writable-clean and HTTU is enabled.

## 3.24.6.2 Invalid to valid transition

Assuming that initially the translation is Invalid then software must:

1. Configure the DPT to grant access for the granule
2. Perform appropriate cache maintenance and barriers
3. Configure the final enabled stage of translation to grant access for the granule

Note: TLB maintenance is not required for Invalid to Valid transitions.

## 3.24.6.3 Valid to invalid transition

When revoking access to a granule, software must:

1. Mark the descriptor in the final enabled stage of translation as Invalid.
2. Perform the appropriate TLBI and sync operation. Note: this means that new ATS translation requests will fail, but Translated transactions may still succeed.
3. Perform the appropriate CMD\_ATC\_INV and sync operation. Note: This means the device should not issue ATS Translated transactions, other than write-backs in case of a fully-coherent device.
4. If the StreamID is associated with a fully-coherent device, issue the appropriate CMOs for the granule. This might result with device write-backs.
5. Mark the DPT configuration as invalid. Note: This means that rogue ATS Translated transactions might succeed or fail.
6. Perform the appropriate CMD\_DPTI\_* and sync operation. Note: This means that rogue ATS Translated transactions will fail.

## 3.24.6.4 Clearing DPT lookup errors

DPT lookup errors for a Security state are reported in both SMMU\_(R\_)DPT\_CFG\_FAR and SMMU\_(R\_)GERROR.DPT\_ERR, if they are not already active. This means that the algorithm for clearing a DPT lookup error, once the error is resolved, is as follows:

1. Write 0 to SMMU\_(R\_)DPT\_CFG\_FAR.FAULT. Note: This will clear the whole register to zero.
2. Acknowledge SMMU\_(R\_)GERROR.DPT\_ERR by writing SMMU\_(R\_)GERRORN.DPT\_ERR to the same value.
3. Read SMMU\_(R\_)DPT\_CFG\_FAR.FAULT again to see if a new fault occurred between steps 1 and 2.

See also:

- 3.24.4 DPT lookup errors .

## 3.24.7 Considerations for configuring Split-stage ATS versus Full ATS with DPT checking

This section is informative.

If a use case relies on direct device access to physical address space, Full ATS with DPT checks must be configured for functional, not security reasons. If direct device access to physical address space is not required, then Split-stage ATS is preferable to configuration of Full ATS with DPT checks. The two approaches have comparable protection and performance characteristics, but Split-stage ATS is simpler to configure.

Functional considerations:

- If the device interface requires direct access to physical address space, for example if it has a fully coherent cache or if PCIe peer-to-peer routing is required without routing transactions via the host Root Port, Full ATS is required in order for address-based routing to function correctly.

Security considerations:

- Both configurations still enforce granule protection checks and limit access from a device to the physical address footprint of the guest in question.
- Split-stage ATS permits the SMMU to enforce stage 2 permissions checks on Translated transactions, at a granularity of read/write/execute. Full ATS with DPT cannot distinguish these levels of permission.

Performance considerations:

- If Split-stage ATS is used, the EL2 software managing the SMMU does not need to configure the DPT for granules associated with that StreamID, and can therefore avoid the overhead of having to update the table and issue CMD\_DPTI\_* operations.
- SMMU lookup performance and cacheability is expected to be comparable between the two different configurations. On a TLB miss, DPT lookup is likely to result in fewer levels of walk.