## 4.4 TLB invalidation

The TLB invalidation commands are similar to the Armv8-A broadcast TLB invalidation messages originating from PE TLB invalidation operations. These commands only affect the SMMU TLB and do not generate any broadcast operations to other agents in the system.

Note: SMMU TLB invalidate commands might be required because:

- The SMMU or interconnect does not support broadcast TLB invalidation messages.
- The ASET flag in a Context Descriptor might cause a TLB entry to be marked as not participating in certain types of broadcast TLB invalidation, see section 3.17 TLB tagging, VMIDs, ASIDs and participation in broadcast TLB maintenance .

The Armv8-A Last Level (leaf) scope is supported, to only invalidate an indicated TLB entry and last level cache.

Entries in this section show the PE TLB invalidation instructions that have the same scope as the SMMU command being described. Broadcast TLB invalidation messages from these PE operations trigger the equivalent operation on the SMMU. The scope of broadcast TLB invalidation and SMMU TLB invalidation commands are affected by VMID Wildcards, if enabled, see section 3.17.6 VMID Wildcards and SMMU\_(*\_)CR0.VMW.

ASID and VMID parameters to TLB invalidation commands are either 8-bit or 16-bit values, as appropriate, depending on whether the SMMU implementation supports 8-bit or 16-bit ASIDs and VMIDs (SMMU\_IDR0.{ASID16,VMID16}). When support for either ASIDs or VMIDs is 8 bits, the upper 8 bits of the corresponding 16-bit parameter field are RES0. In this case, if the upper 8 bits are non-zero, the command is not required to affect TLB entries.

Note: There are some configurations where VMID is RES0. See Section 4.4.2 TLB invalidation of stage 1 .

Commands matching TLB entries on ASID disregard the ASET value with which TLB entries were inserted.

Each command specifies the minimum required scope of TLB invalidation that must be performed. An implementation is permitted to invalidate more non-locked entries than this required scope (over-invalidation) but doing so can adversely affect performance and is not recommended by Arm. Where IMPLEMENTATION DEFINED TLB locking is used, invalidation semantics set out in section 16.6.1 Configuration and translation cache locking must be observed.

Note: As described in section 4.3.8 Configuration structure invalidation semantics/rules above, a CMD\_SYNC completes when prior TLB invalidations have completed. A sequence of CMD\_TLBI\_* commands followed by a CMD\_SYNC is analogous to a sequence of TLBI instructions followed by a DSB on the PE, where the DSB ensures TLB invalidation completion.

Note: Consistent with the A-profile architecture[2], for an entry to be eligible for invalidation, addresses that are provided for non-ranged TLB invalidation are not required to be aligned to the start of a TLB entry address range. To match a TLB entry, the least significant bits of the address are ignored as needed, given the size of the entry.

## 4.4.1 Common TLB invalidation fields

## 4.4.1.1 Range-based invalidation and level hint

Armv8.4 [2] introduces range-based TLB invalidation operations and adds a level hint to both existing and range-based invalidation operations.

The SMMU\_IDR3.RIL bit indicates support for both range-based invalidation and the level hint. This feature is mandatory in SMMUv3.2 or later.

The following fields are common across all address-based invalidation operation commands, for VA and IPA, as described in sections 4.4.2 TLB invalidation of stage 1 and 4.4.3 TLB invalidation of stage 2 .

| Bits    | Name   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|---------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [25:20] | SCALE  | Range invalidation scale. • See below for use of this field in range invalidation. • When TG == 0b00 this field is RES0. • If SMMU_IDR3.RIL == 0, this field is RES0. • If SMMU_IDR5.DS == 0, this field is 5 bits wide, bits [24:20]. Bit 25 is RES0. • If SMMU_IDR5.DS == 1, this field is 6 bits wide, bits [25:20]. Values of this field that are greater than 39 are treated as 39, but software must not rely on this behavior. With the larger values of this field, it is possible that a CMD_TLBI_* with a base address that targets the TTB0 region can include a range that overflows into the TTB1 region, for translation regimes that have two VA ranges. In this scenario, the CMD_TLBI_* is not required to invalidate any entries in the TTB1 region.                                                                                                                                                                                                                                       |
| [16:12] | NUM    | Range invalidation granule multiplier • See below for use of this field in range invalidation. • When TG = 0b00 , this field is RES0. • If SMMU_IDR3.RIL == 0, this field is RES0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [75:74] | TG     | Translation Granule • This field indicates the Translation Granule size of the TLB entries that are intended to be invalidated and is used with both the range TLB invalidation and the TTL hint, as described in Armv8.4 (1) . It applies to TLB entries that cache information from Table descriptors or information from last level descriptors. • TG is encoded as follows: - 0b00 : Entries to be invalidated were inserted using any Translation Granule size, and: * Range invalidation is not performed. * The TTL hint is not used. - 0b01 : Entries to be invalidated were inserted using a 4KB Translation Granule. - 0b10 : Entries to be invalidated were inserted using a 16KB Translation Granule. - 0b11 : Entries to be invalidated were inserted using a 64KB Translation Granule. • If SMMU_IDR3.RIL == 0, this field is RES0. • If a non-zero value is specified then the SMMUis only required to invalidate TLB entries that were inserted using a Translation Granule that matches TG. |
| [73:72] | TTL    | Translation Table Level • When TG != 0b00 , this field provides a hint that indicates the level of the translation table walk holding the leaf entry for the address that is being invalidated, as described in Armv8.4 (1) . • When TG == 0b00 , this field is RES0. The TTL field does not affect the scope of the invalidation. • If a non-zero value is specified, then the SMMUis only required to invalidate TLB entries that were inserted from a translation table walk level matching TTL. • If SMMU_IDR3.RIL == 0, this field is RES0.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

| Bits   | Name   | Meaning                                                                                                                                                                                                                                             |
|--------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [71]   | TTL128 | Translation Table Level when using 128-bit descriptors • When TG != 0b00 and TTL != 0b00 , this field indicates that the TTL hint applies to a translation regime using 128-bit descriptors. • When TG == 0b00 or TTL == 0b00 , this field is RES0. |

(1) [2]

The encodings of TTL reduce the required scope of the invalidation as follows:

| TTL   | When TG == 0b00                                                              | When TG == 0b01                                   | When TG == 0b10                                                                                                                     | When TG == 0b11                                    |
|-------|------------------------------------------------------------------------------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| 0b00  | TTL is RES0, not used. Leaf entries at any level of walk of a table with any | Leaf entries at any level of a 4KB Granule table. | Leaf entries at any level of a 16KB Granule table.                                                                                  | Leaf entries at any level of a 64KB Granule table. |
| 0b01  |                                                                              | Leaf entries at Level 1 of a 4KB Granule table.   | If SMMU_IDR5.DS == 1 then leaf entries at level 1 of a 16KB Granule table. Otherwise Reserved, and hardware treats as TTL == 0b00 . | Leaf entries at Level 1 of a 64KB Granule table.   |
| 0b10  |                                                                              | Leaf entries at Level 2 of a 4KB Granule table.   | Leaf entries at Level 2 of a 16KB Granule table.                                                                                    | Leaf entries at Level 2 of a 64KB Granule table.   |
| 0b11  |                                                                              | Leaf entries at Level 3 of a 4KB Granule table.   | Leaf entries at Level 3 of a 16KB Granule table.                                                                                    | Leaf entries at Level 3 of a 64KB Granule table.   |

Note: Armv8.7 FEAT\_LPA2 [2] introduces a TTL encoding to target level 0 block descriptors for the 4KB translation granule size. The SMMU CMD\_TLBI\_* operations do not have an equivalent encoding.

When TG = 0b00 , the TTL and TTL128 hints are not used and range invalidation is not performed.

Note: The TTL hint gives the level of translation table walk of the page or block last level descriptor entries for the addresses being invalidated. For operations with Leaf=0, invalidation of cached Table descriptors for the address and scope additionally occurs at levels between the start of the walk and the level before the last level given by TTL.

When TG != 0b00 :

- The TTL field might indicate a level hint.
- A range invalidation is performed. The range, in bytes, of virtual or intermediate physical addresses are given by:
- -Range = ((NUM+1)*2 SCALE )*Translation\_Granule\_Size

- -The range begins at the address given by the Address field in the command, meaning that the set of invalidated addresses, A, is given by:
* Address &lt;= A &lt; Address + Range
- -Note: This differs from the range expressible using an Armv8.4 [2] PE 'TLBI R' instruction, because the SCALE field is larger in an SMMU command. The SMMU encoding can express a superset of all possible ranges expressible in a PE 'TLBI R' instruction.
- -Note: The span is a single granule when NUM == 0 and SCALE == 0. In this case, the command has similar behavior to a non-range SMMU invalidation operation, except it uses the TTL hint. If SMMU\_IDR5.DS == 0, a TLBI configured with TG == 0b10 and TTL == 0b01 , raises a CERROR\_ILL, since TTL is treated as 0b00 , whereas for an equivalent single address TLBI issued by a PE, the invalidation is performed and the encoding means that the leaf entry can be from any level.
- -Note: A CMD\_TLBI\_ can be issued with an Address in the TTB1 half of the Virtual Address space, with SCALE and NUM values such that the Range exceeds the top of the address space. The Address is not considered to 'wrap' on overflow and the SMMU is not required to invalidate any entries inserted for the TTB0 half of the Virtual Address space in this scenario.
- For 64-bit descriptors, the range of addresses that is invalidated is UNPREDICTABLE in the following conditions:
- -For the 4K translation granule (TG == 0b01 ):
- -For the 16K translation granule (TG == 0b10 ):
* If TTL == 0b10 and bits Address[24:12] are not all zero.
* If TTL == 0b11 or 0b00 and bits Address[13:12] are not all zero.
* If SMMU\_IDR5.DS == 1, TTL == 0b01 , and bits Address[35:12] are not all zero.
* Note: If SMMU\_IDR5.DS == 0 then TTL == 0b01 is Reserved when TG == 0b10 and this value should not be programmed. Hardware treats TTL == 0b01 as though TTL == 0b00 . This means that, to avoid an unpredictable range of invalidation, Address[13:12] are also required to be zero when TTL == 0b01 .
- -For the 64K translation granule (TG == 0b11 ):
* If TTL == 0b11 or 0b00 and bits Address[15:12] are not all zero.
- For 128-bit descriptors, the TLBI is not required to invalidate any TLB entries in the following conditions:
- -For the 4K translation granule (TG == 0b01 ):
* If TTL == 0b01 and bits Address[27:12] are not all zero. * If TTL == 0b10 and bits Address[19:12] are not all zero. -For the 16K translation granule (TG == 0b10 ): * If TTL == 0b01 and bits Address[33:12] are not all zero. * If TTL == 0b10 and bits Address[23:12] are not all zero. * If TTL == 0b11 and bits Address[13:12] are not all zero. -For the 64K translation granule (TG == 0b11 ): * If TTL == 0b01 and bits Address[39:12] are not all zero. * If TTL == 0b10 and bits Address[27:12] are not all zero. * If TTL == 0b11 and bits Address[15:12] are not all zero.
- -Note: Bits Address[11:0] are not supplied in the address argument.

```
* If TTL == 0b01 and bits Address[29:12] are not all zero. * If TTL == 0b10 and bits Address[20:12] are not all zero.
```

```
* If TTL == 0b01 and bits Address[41:12] are not all zero. * If TTL == 0b10 and bits Address[28:12] are not all zero.
```

- The parameter combination of NUM == 0, SCALE == 0 and TTL = 0b00 is Reserved. Use of this Reserved combination of parameters causes CERROR\_ILL.
- -Note: Providing granule information without using TTL or a range invalidate has no purpose and this command encoding is Reserved.
- If TTL != 0b00 :
- -If the TTL128 field is RES0 or zero, invalidation is performed to TLB entries using TG and 64-bit descriptor format, from the level of walk in TTL.
- -If the TTL128 field is 1 then invalidation is performed to TLB entries using TG and 128-bit descriptor format, from the level of walk in TTL.

An implementation of SMMUv3.2 or later in a system that supports broadcast invalidation, that is when SMMU\_IDR0.BTM == 1, also supports broadcast range invalidation operations.

Note: For example, for a TLBI issued with TTL= 0b10 and Leaf=0:

- The SMMU will invalidate cached entries for matching:
- -Level 2 block entries.
- -Level 0 and level 1 table entries.
- The SMMU is not required to invalidate:
- -Level 3 entries.
- -Level 2 table entries.
- -Level 1 block entries.

## 4.4.2 TLB invalidation of stage 1

The following commands are available on a stage 1-only and a stage 1 and stage 2 SMMU. On a stage 2-only SMMU, they result in CERROR\_ILL.

| Stage 1 command                                                     | Stage 1 not supported   | From Non-secure Command queue                                                                                                                                                      | From Secure Command queue, if present                                                                                                                                              |
|---------------------------------------------------------------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CMD_TLBI_NH_ALL CMD_TLBI_NH_ASID CMD_TLBI_NH_VAA CMD_TLBI_NH_VA     | CERROR_ILL              | Invalidate NS EL1 mappings                                                                                                                                                         | Invalidate Secure stage 1 mappings (inserted with StreamWorld == Secure). Note: EL3 entries are not required to be affected.                                                       |
| CMD_TLBI_EL3_ALL CMD_TLBI_EL3_VA                                    |                         | CERROR_ILL                                                                                                                                                                         | Invalidate EL3 stage 1 mappings (insered with StreamWorld ==                                                                                                                       |
| CMD_TLBI_EL2_ALL CMD_TLBI_EL2_VA CMD_TLBI_EL2_VAA CMD_TLBI_EL2_ASID |                         | If SMMU_IDR0.Hyp == 1, invalidate EL2 or El2-E2H stage 1 mappings as indicated by SMMU_CR2.E2H, in the corresponding Security state (see text). If SMMU_IDR0.Hyp == 0, CERROR_ILL. | If SMMU_IDR0.Hyp == 1, invalidate EL2 or El2-E2H stage 1 mappings as indicated by SMMU_CR2.E2H, in the corresponding Security state (see text). If SMMU_IDR0.Hyp == 0, CERROR_ILL. |

Note: Arm expects that software controlling a stage 1-only SMMU will use the first four commands. This includes driver software operating in a virtual machine controlling a stage 1-only SMMU interface.

In the following CMD\_TLBI\_NH\_* commands, VMID is only matched when stage 2 is supported for the Security state corresponding to the command queue that the command was issued in. Otherwise, the VMID parameter is

RES0 and, if it has a non-zero value, the SMMU is permitted to perform the invalidation on an UNKNOWN VMID value, or to not perform an invalidation.

Note: A stage 1-only implementation is not required to check that the VMID parameter of CMD\_TLBI\_NH\_* is zero.

The Address parameters of these commands are VAs. An implementation is permitted but not required to treat the parameter as out of range if bits at Address[V AS-1] and upwards are not all equal in value. TBI is permitted but not required to apply to the parameter.

## 4.4.2.1 CMD\_TLBI\_NH\_ALL(VMID)

<!-- image -->

When issued from the Non-secure Command queue, the invalidation scope is equivalent to that of VMALLE1, invalidates all stage 1 NS-EL1 (not NS-EL2 or NS-EL2-E2H) entries for VMID, including global entries.

When issued from the Secure Command queue and Secure stage 2 is not supported, the invalidation scope is equivalent to that of Secure ALLE1, invalidates all Secure entries, including global entries.

When issued from the Secure Command queue and Secure stage 2 is supported, the invalidation scope is equivalent to that of Secure VMALLE1, invalidates all Secure stage 1 EL1 (not S-EL2 or S-EL2-E2H) entries for VMID, including global entries.

For an equivalent to Non-secure ALLE1, see CMD\_TLBI\_NSNH\_ALL.

When issued from the Realm Command queue, the invalidation scope is equivalent to that of VMALLE1, invalidates all stage 1 Realm-EL1 (not Realm-EL2 or Realm-EL2-E2H) entries for VMID, including global entries.

## 4.4.2.2 CMD\_TLBI\_NH\_ASID(VMID, ASID)

<!-- image -->

|          | 127      | 127      | 127      | 96   | 127      |
|----------|----------|----------|----------|------|----------|
| RES0     | RES0     | RES0     | RES0     | RES0 | RES0     |
| 95       | 95       | 95       | 95       | 64   | 95       |
| RES0     | RES0     | RES0     | RES0     | RES0 | RES0     |
| 63 48 47 | 63 48 47 | 63 48 47 | 63 48 47 | 32   | 63 48 47 |
| ASID     | ASID     | VMID     | VMID     |      |          |
| 31       | 31       | 8 7      | 8 7      | 0    |          |
| RES0     | RES0     | RES0     | 0x11     | 0x11 |          |

The invalidation scope is equivalent to that of ASIDE1:

When issued from the Non-secure Command queue, invalidates stage 1 NS-EL1 non-global entries by ASID and VMID.

When issued from the Secure Command queue and Secure stage 2 is not supported, invalidates stage 1 Secure non-global entries by ASID.

When issued from the Secure Command queue and Secure stage 2 is supported, invalidates Secure stage 1 non-global entries by ASID and VMID.

When issued from the Realm Command queue, invalidates stage 1 Realm-EL1 non-global entries by ASID and VMID.

## 4.4.2.3 CMD\_TLBI\_NH\_VAA(VMID, Addr, Leaf)

<!-- image -->

The invalidation scope is equivalent to that of V AA{L}E1:

When issued from the Non-secure Command queue, invalidates stage 1 NS-EL1 entries by VA for all ASIDs in VMID, including global entries.

When issued from the Secure Command queue and Secure stage 2 is not supported, invalidates stage 1 Secure entries by V A for all ASIDs, including global entries.

When issued from the Secure Command queue and Secure stage 2 is supported, invalidates stage 1 Secure entries by VA for all ASIDs in VMID, including global entries.

When Leaf == 1, only cached entries for the last level of translation table walk are required to be invalidated.

When issued from the Realm Command queue, invalidates stage 1 Realm-EL1 entries by VA for all ASIDs in VMID, including global entries.

## 4.4.2.4 CMD\_TLBI\_NH\_VA(VMID, ASID, Addr, Leaf)

<!-- image -->

The invalidation scope is equivalent to that of V A{L}E1:

When issued from the Non-secure Command queue, invalidates stage 1 NS-EL1 entries by VMID, ASID and VA, as well as global entries by VMID and VA regardless of the ASID used during allocation.

When issued from the Secure Command queue and Secure stage 2 is not supported, invalidates stage 1 Secure entries by ASID and VA, as well as global entries by V A regardless of the ASID used during allocation.

When issued from the Secure Command queue and Secure stage 2 is supported, invalidates stage 1 Secure entries by VMID, ASID and VA, as well as global entries by VMID and VA regardless of the ASID used during allocation.

When Leaf == 1, only cached entries for the last level of translation table walk are required to be invalidated.

When issued from the Realm Command queue, invalidates stage 1 Realm-EL1 entries by VMID, ASID and VA, as well as global entries by VMID and VA regardless of the ASID used during allocation.

## 4.4.2.5 CMD\_TLBI\_EL3\_ALL

<!-- image -->

The invalidation scope is equivalent to that of ALLE3, invalidates all stage 1 EL3 entries.

This command is valid only on the Secure Command queue, otherwise a CERROR\_ILL is raised.

If SMMU\_IDR0.RME\_IMPL == 1, this command results in CERROR\_ILL, as EL3 StreamWorld is not supported. Issuing this command to the Realm Command queue results in CERROR\_ILL.

## 4.4.2.6 CMD\_TLBI\_EL3\_VA(Addr, Leaf)

<!-- image -->

The invalidation scope is equivalent to that of V A{L}E3, invalidates stage 1 EL3 by V A.

When Leaf == 1, only cached entries for the last level of translation table walk are required to be invalidated.

This command is valid only on the Secure Command queue, otherwise a CERROR\_ILL is raised.

If SMMU\_IDR0.RME\_IMPL == 1, this command results in CERROR\_ILL, as EL3 StreamWorld is not supported. Issuing this command to the Realm Command queue results in CERROR\_ILL.

## 4.4.2.7 CMD\_TLBI\_EL2\_ALL

<!-- image -->

All stage 1 NS-EL2/Hyp entries are invalidated, whether ASID-tagged (inserted in NS-EL2-E2H mode when SMMU\_CR2.E2H == 1) or not.

The invalidation scope is equivalent to that of ALLE2, and when HCR\_EL2.TGE == 1 &amp;&amp; HCR\_EL2.E2H == 1, VMALLE1.

When SMMU\_IDR0.Hyp == 0, this command causes a CERROR\_ILL.

This command has the same effect whether issued from the Secure or Non-secure command queues.

When issued on a Realm Command queue, all stage 1 Realm-EL2 entries are invalidated, whether ASID-tagged (inserted in Realm-EL2-E2H mode when SMMU\_R\_CR2.E2H == 1) or not.

## 4.4.2.8 CMD\_TLBI\_EL2\_VA(ASID, Addr, Leaf)

<!-- image -->

When issued on a Non-secure or Secure command queue, stage 1 NS-EL2/Hyp entries by VA are invalidated, including global.

When Leaf == 1, only cached entries for the last level of translation table walk are required to be invalidated.

This behavior of the command is governed by SMMU\_CR2.E2H:

- When SMMU\_CR2.E2H == 1, TLB entries inserted with a StreamWorld == NS-EL2-E2H configuration are invalidated if ASID matches (or global) and VA matches. TLB entries inserted with StreamWorld == NS-EL2 are not required to be invalidated.
- When SMMU\_CR2.E2H == 0, TLB entries inserted with a StreamWorld == NS-EL2 configuration are invalidated if V A matches, and the ASID parameter is ignored. TLB entries inserted with StreamWorld == NS-EL2-E2H are not required to be invalidated.

This command must not be submitted to a Command queue when the effective value of SMMU\_CR2.E2H is UNKNOWN. Otherwise, it is UNPREDICTABLE whether any NS-EL2 or NS-EL2-E2H entries that match Addr and ASID are invalidated. See section 6.3.12.3 E2H .

The invalidation scope is equivalent to that of V A{L}E2, and when HCR\_EL2.TGE == 1 &amp;&amp; HCR\_EL2.E2H == 1, VA{L}E1.

When SMMU\_IDR0.Hyp == 0, this command causes a CERROR\_ILL.

This command has the same effect whether issued from the Secure or Non-secure command queues.

When issued to a Realm command queue, this command applies to Realm EL2 or EL2-E2H TLB entries with the same qualification about E2H that are described for Non-secure state.

## 4.4.2.9 CMD\_TLBI\_EL2\_VAA(Addr, Leaf)

<!-- image -->

When issued on a Non-secure or Secure command queue, stage 1 NS-EL2/Hyp entries by VA for all ASIDs are invalidated, including global.

When Leaf == 1, only cached entries for the last level of translation table walk are required to be invalidated.

This behavior of this command is governed by SMMU\_CR2.E2H:

- When SMMU\_CR2.E2H == 1, TLB entries inserted with a StreamWorld == NS-EL2-E2H configuration are invalidated if the V A matches, for all ASIDs. TLB entries inserted with StreamWorld == NS-EL2 are not required to be invalidated.
- When SMMU\_CR2.E2H == 0, TLB entries inserted with a StreamWorld == NS-EL2 configuration are invalidated if the V A matches. TLB entries inserted with StreamWorld == NS-EL2-E2H are not required to be invalidated.

This command must not be submitted to a Command queue when the effective value of E2H is UNKNOWN. Otherwise, it is UNPREDICTABLE whether any NS-EL2 or NS-EL2-E2H entries that match Addr and ASID are invalidated. See section 6.3.12.3 E2H .

Note: An implementation might choose to optimize search of a TLB given this information, and access a single location for the given V A.

The invalidation scope is equivalent to that of V AA{L}E1 when HCR\_EL2.TGE == 1 &amp;&amp; HCR\_EL2.E2H == 1. When a PE is not in EL2-E2H mode, it does not have an equivalent.

When SMMU\_IDR0.Hyp == 0, this command causes CERROR\_ILL.

This command has the same effect whether issued from the Secure or Non-secure command queues.

When issued to a Realm command queue, this command always applies to Realm EL2 or EL2-E2H TLB entries with the same qualifications about E2H that are described for Non-secure state above.

## 4.4.2.10 CMD\_TLBI\_EL2\_ASID(ASID)

<!-- image -->

Invalidates stage 1 NS-EL2/Hyp non-global entries by ASID.

Non-global TLB entries inserted with a StreamWorld == NS-EL2-E2H configuration are invalidated if ASID matches. EL2 (non-ASID-tagged) entries are not required to be invalidated.

The invalidation scope is equivalent to that of ASIDE1 when HCR\_EL2.TGE == 1 &amp;&amp; HCR\_EL2.E2H == 1. When a PE is not in NS-EL2-E2H mode, it does not have an equivalent.

When SMMU\_IDR0.Hyp == 0, this command causes a CERROR\_ILL.

This command has the same effect whether issued from the Secure or Non-secure command queues.

When issued to a Realm command queue, this command always applies to Realm-EL2-E2H TLB entries.

## 4.4.2.11 CMD\_TLBI\_S\_EL2\_ALL

<!-- image -->

This command is equivalent to, and is encoded similarly to CMD\_TLBI\_EL2\_ALL but acts on S-EL2 instead of NS-EL2. This command relates to SMMU\_S\_CR2.E2H in a similar way as CMD\_TLBI\_EL2\_ALL relates to SMMU\_CR2.E2H.

This command causes CERROR\_ILL when used on the Non-secure Command queue. The opcode for this command is Reserved and causes CERROR\_ILL when Secure EL2 is not supported. See section 3.10.2.2 Secure EL2 and support for Secure stage 2 translation .

Issuing this command to the Realm Command queue results in CERROR\_ILL.

## 4.4.2.12 CMD\_TLBI\_S\_EL2\_VA

<!-- image -->

This command is equivalent to, and is encoded similarly to CMD\_TLBI\_EL2\_VA but acts on S-EL2 instead of NS-EL2. This command relates to SMMU\_S\_CR2.E2H in a similar way as CMD\_TLBI\_EL2\_VA relates to SMMU\_CR2.E2H.

This command causes CERROR\_ILL when used on the Non-secure Command queue. The opcode for this command is Reserved and causes CERROR\_ILL when Secure EL2 is not supported.

Issuing this command to the Realm Command queue results in CERROR\_ILL.

## 4.4.2.13 CMD\_TLBI\_S\_EL2\_VAA

<!-- image -->

This command is equivalent to, and is encoded similarly to CMD\_TLBI\_EL2\_VAA but acts on S-EL2 instead of NS-EL2. This command relates to SMMU\_S\_CR2.E2H in a similar way as CMD\_TLBI\_EL2\_VAA relates to SMMU\_CR2.E2H.

This command causes CERROR\_ILL when used on the Non-secure Command queue. The opcode for this command is Reserved and causes CERROR\_ILL when Secure EL2 is not supported.

Issuing this command to the Realm Command queue results in CERROR\_ILL.

## 4.4.2.14 CMD\_TLBI\_S\_EL2\_ASID

<!-- image -->

This command is equivalent to, and is encoded similarly to CMD\_TLBI\_EL2\_ASID but acts on S-EL2 instead of NS-EL2. This command relates to SMMU\_S\_CR2.E2H in a similar way as CMD\_TLBI\_EL2\_ASID relates to SMMU\_CR2.E2H.

This command causes CERROR\_ILL when used on the Non-secure Command queue. The opcode for this command is Reserved and causes CERROR\_ILL when Secure EL2 is not supported.

Issuing this command to the Realm Command queue results in CERROR\_ILL.

## 4.4.3 TLB invalidation of stage 2

These commands allow a hypervisor to perform stage 2 invalidations on behalf of a VM.

## 4.4.3.1 CMD\_TLBI\_S2\_IPA(VMID, Addr, Leaf)

<!-- image -->

The invalidation scope is equivalent to that of IPAS2{L}E1, invalidates stage 2 by VMID and IPA.

When Leaf == 1, only cached entries for the last level of translation table walk are required to be invalidated.

When issued on an SMMU without stage 2 support, a CERROR\_ILL is raised.

If issued on a Non-secure or Secure Command queue, the Address parameter is a Non-secure IPA in the Non-secure translation regime. An implementation is permitted but not required to treat the parameter as out of range if bits at Address[IAS] and upwards are not all zero. Address bits [11:0] are treated as 0s.

Consistent with Armv8-A [2], this command is not required to invalidate structures containing combined stage 1 and stage 2 information (from nested stage 1 and 2 translation configuration). Where combined Stage 1 and stage 2 mappings are possible, this command is expected to be used with CMD\_TLBI\_NH\_ALL or CMD\_TLBI\_NH\_VAA. However, this command is sufficient to invalidate translations resulting from stage 2-only configuration.

Note: An implementation choosing to combine all stages of translation into one TLB must distinguish whether an entry represents a VA or an IPA (inserted from stage 1, stage 1 and 2 configuration or stage 2-only) so that

invalidation by IPA is able to locate entries inserted from stage 2-only configurations.

This command has the same effect whether issued from the Secure or Non-secure command queues.

When issued to a Realm command queue, this command always applies to Realm stage 2 TLB entries.

## 4.4.3.2 CMD\_TLBI\_S12\_VMALL(VMID)

<!-- image -->

The invalidation scope is equivalent to that of VMALLS12E1, invalidates all Non-secure (and non-Hyp) entries at all implemented stages for VMID. When issued on an SMMU without stage 2 support, a CERROR\_ILL is raised.

This command has the same effect whether issued from the Secure or Non-secure command queues.

When issued to a Realm command queue, this command always applies to Realm EL1 TLB entries.

## 4.4.3.3 CMD\_TLBI\_S\_S2\_IPA(VMID, Addr, Leaf, NS)

<!-- image -->

Invalidates Secure stage 2-only by IPA. This command is similar to the Non-secure CMD\_TLBI\_S2\_IPA command, except acts on TLB entries in the Secure translation regime and has an additional parameter, NS, defined as follows:

- 0: The Addr parameter is in the Secure IPA address space in the Secure translation regime.
- 1: The Addr parameter is in the Non-secure IPA address space in the Secure translation regime.

This command causes CERROR\_ILL when used on the Non-secure Command queue. The opcode for this command is Reserved and causes CERROR\_ILL when Secure stage 2 is not supported.

Issuing this command to the Realm Command queue results in CERROR\_ILL.

## 4.4.3.4 CMD\_TLBI\_S\_S12\_VMALL(VMID)

<!-- image -->

Invalidates all stages for all TLB entries in the Secure translation regime, by VMID. This command is the Secure equivalent of the CMD\_TLBI\_S12\_VMALL command and is equivalent to Secure VMALLS12E1 scope on the PE. This command invalidates all TLB entries in the Secure translation regime matching VMID.

This command causes CERROR\_ILL when used on the Non-secure Command queue. This command opcode is RESERVED and causes CERROR\_ILL when Secure stage 2 is not supported.

Issuing this command to the Realm Command queue results in CERROR\_ILL.

## 4.4.4 Common TLB invalidation

## 4.4.4.1 CMD\_TLBI\_NSNH\_ALL

<!-- image -->

| 127   |      | 96   |      |
|-------|------|------|------|
| RES0  | RES0 | RES0 | RES0 |
| 95    |      | 64   |      |
|       | RES0 |      |      |
| 63    |      | 32   |      |
|       | RES0 |      |      |
| 31    |      | 0    |      |
|       | RES0 |      |      |

When issued on a Non-secure or Secure Command queue, the invalidation scope is equivalent to that of Non-secure ALLE1, valid from both the Non-secure and Secure Command queue. All Non-secure, non-NS-EL2, non-NS-EL2-E2H TLB entries are invalidated at all implemented stages.

Note: A stage 1-only Non-secure SMMU with SMMU\_IDR0.Hyp == 0 can also be initialized with CMD\_TLBI\_NH\_ALL.

This command is valid whether the SMMU supports only stage 1, only stage 2, or both stages.

When issued from a Realm Command queue, this command behaves according to Realm ALLE1.

Note: When issuing to the Realm programming interface, even though this command has NS in its name, it only applies to Realm entries.

## 4.4.4.2 CMD\_TLBI\_SNH\_ALL

<!-- image -->

All stages for all TLB entries in the Secure translation regime are invalidated. This command is the Secure equivalent of the CMD\_TLBI\_NSNH\_ALL command and is equivalent to Secure ALLE1 scope on the PE. This command invalidates all Secure, non-S-EL2, non-S-EL2-E2H TLB entries at all implemented stages.

This command causes CERROR\_ILL when used on the Non-secure Command queue. This command opcode is RESERVED and causes CERROR\_ILL when Secure stage 2 is not supported.

Issuing this command to the Realm Command queue results in CERROR\_ILL.