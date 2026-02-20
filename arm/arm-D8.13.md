## D8.13 Virtualization Host Extensions

| I QJTJN   | Virtualization Host Extensions provide enhanced support for a Type 2 virtualization solution, where there is a Host OS that is either more privileged than the hypervisor or is the hypervisor.   |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R SJSDF   | All statements in this chapter require implementation of FEAT_VHE.                                                                                                                                |
| R CSTLG   | If and only if an implementation includes EL2 using AArch64, then Virtualization Host Extensions, FEAT_VHE, can apply.                                                                            |

RGNLPT

FEAT\_VHE adds all of the following state:

- The HCR\_EL2.E2H configuration bit.
- The CONTEXTIDR\_EL2 register, which has the same format and contents as the CONTEXTIDR\_EL1 register.
- The TTBR1\_EL2 register, which has the same format and contents as the TTBR1\_EL1 register.
- The CNTHV\_CTL\_EL2, CNTHV\_CVAL\_EL2, and CNTHV\_TVAL\_EL2 registers, which have the same format and contents as the CNTV\_CTL\_EL0, CNTV\_CVAL\_EL0, and CNTV\_TVAL\_EL0 registers, respectively.
- An EL2 virtual timer with all of the following properties:
- -It is accessed using the CNTHV\_CTL\_EL2, CNTHV\_CVAL\_EL2, and CNTHV\_TVAL\_EL2 registers.
- -The virtual offset is treated as 0.

## D8.13.1 Behavior of HCR\_EL2.E2H

ISSMWM

Setting HCR\_EL2.E2H to 1 enables a configuration where a host operating system is running in EL2, and the host operating system applications are running in EL0. The host operating system might also manage guest virtual machines that run in EL1&amp;0, with stage 2 translation enabled and controlled by the host operating system.

ICDMXB HCR\_EL2.E2H is RES1 unless FEAT\_E2H0 is implemented. Arm deprecates setting HCR\_EL2.E2H to 0.

RVJBPM If the Effective value of HCR\_EL2.E2H is 0, then all of the following apply:

- Execution at EL2 uses the EL2 translation regime.
- All of the following effects apply to the contents of TTBR1\_EL2:
- -The contents can be read by an MRS instruction and written by an MSR instruction.
- -For all other hardware operations, the contents are ignored.
- The Context ID matching breakpoint has all of the following properties:
- -It is disabled at EL2.
- -It uses the value of CONTEXTIDR\_EL1 at EL0 and EL1.

If the Effective value of HCR\_EL2.E2H is 1, then the translation regime controlled by TCR\_EL2 is the EL2&amp;0

translation regime.

HCR\_EL2.E2H is permitted to be cached in a TLB, and EL2 software is expected to perform a TLBI ALLE2 operation after changing the value of HCR\_EL2.E2H.

All of the following are properties of the EL2&amp;0 translation regime:

- The EL2&amp;0 translation regime behaves the same as stage 1 in the EL1&amp;0 translation regime and uses an upper address range translated by tables pointed to by TTBR1\_EL2.
- TTBR0\_EL2 translates the lower address range of the EL2&amp;0 translation regime and is extended to have the same format and contents as TTBR0\_EL1.
- The Privileged Access Never mechanism applies to data accesses from EL2.
- When CNTVCT\_EL0 is read from EL2, the virtual offset is reported as 0.
- All of the following registers are redefined:
- -CNTHCTL\_EL2.
- -CPTR\_EL2.
- -TCR\_EL2.

RMNWSS

ISTSYY

RQXCQP

RBLXMQ

RFLVFR

RVMWQQ

RXCLCK

- RKJKRH

If the Effective value of HCR\_EL2.E2H is 1, then all of the following effects to the Context ID apply:

- When executing at EL2, a Context ID matching breakpoint uses CONTEXTIDR\_EL2.
- Both VMID and VMID plus Context ID matching breakpoints do not match at EL2.

If the Effective value of HCR\_EL2.{E2H, TGE} is {1, 0}, then accesses from EL1 and EL0 use the EL1&amp;0 translation regime.

If the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, then when executing at EL0, all of the following apply:

- The EL2&amp;0 translation regime is used and accesses are treated as unprivileged.
- AContext ID matching breakpoint uses CONTEXTIDR\_EL2.
- The following timer registers, and their equivalent AArch32 registers, are redefined to access the associated EL2 register, rather than accessing the EL0 register:
- -CNTP\_CTL\_EL0.
- -CNTP\_CVAL\_EL0.
- -CNTP\_TVAL\_EL0.
- -CNTV\_CTL\_EL0.
- -CNTV\_CVAL\_EL0.
- -CNTV\_TVAL\_EL0.
- Both VMID and VMID plus Context ID matching breakpoints do not match at EL0.

RCFMND If the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, then when executing at EL2, all of the following apply:

- The EL2&amp;0 translation regime is used.
- For permission and watchpoint checking, the behavior of unprivileged memory access instructions executed at EL2 is determined by the Effective value of PSTATE.UAO.

If the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, then all of the following register effects apply:

- Except for the purpose of reading the value held in the register, some fields in HCR\_EL2 and all fields in HSTR\_EL2 are treated as effectively having a specific value.
- SCTLR\_EL2 is redefined in all of the following ways:
- -Additional fields from SCTLR\_EL1 are included.
- -The register applies to execution at EL0.
- When CNTVCT\_EL0 is read from EL0 or EL2, the virtual offset is treated as 0.
- SCTLR\_EL1.UMA and SCTLR\_EL1.A bit are both treated as 0 for all purposes other than reading the value of the register.

RXXZKM If the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, then when an exception is taken from EL0 to EL2, the value of the HCR\_EL2.RW bit is ignored when determining the exception vector offset to use.

RQWHVM

If the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, then the TLB maintenance and address translation

- instructions that apply to the EL1&amp;0 translation regime are redefined to apply to the EL2&amp;0 translation regime.
- RHGWKR If the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, then when executing at EL2 or EL0, any physical interrupt

that is configured to be taken at EL2 is subject to the PSTATE.{D, A, I, F} interrupt masks, and if FEAT\_NMI is implemented, then the effect of PSTATE.ALLINT.

For more information, see The PSTATE debug mask bit, D and Asynchronous exception masking.

If the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, then all of the following apply to EL1:

- Access from EL1 is not possible.
- CPACR\_EL1 does not cause any instructions to be trapped to EL1.
- CNTKCTL\_EL1 does not cause any instructions to be trapped to EL1, and the event stream caused by CNTKCTL\_EL1 is disabled.

## D8.13.2 System and Special-purpose register redirection

RJGGMV

If all of the conditions in the following list are true, then the System register mapping in the following table applies:

- The PE is executing at EL2.
- The Effective value of HCR\_EL2.E2H is 1.

## Table D8-113 System register redirection

| Specified EL1 System register   | Equivalent EL2 System register accessed at EL2   |
|---------------------------------|--------------------------------------------------|
| ACTLRMASK_EL1                   | ACTLRMASK_EL2                                    |
| AFSR0_EL1                       | AFSR0_EL2                                        |
| AFSR1_EL1                       | AFSR1_EL2                                        |
| AMAIR_EL1                       | AMAIR_EL2                                        |
| AMAIR2_EL1                      | AMAIR2_EL2                                       |
| BRBCR_EL1                       | BRBCR_EL2                                        |
| CPACRMASK_EL1                   | CPTRMASK_EL2                                     |
| CNTKCTL_EL1                     | CNTHCTL_EL2                                      |
| CONTEXTIDR_EL1                  | CONTEXTIDR_EL2                                   |
| CPACR_EL1                       | CPTR_EL2                                         |
| ESR_EL1                         | ESR_EL2                                          |
| FAR_EL1                         | FAR_EL2                                          |
| GCSCR_EL1                       | GCSCR_EL2                                        |
| GCSPR_EL1                       | GCSPR_EL2                                        |
| MAIR_EL1                        | MAIR_EL2                                         |
| MAIR2_EL1                       | MAIR2_EL2                                        |
| MPAM1_EL1                       | MPAM2_EL2                                        |
| MPAMBW1_EL1                     | MPAMBW2_EL2                                      |
| PFAR_EL1                        | PFAR_EL2                                         |
| PIR_EL1                         | PIR_EL2                                          |
| PIRE0_EL1                       | PIRE0_EL2                                        |
| PMSCR_EL1                       | PMSCR_EL2                                        |
| POR_EL1                         | POR_EL2                                          |
| SCTLR_EL1                       | SCTLR_EL2                                        |
| SCTLR2_EL1                      | SCTLR2_EL2                                       |
| SCTLRMASK_EL1                   | SCTLRMASK_EL2                                    |
| SCTLR2MASK_EL1                  | SCTLR2MASK_EL2                                   |
| SCXTNUM_EL1                     | SCXTNUM_EL2                                      |
| SMCR_EL1                        | SMCR_EL2                                         |
| SPMACCESSR_EL1                  | SPMACCESSR_EL2                                   |
| TCR_EL1                         | TCR_EL2                                          |
| TCR2_EL1                        | TCR2_EL2                                         |
| TCRMASK_EL1                     | TCRMASK_EL2                                      |
| TCR2MASK_EL1                    | TCR2MASK_EL2                                     |
| TFSR_EL1                        | TFSR_EL2                                         |

| Specified EL1 System register   | Equivalent EL2 System register accessed at EL2   |
|---------------------------------|--------------------------------------------------|
| TRCITECR_EL1                    | TRCITECR_EL2                                     |
| TRFCR_EL1                       | TRFCR_EL2                                        |
| TTBR0_EL1                       | TTBR0_EL2                                        |
| TTBR1_EL1                       | TTBR1_EL2                                        |
| VBAR_EL1                        | VBAR_EL2                                         |
| ZCR_EL1                         | ZCR_EL2                                          |

## RRZRWZ

If all of the conditions in the following list are true, then the System register mapping in the following table applies:

- The PE is executing at EL2.
- The Effective value of HCR\_EL2.E2H is 1.
- The Effective value of SCR\_EL3.NS is 1.

Table D8-114 Additional System register redirection when the Effective value of SCR\_EL3.NS is 1

| Specified System register   | Equivalent EL2 System register accessed at EL2   |
|-----------------------------|--------------------------------------------------|
| CNTP_CTL_EL0                | CNTHP_CTL_EL2                                    |
| CNTP_CVAL_EL0               | CNTHP_CVAL_EL2                                   |
| CNTP_TVAL_EL0               | CNTHP_TVAL_EL2                                   |
| CNTV_CTL_EL0                | CNTHV_CTL_EL2                                    |
| CNTV_CVAL_EL0               | CNTHV_CVAL_EL2                                   |
| CNTV_TVAL_EL0               | CNTHV_TVAL_EL2                                   |

RLLSLV

If all of the conditions in the following list are true, then the System register mapping in the following table applies:

- The PE is executing at EL2.
- The Effective value of HCR\_EL2.E2H is 1.
- The Effective value of SCR\_EL3.NS is 0.

Table D8-115 Additional System register redirection when the Effective value of SCR\_EL3.NS is 0

| Specified EL1 System register   | Equivalent EL2 System register accessed at EL2   |
|---------------------------------|--------------------------------------------------|
| CNTP_CTL_EL0                    | CNTHPS_CTL_EL2                                   |
| CNTP_CVAL_EL0                   | CNTHPS_CVAL_EL2                                  |
| CNTP_TVAL_EL0                   | CNTHPS_TVAL_EL2                                  |
| CNTV_CTL_EL0                    | CNTHVS_CTL_EL2                                   |
| CNTV_CVAL_EL0                   | CNTHVS_CVAL_EL2                                  |
| CNTV_TVAL_EL0                   | CNTHVS_TVAL_EL2                                  |

## RZNNRM

If all of the conditions in the following list are true, then the Special-purpose register mapping in the following table applies:

- The PE is executing at EL2.
- The Effective value of HCR\_EL2.E2H is 1.

## Table D8-116 Special-purpose register redirection

| Specified EL1 Special-purpose register   | Equivalent EL2 Special-purpose register accessed at EL2   |
|------------------------------------------|-----------------------------------------------------------|
| ELR_EL1                                  | ELR_EL2                                                   |
| SPSR_EL2                                 | SPSR_EL1                                                  |

IWJCBD

For more information, see System and Special-purpose register aliasing.

## D8.13.3 System and Special-purpose register aliasing

RKSPRM

If all of the conditions in the following list are true, then the System register mapping in the following table applies:

- FEAT\_SRMASK is implemented.
- The PE is executing at EL1.

## Table D8-117 EL1 System register aliases

| Alias mnemonic   | EL1 System register accessed at EL1   |
|------------------|---------------------------------------|
| ACTLRALIAS_EL1   | ACTLR_EL1                             |
| CPACRALIAS_EL1   | CPACR_EL1                             |
| SCTLRALIAS_EL1   | SCTLR_EL1                             |
| SCTLR2ALIAS_EL1  | SCTLR2_EL1                            |
| TCRALIAS_EL1     | TCR_EL1                               |
| TCR2ALIAS_EL1    | TCR2_EL1                              |

RPHHPL

If all of the conditions in the following list are true, then the System register mapping in the following table applies. The aliases are UNDEFINED at EL1 and EL0.

- EL2 is enabled in the current Security state.
- The Effective value of HCR\_EL2.E2H is 1.
- The PE is executing at EL2 or EL3.

## Table D8-118 System register aliases

| Alias mnemonic   | EL1 or EL0 System register accessed at EL2 or EL3   |
|------------------|-----------------------------------------------------|
| ACTLRMASK_EL12   | ACTLRMASK_EL1                                       |
| AFSR0_EL12       | AFSR0_EL1                                           |
| AFSR1_EL12       | AFSR1_EL1                                           |
| AMAIR_EL12       | AMAIR_EL1                                           |
| AMAIR2_EL12      | AMAIR2_EL1                                          |
| BRBCR_EL12       | BRBCR_EL1                                           |
| CNTKCTL_EL12     | CNTKCTL_EL1                                         |

| Alias mnemonic   | EL1 or EL0 System register accessed at EL2 or EL3   |
|------------------|-----------------------------------------------------|
| CNTP_CTL_EL02    | CNTP_CTL_EL0                                        |
| CNTP_CVAL_EL02   | CNTP_CVAL_EL0                                       |
| CNTP_TVAL_EL02   | CNTP_TVAL_EL0                                       |
| CNTV_CTL_EL02    | CNTV_CTL_EL0                                        |
| CNTV_CVAL_EL02   | CNTV_CVAL_EL0                                       |
| CNTV_TVAL_EL02   | CNTV_TVAL_EL0                                       |
| CONTEXTIDR_EL12  | CONTEXTIDR_EL1                                      |
| CPACR_EL12       | CPACR_EL1                                           |
| CPACRMASK_EL12   | CPACRMASK_EL1                                       |
| ESR_EL12         | ESR_EL1                                             |
| FAR_EL12         | FAR_EL1                                             |
| GCSCR_EL12       | GCSCR_EL1                                           |
| GCSPR_EL12       | GCSPR_EL1                                           |
| MAIR_EL12        | MAIR_EL1                                            |
| MAIR2_EL12       | MAIR2_EL1                                           |
| MPAM1_EL12       | MPAM1_EL1                                           |
| MPAMBW1_EL12     | MPAMBW1_EL1                                         |
| PFAR_EL12        | PFAR_EL1                                            |
| PIR_EL12         | PIR_EL1                                             |
| PIRE0_EL12       | PIRE0_EL1                                           |
| PMSCR_EL12       | PMSCR_EL1                                           |
| POR_EL12         | POR_EL1                                             |
| SCTLR_EL12       | SCTLR_EL1                                           |
| SCTLRMASK_EL12   | SCTLRMASK_EL1                                       |
| SCTLR2_EL12      | SCTLR2_EL1                                          |
| SCTLR2MASK_EL12  | SCTLR2MASK_EL1                                      |
| SCXTNUM_EL12     | SCXTNUM_EL1                                         |
| SMCR_EL12        | SMCR_EL1                                            |
| SPMACCESSR_EL12  | SPMACCESSR_EL1                                      |
| TCR_EL12         | TCR_EL1                                             |
| TCRMASK_EL12     | TCRMASK_EL1                                         |
| TCR2_EL12        | TCR2_EL1                                            |
| TCR2MASK_EL12    | TCR2MASK_EL1                                        |
| TFSR_EL12        | TFSR_EL1                                            |
| TRCITECR_EL12    | TRCITECR_EL1                                        |
| TRFCR_EL12       | TRFCR_EL1                                           |
| TTBR0_EL12       | TTBR0_EL1                                           |
| TTBR1_EL12       | TTBR1_EL1                                           |
| VBAR_EL12        | VBAR_EL1                                            |
| ZCR_EL12         | ZCR_EL1                                             |

RKTWST

If all of the conditions in the following list are true, then the Special-purpose register mapping in the following table applies. The aliases are UNDEFINED at EL1 and EL0.

- EL2 is enabled in the current Security state.
- The Effective value of HCR\_EL2.E2H is 1.
- The PE is executing at EL2 or EL3.

Table D8-119 Special-purpose register aliases

| Alias mnemonic   | Equivalent EL1 Special-purpose register accessed at EL2 or EL3   |
|------------------|------------------------------------------------------------------|
| ELR_EL12         | ELR_EL1                                                          |
| SPSR_EL12        | SPSR_EL1                                                         |

IZXNTN

For more information, see System and Special-purpose register redirection.