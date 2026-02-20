## D8.2 Translation process

IGDSWV

The translation of a V A to a PA begins with reading the translation table base address register, followed by a walk through the translation tables to read the descriptors associated with the mapping.

## D8.2.1 Translation table walk

RBTTHB

Atranslation table walk is the set of translation table lookups that are required to do all of the following:

- For a single stage translation at stage 1, translate a V A to a PA.
- For two translation stages and stage 1 is disabled, translate an IPA to a PA.
- For a two stage translation, all of the following:
- -For a stage 1 translation, translate a V A to an IPA.
- -For a stage 2 translation, translate an IPA to a PA for each of the stage 1 translation table lookups.
- -For a stage 2 translation, translate an IPA to a PA for the stage 1 OA.

RRHQPX When a translation table walk begins, the initial translation table lookup uses the translation table base address stored in the TTBR\_ELx register to locate the translation table.

RYKQTS When a translation table lookup occurs, the descriptor held in the translation table entry is read as one of the following:

- For the VMSAv8-64 translation system, an 8-byte single-copy atomic access.
- For the VMSAv9-128 translation system, a 16-byte single-copy atomic access.

For information on the translation table alignment requirements, see Translation table alignment.

The descriptor type indicates one of the following:

- The translation table walk is complete and the translation table entry is the final entry.
- The translation table walk requires an extra lookup at the next higher lookup level.
- The descriptor is invalid.

All of the following descriptor types conclude the translation process:

- Page descriptor.
- Block descriptor.
- Invalid descriptor.

For more information, see Translation table descriptor formats.

When an Invalid descriptor is returned during the translation process, a Translation fault at the current lookup level is generated.

When an extra lookup level is required, the descriptor contains all of the following information:

- The translation table base address of the next lookup level.
- For stage 1 descriptors, if the Effective value of TCR\_ELx.HPD n is 0, then the descriptor has hierarchical access permissions that are applied to the final translation.
- If the translation is made in a Secure translation regime, then a stage 1 descriptor indicates whether the base address is in the Secure address space or the Non-secure address space, unless a hierarchical control at a previous lookup level has indicated that it is required to be in the Non-secure address space.

For more information, see Security state of translation table lookups.

For a translation lookup level, the translation table base address is one of the following:

- For the initial lookup level, the aligned value of the appropriate TTBR\_ELx.BADDR field.
- For subsequent lookup levels, the next-level translation table base address returned by the previous lookup level.

For the VMSAv9-128 translation system, the Skip level (SKL) field in the descriptors and translation table base address registers permit the translation table walk to skip subsequent lookup levels.

When the last lookup level of a translation stage returns a valid descriptor, it contains all of the following:

- The OA from the translation stage.

RYPWQG

RNMTJN

IWMLYG

IQPHCD

RVSJGV

IHFBGP

IZMMXH

IVPFHD

- The memory region access permissions.
- The memory region attributes.

For more information, see Memory region attributes and Memory access control.

RRZHGL

For a translation regime that uses two translation stages, the stage 1 descriptor addresses require stage 2 translation from IPA to PA.

RNLLYJ

When a translation table walk succeeds, all of the following are returned:

- The OA.
- If the translation table walk is made in a Secure translation regime, then the information returned indicates whether the OA is in the Secure IPA or PA space, or the Non-secure IPA or PA space.
- If the translation table walk is made in a Realm translation regime, then the information returned indicates whether the OA is in the Realm PA space, or the Non-secure PA space.
- If the translation table walk is made in Root state, then the OA can be in the Root, Realm, Secure, or Non-secure PA spaces.
- The output memory region attributes.
- The output memory region access permissions.

For more information, see Security state of translation table lookups.

The following figure is a generalized view of a single address translation stage with three lookup levels.

Figure D8-1 Generalized view of a single address translation stage

<!-- image -->

If all of the following are true, then a translation table entry is permitted to be cached in a Translation Lookaside Buffer (TLB):

- The entry is valid.
- Using the entry does not generate a Translation fault, an Address size fault, or an Access flag fault.

TLB caching can reduce the number of required translation table lookups.

If two address translation stages are used and when a full translation table walk at both stages is required, then all of the following apply:

- S1 is the number of lookup levels required for a stage 1 translation.
- S2 is the number of lookup levels required for a stage 2 translation.
- The maximum number of translation table lookups required is (S1+1)*(S2+1)-1.

IJWQFM

IZTRGT

IJQDTN

## D8.2.2 Concatenated translation tables

| R MCGQP   | All statements in this section apply only to the VMSAv8-64 translation system.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I TDMHR   | For the initial lookup of a stage 2 address translation, up to 16 translation tables can be concatenated.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| R HRSBS   | For a stage 2 translation, if the translation table in the initial lookup level would require 16 or fewer entries, then the stage 2 translation can be configured to have all of the following properties: • The initial lookup of the stage 2 translation starts at the next lookup level. • Anumber of translation tables corresponding to the original number of translation table entries at the previously initial lookup level are concatenated at that next lookup level.                                                |
| R DXBSH   | For the 16KB translation granule, if the Effective value of VTCR_EL2.DS is 0 and a 48-bit address size is translated by the stage 2 translation, then the initial lookup is required to start at level 1 with two concatenated translation tables.                                                                                                                                                                                                                                                                              |
| R JKZFY   | For the initial lookup in a stage 2 translation, if concatenated translation tables are used, then all of the following apply: • Up to four additional IA bits are resolved by the initial lookup. • For each additional n IA bits resolved by the initial lookup, the number of least significant translation table base address bits held in the TTBR_ELx is reduced by n bits. • For each additional n IA bits resolved by the initial lookup, 2 n concatenated translation tables are required at the initial lookup level. |
| I DRXGV   | Using a concatenated translation table eliminates the overhead of an extra lookup level.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| I YXFPJ   | If concatenated translation tables are used, then software is required to do all of the following: • Align the base address of the first translation table to the sum of the size of the memory occupied by the concatenated translation tables. • Program VTTBR_EL2 or VSTTBR_EL2 with the address of the first translation table in the set of concatenated translation tables.                                                                                                                                               |

## D8.2.3 Translation table base address register

| I TLWRN   | For a translation stage, the translation table base address register, TTBR_ELx, holds the translation table base address of the initial lookup.                                                                                                                                                                                                            |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R DXLKR   | For a translation stage that supports two VA ranges, two translation table base address registers are required.                                                                                                                                                                                                                                            |
| I HPFDM   | Software can use TCR_ELx.TnSZ to configure the translation stage IA size to be smaller than the supported size.                                                                                                                                                                                                                                            |
| R QKFFR   | If EL2 is disabled or not implemented, then for the stage 1 EL1&0 regime, all of the following apply: • The translation table base address held in the TTBR_ELx register is a PA. • The translation table base address returned by a Table descriptor is a PA.                                                                                             |
| R QSWHS   | If EL2 is enabled, then for all address translation stages other than stage 1 in EL1&0, all of the following apply: • The translation table base address held in the TTBR_ELx register is a PA. • The translation table base address returned by a Table descriptor is a PA.                                                                               |
| R PNHHK   | If EL2 is enabled, then for stage 1 address translations in EL1&0, all of the following apply: • The stage 1 translation table base address held in the TTBR_ELx register is an IPA. • The stage 1 translation table base address returned by a Table descriptor is an IPA. • Accesses to stage 1 translation tables are subject to a stage 2 translation. |
| R GYQHZ   | For an address translation stage, the translation table base address in TTBR_ELx is defined for the supported OAsize of that stage.                                                                                                                                                                                                                        |

ISXSYL

For the VMSAv8-64 translation system, the number of {I}PA bits held in TTBR\_ELx is determined by the granule size and OA address size. The bits used for each granule size when using the maximum OA address size of 48 bits or 52 bits are shown in the following table. Software might be required to set one or more of the low-order base address bits to zero to align the table to the table size.

Table D8-10 {I}PA bits held in TTBR\_ELx

| Granule size       | Maximum OA size    | Translation table base address   | {I}PA bits held in TTBR_ELx   |
|--------------------|--------------------|----------------------------------|-------------------------------|
| 4KB, 16KB, or 64KB | 52 bits            | TTBR_ELx[5:2]                    | {I}PA[51:48]                  |
| 4KB                | 48 bits or 52 bits | TTBR_ELx[47:12]                  | {I}PA[47:12]                  |
| 16KB               | 48 bits or 52 bits | TTBR_ELx[47:14]                  | {I}PA[47:14]                  |
| 64KB               | 48 bits or 52 bits | TTBR_ELx[47:16]                  | {I}PA[47:16]                  |

IQTPMQ

If an address translation stage uses an OA size smaller than the maximum, then the upper bits of the translation table base address in TTBR\_ELx corresponding to the upper bits of OA size are required to be set by software to zero.

ILXTNH

RVPBBF

RDYDPX

IRBMTM

IQBVNF

IGRBLY

If TCR\_ELx.T n SZ specifies an IA size that is smaller than the maximum size resolved at the initial lookup level, then more low-order TTBR\_ELx bits are used to hold the translation table base address.

If an address translation stage uses an OA size smaller than the maximum and if the bits above the configured OA size of the translation table base address in TTBR\_ELx are not set to zero, then an Address size fault is generated and reports all of the following:

- Atranslation level 0 lookup as generating the fault, regardless of whether or not the translation stage starts with a level 0 lookup.
- The translation stage that generated the fault.

Direct writes to TTBR0\_ELx and TTBR1\_ELx occur in program order relative to one another, without the need for explicit synchronization. For any one translation, all indirect reads of TTBR0\_ELx and TTBR1\_ELx that are made as part of the translation observe only one point in that order of direct writes.

Consistent with the general requirements for direct writes to System registers, direct writes to TTBR\_ELx are not required to be observed by indirect reads until completion of a Context synchronization event.

Example D8-1 Changing translation table base address and ASID value when TCR\_EL1.A1=0 The following is an example software sequence for changing translation table base address and ASID value when

TCR\_EL1.A1=0:

```
Change TTBR1 to point only at global entries Change TTBR0 (includes changing the ASID) Change TTBR1 to point at tables containing non-global
```

```
entries ISB
```

IBSFJP

<!-- image -->

For more information, see System registers relevant to MMU operation.

## D8.2.4 Selection between TTBR0\_ELx and TTBR1\_ELx when two VA ranges are supported

RHCTPT

RYYVYV

ITHCZK

IBCMMD

If a stage 1 translation regime supports two V A ranges, then the translation regime TTBR\_ELx registers point to all of the following address ranges:

- For the lower V A range that begins at address 0x0000\_0000\_0000\_0000 , TTBR0\_ELx points to the translation table for the initial lookup level.
- For the upper V A range that ends at address 0xFFFF\_FFFF\_FFFF\_FFFF , TTBR1\_ELx points to the translation table for the initial lookup level.

If a stage 1 translation regime supports two V A ranges, then the TCR\_ELx.{T0SZ, T1SZ} fields configure all of the following address range sizes:

- The lower VA range is 0x0000\_0000\_0000\_0000 to (2 (64-T0SZ) - 1).
- The upper VA range is (2 64 - 2 (64-T1SZ) ) to 0xFFFF\_FFFF\_FFFF\_FFFF .

If a stage 1 translation regime supports two V A ranges, when an accessed address is not in the lower V A range or the upper VA range, a stage 1 level 0 Translation fault is generated.

The following figure illustrates the two address ranges translated by the tables the TTBR\_ELx registers point to.

Figure D8-2 Example of a stage 1 translation that supports two VA ranges

<!-- image -->

If a stage 1 translation regime supports two V A ranges, then all of the following are used to select the TTBR\_ELx:

- If V A bit[55] is zero, then TTBR0\_ELx is selected.
- If V A bit[55] is one, then TTBR1\_ELx is selected.

| I ZFSYQ   | If a stage 1 translation regime supports two VA ranges and TCR_ELx.EPD n is one, then when a TLB miss occurs based on TTBRn_ELx, a level 0 Translation fault is generated, and no translation table walk is done.                                                                                                                                                                                                                                                                                            |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I SMKQB   | For the VMSAv9-128 translation system, if a stage 1 translation regime supports two VA ranges, then the maximum supported VAwidth is 55 bits, and the smallest permitted value of the T n SZ field is 9.                                                                                                                                                                                                                                                                                                     |
| I QBLKT   | For more information, see Address tagging.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|           | D8.2.4.1 Preventing EL0 access to halves of the address map                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| R BNDVG   | All statements in this section require implementation of FEAT_E0PD.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| I PZZHN   | The TCR_ELx.{E0PD0, E0PD1} fields can be used to prevent EL0 access to the addresses translated by the corresponding TTBR0_ELx or TTBR1_ELx.                                                                                                                                                                                                                                                                                                                                                                 |
| I RFRSQ   | When the TCR_ELx.{E0PD0, E0PD1} fields prevent EL0 access to an address translated by TTBR0_ELx or TTBR1_ELx, then a level 0 Translation fault is generated.                                                                                                                                                                                                                                                                                                                                                 |
| R DDFWH   | When the TCR_ELx.{E0PD0, E0PD1} fields generate a level 0 Translation fault, then all of the following apply: • The time needed to take the fault should be the same whether or not the address accessed is present in a TLB, to mitigate attacks that use fault timing. • The fault generated does not affect any micro-architectural state of the PE in a manner that is different if the address accessed is present in a TLB or not, to prevent this information being used to determine the presence of |
| R CZWGX   | When the TCR_ELx.{E0PD0, E0PD1} fields generate a level 0 Translation fault, the fault is not counted as a TLB miss for performance monitoring features.                                                                                                                                                                                                                                                                                                                                                     |

## D8.2.5 Translation table and translation table lookup properties

ISLRTY

RYDJDH

RWDRNX

RNVTHS

IZMLQD

Translation table and translation table lookup properties include the table size, table alignment, table endianness, and memory attributes.

## D8.2.5.1 Translation table size

The descriptor size in a translation table entry is one of the following:

- For the VMSAv8-64 translation system, an eight-byte, or 64-bit, object.
- For the VMSAv9-128 translation system, a 16-byte, or 128-bit, object.

If n is the number of bits resolved by a lookup level, then the number of translation table entries required at that lookup level is 2 n .

The size of a translation table in bytes is determined by multiplying the number of entries by the descriptor size.

The maximum number of translation table entries is determined by the translation granule size, which is defined by one of the following:

- For a stage 1 translation that supports one V A range, TCR\_ELx.TG0.
- For a stage 1 translation that can support two V A ranges, all of the following:
- -For the lower V A range, TCR\_ELx.TG0.
- -For the upper V A range, TCR\_ELx.TG1.
- For a stage 2 translation in the Non-secure EL1&amp;0 translation regime, VTCR\_EL2.TG0.
- For a stage 2 translation in the Secure EL1&amp;0 translation regime, one of the following:
- -If the stage 2 IA is a Non-secure IPA, then VTCR\_EL2.TG0.
- -If the stage 2 IA is a Secure IPA, then VSTCR\_EL2.TG0.
- For a stage 2 translation in the Realm EL1&amp;0 translation regime, VTCR\_EL2.TG0.

## D8.2.5.2 Translation table alignment

| R KBLCR   | Atranslation table is required to be aligned to one of the following:                                                                                                                                                                                                                                                                                                |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I TBPFK   | Only when all of the following are true is it possible to have fewer than 8 translation table entries: • The translation table is at the initial lookup level. • Concatenated translation tables are not used.                                                                                                                                                       |
| R VCLZN   | If concatenated translation tables are used, then the concatenated translation tables are required to be aligned to the overall size of the memory occupied by the concatenated translation tables.                                                                                                                                                                  |
| I LBMWQ   | When a translation table lookup reads a translation table entry, all of the following apply: • If the VMSAv8-64 translation system is used, the read is an 8-byte single-copy atomic access. • If the VMSAv9-128 translation system is used, the read is a 16-byte single-copy atomic access.                                                                        |
| R FDKMS   | The endianness of a translation table lookup is determined by the appropriate SCTLR_ELx.EE bit.                                                                                                                                                                                                                                                                      |
| R PZVGH   | Changing an SCTLR_ELx.EE bit requires synchronization before the change is guaranteed to be visible to subsequent operations. For more information, see Synchronization requirements for AArch64 System registers.                                                                                                                                                   |
| I QJDJV   | Arm does not recommend changing an SCTLR_ELx.EE bit unless one or more of the following apply: • The translation table lookups affected by the modified SCTLR_ELx.EE bit belong to an out-of-context translation regime. • For any translation stage affected by the modified SCTLR_ELx.EE bit, address translation is disabled.                                     |
| I TXCPH   | For a translation table lookup in an address translation stage, the TCR_ELx and VTCR_EL2 registers determine the memory Cacheability and Shareability attributes that apply.                                                                                                                                                                                         |
| R ZZSYD   | For a translation table lookup in an address translation stage, the required memory type is Normal memory.                                                                                                                                                                                                                                                           |
| I RMDMS   | For a two stage translation regime, when a translation table lookup from stage 1 occurs, all of the following apply: • Arm recommends that the stage 2 translation of the stage 1 translation table lookup does not map to Device memory. • Software can configure HCR_EL2.PTW to protect stage 2 table walks from mapping stage 1 translation tables Device memory. |
| R XGXKR   | When memory locations that hold the translation tables are accessed by software, and the memory accesses and the translation table walks have mismatched memory attributes, the behavior is the same as different memory accesses to same memory location using mismatched memory attributes. For more information, see Mismatched memory attributes.                |
| I BSKKL   | Arm recommends that the memory attributes applied by the TCR_ELx to the translation tables are the same as the attributes that are applied by other accesses to the memory that holds the translation tables.                                                                                                                                                        |
| I WVTXS   | For more information on Normal and Device memory and on the Cacheability and Shareability attributes, see Memory types and attributes.                                                                                                                                                                                                                               |

## D8.2.6 Translation table walk properties

## D8.2.6.1 Ordering of memory accesses from translation table walks

RTGRMW Atranslation table walk is considered to be a separate observer. An explicit write to the translation tables might be observed by that separate observer for either of the following:

- Atranslation table walk caused by a different explicit write generated by the same instruction.
- Atranslation table walk caused by an explicit access generated by any instruction appearing in program order after the instruction doing the explicit write to the translation table.

RSPVBD The explicit write to the translation tables is guaranteed to be observable, to the extent required by the Shareability attributes, only after the execution of a DSB instruction. This DSB instruction and the instruction that performed the explicit write to the translation tables must have been executed by the same PE.

RRGPMV Any writes to the translation tables are not observed by any translation table accesses associated with an explicit memory access generated by a load or store that occurs in program order before the instruction that performs the write to the translation tables.

RNNFPF

IJBHNF

RQVWHP

IVKSMJ

If FEAT\_ETS2 is implemented, then an Effect E1 is Ordered-before an Effect E2 when all of the following apply:

- E1 is not generated by an Advanced SIMD, floating-point, SVE, or SME instruction.
- E2 is not generated for an instruction fetch.
- E1 is an Explicit Memory Effect.
- E1 appears in program order before E3.
- E3 is a TLBUncacheable Fault Effect.
- E2 is Translation-intrinsically-before E3.
- E2 is an Implicit TTD Memory Read Effect.

The full definition of the ordering implications of FEAT\_ETS2 is covered formally in Ordering requirements defined by the formal concurrency model, and the rules in this section are not intended to contradict that section.

For more information about ordering requirements to FEAT\_ETS2, see DSB-ordered-before and ETS-ordered-before.

If FEAT\_ETS3 is implemented, then an Effect E1 is Ordered-before an Effect E2 when all of the following apply:

- E1 is not generated by an Advanced SIMD, floating-point, SVE, or SME instruction.
- E2 is not generated for an instruction fetch.
- E1 is an Explicit Memory Effect.
- E1 appears in program order before E3.
- E3 is an MMU Fault Effect.
- E2 is Translation-intrinsically-before E3.
- E2 is an Implicit TTD Memory Read Effect.

The full definition of the ordering implications of FEAT\_ETS3 is covered formally in Ordering requirements defined by the formal concurrency model, and the rules in this section are not intended to contradict that section.

For more information about ordering requirements to FEAT\_ETS3, see DSB-ordered-before and ETS-ordered-before.

ILTSNZ For more information, see:

- External visibility requirement.
- Memory barriers.

## D8.2.6.2 Security state of translation table lookups

For a translation table walk in a Non-secure translation regime, all translation table lookups are done to Non-secure IPA or PA space.

When EL2 is enabled, the OA space of the Secure EL1&amp;0 stage 1 translation regime is IPA space. In all other cases, the

OAspace for a Secure stage 1 translation regime is PA space.

For a stage 1 translation table walk in a Secure Translation Regime, including the EL3 translation regime when FEAT\_RME is not implemented, the OA space at stage 1 of the translation table lookups is determined by all of the following:

RPXRPP

IMBWLG

RSCHHQ

- The initial translation table lookup is done to Secure OA space.
- When the Table descriptor lookup is to Secure OA space, the descriptor NSTable bit determines one of the following:
- -If NSTable is zero, the next translation table lookup is done to Secure OA space.
- -If NSTable is one, the next translation table lookup is done to Non-secure OA space.
- When the Table descriptor lookup is to Non-secure OA space, the next translation table lookup is done to Non-secure OA space.

For more information, see Hierarchical control of Secure or Non-secure memory accesses.

IVRNWF For a stage 2 translation in a Secure translation regime, the PA space of translation table lookups is determined by one of the following:

- When translating an address in Secure IPA space, the Effective value of the VSTCR\_EL2.SW bit.
- When translating an address in Non-secure IPA space, the Effective value of the VTCR\_EL2.NSW bit.

IKXGHL When an IPA from a Secure translation regime is translated by stage 2 translation, the output PA space of the translation is determined by one of the following:

- When translating an address in Secure IPA space, the Effective value of the VSTCR\_EL2.SA bit.
- When translating an address in Non-secure IPA space, the Effective value of the VTCR\_EL2.NSA bit.

| R DVGRP   | For a stage 1 translation table walk in the Realm EL2 or Realm EL2&0 translation regime, all translation table lookups are done to the Realm PA space.                                             |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I TGPMX   | Regardless of whether stage 1 translation is enabled or disabled in the Realm EL1&0 translation regime, Realm EL2 is always enabled and the OAof a Realm EL1&0 stage 1 translation is a Realm IPA. |
| R PGRQD   | For a stage 2 translation table walk in the Realm EL1&0 translation regime, all translation table lookups are done to the Realm PA space.                                                          |
| I KCYMF   | For a stage 2 translation table walk in the Realm EL1&0 translation regime, VTCR_EL2[30:29] are RES0 and there is no equivalent of the NSA, NSWfields.                                             |
| R CFPDJ   | For a stage 1 translation table walk in the EL3 translation regime, if FEAT_RME is implemented, then all translation table lookups are done to the Root PA space.                                  |

## D8.2.7 Translation Hardening Extension

RFYNMT All statements in this section and subsections require implementation of the OPTIONAL feature, FEAT\_THE.

IYGPNC

To protect the integrity of kernel translations, the Translation Hardening Extension, FEAT\_THE, prevents the Exception level that owns the translation tables from modifying an arbitrary subset of those translation table entries.

## D8.2.7.1 Stage 1 Protected Attribute

RMCDSQ For stage 1 of each translation regime using VMSAv8-64, the value of PnCH is determined as shown in the following table:

## Table D8-11 Determination of PnCH

| Translation regime   | Field          |
|----------------------|----------------|
| EL1&0                | TCR2_EL1.PnCH. |
| EL2&0                | TCR2_EL2.PnCH. |
| EL2                  | TCR2_EL2.PnCH. |
| EL3                  | TCR_EL3.PnCH.  |

RNHZZY

RNBVJL

If one of the following is true, then Protection is enabled:

- If stage 1 translation is using VMSAv8-64 and PnCH is 1.
- If stage 1 translation is using VMSAv9-128.

Otherwise, Protection is disabled. This applies even when stage 1 translation is not enabled.

If Protection is enabled, then the value of the Protected bit in the stage 1 descriptor indicates all of the following:

- If the Protected bit is 0, the descriptor is said to be Non-protected.
- If the Protected bit is 1, the descriptor is said to be Protected.

This applies even when stage 1 translation is not enabled.

RVDPDW For a stage 1 descriptor, if Protection is enabled and the RCW checks fail, then RCW and RCWS instructions do not update that descriptor. The RCW checks are:

- RCWState Checks:
- -For a Protected descriptor, there is an attempt to change the protection or validity of that descriptor.
- -For a Non-protected descriptor, there is an attempt to change the protection of that descriptor.
- RCWMaskCheck:
- -For a Protected and valid descriptor, when an attempt is made to update a bit in that descriptor and the Effective value of the corresponding RCWMASK\_EL1 bit is 0.

RNYFNK For a stage 1 descriptor, if RCWS checks fail, then RCWS instructions do not update that descriptor. The RCWS checks are:

- RCWSState check:
- -This check fails if there is an attempt to change the validity of that descriptor and one of the following applies:
- -The descriptor is valid.
- -The descriptor is invalid and Protection is disabled.
- -The descriptor is invalid and it is a Non-protected descriptor.
- RCWSMask check:
- -This check fails if, for a valid descriptor, an attempt is made to update a bit in that descriptor and the Effective value of the corresponding RCWSMASK\_EL1 bit is 0.

ILBYCD Even when a descriptor is not Protected, the bitmask in RCWSMASK\_EL1 controls which fields in a descriptor are permitted to be updated by an RCWS instruction, as follows:

- Avalue of 0 indicates that the corresponding bit of the descriptor cannot be changed.
- Avalue of 1 indicates that the corresponding bit of the descriptor can be changed.

IQSXGJ It is expected that the contents of RCWMASK\_EL1 and RCWSMASK\_EL1 registers are set once by the hypervisor for each instance of a Virtual Machine.

RCRSZF If Protection is not enabled, then RCW instructions can change all bits in a stage 1 descriptor.

ILWWYX RCWS instructions are subject to the RCWS State and Mask checks, even if Protection is disabled.

RQVMPP

When stage 1 translation is disabled at ELx, all of the following apply:

- RCW instructions are subjected to RCW checks.
- RCWS instructions are subjected to RCW checks and RCWS checks.

IXSNQG It is expected that RCW instructions at ELx are used to update stage 1 descriptors owned by ELx. RCW instructions at ELx are not expected to update stage 1 descriptors not owned by ELx, or stage 2 descriptors.

IMWKTV It is expected that RCWS instructions are used to update bits in descriptors that are reserved for software use and, correspondingly, only bits reserved for software use are set to 1 in RCWSMASK\_EL1. If descriptor changes affect only bits that are interpreted by software, then it is not necessary to do TLB maintenance to synchronize the effect on the TLB.

RSSRXH

## D8.2.7.2 Stage 1 Reduced Coherence write

RNRVRT

Awrite has the Reduced Coherence property if and only if it is written by an RCWS instruction and Permit Translation Table Walk Incoherence , PTTWI, is 1 on the PE executing that RCWS instruction.

RQWZDZ

For stage 1 translations in a translation regime, the value of PTTWI is obtained as shown in the following table:

## Table D8-12 Determination of PTTWI

| Translation Regime   | Field                                                                                                |
|----------------------|------------------------------------------------------------------------------------------------------|
| EL1&0                | If EL2 is not enabled, then TCR2_EL1.PTTWI. If EL2 is enabled, then TCR2_EL1.PTTWI &&HCRX_EL2.PTTWI. |
| EL2&0                | TCR2_EL2.PTTWI                                                                                       |
| EL2                  | TCR2_EL2.PTTWI                                                                                       |
| EL3                  | TCR_EL3.PTTWI                                                                                        |

## RDTFHS

If all of the following apply, a read of a memory location as part of a translation table walk is permitted to observe the most-recent write entry without the Reduced Coherence property, W1, in the coherence order of that memory location:

- The read is done as part of a translation table walk.
- The read is not the read effect due to a hardware update of a translation table entry.
- The read is permitted by the memory model to observe a write entry with the Reduced Coherence property, W2, in the coherence order of that memory location.

RGLBZZ

The effect of PTTWI on RCWS instructions applies regardless of whether translation is enabled or disabled.

RYHRDF

It is permitted to implement each PTTWI bit as a read-only bit with a fixed value of 0.

IBBTRQ

PTTWI is permitted to be cached in a TLB.

## D8.2.7.3 Assured translation

If all of the following apply, the level of the stage 1 translation table walk for a V A has the Assured Translation property:

- The EL1&amp;0 translation regime has two translation stages enabled.
- For the initial lookup level of a walk, one of the following applies:
- -The walk is from TTBR0\_EL1 and VTCR\_EL2.TL0 is 1.
- -The walk is from TTBR1\_EL1 and VTCR\_EL2.TL1 is 1.
- For subsequent levels, all of the following apply:
- -All previous levels of the stage 1 walk have the Assured Translation property.
- -The stage 1 translation table descriptor is a Protected descriptor and is fetched from an IPA with the with stage 2 MRO permission.

Note

When Stage 2 Overlay permissions are enabled, S2OverlayPerm can provide MRO permission for an IPA. To ensure that EL1 cannot create Assured translations for itself, EL2 must either disable Stage 2 Overlay permissions or disable EL1 access to S2POR\_EL1. For more information, see Stage 2 Overlay permissions.

RYXKRB

The IPA AssuredOnly attribute is determined as shown in the following table:

| Stage 2 format   | VTCR_EL2.AssuredOnly   | AssuredOnly attribute                      |
|------------------|------------------------|--------------------------------------------|
| VMSAv8-64        | 0                      | 0                                          |
| VMSAv8-64        | 1                      | Block or Page descriptor AssuredOnly field |
| VMSAv9-128       | RES0                   | Block or Page descriptor AssuredOnly field |

RWWYDL

RQNQZJ

IZCRKQ

RBCSRJ

If an IPA is translated by a stage 2 Block or Page descriptor with the AssuredOnly attribute set to 1, and any of the following apply, then any access translated by that descriptor generates a stage 2 Permission fault:

- The level of the stage 1 translation table walk that generated the IPA does not have the Assured Translation property.
- Stage 1 translation is disabled.

If all of the following apply, privileged Guarded control stack data accesses from EL1 to a memory location generate a stage 2 Permission fault due to an AssuredOnly check, independent of whether the stage 1 translation has the Assured Translation property:

- VTCR\_EL2.GCSH is 1.
- Stage 2 translation is enabled.
- The memory location is translated using a stage 2 Block or Page descriptor with the AssuredOnly attribute set to 0.

For more information, see Guarded Control Stack data accesses.

## D8.2.7.4 Stage 2 TopLevel checks

If stage 2 translation is enabled, then the stage 2 TopLevel0 and TopLevel1 permissions indicate that the IPA can be used as a top-level table for TTBR0\_EL1 and TTBR1\_EL1 respectively.

For more information, see Stage 2 Base permissions.

For a VA translated by TTBR0\_EL1, the stage 2 translation of the initial lookup level of the stage 1 translation table walk generates a stage 2 Permission fault due to the TopLevel checks according to the conditions in the following table:

Table D8-14 TopLevel check conditions for translations by TTBR0\_EL1

| VTCR_EL2.TL0   | VTCR_EL2.TL1   | {TopLevel0, TopLevel1}   | Permission fault   |
|----------------|----------------|--------------------------|--------------------|
| 0              | 0              | {x, x}                   | No                 |
| 0              | 1              | {0, 1}                   | Yes                |
|                |                | {0, 0}, {1, x}           | No                 |
| 1              | x              | {0, x}                   | Yes                |
|                |                | {1, x}                   | No                 |

For more information, see Stage 2 Base permissions.

For a VA translated by TTBR1\_EL1, the stage 2 translation of the initial lookup level of the stage 1 translation table walk generates a stage 2 Permission fault due to the TopLevel checks according to the conditions in the following table:

RSWLZW

Table D8-15 TopLevel check conditions for translations by TTBR1\_EL1

| VTCR_EL2.TL0   | VTCR_EL2.TL1   | {TopLevel0, TopLevel1}   | Permission fault   |
|----------------|----------------|--------------------------|--------------------|
| 0              | 0              | {x, x}                   | No                 |
| 1              | 0              | {1, 0}                   | Yes                |
|                |                | {0, 0}, {x, 1}           | No                 |
| x              | 1              | {x, 0}                   | Yes                |
|                |                | {x, 1}                   | No                 |

For more information, see Stage 2 Base permissions.

## D8.2.8 VMSAv8-64 translation using the 4KB granule

| R LCVYF   | All statements in this section and subsections require a translation stage use the VMSAv8-64 translation system.                                                                                                                                                                                              |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I SZLLC   | Address translations that use the 4KB granule have a 4KB page size. Depending on the settings and supported features, up to 40 address bits are resolved using up to 5 lookup levels.                                                                                                                         |
| R FMKVP   | Throughout this section, if an address translation stage is not specified, then references to the Effective value of TCR_ELx.DS also apply to VTCR_EL2.DS.                                                                                                                                                    |
| I VNNCG   | For the 4KB translation granule, the maximum VA and PA supported by a translation regime is one of the following: • If the Effective value of TCR_ELx.DS is 0, then the maximum VA and PA supported is 48 bits. • If the Effective value of TCR_ELx.DS is 1, then the maximum VA and PA supported is 52 bits. |
| R QGLQX   | For the 4KB translation granule, if the Effective value of TCR_ELx.DS is 0, then OA[51:48] are treated as 0b0000 .                                                                                                                                                                                            |
| R KSBQV   | For each lookup level supported by the 4KB translation granule, the following table describes the translation table properties at that level.                                                                                                                                                                 |

Table D8-16 4KB granule translation table properties at each lookup level

| Lookup level   | Index into translation table   | Maximum entries in table   | Contents of translation table entries   | Additional requirements             |
|----------------|--------------------------------|----------------------------|-----------------------------------------|-------------------------------------|
| -1             | -                              | -                          | Lookup level not supported              | Effective value of TCR_ELx.DS is 0. |
|                | IA[51:48]                      | 16                         | Table descriptors                       | Effective value of TCR_ELx.DS is 1. |
| 0              | IA[47:39]                      | 512                        | Table descriptors                       | Effective value of TCR_ELx.DS is 0. |
|                |                                |                            | Table descriptors and Block descriptors | Effective value of TCR_ELx.DS is 1. |
| 1              | IA[38:30]                      | 512                        | Table descriptors and Block descriptors | -                                   |
| 2              | IA[29:21]                      | 512                        | Table descriptors and Block descriptors | -                                   |
| 3              | IA[20:12]                      | 512                        | Page descriptors                        | -                                   |

RYLGLV

For the 4KB translation granule, a translation resolved by a Page descriptor at lookup level 3 has all of the following properties:

- The page size is 4KB.
- The translation can resolve a page using one of the following maximum address ranges:
- -If the Effective value of TCR\_ELx.DS is 0, then IA[47:12].
- -If the Effective value of TCR\_ELx.DS is 1, then IA[51:12].

RNKQNK

RGWNBR

- The page is addressed by one of the following:
- -If the Effective value of TCR\_ELx.DS is 0, then OA[47:12].
- -If the Effective value of TCR\_ELx.DS is 1, then OA[51:12].
- IA[11:0] is mapped directly to OA[11:0].

For the 4KB translation granule, a translation resolved by a Block descriptor at the specified lookup level has all of the properties shown in the following table:

Table D8-17 4KB granule block descriptor properties at each lookup level

| Lookup level   | Size of memory region addressed by Block descriptor   | Bit range that is direct mapped from IA to OA   | IA bit range that selects Block descriptor   |   Effective value of TCR_ELx.DS |
|----------------|-------------------------------------------------------|-------------------------------------------------|----------------------------------------------|---------------------------------|
| 0              | Not supported                                         | -                                               | -                                            |                               0 |
|                | 512GB                                                 | IA[38:0] maps to OA[38:0]                       | IA[51:39]                                    |                               1 |
| 1              | 1GB                                                   | IA[29:0] maps to OA[29:0]                       | IA[47:30]                                    |                               0 |
|                |                                                       |                                                 | IA[51:30]                                    |                               1 |
| 2              | 2MB                                                   | IA[20:0] maps to OA[20:0]                       | IA[47:21]                                    |                               0 |
|                |                                                       |                                                 | IA[51:21]                                    |                               1 |

IXLXHW

For the 4KB translation granule, the following figure shows how the maximum 52-bit IA size is resolved. An IA larger than 48 bits requires that the Effective value of TCR\_ELx.DS is 1.

## Using the 4KB translation granule

Figure D8-3 52-bit IA resolved using 4KB translation granule

<!-- image -->

## D8.2.8.1 VMSAv8-64 Stage 1 address translation using the 4KB translation granule

For the 4KB translation granule, when a stage 1 translation table walk is started, the initial lookup level is determined by the value of the TCR\_ELx.T n SZ field as shown in the following table.

IGVFLG

Table D8-18 4KB granule, determining stage 1 initial lookup level

|   Initial lookup level |   T n SZ minimum value | Maximum IA bits resolved   |   T n SZ maximum value | Minimum IA bits resolved   | Additional requirements            |
|------------------------|------------------------|----------------------------|------------------------|----------------------------|------------------------------------|
|                     -1 |                     12 | IA[51:12]                  |                     15 | IA[48:12]                  | Effective value of TCR_ELx.DS is 1 |
|                      0 |                     16 | IA[47:12]                  |                     24 | IA[39:12]                  | -                                  |
|                      1 |                     25 | IA[38:12]                  |                     33 | IA[30:12]                  | -                                  |
|                      2 |                     34 | IA[29:12]                  |                     39 | IA[24:12]                  | -                                  |
|                      2 |                     40 | IA[23:12]                  |                     42 | IA[21:12]                  | FEAT_TTST is implemented           |
|                      3 |                     43 | IA[20:12]                  |                     48 | IA[15:12]                  | FEAT_TTST is implemented           |

IJCHLN

For a stage 1 translation in the 4KB translation granule, depending on the IA size, the initial lookup level is indexed by up to 9 bits and all remaining lookup levels are indexed by exactly 9 bits.

IVKJBP

For the 4KB translation granule and a 52-bit IA, the following figure is a generalized view of a stage 1 address translation. An IA and an OA larger than 48 bits requires that the Effective value of TCR\_ELx.DS is 1. The 512GB block size requires that the Effective value of TCR\_ELx.DS is 1.

Figure D8-4 Generalized view of a stage 1 address translation using the 4KB granule

<!-- image -->

## D8.2.8.2 VMSAv8-64 Stage 2 address translation using the 4KB translation granule

For the 4KB translation granule, when a stage 2 translation table walk is started, the initial lookup level is determined by one of the following:

- If the Effective value of VTCR\_EL2.DS is 0, then the initial lookup level is determined by one of VTCR\_EL2.SL0 or VSTCR\_EL2.SL0, and VTCR\_EL2.SL2 and VSTCR\_EL2.SL2 are RES0 .

IPBGCS

- If the Effective value of VTCR\_EL2.DS is 1, then the initial lookup level is determined by the combination of VTCR\_EL2.SL0 and VTCR\_EL2.SL2, or VSTCR\_EL2.SL0 and VSTCR\_EL2.SL2.

For the 4KB translation granule, when a stage 2 translation table walk is started, the following table shows the initial lookup level determined by VTCR\_EL2.SL0 or VSTCR\_EL2.SL0 and, when the Effective value of VTCR\_EL2.DS is 1, the corresponding VTCR\_EL2.SL2 or VSTCR\_EL2.SL2.

Table D8-19 4KB granule, determining stage 2 initial lookup level

| SL2   | SL0   | Initial lookup level   |
|-------|-------|------------------------|
| 0b0   | 0b00  | Level 2                |
| 0b0   | 0b01  | Level 1                |
| 0b0   | 0b10  | Level 0                |
| 0b0   | 0b11  | Level 3                |
| 0b1   | 0b00  | Level -1               |
| 0b1   | 0b01  | Reserved               |
| 0b1   | 0b10  | Reserved               |
| 0b1   | 0b11  | Reserved               |

RDBNDG

For the 4KB translation granule, when a stage 2 translation table walk is started and the initial lookup level is -1, the following table shows all of the permitted concatenated translation table configurations and the corresponding VTCR\_EL2.T0SZ or VSTCR\_EL2.T0SZ value:

## Table D8-20 4KB granule, stage 2 initial lookup at level -1

| Number of concatenated translation tables   | IA bits resolved    | T0SZ   | Additional requirements             |
|---------------------------------------------|---------------------|--------|-------------------------------------|
| None (1 table)                              | IA[51:12]-IA[48-12] | 12-15  | Effective value of VTCR_EL2.DS is 1 |

RPZFHQ

For the 4KB translation granule, when a stage 2 translation table walk is started and the initial lookup level is 0, the following table shows all of the permitted concatenated translation table configurations and the corresponding VTCR\_EL2.T0SZ or VSTCR\_EL2.T0SZ value:

Table D8-21 4KB granule, stage 2 initial lookup at level 0

| Number of concatenated translation tables   | IA bits resolved    | T0SZ   | Additional requirements             |
|---------------------------------------------|---------------------|--------|-------------------------------------|
| None (1 table)                              | IA[47:12]-IA[39:12] | 16-24  | -                                   |
| 2                                           | IA[48:12]           | 15     | Effective value of VTCR_EL2.DS is 1 |
| 4                                           | IA[49:12]           | 14     | Effective value of VTCR_EL2.DS is 1 |
| 8                                           | IA[50:12]           | 13     | Effective value of VTCR_EL2.DS is 1 |
| 16                                          | IA[51:12]           | 12     | Effective value of VTCR_EL2.DS is 1 |

RMKPBG

For the 4KB translation granule, when a stage 2 translation table walk is started and the initial lookup level is 1, the following table shows all of the permitted concatenated translation table configurations and the corresponding VTCR\_EL2.T0SZ or VSTCR\_EL2.T0SZ value:

## Table D8-22 4KB granule, stage 2 initial lookup at level 1

| Number of concatenated translation tables   | IA bits resolved    | T0SZ   | Additional requirements   |
|---------------------------------------------|---------------------|--------|---------------------------|
| None (1 table)                              | IA[38:12]-IA[30:12] | 25-33  | -                         |
| 2                                           | IA[39:12]           | 24     | -                         |
| 4                                           | IA[40:12]           | 23     | -                         |
| 8                                           | IA[41:12]           | 22     | -                         |
| 16                                          | IA[42:12]           | 21     | -                         |

RKKRSZ

For the 4KB translation granule, when a stage 2 translation table walk is started and the initial lookup level is 2, the following table shows all of the permitted concatenated translation table configurations and the corresponding VTCR\_EL2.T0SZ or VSTCR\_EL2.T0SZ value:

Table D8-23 4KB granule, stage 2 initial lookup at level 2

| Number of concatenated translation tables   | IA bits resolved    | T0SZ   | Additional requirements   |
|---------------------------------------------|---------------------|--------|---------------------------|
| None (1 table)                              | IA[23:12]-IA[21:12] | 40-42  | FEAT_TTST is implemented  |
| None (1 table)                              | IA[29:12]-IA[24:12] | 34-39  | -                         |
| 2                                           | IA[30:12]           | 33     | -                         |
| 4                                           | IA[31:12]           | 32     | -                         |
| 8                                           | IA[32:12]           | 31     | -                         |
| 16                                          | IA[33:12]           | 30     | -                         |

RTJMNP

For the 4KB translation granule, when a stage 2 translation table walk is started and the initial lookup level is 3, the following table shows all of the permitted concatenated translation table configurations and the corresponding VTCR\_EL2.T0SZ or VSTCR\_EL2.T0SZ value:

## Table D8-24 4KB granule, stage 2 initial lookup at level 3

| Number of concatenated translation tables   | IA bits resolved    | T0SZ   | Additional requirements   |
|---------------------------------------------|---------------------|--------|---------------------------|
| None (1 table)                              | IA[20:12]-IA[15:12] | 43-48  | FEAT_TTST is implemented  |
| 2                                           | IA[21:12]           | 42     | FEAT_TTST is implemented  |
| 4                                           | IA[22:12]           | 41     | FEAT_TTST is implemented  |
| 8                                           | IA[23:12]           | 40     | FEAT_TTST is implemented  |
| 16                                          | IA[24:12]           | 39     | FEAT_TTST is implemented  |

ISWBVJ

For the 4KB translation granule and a 52-bit IA, the following figure is a generalized view of a stage 2 address translation. An IA larger than 48 bits requires that the Effective value of VTCR\_EL2.DS is 1. The 512GB block size requires that the Effective value of VTCR\_EL2.DS is 1.

Figure D8-5 Generalized view of a stage 2 address translation using the 4KB granule

<!-- image -->

For the 4KB translation granule, when a stage 2 translation table walk is started and one of the following is true, a stage 2 level 0 Translation fault is generated:

- If the Effective value of VTCR\_EL2.DS is 0, then one or more of the following is true:
- -The VTCR\_EL2.T0SZ or VSTCR\_EL2.T0SZ value is not consistent with the corresponding VTCR\_EL2.SL0 or VSTCR\_EL2.SL0 value.
- -VTCR\_EL2.SL0 or VSTCR\_EL2.SL0 is programmed to a reserved value.
- If the Effective value of VTCR\_EL2.DS is 1, then one or more of the following is true:
- -The VTCR\_EL2.T0SZ or VSTCR\_EL2.T0SZ value is not consistent with the corresponding VTCR\_EL2.{SL2, SL0} or VSTCR\_EL2.{SL2, SL0} value.
- -VTCR\_EL2.{SL2, SL0} or VSTCR\_EL2.{SL2, SL0} is programmed to a reserved value.

For more information, see Concatenated translation tables.

RKTKWK

IHBWKN

RVMRQS

## D8.2.8.3 Finding the descriptor when using the VMSAv8-64 4KB translation granule

For the 4KB translation granule, the following table shows the algorithm to find the descriptor address at each supported lookup level, using of all of the following information:

- The translation table base address, BaseAddr .
- The number of bits in the supported PA size, PAsize .
- The IA supplied to the translation stage and used as an index into the translation table.
- For each initial lookup level, the permitted range of values for TCR\_ELx.T n SZ.
- For a stage 2 translation, all of the following:
- -The value of VTCR\_EL2.T0SZ or VSTCR\_EL2.T0SZ.
- -The value of VTCR\_EL2.SL0 or VSTCR\_EL2.SL0.
- -If the Effective value of VTCR\_EL2.DS is 1, then the value of VTCR\_EL2.SL2 or VSTCR\_EL2.SL2.

## Table D8-25 4KB granule, finding the descriptor address

|   Lookup level | Stage 1 translation table descriptor address                                                         | Stage 2 translation table descriptor address                                                                    |
|----------------|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
|             -1 | if 12 <= T n SZ <= 15 then x = (19 - T n SZ) BaseAddr[PAsize-1: x ]:IA[ x +44:48]: 0b000             | if SL2==1 and SL0==0 then if 12 <= T0SZ <= 15 then x = (19 - T0SZ) BaseAddr[PAsize-1: x ]:IA[ x +44:48]: 0b000  |
|              0 | if 16 <= T n SZ <= 24 then x = (28 - T n SZ) else x = 12 BaseAddr[PAsize-1: x ]:IA[ x +35:39]: 0b000 | if SL0==2 then if 12 <= T0SZ <= 24 then x = (28 - T0SZ) else x = 12 BaseAddr[PAsize-1: x ]:IA[ x +35:39]: 0b000 |
|              1 | if 25 <= T n SZ <= 33 then x = (37 - T n SZ) else x = 12                                             | if SL0==1 then if 21 <= T0SZ <= 33 then x = (37 - T0SZ) else x = 12                                             |
|              2 | if 34 <= T n SZ <= 42 then x = (46 - T n SZ) else x = 12 BaseAddr[PAsize-1: x ]:IA[ x +17:21]: 0b000 | if SL0==0 then if 30 <= T0SZ <= 42 then x = (46 - T0SZ) else x = 12 BaseAddr[PAsize-1: x ]:IA[ x +17:21]: 0b000 |
|              3 | if 43 <= T n SZ <= 48 then x = (55 - T n SZ) else x = 12 BaseAddr[PAsize-1: x ]:IA[ x +8:12]: 0b000  | if SL0==3 then if 39 <= T0SZ <= 48 then x = (55 - T0SZ) else x = 12 BaseAddr[PAsize-1: x ]:IA[ x +8:12]: 0b000  |

## D8.2.9 VMSAv8-64 translation using the 16KB granule

| R QSQNQ   | All statements in this section and subsections require a translation stage use the VMSAv8-64 translation system.                                                                                                                                                                                               |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I TDTCY   | Address translations that use the 16KB granule have a 16KB page size. Depending on the settings and supported features, up to 38 address bits are resolved using up to 4 lookup levels.                                                                                                                        |
| R VQYZX   | Throughout this section, if an address translation stage is not specified, then references to the Effective value of TCR_ELx.DS also apply to VTCR_EL2.DS.                                                                                                                                                     |
| I JCYXY   | For the 16KB translation granule, the maximum VA and PA supported by a translation regime is one of the following: • If the Effective value of TCR_ELx.DS is 0, then the maximum VA and PA supported is 48 bits. • If the Effective value of TCR_ELx.DS is 1, then the maximum VA and PA supported is 52 bits. |

RCDLYH

For the 16KB translation granule, if the Effective value of TCR\_ELx.DS is 0, then OA[51:48] are treated as 0b0000 .

RVGVLD

For each lookup level supported by the 16KB translation granule, the following table describes the translation table properties at that level.

Table D8-26 16KB granule translation table properties at each lookup level

| Lookup level   | Index into translation table   | Maximum entries in table   | Contents of translation table entries                        | Additional requirements            |
|----------------|--------------------------------|----------------------------|--------------------------------------------------------------|------------------------------------|
| 0              | IA[47]                         | 232                        | Table descriptors Lookup level 0 supported only at stage 1   | Effective value of TCR_ELx.DS is 0 |
|                | IA[51:47]                      |                            | Table descriptors Lookup level 0 supported at stages 1 and 2 | Effective value of TCR_ELx.DS is 1 |
| 1              | IA[46:36]                      | 2048                       | Table descriptors                                            | Effective value of TCR_ELx.DS is 0 |
|                |                                |                            | Table descriptors and Block descriptors                      | Effective value of TCR_ELx.DS is 1 |
| 2              | IA[35:25]                      | 2048                       | Table descriptors and Block descriptors                      | -                                  |
| 3              | IA[24:14]                      | 2048                       | Page descriptors                                             | -                                  |

RRYDBQ

RFFHSQ

For the 16KB translation granule, a translation resolved by a Page descriptor at lookup level 3 has all of the following properties:

- The page size is 16KB.
- The translation can resolve a page using one of the following maximum address ranges:
- -If the Effective value of TCR\_ELx.DS is 0, then IA[47:14].
- -If the Effective value of TCR\_ELx.DS is 1, then IA[51:14].
- The page is addressed by one of the following:
- -If the Effective value of TCR\_ELx.DS is 0, then OA[47:14].
- -If the Effective value of TCR\_ELx.DS is 1, then OA[51:14].
- IA[13:0] is mapped directly to OA[13:0].

For the 16KB translation granule, a translation resolved by a Block descriptor at the specified lookup level has all of the properties shown in the following table:

Table D8-27 16KB granule block descriptor properties at each lookup level

| Lookup level   | Size of memory region addressed by Block descriptor   | Bit range that is direct mapped from IA to OA   | IA bit range that selects Block descriptor   |   Effective value of TCR_ELx.DS |
|----------------|-------------------------------------------------------|-------------------------------------------------|----------------------------------------------|---------------------------------|
| 1              | Not supported                                         | -                                               | -                                            |                               0 |
|                | 64GB                                                  | IA[35:0] maps to OA[35:0]                       | IA[51:36]                                    |                               1 |
| 2              | 32MB                                                  | IA[24:0] maps to OA[24:0]                       | IA[47:25]                                    |                               0 |
|                |                                                       |                                                 | IA[51:25]                                    |                               1 |

IMJSJR

For the 16KB translation granule, the following figure shows how the maximum 52-bit IA size is resolved. An IA larger than 48 bits requires that the Effective value of TCR\_ELx.DS is 1.

RJHFFJ

Figure D8-6 52-bit IA resolved using 16KB translation granule

<!-- image -->

## D8.2.9.1 VMSAv8-64 Stage 1 address translation using the 16KB translation granule

For the 16KB translation granule, when a stage 1 translation table walk is started, the initial lookup level is determined by the value of the TCR\_ELx.T n SZ field as shown in the following table:

Table D8-28 16KB granule, determining stage 1 initial lookup level

|   Initial lookup level |   T n SZ minimum value | Maximum IA bits resolved   |   T n SZ maximum value | Minimum IA bits resolved   | Additional requirements            |
|------------------------|------------------------|----------------------------|------------------------|----------------------------|------------------------------------|
|                      0 |                     12 | IA[51:14]                  |                     15 | IA[48:14]                  | Effective value of TCR_ELx.DS is 1 |
|                      0 |                     16 | IA[47:14]                  |                     16 | IA[47:14]                  | -                                  |
|                      1 |                     17 | IA[46:14]                  |                     27 | IA[36:14]                  | -                                  |
|                      2 |                     28 | IA[35:14]                  |                     38 | IA[25:14]                  | -                                  |
|                      3 |                     39 | IA[24:14]                  |                     39 | IA[24:14]                  | -                                  |
|                      3 |                     40 | IA[23:14]                  |                     48 | IA[15:14]                  | FEAT_TTST is implemented           |

IFLDKN

For a stage 1 translation in the 16KB translation granule, depending on the IA size, the initial lookup level is indexed by up to 11 bits and all remaining lookup levels are indexed by exactly 11 bits.

IKSSHJ

For the 16KB translation granule and a 52-bit IA, the following figure is a generalized view of a stage 1 address translation. An IA and an OA larger than 48 bits requires that the Effective value of TCR\_ELx.DS is 1. The 64GB block size requires that the Effective value of TCR\_ELx.DS is 1.

Figure D8-7 Generalized view of a stage 1 address translation using the 16KB granule

<!-- image -->

## D8.2.9.2 VMSAv8-64 Stage 2 address translation using the 16KB translation granule

IQDHZV

For the 16KB translation granule, when a stage 2 translation table walk is started, the initial lookup level is determined by the corresponding VTCR\_EL2.SL0 or VSTCR\_EL2.SL0 value.

IMKHHJ

For the 16KB translation granule, when a stage 2 translation table walk is started, the following table shows the initial lookup level determined by SL0:

Table D8-29 16KB granule, determining stage 2 initial lookup level

| SL0   | Initial lookup level   |
|-------|------------------------|
| 0b00  | Level 3                |
| 0b01  | Level 2                |
| 0b10  | Level 1                |
| 0b11  | Level 0                |

RJKYLY

For the 16KB translation granule, when a stage 2 translation table walk is started and the initial lookup level is 0, the following table shows all of the permitted concatenated translation table configurations and the corresponding VTCR\_EL2.T0SZ or VSTCR\_EL2.T0SZ value:

## Table D8-30 16KB granule, stage 2 initial lookup at level 0

| Number of concatenated translation tables   | IA bits resolved    | T0SZ   | Additional requirements             |
|---------------------------------------------|---------------------|--------|-------------------------------------|
| None (1 table)                              | IA[51:14]-IA[47:14] | 12-16  | Effective value of VTCR_EL2.DS is 1 |

RFBHPY

For the 16KB translation granule, when a stage 2 translation table walk is started and the initial lookup level is 1, the following table shows all of the permitted concatenated translation table configurations and the corresponding VTCR\_EL2.T0SZ or VSTCR\_EL2.T0SZ value:

## Table D8-31 16KB granule, stage 2 initial lookup at level 1

| Number of concatenated translation tables   | IA bits resolved    | T0SZ   | Additional requirements             |
|---------------------------------------------|---------------------|--------|-------------------------------------|
| None (1 table)                              | IA[46:14]-IA[36:14] | 17-27  | -                                   |
| 2                                           | IA[47:14]           | 16     | -                                   |
| 4                                           | IA[48:14]           | 15     | Effective value of VTCR_EL2.DS is 1 |
| 8                                           | IA[49:14]           | 14     | Effective value of VTCR_EL2.DS is 1 |
| 16                                          | IA[50:14]           | 13     | Effective value of VTCR_EL2.DS is 1 |

RMJPYK

For the 16KB translation granule, when a stage 2 translation table walk is started and the initial lookup level is 2, the following table shows all of the permitted concatenated translation table configurations and the corresponding VTCR\_EL2.T0SZ or VSTCR\_EL2.T0SZ value:

## Table D8-32 16KB granule, stage 2 initial lookup at level 2

| Number of concatenated translation tables   | IA bits resolved    | T0SZ   | Additional requirements   |
|---------------------------------------------|---------------------|--------|---------------------------|
| None (1 table)                              | IA[35:14]-IA[25:14] | 28-38  | -                         |
| 2                                           | IA[36:14]           | 27     | -                         |
| 4                                           | IA[37:14]           | 26     | -                         |
| 8                                           | IA[38:14]           | 25     | -                         |
| 16                                          | IA[39:14]           | 24     | -                         |

RWDMGC

For the 16KB translation granule, when a stage 2 translation table walk is started and the initial lookup level is 3, the following table shows all of the permitted concatenated translation table configurations and the corresponding VTCR\_EL2.T0SZ or VSTCR\_EL2.T0SZ value:

## Table D8-33 16KB granule, stage 2 initial lookup at level 3

| Number of concatenated translation tables   | IA bits resolved    | T0SZ   | Additional requirements   |
|---------------------------------------------|---------------------|--------|---------------------------|
| None (1 table)                              | IA[23:14]-IA[15:14] | 40-48  | FEAT_TTST is implemented  |
| None (1 table)                              | IA[24:14]           | 39     | -                         |
| 2                                           | IA[25:14]           | 38     | -                         |
| 4                                           | IA[26:14]           | 37     | -                         |
| 8                                           | IA[27:14]           | 36     | -                         |
| 16                                          | IA[28:14]           | 35     | -                         |

IGBRMW

For the 16KB translation granule and a 52-bit IA, the following figure is a generalized view of a stage 2 address translation. An IA larger than 48 bits requires that the Effective value of VTCR\_EL2.DS is 1. The 64GB block size requires that the Effective value of VTCR\_EL2.DS is 1.

Figure D8-8 Generalized view of a stage 2 address translation using the 16KB granule

<!-- image -->

For the 16KB translation granule, when a stage 2 translation table walk is started and one of the following is true, a stage 2 level 0 Translation fault is generated:

- The VTCR\_EL2.T0SZ or VSTCR\_EL2.T0SZ value is not consistent with the corresponding VTCR\_EL2.SL0 or VSTCR\_EL2.SL0 value.
- VTCR\_EL2.SL0 or VSTCR\_EL2.SL0 is programmed to a reserved value.

For more information, see Concatenated translation tables.

## D8.2.9.3 Finding the descriptor when using the VMSAv8-64 16KB translation granule

For the 16KB translation granule, the following table shows the algorithm to find the descriptor address at each supported lookup level, using of all of the following information:

- The translation table base address, BaseAddr .
- The number of bits in the supported PA size, PAsize .
- The IA supplied to the translation stage and used as an index into the translation table.
- For each initial lookup level, the permitted range of values for TCR\_ELx.T n SZ.

RNWPLD

IFXRPG

RKMTBZ

- For a stage 2 translation, all of the following:
- -The value of VTCR\_EL2.T0SZ or VSTCR\_EL2.T0SZ.
- -The value of VTCR\_EL2.SL0 or VSTCR\_EL2.SL0.

## Table D8-34 16KB granule, finding the descriptor address

|   Lookup level | Stage 1 translation table descriptor address                                                         | Stage 2 translation table descriptor address                                                                    |
|----------------|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
|              0 | if 12 <= T n SZ <= 16 then x = (20 - T n SZ) BaseAddr[PAsize-1: x ]:IA[ x +43:47]: 0b000             | if SL0==3 then if 12 <= T0SZ <= 16 then x = (20 - T0SZ) BaseAddr[PAsize-1: x ]:IA[ x +43:47]: 0b000             |
|              1 | if 17 <= T n SZ <= 27 then x = (31 - T n SZ) else x = 14 BaseAddr[PAsize-1: x ]:IA[ x +32:36]: 0b000 | if SL0==2 then if 13 <= T0SZ <= 27 then x = (31 - T0SZ) else x = 14 BaseAddr[PAsize-1: x ]:IA[ x +32:36]: 0b000 |
|              2 | if 28 <= T n SZ <= 38 then x = (42 - T n SZ) else x = 14 BaseAddr[PAsize-1: x ]:IA[ x +21:25]: 0b000 | if SL0==1 then if 24 <= T0SZ <= 38 then x = (42 - T0SZ) else x = 14 BaseAddr[PAsize-1: x ]:IA[ x +21:25]: 0b000 |
|              3 | if 39 <= T n SZ <= 48 then x = (53 - T n SZ) else x = 14 BaseAddr[PAsize-1: x ]:IA[ x +10:14]: 0b000 | if SL0==0 then if 35 <= T0SZ <= 48 then x = (53 - T0SZ) else x = 14 BaseAddr[PAsize-1: x ]:IA[ x +10:14]: 0b000 |

## D8.2.10 VMSAv8-64 translation using the 64KB granule

| R RGNZV   | All statements in this section and subsections require a translation stage use the VMSAv8-64 translation system.                                                                                                                                                     |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I VDPWL   | Address translations that use the 64KB granule have a 64KB page size. Depending on the settings and supported features, up to 36 address bits are resolved using up to 3 lookup levels.                                                                              |
| I LRFQD   | For the 64KB translation granule, the maximum VA size supported by a translation regime is one of the following: • If FEAT_LVA is not implemented, then the maximum VA supported is 48 bits. • If FEAT_LVA is implemented, then the maximum VA supported is 52 bits. |
| I YZDPC   | For the 64KB translation granule, the maximum PA size supported by a translation regime is one of the following: • If FEAT_LPA is not implemented, then the maximum PA supported is 48 bits. • If FEAT_LPA is implemented, then the maximum PA supported is 52 bits. |
| R NSQXP   | For the 64KB translation granule, if FEAT_LPA is not implemented, then OA[51:48] are treated as 0b0000 .                                                                                                                                                             |
| R MLLGN   | For each lookup level supported by the 64KB translation granule, the following table describes the translation table properties at that level.                                                                                                                       |

## Table D8-35 64KB granule translation table properties at each lookup level

|   Lookup level | Index into translation table   |   Maximum entries in table | Contents of translation table entries   | Additional requirements for stage 1   | Additional requirements for stage 2   |
|----------------|--------------------------------|----------------------------|-----------------------------------------|---------------------------------------|---------------------------------------|
|              1 | IA[47:42]                      |                         64 | Table descriptors                       | -                                     | -                                     |
|              1 | IA[47:42]                      |                         64 | Table descriptors and Block descriptors | FEAT_LPA                              | FEAT_LPA                              |
|              1 | IA[51:42]                      |                       1024 | Table descriptors                       | FEAT_LVA                              | -                                     |
|              1 | IA[51:42]                      |                       1024 | Table descriptors and Block descriptors | FEAT_LVA, FEAT_LPA                    | FEAT_LPA                              |
|              2 | IA[41:29]                      |                       8192 | Table descriptors and Block descriptors | -                                     | -                                     |
|              3 | IA[28:16]                      |                       8192 | Page descriptors                        | -                                     | -                                     |

RZWQBH

RRBNGS

For the 64KB translation granule, a translation resolved by a Page descriptor at lookup level 3 has all of the following properties:

- The page size is 64KB.
- For stage 1, the translation can resolve a page using one of the following maximum address ranges:
- -If FEAT\_LVA is not implemented, then IA[47:16].
- -If FEAT\_LVA is implemented, then IA[51:16].
- For stage 2, the translation can resolve a page using one of the following maximum address ranges:
- -If FEAT\_LPA is not implemented, then IA[47:16].
- -If FEAT\_LPA is implemented, then IA[51:16].
- For stage 1 and stage 2, the page is addressed by one of the following:
- -If FEAT\_LPA is not implemented, then OA[47:16].
- -If FEAT\_LPA is implemented, then OA[51:16].
- IA[15:0] is mapped directly to OA[15:0].

For the 64KB translation granule, a translation resolved by a Block descriptor at the specified lookup level has all of the properties shown in the following table:

Table D8-36 64KB granule block descriptor properties at each lookup level

| Lookup level   | Size of memory region addressed by Block descriptor   | Bit range that is direct mapped from IA to OA   | IA bit range that selects Block descriptor   | Additional requirements for stage 1   | Additional requirements for stage 2   |
|----------------|-------------------------------------------------------|-------------------------------------------------|----------------------------------------------|---------------------------------------|---------------------------------------|
| 1              | 4TB                                                   | IA[41:0] maps to OA[41:0]                       | IA[47:42]                                    | FEAT_LPA                              | FEAT_LPA                              |
|                |                                                       |                                                 | IA[51:42]                                    | FEAT_LVA, FEAT_LPA                    | FEAT_LPA                              |
| 2              | 512MB                                                 | IA[28:0] maps to OA[28:0]                       | IA[47:29]                                    | -                                     | -                                     |
|                |                                                       |                                                 | IA[51:29]                                    | FEAT_LVA                              | FEAT_LPA                              |

ITVDSK

For the 64KB translation granule, the following figure shows how the maximum 52-bit IA size is resolved. For a stage 1 translation, an IA larger than 48 bits requires the implementation of FEAT\_LV A. For a stage 2 translation, an IA larger than 48 bits requires the implementation of FEAT\_LPA.

## Using the 64KB translation granule

<!-- image -->

OA Output address

- a. Table entry at previous lookup level
- b. Block entry at previous lookup level

Figure D8-9 52-bit IA resolved using 64KB translation granule

## D8.2.10.1 VMSAv8-64 Stage 1 address translation using the 64KB translation granule

For the 64KB translation granule, when a stage 1 translation table walk is started, the initial lookup level is determined by the value of the TCR\_ELx.T n SZ field as shown in the following table:

## Table D8-37 64KB granule, determining stage 1 initial lookup level

|   Initial lookup level |   T n SZ minimum value | Maximum IA bits resolved   |   T n SZ maximum value | Minimum IA bits resolved   | Additional requirements   |
|------------------------|------------------------|----------------------------|------------------------|----------------------------|---------------------------|
|                      1 |                     12 | IA[51:16]                  |                     15 | IA[48:16]                  | FEAT_LVA is implemented   |
|                      1 |                     16 | IA[47:16]                  |                     21 | IA[42:16]                  | -                         |
|                      2 |                     22 | IA[41:16]                  |                     34 | IA[29:16]                  | -                         |
|                      3 |                     35 | IA[28:16]                  |                     39 | IA[24:16]                  | -                         |
|                      3 |                     40 | IA[23:16]                  |                     47 | IA[16:16]                  | FEAT_TTST is implemented  |

IFQFFW

For a stage 1 translation in the 64KB translation granule, depending on the IA size, the initial lookup level is indexed by up to 13 bits and all remaining lookup levels are indexed by exactly 13 bits.

IMRDWZ

For the 64KB translation granule and a 52-bit IA, the following figure is a generalized view of a stage 1 address translation. An IA larger than 48 bits requires implementation of FEAT\_LV A, and an OA larger than 48 bits requires implementation of FEAT\_LPA. The 4TB block size requires implementation of FEAT\_LPA.

RFMBKV

Figure D8-10 Generalized view of a stage 1 address translation using the 64KB granule

<!-- image -->

## D8.2.10.2 VMSAv8-64 Stage 2 address translation using the 64KB translation granule

IHHFJP

For the 64KB translation granule, when a stage 2 translation table walk is started, the initial lookup level is determined by the corresponding VTCR\_EL2.SL0 or VSTCR\_EL2.SL0 value.

IVLBLQ

For the 64KB translation granule, when a stage 2 translation table walk is started, the following table shows the initial lookup level determined by SL0:

## Table D8-38 64KB granule, determining stage 2 initial lookup level

| SL0   | Initial lookup level   |
|-------|------------------------|
| 0b00  | Level 3                |
| 0b01  | Level 2                |
| 0b10  | Level 1                |
| 0b11  | Reserved               |

RQCSFP

For the 64KB translation granule, when a stage 2 translation table walk is started and the initial lookup level is 1, the following table shows all of the permitted concatenated translation table configurations and the corresponding VTCR\_EL2.T0SZ or VSTCR\_EL2.T0SZ value:

## Table D8-39 64KB granule, stage 2 initial lookup at level 1

| Number of concatenated translation tables   | IA bits resolved    | T0SZ   | Additional requirements   |
|---------------------------------------------|---------------------|--------|---------------------------|
| None (1 table)                              | IA[51:16]-IA[48:16] | 12-15  | FEAT_LPA is implemented   |
| None (1 table)                              | IA[47:16]-IA[42:16] | 16-21  | -                         |

RWHSBD

For the 64KB translation granule, when a stage 2 translation table walk is started and the initial lookup level is 2, the following table shows all of the permitted concatenated translation table configurations and the corresponding VTCR\_EL2.T0SZ or VSTCR\_EL2.T0SZ value:

## Table D8-40 64KB granule, stage 2 initial lookup at level 2

| Number of concatenated translation tables   | IA bits resolved    | T0SZ   | Additional requirements   |
|---------------------------------------------|---------------------|--------|---------------------------|
| None (1 table)                              | IA[41:16]-IA[29:16] | 22-34  | -                         |
| 2                                           | IA[42:16]           | 21     | -                         |
| 4                                           | IA[43:16]           | 20     | -                         |
| 8                                           | IA[44:16]           | 19     | -                         |
| 16                                          | IA[45:16]           | 18     | -                         |

RPLLHG

For the 64KB translation granule, when a stage 2 translation table walk is started and the initial lookup level is 3, the following table shows all of the permitted concatenated translation table configurations and the corresponding VTCR\_EL2.T0SZ or VSTCR\_EL2.T0SZ value:

## Table D8-41 64KB granule, stage 2 initial lookup at level 3

| Number of concatenated translation tables   | IA bits resolved    | T0SZ   | Additional requirements   |
|---------------------------------------------|---------------------|--------|---------------------------|
| None (1 table)                              | IA[23:16]-IA[16:16] | 40-47  | FEAT_TTST is implemented  |
| None (1 table)                              | IA[28:16]-IA[24:16] | 35-39  | -                         |
| 2                                           | IA[29:16]           | 34     | -                         |
| 4                                           | IA[30:16]           | 33     | -                         |
| 8                                           | IA[31:16]           | 32     | -                         |
| 16                                          | IA[32:16]           | 31     | -                         |

ISYRCT

For the 64KB translation granule and a 52-bit IA, the following figure is a generalized view of a stage 2 address translation. An IA larger than 48 bits requires the implementation of FEAT\_LPA. The 4TB block size requires implementation of FEAT\_LPA.

Figure D8-11 Generalized view of a stage 2 address translation using the 64KB granule

<!-- image -->

For the 64KB translation granule, when a stage 2 translation table walk is started and one of the following is true, a stage 2 level 0 Translation fault is generated:

- The VTCR\_EL2.T0SZ or VSTCR\_EL2.T0SZ value is not consistent with the corresponding VTCR\_EL2.SL0 or VSTCR\_EL2.SL0 value.
- VTCR\_EL2.SL0 or VSTCR\_EL2.SL0 is programmed to a reserved value.

For more information, see Concatenated translation tables.

## D8.2.10.3 Finding the descriptor when using the VMSAv8-64 64KB translation granule

For the 64KB translation granule, the following table shows the algorithm to find the descriptor address at each supported lookup level, using of all of the following information:

- The translation table base address, BaseAddr .
- The number of bits in the supported PA size, PAsize .
- The IA supplied to the translation stage and used as an index into the translation table.
- For each initial lookup level, the permitted range of values for TCR\_ELx.T n SZ.
- For a stage 2 translation, all of the following:
- -The value of VTCR\_EL2.T0SZ or VSTCR\_EL2.T0SZ.

RSGCBS

IDKRJG

RLMDCR

RBYPBM

- -The value of VTCR\_EL2.SL0 or VSTCR\_EL2.SL0.

## Table D8-42 64KB granule, finding the descriptor address

|   Lookup level | Stage 1 translation table descriptor address                                                         | Stage 2 translation table descriptor address                                                                    |
|----------------|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
|              1 | if 12 <= T n SZ <= 21 then x = (25 - T n SZ) BaseAddr[PAsize-1: x ]:IA[ x +38:42]: 0b000             | if SL0==2 then if 12 <= T0SZ <= 21 then x = (25 - T0SZ) BaseAddr[PAsize-1: x ]:IA[ x +38:42]: 0b000             |
|              2 | if 22 <= T n SZ <= 34 then x = (38 - T n SZ) else x = 16 BaseAddr[PAsize-1: x ]:IA[ x +25:29]: 0b000 | if SL0==1 then if 18 <= T0SZ <= 34 then x = (38 - T0SZ) else x = 16 BaseAddr[PAsize-1: x ]:IA[ x +25:29]: 0b000 |
|              3 | if 35 <= T n SZ <= 47 then x = (51 - T n SZ) else x = 16 BaseAddr[PAsize-1: x ]:IA[ x +12:16]: 0b000 | if SL0==0 then if 31 <= T0SZ <= 47 then x = (51 - T0SZ) else x = 16 BaseAddr[PAsize-1: x ]:IA[ x +12:16]: 0b000 |

## D8.2.11 Translation using the VMSAv9-128 translation system

RTZZMT All statements in this section and subsections require a translation stage use the VMSAv9-128 translation system.

RKWKRB

For a translation granule used in the VMSAv9-128 translation system, all of the following properties apply:

- The Stride is the minimum number of bits used to index a lookup level other than the initial lookup level.
- The minimum number of translation table entries at lookup levels other than the initial lookup level is 2 Stride .
- The number of address bits resolved by a Page descriptor at lookup level 3, PageIndex , is Stride+4 .

Those properties are shown in the following table.

Table D8-43 Translation granule properties at lookup levels other than the initial lookup level

| Translation granule   |   Minimum number of translation table entries |   Stride |   PageIndex |
|-----------------------|-----------------------------------------------|----------|-------------|
| 4KB                   |                                           256 |        8 |          12 |
| 16KB                  |                                          1024 |       10 |          14 |
| 64KB                  |                                          4096 |       12 |          16 |

## D8.2.11.1 Starting the VMSAv9-128 translation

The regular start level is determined by the translation granule size and the T n SZ fields in the corresponding TCR\_ELx, as shown in the following table:

Table D8-44 Regular start levels in the VMSAv9-128 translation system

| Translation granule   |   T n SZ maximum value |   T n SZ minimum value |   Regular start level |
|-----------------------|------------------------|------------------------|-----------------------|
| 4KB                   |                     11 |                      8 |                    -2 |
|                       |                     19 |                     12 |                    -1 |

| Translation granule   |   T n SZ maximum value |   T n SZ minimum value |   Regular start level |
|-----------------------|------------------------|------------------------|-----------------------|
|                       |                     27 |                     20 |                     0 |
|                       |                     35 |                     28 |                     1 |
|                       |                     43 |                     36 |                     2 |
|                       |                     48 |                     44 |                     3 |
| 16KB                  |                      9 |                      8 |                    -1 |
| 16KB                  |                     19 |                     10 |                     0 |
| 16KB                  |                     29 |                     20 |                     1 |
| 16KB                  |                     39 |                     30 |                     2 |
| 16KB                  |                     48 |                     40 |                     3 |
| 64KB                  |                     11 |                      8 |                     0 |
| 64KB                  |                     23 |                     12 |                     1 |
| 64KB                  |                     35 |                     24 |                     2 |
| 64KB                  |                     47 |                     36 |                     3 |

RDBQZN

When a translation table walk begins, the start level is determined by adding the value of the TTBR\_ELx.SKL field to the regular start level.

RFYTMS If the start level is greater than 3, a level 0 Translation fault is generated.

Note

This can be due to misprogramming the TTBR\_ELx.SKL and TCR\_ELx.{TG n , T n SZ} fields.

IJHGNJ When stage 2 uses the VMSAv9-128 translation system, the VTCR\_EL2.{SL2, SL0} and VSTCR\_EL2.{SL2, SL0}

fields are RES0.

For a translation granule, the properties of the start level translation table and the start level address are calculated using of all of the following information:

- The translation table base address, BaseAddr , in TTBR\_ELx.BADDR.
- The IA supplied to the translation and used as an index into the start level translation table.
- The permitted range of values for TCR\_ELx.T n SZ.
- The translation granule Stride value.
- The translation table base address register SKL value.

RJXBPC The number of address bits resolved by the table walk process, X , is 64-TnSZ-PageIndex .

RZZDZK The number of address bits resolved at all lookup levels other than the start level, Y , is (3-start level)*Stride

RCNZNY The number of address bits resolved at the start level, Z , is X-Y .

RYQVMK

The size of the start level translation table is 2 Z x16 bytes.

RTBNJK The start level address used to fetch the first descriptor is determined by appending BaseAddr to an index determined from the IA supplied to the translation stage, as follows:

- Start level address = BaseAddr[55:Z+4]:IA[64-TnSZ-1:64-TnSZ-Z]:0b0000 .

RPMSLB

If the high order start level address bits greater than the OA size are not 0, then an Address size fault is generated at level 0.

IDHBWG

.

RQYWCB

## D8.2.11.2 Continuing the VMSAv9-128 translation

| R DZXSB   | When a Table descriptor is returned at the current lookup level and does not generate an MMUfault, the translation table walk continues to the next lookup level .   |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R RCJXL   | The number of address bits resolved by all remaining lookup levels, K , is (3-current lookup level)*Stride .                                                         |
| R CWNTJ   | The next lookup level is current lookup level + 1 + Table descriptor SKL field .                                                                                     |
| R FSZKG   | The number of address bits resolved at the next lookup level, N , is (SKL+1)*Stride .                                                                                |
| R ZRZLX   | The size of the next level translation table is 2 N x16 bytes, determined according to the following table:                                                          |

## Table D8-45 Next level translation table sizes

| Translation granule   |   Descriptor SKL field | Translation table size   |
|-----------------------|------------------------|--------------------------|
| 4KB                   |                      0 | 4KB                      |
| 4KB                   |                      1 | 1MB                      |
| 4KB                   |                      2 | 256MB                    |
| 4KB                   |                      3 | 64GB                     |
| 16KB                  |                      0 | 16KB                     |
| 16KB                  |                      1 | 16MB                     |
| 16KB                  |                      2 | 16GB                     |
| 16KB                  |                      3 | Invalid descriptor       |
| 64KB                  |                      0 | 64KB                     |
| 64KB                  |                      1 | 256MB                    |
| 64KB                  |                      2 | 1TB                      |
| 64KB                  |                      3 | Invalid descriptor       |

Note

For each translation granule, the list of translation table sizes in Table D8-45 is the same as the list of supported block and page sizes in Table D8-46, although the table sizes are not limited to specific lookup levels.

If the size of the next level table is greater than the permitted translation table size, then a Translation fault at the current lookup level is generated. See Table D8-46.

RKMLSH The next level address used to fetch the next descriptor is determined by appending the next level table address to an index determined from the IA supplied to the translation stage, as follows:

- Next level address = Next level table address[55:N+4]:IA[K+Pageindex-1:K+PageIndex-N]:0b0000 .

If the high order next level address bits greater than the OA size are not 0, then an Address size fault is generated at the current lookup level.

## D8.2.11.3 Completing the VMSAv9-128 translation

When a Block or Page descriptor is returned at the current lookup level, the translation table walk completes and the current lookup level is the final lookup level .

For the VMSAv9-128 translation system, a translation resolved by a Block or Page descriptor has all of the properties shown in the following table. In this table, all of the following apply:

RRNCRQ

RWXRFL

RMYHXN

- OAbase (OAB) is the OA supplied by the descriptor at the final lookup level.
- IA is the IA supplied to the translation stage.
- Final address is the OA supplied by the translation stage.

## Table D8-46 Block and Page descriptor properties in the VMSAv9-128 translation system

| Translation Granule   |   Lookup level | Supported block or page size   | Final address       |
|-----------------------|----------------|--------------------------------|---------------------|
| 4KB                   |              0 | 64GB block                     | OAB[55:36]:IA[35:0] |
| 4KB                   |              1 | 256MB block                    | OAB[55:28]:IA[27:0] |
| 4KB                   |              2 | 1MBblock                       | OAB[55:20]:IA[19:0] |
| 4KB                   |              3 | 4KB page                       | OAB[55:12]:IA[11:0] |
| 16KB                  |              1 | 16GB block                     | OAB[55:34]:IA[33:0] |
| 16KB                  |              2 | 16MB block                     | OAB[55:24]:IA[23:0] |
| 16KB                  |              3 | 16KB page                      | OAB[55:14]:IA[13:0] |
| 64KB                  |              1 | 1TB block                      | OAB[55:40]:IA[39:0] |
| 64KB                  |              2 | 256MB block                    | OAB[55:28]:IA[27:0] |
| 64KB                  |              3 | 64KB page                      | OAB[55:16]:IA[15:0] |

RBFVYY

For the final address supplied by a translation stage, if the address bits above the OA size are not set to zero, then an Address size fault is generated at the current lookup level.

## D8.2.12 The effects of disabling an address translation stage

IHBZJC

RPPDBS

Stage 1 and stage 2 translations can be disabled independently, and doing so affects the MMU behavior.

## D8.2.12.1 Behavior when stage 1 address translation is disabled

If stage 1 address translation is disabled, then all of the following apply to memory accesses that would otherwise be translated at stage 1:

- The stage 1 IA is flat mapped to the OA.
- No Translation faults, Access flag faults, or Permission faults can be generated.
- Address size faults and Alignment faults can be generated.
- No memory is guarded.
- The access is to one of the following IPA or PA spaces:
- -For accesses from Non-secure state, the access is to Non-secure IPA or PA space.
- -For accesses from Secure state, the access is to Secure IPA or PA space.
- -For accesses from Realm state, the access is to Realm IPA or PA space.
- -For accesses from Root state, the access is to Root PA space.

RWFZPW If stage 1 address translation is disabled, then the stage 1 translation assigns one of the following attributes to memory accesses:

- For memory accesses using the EL1&amp;0 regime, if the effective value of HCR\_EL2.DC is 1, then all of the following memory attributes are assigned:
- -The Tagged attribute is set according to HCR\_EL2.DCT.
- -Normal Inner Write-Back Cacheable Read-Allocate Write-Allocate.
- -Normal Outer Write-Back Cacheable Read-Allocate Write-Allocate.
- -Non-shareable.
- -If FEAT\_XS is implemented, then the XS attribute is set to 0.
- For all other memory accesses, one of the following memory attributes are assigned:

- -For a data access, the Device-nGnRnE memory attribute.
- -For an instruction access, the Normal memory attribute and one of the following:
- -If SCTLR\_ELx.I is 0, then the Non-cacheable and Outer Shareable attributes.
- -If SCTLR\_ELx.I is 1, then the Cacheable, Inner Write-Through Read-Allocate No Write-Allocate, Outer Write-Through Read-Allocate No Write-Allocate Outer Shareable attribute.
- -For data accesses and instruction accesses, if FEAT\_XS is implemented, then the XS attribute is set to 1.

RCSDNK If all of the following apply, then the stage 1 memory attribute assignments and OA can be modified by the stage 2 translation:

- EL1&amp;0 stage 2 address translation is enabled.
- An access using the EL1&amp;0 translation regime occurs.
- RLBPTY If HCR\_EL2.DC is 1, then all of the following apply:
- For all purposes other than reading the value of the bit, the Effective value of SCTLR\_EL1.M is 0, disabling stage 1 address translation in the EL1&amp;0 translation regime.
- If EL2 is enabled, then for all purposes other than reading the value of the bit, the Effective value of HCR\_EL2.VM is 1, enabling stage 2 address translation in the EL1&amp;0 translation regime.

## D8.2.12.2 Behavior when stage 2 address translation is disabled

RQVLSD If stage 2 address translation is disabled, then all of the following apply to memory accesses that would otherwise be translated at stage 2:

- No stage 2 MMU faults can be generated.
- The IPA is flat mapped to the PA.
- The memory attributes and permissions assigned by the stage 1 translation are assigned to the PA.
- The access is to one of the following PA spaces:
- -For accesses from the Non-secure IPA space, the access is to the Non-secure PA space.
- -For accesses from the Secure IPA space, the access is to the Secure PA space.
- -For accesses from the Realm IPA space, the access is to the Realm PA space.

## D8.2.12.3 Instruction fetch behavior when all translation stages are disabled

IDLNTB If all associated address translation stages are disabled, then software is required to place instructions that will be executed in memory regions where those regions and the memory regions immediately following each have all the following properties:

- The memory region size is equal to the minimum implemented translation granule size.
- The memory region is tolerant to speculative accesses.
- The memory region is naturally aligned.
- RWLVZN If execution is in AArch64 state and all associated address translation stages are disabled, a memory location might be accessed as a result of an instruction fetch, including a speculative instruction fetch, in all of the following cases:
- The memory location is in the same memory region, or in the next contiguous memory region, as an instruction that simple sequential program execution either requires to be fetched now or has required to be fetched since the last reset.
- The memory location is the target of a direct branch that simple sequential program execution would have taken since the most recent of one of the following:
- -The last reset.
- -The last synchronization of instruction cache maintenance targeting the branch instruction address.
- IFZQCN If all address translation stages are disabled, then speculative instruction fetches can cause unintended memory location accesses, regardless of whether the fetched instruction is committed to execution.

## D8.2.12.4 Effect of disabling address translation on maintenance and address translation instructions

RSJBMV

Cache maintenance instructions act on the target location regardless of all of the following:

- Whether or not any address translation stages are disabled.

- The memory attribute values.

RZSSPZ

For an address translation stage that is disabled, cache maintenance instructions use flat address mapping.

RFZYGN

If an address translation stage is disabled, TLB maintenance operations are not affected.

IHRNPD

For more information, see:

- A64 Cache maintenance instructions.

- Address translation instructions.

- TLB maintenance instructions.

## D8.2.13 Address translation instructions

ITMFCK

Address translation instructions return the result of translating an IA using a specified translation stage or regime.

IBDZFF

An address translation instruction has all of the following properties:

- An IA is supplied as the argument to the instruction.
- The instruction encoding determines the translation stage and regime used by the translation.
- The PAR\_EL1 register is updated with the translation result.
- For the security state of the instruction as selected by SCR\_EL3.{NSE, NS}, the architecture guarantees all of the following:
- -If executed in Non-secure state, then no result is returned from a Secure, Realm, or Root address translation stage.
- -If executed in Secure state, then no result is returned from a Realm or Root address translation stage.
- -If executed in Realm state, then no result is returned from a Secure or Root address translation stage.
- If an address translation stage is controlled by a higher Exception level than the Exception level at which the address translation instruction is executed, then the instruction is UNDEFINED.

ICSYQZ If FEAT\_MTE2 is enabled, then the results of AT* instructions reflect whether the translation is Tagged or Untagged. For more information, see Memory region tagging types.

ITSJPJ

The A64 assembly language syntax of an address translation instruction is AT &lt;operation&gt;, &lt;Xt&gt; .

IPRNLQ

ICQWJY

The &lt;operation&gt; in AT &lt;operation&gt;, &lt;Xt&gt; is one of the following:

- S1E1R , S1E1W , S1E0R , S1E0W , S12E1R , S12E1W , S12E0R , S12E0W , S1E2R , S1E2W , S1E3R , or S1E3W .
- If FEAT\_PAN2 is implemented, then S1E1WP or S1E1RP .
- If FEAT\_ATS1A is implemented, then S1E1A , S1E2A, or S1E3A .

The &lt;operation&gt; in AT &lt;operation&gt;, &lt;Xt&gt; has a structure of &lt;stages&gt;&lt;el&gt;(&lt;read|write&gt;{&lt;pan&gt;})|&lt;ignore&gt; with all of the following components:

- &lt;stages&gt; is one of the following address translation stages:
- -S1 specifies a stage 1 translation.
- -S12 specifies a stage 1 translation followed by a stage 2 translation.
- &lt;el&gt; is one of the following Exception levels that apply to the translation:
- -E0 specifies EL0.
- -E1 specifies EL1.
- -E2 specifies EL2.
- -E3 specifies EL3.
- &lt;read|write&gt; is one of the following:
- -R specifies Read.
- -W specifies Write.

- If FEAT\_PAN2 is implemented, then the &lt;pan&gt; component is included and has all of the following properties:
- -P determines whether the PSTATE.PAN value is considered when determining permissions. For more information, see PSTATE.PAN.
- -The field is optional.
- -If &lt;stages&gt; = S1 and &lt;el&gt; = E1 , the field is permitted.
- -If &lt;stages&gt; != S1 or &lt;el&gt; != E1 , the field is not permitted.
- If FEAT\_ATS1A is implemented, then the &lt;ignore&gt; component is included and has all of the following properties:
- -A specifies that the permission checks are ignored.
- -The field is optional.
- -If this field is specified, the &lt;read|write&gt; and &lt;pan&gt; fields are not permitted.

IXLYWF If &lt;el&gt; is higher than the current Exception level, then the address translation instruction is UNDEFINED.

ISYHWD The &lt;Xt&gt; in AT &lt;operation&gt;, &lt;Xt&gt; specifies the 64-bit register holding the address to be translated.

IGSXHM When an address translation instruction applies to a translation regime that is using AArch32, V A[63:32] is RES0.

RNJGLC When an address is translated by an address translation instruction, no alignment restrictions exist and therefore an address translation instruction cannot generate an Alignment fault.

ILRNWF

Execution of an AT instruction may result in a successful translation reported in PAR\_EL1, an MMU fault being reported in PAR\_EL1, or an MMU fault generating an exception.

For more information see:

- MMUfaults generated by address translation instructions
- Address translation instructions, successful address translation
- RNWDPJ When an address translation instruction is executed, the specified translation stage and regime determines all of the following:
- The entries in TLB caching structures that are permitted to be used.
- How the translation table walk is done.

RNPZWX When an address translation instruction is executed, it is IMPLEMENTATION DEFINED whether the result can be returned from a TLB, or a translation table walk occurs.

IWGXJK

If TLB entries might differ from the underlying translation tables held in memory, such as when waiting for a maintenance or synchronization event to complete after updating the translation tables, Arm recommends not using the address translation instructions.

## D8.2.13.1 Address translation instructions, successful address translation

RLRYRY When an address translation instruction successfully translates an address, all of the following are updated in PAR\_EL1:

- PAR\_EL1.F is set to 0.
- The resulting OA is returned in PAR\_EL1.PA, and the resulting attributes are returned in the other fields of PAR\_EL1.

When populating PAR\_EL1 with the result of an address translation instruction, the fetches of stage 1 or stage 2

IPVCPF descriptors use the appropriate MECID register values for the translation regime.

IQKWHX The architecture defines a single PAR, PAR\_EL1, that is used regardless of all of the following:

- The Exception level at which the address translation instruction was executed.
- The Exception level that controls the address translation stage or stages used by the address translation instruction.

RYLPDG If single-stage address translation instructions, ATS1* , target the VMSAv9-128 translation system, then they report their result using the 128-bit format of PAR\_EL1.

RXVCRF

If one of the following is true, then ATS12* instructions report their result using the 128-bit format of PAR\_EL1:

- Stage 2 of the target translation system is enabled and the stage 2 translation system uses VMSAv9-128.
- Stage 2 of the target translation system is disabled and the stage 1 translation system uses VMSAv9-128. Otherwise, the 64-bit format of PAR\_EL1 is used.

## D8.2.13.2 Address translation instructions, effect of translation regime

RFKTKP

If EL2 is disabled or not implemented, the AT S1E2R, AT S1E2W, and AT S1E2A instructions are UNDEFINED.

RNYXTL

If EL3 is implemented, then when an address translation instruction that applies to an Exception level lower than EL3 is executed, the Effective value of SCR\_EL3.{NSE, NS} determines the target Security state that the instruction applies to, as shown in the following table:

| NSE, NS   | Security State           |
|-----------|--------------------------|
| 0, 0      | Secure                   |
| 0, 1      | Non-secure               |
| 1, 0      | Instruction is UNDEFINED |
| 1, 1      | Realm                    |

RRKBPZ

RPXNSR

IKJDTT

IJTYVP

IPCPWC

If EL3 is implemented and EL2 is disabled or not implemented for the target Security state, then all of the following apply to the AT S12E** instruction behavior:

- The instruction has the same behavior as the equivalent AT S1E** instruction.
- The instruction behaves consistently with an implementation that has all of the following characteristics:
- -EL2 is implemented.
- -Stage 2 translation is disabled.

If the Effective value of SCR\_EL3.{NSE, NS} is {0, 0} and Secure EL2 is disabled or not implemented, then executing the following AT instructions at EL3 is UNDEFINED:

- AT S1E2R.
- AT S1E2W.
- AT S1E2A.

The value of HCR\_EL2.DC affects all of the following instructions:

- AT S1E0* .
- AT S1E1* .
- AT S12E0* .
- AT S12E1* .

## D8.2.13.3 Address translation instructions, synchronization requirements

When an address translation instruction is executed, explicit synchronization is required to guarantee the result is visible to subsequent direct reads of PAR\_EL1.

For more information, see Synchronization requirements for AArch64 System registers.

Requiring explicit synchronization after executing an address translation instruction is consistent with the general requirement that the effect of a write to a System register requires explicit synchronization before the result is guaranteed to be visible to subsequent instructions.