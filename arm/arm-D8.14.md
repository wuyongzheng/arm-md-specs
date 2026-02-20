## D8.14 Nested virtualization

| I FDMLZ   | Nested virtualization is an OPTIONAL feature that enables a Host hypervisor executing at EL2 to run a Guest hypervisor at EL1.                                                                                                                                    |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R QQDQK   | All statements in this section and subsections require implementation of FEAT_NV.                                                                                                                                                                                 |
| I CDTFC   | Nested virtualization adds the HCR_EL2.{NV, NV1, AT} fields.                                                                                                                                                                                                      |
| I WHFTT   | An implementation is permitted to cache the HCR_EL2.{NV, NV1} fields in a TLB.                                                                                                                                                                                    |
| I CQNPK   | If FEAT_E2H0 is not implemented, it is permitted to implement HCR_EL2.NV1 as RES0. See ID_AA64MMFR4_EL1.                                                                                                                                                          |
| S RHQHT   | If the Host hypervisor has set HCR_EL2.NV1 to 1 because a Guest hypervisor believes that HCR_EL2.E2H is 0, the Host hypervisor should also set both HCR_EL2.TVM and CPTR_EL2.TCPAC to 1 to trap Guest hypervisor accesses to EL1 System registers.                |
| I FPHRW   | Nested virtualization does not modify either self-hosted debug or the Performance Monitors Extension.                                                                                                                                                             |
| I FFWLP   | Arm assumes that the Host hypervisor traps accesses to the Breakpoint registers and Performance Monitors registers to EL2, so that it can process any accesses to these registers made by a Guest hypervisor or by a Guest OS running under the Guest hypervisor. |

## D8.14.1 Behavior when HCR\_EL2.NV is 1

IZMLPV

Nested Virtualization traps functionality that is permitted at EL2 and would be UNDEFINED at EL1 if HCR\_EL2.NV was 0.

ITZTZL

If HCR\_EL2.NV is 1 and the current Exception level is EL1, then all of the following apply:

- If a read access or write access from EL1 to one of the following System registers or Special-purpose registers occurs and that access is not UNDEFINED at EL2 in the current Security state and not trapped to EL3 by a higher priority trap, then that access is trapped to EL2 and reported using EC syndrome value 0x18 in ESR\_EL2:
- -Any System register accessed using MRS or MSR named *\_EL2, except all of the following:
- -SP\_EL2.
- -MECIDR\_EL2, MECID\_A0\_EL2, MECID\_A1\_EL2, MECID\_P0\_EL2, and MECID\_P1\_EL2.
- -VMECID\_A\_EL2 and VMECID\_P\_EL2.
- -Any System register accessed using MRS or MSR named *\_EL12.
- -Any System register accessed using MRS or MSR named *\_EL02.
- -Special-purpose registers SPSR\_irq, SPSR\_abt, SPSR\_und, and SPSR\_fiq, accessed using MRS or MSR .
- -Special-purpose register SP\_EL1 accessed using the dedicated MRS or MSR instruction.
- If one of the following instructions is executed from EL1, then the instruction is trapped to EL2 and reported using EC syndrome value 0x18 in ESR\_EL2:
- -Address Translation instructions that are accessible only from EL2 and above.
- -TLB maintenance instructions that are accessible only from EL2 and above.
- If the ERET , ERETAA , or ERETAB instruction is executed from EL1, then the instruction is trapped to EL2 and reported using EC syndrome value 0x1A in ESR\_EL2.
- If EL3 is not implemented and the Effective value of HCR\_EL2.TSC is 1, then when an SMC instruction is executed at EL1, all of the following apply:
- -The SMC instruction is trapped to EL2.
- -The exception is reported using EC syndrome value 0x17 in ESR\_EL2.

If HCR\_EL2.NV is 1 and the current Exception level is EL1, then EL1 read accesses to the CurrentEL register return a value of 0x2 in bits[3:2].

RGFLDX

## D8.14.2 Additional behavior when HCR\_EL2.NV is 1 and HCR\_EL2.NV1 is 0

IZJRNN

If the Effective value of HCR\_EL2.{NV, NV1} is {1, 0} and the current Exception level is EL1, then any exception taken from EL1 to EL1 causes SPSR\_EL1.M[3:2] to be set to 0b10 and not 0b01 .

## D8.14.3 Additional behavior when HCR\_EL2.NV is 1 and HCR\_EL2.NV1 is 1

IJKLJK

IFQZDC

IFWVWB

If the Effective value of HCR\_EL2.{NV, NV1} is {1, 1} and the current Exception level is EL1, then all of the following apply:

- If an access to one of the following registers occurs, then the access is trapped to EL2 and reported using EC syndrome value 0x18 in ESR\_EL2:
- -An access to VBAR\_EL1.
- -An access to ELR\_EL1.
- -An access to SPSR\_EL1.
- -If implemented, then an access from EL1 to SCXTNUM\_EL1.
- For Block descriptors and Page descriptors in the EL1&amp;0 translation regime, all of the following apply:
- -Block descriptor and Page descriptor bit[54] holds PXN, not UXN.
- -Block descriptor and Page descriptor bit[53] is RES0.
- -Block descriptor and Page descriptor bit[6], AP[1], is treated as 0 regardless of the actual value.
- For Table descriptors in the EL1&amp;0 translation regime, if hierarchical permissions are enabled, then all of the following apply:
- -Table descriptor bit[61], APTable[0], is treated as 0 regardless of the actual value.
- -Table descriptor bit[60] holds PXNTable, not UXNTable.
- -Table descriptor bit[59] is RES0.
- PSTATE.PAN is treated as 0 for all purposes except reading the value of the bit.
- The Effective value of PSTATE.UAO is 1.

Arm expects software to clear the HCR\_EL2.NV1 bit to 0 before permitting execution at EL0.

If ID\_AA64MMFR4\_EL1.E2H0 is 0b1110 , then HCR\_EL2.NV1 is RES0.

## D8.14.4 Behavior when HCR\_EL2.NV is 0 and HCR\_EL2.NV1 is 1

IKZNPS

If the Effective value of HCR\_EL2.{NV, NV1} is {0, 1} and the current Exception level is EL1, then one of the following CONSTRAINED UNPREDICTABLE behaviors apply:

- For all purposes other than reading back the value of the HCR\_EL2.NV bit, the implementation behaves as if HCR\_EL2.{NV, NV1} is {1, 1}.
- For all purposes other than reading back the value of the HCR\_EL2.NV1 bit, the implementation behaves as if HCR\_EL2.{NV, NV1} is {0, 0}.
- The implementation behaves as defined when HCR\_EL2.NV is 0, with HCR\_EL2.NV1 set to 1 having the effect of trapping to EL2 the same set of registers that are trapped when HCR\_EL2.{NV , NV1} is {1, 1}, as defined in IJKLJK.

## D8.14.5 Effect of HCR\_EL2.AT

IRBYYS

If HCR\_EL2.AT is 1, then all of the following are trapped to EL2 and reported using EC syndrome value 0x18 in ESR\_EL2:

- Executing AT S1E0R from EL1. · Executing AT S1E0W from EL1. · Executing AT S1E1R from EL1. · Executing AT S1E1W from EL1. · Executing AT S1E1RP from EL1. · Executing AT S1E1WP from EL1. · If FEAT\_ATS1A is implemented, executing AT S1E1A from EL1.

## D8.14.6 Enhanced support for nested virtualization

- IGDQNK Enhanced support for nested virtualization provides a mechanism for hardware to transform reads and writes from System registers into reads and writes from memory.

RJXWDQ

ITMCKW

IVGFWB

IZSQQK

- IRKLVD
- IDLGPW

All statements in this section and subsections require implementation of FEAT\_NV2.

If the Effective value of HCR\_EL2.NV2 is 1 and the current Exception level is EL1, then all of the following apply:

- Accesses to EL2 registers are redirected to EL1 registers.
- Accesses to System registers are transformed to memory accesses.

If the Effective value of HCR\_EL2.NV2 is 0, then the behavior of HCR\_EL2.{NV, NV1} is unchanged.

If ID\_AA64MMFR4\_EL1.NV\_frac is 0b0001 and HCR\_EL2.NV is 1, then the Effective value of HCR\_EL2.NV2 is 1.

## D8.14.6.1 Redirection of register accesses from EL2 to EL1

If the Effective value of HCR\_EL2.{NV, NV2} is {1, 1} and the current Exception level is EL1, then accesses to all of the following EL2 Special-purpose registers are redirected to the corresponding EL1 register:

- An access from EL1 to SPSR\_EL2 is redirected to SPSR\_EL1.
- An access from EL1 to ELR\_EL2 is redirected to ELR\_EL1.

If the Effective value of HCR\_EL2.{NV, NV2} is {1, 1} and the current Exception level is EL1, then accesses to all of the following EL2 System registers are redirected to the corresponding EL1 register:

- An access from EL1 to ESR\_EL2 is redirected to ESR\_EL1.
- An access from EL1 to FAR\_EL2 is redirected to FAR\_EL1.
- An access from EL1 to TFSR\_EL2 is redirected to TFSR\_EL1.
- IHFNHT For more information, see:
- op0 == 0b11 , Moves to and from Special-purpose registers.
- Instructions for accessing non-debug System registers.

## D8.14.6.2 Loads and stores generated by transforming register accesses

If the Effective value of HCR\_EL2.{NV, NV2} is {1, 1} and the current Exception level is EL1, then when an MRS or MSRinstruction is executed to access one of the registers listed in Table D8-120, all of the following apply:

- The instruction is treated as an instruction executed at EL1.
- The register accesses do not generate an exception to EL2.
- The register accesses are transformed to memory accesses.
- The memory accesses are treated as EL2 accesses.

When register accesses are transformed to memory accesses, all of the following information is used to form the memory address:

- Abase address that is stored in the VNCR\_EL2 register.
- For a register that is redirected to memory, a unique memory offset value.
- The memory address is a combination of the base address and the memory offset according to the formula SignExtend(VNCR\_EL2.BADDR : Offset&lt;11:0&gt;, 64) .
- When register accesses are transformed to memory accesses, the following table shows the unique memory offset that is assigned to the register.
- IKYDSS

ILKWDD

RCSRPQ

Table D8-120 Memory address offset associated with transformed register access

| Register access if the Effective value of HCR_EL2.NV1 is 0   | Register access if the Effective value of HCR_EL2.NV1 is 1   | Memory offset   |
|--------------------------------------------------------------|--------------------------------------------------------------|-----------------|
| VTTBR_EL2                                                    | VTTBR_EL2                                                    | 0x20            |
| VSTTBR_EL2                                                   | VSTTBR_EL2                                                   | 0x30            |
| VTCR_EL2                                                     | VTCR_EL2                                                     | 0x40            |
| VSTCR_EL2                                                    | VSTCR_EL2                                                    | 0x48            |
| VMPIDR_EL2                                                   | VMPIDR_EL2                                                   | 0x50            |
| CNTVOFF_EL2                                                  | CNTVOFF_EL2                                                  | 0x60            |
| HCR_EL2                                                      | HCR_EL2                                                      | 0x78            |
| HSTR_EL2                                                     | HSTR_EL2                                                     | 0x80            |
| VPIDR_EL2                                                    | VPIDR_EL2                                                    | 0x88            |
| TPIDR_EL2                                                    | TPIDR_EL2                                                    | 0x90            |
| HCRX_EL2                                                     | HCRX_EL2                                                     | 0xA0            |
| VNCR_EL2                                                     | VNCR_EL2                                                     | 0xB0            |
| CPACR_EL12                                                   | CPACR_EL1                                                    | 0x100           |
| CONTEXTIDR_EL12                                              | CONTEXTIDR_EL1                                               | 0x108           |
| SCTLR_EL12                                                   | SCTLR_EL1                                                    | 0x110           |
| ACTLR_EL1                                                    | ACTLR_EL1                                                    | 0x118           |
| TCR_EL12                                                     | TCR_EL1                                                      | 0x120           |
| AFSR0_EL12                                                   | AFSR0_EL1                                                    | 0x128           |
| AFSR1_EL12                                                   | AFSR1_EL1                                                    | 0x130           |
| ESR_EL12                                                     | ESR_EL1                                                      | 0x138           |
| MAIR_EL12                                                    | MAIR_EL1                                                     | 0x140           |
| AMAIR_EL12                                                   | AMAIR_EL1                                                    | 0x148           |
| MDSCR_EL1                                                    | MDSCR_EL1                                                    | 0x158           |
| SPSR_EL12                                                    | SPSR_EL1                                                     | 0x160           |
| CNTV_CVAL_EL02                                               | CNTV_CVAL_EL0                                                | 0x168           |
| CNTV_CTL_EL02                                                | CNTV_CTL_EL0                                                 | 0x170           |
| CNTP_CVAL_EL02                                               | CNTP_CVAL_EL0                                                | 0x178           |
| CNTP_CTL_EL02                                                | CNTP_CTL_EL0                                                 | 0x180           |
| SCXTNUM_EL12                                                 | SCXTNUM_EL1                                                  | 0x188           |
| TFSR_EL12                                                    | TFSR_EL1                                                     | 0x190           |
| HDFGRTR2_EL2                                                 | HDFGRTR2_EL2                                                 | 0x1A0           |
| CNTPOFF_EL2                                                  | CNTPOFF_EL2                                                  | 0x1A8           |
| HDFGWTR2_EL2                                                 | HDFGWTR2_EL2                                                 | 0x1B0           |
| HFGRTR_EL2                                                   | HFGRTR_EL2                                                   | 0x1B8           |
| HFGWTR_EL2                                                   | HFGWTR_EL2                                                   | 0x1C0           |
| HFGITR_EL2                                                   | HFGITR_EL2                                                   | 0x1C8           |
| HDFGRTR_EL2                                                  | HDFGRTR_EL2                                                  | 0x1D0           |
| HDFGWTR_EL2                                                  | HDFGWTR_EL2                                                  | 0x1D8           |

| Register access if the Effective value of HCR_EL2.NV1 is 0   | Register access if the Effective value of HCR_EL2.NV1 is 1   | Memory offset   |
|--------------------------------------------------------------|--------------------------------------------------------------|-----------------|
| ZCR_EL12                                                     | ZCR_EL1                                                      | 0x1E0           |
| HAFGRTR_EL2                                                  | HAFGRTR_EL2                                                  | 0x1E8           |
| SMCR_EL12                                                    | SMCR_EL1                                                     | 0x1F0           |
| SMPRIMAP_EL2                                                 | SMPRIMAP_EL2                                                 | 0x1F8           |
| TTBR0_EL12                                                   | TTBR0_EL1                                                    | 0x200           |
| TTBR1_EL12                                                   | TTBR1_EL1                                                    | 0x210           |
| FAR_EL12                                                     | FAR_EL1                                                      | 0x220           |
| ELR_EL12                                                     | ELR_EL1                                                      | 0x230           |
| SP_EL1                                                       | SP_EL1                                                       | 0x240           |
| VBAR_EL12                                                    | VBAR_EL1                                                     | 0x250           |
| TCR2_EL12                                                    | TCR2_EL1                                                     | 0x270           |
| SCTLR2_EL12                                                  | SCTLR2_EL1                                                   | 0x278           |
| MAIR2_EL12                                                   | MAIR2_EL1                                                    | 0x280           |
| AMAIR2_EL12                                                  | AMAIR2_EL1                                                   | 0x288           |
| PIRE0_EL12                                                   | PIRE0_EL1                                                    | 0x290           |
| PIRE0_EL1                                                    | PIRE0_EL2                                                    | 0x298           |
| PIR_EL12                                                     | PIR_EL1                                                      | 0x2A0           |
| POR_EL12                                                     | POR_EL1                                                      | 0x2A8           |
| S2PIR_EL2                                                    | S2PIR_EL2                                                    | 0x2B0           |
| S2POR_EL1                                                    | S2POR_EL1                                                    | 0x2B8           |
| HFGRTR2_EL2                                                  | HFGRTR2_EL2                                                  | 0x2C0           |
| HFGWTR2_EL2                                                  | HFGWTR2_EL2                                                  | 0x2C8           |
| PFAR_EL12                                                    | PFAR_EL1                                                     | 0x2D0           |
| HFGITR2_EL2                                                  | HFGITR2_EL2                                                  | 0x310           |
| SCTLRMASK_EL12                                               | SCTLRMASK_EL1                                                | 0x318           |
| CPACRMASK_EL12                                               | CPACRMASK_EL1                                                | 0x320           |
| SCTLR2MASK_EL12                                              | SCTLR2MASK_EL1                                               | 0x328           |
| TCRMASK_EL12                                                 | TCRMASK_EL1                                                  | 0x330           |
| TCR2MASK_EL12                                                | TCR2MASK_EL1                                                 | 0x338           |
| ACTLRMASK_EL12                                               | ACTLRMASK_EL1                                                | 0x340           |
| ICH_LR<n>_EL2                                                | ICH_LR<n>_EL2                                                | 0x400+8*n       |
| ICH_AP0R<n>_EL2                                              | ICH_AP0R<n>_EL2                                              | 0x480+8*n       |
| ICH_AP1R<n>_EL2                                              | ICH_AP1R<n>_EL2                                              | 0x4A0+8*n       |
| ICH_HCR_EL2                                                  | ICH_HCR_EL2                                                  | 0x4C0           |
| ICH_VMCR_EL2                                                 | ICH_VMCR_EL2                                                 | 0x4C8           |
| VDISR_EL2                                                    | VDISR_EL2                                                    | 0x500           |
| VSESR_EL2                                                    | VSESR_EL2                                                    | 0x508           |
| PMBLIMITR_EL1                                                | PMBLIMITR_EL1                                                | 0x800           |
| PMBPTR_EL1                                                   | PMBPTR_EL1                                                   | 0x810           |
| PMBSR_EL1                                                    | PMBSR_EL1                                                    | 0x820           |

| Register access if the Effective value of HCR_EL2.NV1 is 0   | Register access if the Effective value of HCR_EL2.NV1 is 1   | Memory offset   |
|--------------------------------------------------------------|--------------------------------------------------------------|-----------------|
| PMSCR_EL12                                                   | PMSCR_EL1                                                    | 0x828           |
| PMSEVFR_EL1                                                  | PMSEVFR_EL1                                                  | 0x830           |
| PMSICR_EL1                                                   | PMSICR_EL1                                                   | 0x838           |
| PMSIRR_EL1                                                   | PMSIRR_EL1                                                   | 0x840           |
| PMSLATFR_EL1                                                 | PMSLATFR_EL1                                                 | 0x848           |
| PMSNEVFR_EL1                                                 | PMSNEVFR_EL1                                                 | 0x850           |
| PMSDSFR_EL1                                                  | PMSDSFR_EL1                                                  | 0x858           |
| TRFCR_EL12                                                   | TRFCR_EL1                                                    | 0x880           |
| TRCITECR_EL12                                                | TRCITECR_EL1                                                 | 0x888           |
| GCSPR_EL12                                                   | GCSPR_EL1                                                    | 0x8C0           |
| GCSCR_EL12                                                   | GCSCR_EL1                                                    | 0x8D0           |
| BRBCR_EL12                                                   | BRBCR_EL1                                                    | 0x8E0           |
| SPMACCESSR_EL12                                              | SPMACCESSR_EL1                                               | 0x8E8           |
| MPAM1_EL12                                                   | MPAM1_EL1                                                    | 0x900           |
| MPAMBW1_EL12                                                 | MPAMBW1_EL1                                                  | 0x908           |
| MPAMBWCAP_EL2                                                | MPAMBWCAP_EL2                                                | 0x910           |
| MPAMHCR_EL2                                                  | MPAMHCR_EL2                                                  | 0x930           |
| MPAMVPMV_EL2                                                 | MPAMVPMV_EL2                                                 | 0x938           |
| MPAMVPM0_EL2                                                 | MPAMVPM0_EL2                                                 | 0x940           |
| MPAMVPM1_EL2                                                 | MPAMVPM1_EL2                                                 | 0x948           |
| MPAMVPM2_EL2                                                 | MPAMVPM2_EL2                                                 | 0x950           |
| MPAMVPM3_EL2                                                 | MPAMVPM3_EL2                                                 | 0x958           |
| MPAMVPM4_EL2                                                 | MPAMVPM4_EL2                                                 | 0x960           |
| MPAMVPM5_EL2                                                 | MPAMVPM5_EL2                                                 | 0x968           |
| MPAMVPM6_EL2                                                 | MPAMVPM6_EL2                                                 | 0x970           |
| MPAMVPM7_EL2                                                 | MPAMVPM7_EL2                                                 | 0x978           |
| AMEVCNTVOFF0<n>_EL2                                          | AMEVCNTVOFF0<n>_EL2                                          | 0xA00+8*n       |
| AMEVCNTVOFF1<n>_EL2                                          | AMEVCNTVOFF1<n>_EL2                                          | 0xA80+8*n       |

| R QSKNK   | Unallocated memory offset values up to but not including 0x1000 are reserved.                                                                                                                                         |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R JSCYJ   | When a register access instruction targets a register that is not implemented, the PE treats access to that register as unallocated.                                                                                  |
| R DHMDM   | When a System register access instruction is trapped by either or both of the Effective values of HCR_EL2.{NV, NV1}, then the instruction is transformed into a memory access instruction instead of creating a trap. |
| I TFJCH   | When a System register access instruction is not trapped by either or both of the Effective values of HCR_EL2.{NV, NV1}, then the trap is subject to the exception prioritization rules.                              |
| I RSCBR   | Accesses to all of the following registers that affect hypervisor execution by controlling the event stream are not transformed into memory accesses: • CNTHCTL_EL2.                                                  |

- If the Effective value of HCR\_EL2.NV1 is 0, then CNTKCTL\_EL12.

RVFMQB

IZLKQZ

- If the Effective value of HCR\_EL2.NV1 is 1, then CNTKCTL\_EL1.

When an MSR or MRS System register access is transformed into a memory access, the memory access has all of the following properties:

- The memory access is translated by one of the following:
- -If the Effective value of HCR\_EL2.E2H is 0, then the EL2 translation regime.
- -If the Effective value of HCR\_EL2.E2H is 1, then the EL2&amp;0 translation regime.
- The endianness of the memory access is defined by SCTLR\_EL2.EE.
- The memory access is 64-bit single-copy atomic aligned to 64 bits.
- The memory access does not have Acquire or Release semantics.
- The memory access is ordered as if it is generated by a load or store instruction.
- The memory access behaves as if PSTATE.PAN is 0.
- For fields in a transformed System register that are defined to be RES0 or RES1, the memory access does not check that the fields are set correctly, nor are they forced to their dedicated value.

RBSBZP When an MSRR or MRRS System register access is transformed into a memory access, the memory access has all of the following properties:

- The memory access is 128-bit aligned.
- If the target memory region is Inner and Outer Write-back Cacheable, then the access is 128-bit single-copy atomic.
- If the target memory region is not Inner and Outer Write-back Cacheable, then it is CONSTRAINED UNPREDICTABLE whether the access is 64-bit or 128-bit single-copy atomic.
- All other properties of the memory access are the same as for MSR and MRS operations that are transformed to memory accesses.

ICRPJG All memory address offset values associated with transformed register accesses for 128-bit System registers are aligned to 16-bytes.

ITRBJN For more information, see Prioritization of Synchronous exceptions taken to AArch64 state.

## D8.14.6.3 Exceptions from transformed register accesses

IDBTLM If the Effective value of HCR\_EL2.{NV, NV2} is {1, 1}, then any exception taken from EL1 and taken to EL1 causes the SPSR\_EL1.M[3:2] to be set to 0b10 and not 0b01 .

RYWCZS If a System register access is transformed to a memory access, then when the memory access generates a Data Abort, the resulting fault has all of the following properties:

- The fault is taken to EL2, using the standard vector offset for exceptions from EL1 to EL2.
- The fault is reported as a Data Abort from the current Exception level with the ESR\_EL2.EC code 0x25 .
- FAR\_EL2 is updated to hold the faulting address.

RFRWJX If a System register access is transformed to a memory access, then when the memory access generates a synchronous External abort and External aborts are not configured to be taken to EL3, the resulting fault has all of the following properties:

- The fault is taken to EL2, using the standard vector offset for exceptions from EL1 to EL2.
- The fault is reported as a Data Abort from the current Exception level with the ESR\_EL2.EC code 0x25 .

The VNCR field in ESR\_EL2 and ESR\_EL3 identifies whether the fault came from use of VNCR\_EL2 by EL1.

IBKFTF For more information, see ISS encoding for an exception from a Data Abort.

## D8.14.6.4 Interaction with self-hosted and External debug

When a System register access is transformed into a memory access, all of the following operations treat the instruction as being executed at EL1:

- PMUevents filtered by Exception level.
- For trace or Statistical Profiling, instructions filtered by Exception level.
- Checking the instruction address against breakpoint registers or trace resources.

RCJQGX

RZZSMN

When a System register access is transformed into a memory access, all of the following operations treat the memory access as being executed at EL2:

- The memory access is checked against the watchpoint registers.
- The memory address is recorded in a Statistical Profiling record.

RZNPSG If all of the following apply, then it is CONSTRAINED UNPREDICTABLE whether there is a watchpoint match:

- ASystem register access is transformed into a memory access.
- The memory access matches an EL2 access in the watchpoint registers.
- Awatchpoint is linked to a context-aware breakpoint that is programmed to match the value held in CONTEXTIDR\_EL1 or VMID.

RDDNDL If all of the following apply, then a watchpoint match generates a Watchpoint debug event:

- ASystem register access is transformed into a memory access.
- EDSCR.HDE is 1.
- Halting is allowed.
- OS Lock is unlocked.

RYGWHK If all of the following apply, then a watchpoint match generates a Watchpoint exception:

- ASystem register access is transformed into a memory access.
- EDSCR.HDE is 0 or halting is prohibited in current security state.
- Debug exceptions are enabled at EL2.
- OS Lock is unlocked.
- RDGCTK If a System register access is transformed to a memory access, then when a watchpoint match generates a Watchpoint exception, the resulting exception has all of the following properties:
- The exception is taken to EL2.
- The fault is reported as a Watchpoint from the current Exception level with the ESR\_EL2.EC code 0x35 .
- FAR\_EL2 is updated to hold the watchpointed address.
- RVYZMX If a System register access is transformed to a memory access, then when a Watchpoint exception is generated, the VNCRfield in ESR\_EL2 identifies whether the Watchpoint exception came from use of VNCR\_EL2 by EL1.
- RHZJLY If a System register access is transformed to a memory access, then the resulting loads and stores are treated by the Performance Monitors as Memory-read operations and Memory-write operations.
- RMVNHT If a System register access is transformed to a memory access, then when the Statistical Profiling Unit selects the instruction generating the memory access for profiling, it records the operation as a Load/Store operation.
- RZVXYL If a System register access is transformed to a memory access, then when the Statistical Profiling Unit selects the instruction generating the memory access for profiling and Statistical Profiling is disabled at EL2, the V A for the memory access is not recorded.