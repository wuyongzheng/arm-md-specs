## D8.5 Hardware updates to the translation tables

IFNBGK

All of the following determine whether hardware can update the descriptor access flag and dirty state:

- The features implemented and enabled by the PE.

- The descriptor type.

- The translation regime.

- The translation stage.

ICGGMJ

Hardware updates to the translation tables are subject to memory ordering requirements and restrictions on the memory types.

## D8.5.1 The Access flag

RXFXTY

The AF in a Block descriptor and Page descriptor indicates one of the following:

- If the value is 0, then the memory region has not been accessed since the value of AF was last set to 0.
- If the value is 1, then the memory region has been accessed since the value of AF was last set to 0.

Descriptors with AF set to zero can never be cached in a TLB.

For more information about when translation table entries are permitted to be cached in a TLB, see Translation Lookaside Buffers.

## D8.5.1.1 Software management of the Access flag

ICDQDG If the AF is not managed by hardware, software management of the AF is required.

RSWTYY For an implementation that does not manage the AF in hardware, when an attempt is made to translate an address using a descriptor with an AF of 0, an Access flag fault is generated.

IFDYZF For an implementation that does not manage the AF in hardware, when an Access flag fault is generated, software is expected to set the AF to 1 in the descriptor that generated the fault.

IKQMYT Setting the AF to 1 prevents the Access flag fault from being generated the next time an attempt is made to translate an address using that descriptor.

IHQBRF When software sets the AF to 1, there is no requirement to perform TLB invalidation after setting the flag because entries with an AF set to 0 are never held in a TLB.

IBMRWH If a system incorporates components that can autonomously update translation table entries that are shared with the PE, then any changes by system software to translation table entries with an AF of 0 should avoid the possibility of simultaneous updates. This excludes changes to the AF value. For example, this can be done by using a Load-Exclusive/Store-Exclusive loop or an atomic compare-and-swap operation.

## D8.5.1.2 Hardware management of the Access flag

RWMGCW All statements in this section require implementation of the OPTIONAL feature, FEAT\_HAFDBS.

RLFTXR When the PE performs a hardware update of the AF, it sets the AF to 1 in the corresponding descriptor in memory, in a coherent manner, using an atomic read-modify-write of that descriptor.

RHDHQG For a translation stage, if the value of the corresponding TCR\_ELx.HA is 1, then AF hardware management is enabled.

IBDRJG

For each translation stage, AF hardware management can be enabled independently.

RHDTRB If AF hardware management is enabled, then hardware updates the AF when a memory access is made using a Block descriptor or Page descriptor and all of the following apply:

- The access does not generate an Alignment fault based on the memory type, or a Permission fault.
- If AF hardware management was disabled or not implemented, the access would have generated an Access flag fault.

RDWZCQ

| R QSPMS   | If AF hardware management is enabled, then it is CONSTRAINED UNPREDICTABLE whether hardware updates the AF when a memory access is made using a Block descriptor or Page descriptor and all of the following apply: • The access generates an Alignment fault based on the memory type, a Permission fault, or any fault that has a lower priority than a Permission fault from that stage of translation. • If AF hardware management were disabled or not implemented, the access would have generated an Access flag                                                                                        |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I RGQLZ   | If hardware does not update the AF from 0 to 1, then the descriptor is not permitted to be cached in a TLB.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| R VNHWC   | If AF hardware management is enabled in one or both translation stages, then when a memory access occurs, one or more of the following can be updated: • The stage 1 AF. • Each of the stage 2 AFs used to translate accesses to the stage 1 translation table walk and the OA.                                                                                                                                                                                                                                                                                                                                |
| I CVNQR   | For stage 1 translations, if AF hardware management is enabled, then when stage 2 translation does not permit access to the OAreturned by the stage 1 translation, it is permitted, but not required, for the stage 1 AF to be updated.                                                                                                                                                                                                                                                                                                                                                                        |
| I MYQJN   | For stage 2 translations, if AF hardware management is enabled, then when stage 1 translation does not permit access, it is permitted, but not required, for the stage 2 AF to be updated.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| R LHQRX   | If AF hardware management is enabled and a speculative access is successfully translated, then it is permitted, but not required, for hardware to update the AF.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| R GGYFS   | When a speculative access occurs, the rules determining the AF hardware update apply.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| I GXGPN   | When the translation of an architecturally executed memory access occurs, the architecture requires that AF is set to 1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| I LLCCB   | When a translation occurs, the AF is permitted to be set to 1 even in the case where no architecturally executed memory access occurs. This could be due to a speculative memory access.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| I PJWQY   | When hardware updates of the Access Flag are enabled, it is permitted to update the Access Flag speculatively. This is not affected by the granule protection check on the output address of the translation.                                                                                                                                                                                                                                                                                                                                                                                                  |
| R XQSMX   | For an address translation stage, if AF hardware management is enabled, then when an address translation instruction is executed, all of the following apply: • Hardware is permitted, but not required, to update the AF in the Block or Page descriptor that resolves the translation. • If hardware attempts to update the AF and the update generates a fault, it is IMPLEMENTATION DEFINED whether this is reported as a Data Abort or not. • If a Data Abort does not occur, then the instruction reports a result in the PAR as if the descriptors used to translate the address have an AF value of 1. |
| I ZWQRX   | For more information, see Using break-before-make when updating translation table entries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| I KJBFT   | If an implementation does not generate Access flag faults for cache maintenance by VA instructions, it is not required to perform hardware updates of AF for those cache maintenance instructions. See also MMUfaults generated by cache maintenance operations.                                                                                                                                                                                                                                                                                                                                               |
|           | D8.5.1.3 Hardware management of the Table descriptor Access Flag                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| R LWKQH   | All statements in this section require implementation of FEAT_HAFT.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| R PJFRD   | All statements in this section apply when the translation stage uses VMSAv8-64 or VMSAv9-128. They do not apply when the translation stage uses VMSAv8-32.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| I HZHJT   | Software management of the Table descriptor AF is not supported, and no Access Flag fault is generated from Table descriptors.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

RFWSJH

For a translation stage, the Hardware managed Access Flag for Tables (HAFT) value is determined according to the following table:

## Table D8-89 Determination of HAFT value

| Translation stage   | Translation regime   | HAFT value    |
|---------------------|----------------------|---------------|
| Stage 1             | EL1&0                | TCR2_EL1.HAFT |
|                     | EL2&0                | TCR2_EL2.HAFT |
|                     | EL2                  | TCR2_EL2.HAFT |
|                     | EL3                  | TCR_EL3.HAFT  |
| Stage 2             | EL1&0                | VTCR_EL2.HAFT |

RSNVTX

For a translation stage, if the value of TCR\_ELx.HA is 0, then the Effective value of the corresponding HAFT is 0.

RHTTKB

The Effective value of HAFT is permitted to be cached in a TLB.

RYCTVZ

The HAFT value determines whether the Table descriptor AF is managed by hardware, as shown in the following table:

## Table D8-90 Meaning of HAFT value

| HAFT value   | Meaning                                                                                                                                                                                                                                                                                                                                                 |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0            | There is no AF in Table descriptors.                                                                                                                                                                                                                                                                                                                    |
| 1            | Hardware management of the Table descriptor AF is enabled.                                                                                                                                                                                                                                                                                              |
| I PDQYR      | Table descriptor AF hardware management can be enabled for each translation stage independently.                                                                                                                                                                                                                                                        |
| R BCWSB      | When the PE performs a hardware update of the Table descriptor AF, it sets the AF to 1 in the corresponding descriptor in memory, in a coherent manner, using an atomic read-modify-write of that descriptor.                                                                                                                                           |
| R ZGNSH      | If Table descriptor AF hardware management is enabled at a translation stage, then a speculative memory access is permitted to cause a hardware update to set the AF to 1 in any Table descriptor that is accessed during the translation table walk for the access and for which the AF is 0.                                                          |
| R MDMYP      | When a speculative access occurs, the rules determining the Table descriptor AF hardware update apply.                                                                                                                                                                                                                                                  |
| R CGKWB      | For an architecturally executed memory access translated by a translation stage with Table descriptor AF hardware management enabled, the PE is required to set the AF to 1 in all Table descriptors accessed during the translation table walk for that access that have the AF set to 0.                                                              |
| R FBZPR      | When an address translation instruction is executed, for a translation stage with Table descriptor AF hardware management enabled, the PE is required to set AF to 1 in all Table descriptors accessed during the translation table walk that have the AF set to 0.                                                                                     |
| R XYNNS      | For a translation stage with Table descriptor AF hardware management enabled, if the AF is updated in a Table descriptor, Block descriptor, or Page descriptor, then all Table descriptors that are accessed from memory leading up to that descriptor in the translation table walk are required to either already have AF set to 1 or update AF to 1. |
| I QYLZN      | For information on the memory ordering requirements and restrictions on the memory types when hardware updates the Table descriptor AF, see Hardware updates to the translation tables.                                                                                                                                                                 |
| I VPNMG      | Updates to the stage 1 Table descriptors are subject to stage 2 permission checks.                                                                                                                                                                                                                                                                      |

RJFCYB

For a translation stage with Table descriptor AF hardware management enabled, a Table descriptor with AF set to 0 is not permitted to be cached in a TLB.

## D8.5.2 The dirty state

IHTJWZ

The dirty state is used to indicate a memory block or page has been modified. When hardware update of the dirty state is enabled, the descriptor DBM field indicates whether the descriptor is a candidate for hardware updates of the dirty state.

RLRMSH

For the purpose of FEAT\_HAFDBS dirty state management, a Block descriptor or Page descriptor can be described as having one of the following states:

- Non-writable.
- Writable-clean.
- Writable-dirty.

| R XSTDV   | If a Block descriptor or Page descriptor is not writable-clean and not writable-dirty, then it is described as non-writable .                                                                   |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R CLBGT   | For a translation stage using Indirect permissions, software or hardware is permitted to manage the dirty state.                                                                                |
| R DQQCV   | For a translation stage using Direct permissions, only hardware is permitted to manage the dirty state.                                                                                         |
| R VRNVZ   | For more information on managing the dirty state in hardware, see Hardware management of the dirty state.                                                                                       |
| I CPTSY   | For a stage 1 translation using Indirect permissions at ELx, if the Effective value of TCR_ELx.HD is 0, then dirty state is managed by software.                                                |
| I ZCPYX   | For stage 2 translations using Indirect permissions, if the Effective value of VTCR_EL2.HD is 0, then dirty state is managed by software.                                                       |
| R QXCRT   | For stage 1 translations using Indirect permissions that grant write permission, the following table shows the descriptor state based on the Block descriptor and Page descriptor nDirty field: |

|   nDirty field | Descriptor state   |
|----------------|--------------------|
|              0 | Writable-dirty     |
|              1 | Writable-clean     |

Note

The polarity of the nDirty field matches the polarity of the AP[2] field used by Direct permissions.

For stage 2 translations using Indirect permissions that grant write permission, the following table shows the descriptor state based on the Block descriptor and Page descriptor Dirty field:

RXXBLY

|   Dirty field | Descriptor state   |
|---------------|--------------------|
|             0 | Writable-clean     |
|             1 | Writable-dirty     |

RPPGMC

For write accesses translated by a writable-clean descriptor, if the descriptor dirty state is managed by software, then a Permission fault due to dirty state is generated. For information on the priority of a Permission fault due to dirty state, see Prioritization of Permission faults.

## D8.5.2.1 Hardware management of the dirty state

| R QRTKG   | All statements in this section require implementation of the OPTIONAL feature, FEAT_HAFDBS, which supports both hardware update of the Access flag and hardware update of the dirty state.                                                                                                                                                                                                   |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I FLYZP   | For stage 1 translations, if the Effective value of the corresponding TCR_ELx.HD is 1, then dirty state hardware management is enabled.                                                                                                                                                                                                                                                      |
| I MHJZP   | For stage 2 translations, if the Effective value of VTCR_EL2.HD is 1, then dirty state hardware management is enabled.                                                                                                                                                                                                                                                                       |
| I DLNSK   | If a translation stage uses Direct permissions and hardware update of the dirty state is enabled, then the descriptorDBM field indicates whether the descriptor is a candidate for hardware updates of the dirty state.                                                                                                                                                                      |
| R PZFQC   | For translations using Direct permissions, if the DBMfield in a Block descriptor or Page descriptor is 0, then all of the following apply: • For write accesses translated by the descriptor, the generation of Permission faults are unaffected by FEAT_HAFDBS. • Hardware does not update the dirty state.                                                                                 |
| R XZFQH   | For each translation stage using Direct permissions, if all of the following apply, then a Block descriptor or Page descriptor is described as writable-clean : • Dirty state hardware update is enabled at that translation stage. • The descriptor DBMfield is 1. • For a descriptor used by stage 1 translation, the AP[2] field is 1 and this is the only reason that a Permission fault |
| R BRFGY   | For each translation stage using Direct permissions, if all of the following apply, then a Block descriptor or Page descriptor is described as writable-dirty : • Dirty state hardware update is enabled at that translation stage. • The descriptor DBMfield is 1. • For a stage 1 translation, the AP[2] field is 0.                                                                       |
| I HFBCN   | If a translation stage uses Indirect permissions, then dirty state hardware management is not separately determined by each Block descriptor and Page descriptor. This is different from the case where a translation stage uses Direct permissions, and the DBMfield indicates whether the descriptor is a candidate for dirty state hardware updates.                                      |
| I BFDYL   | Only if a descriptor is writable-clean, then hardware can update the dirty state.                                                                                                                                                                                                                                                                                                            |
| R TYCNM   | For write accesses translated by a writable-clean descriptor, if the descriptor dirty state is managed by hardware, then a Permission fault due to dirty state is not generated.                                                                                                                                                                                                             |
| R NSXRD   | For write accesses translated by a writable-clean descriptor, if all of the following apply, then hardware updates that descriptor to writable-dirty: • The descriptor dirty state is managed by hardware. • The only reason that a Permission fault would be generated due to that write access would be if dirty state hardware management were disabled.                                  |
| R PQJJR   | For a translation stage, when the dirty state is updated by hardware, the PE updates the corresponding descriptor in memory, in a coherent manner, using an atomic read-modify-write of that descriptor to change the descriptor from writable-clean to writable-dirty.                                                                                                                      |
| R PRHKD   | If the requirements to update both the Access flag and dirty state by hardware are met, the PE is permitted to update the Access flag to 1 as part of the same atomic read-modify-write of the descriptor that performs the dirty state update.                                                                                                                                              |
| I DSHLJ   | For a translation stage, Access flag faults are reported with higher priority than Permission faults. Therefore, it is not permitted for hardware to update the dirty state so that a descriptor is writable-dirty but has the Access flag clear.                                                                                                                                            |

| R SGJBL   | When the dirty state is updated by hardware, the PE is required to check that any copy of the descriptor cached in a TLB is not stale with regard to the descriptor in memory.                                                                                                                                                                                                                                                                                                                                                                       |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I YZSVV   | If the descriptor has changed, then the PE is required to use the new information from the descriptor in memory, regardless of whether the modified descriptor has a different OA, different attributes, or generates a fault.                                                                                                                                                                                                                                                                                                                       |
| I WZRPC   | For performance purposes, when the dirty state is updated by hardware, the PE should update or invalidate any TLB entry that contains a previously-cached copy of the descriptor. This is to prevent multiple writes by the PE from causing multiple updates to the descriptor.                                                                                                                                                                                                                                                                      |
| I HQBGN   | Arm expects many implementations to cause a translation table walk to occur when dirty state hardware management causes an update of a translation table descriptor.                                                                                                                                                                                                                                                                                                                                                                                 |
| R RNMLQ   | If a write access translated by a writable-clean descriptor is performed architecturally, then hardware updates the dirty state of that descriptor.                                                                                                                                                                                                                                                                                                                                                                                                  |
| R DYCFD   | If a write access translated by a writable-clean descriptor is not performed architecturally, then unless specified here hardware does not update the dirty state of that descriptor. In all of the following cases, hardware is permitted to update the dirty state while attempting to translate the explicit write access: • The translation generates an MMUfault that is reported with lower priority than a Permission fault at that                                                                                                           |
| R BZXVS   | If a tag write by an instruction that does not also write data is translated by a writable-clean descriptor, but the tag write effect is IGNORED due to one of the following reasons, then if all of the other requirements for a hardware update of Dirty state are met, it is CONSTRAINED UNPREDICTABLE whether hardware updates the dirty state of that descriptor: • The stage 1 descriptor does not have the Tagged attribute. • Allocation Tag Access is disabled for the instruction by SCR_EL3.ATA, HCR_EL2.ATA, or SCTLR_ELx.{ATA, ATA0}.   |
| R BDJJL   | If both translation stages are enabled, and the conditions to update a stage 1 descriptor by hardware are met, then the stage 2 translation of the location holding that stage 1 descriptor results in one of the following: • The stage 2 translation grants write permissions and the stage 1 hardware update occurs, including both of the following cases: - The stage 2 translation already grants write permission and does not need to be updated. - The stage 2 translation is writable-clean and is successfully updated to writable-dirty. |
| I TZTHF   | If a speculative update of a stage 1 Access flag would otherwise be permitted, but the stage 2 translation of the stage 1                                                                                                                                                                                                                                                                                                                                                                                                                            |

RJCXVS

If all of the following apply, hardware can update the dirty state of a stage 2 descriptor even if the stage 1 descriptor is not updated, including the case where the stage 1 descriptor is not a Block descriptor or Page descriptor:

- Stage 1 hardware updates of the Access flag or dirty state are enabled.
- The stage 2 translation of a stage 1 translation table walk uses a writable-clean descriptor.

RLXCKP The dirty state hardware update mechanism does not affect the fault reporting priority except in all of the following cases:

- If all of the following stage 2 MMU faults are generated due to a non-speculative access that causes a stage 1 hardware update, then either fault is permitted to be reported:
- -That stage 1 hardware update generates a stage 2 MMU fault.
- -The stage 2 translation of the stage 1 OA generates a stage 2 MMU fault.
- If a hardware update is permitted, that update is permitted to generate a synchronous External abort or an IMPLEMENTATION DEFINED abort caused by a memory type not supporting an atomic read-modify-write.

RQDRWL If an instruction that generates more than one single-copy atomic memory access has a fault on some, but not all, of those memory accesses, then all of the following apply:

- All accesses that do not fault are permitted to cause hardware updates of the dirty state.
- For faulting accesses that meet the requirements for hardware updates of the dirty state, those accesses are also permitted to cause hardware updates of the dirty state.

IBSLWF For more information, see:

- MMUfault prioritization from a single address translation stage.
- Faults and watchpoints.

## D8.5.2.2 Implications of enabling the dirty state management mechanism

- RYWCDD All statements in this section require implementation of the OPTIONAL feature, FEAT\_HAFDBS, which supports both hardware update of the Access flag and hardware update of the dirty state.
- RTTLCV For stage 1 translations, translations using a descriptor in the writable-clean state are considered writable for the purposes of the corresponding SCTLR\_ELx.WXN control.

INSYYW For stage 1 translations, if the corresponding SCTLR\_ELx.WXN is 1, then all of the following apply:

- For a translation regime that supports a single privilege level, translations using a writable-clean descriptor are treated as execute-never.
- For a translation regime that supports two privilege levels, translations using a privileged writable-clean descriptor are treated as privileged execute-never.
- For a translation regime that supports two privilege levels, translations using an unprivileged writable-clean descriptor are treated as unprivileged execute-never.
- RNKLQN For a translation regime that supports two privilege levels, translations using an unprivileged writable-clean descriptor are treated as privileged execute-never.

RZYGHJ Cache invalidation instructions and address translation instructions never cause a dirty state hardware update of either:

- The stage 1 Block descriptor or Page descriptor translating the address specified in the instruction.
- The stage 2 Block descriptor or Page descriptor translating the OA from the stage 1 translation.
- RMBXNP Cache invalidation instructions and address translation instructions never cause a dirty state hardware update the stage 1 Block descriptor or Page descriptor translating the address specified in the instruction.
- RRKMHW For the following instructions that require write permission, if the address specified in the instruction is translated by a writable-clean descriptor and hardware management of Dirty state is enabled for the corresponding stage of translation, then the descriptor is considered to grant write access and the hardware does not update the Dirty state of that descriptor:
- Data cache invalidation instruction, DC IV AC.
- Data cache and instruction cache maintenance instructions that are affected by FEAT\_CMOW.
- Address translation instructions, AT S12E0W, AT S12E1W, AT S1E0W, AT S1E1W, AT S1E2W, AT S1E3W.

| R QXXXL   | For all of the following cases, if the stage 1 descriptor is writable-clean, then it is IMPLEMENTATION DEFINED whether hardware updates the dirty state:                                                                                                                  |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R KLVVN   | Ahardware update of the dirty state performed by one PE does not require invalidation of any corresponding TLB entries in other PEs.                                                                                                                                      |
| R TXGHB   | For a CAS or CASP instruction to an address translated by a writable-clean descriptor, if the comparison fails and the location is therefore not updated, then it is CONSTRAINED UNPREDICTABLE whether hardware updates the dirty state.                                  |
| R SMTCW   | For an RCW or RCWS instruction to an address translated by a writable-clean descriptor, if the RCWchecks orRCWS checks fail and the location is therefore not updated, then it is CONSTRAINED UNPREDICTABLE whether hardware updates the dirty state.                     |
| R KTXCF   | For a stage 2 writable-clean descriptor, if an atomic instruction to the address translated by the descriptor generates a stage 2 Permission fault only as a result of not having read permission, then it is CONSTRAINED UNPREDICTABLE hardware updates the dirty state. |
|           | whether                                                                                                                                                                                                                                                                   |
| I NWXLF   | The hardware dirty state tracking structure (HDBSS) keeps a record of dirtied stage 2 Block and Page descriptors, enabling EL2 software to retrieve this information without scanning translation tables.                                                                 |
| R RGTLS   | All statements in this section require implementation of the OPTIONAL feature, FEAT_HDBSS.                                                                                                                                                                                |
| R GKFDY   | If VTCR_EL2.HDBSS is 0, then all of the following apply: • The PE does not update the HDBSS in response to a dirty state hardware update.                                                                                                                                 |
|           | • The PE does not speculatively read the memory region configured by the HDBSSBR_EL2 fields.                                                                                                                                                                              |
| I SXBYL   | All of the following apply to the HDBSS base address: • It is a PA configured in HDBSSBR_EL2.BADDR. • For encodings of HDBSSBR_EL2.SZ greater than 4KB, bits [(SZ+12-1):12] of HDBSSBR_EL2.BADDR are                                                                      |
|           | RES0, such that the base address is aligned to its size.                                                                                                                                                                                                                  |
| R         | The PA space of the HDBSS base address is determined by the Effective value of SCR_EL3.{NSE, NS}.                                                                                                                                                                         |
| DBTZQ     |                                                                                                                                                                                                                                                                           |
| I JRDPM   | The HDBSS size is configured in HDBSSBR_EL2.SZ.                                                                                                                                                                                                                           |
| R BWVKS   | Each HDBSS entry is eight bytes.                                                                                                                                                                                                                                          |

RQWSGD

The following table defines the fields in an HDBSS entry.

RKFLNY

## Table D8-93 Hardware dirty state tracking structure fields

| Bit position   | Field       | Comment                                                                                                                                                                                                                                          |
|----------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [63:56]        | RES0        | -                                                                                                                                                                                                                                                |
| [55:12]        | IPA         | The IPA translated by the stage 2 descriptor that was updated from writable-clean to writable-dirty. The IPA is aligned to the size of the Page or Block descriptor that was updated. Bits above the implemented physical address size are RES0. |
| [11]           | NSIPA       | For Secure state, indicates one of the following: • 0, Secure IPA. • 1, Non-secure IPA. For Realm and Non-secure states, this bit is RES0.                                                                                                       |
| [10:4]         | RES0        | -                                                                                                                                                                                                                                                |
| [3:1]          | TTWL        | Translation table walk level at which the descriptor has been marked dirty. This field is a 3-bit two's complement signed integer.                                                                                                               |
| [0]            | Valid entry | 0, entry is invalid. 1, entry is valid.                                                                                                                                                                                                          |

RWZKFT If HDBSS is enabled, then when hardware updates a stage 2 descriptor from writable-clean to writable-dirty, the PE writes to the HDBSS.

IRYKVL The index of the next eight-byte HDBSS entry to write is indicated by HDBSSPROD\_EL2.INDEX.

RHKCCN The PE is permitted to mark HDBSS entries ahead of the HDBSSPROD\_EL2.INDEX as zero.

RPCTTC When the PE writes an HDBSS entry, all the following occur:

- The IPA that caused hardware to update the stage 2 descriptor dirty state, and the associated NSIPA and TTWL, are written to the HDBSS using the current HDBSSPROD\_EL2.INDEX. The write is done as a 64-bit single-copy atomic operation.
- The value of HDBSSPROD\_EL2.INDEX is incremented by 1.

Accesses to the HDBSS use the same memory attributes as stage 2 translation table walks, including all of the following:

- The endianness configured by SCTLR\_EL2.EE.
- The Normal memory type.
- The Cacheability and Shareability attributes configured by VTCR\_EL2.{IRGN0, ORGN0, SH0}.
- If FEAT\_MTE2 is implemented, accesses are always Tag Unchecked.
- If FEAT\_MEC is implemented, the MECID used for stage 2 translation table walks.
- If FEAT\_MPAM is implemented, the PARTID value, PMG value, and PARTID space used for stage 2 translation table walks.

INMYYP If FEAT\_RME is implemented and GPC is enabled, accesses to the HDBSS are subject to Granule Protection Checks.

- RTCJKB

If the translation table update or the HDBSS update is observable to the PE that performed the write that caused these updates, then completion of a DSB that applies to both loads and stores on the same PE guarantees observability of the other update.

RSTDKM

If any of the following apply, then there is no guarantee of order between the two updates described, and atomicity might be lost:

- The HDBSS entry and the translation table entry to be updated are at the same location.

RMWNLK

- The write to the HDBSS and the write access being translated target the same location.

RCGCHP On exception entry to ELx, where EL1&amp;0 is out-of-context, outstanding HDBSS writes performed by the PE during execution at EL1&amp;0 are guaranteed to be observable to memory accesses from ELx after completion of a DSB instruction that applies to both loads and stores.

IXXFYP Hardware increments of HDBSSPROD\_EL2.INDEX are indirect writes, and are therefore not guaranteed to be observable to direct reads of HDBSSPROD\_EL2 until completion of a context synchronization event.

RRXCMY The HDBSS is full when HDBSSPROD\_EL2.INDEX is greater than or equal to 2 (HDBSSBR\_EL2.SZ+12) /8.

ILMSZL If an HDBSS access generates an External abort or a GPC fault, and HDBSSPROD\_EL2.FSC is updated to a non-zero value, then the update of the FSC field might not happen synchronously relative to some stage 2 hardware updates of the dirty state. Therefore, one or more HDBSS entries might be lost. See GPC fault on HDBSS access and External aborts on HDBSS access.

RYHLRY If the HDBSS is full and enabled, then the PE does not update any stage 2 descriptors from writable-clean to writable-dirty.

RSTJMN If the HDBSS is enabled, and either the HDBSS is full or HDBSSPROD\_EL2.FSC is set to any value other than 0b000000 , then all of the following apply:

- The PE cannot append entries to the HDBSS.
- Stage 2 dirty state hardware updates are prevented.
- Any access that requires a stage 2 dirty state hardware update generates a stage 2 Permission fault that is reported as it would be if VTCR\_EL2.HD were 0. If the fault is reported in ESR\_EL2, ESR\_EL2.ISS2.HDBSSF is reported as 1, to indicate that the failed update was a result of the HDBSS being full or in an error state.

IKZMGK MMUfaults on speculative accesses are never reported.

If the HDBSS is full and enabled, and this generates a stage 2 Permission fault as part of resolving an AT *E1* operation executed at EL2, it is reported in PAR\_EL1 as a stage 2 Permission fault on a stage 1 translation table walk, at the level of stage 2 walk that experienced the fault.

## D8.5.2.3.1 GPC fault on HDBSS access

RLHLSD If FEAT\_RME is implemented and GPC is enabled, then when the hardware updates the stage 2 descriptor dirty state and the associated HDBSS access generates a GPC fault, all of the following apply:

- AGPCfault is reported.
- HDBSSPROD\_EL2.INDEX points to the HDBSS entry that generated the fault.
- It is IMPLEMENTATION DEFINED which of the following reporting mechanisms is used:
- -Aprecise exception is reported as though the dirty state hardware update generated the GPC fault, and ESR\_EL2.ISS2.HDBSSF is also set to 1.
- -The fault is reported in HDBSSPROD\_EL2.FSC.

IZRRMT For an HDBSS access, if a GPC fault is reported precisely, then that fault can be reported as a Data Abort, Instruction Abort, or Granule Protection Check exception, and taken to EL2 or EL3, according to the criteria described in Granule Protection Check faults.

## D8.5.2.3.2 External aborts on HDBSS access

- When an HDBSS write generates an External abort, HDBSSPROD\_EL2.INDEX points to the entry that generated the

RJHHQW fault, and it is IMPLEMENTATION DEFINED which of the following reporting mechanisms is used:

- Asynchronous fault is generated with all of the following properties:
- -It is reported as an Instruction Abort or Data Abort taken to EL2 or EL3, according to the value of SCR\_EL3.EA.
- -ESR\_ELx.IFSC or ESR\_ELx.DFSC indicates a synchronous External abort on a translation table walk or translation table hardware update.
- -ESR\_EL2.ISS2.HDBSSF is set to 1, indicating the HDBSS caused a synchronous External abort.
- The fault is reported by HDBSSPROD\_EL2.FSC.

When an HDBSS write generates a synchronous External abort, the MMU is permitted to do a hardware update of the stage 2 dirty state.

RQNJKV

RZLNFF

IXZGCW

RBFTGZ

When the hardware update of the stage 2 dirty state generates a synchronous External abort, or an Unsupported atomic hardware update fault, the MMU is permitted to write to the HDBSS.

## D8.5.2.4 Hardware accelerator for cleaning dirty state

IDRTDK The hardware accelerator for cleaning dirty state (HACDBS) accelerates the process of updating Block and Page descriptors from writable-dirty to writable-clean.

RQLGSL All statements in this section require implementation of the OPTIONAL feature, FEAT\_HACDBS.

ICYLPL The HACDBS is an HDBSS-like structure originating from either the same PE or different PEs. The format of entries in this structure is described in Table D8-93.

IBGSDY HACDBSprocessing is enabled only if HACDBSBR\_EL2.EN is 1 and HCR\_EL2.VM is 1.

RBBWCH When HACDBS processing is disabled by a changing HACDBSBR\_EL2.EN from 1 to 0, completion of a DSB instruction guarantees that all outstanding translation table walks have completed.

IBYRXM

All of the following apply to the HACDBS base address:

- It is a PA configured in HACDBSBR\_EL2.BADDR.
- For encodings of HACDBSBR\_EL2.SZ greater than 4KB, bits [(SZ+12-1):12] of HACDBSBR\_EL2.BADDR are RES0, such that the base address is aligned to its size.

RHGVVT The PA space of the HACDBS base address is determined by the Effective value of SCR\_EL3.{NSE, NS}.

ITQKLR

The HACDBS size is configured in HACDBSBR\_EL2.SZ.

RVRMKP Each HACDBS entry is eight bytes.

RSNFDZ

When processing an entry in the HACDBS, all of the following apply:

- The PE reads the HACDBS entry at the current value of HACDBSCONS\_EL2.INDEX. The read is done as a 64-bit single-copy atomic operation.
- If the entry is valid, the PE decodes the HACDBS entry to determine the IPA, NSIPA and TTWL fields.
- For a valid entry, the PE uses a stage 2 translation table walk to locate the stage 2 Block or Page descriptor that translates the IPA, and NSIPA attribute if appropriate. See Translation table walk.
- If any fault is generated, then HACDBS processing stops and the fault reporting requirements apply.
- If no fault is generated, then all of the following apply:
- -If the stage 2 descriptor is writable-dirty, then that descriptor is updated to writable-clean in a coherent manner, using an atomic read-modify-write.
- -If the stage 2 descriptor is writable-clean, it is not updated.
- -The value of HACDBSCONS\_EL2.INDEX is incremented by 1.

RKTPXV For the purpose of processing HACDBS entries and qualifying a descriptor as writeable-clean or writeable-dirty in this context, it is not required that stage 2 dirty state hardware update be enabled.

If stage 2 Direct permissions are used, then the descriptor DBM bit must be 1 for the descriptor to be considered writable-dirty.

If stage 2 Indirect permissions are used, then the descriptor is writable-dirty if the Dirty bit in the descriptor is 1, and the permissions configured for the descriptor include Data Write or MMU Write permission.

If an entry in the HACDBS is not valid, then all of the following apply:

- The PE does not process the invalid entry.
- HACDBSCONS\_EL2.INDEX is incremented by 1.

When the PE processes an entry and updates the corresponding stage 2 descriptor to writable-clean, the PE is not required to update any copy of that descriptor cached in a TLB.

Accesses to the HACDBS use the same memory attributes as stage 2 translation table walks, including all of the following:

RMRBXC

- The endianness configured by SCTLR\_EL2.EE.
- The Normal memory type.
- The Cacheability and Shareability attributes configured by VTCR\_EL2.{IRGN0, ORGN0, SH0}.
- If FEAT\_MTE2 is implemented, accesses are always Tag Unchecked.
- If FEAT\_MEC is implemented, the MECID used for stage 2 translation table walks.
- If FEAT\_MPAM is implemented, the PARTID value, PMG value, and PARTID space used for stage 2 translation table walks.

IPQQJG If FEAT\_RME is implemented and GPC is enabled, accesses to the HACDBS are subject to Granule Protection Checks.

ITDFSP For the purpose of cleaning HACDBS entries, Overlay permissions and the AssuredOnly property are ignored.

RJSHZF If the requirements in this subsection and the requirements for fault reporting are met, then the PE is permitted to process entries in the HACDBS ahead of the current value of HACDBSCONS\_EL2.INDEX.

RHWNDK In the absence of an error, all entries preceding the entry pointed to by HACDBSCONS\_EL2.INDEX have been successfully cleaned.

RDPCSW In the presence of an error, all the entries preceding the entry pointed to by HACDBSCONS\_EL2.INDEX have been successfully cleaned and the entry at the current index caused a fault.

IWWTCD In the presence of an error, the PE is permitted to have successfully cleaned entries after the one pointed to by HACDBSCONS\_EL2.INDEX.

IRMLQL If the HACDBS has empty entries, software can cause the PE to terminate processing before the end of the HACDBS is reached. This is done by programming the first empty entry in the HACDBS as follows:

- The Valid field is set to 1.
- The TTWL field is set to a reserved value.
- The remaining fields are set to any value.

Processing this entry causes the PE to raise an error, at which point software can intervene and disable processing of the HACDBS.

RLFZLR Hardware has finished processing the HACDBS when HACDBSCONS\_EL2.INDEX is greater than or equal to 2 (HACDBSBR\_EL2.SZ+12) /8.

RDLWRN

RRMVBG

The HACDBS interrupt request signal, HACDBSIRQ , is a level-sensitive interrupt request that is asserted when the Effective value of HACDBSBR\_EL2.EN is 1, and one or more of the following are true:

- Hardware has finished processing the HACDBS.
- HACDBSCONS\_EL2.ERR\_REASON is set to a value other than 0b00 .

The interrupt remains asserted until both conditions are no longer true.

If a Generic Interrupt Controller (GIC) is implemented, HACDBSIRQ must be a Private Peripheral Interrupt (PPI) in a multiprocessor system. This interrupt is signaled by the PE that implements the HACDBS.

RGQLDJ When hardware has finished processing the HACDBS, all of the following occur:

- The PE stops processing entries from the HACDBS.
- The HACDBSIRQ is asserted.

Note

When the PE stops processing the HACDBS, it is the responsibility of EL2 software to set HACDBSBR\_EL2.EN to 0.

If HACDBSBR\_EL2.EN is 1 and HACDBSCONS\_EL2 does not indicate any error state, and software modifies HACDBSBR\_EL2.{BADDR, SZ} or any field in HACDBSCONS\_EL2, then any of the following are permitted to occur:

- The direct write is IGNORED.
- The fields in HACDBSCONS\_EL2 become UNKNOWN.
- The address used for fetches of HACDBS entries is UNKNOWN.

IYFJTM

RZJYKS

RLMZLD

RWHMDV

- ILYJMC

RWLNPL

## D8.5.2.4.1 HACDBS errors

When an error occurs while processing an HACDBS entry, HACDBSCONS\_EL2.ERR\_REASON indicates the reason for the error.

When reading an entry from the HACDBS generates any of the following, HACDBSCONS\_EL2.ERR\_REASON is set to 0b01 :

- An External abort.
- If FEAT\_RME is implemented, then a GPC fault.

When an entry from the HACDBS is processed and the translation table walk for the IPA generates an MMU fault at any lookup level, HACDBSCONS\_EL2.ERR\_REASON is set to 0b10 . This includes all MMU faults except for the following:

- If the Access flag in the Block or Page descriptor is 0, an Access flag fault is not generated and the PE can update the descriptor to writable-clean.
- APermission fault.

RHDDCT When HACDBS entry is processed and any of the following apply during the translation table walk for the IPA, HACDBSCONS\_EL2.ERR\_REASON is set to 0b11 :

- The write permissions provided by the descriptor are anything other than writable-clean or writable-dirty.
- The Contiguous bit in the Block or Page descriptor is 1.
- The final lookup level does not match the TTWL field in the HACDBS entry.

RFQSJP When HACDBSCONS\_EL2.ERR\_REASON is set to a value other than 0b00 , all of the following occur:

- The PE stops processing entries from the HACDBS.
- HACDBSIRQ is asserted.

When a fault is generated, HACDBSCONS\_EL2.INDEX points to either:

- In the presence of a single fault, the HACDBS entry that generated the fault.
- In the presence of multiple faults, the oldest HACDBS entry that generated a fault. HACDBSCONS\_EL2.INDEX is the smallest value pointing to an entry that generated a fault.

Arm expects that after resolving an error related to the HACDBS, EL2 software increments HACDBSCONS\_EL2.INDEX by 1 and sets HACDBSCONS\_EL2.ERR\_REASON to 0b00 .

When an error occurs while processing an HACDBS entry, subsequent completion of a DSB instruction that applies to both loads and stores on the same PE guarantees that all outstanding fetches of HACDBS entries, and stage 2 translation table walks for processing HACDBS entries, have completed.

## D8.5.3 Ordering of hardware updates to the translation tables

RMKHJS

Ahardware update to the translation table that is caused by a load or a store, including an atomic instruction, is guaranteed to be observed, to the extent required by the Shareability attributes:

- Before a load or store, including an atomic instruction, to an arbitrary address, other than the address of the translation table entry, that appears in program order after the load or store, including an atomic instruction, causing the update to the translation table entry only if a DSB with the appropriate Shareability attributes, where the DSB applies to both loads and stores, is executed between the load or store, including an atomic instruction, that caused the update to the translation table and the subsequent load or store.
- Before a load to the translation table entry that is being updated that appears in program order after the load or store, including an atomic instruction, causing the update to the translation table entry only if a DSB with the appropriate Shareability attributes, where the DSB applies to both loads and stores, is executed between the load or store, including an atomic instruction, that caused the update to the translation table and the subsequent load.
- Before a store or atomic access to the translation table entry that is being updated that appears in program order after the load or store, including an atomic instruction, causing the update to the translation table entry.
- Before a cache maintenance instruction to an arbitrary address appearing in program order after the load or store, including an atomic instruction, causing the update to the translation table entry only if a DSB with the appropriate Shareability attributes, where the DSB applies to both loads and stores, is executed between the load or store, including an atomic instructing that caused the update to the translation table entry and the subsequent cache maintenance instruction.

| R PLLLM   | An update to the translation table that is caused by a load is not ordered with respect to the load itself.                                                                                                                                                                       |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R FSZNW   | An update to the translation table that is caused by a store or an atomic access is observed by all observers, to the extent required by the Shareability attributes, before the store itself in the case that the store is to the same location as the translation table update. |
| R RZYCN   | An update to the translation table that is caused by a store or an atomic access is not ordered with respect to the store itself in the case that the store is not the same location as the translation table update.                                                             |

## D8.5.4 Restriction on memory types for hardware updates to translation tables

IYTWWW Atranslation table can be placed in Normal memory with any Cacheability.

IXPRCJ

If hardware update of translation table entries is enabled, software is required to ensure that the translation table is located in memory that supports atomic read-modify-write updates in a coherent manner.

IMYHXH Atomicity properties can only be met at the system level, and some system implementations might not support this functionality in all memory regions, including all of the following:

- Any system memory type that does not support hardware cache coherency.
- Non-cacheable memory, or memory that is treated as Non-cacheable, in an implementation that does not support hardware cache coherency.

IPCHYY The system implementation determines which memory type is treated as Non-cacheable.

RWLTNL All of the following Conventional memory types architecturally guarantee that hardware updates of the translation tables are atomic:

- Inner Shareable, Inner Write-Back, Outer Write-Back Normal memory.
- Outer Shareable, Inner Write-Back, Outer Write-Back Normal memory.

If a translation table hardware update is not atomic as observed by other agents that can access memory, then the update can have one or more of the following effects:

- Asynchronous External abort on the translation table walk is generated.
- The instruction generates an SError exception.
- An MMU fault is generated, reported as an Unsupported atomic hardware update using one of the following Fault status codes:
- -For Data Abort exceptions, ESR\_ELx.DFSC = 0b110001 .
- -For Instruction Abort exceptions, ESR\_ELx.IFSC = 0b110001 .
- -For an abort on a write to the Statistical Profiling buffer, PMBSR\_EL1.FSC = 0b110001 .
- The hardware updates occur and all of the following apply:
- -There is no guarantee that the memory accesses are done atomically in regard to accesses to memory by other agents.
- -The instruction might also generate an SError exception.

RVSXXT If a translation table hardware update is not atomic as observed by other agents that can access memory, and the update generates an MMU fault, all of the following apply:

- If EL2 is implemented and enabled in the current Security state, then for the EL1&amp;0 translation regime, one of the following:
- -If the atomic hardware update is not supported in the stage 1 translation due to the defined memory type, or if the stage 2 translation is not enabled, then this exception is a stage 1 abort and is taken to EL1.
- -In all other cases, the exception is a stage 2 abort and is taken to EL2.
- For a translation stage, the MMU fault priority is at an IMPLEMENTATION DEFINED point between all of the following:
- -Immediately before the priority of an Access flag fault that is generated at the same translation stage.
- -Immediately after the priority of a Permission fault that is generated at the same translation stage.

If translation table hardware updates are not atomic as observed by other agents that can access memory, then in all of the following cases, the architecture permits, but does not require, an address translation instruction to generate an MMU fault, reported as an Unsupported atomic hardware update using PAR\_EL1.FST = 0b110001 :

RNNNMB

RYQMMR

IFGVJW

- For a stage 1 translation at EL1, stage 1 translation table hardware updates are enabled.
- For EL2 or EL3, translation table hardware updates are enabled.

For more information, see Possible implementation restrictions on using atomic instructions.

## D8.5.5 Use of the Contiguous bit with hardware updates to the translation tables

| R XDPXQ   | When hardware updates any of the AF, AP[2] or S2AP[1] either of the AF or AP[2] bits, then the update applies to a single translation table entry.                                                                                                                                                                                                                             |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R LCGVS   | If hardware updates a translation table entry, and if the Contiguous bit in that entry is 1, then the members in a group of contiguous translation table entries can have different AF, AP[2], and S2AP[1] values.                                                                                                                                                             |
| R GPHKF   | If all of the following apply, then the architecture does not require a hardware update of the AF: • An access is to a location translated by an entry that has the Contiguous bit set to 1. • At least one descriptor in the set of contiguous translation table entries has AF set to 1.                                                                                     |
| R JKCXG   | If all of the following apply, then the architecture does not require a hardware update of the AP[2] or S2AP[1] bit: • Awrite is done to a location translated by a descriptor that has the Contiguous bit set to 1. • The corresponding AP[2] or S2AP[1] bit in at least one descriptor in the set of contiguous translation table entries indicates that the entry is dirty. |
| I QDCMP   | The Contiguous bit permits, but does not require, hardware to hold a single entry in a TLB for the set of translation table entries in the group, and to have updated only one or more of the AF and the AP[2] bit or S2AP[1] bit in the single translation table entry that resulted in the TLB entry.                                                                        |
| I NFFSV   | Software is required to combine the AF values and AP[2] or S2AP[1] values across all translation table entries in a contiguous group to determine whether any of the entries have been accessed or are dirty.                                                                                                                                                                  |
| I QKKDC   | For more information on the Contiguous bit, see The Contiguous bit.                                                                                                                                                                                                                                                                                                            |