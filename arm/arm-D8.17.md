## D8.17 TLB maintenance

- RRVJDB For the purpose of TLB maintenance, a TLB entry is any structure that holds a translation table entry, including intermediate TLB caching structures and temporary working registers in translation table walk hardware.
- INDFND When a translation table walk occurs, translation table entries that are permitted to be cached in a TLB might be held in TLB caching structures.

RNWYRD Entries held in a TLB are distinguished by all of the following context information:

- The Security state.
- The translation regime, with the exception that hardware is not required to distinguish between EL2 and EL2&amp;0 TLB entries.
- If applicable to the translation regime, then the VMID.
- If applicable to the translation regime, then whether the translation is global or non-global.
- If the translation is non-global, then the ASID.
- RFFWJK TLBs, or TLB caching structures, are not guaranteed to remain coherent with changes to translation table entries, and are therefore distinct from data caches.

RZYZYK Indexing an intermediate TLB structure by the IA is permitted.

- RBKKRB If FEAT\_nTLBPA is not implemented, then indexing an intermediate TLB structure by all of the following is also permitted:
- The PA of the location holding the translation table entry.
- For stage 1 translations, the IPA of the location holding the translation table entry.
- RTJQVP If FEAT\_nTLBPA is not implemented, any TLB maintenance instruction that applies to a PE with the context information that is relevant to the translation table entry ensures cached copies of translation table entries are invalidated for that PE in all of the following implementations of intermediate TLB structures:
- Indexing the TLB using the PA of the location holding the translation table entry.
- For stage 1 translations, indexing the TLB using the IPA of the location holding the translation table entry.
- IPFNFJ FEAT\_nTLBPA permits software to determine the existence of intermediate TLB caching structures that are indexed by PA or IPA and perform TLB maintenance accordingly when it would otherwise not be required.

RLGSCG

RTVTYQ

When a TLB maintenance instruction targets only stage 1 entries, all of the following apply:

- The maintenance applies to any entries in caching structures that include stage 1 information used to translate the address or range of addresses being invalidated.
- If the TLB maintenance targets a specific ASID, then entries in caching structures that are not tagged with the specific ASID are not invalidated.
- If the stage 1 translation information contained in a single Block or Page has been collectively cached as one or more smaller TLB entries, for example as the result of splintering, then all entries containing that stage 1 information are invalidated, regardless of whether the entry would be used to translate the address being invalidated.

When a TLB maintenance instruction applies only to stage 2 entries, all of the following apply:

- The maintenance applies to any entries in caching structures that include only stage 2 information used to translate the address or range of addresses being invalidated.
- If the stage 2 translation information contained in a single Block or Page has been collectively cached as one or more smaller TLB entries, for example as the result of splintering, then all entries containing that stage 2 information are invalidated, regardless of whether the entry would be used to translate the address being invalidated.
- The maintenance is not required to apply to structures combining stage 1 and stage 2 information used to translate the address or range of addresses being invalidated.

RGNJPZ When a TLB maintenance instruction applies to both stage 1 and stage 2 entries, all of the following apply:

- The maintenance applies to any entries in caching structures that include stage 1 information.
- The maintenance applies to any entries in caching structures that include stage 2 information.

RPVVPF

- The maintenance applies to structures combining stage 1 and stage 2 information.

TLB maintenance instructions that remove dirty state from stage 2 entries apply to entries that meet all of the following requirements:

- The entry would be used for stage 2 translation. This applies if the TLB entry holds information from stage 2 translation only, or combined information from stage 1 and stage 2 translation.
- The entry would be used with the current VMID.
- The entry would be used in an EL1&amp;0 translation regime in the Security state selected by the Effective value of SCR\_EL3.{NSE, NS}.

RSYCZJ If the Effective value of SCR\_EL3.{NSE, NS} is {0, 0} and the value of SCR\_EL3.EEL2 is 0, then no TLB entries are affected by TLB maintenance instructions that only remove dirty state from stage 2 entries.

RNNZGV When a TLB maintenance instruction applies only to remove dirty state from stage 2 entries, in a manner consistent with clearing the S2AP[1] bit, or the Dirty bit if Indirect permissions are used, all of the following apply:

- If VTCR\_EL2.HD is 1 and the TLB entry was a cached copy of a writable-dirty descriptor, then a subsequent write access translated by that TLB entry causes hardware to update the stage 2 dirty state, including checking to ensure that the cached copy of the descriptor is not stale with regard to the descriptor in memory.
- If Direct permissions are used at stage 2, and the TLB entry was a cached copy of a descriptor that allowed write permission and had DBM = 0, then a subsequent write access translated by that TLB entry causes a check to ensure that the cached copy of the descriptor is not stale with regard to the descriptor in memory.
- If Indirect or Direct permissions are used at stage 2, but VTCR\_EL2.HD is 0, then it is permitted for a subsequent write access translated by that TLB entry to generate a stage 2 Permission fault.
- In all cases, over-invalidation is permitted, and it is possible that a subsequent write access causes a new translation table walk.

These requirements apply for all write accesses, including both explicit writes and implicit writes, such as writes that are part of a hardware update of a stage 1 translation table entry.

| R SWNLK   | TLB maintenance operations that only remove dirty state from stage 2 entries apply regardless of the stage 2 Overlay permissions. Only the Base permissions in the TLB entries determine the effect of these TLBI operations.                                                                                                                                                                                                                                            |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R GPPYH   | When a translation table entry associated with a specific VMIDor ASID is modified, software is required to invalidate the corresponding TLB entry to ensure that the modified translation table entry is visible to subsequent execution, including speculative execution.                                                                                                                                                                                               |
| R VNRFW   | When a System register field is modified and that field is permitted to be cached in a TLB, software is required to invalidate all TLB entries that might be affected by the field, at any address translation stage in the translation regime even if the translation stage is disabled, using the appropriate VMIDand ASID, after any required System register synchronization. For more information, see Synchronization requirements for AArch64 System registers.   |
| I WZCBG   | When a translation table entry that generates a Translation fault, Address size fault, or Access flag fault is changed to one that does not fault, all of the following apply to software: • TLB invalidation is not required because an entry that generates one of the listed faults is never cached in a TLB. • AContext synchronization event is required to ensure that the completed change to the translation table entry affects subsequent instruction fetches. |

## D8.17.1 Using break-before-make when updating translation table entries

RWHZWS If multiple execution threads use the same translation tables, then when a translation table entry is modified in one or more of the following ways, the architecture requires software to use a break-before-make sequence:

- Achange to the memory type, Shareability or Cacheability.
- The translation OA is changed and one or more of the following apply:
- -Either or both of the old and new translations grant write permission, including cases where the DBM bit is 1 and hardware updates of the dirty state is enabled.
- -The memory contents at the new OA do not match the memory contents at the previous OA.
- If software does not follow the sequence enabled by FEAT\_BBML1 and FEAT\_BBML2 is not implemented, all of the following changes to the block size used by the translation system:

RFVQCK

IHLHBH

- -Changing from a smaller size to a larger size, such as when a level 2 Table descriptor is replaced with a Block descriptor.
- -Changing from a larger size to a smaller size, such as when a level 2 Block descriptor is replaced with a Table descriptor.
- Aglobal entry is created that might overlap with non-global entries in a TLB.

IWZRHR Achange to the translation OA space is considered a change to the translation OA.

ITHWDH Use of a break-before-make sequence to ensure that old and new translation table entries are never simultaneously visible to different execution threads is guaranteed to prevent all of the following problems:

- Creating multiple TLB entries that apply to the same address.
- The effects of TLB caching breaking coherency.
- The effects of TLB caching breaking single-copy atomicity properties.
- The effects of TLB caching breaking ordering guarantees or uniprocessor semantics.
- The effects of TLB caching causing a failure to clear the Exclusives monitors.
- RDDMVT Abreak-before-make sequence requires all of the following steps:
1. Replace the old translation table entry with an invalid entry.
2. Execute a DSB instruction to ensure the invalid entry is visible.
3. Invalidate TLB entries based on the translation table entry with a broadcast TLB invalidation instruction.
4. Execute a DSB instruction to ensure the invalidation completes.
5. Write the new translation table entry
6. Execute a DSB instruction to ensure the new entry is visible.
- IGXGZY For a translation stage with AF hardware management enabled, if a translation table entry is modified and the break-before-make sequence is not followed, then all of the following failures associated with AF hardware updates can occur:
- When a memory location associated with that translation table entry is accessed, the AF is not set.
- When hardware updates to that translation table entry are followed by stores appearing later in program order, the ordering required is not followed.
- RRTBRL For a translation stage with dirty state hardware management enabled, if a translation table entry is modified and the break-before-make sequence is not followed, then all of the following failures associated with dirty state hardware updates can occur:
- When a memory location associated with that translation table entry is not written, hardware modifies the AP[2] or S2AP[1] descriptor bit.
- When a memory location associated with that translation table entry is written, hardware does not modify the AP[2] or S2AP[1] descriptor bit.
- When hardware updates to that translation table entry are followed by stores appearing later in program order, the ordering required is not followed.

If translation table entries are changed without appropriate TLB maintenance operations, including in the case where use of the break-before-make sequence is required but software does not follow the break-before-make sequence, it is possible that TLBs concurrently hold multiple different copies of those translation table entries.

In this situation, the following behaviors are permitted for a speculative or architectural access to the address resolved by those TLB entries:

- Use of the address matches multiple entries in a TLB, and a TLB conflict abort is detected. In this case, no access is made to memory based on those TLB entries. If the access is architectural, then the TLB conflict abort is reported as an exception.
- The resulting behavior is CONSTRAINED UNPREDICTABLE, and gives a behavior consistent with translation using one of the matching entries, or an amalgamation of more than one of the matching entries, but cannot permit access to memory regions with permissions or attributes that would not be possible in the current Security state at the current Exception level. This includes, for example:
- -Insufficient TLB maintenance for stage 1 translations by EL1 must not permit it to bypass the configuration of stage 2 translation.
- -Insufficient TLB maintenance by Non-secure state must not permit it to access any memory in Secure PA space.

For more information, see CONSTRAINED UNPREDICTABLE behaviors due to caching of control or data values.

## D8.17.2 Support levels for changing table or block size

RPVTFW

All statements in this section apply only to changing table or block sizes without changing any other property requiring break-before-make as specified in the rule RWHZWS in Using break-before-make when updating translation table entries.

RKFLJB

When a translation table entry is modified to change the table or block size, the hardware provides one of the following possible implementations affecting the break-before-make requirement to avoid breaking coherency, ordering guarantees or uniprocessor semantics, or failing to clear the Exclusives monitors:

- If FEAT\_BBML1 is not implemented, then software is required to use the break-before-make sequence.
- If FEAT\_BBML1 is implemented, then software can use all of the following:
- -The break-before-make sequence.
- -The nT bit in the Table descriptor or Block descriptor.
- If FEAT\_BBML2 is implemented, then software can change table or block size without breaking coherency, ordering guarantees or uniprocessor semantics, or failing to clear the Exclusives monitors.

For more information, see Block translation entry.

| R HHCXC   | When using a Table descriptor or Block descriptor with the nT bit set to 1, any accesses translated do not break coherency, ordering guarantees or uniprocessor semantics, or fail to clear the Exclusives monitors.                                                                                                                              |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I HYQMB   | If the TLB entries are not invalidated after the writes that modified the translation table entries are completed, then a TLB conflict abort can be generated because in a TLB there might be multiple translation table entries that all translate the same IA. For Table descriptors, this also applies to intermediate TLB caching structures. |
| I GYJBJ   | When an MMUfault is reported while changing table or block sizes but before completing the required TLBI to invalidate the old translation table entry, the syndrome information reported for the fault is consistent with one of the following:                                                                                                  |
| R KHRBC   | If FEAT_BBML1 is implemented, then changing the Contiguous bit in a set of Block descriptors or Page descriptors be done without breaking coherency, ordering guarantees or uniprocessor semantics, or failing to clear the Exclusives monitors.                                                                                                  |
| R FCPSG   | If FEAT_BBML1 is implemented and the Contiguous bit in a set of Block descriptors or Page descriptors is changed, then a TLB conflict abort can be generated because multiple translation table entries might exist within a TLB that translates the same IA.                                                                                     |
| I CFFVK   | If FEAT_BBML1 is implemented and a TLB conflict abort is generated, then TLB maintenance is required to remove the multiple TLB entries that translate the same address. For Table descriptors, this also applies to intermediate TLB caching structures. For more information, see TLB maintenance due to TLB conflict.                          |

## D8.17.3 TLB maintenance due to TLB conflict

| R BLRKC   | If multiple TLB entries translate the same address, then the ALL or VMALL form of a TLB maintenance instruction that targets the given translation regime is guaranteed to remove all TLB entries within that regime.                                                                                                                                                                                                                                                   |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I JCCRT   | All of the following instructions are guaranteed to remove the TLB entries associated with a conflict: • For the EL1&0 translation regime, when stage 2 translations are in use, either VMALLS12E1 or ALLE1 . • For the EL1&0 translation regime, when stage 2 translations are not in use, either VMALLE1 or ALLE1 . • For the EL2&0 translation regime, either VMALLE1 or ALLE2 . • For the EL2 translation regime, ALLE2 . • For the EL3 translation regime, ALLE3 . |
| R GRVDR   | If multiple TLB entries translate the same address, then the minimum set of TLB maintenance operations required to guarantee all TLB entries associated with that address and translation regime have been invalidated is IMPLEMENTATION DEFINED.                                                                                                                                                                                                                       |

## D8.17.4 The interaction of TLB lockdown with TLB maintenance instructions

| R VGPNS   | If a TLB entry is locked and a TLB invalidate all instruction is executed and, if that entry was not locked the TLB invalidate all instruction would invalidate that entry, then one of the following IMPLEMENTATION DEFINED behaviors occur: • The locked TLB entry is not affected.               |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I FRJSL   | The IMPLEMENTATION DEFINED Data Abort on a TLB invalidate all instruction permits TLB invalidation routines to choose to invalidate a large range of addresses, without considering whether any TLB entries are locked, or to not affect locked TLB entries.                                        |
| R BMHZW   | If a TLB entry is locked and a TLB invalidate by VAor invalidate by ASID instruction is executed and, if that entry was not locked the TLB invalidate by VA or invalidate by ASID instruction would invalidate that entry, then one of the following IMPLEMENTATION DEFINED behaviors occur:        |
| I FXBBY   | The exception syndrome definitions include a fault code for cache and TLB lockdown faults.                                                                                                                                                                                                          |
| R BCLPC   | If an implementation uses an abort mechanism when entries that can be locked down are not actually locked down, then all of the following are required: • The IMPLEMENTATION DEFINED instruction sequences that perform the required operations on entries that are not locked down are documented. |
| I DRZHY   | If an implementation supports TLB lockdown, then Arm recommends that IMPLEMENTATION DEFINED TLB maintenance instruction sequences use the architecturally-defined operations to minimize the number of customized operations required.                                                              |
| I PNDQN   | For more information on TLB lockdown, see TLB lockdown.                                                                                                                                                                                                                                             |

## D8.17.5 TLB maintenance instructions

IQJNCT

IXMWNR

IJFCRF

IKTDKY

For a given translation regime, the architecture defines TLB maintenance instructions that provide all of the following functions:

- Invalidate all corresponding entries in a TLB.
- Invalidate a corresponding single TLB entry by ASID for a non-global entry.
- Invalidate all corresponding TLB entries that match a specific ASID.
- Invalidate all corresponding TLB entries that match a specific V A, regardless of the ASID.
- Invalidate all corresponding TLB entries within a range of addresses.
- Update all corresponding stage 2 TLB entries that match a specific VMID from writable-dirty to writable-clean.

Each TLB maintenance instruction can be applied to one of the following:

- Only the PE that executes the instruction
- All PEs in the same Shareability domain as the PE that executes the instruction.

The A64 assembly language syntax of a TLB maintenance instruction is TLBI{P} &lt;operation&gt;{, &lt;Xt&gt;} .

All of the following apply to the TLB maintenance instructions:

- The TLBI operations take zero or one register arguments, for cases where 64 bits or fewer of scope information is required.
- The TLBIP operations take a pair of register arguments, for cases where more than 64 bits of scope information is required.

## ILHQBV When VMSAv9-128 is in use, all of the following apply:

- For TLBI RVA* instructions, BaseADDR[52:16] is determined by input bits [36:0], and BaseADDR[55:53] is treated as having the same value as BaseADDR[52] .
- For TLBI RIPA* instructions, BaseADDR[52:16] is determined by input bits [36:0], and BaseADDR[55:53] is treated as 0.

## IRJQTT For the TLBI instructions, the invalidation scope applies to VMSAv8-64 and VMSAv9-128 TLB entries, except for all of the following:

- For TLBI VA* and TLBI RVA* instructions, when a translation table level hint is provided, the invalidation scope only applies to stage 1 VMSAv8-64 TLB entries.
- For TLBI IPA* , TLBI RIPA* instructions, when a translation table level hint is provided, the invalidation scope only applies to stage 2 VMSAv8-64 TLB entries.

## IBDQZT For the TLBIP instructions, the invalidation scope applies to VMSAv8-64 and VMSAv9-128 TLB entries, except for all of the following:

- For TLBIP VA* and TLBIP RVA* instructions, when a translation table level hint is provided, the invalidation scope only applies to stage 1 VMSAv9-128 entries.
- For TLBIP IPA* , TLBIP RIPA* instructions, when a translation table level hint is provided, the invalidation scope only applies to stage 2 VMSAv9-128 TLB entries.

## INDJSJ The &lt;operation&gt; in TLBI{P} &lt;operation&gt;{, &lt;Xt&gt;}

- For TLBI instructions:
- -ALLE1{NXS} , ALLE2{NXS} , ALLE3{NXS} , ALLE1IS{NXS} , ALLE2IS{NXS} , ALLE3IS{NXS} , ALLE1OS{NXS} , ALLE2OS{NXS} , or ALLE3OS{NXS} .
- -VMALLE1{NXS} , VMALLE1IS{NXS} , VMALLE1OS{NXS} , VMALLS12E1{NXS} , VMALLS12E1IS{NXS} , VMALLS12E1OS{NXS} , VMALLWS2E1{NXS} , VMALLWS2E1IS{NXS} , or VMALLWS2E1OS{NXS} .
- -ASIDE1{NXS} , ASIDE1IS{NXS} , or ASIDE1OS{NXS} .
- For TLBI and TLBIP instructions:
- -{R}VA{L}E1{NXS} , {R}VA{L}E2{NXS} , {R}VA{L}E3{NXS} , {R}VA{L}E1IS{NXS} , {R}VA{L}E2IS{NXS} , {R}VA{L}E3IS{NXS} , {R}VA{L}E1OS{NXS} , {R}VA{L}E2OS{NXS} , or {R}VA{L}E3OS{NXS} .
- -{R}VAA{L}E1{NXS} , {R}VAA{L}E1IS{NXS} , or {R}VAA{L}E1OS{NXS} .
- -{R}IPAS2{L}E1{NXS} , {R}IPAS2{L}E1IS{NXS} , or {R}IPAS2{L}E1OS{NXS} .

## IDMCXY The &lt;operation&gt; in TLBI{P} &lt;operation&gt;{, &lt;Xt&gt;} has a structure of

{R}&lt;type&gt;&lt;regime&gt;&lt;shareability&gt;{NXS} with all of the following components:

- R is optional and determines one of the following:
- -When present, the instruction applies to all TLB entries translating addresses within the address range.
- -When not present, the instruction applies to all TLB entries translating a single address that could be used by the PE that executes the TLB maintenance instruction.
- &lt;type&gt; is one of the following:
- -ALL specifies all translations at &lt;regime&gt; .
- -VMALL specifies all stage 1 translations for the affected translation regime, and if applicable, matching the current VMID.
- -VMALLS12 specifies all stage 1 and stage 2 translations at EL1 with the current VMID.
- -VMALLWS2 specifies all writable-dirty stage 2 translations at EL1 with the current VMID.
- -ASID specifies all non-global translations for the affected translation regime with the supplied ASID.
- -VA{L} specifies all translations at &lt;regime&gt; using the supplied address and, if an ASID is supplied, the supplied ASID or global entries.
- -VAA{L} specifies all global entries and non-global entries, regardless of the ASID value, for the affected translation regime using the supplied address.
- -IPAS2{L} specifies all stage 2 translations using the supplied IPA.
- For the VA{L} , VAA{L} , and IPAS2{L} types, L is an optional parameter specifying that the invalidation applies only to cached entries containing translation information returned by the final lookup level of the translation table walk.
- &lt;regime&gt; is one of the following Exception levels:
- -If E1 , then EL1.

is one of the following:

IBNSBV

- -If E2 , then EL2.
- -If E3 , then EL3.
- &lt;shareability&gt; is one of the following:
- -IS indicates that the instruction applies to all TLBs in the Inner Shareable domain.
- -OS indicates that the instruction applies to all TLBs in the Outer Shareable domain.
- -The parameter is optional, and no value indicates that the instruction applies to all TLBs that could be used by the PE that executes the instruction.
- NXS has all of the following properties:
- -The parameter is optional.
- -When present, the instruction is considered complete after all issued memory transactions using translation information held in TLB entries that have the associated XS attribute set to 0 and are within the scope of the instruction, are complete.
- -When not present, the instruction is considered complete after all issued memory transactions using translation information held in TLB entries that are within the scope of the instruction are complete, regardless of the XS attribute value.
- -The parameter can only be present when FEAT\_XS is implemented.

IYKBMJ If &lt;regime&gt; is higher than the current Exception level, then the TLB maintenance instruction is UNDEFINED.

IDJQYS

IXMYBL

ISRWLL

All TLB maintenance instructions are UNDEFINED at EL0.

Unless trapped by HCR\_EL2.NV to EL2, then all of the following TLB maintenance instructions are UNDEFINED at EL1:

- TLBI ALLE1{NXS} , TLBI ALLE1IS{NXS} , and TLBI ALLE1OS{NXS} .
- TLBI{P} {R}IPAS2{L}E1{NXS} , TLBI{P} {R}IPAS2{L}E1IS{NXS} , and TLBI{P} {R}IPAS2{L}E1OS{NXS} .
- TLBI VMALLS12E1{NXS} , TLBI VMALLS12E1IS{NXS} , and TLBI VMALLS12E1OS{NXS} .
- TLBI VMALLWS2E1{NXS} , TLBI VMALLWS2E1IS{NXS} , and TLBI VMALLWS2E1OS{NXS} .

If EL2 is not implemented, then all of the following TLB instructions are UNDEFINED:

- TLBI{P} {R}VA{L}E2{NXS} , TLBI{P} {R}VA{L}E2IS{NXS} , and TLBI{P} {R}VA{L}E2OS{NXS} .
- TLBI ALLE2{NXS} , TLBI ALLE2IS{NXS} , and TLBI ALLE2OS{NXS} .

IBWGVK When a TLB entry is invalidated by one PE, it is inconsistent with the architecture to allow another PE to refill that TLB

entry so that the new entry gives the appearance to software that the invalidation did not occur.

The &lt;Xt&gt; in TLBI{P} &lt;operation&gt;{, &lt;Xt&gt;} has all of the following properties:

- It specifies a register that passes one or both of an address and an ASID as an argument.
- For operations that include a V A, if FEAT\_TTL is implemented, then the register passes the level hint.
- For range-based TLB maintenance operations, then the register passes information about the address range.
- It is required by the TLBI ASID , TLBI{P} {R}VA{L} , TLBI{P} {R}VAA{L} , and TLBI{P} {R}IPAS2{L} instructions.

## D8.17.5.1 TLB maintenance instructions that do not apply to a range of addresses

IZVNJG For TLB maintenance instructions that take a V A, an ASID, or both as an argument, and that do not apply to a range of addresses, the register specified by the Xt argument has the following format:

- Register bits[63:48] are one of the following:
- -If the instruction requires an ASID argument, the ASID.
- -If the instruction does not require an ASID argument, RES0.
- If FEAT\_TTL is not implemented, then register bits[47:44] are RES0.
- If FEAT\_TTL is implemented, then register bits[47:44] are one of the following:
- -If the instruction requires a V A argument, the translation table level hint, TTL.
- -If the instruction does not require a V A argument, RES0.
- Register bits[43:0] are one of the following:
- -If the instruction requires a V A argument, V A[55:12].
- -If the instruction does not require a V A argument, RES0.

- RJGGKN For TLB maintenance instructions that take a V A, hardware interprets V A[63:56] as each having the same value as

VA[55].

- RFGPTT For TLB maintenance instructions that take a V A, if the instruction targets a translation regime that is using AArch32, then all of the following apply:
- Software is required to treat V A[55:32] as RES0.
- VA[55:32] are ignored when the instruction is executed, and interpreted as being zero.
- VA[63:56] are interpreted as being zero.
- ILHKCP If the implementation supports 16-bit ASIDs, then software is required to set the upper 8 bits of the ASID to 0 when the context being invalidated uses only 8 bits.
- ICPNYZ For TLB maintenance instructions that take a register argument that holds an IPA and that do not apply to a range of addresses, the register specified by the Xt argument has the following format:
- Register bit[63] is one of the following:
- -If the Effective value of SCR\_EL3.{NSE, NS} is {0, 0}, the NS bit specifying the Secure or Non-secure IPA space.
- -If the Effective value of SCR\_EL3.{NSE, NS} is {0, 1}, this field is RES0 and the instruction applies to the Non-secure IPA space.
- -If the Effective value of SCR\_EL3.{NSE, NS} is {1, 1}, this field is RES0 and the instruction applies to the Realm IPA space.
- -If the Effective value of SCR\_EL3.{NSE, NS} is {1, 0}, the instruction is not required to invalidate any TLB entries.
- If FEAT\_TTL is not implemented, then register bits[62:40] are RES0.
- If FEAT\_TTL is implemented, then all of the following apply:
- -Register bits[62:48] are RES0.
- -Register bits[47:44] are the translation table level hint, TTL.
- -Register bits[43:40] are RES0.
- Register bits[39:36] are one of the following:
- -If 52-bit addresses are supported, IPA[51:48].
- -If 52-bit addresses are not supported, RES0.
- Register bits[35:0] are IPA[47:12].

IHQTLK For TLB maintenance instructions that take a register argument that holds a V A or an IPA, register bits that hold the address have all of the following properties:

- If the 4KB granule size is used, all address bits in the register bits are used by the invalidation instruction.
- If the 16KB granule size is used, register bits[1:0] are ignored because address bits[13:12] have no effect on the invalidation instruction.
- If the 64KB granule size is used, register bits[3:0] are ignored because address bits[15:12] have no effect on the invalidation instruction.

## D8.17.5.2 TLB maintenance instructions that apply to a range of addresses

- IQPHNP For TLB maintenance instructions that take a V A, or a V A and an ASID, and that apply to a range of addresses, the register specified by the Xt argument has the following format:
- Register bits[63:48] are one of the following:
- -If the instruction requires an ASID argument, the ASID.
- -If the instruction does not require an ASID argument, RES0.
- Register bits[47:46] are the translation granule size, TG.
- Register bits[45:44] are the SCALE field that is the exponent element of the calculation that produces the upper range.
- Register bits[43:39] are the NUM field that is the base element of the calculation that produces the upper range.
- If FEAT\_TTL is not implemented, then register bits[38:37] are RES0.
- If FEAT\_TTL is implemented, then register bits[38:37] are the translation table level hint, TTL.
- Register bits[36:0] give the starting address of the range of addresses, BaseADDR.

For TLB maintenance instructions that take a register argument that holds an IPA and that apply to a range of addresses, the register specified by the Xt argument has the following format:

IXPNPP

RPVVXP

- Register bit[63] is one of the following:
- -If the Effective value of SCR\_EL3.{NSE, NS} is {0, 0}, the NS bit specifying the Secure or Non-secure IPA space.
- -If the Effective value of SCR\_EL3.{NSE, NS} is {0, 1}, this field is RES0 and the instruction applies to the Non-secure IPA space.
- -If the Effective value of SCR\_EL3.{NSE, NS} is {1, 1}, this field is RES0 and the instruction applies to the Realm IPA space.
- -If the Effective value of SCR\_EL3.{NSE, NS} is {1, 0}, the instruction is not required to invalidate any TLB entries.
- Register bits[62:48] are RES0.
- Register bits[47:46] are the translation granule size, TG.
- Register bits[45:44] are the SCALE field that is the exponent element of the calculation that produces the upper range.
- Register bits[43:39] are the NUM field that is the base element of the calculation that produces the upper range.
- If FEAT\_TTL is not implemented, then register bits[38:37] are RES0.
- If FEAT\_TTL is implemented, then register bits[38:37] are the translation table level hint, TTL.
- Register bits[36:0] specify the starting address of the range of addresses, BaseADDR.

For TLB instructions that apply to a range of addresses, the following table shows the TG field encodings that define the translation granule size for the translations that are being invalidated, and the Translation\_Granule\_Size in bytes used in determining the address range.

## Table D8-122 TG field encodings in TLB instructions that apply to a range of addresses

|   TG | Translation granule size   | Translation_Granule_Size   |
|------|----------------------------|----------------------------|
|   00 | Reserved                   | N/A                        |
|   01 | 4KB translation granule    | 4096                       |
|   10 | 16KB translation granule   | 16384                      |
|   11 | 64KB translation granule   | 65536                      |

RXKMMX

For TLB instructions that apply to a range of addresses, if the translations use a different translation granule size than the one specified by the TG field, then the architecture does not require that the instruction invalidate those entries.

RQKRKL

RQNPXY

IHKYNQ

For all TLB range maintenance instructions, TLB entries that translate one or more addresses within the address range determined by the following formula are invalidated:

[BaseADDR &lt;= input\_address &lt; BaseADDR + ((NUM +1)*2^(5*SCALE +1) * Translation\_Granule\_Size)] .

For a translation regime that supports two V A ranges, if a TLB range maintenance instruction is issued with an address in the TTBR1\_ELx half of the VA space, and the SCALE and NUM values cause the range to exceed the top of the address space, then the address is not considered to wrap on overflow and the PE is not required to invalidate any entries inserted for the corresponding TTBR0\_ELx half of the VA space.

For a TLBI range maintenance instruction, BaseADDR is derived from bits[36:0] in the register specified by the Xt argument as one of the following:

- For the 4KB granule size, one of the following:
- -If the Effective value of TCR\_EL1.DS is 0, then BaseADDR[48:12] .
- -If the Effective value of TCR\_EL1.DS is 1, then BaseADDR[52:16] . In this case, BaseADDR[15:12] is treated as all zero.
- For the 16KB granule size, one of the following:
- -If the Effective value of TCR\_EL1.DS is 0, then BaseADDR[50:14] .
- -If the Effective value of TCR\_EL1.DS is 1, then BaseADDR[52:16] . In this case, BaseADDR[15:14] is treated as all zero.

ITYBWT

- For the 64KB granule size, BaseADDR[52:16] .

For all of the following, the invalidated address range is UNPREDICTABLE:

- For the 4KB translation granule, one of the following:
- -The Effective value of TCR\_EL1.DS is 1, the TTL field is 0b00 , and BaseADDR[38:12] are not all zero.
- -The TTL field is 0b01 and BaseADDR[29:12] are not all zero.
- -The TTL field is 0b10 and BaseADDR[20:12] are not all zero.
- For the 16KB translation granule, one of the following:
- -The Effective value of TCR\_EL1.DS is 1, the TTL field is 0b01 , and BaseADDR[35:14] are not all zero.
- -The TTL field is 0b10 and BaseADDR[24:14] are not all zero.
- For the 64KB translation granule, one of the following:
- -The TTL field is 0b01 and BaseADDR[41:16 ] are not all zero.
- -The TTL field is 0b10 and BaseADDR[28:16] are not all zero.

| I ZNXDY   | For more information, see Broadcast TLB maintenance.                                                                                                                                               |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R BLDQZ   | All statements in this section require implementation of FEAT_TTL.                                                                                                                                 |
| I LTZBK   | For the address being invalidated by a TLB maintenance instruction, the TTL field in the register specified by Xt indicates the lookup level of the translation table walk holding the leaf entry. |
| I WVDLN   | Hardware can use the TTL field to determine if the page might have been splintered into multiple TLB entries.                                                                                      |
| R SQXYZ   | For an entry being invalidated by a TLB maintenance instruction, if an incorrect TTL value is specified, then the architecture does not require any entries to be invalidated from a TLB.          |
| I VWPQL   | For TLB instructions that apply to a single address, the following table shows the 4-bit TTL field encodings.                                                                                      |

Table D8-123 TTL field encodings in TLB instructions that apply to a single address

|   TTL[3:2] | Translation granule   | TTL[1:0]   | Information supplied                                                                                                                                                                                                                            |
|------------|-----------------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|         00 | -                     | RES0       | No information supplied about the translation level. Hardware assumes that the leaf entry can be from any level.                                                                                                                                |
|         01 | 4KB                   | 00         | If FEAT_LPA2 is not implemented, then this value is reserved, and hardware treats this as if TTL[3:2] is 0b00 . If FEAT_LPA2 is implemented, then the leaf entry for the address being invalidated is on level 0 of the translation table walk. |
|         01 | 4KB                   | 01         | The leaf entry for the address being invalidated is on level 1 of the translation table walk.                                                                                                                                                   |
|         01 | 4KB                   | 10         | The leaf entry for the address being invalidated is on level 2 of the translation table walk.                                                                                                                                                   |
|         01 | 4KB                   | 11         | The leaf entry for the address being invalidated is on level 3 of the translation table walk.                                                                                                                                                   |
|         10 | 16KB                  | 00         | This value is reserved, and hardware treats this as if TTL[3:2] is 0b00 .                                                                                                                                                                       |
|         10 | 16KB                  | 01         | If FEAT_LPA2 is not implemented, then this value is reserved, and hardware treats this as if TTL[3:2] is 0b00 . If FEAT_LPA2 is implemented, then the leaf entry for the address being invalidated is on level 1 of the translation table walk. |

| TTL[3:2]   | Translation granule   |   TTL[1:0] | Information supplied                                                                          |
|------------|-----------------------|------------|-----------------------------------------------------------------------------------------------|
|            |                       |         10 | The leaf entry for the address being invalidated is on level 2 of the translation table walk. |
|            |                       |         11 | The leaf entry for the address being invalidated is on level 3 of the translation table walk. |
| 11         | 64KB                  |         00 | This value is reserved, and hardware treats this as if TTL[3:2] is 0b00 .                     |
| 11         | 64KB                  |         01 | The leaf entry for the address being invalidated is on level 1 of the translation table walk. |
| 11         | 64KB                  |         10 | The leaf entry for the address being invalidated is on level 2 of the translation table walk. |
| 11         | 64KB                  |         11 | The leaf entry for the address being invalidated is on level 3 of the translation table walk. |

IVNDBJ

For TLB instructions that apply to a range of addresses, the following table shows the 2-bit TTL field encodings.

## Table D8-124 TTL field encodings in TLB instructions that apply to a range of addresses

|   TTL | Information supplied                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    00 | The leaf entries in the range can be using any level for the translation table entries.                                                                                                                                                                                                                                                                                                                                  |
|    01 | When the 4KB or 64KB translation granule is used, all leaf entries to invalidate are level 1 translation table entries. If FEAT_LPA2 is not implemented, then when using a 16KB translation granule, this value is reserved, and hardware treats this as if TTL is 0b00 . If FEAT_LPA2 is implemented, then when using a 16KB translation granule, all leaf entries to invalidate are level 1 translation table entries. |
|    10 | All leaf entries to invalidate are level 2 translation table entries.                                                                                                                                                                                                                                                                                                                                                    |
|    11 | All leaf entries to invalidate are level 3 translation table entries.                                                                                                                                                                                                                                                                                                                                                    |

## D8.17.5.4 TLB maintenance instruction scope

If &lt;type&gt; is ALL in a TLB maintenance instruction, then all of the following apply:

- For all values of &lt;regime&gt; , the instruction exists.
- For the Security state specified by the Effective value of SCR\_EL3.{NSE, NS} and for the value of SCR\_EL3.EEL2, the instruction applies to all cached copies of the stage 1 and stage 2 translation table entries from any lookup level in the translation table walk required to translate any address at the specified Exception level.
- If EL2 is enabled, then for entries from the EL1&amp;0 translation regime the instruction applies to cached copies of translation table entries with any VMID.
- For entries from a translation regime in which an ASID is valid, the instruction applies to all of the following cached copies of translation table entries from any lookup level in the translation table walk:
- -Global entries.
- -Non-global entries with any ASID.

If &lt;type&gt; is VMALL in a TLB maintenance instruction, then all of the following apply:

- If and only if the value of &lt;regime&gt; is E1, then the instruction applies to all of the following:
- -When the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, then the EL1&amp;0 translation regime.
- -When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, then the EL2&amp;0 translation regime.
- For the Security state specified by the Effective value of SCR\_EL3.{NSE, NS} and for the value of SCR\_EL3.EEL2, the instruction applies to all cached copies of the stage 1 translation table entries from any lookup level in the translation table walk required to translate any address at the specified Exception level.
- If EL2 is enabled, then for entries from the EL1&amp;0 translation regime the instruction applies only to cached copies of translation table entries with the current VMID.

RWHKKS

RPMNQC

RBMMCC

RJQQFG

RFKSVM

RDRCZZ

- For entries from a translation regime in which an ASID is valid, the instruction applies to all of the following cached copies of translation table entries from any lookup level in the translation table walk:
- -Global entries.
- -Non-global entries with any ASID.

If &lt;type&gt; is VMALLS12 in a TLB maintenance instruction, then all of the following apply:

- If and only if the value of &lt;regime&gt; is E1, then the instruction applies to the EL1&amp;0 translation regime.
- For the Security state specified by the Effective value of SCR\_EL3.{NSE, NS} and for the value of SCR\_EL3.EEL2, the instruction applies to all cached copies of the stage 1 and stage 2 translation table entries from any lookup level in the translation table walk required to translate any address at the specified Exception level.
- The instruction applies only to cached copies of translation table entries with the current VMID.
- For entries from a translation regime in which an ASID is valid, the instruction applies to all of the following cached copies of translation table entries from any lookup level in the translation table walk:
- -Global entries.
- -Non-global entries with any ASID.
- If one of the following is true and the instruction is executed at EL3, the instruction is not UNDEFINED and has the same effect as TLBI VMALL because there are no stage 2 translations to invalidate:
- -EL2 is not implemented.
- -The Effective value of SCR\_EL3.NS is 0 and EL2 is disabled.

If &lt;type&gt; is VMALLWS2 in a TLB maintenance instruction, then all of the following apply:

- The value of &lt;regime&gt; is always E1, and the instruction applies to the EL1&amp;0 translation regime.
- For the Security state specified by the Effective value of SCR\_EL3.{NSE, NS} and for the value of SCR\_EL3.EEL2, the instruction applies to all writable-dirty cached copies of the stage 2 translation table entries from any lookup level in the translation table walk required to translate any address at the specified Exception level.
- The instruction applies only to cached copies of translation table entries with the current VMID.
- Entries affected by the instruction are updated to writable-clean but are not required to be invalidated.

If &lt;type&gt; is ASID in a TLB maintenance instruction, then all of the following apply:

- If and only if the value of &lt;regime&gt; is E1, then the instruction applies to all of the following:
- -When the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, then the EL1&amp;0 translation regime when executing at EL1.
- -When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, then the EL2&amp;0 translation regime when executing at EL2.
- For the Security state specified by the Effective value of SCR\_EL3.{NSE, NS} and for the value of SCR\_EL3.EEL2, the instruction applies to all cached copies of the stage 1 translation table entries from any lookup level in the translation table walk required to translate any address at the specified Exception level.
- If EL2 is enabled, then for entries from the EL1&amp;0 translation regime the instruction applies only to cached copies of translation table entries with the current VMID.
- The instruction applies only to non-global entries from the final lookup level that matches the specified ASID.

RVMSWQ If &lt;type&gt; is VA

in a TLB maintenance instruction, then all of the following apply:

- For all values of &lt;regime&gt; , the instruction exists.
- For the Security state specified by the Effective value of SCR\_EL3.{NSE, NS} and for the value of SCR\_EL3.EEL2, the instruction applies to all cached copies of the stage 1 translation table entries from any lookup level in the translation table walk required to translate the address at the specified Exception level.
- If EL2 is enabled, then for entries from the EL1&amp;0 translation regime the instruction applies only to cached copies of translation table entries with the current VMID.
- For instructions where the value of &lt;regime&gt; is E2, the instruction applies to the EL2&amp;0 or EL2 translation regime, as determined by the Effective value of HCR\_EL2.E2H.
- For entries from a translation regime in which an ASID is valid, the instruction applies only to all of the following cached copies of translation table entries:
- -Anon-global entry from any lookup level that matches the specified ASID.
- -Aglobal entry from the final lookup level.

If &lt;type&gt; is VAL in a TLB maintenance instruction, then all of the following apply:

- For all values of &lt;regime&gt; , the instruction exists.
- For the Security state specified by the Effective value of SCR\_EL3.{NSE, NS} and for the value of SCR\_EL3.EEL2, the instruction applies to all cached copies of the stage 1 translation table entries from the final lookup level in the translation table walk required to translate the address at the specified Exception level.
- If EL2 is enabled, then for entries from the EL1&amp;0 translation regime the instruction applies only to cached copies of translation table entries from the final lookup level with the current VMID.
- For instructions where the value of &lt;regime&gt; is E2, the instruction applies to the EL2&amp;0 or EL2 translation regime, as determined by the Effective value of HCR\_EL2.E2H.
- For entries from a translation regime in which an ASID is valid, the instruction applies only to all of the following cached copies of translation table entries:
- -Anon-global entry from the final lookup level that matches the specified ASID.
- -Aglobal entry from the final lookup level.

RZSXRQ If &lt;type&gt; is VAA in a TLB maintenance instruction, then all of the following apply:

- If and only if the value of &lt;regime&gt; is E1, then the instruction applies to all of the following:
- -When the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, then the EL1&amp;0 translation regime when executing at EL1.
- -When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, then the EL2&amp;0 translation regime when executing at EL2.
- For the Security state specified by the Effective value of SCR\_EL3.{NSE, NS} and for the value of SCR\_EL3.EEL2, the instruction applies to all cached copies of the stage 1 translation table entries from any lookup level in the translation table walk required to translate the address at the specified Exception level.
- If EL2 is enabled, then for entries from the EL1&amp;0 translation regime the instruction applies only to cached copies of translation table entries with the current VMID.
- For instructions where the value of &lt;regime&gt; is E2, the instruction applies to the EL2&amp;0 or EL2 translation regime, as determined by the Effective value of HCR\_EL2.E2H.
- The instruction applies to all of the following cached copies of translation table entries from any lookup level in the translation table walk:
- -Global entries.
- -Non-global entries with any ASID.

RJXKNN If &lt;type&gt; is VAAL in a TLB maintenance instruction, then all of the following apply:

- If and only if the value of &lt;regime&gt; is E1, then the instruction applies to all of the following:
- -When the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, then the EL1&amp;0 translation regime when executing at EL1.
- -When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, then the EL2&amp;0 translation regime when executing at EL2.
- For the Security state specified by the Effective value of SCR\_EL3.{NSE, NS} and for the value of SCR\_EL3.EEL2, the instruction applies to all cached copies of the stage 1 translation table entries from the final lookup level in the translation table walk required to translate the address at the specified Exception level.
- If EL2 is enabled, then for entries from the EL1&amp;0 translation regime the instruction applies only to cached copies of translation table entries from the final lookup level with the current VMID.
- For instructions where the value of &lt;regime&gt; is E2, the instruction applies to the EL2&amp;0 or EL2 translation regime, as determined by the Effective value of HCR\_EL2.E2H.
- The instruction applies to all of the following cached copies of translation table entries from the final lookup level in the translation table walk:
- -Global entries.
- -Non-global entries with any ASID.

RVZZVZ If &lt;type&gt; is IPAS2

in a TLB maintenance instruction, then all of the following apply:

- If and only if the value of &lt;regime&gt; is E1, and if EL2 is enabled, then the instruction applies only to the EL1&amp;0 translation regime.
- If all of the following apply, the instruction applies to all cached copies of the stage 2 translation table entries from any lookup level in the translation table walk required to translate the address:
- -The TLB entry holds only a stage 2 translation table entry.
- -The entry applies only to the current VMID.
- The instruction is not required to invalidate TLB entries that combine stage 1 and stage 2 translation table entries.

RNSDNR

RKBSSD

- If one of the following is true, then the instruction executes as a NOP:
- -EL2 is not implemented.
- -The Effective value of SCR\_EL3.NS is 0 and EL2 is disabled.

If &lt;type&gt; is IPAS2L in a TLB maintenance instruction, then all of the following apply:

- If and only if the value of &lt;regime&gt; is E1, and if EL2 is enabled, then the instruction applies only to the EL1&amp;0 translation regime.
- If all of the following apply, the instruction applies to all cached copies of the stage 2 translation table entries from the final lookup level in the translation table walk required to translate the address:
- -The TLB entry holds only a stage 2 translation table entry.
- -The entry applies only to the current VMID.
- The instruction is not required to invalidate TLB entries that combine stage 1 and stage 2 translation table entries.
- If one or more of the following is true, then the instruction executes as a NOP:
- -EL2 is not implemented.
- -The Effective value of SCR\_EL3.NS is 0 and EL2 is disabled.

It is IMPLEMENTATION SPECIFIC whether a TLBI maintenance operation with the nXS qualifier invalidates TLB entries with the XS attribute set to 1.

## D8.17.6 Operation of the TLB maintenance instructions

- RXQBCL ATLBmaintenance instruction applies whether a translation stage is enabled or disabled.

RKKDKL ATLBmaintenance instruction can affect any TLB entries that are not locked down.

- IYGYRY There is no guarantee that an unlocked TLB entry remains in the cache. Therefore, it is not possible to determine architecturally whether a TLB maintenance instruction has affected any TLB entries that were not specified by the instruction.

ILMGTM The TLB maintenance instructions specify the Exception level of the translation regime to which they apply.

RTBLDD ATLBmaintenance instruction never generates an MMU abort.

IBDTLG If EL3 is implemented, then the Effective value of SCR\_EL3.{NSE, NS} modifies the effect of the TLB maintenance instructions in all of the following ways:

- For instructions that apply to the EL2 or EL2&amp;0 translation regime, if SCR\_EL3.{EEL2, NS} is not {0, 0}, then all of the following apply:
- -If the Effective value of SCR\_EL3.{NSE, NS} is {0, 0}, then the instruction applies to the Secure variant of the corresponding regime.
- -If the Effective value of SCR\_EL3.{NSE, NS} is {0, 1}, then the instruction applies to the Non-secure variant of the corresponding regime.
- -If the Effective value of SCR\_EL3.{NSE, NS} is {1, 1}, then the instruction applies to the Realm variant of the corresponding regime.
- -If the Effective value of SCR\_EL3.{NSE, NS} is {1, 0}, then the instruction is not required to invalidate any TLB entries.
- If SCR\_EL3.{EEL2, NS} is {0, 0}, then instructions that apply to the EL2 or EL2&amp;0 translation regime are UNDEFINED.
- For instructions that apply to the EL3 translation regime, the Effective value of SCR\_EL3.{NSE, NS} has no effect.

ATLBmaintenance instruction is not affected by the current state of all of the following control bits involved in the translation process:

- In AArch64 state, all of the following:
- -SCTLR\_EL1.M.
- -SCTLR\_EL2.M.
- -SCTLR\_EL3.{M, RW}.

IGDZCC

ILRXYX

- -HCR\_EL2.{VM, RW}.
- -TCR\_EL1.{TG1, EPD1, T1SZ, TG0, EPD0, T0SZ, AS, A1}.
- -If the Effective value of HCR\_EL2.E2H is 0, then TCR\_EL2.{TG0, T0SZ}.
- -If the Effective value of HCR\_EL2.E2H is 1, then TCR\_EL2.{TG1, EPD1, T1SZ, TG0, EPD0, T0SZ, AS, A1}.
- -TCR\_EL3.{TG0, T0SZ}.
- -VTCR\_EL2.{SL0, T0SZ}.
- -TTBR0\_EL1.ASID.
- -TTBR1\_EL1.ASID.
- -If the Effective value of HCR\_EL2.E2H is 1, then all of the following:
- -TTBR0\_EL2.ASID.
- -TTBR1\_EL2.ASID.
- In AArch32 state, all of the following:
- -SCTLR.M.
- -HCR.VM.
- -TTBCR.{EAE, PD1, PD0, N, EPD1, T1SZ, EPD0, T0SZ, A1}.
- -HTCR.T0SZ.
- -VTCR.{SL0, T0SZ}.
- -TTBR0.ASID.
- -TTBR1.ASID.
- -CONTEXTIDR.ASID.

RFZTHY Address-based TLB maintenance instructions are applied to the extent of the &lt;shareability&gt; specified by the instruction regardless of the Shareability assigned by any translation of the IA or Shareability attribute stored in TLB entries.

RMLYGB For TLB maintenance instructions that operate only on instruction TLBs or only on data TLBs, Arm deprecates their use in AArch32 state.

RLQLSD When a TLB maintenance instruction is executed, all of the following apply:

- The minimum size of a TLB entry that is required to be invalidated from the TLB is at least the size specified by the corresponding translation table entry.
- The Contiguous bit does not affect the minimum size of a TLB entry that is required to be invalidated from the TLB.
- IJQPNP When invalidating a mapping greater than a translation granule size or block size, for example a mapping that is specified using the Contiguous bit, software is required to issue a TLB maintenance instruction for each block or granule within the configured contiguous region size to invalidate the entire mapping.

RMMZTY An implementation is permitted to invalidate more than the minimum required TLB entries.

IZWTPG Arm recommends not invalidating entries that are not required to be invalidated to minimize the performance impact.

- IRTRQB Arm expects software to mostly use address-based TLB invalidation instructions that apply to entries cached from the last level of a stage 1 or a stage 2 translation table walk to avoid unnecessary loss of the cached intermediate translation table entries.
- RTLJCY For all of the following reasons, software is required to set VTTBR\_EL2.VMID[7:0] to a known value as part of the PE initialization sequence:
- The VTTBR\_EL2.VMID field resets to a value that is architecturally UNKNOWN.
- If EL2 is enabled, then dependencies on the VMID in the EL1&amp;0 translation regime apply whether stage 2 translation is enabled or disabled.

## D8.17.6.1 Invalidating TLB entries from stage 2 translations

The following code is required to invalidate all cached copies of the stage 2 translation of the IPA held in Xt using the current VMID, with the corresponding requirement applied to the broadcast versions of the instructions:

ICKZGP

IQKHVL

IXPBXT

IRGYNM

```
TLBI IPAS2E1, Xt DSB TLBI VMALLE1
```

The following code is required to invalidate all cached copies of the stage 2 translations of the IPA held in Xt used to translate the V A, and the specified ASID when executing TLBI VAE1 , held in Xt2 , with the corresponding requirement applied to the broadcast versions of the instructions:

```
TLBI IPAS2E1, Xt DSB TLBI VAE1, Xt2 ; or TLBI VAAE1, Xt2
```

The following code is required to invalidate all cached copies of the stage 2 translations of the IPA held in Xt used to translate the IPA produced by the last level of stage 1 translation table lookup for the V A, and the specified ASID when executing TLBI VALE1 , held in Xt2 , with the corresponding requirement applied to the broadcast versions of the instructions:

```
TLBI IPAS2E1, Xt DSB
```

TLBI VALE1, Xt2 ; or TLBI VAALE1, Xt2

For an EL1&amp;0 translation regime with stage 2 translation enabled, software is required to use the entire invalidation sequences, even if stage 1 translation is disabled.

Equivalent architectural requirements apply to the IPAS2L instruction, except that the only TLB entries required to be invalidated by an IPAS2L instruction are those that come from the final translation table lookup level.

## D8.17.7 Broadcast TLB maintenance

RTHTWM

If all of the following apply, then a TLB maintenance instruction executed by a PE in an Exception level that is using AArch64 can affect a PE that executes the same Exception level using AArch32:

- The PE lies within the target Shareability domain of the TLB maintenance instruction.
- If V A matching is required, then the V A is 0x0000\_FFFF\_FFFF or lower in the memory map.
- If ASID matching is required, then one of the following:
- -If the PE using AArch64 is using an 8-bit ASID, then the ASIDs match.
- -If the PE using AArch64 is using a 16-bit ASID and the top 8 bits of the 16-bit ASID are zero, then the ASIDs match.
- If VMID matching is required, then one of the following:
- -If the PE using AArch64 is using an 8-bit VMID, then the VMIDs match.
- -If the PE using AArch64 is using a 16-bit VMID and the top 8 bits of the 16-bit VMID are zero, then the VMIDs match.
- RVYLVH If all of the following apply, then a TLB maintenance instruction executed by a PE in an Exception level that is using AArch32 can affect a PE that executes the same Exception level using AArch64:
- The PE lies within the same Inner Shareable Shareability domain of the TLB maintenance instruction.
- If V A matching is required, then when the supplied V A is zero-extended, the V As match.
- If IPA matching is required, then when the supplied IPA is zero-extended, the IPAs match.
- If ASID matching is required, then one of the following:
- -If the PE using AArch64 is using an 8-bit ASID, then the ASIDs match.
- -If the PE using AArch64 is using a 16-bit ASID, then when the supplied ASID is zero-extended, then the ASIDs match.
- If VMID matching is required, then one of the following:
- -If the PE using AArch64 is using an 8-bit VMID, then the VMIDs match.
- -If the PE using AArch64 is using a 16-bit VMID, then when the supplied VMID is zero-extended, the VMIDs match.

RWMNBC If a PE with EL3 using AArch32 issues a broadcast AArch32 TLB maintenance instruction affecting entries in Secure state, then the instruction is not required to affect one or more of the following in the Inner Shareable domain:

- The EL3 translation regime of the PEs with EL3 using AArch64.
- If EL2 is disabled, then the EL1&amp;0 translation regime of the PEs with EL3 using AArch64, regardless of whether the EL1&amp;0 translation regime is using AArch64 or AArch32.
- RSLJFD If a PE with EL3 using AArch64 issues a broadcast AArch64 TLB maintenance instruction affecting EL3 entries, then the instruction is not required to affect the EL3 translation regime of the PEs with EL3 using AArch32 in the Inner Shareable domain.
- RGKQML If a PE with EL3 using AArch64 issues a broadcast AArch64 TLB maintenance instruction affecting Secure EL1 entries, then the instruction is not required to affect the EL3 translation regime of the PEs with EL3 using AArch32 in the Inner Shareable domain.
- RXMZFH In all of the following cases, a broadcast TLB maintenance instruction is not required to perform any invalidation on the recipient PE within the target Shareability domain:
- ATLBmaintenance instruction specifying a VA and affecting one of the following translation regimes is broadcast from a PE using one translation granule size for that translation regime to a PE using a different translation granule size for that V A in the same translation regime:
- -The EL2 translation regime.
- -The EL2&amp;0 translation regime.
- -The EL3 translation regime.
- ATLBmaintenance instruction specifying a VA and affecting the EL1&amp;0 translation regime is broadcast from a PE using a stage 1 translation granule size for that translation regime to a PE using EL1 and a different stage 1 translation granule size for that V A.
- If EL2 is enabled, then a TLB maintenance instruction specifying a V A and affecting the EL1&amp;0 translation regime is broadcast from a PE using a stage 2 translation granule size to a PE using a different stage 2 translation granule size.
- If EL2 is enabled, then a TLB maintenance instruction specifying an IPA and affecting the EL1&amp;0 translation regime is broadcast from a PE using a stage 2 translation granule size to a PE using a different stage 2 translation granule size.
- ATLBmaintenance instruction specifying a range of VAs or IPAs is broadcast from one PE to a PE that does not support the TLB range-based operations.
- RYNPVV The set of Requesters containing TLBs that support TLB range-based operations is defined by the system architecture.
- IWHFDZ Arm strongly recommends that within an Inner Shareable domain, all PEs support the same set of broadcast TLB range maintenance instructions.
- RTVMHK If an Armv7 PE is in the same Inner Shareable domain as an Armv8 PE, and the Armv8 PE issues a broadcast TLB maintenance instruction that is not defined in Armv7, then that instruction is not required to affect the TLBs of the Armv7 PE.
- IFSWKY All of the following TLB maintenance instructions are added to the Armv8 T32 and A32 instruction sets, and do not exist in Armv7:
- For stage 1 translations, all of the following instructions that operate on TLB entries for the final level of translation table walk:
- -TLBIMVALIS.
- -TLBIMVAALIS.
- -TLBIMVALHIS.
- -TLBIMVAL.
- -TLBIMVAAL.
- -TLBIMVALH.
- For stage 2 translations, all of the following instructions that operate by IPA on TLB entries:
- -TLBIIPAS2IS.
- -TLBIIPAS2LIS.
- -TLBIIPAS2.
- -TLBIIPAS2L.

## D8.17.8 Ordering and completion of TLB maintenance instructions

| R TGVWD         | For all of the following instructions, the effects of a TLB maintenance instruction can be observed in any order relative that instruction unless a DSB is executed between the instructions:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R QRNJC         | ATLBmaintenance instruction executed by a PE causes a TLB maintenance operation to occur on each PE within the Shareability domain specified by the instruction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| I NVLMG I SFCHD | If a TLB maintenance instruction has the nXS qualifier, then the associated TLB maintenance operations have the nXS qualifier. If a TLB maintenance instruction does not have the nXS qualifier and the Effective value of HCRX_EL2.FnXS is 1, then all of the following apply: • When the instruction is not executed at EL1, the associated TLB maintenance operations do not have the nXS qualifier. • When the instruction is executed at EL1, the associated TLB maintenance operations have the nXS qualifier. If a translation regime uses two translation stages, then the XS attribute used to determine the behavior of a TLB maintenance instruction with the nXS qualifier is the attribute determined after both translation stages have been When a TLB maintenance instruction is executed, in-scope old translation information is any translation information related to addresses within the scope of that instruction that is not consistent with one or more of the following: • The architectural translation information held in the translation tables. • Any architecture translation information that is Coherence-after the information held in the translation tables. In-scope old translation information might be held in TLBs or other non-coherent caching structures. For a PE that handles a TLB maintenance operation without the nXS qualifier, the TLB maintenance operation is |
| I BBMSB         | applied. finished when all of the following apply: • All memory accesses generated by that PE using in-scope old translation information are complete. • All memory accesses, RWx, generated by that PE are complete, where RWxis the set of all memory accesses generated by instructions for that PE that appear in program order before an instruction I1 executed by that PE, where all of the following apply: - I1 uses the in-scope old translation information. - The use of the in-scope old translation information generates a synchronous Data Abort. - If I1 did not generate an abort from use of the in-scope old translation information, I1 would generate a memory access that RWxwould be locally-ordered-before. For a PE that handles a TLB maintenance operation with the nXS qualifier, the TLB maintenance operation is finished                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| R WWQZZ         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| I YMDMJ         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| R STPSQ         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| R TSJSN         | when all of the following apply: • All memory accesses with the XS attribute set to 0 generated by that PE using in-scope old translation information are complete. • All memory accesses, RWx, generated by that PE are complete, where RWxis the set of all memory accesses generated by instructions for that PE that appear in program order before an instruction I1 executed by that PE, where all of the following apply: - I1 uses the in-scope old translation information. - The use of the in-scope old translation information generates a synchronous Data Abort. - If I1 did not generate an abort from use of the in-scope old translation information, I1 would generate a memory access with the XS attribute set to 0 that RWxwould be locally-ordered-before.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                 | For best real-time performance, Arm recommends that the completion of a TLB maintenance instruction with the nXS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| I KFTWB         | qualifier executed by a PE should not depend on the completion of any memory accesses with the XS attribute set to 1 generated by a second PE.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| TFQRW           | To guarantee completion of memory accesses with the XS attribute set to 1, software must use a TLBI maintenance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                 | instruction without the nXS qualifier, and a DSB without the nXS qualifier.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| I               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

| R DCJQM   | When the TLB maintenance operations specified by a TLB maintenance instruction are finished for all PEs, the TLB maintenance instruction is complete.                                                                                                                                                                                                                                                                      |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R LXHLD   | If a TLB maintenance instruction is complete, then no new memory accesses using the in-scope old translation information are architecturally performed by any observer that is affected by the TLB maintenance instruction.                                                                                                                                                                                                |
| I CPZSM   | If it is impossible for software running on any observer to determine that the memory accesses have been performed, then speculative memory accesses can be performed using in-scope old translation information.                                                                                                                                                                                                          |
| R PSMWS   | When a DSB instruction is used to ensure the completion of TLB maintenance instructions, all of the following apply: • The DSB is required to apply to both loads and stores. • ADSB NSH is sufficient to ensure completion of TLB maintenance instructions that apply to a single PE. • ADSB ISH is sufficient to ensure completion of TLB maintenance instructions that apply to PEs in the same Inner Shareable domain. |
| R YNJCP   | When a PE, PEx, executes a TLB maintenance instruction, the instruction can complete at any time after it is issued, but the instruction is only guaranteed to be finished for a PE other than PEx after the execution of DSB by the PEx.                                                                                                                                                                                  |
| R BLDZX   | For the TLB of a PE that issues a TLB maintenance instruction, one of the following determines when the instruction is guaranteed to be complete:                                                                                                                                                                                                                                                                          |
|           | by that PE, followed by a Context synchronization event. • If FEAT_ETS2 is implemented, all of the following determine when the instruction is guaranteed to be complete: - If the instruction applies only to translations without execute permission and where translation information that is coherence-after also do not have execute permission, then the instruction is guaranteed                                   |
| I MGRRK   | For more information, see Ordering requirements defined by the formal concurrency model.                                                                                                                                                                                                                                                                                                                                   |