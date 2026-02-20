## D8.1 Address translation

RDWFWP If an implementation is executing in AArch64 state, then that implementation uses either or both of the VMSAv8-64 and the VMSAv9-128 translation systems.

RRKHJV

ICCTQS

All of the following determine whether a translation stage uses the VMSAv9-128 translation system:

- For stage 1 translations in the EL1&amp;0 translation regime, the Effective value of TCR2\_EL1.D128 is 1.
- For stage 1 translations in the EL2&amp;0 translation regime, the Effective value of TCR2\_EL2.D128 is 1.
- For stage 1 translations in the EL3 translation regime, the Effective value of TCR\_EL3.D128 is 1.
- For stage 2 translations, the Effective value of VTCR\_EL2.D128 is 1.

Otherwise, the translation stage uses the VMSAv8-64 translation system.

This applies even when the translation stage is disabled.

Address translation converts the addresses used by instructions to the addresses used by the physical memory system.

RCRPHV (VA). This includes any

When a data address or instruction address is used in an instruction, it is a virtual address address stored in one of the following registers:

- Program counter (PC).
- Stack pointers (SP).
- Link register (LR).
- Exception link register (ELR).

RCRDGS When an access is made to the physical memory system, a physical address (PA) is used.

RKCNRX An address translation maps a V A to a PA.

RCCCQQ

An address translation requires one of the following:

- Asingle translation stage, stage 1.
- Two sequential translation stages, stage 1 and stage 2.

RZKJWW An address translation stage maps an input address (IA) to an output address (OA).

RBCKLH If one address translation stage is used, then a V A is mapped to a PA using all of the following steps:

1. The VA is input as the IA to the translation stage.
2. The PA is output as the OA from the translation stage.

If two address translation stages are used, then a V A is mapped to a PA using all of the following steps:

1. The VA is input as the IA to the stage 1 translation.
2. The intermediate physical address (IPA) is output as the OA from the stage 1 translation.
3. The IPA is input as the IA to the stage 2 translation.
4. The PA is output as the OA from the stage 2 translation.

IMBNVX If an address translation stage is disabled, then the value of the OA is the same as the IA.

IYXNZL When an IA is translated to an OA, an address translation stage uses a set of memory mapped translation tables that hold all of the following information:

- The OA corresponding to the IA.
- For accesses made from Secure state, whether the OA access is to the Secure or Non-secure address map.
- The OA memory access permissions.
- The OA memory region attributes.

IFJFQR When an IA is translated by an address translation stage, all of the following apply:

- Atranslation table lookup reads an entry from a translation table.
- Atranslation table entry resolves a subset of the IA.
- Multiple translation table entries can be required to completely resolve an IA.

RKXSMJ

- An address translation can require multiple lookups across different lookup levels and multiple translation tables.

RJTYJP

When memory is accessed, the Memory Management Unit (MMU) controls address translation, memory access permissions, memory attribute determination, and memory attribute checking.

RRJPRG

When the MMU cannot translate the IA, an MMU fault is generated.

RFLRHM

When an address translation stage generates an MMU fault, it is one of the following:

- When a stage 1 translation cannot translate an IA, a stage 1 MMU fault is generated.

- When a stage 2 translation cannot translate an IA, a stage 2 MMU fault is generated.

IZWCKD

For more information, see:

- Implemented physical address size.

- Output address size configuration.

- Supported virtual address ranges.

- Input address size configuration.

- Intermediate physical address size configuration.

- Translation process.

- The effects of disabling an address translation stage.

- Memory aborts

## D8.1.1 Translation granules

| I GZDPY   | The translation granule size determines the number of bits resolved by each lookup level when mapping from an IA to OA, and the maximum size of a single translation table.                                                                                                                                                                                                                                                      |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R ZVQXW   | The VMSAdefines all of the following translation granule sizes: • 4KB. • 16KB. • 64KB.                                                                                                                                                                                                                                                                                                                                           |
| R JZCBC   | For each translation granule size, and translation stage, support is IMPLEMENTATION DEFINED.                                                                                                                                                                                                                                                                                                                                     |
| R VKNXT   | Each address translation stage can be independently configured to use one of the supported translation granule sizes.                                                                                                                                                                                                                                                                                                            |
| R QKCFY   | Apage is the smallest memory region in which an IA to OAmapping can be specified.                                                                                                                                                                                                                                                                                                                                                |
| I MGPLT   | The translation granule determines all of the following: • The translation process used to resolve an IA to an OA. • The page size of the address translation stage. • The number of address bits required to address a page. • The maximum translation table size of the address translation stage. • The number of address bits that can be resolved in a single translation table lookup.                                     |
| I KZLYC   | For all of the following reasons, a larger translation granule can reduce the number of translation lookup levels: • The larger granule uses a larger translation table with more entries. • Asingle lookup can resolve more IA bits. • The larger page size means more of the least significant address bits are used to address within a page and do not require translation because those bits are flat-mapped from IA to OA. |
| I QRLDB   | Arm recommends separating memory-mapped peripherals by an integer multiple of the largest granule size supported the PEs in the system, to allow independent management of each peripheral.                                                                                                                                                                                                                                      |
| I XKKTX   | If FEAT_GTG is not implemented, then the ID_AA64MMFR0_EL1.{TGran4, TGran16, TGran64} fields specify the translation granules supported in both stage 1 and stage 2 translations.                                                                                                                                                                                                                                                 |

IFXFSZ

If FEAT\_GTG is implemented, then support for translation granule sizes are determined by all of the following:

- The ID\_AA64MMFR0\_EL1.{TGran4, TGran16, TGran64} fields specify the translation granules supported in stage 1 translations.
- The ID\_AA64MMFR0\_EL1.{TGran4\_2, TGran16\_2, TGran64\_2} fields specify the translation granules supported in stage 2 translations.

## D8.1.2 Translation regimes

ICJMWY

Atranslation regime determines how a VA is mapped to a PA. The translation regime is affected by the current Security state, the current Exception level, the enabled Exception levels, HCR\_EL2 settings, and implemented features.

IHLQTD

The architecture defines all of the following translation regimes:

- Non-secure EL1&amp;0 translation regime.
- Secure EL1&amp;0 translation regime.
- Realm EL1&amp;0 translation regime.
- Non-secure EL2&amp;0 translation regime.
- Secure EL2&amp;0 translation regime.
- Realm EL2&amp;0 translation regime.
- Non-secure EL2 translation regime.
- Secure EL2 translation regime.
- Realm EL2 translation regime.
- EL3 translation regime.

IDQHFH

The implemented Exception levels affect the supported translation regimes and translation stages.

RFVYPX

For each Security state, configuration of stage 1 and stage 2 translation can produce output addresses only in physical address spaces marked as YES in the following table:

Table D8-1 Relationship between Security state and permitted PA space

| PA space   | Non-secure state   | Secure state   | Realm state   | Root state   |
|------------|--------------------|----------------|---------------|--------------|
| Non-secure | Yes                | Yes            | Yes           | Yes          |
| Secure     | No                 | Yes            | No            | Yes          |
| Realm      | No                 | No             | Yes           | Yes          |
| Root       | No                 | No             | No            | Yes          |

RTSFYG

Only the EL1&amp;0 translation regimes support a stage 2 translation.

IDTPTJ

If a software agent, such as an operating system, uses or configures stage 1 translations, then that software agent might be unaware of all of the following:

- The stage 2 translation.

- The distinction between IPA and PA.

RZQYNV

If the Effective value of HCR\_EL2.E2H is 0, then only the EL1&amp;0 translation regime, stage 1, can support two V A ranges.

RQLSFG

If the Effective value of HCR\_EL2.E2H is 1, then the EL2&amp;0 translation regime, stage 1, can support two V A ranges.

IQCFSC

If a stage 1 translation supports two V A ranges, then that translation stage also supports two privilege levels.

IMZRPG

Support for execution in Realm state at EL0 in AArch32 is IMPLEMENTATION DEFINED. Use of the Realm translation regimes at EL0 in AArch32 depends on that support for AArch32 at EL0. Support for execution in Realm state at other Exception levels is available in AArch64 only.

RQJSCR

IFYLSZ

RDKYXN

RBTYVG

## D8.1.2.1 Non-secure EL1&amp;0 translation regime

If all of the following apply, then the Non-secure EL1&amp;0 translation regime is used to translate addresses:

- The memory accesses occur in Non-secure state.
- One of the following applies:
- -Memory is accessed from EL1.
- -Memory is accessed from EL0 and the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}.

RLLNVY If Non-secure EL2 is not implemented, then the Non-secure EL1&amp;0 translation regime has a single address translation stage, stage 1, that does all the following:

- Maps VAs to PAs.
- Supports two VA ranges and the use of ASIDs.

RPMRVM If Non-secure EL2 is implemented, then the Non-secure EL1&amp;0 translation regime supports all of the following:

- Translation stage 1 that does all the following:
- -Maps VAs to IPAs.
- -Supports two VA ranges and the use of ASIDs.
- Translation stage 2 that does all the following:
- -Maps stage 1 IPAs to PAs.
- -Supports a single IPA range.
- The translations are associated with a VMID.
- Translation stage 1 and translation stage 2 can be enabled independent of each other.

For more information, see Use of ASIDs and VMIDs to reduce TLB maintenance requirements.

Non-secure EL2 is effectively disabled if it is not implemented.

## D8.1.2.2 Secure EL1&amp;0 translation regime

If all of the following apply, then the Secure EL1&amp;0 translation regime is used to translate addresses:

- The memory accesses occur in Secure state.
- One of the following applies:
- -Memory is accessed from EL1.
- -Memory is accessed from EL0 and the Effective value of HCR\_EL2.{E2H,TGE} is not {1,1}.

RYTZXB If Secure EL2 is disabled or not implemented, then the Secure EL1&amp;0 translation regime has a single address translation stage, stage 1, that does all the following:

- Maps VAs to PAs.
- Supports two VA ranges and the use of ASIDs.

RJMRWC If Secure EL2 is enabled, then the Secure EL1&amp;0 translation regime, supports all of the following:

- Translation stage 1 that does all the following:
- -Maps VAs to IPAs.
- -Supports two VA ranges and the use of ASIDs.
- Translation stage 2 that does all the following:
- -Maps stage 1 IPAs to PAs.
- -Supports a single Non-secure IPA range and a single Secure IPA range.
- The translations are associated with a VMID.
- Translation stage 1 and translation stage 2 can be enabled independent of each other.

For more information, see Use of ASIDs and VMIDs to reduce TLB maintenance requirements.

## D8.1.2.3 Realm EL1&amp;0 translation regime

If all of the following apply, then the Realm EL1&amp;0 translation regime is used to translate addresses:

- The memory accesses occur in Realm state.
- One of the following applies:
- -Memory is accessed from EL1.

- Memory is accessed from EL0 and the Effective value of HCR\_EL2.{E2H,TGE} is not {1,1}.

RYXQTB The Realm EL1&amp;0 translation regime supports all of the following:

- Translation stage 1 that does all the following:

- Maps VAs to Realm InAs.

- Supports two VA ranges and the use of ASIDs.

- Translation stage 2 that does all the following:

- Supports one IPA range.

- Maps stage 1 Realm IPAs to Realm PAs or Non-secure PAs.

- The translation is associated with a VMID.

- The translations are associated with a VMID.

- Translation stage 1 and translation stage 2 can be enabled independent of each other.

For more information, see Use of ASIDs and VMIDs to reduce TLB maintenance requirements.

RHMWYX All features supported for the Non-secure EL1&amp;0 stage 1 translation regime are supported for the Realm EL1&amp;0 stage 1 translation regime.

RPDRZK All features supported for the Non-secure EL1&amp;0 stage 2 translations are supported for Realm EL1&amp;0 stage 2 translations.

## D8.1.2.4 Non-secure EL2&amp;0 translation regime

RKBSNT If all of the following apply, then the Non-secure EL2&amp;0 translation regime is used to translate addresses:

- The memory accesses occur in Non-secure state.

- One of the following applies:

- The Effective value of HCR\_EL2.{E2H, TGE} is {1, 0} and memory accesses are from EL2.

- The Effective value of HCR\_EL2.{E2H, TGE} is {1, 1} and memory accesses are from EL2 or EL0.

For more information, see Virtualization Host Extensions.

RMNQBD

The Non-secure EL2&amp;0 translation regime has a single address translation stage, stage 1, that does all the following:

- Maps VAs to PAs.

- Supports two VA ranges and the use of ASIDs.

For more information, see Use of ASIDs and VMIDs to reduce TLB maintenance requirements.

ILKPNM The Non-secure EL2&amp;0 regime might also be used when execution is at EL1, and in some cases at EL0 when HCR\_EL2.{E2H, TGE} is not {1, 1}. For example:

- At EL1 when FEAT\_NV2 is in use, as described in Loads and stores generated by transforming register accesses.

- At EL1 or EL0 when the Statistical Profiling Unit is enabled, as described in The owning translation regime.

- At EL1 or EL0 when the Trace Buffer Extension is enabled, as described in The owning translation regime.

## D8.1.2.5 Secure EL2&amp;0 translation regime

RRJHRJ

If all of the following apply, then the Secure EL2&amp;0 translation regime is used to translate addresses:

- The Effective value of SCR\_EL3.EEL2 is 1.

- The memory accesses occur in Secure state.

- One of the following applies:

- The Effective value of HCR\_EL2.{E2H, TGE} is {1, 0} and memory accesses are from EL2.

- The Effective value of HCR\_EL2.{E2H, TGE} is {1, 1} and memory accesses are from EL2 or EL0.

For more information, see Virtualization Host Extensions.

RRRQTL The Secure EL2&amp;0 translation regime has a single address translation stage, stage 1, that does all the following:

- Maps VAs to Secure PAs or Non-secure PAs.

- Supports two VA ranges and the use of ASIDs.

For more information, see Use of ASIDs and VMIDs to reduce TLB maintenance requirements.

ILLMSY

The Secure EL2&amp;0 regime might also be used when execution is at EL1, and in some cases at EL0 when HCR\_EL2.{E2H, TGE} is not {1, 1}. For example:

- At EL1 when FEAT\_NV2 is in use, as described in Loads and stores generated by transforming register accesses.

- At EL1 or EL0 when the Statistical Profiling Unit is enabled, as described in The owning translation regime.

- At EL1 or EL0 when the Trace Buffer Extension is enabled, as described in The owning translation regime.

RJYGWW

RPMTLC

RLCPJJ

RGFVNF

IZGLNV

RFMHTT

RWYXPT

## D8.1.2.6 Realm EL2&amp;0 translation regime

If all of the following apply, then the Realm EL2&amp;0 translation regime is used to translate addresses:

- The memory accesses occur in Realm state.
- One of the following applies:
- -The Effective value of HCR\_EL2.{E2H, TGE} is {1, 0} and memory accesses are from EL2.
- -The Effective value of HCR\_EL2.{E2H, TGE} is {1, 1} and memory accesses are from EL2 or EL0.

For more information, see Virtualization Host Extensions.

The Realm EL2&amp;0 translation regime has a single address translation stage, stage 1, that does all the following:

- Maps VAs to Realm PAs or Non-secure PAs.
- Supports two VA ranges and the use of ASIDs.

For more information, see Use of ASIDs and VMIDs to reduce TLB maintenance requirements.

## D8.1.2.7 Non-secure EL2 translation regime

If all of the following apply, then the Non-secure EL2 translation regime is used to translate addresses:

- The memory accesses occur in Non-secure state.
- The Effective value of HCR\_EL2.E2H is 0.
- Memory is accessed from EL2.

RPYJCB The Non-secure EL2 translation regime has a single address translation stage, stage 1, that does all the following:

- Maps VAs to PAs.
- Supports a single V A range.

IRRDHX The Non-secure EL2 regime might also be used when execution is at EL1, and in some cases at EL0 when HCR\_EL2.{E2H, TGE} is not {1, 1}. For example:

- At EL1 when FEAT\_NV2 is in use, as described in Loads and stores generated by transforming register accesses.
- At EL1 or EL0 when the Statistical Profiling Unit is enabled, as described in The owning translation regime.
- At EL1 or EL0 when the Trace Buffer Extension is enabled, as described in The owning translation regime.

## D8.1.2.8 Secure EL2 translation regime

If all of the following apply, then the Secure EL2 translation regime is used to translate addresses:

- The Effective value of SCR\_EL3.EEL2 is 1.
- The memory accesses occur in Secure state.
- The Effective value of HCR\_EL2.E2H is 0.
- Memory is accessed from EL2.

RCTSYJ The Secure EL2 translation regime has a single address translation stage, stage 1, that does all the following:

- Maps VAs to Secure PAs or Non-secure PAs.
- Supports a single V A range.

The Secure EL2 regime might also be used when execution is at EL1, and in some cases at EL0 when HCR\_EL2.{E2H, TGE} is not {1, 1}. For example:

- At EL1 when FEAT\_NV2 is in use, as described in Loads and stores generated by transforming register accesses.
- At EL1 or EL0 when the Statistical Profiling Unit is enabled, as described in The owning translation regime.
- At EL1 or EL0 when the Trace Buffer Extension is enabled, as described in The owning translation regime.

## D8.1.2.9 Realm EL2 translation regime

If all of the following apply, then the Realm EL2 translation regime is used to translate addresses:

- The memory accesses occur in Realm state.
- The Effective value of HCR\_EL2.E2H is 0.
- Memory is accessed from EL2.

The Realm EL2 translation regime has a single address translation stage, stage 1, that does all the following:

- Maps VAs to Realm PAs or Non-secure PAs.
- Supports a single V A range.

## D8.1.2.10 EL3 translation regime

RPCRZX

If memory is accessed from EL3, then the EL3 translation regime is used to translate addresses.

- RDCCTQ

The EL3 translation regime has a single address translation stage, stage 1, that does all the following:

- Maps VAs to PAs in all supported PA spaces.

- Supports a single V A range.

## D8.1.3 Relationship between translation regimes and implemented Exception levels

| I VNQXD   | The set of translation regimes that an implementation supports depend on the set of Exception levels that the implementation supports.                      |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R GFKSR   | If an implementation does not include EL2, then all of the following apply:                                                                                 |
|           | • If the implementation does not include EL3, then the MMUprovides a single EL1&0 stage 1 translation regime with an IMPLEMENTATION DEFINED Security state. |
|           | • If the implementation includes EL3, then the MMUprovides an EL1&0 stage 1 translation regime in each Security state.                                      |
| R RJWCS   | For each translation stage supported by a translation regime, the following table shows what is required to support that translation stage.                 |

Table D8-2 Translation regimes, translation stages, and associated controls

| Translation stage        | Requires                                                                                                                                                                        |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Non-secure EL2 stage 1   | EL2 is implemented and EL2 uses AArch64. The Effective value of SCR_EL3.{NSE, NS} is {0, 1}. The Effective value of HCR_EL2.E2H is 0.                                           |
| Non-secure EL2&0 stage 1 | EL2 is implemented and EL2 uses AArch64. The Effective value of SCR_EL3.{NSE, NS} is {0, 1}. The Effective value of HCR_EL2.E2H is 1.                                           |
| Non-secure EL1&0 stage 2 | EL2 is implemented and EL2 uses AArch64. The Effective value of SCR_EL3.{NSE, NS} is {0, 1}.                                                                                    |
| Non-secure EL1&0 stage 1 | EL1 uses AArch64. The Effective value of SCR_EL3.{NSE, NS} is {0, 1}.                                                                                                           |
| Secure EL2 stage 1       | EL2 is implemented and EL2 uses AArch64. The Effective value of SCR_EL3.EEL2 is 1. The Effective value of SCR_EL3.{NSE,NS} is {0, 0}. The Effective value of HCR_EL2.E2H is 0.  |
| Secure EL2&0 stage 1     | EL2 is implemented and EL2 uses AArch64. The Effective value of SCR_EL3.EEL2 is 1. The Effective value of SCR_EL3.{NSE, NS} is {0, 0}. The Effective value of HCR_EL2.E2H is 1. |
| Secure EL1&0 stage 2     | EL2 is implemented and EL2 uses AArch64. The Effective value of SCR_EL3.EEL2 is 1. The Effective value of SCR_EL3.{NSE, NS} is {0, 0}.                                          |
| Secure EL1&0 stage 1     | EL1 uses AArch64. The Effective value of SCR_EL3.{NSE, NS} is {0, 0}.                                                                                                           |
| Realm EL2 stage 1        | FEAT_RME is implemented. SCR_EL3.{NSE, NS} is {1, 1}. The Effective value of HCR_EL2.E2H is 0.                                                                                  |

| Translation stage   | Requires                                                                                       |
|---------------------|------------------------------------------------------------------------------------------------|
| Realm EL2&0 stage 1 | FEAT_RME is implemented. SCR_EL3.{NSE, NS} is {1, 1}. The Effective value of HCR_EL2.E2H is 1. |
| Realm EL1&0 stage 2 | FEAT_RME is implemented. SCR_EL3.{NSE, NS} is {1, 1}.                                          |
| Realm EL1&0 stage 1 | FEAT_RME is implemented. SCR_EL3.{NSE, NS} is {1, 1}.                                          |
| EL3 stage 1         | EL3 is implemented and EL3 uses AArch64.                                                       |

RVDVPR

RWNBMG

For a stage 1 translation, if EL0 uses AArch32 state and one or more of the following applies, then VMSAv8-64 translation is required:

- EL1 uses AArch64 and the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}.
- EL2 uses AArch64 and the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}.

For a stage 2 translation, if either EL1 or EL0 uses AArch32 state and EL2 uses AArch64, then VMSAv8-64 translation is required.

- RKXSWD If EL0 uses AArch32, then accesses from EL0 have all of the following properties:
- Accesses use the EL1&amp;0 or EL2&amp;0 translation regime.
- Accesses use the AArch32 application-level memory model.
- Accesses are limited to a 32-bit V A range.

For more information, see The AArch64 Application Level Programmers' Model.

IMQXXQ

## D8.1.4 The system registers relevant to MMU operation

IRJZKJ

If a System register name has a numeric suffix, then the suffix indicates the lowest Exception level that can access the register.

- ITNCZR Translation stages are enabled and controlled by the registers specified in the following table.

Table D8-3 Registers that enable and control translation stages

| Translation Stage        | Controlled from   | Controlling registers                                                                                                        |
|--------------------------|-------------------|------------------------------------------------------------------------------------------------------------------------------|
| Non-secure EL2 stage 1   | Non-secure EL2    | SCTLR_EL2, SCTLR2_EL2, TCR_EL2, TCR2_EL2, MAIR_EL2, MAIR2_EL2, AMAIR_EL2, AMAIR2_EL2, TTBR0_EL2                              |
| Non-secure EL2&0 stage 1 | Non-secure EL2    | SCTLR_EL2, SCTLR2_EL2, TCR_EL2, TCR2_EL2, MAIR_EL2, MAIR2_EL2, AMAIR_EL2, AMAIR2_EL2, TTBR0_EL2, TTBR1_EL2, HCR_EL2          |
| Non-secure EL1&0 stage 2 | Non-secure EL2    | SCTLR_EL2, SCTLR2_EL2, VTCR_EL2, VTTBR_EL2, HCR_EL2                                                                          |
| Non-secure EL1&0 stage 1 | Non-secure EL1    | SCTLR_EL1, SCTLR2_EL1, TCR_EL1, TCR2_EL1, MAIR_EL1, MAIR2_EL1, AMAIR_EL1, AMAIR2_EL1, TTBR0_EL1, TTBR1_EL1, HCR_EL2          |
| Secure EL2 stage 1       | Secure EL2        | SCTLR_EL2, SCTLR2_EL2, TCR_EL2, TCR2_EL2, MAIR_EL2, MAIR2_EL2, AMAIR_EL2, AMAIR2_EL2, TTBR0_EL2, SCR_EL3                     |
| Secure EL2&0 stage 1     | Secure EL2        | SCTLR_EL2, SCTLR2_EL2, TCR_EL2, TCR2_EL2, MAIR_EL2, MAIR2_EL2, AMAIR_EL2, AMAIR2_EL2, TTBR0_EL2, TTBR1_EL2, HCR_EL2, SCR_EL3 |

| Translation Stage    | Controlled from   | Controlling registers                                                                                                        |
|----------------------|-------------------|------------------------------------------------------------------------------------------------------------------------------|
| Secure EL1&0 stage 2 | Secure EL2        | SCTLR_EL2, SCTLR2_EL2, VSTCR_EL2, VSTTBR_EL2, VTCR_EL2, VTTBR_EL2, HCR_EL2, SCR_EL3                                          |
| Secure EL1&0 stage 1 | Secure EL1        | SCTLR_EL1, SCTLR2_EL1, TCR_EL1, TCR2_EL1, MAIR_EL1, MAIR2_EL1, AMAIR_EL1, AMAIR2_EL1, TTBR0_EL1, TTBR1_EL1, HCR_EL2, SCR_EL3 |
| Realm EL2 stage 1    | Realm EL2         | SCTLR_EL2, SCTLR2_EL2, TCR_EL2, TCR2_EL2, MAIR_EL2, MAIR2_EL2, AMAIR_EL2, AMAIR2_EL2, TTBR0_EL2                              |
| Realm EL2&0 stage 1  | Realm EL2         | SCTLR_EL2, SCTLR2_EL2, TCR_EL2, TCR2_EL2, MAIR_EL2, MAIR2_EL2, AMAIR_EL2, AMAIR2_EL2, TTBR0_EL2, TTBR1_EL2, HCR_EL2          |
| Realm EL1&0 stage 2  | Realm EL2         | SCTLR_EL2, SCTLR2_EL2, VTCR_EL2, VTTBR_EL2, HCR_EL2                                                                          |
| Realm EL1&0 stage 1  | Realm EL1         | SCTLR_EL1, SCTLR2_EL1, TCR_EL1, TCR2_EL1, MAIR_EL1, MAIR2_EL1, AMAIR_EL1, AMAIR2_EL1, TTBR0_EL1, TTBR1_EL1, HCR_EL2          |
| EL3 stage 1          | EL3               | SCTLR_EL3, SCTLR2_EL3, SCR_EL3, TCR_EL3, MAIR_EL3, MAIR2_EL3, AMAIR_EL3, AMAIR2_EL3, TTBR0_EL3                               |

IDDTVD

The following table lists the System register common abbreviations used in VMSAv8-64. The common abbreviation is used to describe features that apply to multiple translation regimes or translation stages.

Table D8-4 Common System register abbreviations used in VMSAv8-64

| Common Abbreviation   | Translation stage   | Exception level EL1   | EL2                   | EL3        |
|-----------------------|---------------------|-----------------------|-----------------------|------------|
| AMAIR_ELx             | -                   | AMAIR_EL1             | AMAIR_EL2             | AMAIR_EL3  |
| AMAIR2_ELx            | -                   | AMAIR2_EL1            | AMAIR2_EL2            | AMAIR2_EL3 |
| MAIR_ELx              | -                   | MAIR_EL1              | MAIR_EL2              | MAIR_EL3   |
| MAIR2_ELx             | -                   | MAIR2_EL1             | MAIR2_EL2             | MAIR2_EL3  |
| SCTLR_ELx             | -                   | SCTLR_EL1             | SCTLR_EL2             | SCTLR_EL3  |
| SCTLR2_ELx            | -                   | SCTLR2_EL1            | SCTLR2_EL2            | SCTLR2_EL3 |
| TCR_ELx               | Stage 1             | TCR_EL1               | TCR_EL2               | TCR_EL3    |
| TCR_ELx               | Stage 2             |                       | VTCR_EL2, VSTCR_EL2   |            |
| TCR2_ELx              | Stage 1             | TCR2_EL1              | TCR2_EL2              |            |
| TTBR_ELx              | Stage 1             | TTBR0_EL1, TTBR1_EL1  | TTBR0_EL2, TTBR1_EL2  | TTBR0_EL3  |
| TTBR_ELx              | Stage 2             |                       | VTTBR_EL2, VSTTBR_EL2 |            |
| TTBRn_ELx             | Stage 1             | TTBR0_EL1, TTBR1_EL1  | TTBR0_EL2, TTBR1_EL2  | TTBR0_EL3  |
| TTBR0_ELx             | Stage 1             | TTBR0_EL1             | TTBR0_EL2             | TTBR0_EL3  |
| TTBR1_ELx             | Stage 1             | TTBR1_EL1             | TTBR1_EL2             |            |

IRGGJW

When software that enables or disables an address translation stage uses a PA that differs from the V A, speculative instruction fetching can cause complications. If software controls address translations that apply to the software itself, then when that software enables or disables an address translation stage, Arm recommends that the software uses a PA that is identical to the V A.

ICVKWB

For more information, see:

- Relationship between translation regimes and implemented Exception levels.
- Register name disambiguation by Exception level.

## D8.1.5 Out-of-context translation regimes

| I PTDBT   | Software is required to consider the effects on registers and translation tables when a context switch is made from one translation regime to another.                                                                                                                                                                                                                                                                                                                    |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R NRJPP   | If an implementation is executing at EL3 or EL2, the PE is not permitted to use the registers associated with the EL1&0 translation regime to speculatively access memory or translation tables.                                                                                                                                                                                                                                                                          |
| R FCZXS   | If an implementation is executing at EL3, the PE is not permitted to use the registers associated with the EL2 and EL2&0 translation regimes to speculatively access memory or translation tables.                                                                                                                                                                                                                                                                        |
| R LFHQG   | When an exception to a higher Exception level occurs, memory accesses caused by the translation table walk for the lower exception level can continue speculatively after the higher Exception level is entered.                                                                                                                                                                                                                                                          |
| I QVPYJ   | When an exception to a higher Exception level occurs, executing a DSB instruction after entering that higher Exception level ensures that the memory accesses caused by the translation table walk are completed.                                                                                                                                                                                                                                                         |
| I GFKHK   | If the Statistical Profiling Unit (SPU) is not in use at a lower Exception level, when a DSB instruction is executed and completed after entering a higher Exception level, all of the following apply regarding memory accesses caused by speculative translation table walks from the lower Exception level: • All of the speculative memory accesses are observed as required by the Shareability and Cacheability attributes                                          |
| I JZRDG   | If the SPU is in use at a lower Exception level, when a PSB instruction and a subsequent DSB instruction are executed after entering a higher Exception level, all of the following apply regarding memory accesses caused by speculative translation table walks from a lower Exception level: • All of the speculative memory accesses are observed as required by the Shareability and Cacheability attributes of the lower Exception level translation table entries. |
| I MTHPL   | For exceptions to the rules in this section when the Trace Buffer Unit is enabled, seeR SJFRQ .                                                                                                                                                                                                                                                                                                                                                                           |
| I XHBRX   | If EL2 is enabled, when a switch from one virtual machine to another occurs, software executing at EL0 or EL1 expects register fields controlling or affecting the EL1&0 regime are modified consistently before the next virtual machine starts execution.                                                                                                                                                                                                               |
| I SFZVV   | If the registers fields controlling or affecting the EL1&0 translation regime are modified when changing a virtual machine, then all of the following apply: • Software executing at EL2 does the modification. • The registers are modified out-of-context from software executing at EL1 or EL0. • When modifying the registers, no synchronization precautions are required until the exception return to EL1 or EL0.                                                  |

## D8.1.6 Implemented physical address size

ITRRHX

The implemented PA size is indicated by the value of the ID\_AA64MMFR0\_EL1.PARange field, as shown in the following table. All other values of the ID\_AA64MMFR0\_EL1.PARange field are reserved.

## Table D8-5 Implemented physical address size

| ID_AA64MMFR0_EL1.PARange   | PA memory size   | PA address size   |
|----------------------------|------------------|-------------------|
| 0b0000                     | 4GB              | 32 bits, PA[31:0] |
| 0b0001                     | 64GB             | 36 bits, PA[35:0] |
| 0b0010                     | 1TB              | 40 bits, PA[39:0] |
| 0b0011                     | 4TB              | 42 bits, PA[41:0] |
| 0b0100                     | 16TB             | 44 bits, PA[43:0] |
| 0b0101                     | 256TB            | 48 bits, PA[47:0] |
| 0b0110                     | 4PB              | 52 bits, PA[51:0] |
| 0b0111                     | 64PB             | 56 bits, PA[55:0] |

RHGNFW

If the implemented PA size is greater than 48 bits, then FEAT\_LPA is required.

INRJPM

APAsize greater than 52 bits can only be expressed by the VMSAv9-128 translation system.

RZHZNT

If the VMSAv8-64 translation system is used in an implementation that supports the VMSAv9-128 translation system, then PA bits [55:52] are set to 0b0000 .

## D8.1.7 Output address size configuration

RQQQSJ

For a translation stage that uses the VMSAv8-64 translation system, the maximum OA size that can be described by translation table entries is one of the following:

- For a translation regime controlled by TCR\_ELx, if the 4KB or 16KB translation granule is used, then one of the following:
- -If the Effective value of TCR\_ELx.DS is 0, then 48 bits.
- -If the Effective value of TCR\_ELx.DS is 1, then 52 bits.
- For any translation regime, if the 64KB translation granule is used, then one of the following:
- -If FEAT\_LPA is not implemented, then 48 bits.
- -If FEAT\_LPA is implemented, then 52 bits.

RLWWHG For a translation stage that uses the VMSAv9-128 translation system, the maximum OA size that can be described by translation table entries is 56 bits.

RMRYSR

The name of the TCR\_ELx.{I}PS field is one of the following:

- If the register is TCR\_EL1, then the field is TCR\_EL1.IPS.
- If the register is TCR\_EL2, then one of the following:
- -If the Effective value of HCR\_EL2.E2H is 0, then the field is TCR\_EL2.PS.
- -If the Effective value of HCR\_EL2.E2H is 1, then the field is TCR\_EL2.IPS.
- If the register is TCR\_EL3, then the field is TCR\_EL3.PS.

IYDDNK The OA size from a translation stage is configured by the associated TCR\_ELx.{I}PS field, as shown in the following table.

## Table D8-6 Output address size configuration

| TCR_ELx.{I}PS   | OA memory size   | OA address size   |
|-----------------|------------------|-------------------|
| 0b000           | 4GB              | 32 bits, OA[31:0] |

| TCR_ELx.{I}PS   | OA memory size   | OA address size   |
|-----------------|------------------|-------------------|
| 0b001           | 64GB             | 36 bits, OA[35:0] |
| 0b010           | 1TB              | 40 bits, OA[39:0] |
| 0b011           | 4TB              | 42 bits, OA[41:0] |
| 0b100           | 16TB             | 44 bits, OA[43:0] |
| 0b101           | 256TB            | 48 bits, OA[47:0] |
| 0b110           | 4PB              | 52 bits, OA[51:0] |
| 0b111           | 64PB             | 56 bits, OA[55:0] |

Note

|         | For the TCR_EL2.PS field, if the Effective value of HCR_EL2.E2H is 0, then the value 0b111 is reserved.                                                                                                                                        |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I MNZFV | The TCR_ELx.{I}PS field is three bits and has the same encoding as the three least significant bits of ID_AA64MMFR0_EL1.PARange.                                                                                                               |
| R CLPQT | The OAsize from a translation stage cannot be larger than the implemented PA size. If the OAsize represented by TCR_ELx.{I}PS is larger than the implemented PA size, then the OAsize is treated as being the same as the implemented PA size. |
| I PKBTM | Arm strongly recommends that software avoids configuring TCR_ELx.{I}PS to a value greater than the implemented PA size.                                                                                                                        |
| I HGDWP | If a translation stage is enabled and the translation stage OAis larger than the implemented PA size, then an Address size fault is generated at the lookup level in the translation stage that generated the OA.                              |
| R BZHGM | If all of the following apply, then a stage 2 Translation fault is generated: • Two address translation stages are used. • Stage 2 address translation is enabled.                                                                             |

## D8.1.8 Supported virtual address ranges

IYMKBT

The VA size is determined by configuring the stage 1 translation IA size.

For more information, see Input address size configuration.

RHYPNC For the VMSAv8-64 translation system, the maximum VA size is one of the following:

- For a translation regime controlled by TCR\_ELx, if the 4KB or 16KB translation granule is used, then one of the following:
- -If the Effective value of TCR\_ELx.DS is 0, then 48 bits.
- -If the Effective value of TCR\_ELx.DS is 1, then 52 bits.
- For any translation regime, if the 64KB translation granule is used, then one of the following:
- -If FEAT\_LVA is not implemented, then 48 bits.
- -If FEAT\_LVA is implemented, then 52 bits.

For the VMSAv9-128 translation system, the maximum VA size is one of the following:

- If FEAT\_LVA3 is implemented, then 56 bits.
- If FEAT\_LVA is implemented and FEAT\_LVA3 is not implemented, then 52 bits.
- If FEAT\_LVA is not implemented, then 48 bits.

Only stage 1 address translation in the EL1&amp;0 and EL2&amp;0 translation regimes support two V A ranges.

RXQGZR

IKRQBC

RBXWQW

RGZPNP

RHYYQH

RCSSJN

ITHWTD

If a translation regime supports two V A ranges, then each V A range represents an independent mapping from IA to OA.

If a translation regime supports a single V A range, then all of the following apply:

- The maximum IA width is 56 bits.
- If the maximum VA size is 48 bits, then the maximum VA range is 0x0000\_0000\_0000\_0000 to 0x0000\_FFFF\_FFFF\_FFFF .
- If the maximum VA size is 52 bits, then the maximum VA range is 0x0000\_0000\_0000\_0000 to 0x000F\_FFFF\_FFFF\_FFFF .
- If the maximum VA size is 56 bits, then the maximum VA range is 0x0000\_0000\_0000\_0000 to 0x00FF\_FFFF\_FFFF\_FFFF .

If a translation regime supports two V A ranges, then all of the following apply:

- The maximum IA width is 55 bits.
- IA bit[55] determines one of the following V A ranges:
- -If IA bit[55] is 0, the lower V A range is used.
- -If IA bit[55] is 1, the upper V A range is used.
- The maximum lower VA range is one of the following:
- -If the maximum VA size is 48 bits, then the maximum VA range is 0x0000\_0000\_0000\_0000 to 0x0000\_FFFF\_FFFF\_FFFF .
- -If the maximum VA size is 52 bits, then the maximum VA range is 0x0000\_0000\_0000\_0000 to 0x000F\_FFFF\_FFFF\_FFFF .
- -If the maximum VA size is 55 bits, then the maximum VA range is 0x0000\_0000\_0000\_0000 to 0x007F\_FFFF\_FFFF\_FFFF .
- The maximum upper VA range is one of the following:
- -If the maximum VA size is 48 bits, then the maximum VA range is 0xFFFF\_0000\_0000\_0000 to 0xFFFF\_FFFF\_FFFF\_FFFF .
- -If the maximum VA size is 52 bits, then the maximum VA range is 0xFFF0\_0000\_0000\_0000 to 0xFFFF\_FFFF\_FFFF\_FFFF .
- -If the maximum VA size is 55 bits, then the maximum VA range is 0xFF80\_0000\_0000\_0000 to 0xFFFF\_FFFF\_FFFF\_FFFF .

If the configured size of the upper V A range is less than the maximum, then all of the following apply:

- The range starting address is greater than the address used by the maximum V A size.
- The range ending address is 0xFFFF\_FFFF\_FFFF\_FFFF .

A48-bit VA range defines an address space of 256TB. A 52-bit VA range defines an address space of 4PB. A 56-bit V A range defines an address space of 64PB.

## D8.1.9 Input address size configuration

RTLMML

If a translation stage supports a single V A range, then TCR\_ELx.T0SZ configures the IA size, translated using TTBR0\_ELx.

RGMLRF

If a translation stage supports two V A ranges, then all of the following TCR\_ELx.T n SZ fields specify the IA size:

- TCR\_ELx.T0SZ configures the IA size of the lower VA range, translated using TTBR0\_ELx.

- TCR\_ELx.T1SZ configures the IA size of the upper VA range, translated using TTBR1\_ELx.

IGRZSP

The stage 1 translation IA size is defined as 64-TCR\_ELx.T n SZ.

RPLCGL

For all translation stages, the following table shows how the maximum permitted T n SZ value is determined:

- IQZVXG

## Table D8-7 Determining the maximum permitted TnSZ value

| Translation granule size   |   FEAT_TTST not implemented |   FEAT_TTST implemented |
|----------------------------|-----------------------------|-------------------------|
| 4KB                        |                          39 |                      48 |
| 16KB                       |                          39 |                      48 |
| 64KB                       |                          39 |                      47 |

IFTBXR

RYXNYW

If TCR\_ELx.T n SZ configures an IA size that is smaller than the maximum size, then each one-bit reduction in the IA size has one of the following effects on the lookup level that the table walk starts with:

- The translation table size is reduced by one half.
- The table walk starts one level later.

If the value of T n SZ is greater than the maximum permitted value, then any use of the T n SZ value causes one of the following IMPLEMENTATION DEFINED behaviors to occur:

- For all purposes other than reading back the value, the implementation behaves as if the T n SZ field has the maximum permitted value.
- Any use generates a level 0 Translation fault.

RGTJBY For a stage 1 translation using the VMSAv8-64 translation system, the minimum Effective value of T n SZ is one of the following:

- For the 4KB or 16KB translation granule, one of the following:
- -If the Effective value of TCR\_ELx.DS is 0, then the minimum Effective value of T n SZ is 16.
- -If the Effective value of TCR\_ELx.DS is 1, then the minimum Effective value of T n SZ is 12.
- For the 64KB translation granule, one of the following:
- -If FEAT\_LVA is not implemented, then the minimum Effective value of T n SZ is 16.
- -If FEAT\_LVA is implemented, then the minimum Effective value of T n SZ is 12.

RVRKKV For a stage 1 translation using the VMSAv9-128 translation system, the minimum Effective value of T n SZ is one of the following:

- If FEAT\_LVA3 is implemented, then one of the following:
- -If the translation regime supports a single IA range, then 8.
- -If the translation regime supports two IA ranges, then 9.
- If FEAT\_LVA is implemented and FEAT\_LVA3 is not implemented, then 12.
- If FEAT\_LVA is not implemented, then 16.

RVCDSW If all of the following apply, then a stage 1 level 0 Address size fault is generated:

- Stage 1 translation is disabled.
- The IA size is larger than the implemented PA size.

For an address translation stage, when an attempt is made to translate an address larger than the configured IA size, a level 0 Translation fault at that translation stage is generated.

RSXWGM For a stage 1 address translation, if the value of T n SZ is smaller than the minimum Effective value, then when using the T n SZ value to translate an address, one of the following applies:

- If FEAT\_LVA is not implemented, then it is IMPLEMENTATION DEFINED which of the following behaviors occurs:
- -For all uses other than reading back the value, the implementation behaves as if the T n SZ field has a value of 16.
- -When using the T n SZ value to translate an address, a stage 1 level 0 Translation fault is generated.
- If FEAT\_LVA is implemented, then when using the T n SZ value to translate an address, a stage 1 level 0 Translation fault is generated.

For more information, see Relationship between translation regimes and implemented Exception levels.

ITFBDN

## D8.1.10 Intermediate physical address size configuration

RSCJMS

RTDJSG

RDRRZZ

RDTLMN

When a stage 2 translation occurs, the configured IPA size is specified by one of the following T0SZ values:

- If the IPA is in Non-secure or Realm address space, then VTCR\_EL2.T0SZ
- If the IPA is in Secure address space, then VSTCR\_EL2.T0SZ

The implemented PA size constrains all of the following:

- The maximum IPA size.
- The effective minimum T0SZ value, VTCR\_EL2.T0SZ or VSTCR\_EL2.T0SZ, used to specify the configured IPA size.
- The stage 2 initial lookup level.

When all of the following apply, the stage 2 translation IPA size check generates a stage 2 level 0 Translation fault:

- Stage 2 translation is enabled.
- The OA size from the stage 1 translation, whether or not stage 1 translation is enabled, is larger than the IA size specified by VTCR\_EL2.T0SZ or VSTCR\_EL2.T0SZ.

When a stage 2 translation occurs, the effective minimum value of T0SZ is determined by the implemented PA size as shown in the following table:

Table D8-8 Determining the effective minimum T0SZ value for stage 2 translations

| Implemented PA size   | Effective minimum T0SZ value                                       |
|-----------------------|--------------------------------------------------------------------|
| 32 bits               | 32 if EL1 is using AArch64                                         |
| 32 bits               | 24 if EL1 is using AArch32                                         |
| 36 bits               | 28 if EL1 is using AArch64                                         |
| 36 bits               | 24 if EL1 is using AArch32                                         |
| 40 bits               | 24                                                                 |
| 42 bits               | 22                                                                 |
| 44 bits               | 20                                                                 |
| 48 bits               | 16                                                                 |
| 52 bits               | 12                                                                 |
| 56 bits               | 8 if the translation regime uses the VMSAv9-128 translation system |

RSRKBC

Table D8-9 shows the permitted initial stage 2 lookup levels for each of the effective minimum T0SZ values. For the 4KB granule, an initial lookup level of 3 is only supported if FEAT\_TTST is implemented and the PE is executing in AArch64 state.

Table D8-9 Implications of the effective minimum T0SZ value on the initial stage 2 lookup level

| Supported PA size   | Effective minimum T0SZ value                            | Valid initial lookup levels   | Valid initial lookup levels   |              |
|---------------------|---------------------------------------------------------|-------------------------------|-------------------------------|--------------|
|                     |                                                         | 4KB granule                   | 16KB granule                  | 64KB granule |
| 32 bits             | 32, if EL1 is using AArch64 24, if EL1 is using AArch32 | 3, 2, 1                       | 3, 2                          | 3, 2         |
| 36 bits             | 28, if EL1 is using AArch64 24, if EL1 is using AArch32 | 3, 2, 1                       | 3, 2                          | 3, 2         |
| 40 bits             | 24                                                      | 3, 2, 1                       | 3, 2                          | 3, 2         |

| Supported PA size   | Effective minimum T0SZ value   | Valid initial lookup levels   | Valid initial lookup levels   |              |
|---------------------|--------------------------------|-------------------------------|-------------------------------|--------------|
|                     |                                | 4KB granule                   | 16KB granule                  | 64KB granule |
| 42 bits             | 22                             | 3, 2, 1                       | 3, 2, 1                       | 3, 2         |
| 44 bits             | 20                             | 3, 2, 1, 0                    | 3, 2, 1                       | 3, 2, 1      |
| 48 bits             | 16                             | 3, 2, 1, 0                    | 3, 2, 1                       | 3, 2, 1      |
| 52 bits             | 12                             | 3, 2, 1, 0, -1                | 3, 2, 1, 0                    | 3, 2, 1      |
| 56 bits             | 8                              | 3, 2, 1, 0, -1, -2            | 3, 2, 1, 0, -1                | 3, 2, 1, 0   |

## For more information, see:

- VMSAv8-64 Stage 2 address translation using the 4KB translation granule
- VMSAv8-64 Stage 2 address translation using the 16KB translation granule
- VMSAv8-64 Stage 2 address translation using the 64KB translation granule
- Translation using the VMSAv9-128 translation system

For a stage 2 address translation, if FEAT\_LPA is not implemented and the value of T0SZ is smaller than the effective minimum value, then it is IMPLEMENTATION DEFINED which of the following behaviors occurs:

- For all purposes other than reading back the value of the field, the implementation treats the T0SZ field as having the effective minimum value.
- The implementation generates a stage 2 level 0 Translation fault.

For a stage 2 address translation, if FEAT\_LPA is implemented and the value of the T0SZ field is smaller than the effective minimum value, then a stage 2 level 0 Translation fault is generated.

If the T0SZ field is programmed to a value smaller than the effective minimum value, then a larger address range cannot be supported because an Address size fault is generated due to one of the following reasons:

- For a VMSAv8-64 stage 1 translation, the stage 1 OA is larger than the PA size.
- For a VMSAv8-32 stage 1 translation, the stage 1 OA is larger than 40 bits.

For more information, see:

- Implemented physical address size.
- Translation table walk.
- Memory aborts.

RMWXYY

RMYXHB

IZZJJF

INLYLM