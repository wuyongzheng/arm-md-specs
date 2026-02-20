## D1.3 System register locking

RDJDVH

IDFJZG

All statements in this section require FEAT\_SRMASK.

Note

HCR\_EL2.E2H is RES1 when FEAT\_SRMASK is implemented.

Software can program the mask registers shown in the following table to mask individual control fields of the corresponding System registers, as follows:

- The EL1 mask registers mask EL1 control fields from EL1 MSR writes.
- The EL2 mask registers mask EL2 control fields from EL2 MSR writes.

For example, if TCRMASK\_EL1 is programmed to mask a TCR\_EL1 control field, then EL1 MSR writes to TCR\_EL1 do not update that masked field.

## Table D1-3 System registers and their corresponding mask registers

| System register   | Mask register   |
|-------------------|-----------------|
| ACTLR_EL1         | ACTLRMASK_EL1   |
| CPACR_EL1         | CPACRMASK_EL1   |
| SCTLR_EL1         | SCTLRMASK_EL1   |
| SCTLR2_EL1        | SCTLR2MASK_EL1  |
| TCR_EL1           | TCRMASK_EL1     |
| TCR2_EL1          | TCR2MASK_EL1    |
| ACTLR_EL2         | ACTLRMASK_EL2   |
| CPTR_EL2          | CPTRMASK_EL2    |
| SCTLR_EL2         | SCTLRMASK_EL2   |
| SCTLR2_EL2        | SCTLR2MASK_EL2  |
| TCR_EL2           | TCRMASK_EL2     |
| TCR2_EL2          | TCR2MASK_EL2    |

Using the mask registers makes it possible, for example, for EL1 to frequently change specific EL1 control fields without always trapping the EL1 MSR System register writes to EL2.

| R FHCYV   | EL1 is permitted to program an EL1 mask register when it is zero. Otherwise, the write to the mask register is UNDEFINED unless it is trapped. EL2 is permitted to program an EL2 mask register when it is zero. Otherwise, the write to the mask register is UNDEFINED.                                    |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I VGNST   | An attempt to program a nonzero mask register is only guaranteed to be UNDEFINED if there has been a Context synchronization event since the write that set it to the nonzero value and before the new attempt to program it. This is because the check of whether it is nonzero is an indirect read of it. |
| I QTNLT   | For each EL1 mask register: • HFGRTR2_EL2 contains a fine-grained trap control for EL1 reads. • HFGWTR2_EL2 contains a fine-grained trap control for EL1 writes.                                                                                                                                            |

## D1.3.1 EL1 System register alias names

| I QBPYD   | For each of the EL1 System registers in Table D1-3, FEAT_SRMASK provides an EL1 alias name , <SYSTEM REGISTER NAME>ALIAS_EL1. These are listed in System and Special-purpose register aliasing. • EL1 software that is aware of the presence of the EL1 alias names can use them when it is also aware that fine-grained traps are trapping EL1 writes to EL1 System registers.         |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I CWCFN   | The EL1 mask registers mask the EL1 alias names in addition to masking the corresponding EL1 System registers. For example, if TCRMASK_EL1 is programmed to mask a TCR_EL1 control field, then EL1 MSR writes to TCRALIAS_EL1 do not update that masked field.                                                                                                                          |
| R CSSSN   | MSR and MRS accesses to the EL1 alias names are direct accesses to the corresponding EL1 System registers. However, without explicit synchronization, the accesses might be reordered relative to MSR and MRS accesses to the EL1 System registers.                                                                                                                                     |
| I VPCLQ   | The accessibility from EL1 to each EL1 alias name is the same as for the corresponding EL1 System register, except for the opcode, and that there is a separate fine-grained trap control for each of reads and writes for the EL1 alias name: • HFGRTR2_EL2 contains the fine-grained trap control for EL1 reads. • HFGWTR2_EL2 contains the fine-grained trap control for EL1 writes. |

## D1.3.2 EL12 alias names for mask registers

IHFLBB Because HCR\_EL2.E2H is RES1 when FEAT\_SRMASK is implemented, FEAT\_SRMASK provides an EL12 alias name for each EL1 mask register in Table D1-3, for use by EL2 hypervisor software. See System and Special-purpose register aliasing.

## D1.3.3 Nested virtualization

- IGFHTJ

MSR writes that are transformed to stores by FEAT\_NV2 are not masked by the EL1 mask register configuration.