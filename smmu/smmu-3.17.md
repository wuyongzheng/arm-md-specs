## 3.17 TLB tagging, VMIDs, ASIDs and participation in broadcast TLB maintenance

Cached translations within the SMMU are tagged with:

- A translation regime, given by the STE's StreamWorld and derived in part from STE.STRW. This applies to all cached translations.
- An ASID, if the translation regime supports ASIDs.
- A VMID, if stage 2 is implemented by the SMMU and if the translation regime supports VMIDs.

This is summarized in the table below:

| StreamWorld     | Address Type   | Tags                | Tags    | Tags    |
|-----------------|----------------|---------------------|---------|---------|
|                 |                | ASID                | ASET    | VMID    |
| NS-EL1          | VA             | Yes, if TTD.nG == 1 | Yes (2) | Yes (1) |
| NS-EL1          | IPA (1)        | No                  | No (3)  | Yes (1) |
| Realm-EL1       | VA             | Yes, if TTD.nG == 1 | Yes (2) | Yes (1) |
| Realm-EL1       | IPA (1)        | No                  | No (3)  | Yes (1) |
| any-EL2 (4)     | VA             | No                  | No (3)  | No      |
| any-EL2-E2H (4) | VA             | Yes, if TTD.nG == 1 | Yes (2) | No      |
| Secure          | VA             | Yes, if TTD.nG == 1 | Yes (2) | Yes (5) |
| EL3             | VA             | No                  | No (3)  | No      |

This is consistent with TLB tagging in PEs.

Note: In this specification, the term cached translations refers to the contents of a PE-style ASID/VMID/Address TLB. Any cached configuration structures are considered architecturally separate from the translations that are located from the configuration. Configuration caches are not required to be tagged as described in this section.

Use of these tags ensures that no aliasing occurs between different translations for the same address within different ASIDs, or between the same ASID under different VMIDs, or between the same ASID within different translation regimes, or between different translation regimes without ASIDs (for example any-EL2 and EL3). For both lookup and invalidation purposes, ASID values can be considered to be separate namespaces within each VMID and translation regime.

Note: For example, TLB entries tagged as ASID 3 in a Secure stage 1 cannot be matched by lookups for ASID 3 in an NS-EL1 stage 1 configuration. Similarly, a TLB entry that is tagged as either of S-EL2 or NS-EL2 can never be matched by a lookup from an EL3 context, even if the address matches.

In a regime that lacks ASIDs to differentiate address spaces, all CDs are considered equivalent (similar to two CDs with the same ASID value) even if referenced using different STEs. This implies that SubstreamIDs cannot differentiate address spaces in any-EL2/EL3 StreamWorlds. See section 5.4.1 CD notes for restrictions on permitted differences between CDs in such StreamWorlds.

EL3 tags TLB entries as EL3 without an ASID and Arm expects this StreamWorld to be selected for Secure streams used by EL3 software on an Armv8-A host PE whose EL3 runs in AArch64 state. There are no ASIDs in an AArch64 EL3 translation regime.

When SMMU\_IDR0.S1P == 1, the SMMU supports 16-bit ASIDs if SMMU\_IDR0.ASID16 == 1.

When SMMU\_IDR0.S2P == 1, the SMMU supports 16-bit VMIDs if SMMU\_IDR0.VMID16 == 1.

Consistent with PEs, all TLB entries inserted using NS-EL1 configurations are tagged with VMIDs when stage 2 is implemented, regardless of whether configuration is stage 1-only, stage 2-only or stage 1+stage 2 translation. When stage 2 is configured, with or without stage 1, or if stage 1-only translation is configured, the VMID is taken from the STE.S2VMID field. When stage 2 is not implemented, no VMID tag is required on TLB entries.

Note: Some implementations and interconnects might support the transmission of VMID value onwards into the system, so that Completer devices might further arbitrate access on a per-transaction basis. Where SMMU bypass is enabled (SMMU\_(S\_)CR0.SMMUEN == 0) so that STE structures are unused, the SMMU\_(S\_)GBPA.IMPDEF field might be used. Otherwise, the STE.S2VMID field might be used. Details of these use cases are outside of the scope of this specification.

SMMUsupport for TLB maintenance messages that are broadcast from the PE is optional, but Arm recommends that support is implemented. These messages convey TLB invalidations from certain TLBI instructions on PEs. The Armv8.0 architecture [2] requires invalidation broadcasts to affect other PEs or agents in the same Inner Shareable domain. Armv8.4 [2] adds support for a PE to issue broadcast TLB invalidation operations to the Outer Shareable domain as well as the existing behavior of issuing to the existing Inner Shareable domain. Broadcast TLB invalidate messages convey one or more of an address, an ASID or a VMID as required for a given invalidation operation, the scope defined by a translation stage to be affected and the translation regime in which the TLB entries are tagged. Support for broadcast invalidation is indicated by SMMU\_IDR0.BTM.

Note: The Shareability domain of the SMMU is a property of the system. When broadcast TLB invalidation is implemented then an implementation of any SMMUv3 version responds to the broadcast invalidation scope corresponding to its assigned Shareability domain.

If SMMU\_IDR0.BTM == 1 and SMMU\_(*\_)CR2.PTM == 1, the SMMU is permitted but not required to ignore broadcast TLB invalidation operations for the corresponding Security state. Arm strongly recommends that SMMU implementations ignore broadcast TLB invalidation operations if SMMU\_(*\_)CR2.PTM is 1, for performance and reliability considerations. Broadcast TLB invalidation messages that would invoke an illegal operation, such as an invalidation that applies to a stage or Security state that is not implemented in the SMMU, are silently ignored, with the exception that messages that have a combined effect must affect the implemented stages and ignore any unimplemented stage. When SMMU\_IDR0.S2P == 0, the SMMU matches VMID 0 for incoming broadcast TLB invalidation messages for a regime that uses VMIDs. When SMMU\_IDR0.S2P == 1, a broadcast TLB invalidation message for a regime that uses VMIDs is treated as having VMID 0 if it is sent from a PE that does not implement EL2.

Note: On PEs that implement EL2 but have stage 2 disabled, Arm expects software to configure VTTBR\_EL2.VMID to 0. This ensures that for broadcast TLBI operations that include a VMID the VMID is set to 0.

Note: If, in a translation regime that uses VMIDs, stage 1-only translations coexist with stage 1 and stage 2 translations, then different VMID values must be used in each configuration to avoid the stage 1-only translations matching lookups that use stage 1 and stage 2 configurations.

Note: Arm expects broadcast invalidation from PEs to be used where address spaces are shared with the SMMU and common translations are maintained, such as Shared Virtual Memory applications, or stage 2 translations that share a common stage 2 translation table between VMs and the SMMU. When an address space is not shared with PE processes, broadcast TLB invalidations from the PEs to the SMMU have no useful effects and might over-invalidate unrelated TLB entries. Non-shared address spaces arise when a custom address space is set up for a particular device - for example, scatter-gather or DMA isolation use cases. Arm expects that both shared and non-shared stage 1 translations might be in use simultaneously.

Stage 1 CDs contain an ASET flag, that represents the shared or non-shared nature of the ASID and address space. The set of ASIDs for non-shared address spaces might opt out of broadcast invalidation.

Note: Arm expects that SMMU stage 2 address spaces are generally shared with their respective PE virtual machine stage 2 configuration. If broadcast invalidation is required to be avoided for a particular SMMU stage 2 address space, Arm recommends that a hypervisor configures the STE with a VMID that is not allocated for virtual machine use on the PEs.

For a stage 1 configuration with a StreamWorld that has ASIDs, when CD.ASET == 1, the address space and ASID are non-shared. TLB entries that belong to that StreamWorld are not required to be invalidated by the broadcast invalidation operations that match with an ASID. These operations are VA{L}ExIS and ASIDExIS in the appropriate translation regime. All other matching broadcast invalidations are required to affect these entries. Where CD.ASET == 0, the ASID is considered shared with PE processes. TLB entries that belong to that StreamWorld are required to be affected by all matching broadcast invalidates. The definition of matching is identical to that of Armv8-A PE TLBs [2]. CD.ASET does not affect the invalidation of stage 2 translation information.

For translation lookup of non-global TLB entries and command-based invalidation purposes, ASID values with CD.ASET == 0 are considered equivalent to ASID values with CD.ASET == 1. CMD\_TLBI\_* commands invalidate all matching TLB entries regardless of their ASET value. CD.ASET affects translation lookup of global TLB entries. For information about global TLB entry matching, see section 3.17.1 The Global flag in the translation table descriptor .

A stage 1 configuration in a translation regime that does not have ASIDs, that is where StreamWorld == any-EL2 or StreamWorld == EL3, ignores the ASID field and is permitted but not required to tag TLB entries using ASETs. An equivalent semantic applies, in that ASET == 0 entries are affected by broadcast invalidation and ASET == 1 entries are not required to be invalidated by certain operations. EL2 TLB entries with ASET == 1 are not required to be invalidated by VA{L}ExIS or VAA{L}ExIS but must be invalidated by ALLE2IS. EL3 TLB entries with ASET == 1 are not required to be invalidated by VA{L}E3IS but must be invalidated by ALLE3IS.

Note: Arm does not anticipate that ASET == 1 has an effect on EL2 and EL3 contexts, however the behavior described here is consistent with other StreamWorld configurations.

In a regime that lacks ASIDs to differentiate address spaces, all CDs are considered equivalent (similar to two CDs with the same ASID value) even if referenced using different STEs. This implies that SubstreamIDs cannot differentiate address spaces in any-EL2/EL3 StreamWorlds. See section 5.4.1 CD notes for restrictions on permitted differences between CDs in such StreamWorlds.

Note: A broadcast invalidation operation that originates from a PE in any-EL2-E2H mode is not required to invalidate SMMU TLB entries that were inserted with StreamWorld == any-EL2, see section 3.17.5 EL2 ASIDs and TLB maintenance in EL2 Host (E2H) mode .

Note: See section 16.7.7 AMBADVMmessages with respect to CD.ASET == 1 TLB entries for AMBA interconnect DVMbehavior with respect to ASET == 1.

Note: The ASID namespace might be affected by ASID rollover on the PE. These situations might be handled by:

- Refreshing the ASID namespace on the PE side and reallocating free ASIDs to new processes, but leaving ASIDs that are shared with SMMU contexts untouched.
- Swapping the ASID that is used in a CD, so that the old ASID is removed from the SMMU, and future traffic uses a freshly-allocated ASID. This can be achieved with an overlap in which both the old ASID and new ASID are active as the old ASID is updated in the CDs. This is followed by invalidation commands to the

affected CDs (causing the SMMU to use the new ASID), and a CMD\_SYNC. These steps are followed by TLB invalidation commands and a CMD\_SYNC to remove all usage of the old ASID. When the final CMD\_SYNC has ensured that these commands are complete, the old ASID can be considered free and the system can re-use it for a different address space.

## 3.17.1 The Global flag in the translation table descriptor

For translation regimes that have an ASID, Armv8-A [2], defines an nG bit in the the Block and Page descriptors that allows them to be marked as either global or non-global. A translation that is performed for a Secure stream is treated as non-global, regardless of the value of the nG bit in the descriptor, if the descriptor is fetched from Non-secure memory. The any-EL2 and EL3 StreamWorlds do not support ASIDs, and the nG bit in the descriptor has no effect on these regimes.

Note: A translation table descriptor fetch from Non-secure memory might happen for several different reasons, for example because of the effective NS bit at that level of the translation table walk, or because the fetch uses the Non-secure IPA space which is implicitly Non-secure. See section 3.10.2.2 Secure EL2 and support for Secure stage 2 translation .

When entries are global, an ASID is not required to be recorded in any resulting TLB entry. During lookup, a TLB entry marked as global can match regardless of the ASID that is provided with the lookup. The nG bit in the descriptor does not allow a TLB entry to match a lookup from a StreamWorld that is not the same as the one from which the TLB entry was created.

Note: Global translations are used across address spaces with identical layout conventions, OS kernel addresses might be common across all process address spaces, and so they might be marked global. However, an SMMU might be used with many custom address spaces that are laid out in a manner convenient to the client device they serve, without common mappings.

The SMMU only matches global TLB entries, that is where the nG bit in the descriptor is zero, against lookups from the same StreamWorld and ASID set (ASET). Global TLB entries with ASET == 0 do not match lookups through configurations with ASET == 1. Global TLB entries with ASET == 1 do not match lookups through configurations with ASET == 0.

Invalidation rules for non-locked global mappings are identical to those in Armv8-A, where the ASIDE1 and ASIDE2 scopes are not required to invalidate global mappings.

## 3.17.2 Broadcast TLB maintenance from Armv8-A PEs with EL3 in AArch64

When the Secure Stream table is controlled by an Armv8-A PE where EL3 is using AArch64 state, software has the option of marking an STE as Secure, S-EL2, S-EL2-E2H or EL3 using the StreamWorld field, STE.STRW.

When the StreamWorld is Secure, the stream is configured on behalf of Secure-EL1 software and the resultant TLB entries are tagged as Secure, including an ASID if non-global. Such entries must be invalidated by:

- PE broadcast TLB invalidations (where supported and if CD.ASET allows) from Secure EL1 instructions with the following scope:
- -VA{L}E1
- -VAA{L}E1
- -ASIDE1, for non-global entries
- -ALLE1
- SMMUinvalidation commands on the Secure Command queue. These commands are:
- -CMD\_TLBI\_NH\_ALL
- -CMD\_TLBI\_NH\_ASID, for non-global entries
- -CMD\_TLBI\_NH\_VAA
- -CMD\_TLBI\_NH\_VA

When StreamWorld is EL3, the stream is configured on behalf of EL3 software and resultant TLB entries are tagged as EL3, without ASID, which differentiates them from the Secure case above. Such entries are invalidated

by:

- PE broadcast TLB invalidations (where supported and if CD.ASET allows) from EL3 instructions with scope of VA{L}E3, ALLE3.
- SMMUinvalidation commands on the Secure Command queue:
- -CMD\_TLBI\_EL3\_VA
- -CMD\_TLBI\_EL3\_ALL

An SMMU with SMMU\_IDR0.RME\_IMPL == 1 is not required to perform any invalidation on receipt of a broadcast TLBI for EL3 as EL3 StreamWorld is not supported.

## 3.17.2.1 Broadcast TLB maintenance when Secure EL2 is implemented

The Secure EL2 and Secure stage 2 facilities introduced in SMMUv3.2 interoperate with the corresponding facilities on a PE. Broadcast TLB maintenance from a PE affects SMMU TLB entries of the same scope where supported and if CD.ASET allows.

For broadcast TLB maintenance with Secure EL1 scope from a PE that does not implement Secure EL2, or a PE that implements Secure EL2 and has SCR\_EL3.EEL2 == 0, the following rules apply:

- When SMMU\_S\_IDR1.SEL2 == 0, invalidation scope is not determined by VMID and invalidation occurs as described in 3.17.2 Broadcast TLB maintenance from Armv8-A PEs with EL3 in AArch64 and in [2].
- When SMMU\_S\_IDR1.SEL2 == 1, the invalidation operations are interpreted as though they have VMID 0.
- -Note: When Secure EL2 is implemented, StreamWorld=Secure TLB entries that are inserted from configuration with stage 2 disabled are tagged with VMID 0. See section 3.10.2.2 Secure EL2 and support for Secure stage 2 translation .

Note: When a PE executes a VMALLS12 that targets Secure state, and Secure EL2 is either disabled or not implemented, it is only guaranteed to emit a broadcast TLBI with scope of stage 1 and VMID == 0.

For broadcast TLB maintenance with Secure EL1 scope from a PE that has SCR\_EL3.EEL2 == 1, the following rules apply:

- When SMMU\_S\_IDR1.SEL2 == 0, SMMU TLB entries are not required to be affected.
- When SMMU\_S\_IDR1.SEL2 == 1, TLB entries that are in scope of both the invalidation operation and the supplied VMID are invalidated.

Note: Arm recommends that care is taken when integrating an SMMU implementation of SMMUv3.1 or earlier into a system that supports broadcast TLB maintenance from PEs implementing Secure EL2. Arm recommends that broadcast TLB maintenance from a PE that has SCR\_EL3.EEL2 == 1 does not affect Secure SMMU TLB entries, and that steps are taken to ensure that malfunction is avoided if the SMMU receives new Secure broadcast TLB maintenance operations that contain a VMID.

## 3.17.3 Broadcast TLB maintenance from ARMv7-A PEs or Armv8-A PEs with EL3 using AArch32

When the Secure Stream table is controlled by an ARMv7-A PE or an Armv8-A PE where EL3 is using AArch32 state, Arm expects software to mark the StreamWorld of an STE as Secure. The resultant TLB entries are tagged as Secure, including an ASID if non-global. Such entries are invalidated by:

- PE broadcast TLB invalidations (where supported and if CD.ASET allows) from Secure instructions with the following scope:
- -MVA{L}
- -MVAA{L}
- -ASID, for non-global entries
- -ALL
- -Note: VA{L}E3 and ALLE3 are AArch64-only and unavailable in this scenario.

- SMMUinvalidation commands on the Secure Command queue. These commands are:
- -CMD\_TLBI\_NH\_ALL
- -CMD\_TLBI\_NH\_ASID, for non-global entries
- -CMD\_TLBI\_NH\_VAA
- -CMD\_TLBI\_NH\_VA

Note: Broadcast invalidations from ARMv7-A PEs or Armv8 PEs where EL3 is using AArch32 might fail to invalidate SMMU TLB entries that are tagged with StreamWorld == EL3.

## 3.17.4 Broadcast TLB maintenance in mixed AArch32 and AArch64 systems and with mixed ASID or VMID sizes

Broadcast TLB maintenance instructions that are executed from Armv7-A and Armv8-A PEs using AArch32 and AArch64 Exception levels affect SMMU TLB entries (if broadcast TLB invalidation is supported and participation enabled), when the addresses, ASIDs, VMIDs and StreamWorlds match as appropriate.

The exceptions are:

- If a PE where EL3 uses AArch32 state issues an AArch32 TLBI that affects Secure entries, the TLBI is not required to affect SMMU TLB entries that were created with StreamWorld == EL3.
- If a PE where EL3 uses AArch64 state issues an AArch64 or AArch32 TLBI that affects Secure EL1 entries, the TLBI is not required to affect SMMU TLB entries created with StreamWorld == EL3.
- If a PE where EL3 uses AArch64 state issues an AArch64 TLBI that affects EL3 entries, the TLBI is not required to affect SMMU TLB entries created with StreamWorld == Secure.

ARMv7-A PEs have 8-bit ASIDs and VMIDs. Armv8-A PEs might have 16-bit ASIDs or VMIDs or both. An SMMU implementation supports 8-bit or 16-bit ASIDs and VMIDs, as indicated by SMMU\_IDR0.{ASID16,VMID16}.

A difference in ASID or VMID size between the originator of the broadcast TLB maintenance instruction and the SMMUis resolved as follows. For each of ASID and VMID:

- An SMMU that supports a 16-bit ASID or VMID compares the incoming 16-bit broadcast value to its TLB tags directly and matches if the values are equal.
- -The incoming 16-bit value is constructed by the system from an originator with an 8-bit ASID or VMID by zero-extending the value to 16 bits.
- An SMMU that supports an 8-bit ASID or VMID compares the bottom 8 bits of the incoming broadcast values to its TLB tags:
- -The comparison is required to match if the bottom 8 bits are equal and the top 8 bits are zero.
- -The comparison is not required to, but might, match if the bottom 8 bits are equal but the top 8 bits are non-zero.

When the SMMU supports 16-bit ASIDs, that is when SMMU\_IDR0.ASID16 == 1, it does so for all StreamWorlds that use ASIDs (NS-EL1, Secure, any-EL2-E2H). The SMMU does not differentiate ASID size by AArch32 state contexts, as does an Armv8-A PE and, if supported by an implementation, 16-bit ASIDs can be used in CDs where CD.AA64 == 0. Arm expects that legacy software will continue to write zero-extended 8-bit values in the ASID field in this case. The same behavior applies for 16-bit VMIDs, when SMMU\_IDR0.VMID16 == 1, the behavior of which is not modified by STE.S2AA64 == 0.

## 3.17.5 EL2 ASIDs and TLB maintenance in EL2 Host (E2H) mode

The Non-secure programming interface supports StreamWorlds NS-EL2 and NS-EL2-E2H that correspond to PE Exception level EL2 in Non-secure state with and without E2H mode. When Secure EL2 is supported, the Secure programming interface supports StreamWorld S-EL2 and S-EL2-E2H that correspond to PE Exception level EL2 in Secure state with and without E2H mode.

The EL2 translation regime consists of:

- A stage 1 translation with one translation table without user permission checking.
- TLB entries that are not tagged with an ASID.

In E2H mode, the EL2 translation regime remains stage 1-only, but consists of two stage 1 translation tables that function the same way as those for an EL1 stage 1 translation. The resulting TLB entries are tagged as EL2, and might include an ASID. Non-secure EL2-E2H mode can be configured for Non-secure STEs using STE.STRW when SMMU\_IDR0.Hyp == 1 and SMMU\_CR2.E2H == 1. Secure EL2-E2H mode can be configured for Secure STEs using STE.STRW when SMMU\_S\_IDR1.SEL2 == 1 and SMMU\_S\_CR2.E2H == 1.

Note: In the Armv8.1-A architecture [2], EL2-E2H mode is referred to as the Virtualization Host Extensions.

Broadcast TLB maintenance from a PE affects SMMU TLB entries when the whole system uses EL2 or EL2-E2H mode. Broadcast messages from a PE running in EL2-E2H supply an EL2 scope, and also supply an ASID to match. In addition, EL2-E2H mode extends the set of EL2 broadcast invalidations to the following operations:

- Invalidate all, for EL2-tagged entries.
- Invalidate by VA and ASID, for EL2.
- Invalidate by VA in all ASIDs, for EL2.
- Invalidate all by ASID, for EL2.

If a PE running at EL2 uses E2H mode, but an SMMU contains TLB entries that were inserted with StreamWorld == any-EL2 configuration, the EL2-E2H broadcast invalidations from the PE are not required to invalidate these TLB entries.

If a PE running at EL2 does not use E2H mode, but an SMMU contains TLB entries that were inserted with StreamWorld == any-EL2-E2H configurations, EL2 broadcast invalidations from the PE are not required to invalidate these TLB entries.

Note: For each Security state, if broadcast invalidation is required for translations controlled by EL2 software, Arm recommends that StreamWorld == any-EL2 is used when the corresponding Security state in host PEs does not use E2H mode, and that StreamWorld == any-EL2-E2H is used when the corresponding Security state in host PEs use the E2H mode.

An implementation is not required to differentiate TLB entries with StreamWorld == any-EL2 from those with StreamWorld == any-EL2-E2H. Arm expects that, for a given Security state, the SMMU is programmed in a way that ensures that TLB entries of both of these StreamWorlds never coexist in translation caches. Therefore:

- A change to SMMU\_CR2.E2H must be accompanied by an invalidation of all TLB entries that could have been created from a Non-secure STE with StreamWorld == NS-EL2 or StreamWorld == NS-EL2-E2H. See 6.3.12.3 E2H for details.
- A change to SMMU\_S\_CR2.E2H must be accompanied by an invalidation of all TLB entries that could have been created from a Secure STE with StreamWorld == S-EL2 or StreamWorld == S-EL2-E2H.
- The behavior of TLB invalidation commands CMD\_TLBI\_EL2\_VAA and CMD\_TLBI\_EL2\_VA might change depending on SMMU\_CR2.E2H, see the individual commands for details.
- The behavior of TLB invalidation commands CMD\_TLBI\_S\_EL2\_VAA and CMD\_TLBI\_S\_EL2\_VA might change depending on SMMU\_S\_CR2.E2H, see the individual commands for details.

Note: A TLB lookup through a configuration with StreamWorld == any-EL2-E2H matches the ASID of the configuration with the ASID tag of the EL2 TLB entry, unless the entry is marked Global. A TLB insertion through the same configuration inserts a TLB entry tagged with the ASID of the configuration unless the translation is Global. When StreamWorld == any-EL2 a TLB lookup does not match the ASID tag of EL2 TLB entries, nor does a TLB insertion tag the entry with a known ASID value. A change to SMMU\_CR2.E2H or SMMU\_S\_CR2.E2H can cause unexpected TLB entries to match.

Note: SMMU\_CR2.E2H and SMMU\_S\_CR2.E2H may also be cached in a Configuration Cache.

## 3.17.6 VMID Wildcards

Some virtualization use cases involve the presentation of different views of page permissions in the same address space to different device streams. The mechanism by which one address space is split into more than one view is

outside the scope of this specification.

Note: STEs in the same Security state and with different translation table pointers must have different VMIDs. TTBs in the same VMID are considered equivalent within a Security state.

In the SMMU, SMMU\_CR0.VMW controls a VMID wildcard function that enables groups of Non-secure VMIDs to be associated with each other for the purposes of invalidation. An invalidation operation that matches on Non-secure VMID matches one exact VMID or ignores a configured number of VMID LSBs, as configured by SMMU\_CR0.VMW.

Note: For example, SMMU\_CR0.VMW might configure 1 LSB of VMID to be ignored so an incoming broadcast invalidate for VMID 0x0020 matches TLB entries tagged with VMID 0x0020 or 0x0021 . This configuration allows VMIDs to be allocated in groups of adjacent or contiguous values, using one VMID in the PEs for the VM and one or more of the others to support different IPA address space views in different device stage 2 configurations.

Both broadcast TLB invalidation and explicit SMMU TLB invalidation commands, whether for stage 1 within the guest or at stage 2, affect all Non-secure VMIDs that match the group wildcard when SMMU\_CR0.VMW != 0.

Note: The broadcast TLB invalidation mechanisms that might exist on a PE and interconnect are not modified by this feature. The VMW field modifies the internal behavior of the SMMU on receipt of such a broadcast invalidation.

The VMID wildcard controlled by SMMU\_CR0.VMW only affects a VMID that matches on invalidation. The SMMUcontinues to store all bits of VMID in the TLB entries that require them, and does not allow dissimilar VMID values to alias on lookup.

The SMMU\_S\_CR0.VMW field provides a second Secure VMID wildcard feature that works in a similar way as described in this section, except affects Secure VMIDs only.

## 3.17.7 Broadcast TLB maintenance for GPT information

An SMMU with RME and SMMU\_ROOT\_IDR0.BGPTM == 1 participates in broadcast TLBI *PA* instructions from PEs that are executing in EL3.

Consistent with the definition for FEAT\_RME [2], a TLBI *PA* to the Outer Shareable shareability domain affects the SMMU.

This applies to all SMMUs with RME and SMMU\_ROOT\_IDR0.BGPTM == 1, regardless of the values of SMMU\_IDR0.BTM and SMMU\_(*\_)CR2.PTM.

Note: The behavior of SMMU\_IDR0.BTM and SMMU\_(*\_)CR2.PTM applies only to broadcast invalidations relating to stage 1 and stage 2 translation.

Note: An SMMU with RME does not have to receive the other broadcast TLBI operations. Support for broadcast operations is indicated in SMMU\_IDR0.BTM and configured in SMMU\_(*\_)CR2.PTM.

Note: The SMMU guarantees the same rules around observability and completion of TLBI *PA* and DSB instructions as defined in the RME specification.

## 3.17.8 TLBInXS maintenance operations

This section applies only when SMMU\_IDR0.BTM == 1.

An SMMU that participates in broadcast TLB maintenance operations must correctly interoperate with PEs that support the XS attribute and nXS variants of the TLBI and DSB instructions that were introduced in the Armv8.7-A architecture [2] under the feature name FEAT\_XS.

Note: The Armv8.7-A architecture [2] includes the following rules regarding the effects of the nXS qualifier on the TLBI and DSB instructions:

- TLBI instructions might be executed with or without the nXS qualifier.
- DSB instructions might be executed with or without the nXS qualifier.

- The HCRX\_EL2.FnXS control bit might override the effect of the nXS qualifier for TLBI instructions issued from EL1.

The requirements for an SMMU to interoperate with PEs that support the XS attribute and nXS variants of the TLBI and DSB instructions are as follows:

- The MAIR encodings 0b0000dd01 , 0b01000000 , and 0b10100000 remain Reserved, and the XS attribute is taken to be 0 for all MAIR encodings.
- Bit [11] of stage 2 block and page descriptors remain RES0, and the XS attribute is taken to be 0 for all stage 2 translations.
- The SMMU behaves as though the XS attribute for cached translations is 0 when determining the effect of a TLBI or TLBInXS operation.
- For each Security state, if the corresponding SMMU\_(*\_)CR2.PTM == 0:
- -The SMMU does not complete DSB instructions with the nXS qualifier until the requirements for previously-received TLBInXS operations are complete. This includes the case of TLBI instructions without the nXS qualifier issued from EL1 when HCRX\_EL2.FnXS == 1.
- -The SMMU does not complete DSB instructions without the nXS qualifier until the requirements for previously-received TLBI and TLBInXS operations are complete.