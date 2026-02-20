## D8.16 Translation Lookaside Buffers

| I ZVNKM   | The Arm architecture does not specify any structure of Translation Lookaside Buffers (TLBs), and permits any structure that complies with the requirements described in this section.                                                                                                                                                     |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R XCLRD   | Translation table entries that generate a Translation fault, an Address size fault, or an Access flag fault are never cached in a TLB.                                                                                                                                                                                                    |
| R SQBCS   | When address translation is enabled, a translation table entry for an in-context translation regime that does not cause a Translation fault, an Address size fault, or an Access flag fault is permitted to be cached in a TLB or intermediate TLB caching structure as the result of an explicit or speculative access.                  |
| R ZVMQM   | Atranslation table entry is not permitted to be cached in a TLB or intermediate caching structure if a synchronous external abort on the translation table walk prevents the PE from determining if the translation table entry would otherwise cause a Translation fault, an Address size fault, or an Access flag fault.                |
| I RCGCH   | When address translation is enabled, if a translation table entry meets all of the following requirements, then that translation table entry is permitted to be cached in a TLB or intermediate TLB caching structure at any time:                                                                                                        |
| I LBGNR   | The Arm architecture permits TLBs to cache certain information from System control registers, including when any or all translation stages are disabled. The individual register descriptions specify System control register fields are permitted to be cached in a TLB. For more information, see AArch64 System Register Descriptions. |
| R JBNTF   | For any System register field that is described as being permitted to be cached in a TLB, if that field takes an Effective value as a result of a System register control field at a higher Exception level, then the Effective value is also permitted to be cached in a TLB.                                                            |
| R FXGNQ   | The TLB entries in all of the following translation regimes are out-of-context: • When executing at EL3 or EL2, the TLB entries associated with the EL1&0 translation regime are out-of-context. • When executing at EL3, the TLB entries associated with the EL2 or EL2&0 translation regime are out-of-context.                         |
| I RLTGW   | The VMSAprovides TLB maintenance instructions for the management of TLB contents.                                                                                                                                                                                                                                                         |
| R NDCMB   | When a translation stage is disabled and then re-enabled, TLB entries are not corrupted.                                                                                                                                                                                                                                                  |

## D8.16.1 TLB behavior at reset

IGWZWM

When a reset occurs, an implementation is not required to automatically invalidate a TLB.

RBQCDZ

- IHXRSY

RQNFHZ

When a reset occurs, a TLB is affected in all of the following ways:

- All TLBs reset to an IMPLEMENTATION DEFINED state that might be UNKNOWN.
- It is IMPLEMENTATION DEFINED whether a specific TLB invalidation routine is required to invalidate a TLB before translation is enabled after a reset.

For the ELx reset is taken to, when a reset occurs, SCTLR\_ELx.M is reset to 0. For the translation regime controlled by that SCTLR\_ELx.M bit, when SCTLR\_ELx.M is 0, TLB contents have no effect on address translation.

If an implementation requires a specific TLB invalidation routine, then all of the following apply:

- The routine is IMPLEMENTATION DEFINED.
- The implementation documentation is required to clearly document the routine.
- Arm recommends that the routine is based on the TLB maintenance instructions.

IWVKXW

On a Cold reset or Warm reset, an implementation might require TLBs to maintain their contents from before the reset, including one or more of the following reasons:

- Power management.
- Debug requirements.

IWZHDM

For more information on the TLB maintenance instructions used in a TLB invalidation routine, see TLB maintenance instructions.

## D8.16.2 TLB lockdown

RSSQZC

TLB lockdown support is IMPLEMENTATION DEFINED.

RXXDPS

If an implementation supports TLB lockdown, then all of the following apply:

- The lockdown mechanism is IMPLEMENTATION DEFINED.
- The implementation documentation is required to clearly document the interaction of the TLB lockdown mechanism with the architecture.
- Alocked TLB entry is guaranteed to remain in the TLB, unless the locked TLB entry is affected by a TLB maintenance operation.
- An unlocked TLB entry is not guaranteed to remain in the TLB.
- If a translation table entry is modified, then it is not guaranteed that a locked TLB entry remains coherent with the modified translation table entry.

IDXXYV If a translation table entry is modified, then it is not guaranteed that a locked TLB entry remains incoherent with the modified translation table entry because the lockdown mechanism might permit a TLB maintenance instruction to trigger an update of the locked TLB entry.

For more information, see The interaction of TLB lockdown with TLB maintenance instructions.

RDSQQW The implementation is permitted to use the reserved IMPLEMENTATION DEFINED register encodings to implement TLB lockdown functions.

ILSKYV

RDSLVY

TLB lockdown functions might include, but are not limited to, all of the following:

- Unlock all locked TLB entries.
- Prefetch a translation table entry into a specific TLB level.

If an implementation supports TLB lockdown and EL2 is enabled, then when executing at EL1 or EL0, an exception due to TLB lockdown can be routed to one of the following:

- EL1, as a Data Abort exception.
- EL2, as a Hyp Trap exception.

## D8.16.3 Use of ASIDs and VMIDs to reduce TLB maintenance requirements

ILHWHR TLB maintenance can be reduced during context switches by associating the translation table lookups from some translation regimes with an address space identifier (ASID), virtual machine identifier (VMID), or both.

RDHRKH

The rules in this section apply only to translation regimes that support two privilege levels, and apply for each of the implemented Non-secure, Secure, and Realm Security states.

RWPFJJ

The rules in this section use the following definitions of controlling ELx :

- EL1 is the controlling ELx of stage 1 translations in the EL1&amp;0 translation regime.

- EL2 is the controlling ELx of stage 1 translations in the EL2&amp;0 translation regime.

## D8.16.3.1 Global and process-specific translation table entries

| I FRDGD   | For translation regimes that use an ASID, it is possible to mark translations as global or non-global.                                                                                                                                                                                                                                                                                           |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R XXNPZ   | ATLBentry associated with a specific ASID value, or a specific ASID and a VMIDvalue, can only be used to translate a VAin a context that is associated with the same ASID value, or ASID and VMIDvalue.                                                                                                                                                                                          |
| R WTVTJ   | For stage 1 of a translation regime that supports two privilege levels, non-global TLB entries are associated with a specific ASID.                                                                                                                                                                                                                                                              |
| I LCNWN   | For stage 1 of a translation regime that can support two privilege levels, Arm expects that software configures translations specific to a process to be associated with a specific ASID.                                                                                                                                                                                                        |
| R SHVGC   | For all of the following, the translation does not support association of a translation with an ASID, and all translations are treated as global: • Astage 1 translation that supports a single privilege level                                                                                                                                                                                  |
| I HGKKC   | The ASID permits software to switch between process-specific translation table mappings without removing previous mappings cached for another ASID from a TLB.                                                                                                                                                                                                                                   |
| I LQMXG   | For stage 1 of a translation regime that can support two privilege levels, each TTBR0_ELx and TTBR1_ELx has an ASID field.                                                                                                                                                                                                                                                                       |
| R SCBSR   | All the following values of TCR_ELx.A1 determine the ASID value that is used by the translations of both the lower VA range and upper VA range:                                                                                                                                                                                                                                                  |
| R PYWKY   | For stage 1 of a translation regime that supports two privilege levels, TCR2_ELx.A2 determines all of the following: • If the value is 0, then the one ASID selected by TCR_ELx.A1 is used. • If the value is 1, then two ASIDs are used.                                                                                                                                                        |
| R XPSGZ   | For a controlling ELx, if two concurrent ASIDs are used, then TCR_ELx.A1 does not select which ASID field is used for the purpose of caching translations in a TLB, and instead all of the following apply: • Any non-global translation of an address in the TTBR0_ELxVA range is associated with TTBR0_ELx.ASID.                                                                               |
| I NWLMM   | The scope of TLBI operations is not affected by the Effective value of TCR2_ELx.A2. This means that a TLBI ASIDE1* operation removes TLB entries associated with the specified ASID, regardless of which half of the VA range those entries would be used to translate, and would not be required to remove any other TLB entries.                                                               |
| I WBQGD   | For execution at EL0, if FEAT_CSV2 is implemented, and either the EL1&0 or EL2&0 translation regime is used, the architecture defines a hardware-defined context as including an ASID. However, for execution at EL1 or at EL2 when using these translation regimes, the hardware-defined context does not include an ASID. For more information see Restrictions on the effects of speculation. |
| R SCLCL   | For a controlling ELx, if two concurrent ASIDs are used, then for the purposes of FEAT_CSV2, the ASID used in the hardware-defined context when executing at EL0 is one of the following:                                                                                                                                                                                                        |
| R QGKGF   | The nG bit in a Block descriptor and Page descriptor indicates one of the following: • If the value is 0, the translation is global and the TLB entry applies to all ASID values.                                                                                                                                                                                                                |
| R CHVGJ   | For a translation regime that supports global and non-global translations, translation table entries from lookup levels other than the final lookup level are treated as non-global, regardless of the value of the nG bit in the final lookup level.                                                                                                                                            |

| R JYHZR   | For a translation in Secure state, if the NSTable bit in a Table descriptor is 1 at any level of the translation table walk, then the resulting translation is treated as non-global, regardless of the nG bit value in the Block descriptor or Page descriptor for the translation.                                                                                                                                                                                                                                                   |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R KDVGW   | If TCR2_ELx.FNGy is 1, where y is {0, 1}, then all of the following apply: • For translations in the TTBRy_ELx VA range, the Block and Page descriptor nG field is IGNORED. • Address translations in the TTBRy_ELx VA range are cached in a TLB as non-global entries, regardless of the value of the Block or Page descriptor nG field.                                                                                                                                                                                              |
| I QVBDY   | The effects of TCR2_ELx.FNGy apply regardless of the value of TCR2_ELx.A2.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| R QNPQX   | If EL2 is enabled, then for the EL1&0 translation regime, TLB entries created for the regime are associated with the current VMID.                                                                                                                                                                                                                                                                                                                                                                                                     |
| I YWBQX   | If EL2 is enabled, then for the EL1&0 translation regime, TLB entries are associated with the current VMIDin all cases, and include all of the following: • For both global and non-global translations of any ASID value, and regardless of whether stage 2 translation is disabled, TLB entries containing information from stage 1 translation. • For both stage 1 translation table walks and stage 1 OA, and regardless of whether stage 1 translation is disabled, TLB entries containing information from stage 2 translations. |
| I CNTNV   | For the EL1&0 translation regime, if EL2 is enabled, then TLB entries are associated with a VMIDregardless of whether stage 2 translation is enabled.                                                                                                                                                                                                                                                                                                                                                                                  |
| I SLWFB   | If EL2 is enabled, then for the EL1&0 translation regime, TLB entries associated with a VMIDare associated with a specific virtual machine.                                                                                                                                                                                                                                                                                                                                                                                            |
| I HQXLL   | The VMIDpermits software to switch between virtual machines that have different VMIDs without removing previous translation table mappings from a TLB.                                                                                                                                                                                                                                                                                                                                                                                 |
| I RWYWK   | VTTBR_EL2.VMID holds the current VMID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|           | D8.16.3.2 ASID size                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| R KHXQX   | The ASID size is an IMPLEMENTATION DEFINED choice of 8 bits or 16 bits.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| I NHTBK   | The maximum supported ASID size is indicated by ID_AA64MMFR0_EL1.ASIDBits.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| I BZXYN   | For an implementation that supports 16-bit ASIDs, all of the following values of TCR_ELx.AS specify whether TTBRn_ELx.ASID[15:8] are used: • If TCR_ELx.AS is 0, then TTBRn_ELx.ASID[15:8] are not used and are treated in all of the following ways: - For every purpose other than direct reads of TTBR0_ELx.ASID and TTBR1_ELx.ASID, the bits are ignored by hardware. - When used for allocating and matching entries in a TLB, the bits are treated as if they are all zeros.                                                     |
| I ZRWYC   | Bits[15:8] of the ASID field in TLBI{P} instructions are considered by hardware regardless of the value of TCR_ELx.AS.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| R NKTBP   | For a translation using VMSAv8-32, if the implementation supports 16-bit ASIDs, then the 8-bit ASID used is zero-extended to 16 bits.                                                                                                                                                                                                                                                                                                                                                                                                  |
| I DJKMH   | The AArch32 ASID size is 8 bits.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## D8.16.3.3 VMID size

| R RPSHN   | The VMIDsize is an IMPLEMENTATION DEFINED choice of 8 bits or 16 bits.                                                                                                                                                                                                                                          |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I VLKQX   | The maximum supported VMIDsize is specified by ID_AA64MMFR1_EL1.VMIDBits.                                                                                                                                                                                                                                       |
| I ZDPJB   | If and only if EL2 is using AArch64, then use of a 16-bit VMIDis permitted.                                                                                                                                                                                                                                     |
| I MDGYK   | For an implementation that supports a 16-bit VMID, all of the following values of VTCR_EL2.VS specify whether VTTBR_EL2.VMID[15:8] are used:                                                                                                                                                                    |
|           | • If VTCR_EL2.VS is 0, then VTTBR_EL2.VMID[15:8] are not used and are treated in all of the following - For every purpose other than direct reads of VTTBR_EL2.VMID, the bits are ignored by hardware. - When used for allocating and matching entries in a TLB, the bits are treated as if they are all zeros. |

## D8.16.3.4 Common not private translations

- IXJYLH FEAT\_TTCNP allows multiple PEs in the same Inner Shareable domain and operating in the same translation regime to use the same translation table entries in a given translation stage.
- RFWQJZ If all of the following conditions are met, translation table entries pointed to by TTBR\_ELx are shared with all other PEs in the Inner Shareable domain, and are referred to as common not private translation tables:
- For the PEs that share the translation tables, the Effective value of the corresponding TTBR\_ELx.CnP is 1.
- For the PEs that share the translation tables, the same translation regime in the same Security state applies to the corresponding TTBR\_ELx.
- If an ASID applies to the corresponding translation stage, then all of the PEs that share non-global translation table entries are required to have the same current ASID.
- If a VMID applies to the corresponding translation stage, then all of the PEs that share translation table entries are required to have the same current VMID.
- RLGDJT For a common not private translation table, if a System register field with all of the following characteristics is set by a particular PE to a value that is different than the value set by the other PEs, then it is CONSTRAINED UNPREDICTABLE whether the System register field is interpreted using the value of the particular PE or the value of one of the other PEs that are sharing the translation table entry:
- The register field applies to the translation stage.
- The register field is permitted to be cached in a TLB.
- RZVRZW For a translation regime with both stage 1 and stage 2 translations, a TLB entry can be shared between different PEs in one or more of the following cases only if the value of the TTBR\_ELx.CnP bit is 1 for both stages of translation:
- The TLB entry holds information from stage 1 translation only.
- The TLB entry combines information from stage 1 and stage 2 translations.
- IYVLVD The TTBR\_ELx.CnP bit is permitted to be cached in a TLB.
- RQLGWZ For a common not private translation table, if a TTBR\_ELx does not point to the same translation table as the other TTBR\_ELx registers, then the system is misconfigured and an address translation using that TTBR\_ELx causes one of the following to occur:
- Multiple hits in a TLB, which is permitted to generate a TLB conflict abort.
- ACONSTRAINED UNPREDICTABLE result due to caching of control or data values.

For more information, see TLB conflict abort and CONSTRAINED UNPREDICTABLE behaviors due to caching of control or data values.