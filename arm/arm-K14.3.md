## K14.3 Functional index of AArch64 registers and System instructions

This section is an index of the AArch64 registers and System instructions, divided by functional group. Each of the following sections lists the registers for a functional group:

- Special-purpose registers.
- VMSA-specific registers.
- ID registers.
- Performance monitors registers.
- Activity monitors registers.
- Debug registers.
- Trace registers.
- Branch Record Buffer registers.
- RAS registers.
- Root Security state registers.
- Memory Partitioning and Monitoring registers.
- Generic timer registers.
- Cache maintenance system instructions.
- Address translation system instructions.
- TLB maintenance system instructions.
- Prediction restriction System instructions.
- Base system registers.

## K14.3.1 Special-purpose registers

This section is an index to the registers in the Special-purpose registers functional group.

## Table K14-10 Special-purpose registers

| Register   | Description, see                           |
|------------|--------------------------------------------|
| DLR_EL0    | Debug Link Register                        |
| DSPSR_EL0  | Debug Saved Program Status Register        |
| ELR_EL1    | Exception Link Register (EL1)              |
| ELR_EL2    | Exception Link Register (EL2)              |
| ELR_EL3    | Exception Link Register (EL3)              |
| SP_EL0     | Stack Pointer (EL0)                        |
| SP_EL1     | Stack Pointer (EL1)                        |
| SP_EL2     | Stack Pointer (EL2)                        |
| SP_EL3     | Stack Pointer (EL3)                        |
| SPSR_abt   | Saved Program Status Register (Abort mode) |
| SPSR_EL1   | Saved Program Status Register (EL1)        |
| SPSR_EL2   | Saved Program Status Register (EL2)        |
| SPSR_EL3   | Saved Program Status Register (EL3)        |
| SPSR_fiq   | Saved Program Status Register (FIQ mode)   |

## K14.3.2 VMSA-specific registers

This section is an index to the registers in the Virtual memory control registers functional group.

## Table K14-11 VMSA-specific registers

| Register       | Description, see                                                |
|----------------|-----------------------------------------------------------------|
| AMAIR2_EL1     | Extended Auxiliary Memory Attribute Indirection Register (EL1)  |
| AMAIR2_EL2     | Extended Auxiliary Memory Attribute Indirection Register (EL2)  |
| AMAIR2_EL3     | Extended Auxiliary Memory Attribute Indirection Register (EL3)  |
| AMAIR_EL1      | Auxiliary Memory Attribute Indirection Register (EL1)           |
| AMAIR_EL2      | Auxiliary Memory Attribute Indirection Register (EL2)           |
| AMAIR_EL3      | Auxiliary Memory Attribute Indirection Register (EL3)           |
| CONTEXTIDR_EL1 | Context ID Register (EL1)                                       |
| CONTEXTIDR_EL2 | Context ID Register (EL2)                                       |
| DACR32_EL2     | Domain Access Control Register                                  |
| GPCBW_EL3      | Granule Protection Check Bypass Window Register (EL3)           |
| GPCCR_EL3      | Granule Protection Check Control Register (EL3)                 |
| GPTBR_EL3      | Granule Protection Table Base Register                          |
| HACDBSBR_EL2   | Hardware Accelerator for Cleaning Dirty State Base Register     |
| HACDBSCONS_EL2 | Hardware Accelerator for Cleaning Dirty State Consumer Register |
| HDBSSBR_EL2    | Hardware Dirty State Tracking Structure Base Register           |
| HDBSSPROD_EL2  | Hardware Dirty State Tracking Structure Producer Register       |
| LORC_EL1       | LORegion Control (EL1)                                          |
| LOREA_EL1      | LORegion End Address (EL1)                                      |
| LORID_EL1      | LORegionID (EL1)                                                |
| LORN_EL1       | LORegion Number (EL1)                                           |
| LORSA_EL1      | LORegion Start Address (EL1)                                    |
| MAIR2_EL1      | Extended Memory Attribute Indirection Register (EL1)            |
| MAIR2_EL2      | Extended Memory Attribute Indirection Register (EL2)            |
| MAIR2_EL3      | Extended Memory Attribute Indirection Register (EL3)            |
| MAIR_EL1       | Memory Attribute Indirection Register (EL1)                     |
| MAIR_EL2       | Memory Attribute Indirection Register (EL2)                     |

| Register   | Description, see                               |
|------------|------------------------------------------------|
| SPSR_irq   | Saved Program Status Register (IRQ mode)       |
| SPSR_und   | Saved Program Status Register (Undefined mode) |

| Register     | Description, see                                 |
|--------------|--------------------------------------------------|
| MAIR_EL3     | Memory Attribute Indirection Register (EL3)      |
| PIR_EL1      | Permission Indirection Register 1 (EL1)          |
| PIR_EL2      | Permission Indirection Register 2 (EL2)          |
| PIR_EL3      | Permission Indirection Register 3 (EL3)          |
| PIRE0_EL1    | Permission Indirection Register 0 (EL1)          |
| PIRE0_EL2    | Permission Indirection Register 0 (EL2)          |
| POR_EL0      | Permission Overlay Register 0 (EL0)              |
| POR_EL1      | Permission Overlay Register 1 (EL1)              |
| POR_EL2      | Permission Overlay Register 2 (EL2)              |
| POR_EL3      | Permission Overlay Register 3 (EL3)              |
| RCWMASK_EL1  | Read Check Write Instruction Mask (EL1)          |
| RCWSMASK_EL1 | Software Read Check Write Instruction Mask (EL1) |
| S2PIR_EL2    | Stage 2 Permission Indirection Register (EL2)    |
| S2POR_EL1    | Stage 2 Permission Overlay Register (EL1)        |
| TCR2_EL1     | Extended Translation Control Register (EL1)      |
| TCR2_EL2     | Extended Translation Control Register (EL2)      |
| TCR_EL1      | Translation Control Register (EL1)               |
| TCR_EL2      | Translation Control Register (EL2)               |
| TCR_EL3      | Translation Control Register (EL3)               |
| TTBR0_EL1    | Translation Table Base Register 0 (EL1)          |
| TTBR0_EL2    | Translation Table Base Register 0 (EL2)          |
| TTBR0_EL3    | Translation Table Base Register 0 (EL3)          |
| TTBR1_EL1    | Translation Table Base Register 1 (EL1)          |
| TTBR1_EL2    | Translation Table Base Register 1 (EL2)          |
| VTCR_EL2     | Virtualization Translation Control Register      |
| VTTBR_EL2    | Virtualization Translation Table Base Register   |

## K14.3.3 ID registers

This section is an index to the registers in the Identification registers functional group.

## Table K14-12 ID registers

| Register    | Description, see                 |
|-------------|----------------------------------|
| CCSIDR2_EL1 | Current Cache Size ID Register 2 |
| CCSIDR_EL1  | Current Cache Size ID Register   |
| CLIDR_EL1   | Cache Level ID Register          |
| CSSELR_EL1  | Cache Size Selection Register    |
| CTR_EL0     | Cache Type Register              |

| Register         | Description, see                             |
|------------------|----------------------------------------------|
| DCZID_EL0        | Data Cache Zero ID Register                  |
| GMID_EL1         | Multiple tag transfer ID Register            |
| ID_AA64AFR0_EL1  | AArch64 Auxiliary Feature Register 0         |
| ID_AA64AFR1_EL1  | AArch64 Auxiliary Feature Register 1         |
| ID_AA64DFR0_EL1  | AArch64 Debug Feature Register 0             |
| ID_AA64DFR1_EL1  | AArch64 Debug Feature Register 1             |
| ID_AA64DFR2_EL1  | AArch64 Debug Feature Register 2             |
| ID_AA64FPFR0_EL1 | AArch64 Floating-point Feature Register 0    |
| ID_AA64ISAR0_EL1 | AArch64 Instruction Set Attribute Register 0 |
| ID_AA64ISAR1_EL1 | AArch64 Instruction Set Attribute Register 1 |
| ID_AA64ISAR2_EL1 | AArch64 Instruction Set Attribute Register 2 |
| ID_AA64ISAR3_EL1 | AArch64 Instruction Set Attribute Register 3 |
| ID_AA64MMFR0_EL1 | AArch64 Memory Model Feature Register 0      |
| ID_AA64MMFR1_EL1 | AArch64 Memory Model Feature Register 1      |
| ID_AA64MMFR2_EL1 | AArch64 Memory Model Feature Register 2      |
| ID_AA64MMFR3_EL1 | AArch64 Memory Model Feature Register 3      |
| ID_AA64MMFR4_EL1 | AArch64 Memory Model Feature Register 4      |
| ID_AA64PFR0_EL1  | AArch64 Processor Feature Register 0         |
| ID_AA64PFR1_EL1  | AArch64 Processor Feature Register 1         |
| ID_AA64PFR2_EL1  | AArch64 Processor Feature Register 2         |
| ID_AA64SMFR0_EL1 | SMEFeature ID Register 0                     |
| ID_AA64ZFR0_EL1  | SVE Feature ID Register 0                    |
| ID_AFR0_EL1      | AArch32 Auxiliary Feature Register 0         |
| ID_DFR0_EL1      | AArch32 Debug Feature Register 0             |
| ID_DFR1_EL1      | AArch32 Debug Feature Register 1             |
| ID_ISAR0_EL1     | AArch32 Instruction Set Attribute Register 0 |
| ID_ISAR1_EL1     | AArch32 Instruction Set Attribute Register 1 |
| ID_ISAR2_EL1     | AArch32 Instruction Set Attribute Register 2 |
| ID_ISAR3_EL1     | AArch32 Instruction Set Attribute Register 3 |
| ID_ISAR4_EL1     | AArch32 Instruction Set Attribute Register 4 |
| ID_ISAR5_EL1     | AArch32 Instruction Set Attribute Register 5 |
| ID_ISAR6_EL1     | AArch32 Instruction Set Attribute Register 6 |
| ID_MMFR0_EL1     | AArch32 Memory Model Feature Register 0      |
| ID_MMFR1_EL1     | AArch32 Memory Model Feature Register 1      |
| ID_MMFR2_EL1     | AArch32 Memory Model Feature Register 2      |
| ID_MMFR3_EL1     | AArch32 Memory Model Feature Register 3      |
| ID_MMFR4_EL1     | AArch32 Memory Model Feature Register 4      |
| ID_MMFR5_EL1     | AArch32 Memory Model Feature Register 5      |
| ID_PFR0_EL1      | AArch32 Processor Feature Register 0         |
| ID_PFR1_EL1      | AArch32 Processor Feature Register 1         |

| Register    | Description, see                          |
|-------------|-------------------------------------------|
| ID_PFR2_EL1 | AArch32 Processor Feature Register 2      |
| MIDR_EL1    | Main ID Register                          |
| MPAMIDR_EL1 | MPAMIDRegister (EL1)                      |
| MPIDR_EL1   | Multiprocessor Affinity Register          |
| MVFR0_EL1   | AArch32 Media and VFP Feature Register 0  |
| MVFR1_EL1   | AArch32 Media and VFP Feature Register 1  |
| MVFR2_EL1   | AArch32 Media and VFP Feature Register 2  |
| REVIDR_EL1  | Revision ID Register                      |
| SMIDR_EL1   | Streaming Mode Identification Register    |
| VMPIDR_EL2  | Virtualization Multiprocessor ID Register |
| VPIDR_EL2   | Virtualization Processor ID Register      |

## K14.3.4 Performance monitors registers

This section is an index to the registers in the Performance Monitors registers functional group.

## Table K14-13 Performance monitors registers

| Register       | Description, see                                            |
|----------------|-------------------------------------------------------------|
| PMCCFILTR_EL0  | Performance Monitors Cycle Count Filter Register            |
| PMCCNTR_EL0    | Performance Monitors Cycle Count Register                   |
| PMCCNTSVR_EL1  | Performance Monitors Cycle Count Saved Value Register       |
| PMCEID0_EL0    | Performance Monitors Common Event Identification Register 0 |
| PMCEID1_EL0    | Performance Monitors Common Event Identification Register 1 |
| PMCNTENCLR_EL0 | Performance Monitors Count Enable Clear Register            |
| PMCNTENSET_EL0 | Performance Monitors Count Enable Set Register              |
| PMCR_EL0       | Performance Monitors Control Register                       |
| PMECR_EL1      | Performance Monitors Extended Control Register (EL1)        |
| PMIAR_EL1      | Performance Monitors Instruction Address Register           |
| PMICFILTR_EL0  | Performance Monitors Instruction Counter Filter Register    |
| PMICNTR_EL0    | Performance Monitors Instruction Counter Register           |
| PMINTENCLR_EL1 | Performance Monitors Interrupt Enable Clear Register        |
| PMINTENSET_EL1 | Performance Monitors Interrupt Enable Set Register          |
| PMMIR_EL1      | Performance Monitors Machine Identification Register        |
| PMOVSCLR_EL0   | Performance Monitors Overflow Flag Status Clear Register    |
| PMOVSSET_EL0   | Performance Monitors Overflow Flag Status Set Register      |
| PMSELR_EL0     | Performance Monitors Event Counter Selection Register       |

| Register       | Description, see                                   |
|----------------|----------------------------------------------------|
| PMSWINC_EL0    | Performance Monitors Software Increment Register   |
| PMUACR_EL1     | Performance Monitors User Access Control Register  |
| PMUSERENR_EL0  | Performance Monitors User Enable Register          |
| PMXEVCNTR_EL0  | Performance Monitors Selected Event Count Register |
| PMXEVTYPER_EL0 | Performance Monitors Selected Event Type Register  |
| PMZR_EL0       | Performance Monitors Zero with Mask                |

## K14.3.5 Activity monitors registers

This section is an index to the registers in the Activity Monitors registers functional group.

## Table K14-14 Activity monitors registers

| Register        | Description, see                                          |
|-----------------|-----------------------------------------------------------|
| AMCFGR_EL0      | Activity Monitors Configuration Register                  |
| AMCG1IDR_EL0    | Activity Monitors Counter Group 1 Identification Register |
| AMCGCR_EL0      | Activity Monitors Counter Group Configuration Register    |
| AMCNTENCLR0_EL0 | Activity Monitors Count Enable Clear Register 0           |
| AMCNTENCLR1_EL0 | Activity Monitors Count Enable Clear Register 1           |
| AMCNTENSET0_EL0 | Activity Monitors Count Enable Set Register 0             |
| AMCNTENSET1_EL0 | Activity Monitors Count Enable Set Register 1             |
| AMCR_EL0        | Activity Monitors Control Register                        |
| AMUSERENR_EL0   | Activity Monitors User Enable Register                    |

## K14.3.6 Debug registers

This section is an index to the registers in the Debug registers functional group.

## Table K14-15 Debug registers

| Register          | Description, see                          |
|-------------------|-------------------------------------------|
| DBGAUTHSTATUS_EL1 | Debug Authentication Status Register      |
| DBGCLAIMCLR_EL1   | Debug CLAIM Tag Clear Register            |
| DBGCLAIMSET_EL1   | Debug CLAIM Tag Set Register              |
| DBGDTR_EL0        | Debug Data Transfer Register, half-duplex |
| DBGDTRRX_EL0      | Debug Data Transfer Register, Receive     |
| DBGDTRTX_EL0      | Debug Data Transfer Register, Transmit    |

## K14.3.7 Trace registers

This section is an index to the registers in the Trace unit registers functional group.

| Register     | Description, see                           |
|--------------|--------------------------------------------|
| DBGPRCR_EL1  | Debug Power Control Register               |
| DBGVCR32_EL2 | Debug Vector Catch Register                |
| MDCCINT_EL1  | Monitor DCCInterrupt Enable Register       |
| MDCCSR_EL0   | Monitor DCCStatus Register                 |
| MDCR_EL2     | Monitor Debug Configuration Register (EL2) |
| MDRAR_EL1    | Monitor Debug ROMAddress Register          |
| MDSCR_EL1    | Monitor Debug System Control Register      |
| OSDLR_EL1    | OS Double Lock Register                    |
| OSDTRRX_EL1  | OS Lock Data Transfer Register, Receive    |
| OSDTRTX_EL1  | OS Lock Data Transfer Register, Transmit   |
| OSECCR_EL1   | OS Lock Exception Catch Control Register   |
| OSLAR_EL1    | OS Lock Access Register                    |
| OSLSR_EL1    | OS Lock Status Register                    |
| TRFCR_EL1    | Trace Filter Control Register (EL1)        |
| TRFCR_EL2    | Trace Filter Control Register (EL2)        |

Table K14-16 Trace registers

| Register      | Description, see                                       |
|---------------|--------------------------------------------------------|
| TRCAUTHSTATUS | Trace Authentication Status Register                   |
| TRCAUXCTLR    | Trace Auxiliary Control Register                       |
| TRCBBCTLR     | Trace Branch Broadcast Control Register                |
| TRCCCCTLR     | Trace Cycle Count Control Register                     |
| TRCCIDCCTLR0  | Trace Context Identifier Comparator Control Register 0 |
| TRCCIDCCTLR1  | Trace Context Identifier Comparator Control Register 1 |
| TRCCLAIMCLR   | Trace Claim Tag Clear Register                         |
| TRCCLAIMSET   | Trace Claim Tag Set Register                           |
| TRCCONFIGR    | Trace Configuration Register                           |
| TRCDEVARCH    | Trace Device Architecture Register                     |
| TRCDEVID      | Trace Device Configuration Register                    |
| TRCEVENTCTL0R | Trace Event Control 0 Register                         |
| TRCEVENTCTL1R | Trace Event Control 1 Register                         |
| TRCIDR0       | Trace ID Register 0                                    |
| TRCIDR1       | Trace ID Register 1                                    |

| Register      | Description, see                                                |
|---------------|-----------------------------------------------------------------|
| TRCIDR10      | Trace ID Register 10                                            |
| TRCIDR11      | Trace ID Register 11                                            |
| TRCIDR12      | Trace ID Register 12                                            |
| TRCIDR13      | Trace ID Register 13                                            |
| TRCIDR2       | Trace ID Register 2                                             |
| TRCIDR3       | Trace ID Register 3                                             |
| TRCIDR4       | Trace ID Register 4                                             |
| TRCIDR5       | Trace ID Register 5                                             |
| TRCIDR6       | Trace ID Register 6                                             |
| TRCIDR7       | Trace ID Register 7                                             |
| TRCIDR8       | Trace ID Register 8                                             |
| TRCIDR9       | Trace ID Register 9                                             |
| TRCIMSPEC0    | Trace IMP DEF Register 0                                        |
| TRCITECR_EL1  | Instrumentation Trace Control Register (EL1)                    |
| TRCITECR_EL2  | Instrumentation Trace Control Register (EL2)                    |
| TRCITEEDCR    | Instrumentation Trace Extension External Debug Control Register |
| TRCOSLSR      | Trace OS Lock Status Register                                   |
| TRCPRGCTLR    | Trace Programming Control Register                              |
| TRCQCTLR      | Trace QElement Control Register                                 |
| TRCRSR        | Trace Resources Status Register                                 |
| TRCSEQRSTEVR  | Trace Sequencer Reset Control Register                          |
| TRCSEQSTR     | Trace Sequencer State Register                                  |
| TRCSTALLCTLR  | Trace Stall Control Register                                    |
| TRCSTATR      | Trace Status Register                                           |
| TRCSYNCPR     | Trace Synchronization Period Register                           |
| TRCTRACEIDR   | Trace ID Register                                               |
| TRCTSCTLR     | Trace Timestamp Control Register                                |
| TRCVICTLR     | Trace ViewInst Main Control Register                            |
| TRCVIIECTLR   | Trace ViewInst Include-Exclude Control Register                 |
| TRCVIPCSSCTLR | Trace ViewInst Start-Stop PE Comparator Control Register        |
| TRCVISSCTLR   | Trace ViewInst Start-Stop Control Register                      |
| TRCVMIDCCTLR0 | Trace Virtual Context Identifier Comparator Control Register    |
| TRCVMIDCCTLR1 | Trace Virtual Context Identifier Comparator Control Register    |

## K14.3.8 Branch Record Buffer registers

This section is an index to the registers in the Branch Record Buffer Extension registers functional group.

## Table K14-17 Branch Record Buffer registers

| Register      | Description, see                                       |
|---------------|--------------------------------------------------------|
| BRBCR_EL1     | Branch Record Buffer Control Register (EL1)            |
| BRBCR_EL2     | Branch Record Buffer Control Register (EL2)            |
| BRBFCR_EL1    | Branch Record Buffer Function Control Register         |
| BRBIDR0_EL1   | Branch Record Buffer ID0 Register                      |
| BRBINFINJ_EL1 | Branch Record Buffer Information Injection Register    |
| BRBSRCINJ_EL1 | Branch Record Buffer Source Address Injection Register |
| BRBTGTINJ_EL1 | Branch Record Buffer Target Address Injection Register |
| BRBTS_EL1     | Branch Record Buffer Timestamp Register                |

## K14.3.9 RAS registers

This section is an index to the registers in the RAS registers functional group.

## Table K14-18 RAS registers

| Register      | Description, see                                    |
|---------------|-----------------------------------------------------|
| DISR_EL1      | Deferred Interrupt Status Register                  |
| ERRIDR_EL1    | Error Record ID Register                            |
| ERRSELR_EL1   | Error Record Select Register                        |
| ERXADDR_EL1   | Selected Error Record Address Register              |
| ERXCTLR_EL1   | Selected Error Record Control Register              |
| ERXFR_EL1     | Selected Error Record Feature Register              |
| ERXGSR_EL1    | Selected Error Record Group Status Register         |
| ERXMISC0_EL1  | Selected Error Record Miscellaneous Register 0      |
| ERXMISC1_EL1  | Selected Error Record Miscellaneous Register 1      |
| ERXMISC2_EL1  | Selected Error Record Miscellaneous Register 2      |
| ERXMISC3_EL1  | Selected Error Record Miscellaneous Register 3      |
| ERXPFGCDN_EL1 | Selected Pseudo-fault Generation Countdown Register |
| ERXPFGCTL_EL1 | Selected Pseudo-fault Generation Control Register   |
| ERXPFGF_EL1   | Selected Pseudo-fault Generation Feature Register   |
| ERXSTATUS_EL1 | Selected Error Record Primary Status Register       |
| MFAR_EL3      | Physical Fault Address Register (EL3)               |
| VDISR_EL2     | Virtual Deferred Interrupt Status Register (EL2)    |
| VDISR_EL3     | Virtual Deferred Interrupt Status Register (EL3)    |
| VSESR_EL2     | Virtual SError Exception Syndrome Register (EL2)    |

| Register   | Description, see                                 |
|------------|--------------------------------------------------|
| VSESR_EL3  | Virtual SError Exception Syndrome Register (EL3) |

## K14.3.10 Root Security state registers

This section is an index to the registers in the Root Security state registers functional group.

## Table K14-19 Root Security state registers

| Register   | Description, see                                      |
|------------|-------------------------------------------------------|
| APAS       | Associate PA space                                    |
| GPCBW_EL3  | Granule Protection Check Bypass Window Register (EL3) |
| GPCCR_EL3  | Granule Protection Check Control Register (EL3)       |
| GPTBR_EL3  | Granule Protection Table Base Register                |

## K14.3.11 Memory Partitioning and Monitoring registers

This section is an index to the registers in the Memory Partitioning and Monitoring registers functional group.

## Table K14-20 Memory Partitioning and Monitoring registers

| Register      | Description, see                                            |
|---------------|-------------------------------------------------------------|
| MPAM0_EL1     | MPAM0Register (EL1)                                         |
| MPAM1_EL1     | MPAM1Register (EL1)                                         |
| MPAM2_EL2     | MPAM2Register (EL2)                                         |
| MPAM3_EL3     | MPAM3Register (EL3)                                         |
| MPAMBW0_EL1   | MPAMPE-side Maximum-bandwidth Control Register (EL0)        |
| MPAMBW1_EL1   | MPAMPE-side Maximum-bandwidth Control Register (EL1)        |
| MPAMBW2_EL2   | MPAMPE-side Maximum-bandwidth Control Register (EL2)        |
| MPAMBW3_EL3   | MPAMPE-side Maximum-bandwidth Control Register (EL3)        |
| MPAMBWCAP_EL2 | MPAMPE-side Maximum-bandwidth Limit Virtualization Register |
| MPAMBWIDR_EL1 | MPAMPE-side Bandwidth Controls ID Register                  |
| MPAMBWSM_EL1  | MPAMStreaming Mode Bandwidth Control Register (EL1)         |
| MPAMHCR_EL2   | MPAMHypervisor Control Register (EL2)                       |
| MPAMSM_EL1    | MPAMStreaming Mode Register                                 |
| MPAMVPM0_EL2  | MPAMVirtual PARTID Mapping Register 0                       |
| MPAMVPM1_EL2  | MPAMVirtual PARTID Mapping Register 1                       |
| MPAMVPM2_EL2  | MPAMVirtual PARTID Mapping Register 2                       |

| Register     | Description, see                             |
|--------------|----------------------------------------------|
| MPAMVPM3_EL2 | MPAMVirtual PARTID Mapping Register 3        |
| MPAMVPM4_EL2 | MPAMVirtual PARTID Mapping Register 4        |
| MPAMVPM5_EL2 | MPAMVirtual PARTID Mapping Register 5        |
| MPAMVPM6_EL2 | MPAMVirtual PARTID Mapping Register 6        |
| MPAMVPM7_EL2 | MPAMVirtual PARTID Mapping Register 7        |
| MPAMVPMV_EL2 | MPAMVirtual Partition Mapping Valid Register |

## K14.3.12 Generic timer registers

This section is an index to the registers in the Generic Timer registers functional group.

## Table K14-21 Generic timer registers

| Register        | Description, see                                                |
|-----------------|-----------------------------------------------------------------|
| CNTFRQ_EL0      | Counter-timer Frequency Register                                |
| CNTHCTL_EL2     | Counter-timer Hypervisor Control Register                       |
| CNTHP_CTL_EL2   | Counter-timer Hypervisor Physical Timer Control Register        |
| CNTHP_CVAL_EL2  | Counter-timer Physical Timer CompareValue Register (EL2)        |
| CNTHP_TVAL_EL2  | Counter-timer Physical Timer TimerValue Register (EL2)          |
| CNTHPS_CTL_EL2  | Counter-timer Secure Physical Timer Control Register (EL2)      |
| CNTHPS_CVAL_EL2 | Counter-timer Secure Physical Timer CompareValue Register (EL2) |
| CNTHPS_TVAL_EL2 | Counter-timer Secure Physical Timer TimerValue Register (EL2)   |
| CNTHV_CTL_EL2   | Counter-timer Virtual Timer Control Register (EL2)              |
| CNTHV_CVAL_EL2  | Counter-timer Virtual Timer CompareValue Register (EL2)         |
| CNTHV_TVAL_EL2  | Counter-timer Virtual Timer TimerValue Register (EL2)           |
| CNTHVS_CTL_EL2  | Counter-timer Secure Virtual Timer Control Register (EL2)       |
| CNTHVS_CVAL_EL2 | Counter-timer Secure Virtual Timer CompareValue Register (EL2)  |
| CNTHVS_TVAL_EL2 | Counter-timer Secure Virtual Timer TimerValue Register (EL2)    |
| CNTKCTL_EL1     | Counter-timer Kernel Control Register                           |
| CNTP_CTL_EL0    | Counter-timer Physical Timer Control Register                   |
| CNTP_CVAL_EL0   | Counter-timer Physical Timer CompareValue Register              |
| CNTP_TVAL_EL0   | Counter-timer Physical Timer TimerValue Register                |
| CNTPCT_EL0      | Counter-timer Physical Count Register                           |
| CNTPCTSS_EL0    | Counter-timer Self-Synchronized Physical Count Register         |
| CNTPOFF_EL2     | Counter-timer Physical Offset Register                          |
| CNTPS_CTL_EL1   | Counter-timer Physical Secure Timer Control Register            |
| CNTPS_CVAL_EL1  | Counter-timer Physical Secure Timer CompareValue Register       |
| CNTPS_TVAL_EL1  | Counter-timer Physical Secure Timer TimerValue Register         |

| Register      | Description, see                                       |
|---------------|--------------------------------------------------------|
| CNTV_CTL_EL0  | Counter-timer Virtual Timer Control Register           |
| CNTV_CVAL_EL0 | Counter-timer Virtual Timer CompareValue Register      |
| CNTV_TVAL_EL0 | Counter-timer Virtual Timer TimerValue Register        |
| CNTVCT_EL0    | Counter-timer Virtual Count Register                   |
| CNTVCTSS_EL0  | Counter-timer Self-Synchronized Virtual Count Register |
| CNTVOFF_EL2   | Counter-timer Virtual Offset Register                  |

## K14.3.13 Cache maintenance system instructions

This section is an index to the registers in the Cache maintenance instructions functional group.

## Table K14-22 Cache maintenance system instructions

| System instruction   | Description, see                                                            |
|----------------------|-----------------------------------------------------------------------------|
| DCCGDSW              | Clean of Data and Allocation Tags by Set-Way                                |
| DCCGDVAC             | Clean of Data and Allocation Tags by VA to PoC                              |
| DCCGDVADP            | Clean of Data and Allocation Tags by VA to PoDP                             |
| DCCGDVAOC            | Clean of Data and Allocation Tags by VA to Outer Cache level                |
| DCCGDVAP             | Clean of Data and Allocation Tags by VA to PoP                              |
| DCCGSW               | Clean of Allocation Tags by Set-Way                                         |
| DCCGVAC              | Clean of Allocation Tags by VA to PoC                                       |
| DCCGVADP             | Clean of Allocation Tags by VA to PoDP                                      |
| DCCGVAP              | Clean of Allocation Tags by VA to PoP                                       |
| DCCIGDPAE            | Clean and invalidate of data and allocation tags by PA to PoE               |
| DCCIGDPAPA           | Clean and Invalidate of Data and Allocation Tags by PA to PoPA              |
| DCCIGDSW             | Clean and Invalidate of Data and Allocation Tags by Set-Way                 |
| DCCIGDVAC            | Clean and Invalidate of Data and Allocation Tags by VA to PoC               |
| DCCIGDVAOC           | Clean and Invalidate of Data and Allocation Tags by VA to Outer Cache level |
| DCCIGDVAPS           | Clean and Invalidate of Data and Allocation Tags by VA to PoPS              |
| DCCIGSW              | Clean and Invalidate of Allocation Tags by Set-Way                          |
| DCCIGVAC             | Clean and Invalidate of Allocation Tags by VA to PoC                        |
| DCCIPAE              | Data or unified Cache line Clean and Invalidate by PA to PoE                |
| DCCIPAPA             | Data or unified Cache line Clean and Invalidate by PA to PoPA               |
| DCCISW               | Data or unified Cache line Clean and Invalidate by Set-Way                  |
| DCCIVAC              | Data or unified Cache line Clean and Invalidate by VA to PoC                |
| DCCIVAOC             | Data or unified Cache line Clean and Invalidate by VA to Outer Cache level  |
| DCCIVAPS             | Clean and Invalidate of Data by VA to PoPS                                  |
| DCCSW                | Data or unified Cache line Clean by Set-Way                                 |

| System instruction   | Description, see                                            |
|----------------------|-------------------------------------------------------------|
| DCCVAC               | Data or unified Cache line Clean by VA to PoC               |
| DCCVADP              | Data or unified Cache line Clean by VA to PoDP              |
| DCCVAOC              | Data or unified Cache line Clean by VA to Outer Cache level |
| DCCVAP               | Data or unified Cache line Clean by VA to PoP               |
| DCCVAU               | Data or unified Cache line Clean by VA to PoU               |
| DCGVA                | Data Cache set Allocation Tag by VA                         |
| DCGZVA               | Data Cache set Allocation Tags and Zero by VA               |
| DCIGDSW              | Invalidate of Data and Allocation Tags by Set-Way           |
| DCIGDVAC             | Invalidate of Data and Allocation Tags by VA to PoC         |
| DCIGSW               | Invalidate of Allocation Tags by Set-Way                    |
| DCIGVAC              | Invalidate of Allocation Tags by VA to PoC                  |
| DCISW                | Data or unified Cache line Invalidate by Set-Way            |
| DCIVAC               | Data or unified Cache line Invalidate by VA to PoC          |
| DCZVA                | Data Cache Zero by VA                                       |
| IC IALLU             | Instruction Cache Invalidate All to PoU                     |
| IC IALLUIS           | Instruction Cache Invalidate All to PoU, Inner Shareable    |
| IC IVAU              | Instruction Cache line Invalidate by VA to PoU              |

## K14.3.14 Address translation system instructions

This section is an index to the registers in the Address translation instructions functional group.

Table K14-23 Address translation system instructions

| System instruction   | Description, see                                        |
|----------------------|---------------------------------------------------------|
| AT S12E0R            | Address Translate Stages 1 and 2 EL0 Read               |
| AT S12E0W            | Address Translate Stages 1 and 2 EL0 Write              |
| AT S12E1R            | Address Translate Stages 1 and 2 EL1 Read               |
| AT S12E1W            | Address Translate Stages 1 and 2 EL1 Write              |
| AT S1E0R             | Address Translate Stage 1 EL0 Read                      |
| AT S1E0W             | Address Translate Stage 1 EL0 Write                     |
| AT S1E1A             | Address Translate Stage 1 EL1 Without Permission checks |
| AT S1E1R             | Address Translate Stage 1 EL1 Read                      |
| AT S1E1RP            | Address Translate Stage 1 EL1 Read PAN                  |
| AT S1E1W             | Address Translate Stage 1 EL1 Write                     |
| AT S1E1WP            | Address Translate Stage 1 EL1 Write PAN                 |
| AT S1E2A             | Address Translate Stage 1 EL2 Without Permission checks |
| AT S1E2R             | Address Translate Stage 1 EL2 Read                      |
| AT S1E2W             | Address Translate Stage 1 EL2 Write                     |

| System instruction   | Description, see                                        |
|----------------------|---------------------------------------------------------|
| AT S1E3A             | Address Translate Stage 1 EL3 Without Permission checks |
| AT S1E3R             | Address Translate Stage 1 EL3 Read                      |
| AT S1E3W             | Address Translate Stage 1 EL3 Write                     |

## K14.3.15 TLB maintenance system instructions

This section is an index to the registers in the TLB maintenance instructions functional group.

Table K14-24 TLB maintenance system instructions

| System instruction                  | Description, see                                                                           |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| TLBI ALLE1, TLBI ALLE1NXS           | TLB Invalidate All, EL1                                                                    |
| TLBI ALLE1IS, TLBI ALLE1ISNXS       | TLB Invalidate All, EL1, Inner Shareable                                                   |
| TLBI ALLE1OS, TLBI ALLE1OSNXS       | TLB Invalidate All, EL1, Outer Shareable                                                   |
| TLBI ALLE2, TLBI ALLE2NXS           | TLB Invalidate All, EL2                                                                    |
| TLBI ALLE2IS, TLBI ALLE2ISNXS       | TLB Invalidate All, EL2, Inner Shareable                                                   |
| TLBI ALLE2OS, TLBI ALLE2OSNXS       | TLB Invalidate All, EL2, Outer Shareable                                                   |
| TLBI ALLE3, TLBI ALLE3NXS           | TLB Invalidate All, EL3                                                                    |
| TLBI ALLE3IS, TLBI ALLE3ISNXS       | TLB Invalidate All, EL3, Inner Shareable                                                   |
| TLBI ALLE3OS, TLBI ALLE3OSNXS       | TLB Invalidate All, EL3, Outer Shareable                                                   |
| TLBI ASIDE1, TLBI ASIDE1NXS         | TLB Invalidate by ASID, EL1                                                                |
| TLBI ASIDE1IS, TLBI ASIDE1ISNXS     | TLB Invalidate by ASID, EL1, Inner Shareable                                               |
| TLBI ASIDE1OS, TLBI ASIDE1OSNXS     | TLB Invalidate by ASID, EL1, Outer Shareable                                               |
| TLBI IPAS2E1, TLBI IPAS2E1NXS       | TLB Invalidate by Intermediate Physical Address, Stage 2, EL1                              |
| TLBI IPAS2E1IS, TLBI IPAS2E1ISNXS   | TLB Invalidate by Intermediate Physical Address, Stage 2, EL1, Inner Shareable             |
| TLBI IPAS2E1OS, TLBI IPAS2E1OSNXS   | TLB Invalidate by Intermediate Physical Address, Stage 2, EL1, Outer Shareable             |
| TLBI IPAS2LE1, TLBI IPAS2LE1NXS     | TLB Invalidate by Intermediate Physical Address, Stage 2, Last level, EL1                  |
| TLBI IPAS2LE1IS, TLBI IPAS2LE1ISNXS | TLB Invalidate by Intermediate Physical Address, Stage 2, Last level, EL1, Inner Shareable |
| TLBI IPAS2LE1OS, TLBI IPAS2LE1OSNXS | TLB Invalidate by Intermediate Physical Address, Stage 2, Last level, EL1, Outer Shareable |
| TLBI PAALL                          | TLB Invalidate GPT Information by PA, All Entries, Local                                   |
| TLBI PAALLOS                        | TLB Invalidate GPT Information by PA, All Entries, Outer Shareable                         |
| TLBI RIPAS2E1, TLBI RIPAS2E1NXS     | TLB Range Invalidate by Intermediate Physical Address, Stage 2, EL1                        |

| System instruction                    | Description, see                                                                                 |
|---------------------------------------|--------------------------------------------------------------------------------------------------|
| TLBI RIPAS2E1IS, TLBI RIPAS2E1ISNXS   | TLB Range Invalidate by Intermediate Physical Address, Stage 2, EL1, Inner Shareable             |
| TLBI RIPAS2E1OS, TLBI RIPAS2E1OSNXS   | TLB Range Invalidate by Intermediate Physical Address, Stage 2, EL1, Outer Shareable             |
| TLBI RIPAS2LE1, TLBI RIPAS2LE1NXS     | TLB Range Invalidate by Intermediate Physical Address, Stage 2, Last level, EL1                  |
| TLBI RIPAS2LE1IS, TLBI RIPAS2LE1ISNXS | TLB Range Invalidate by Intermediate Physical Address, Stage 2, Last level, EL1, Inner Shareable |
| TLBI RIPAS2LE1OS, TLBI RIPAS2LE1OSNXS | TLB Range Invalidate by Intermediate Physical Address, Stage 2, Last level, EL1, Outer Shareable |
| TLBI RPALOS                           | TLB Range Invalidate GPT Information by PA, Last level, Outer Shareable                          |
| TLBI RPAOS                            | TLB Range Invalidate GPT Information by PA, Outer Shareable                                      |
| TLBI RVAAE1, TLBI RVAAE1NXS           | TLB Range Invalidate by VA, All ASID, EL1                                                        |
| TLBI RVAAE1IS, TLBI RVAAE1ISNXS       | TLB Range Invalidate by VA, All ASID, EL1, Inner Shareable                                       |
| TLBI RVAAE1OS, TLBI RVAAE1OSNXS       | TLB Range Invalidate by VA, All ASID, EL1, Outer Shareable                                       |
| TLBI RVAALE1, TLBI RVAALE1NXS         | TLB Range Invalidate by VA, All ASID, Last level, EL1                                            |
| TLBI RVAALE1IS, TLBI RVAALE1ISNXS     | TLB Range Invalidate by VA, All ASID, Last Level, EL1, Inner Shareable                           |
| TLBI RVAALE1OS, TLBI RVAALE1OSNXS     | TLB Range Invalidate by VA, All ASID, Last Level, EL1, Outer Shareable                           |
| TLBI RVAE1, TLBI RVAE1NXS             | TLB Range Invalidate by VA, EL1                                                                  |
| TLBI RVAE1IS, TLBI RVAE1ISNXS         | TLB Range Invalidate by VA, EL1, Inner Shareable                                                 |
| TLBI RVAE1OS, TLBI RVAE1OSNXS         | TLB Range Invalidate by VA, EL1, Outer Shareable                                                 |
| TLBI RVAE2, TLBI RVAE2NXS             | TLB Range Invalidate by VA, EL2                                                                  |
| TLBI RVAE2IS, TLBI RVAE2ISNXS         | TLB Range Invalidate by VA, EL2, Inner Shareable                                                 |
| TLBI RVAE2OS, TLBI RVAE2OSNXS         | TLB Range Invalidate by VA, EL2, Outer Shareable                                                 |
| TLBI RVAE3, TLBI RVAE3NXS             | TLB Range Invalidate by VA, EL3                                                                  |
| TLBI RVAE3IS, TLBI RVAE3ISNXS         | TLB Range Invalidate by VA, EL3, Inner Shareable                                                 |
| TLBI RVAE3OS, TLBI RVAE3OSNXS         | TLB Range Invalidate by VA, EL3, Outer Shareable                                                 |
| TLBI RVALE1, TLBI RVALE1NXS           | TLB Range Invalidate by VA, Last level, EL1                                                      |
| TLBI RVALE1IS, TLBI RVALE1ISNXS       | TLB Range Invalidate by VA, Last level, EL1, Inner Shareable                                     |
| TLBI RVALE1OS, TLBI RVALE1OSNXS       | TLB Range Invalidate by VA, Last level, EL1, Outer Shareable                                     |
| TLBI RVALE2, TLBI RVALE2NXS           | TLB Range Invalidate by VA, Last level, EL2                                                      |
| TLBI RVALE2IS, TLBI RVALE2ISNXS       | TLB Range Invalidate by VA, Last level, EL2, Inner Shareable                                     |
| TLBI RVALE2OS, TLBI RVALE2OSNXS       | TLB Range Invalidate by VA, Last level, EL2, Outer Shareable                                     |
| TLBI RVALE3, TLBI RVALE3NXS           | TLB Range Invalidate by VA, Last level, EL3                                                      |

| System instruction                      | Description, see                                                   |
|-----------------------------------------|--------------------------------------------------------------------|
| TLBI RVALE3IS, TLBI RVALE3ISNXS         | TLB Range Invalidate by VA, Last level, EL3, Inner Shareable       |
| TLBI RVALE3OS, TLBI RVALE3OSNXS         | TLB Range Invalidate by VA, Last level, EL3, Outer Shareable       |
| TLBI VAAE1, TLBI VAAE1NXS               | TLB Invalidate by VA, All ASID, EL1                                |
| TLBI VAAE1IS, TLBI VAAE1ISNXS           | TLB Invalidate by VA, All ASID, EL1, Inner Shareable               |
| TLBI VAAE1OS, TLBI VAAE1OSNXS           | TLB Invalidate by VA, All ASID, EL1, Outer Shareable               |
| TLBI VAALE1, TLBI VAALE1NXS             | TLB Invalidate by VA, All ASID, Last level, EL1                    |
| TLBI VAALE1IS, TLBI VAALE1ISNXS         | TLB Invalidate by VA, All ASID, Last Level, EL1, Inner Shareable   |
| TLBI VAALE1OS, TLBI VAALE1OSNXS         | TLB Invalidate by VA, All ASID, Last Level, EL1, Outer Shareable   |
| TLBI VAE1, TLBI VAE1NXS                 | TLB Invalidate by VA, EL1                                          |
| TLBI VAE1IS, TLBI VAE1ISNXS             | TLB Invalidate by VA, EL1, Inner Shareable                         |
| TLBI VAE1OS, TLBI VAE1OSNXS             | TLB Invalidate by VA, EL1, Outer Shareable                         |
| TLBI VAE2, TLBI VAE2NXS                 | TLB Invalidate by VA, EL2                                          |
| TLBI VAE2IS, TLBI VAE2ISNXS             | TLB Invalidate by VA, EL2, Inner Shareable                         |
| TLBI VAE2OS, TLBI VAE2OSNXS             | TLB Invalidate by VA, EL2, Outer Shareable                         |
| TLBI VAE3, TLBI VAE3NXS                 | TLB Invalidate by VA, EL3                                          |
| TLBI VAE3IS, TLBI VAE3ISNXS             | TLB Invalidate by VA, EL3, Inner Shareable                         |
| TLBI VAE3OS, TLBI VAE3OSNXS             | TLB Invalidate by VA, EL3, Outer Shareable                         |
| TLBI VALE1, TLBI VALE1NXS               | TLB Invalidate by VA, Last level, EL1                              |
| TLBI VALE1IS, TLBI VALE1ISNXS           | TLB Invalidate by VA, Last level, EL1, Inner Shareable             |
| TLBI VALE1OS, TLBI VALE1OSNXS           | TLB Invalidate by VA, Last level, EL1, Outer Shareable             |
| TLBI VALE2, TLBI VALE2NXS               | TLB Invalidate by VA, Last level, EL2                              |
| TLBI VALE2IS, TLBI VALE2ISNXS           | TLB Invalidate by VA, Last level, EL2, Inner Shareable             |
| TLBI VALE2OS, TLBI VALE2OSNXS           | TLB Invalidate by VA, Last level, EL2, Outer Shareable             |
| TLBI VALE3, TLBI VALE3NXS               | TLB Invalidate by VA, Last level, EL3                              |
| TLBI VALE3IS, TLBI VALE3ISNXS           | TLB Invalidate by VA, Last level, EL3, Inner Shareable             |
| TLBI VALE3OS, TLBI VALE3OSNXS           | TLB Invalidate by VA, Last level, EL3, Outer Shareable             |
| TLBI VMALLE1, TLBIVMALLE1NXS            | TLB Invalidate by VMID, All at stage 1, EL1                        |
| TLBI VMALLE1IS, TLBI VMALLE1ISNXS       | TLB Invalidate by VMID, All at stage 1, EL1, Inner Shareable       |
| TLBI VMALLE1OS, TLBI VMALLE1OSNXS       | TLB Invalidate by VMID, All at stage 1, EL1, Outer Shareable       |
| TLBI VMALLS12E1, TLBI VMALLS12E1NXS     | TLB Invalidate by VMID, All at Stage 1 and 2, EL1                  |
| TLBI VMALLS12E1IS, TLBI VMALLS12E1ISNXS | TLB Invalidate by VMID, All at Stage 1 and 2, EL1, Inner Shareable |
| TLBI VMALLS12E1OS, TLBI VMALLS12E1OSNXS | TLB Invalidate by VMID, All at Stage 1 and 2, EL1, Outer Shareable |
| TLBI VMALLWS2E1, TLBI VMALLWS2E1NXS     | TLB Invalidate stage 2 dirty state by VMID, EL1&0                  |
| TLBI VMALLWS2E1IS, TLBI VMALLWS2E1ISNXS | TLB Invalidate stage 2 dirty state by VMID, EL1&0, Inner Shareable |

| System instruction                      | Description, see                                                                                 |
|-----------------------------------------|--------------------------------------------------------------------------------------------------|
| TLBI VMALLWS2E1OS, TLBI VMALLWS2E1OSNXS | TLB Invalidate stage 2 write permission by VMID, EL1&0, Outer Shareable                          |
| TLBIP IPAS2E1, TLBIP IPAS2E1NXS         | TLB Invalidate Pair by Intermediate Physical Address, Stage 2, EL1                               |
| TLBIP IPAS2E1IS, TLBIP IPAS2E1ISNXS     | TLB Invalidate Pair by Intermediate Physical Address, Stage 2, EL1, Inner Shareable              |
| TLBIP IPAS2E1OS, TLBIP IPAS2E1OSNXS     | TLB Invalidate Pair by Intermediate Physical Address, Stage 2, EL1, Outer Shareable              |
| TLBIP IPAS2LE1, TLBIP IPAS2LE1NXS       | TLB Invalidate Pair by Intermediate Physical Address, Stage 2, Last level, EL1                   |
| TLBIP IPAS2LE1IS, TLBIP IPAS2LE1ISNXS   | TLB Invalidate Pair by Intermediate Physical Address, Stage 2, Last level, EL1, Inner Shareable  |
| TLBIP IPAS2LE1OS, TLBIP IPAS2LE1OSNXS   | TLB Invalidate Pair by Intermediate Physical Address, Stage 2, Last level, EL1, Outer Shareable  |
| TLBIP RIPAS2E1, TLBIP RIPAS2E1NXS       | TLB Range Invalidate by Intermediate Physical Address, Stage 2, EL1                              |
| TLBIP RIPAS2E1IS, TLBIP RIPAS2E1ISNXS   | TLB Range Invalidate by Intermediate Physical Address, Stage 2, EL1, Inner Shareable             |
| TLBIP RIPAS2E1OS, TLBIP RIPAS2E1OSNXS   | TLB Range Invalidate by Intermediate Physical Address, Stage 2, EL1, Outer Shareable             |
| TLBIP RIPAS2LE1, TLBIP RIPAS2LE1NXS     | TLB Range Invalidate by Intermediate Physical Address, Stage 2, Last level, EL1                  |
| TLBIP RIPAS2LE1IS, TLBIP RIPAS2LE1ISNXS | TLB Range Invalidate by Intermediate Physical Address, Stage 2, Last level, EL1, Inner Shareable |
| TLBIP RIPAS2LE1OS, TLBIP RIPAS2LE1OSNXS | TLB Range Invalidate by Intermediate Physical Address, Stage 2, Last level, EL1, Outer Shareable |
| TLBIP RVAAE1, TLBIP RVAAE1NXS           | TLB Range Invalidate by VA, All ASID, EL1                                                        |
| TLBIP RVAAE1IS, TLBIP RVAAE1ISNXS       | TLB Range Invalidate by VA, All ASID, EL1, Inner Shareable                                       |
| TLBIP RVAAE1OS, TLBIP RVAAE1OSNXS       | TLB Range Invalidate by VA, All ASID, EL1, Outer Shareable                                       |
| TLBIP RVAALE1, TLBIP RVAALE1NXS         | TLB Range Invalidate by VA, All ASID, Last level, EL1                                            |
| TLBIP RVAALE1IS, TLBIP RVAALE1ISNXS     | TLB Range Invalidate by VA, All ASID, Last Level, EL1, Inner Shareable                           |
| TLBIP RVAALE1OS, TLBIP RVAALE1OSNXS     | TLB Range Invalidate by VA, All ASID, Last Level, EL1, Outer Shareable                           |
| TLBIP RVAE1, TLBIP RVAE1NXS             | TLB Range Invalidate by VA, EL1                                                                  |
| TLBIP RVAE1IS, TLBIP RVAE1ISNXS         | TLB Range Invalidate by VA, EL1, Inner Shareable                                                 |
| TLBIP RVAE1OS, TLBIP RVAE1OSNXS         | TLB Range Invalidate by VA, EL1, Outer Shareable                                                 |
| TLBIP RVAE2, TLBIP RVAE2NXS             | TLB Range Invalidate by VA, EL2                                                                  |
| TLBIP RVAE2IS, TLBIP RVAE2ISNXS         | TLB Range Invalidate by VA, EL2, Inner Shareable                                                 |
| TLBIP RVAE2OS, TLBIP RVAE2OSNXS         | TLB Range Invalidate by VA, EL2, Outer Shareable                                                 |
| TLBIP RVAE3, TLBIP RVAE3NXS             | TLB Range Invalidate by VA, EL3                                                                  |
| TLBIP RVAE3IS, TLBIP RVAE3ISNXS         | TLB Range Invalidate by VA, EL3, Inner Shareable                                                 |
| TLBIP RVAE3OS, TLBIP RVAE3OSNXS         | TLB Range Invalidate by VA, EL3, Outer Shareable                                                 |
| TLBIP RVALE1, TLBIP RVALE1NXS           | TLB Range Invalidate by VA, Last level, EL1                                                      |

| System instruction                | Description, see                                                      |
|-----------------------------------|-----------------------------------------------------------------------|
| TLBIP RVALE1IS, TLBIP RVALE1ISNXS | TLB Range Invalidate by VA, Last level, EL1, Inner Shareable          |
| TLBIP RVALE1OS, TLBIP RVALE1OSNXS | TLB Range Invalidate by VA, Last level, EL1, Outer Shareable          |
| TLBIP RVALE2, TLBIP RVALE2NXS     | TLB Range Invalidate by VA, Last level, EL2                           |
| TLBIP RVALE2IS, TLBIP RVALE2ISNXS | TLB Range Invalidate by VA, Last level, EL2, Inner Shareable          |
| TLBIP RVALE2OS, TLBIP RVALE2OSNXS | TLB Range Invalidate by VA, Last level, EL2, Outer Shareable          |
| TLBIP RVALE3, TLBIP RVALE3NXS     | TLB Range Invalidate by VA, Last level, EL3                           |
| TLBIP RVALE3IS, TLBIP RVALE3ISNXS | TLB Range Invalidate by VA, Last level, EL3, Inner Shareable          |
| TLBIP RVALE3OS, TLBIP RVALE3OSNXS | TLB Range Invalidate by VA, Last level, EL3, Outer Shareable          |
| TLBIP VAAE1, TLBIP VAAE1NXS       | TLB Invalidate Pair by VA, All ASID, EL1                              |
| TLBIP VAAE1IS, TLBIP VAAE1ISNXS   | TLB Invalidate Pair by VA, All ASID, EL1, Inner Shareable             |
| TLBIP VAAE1OS, TLBIP VAAE1OSNXS   | TLB Invalidate Pair by VA, All ASID, EL1, Outer Shareable             |
| TLBIP VAALE1, TLBIP VAALE1NXS     | TLB Invalidate Pair by VA, All ASID, Last level, EL1                  |
| TLBIP VAALE1IS, TLBIP VAALE1ISNXS | TLB Invalidate Pair by VA, All ASID, Last Level, EL1, Inner Shareable |
| TLBIP VAALE1OS, TLBIP VAALE1OSNXS | TLB Invalidate Pair by VA, All ASID, Last Level, EL1, Outer Shareable |
| TLBIP VAE1, TLBIP VAE1NXS         | TLB Invalidate Pair by VA, EL1                                        |
| TLBIP VAE1IS, TLBIP VAE1ISNXS     | TLB Invalidate Pair by VA, EL1, Inner Shareable                       |
| TLBIP VAE1OS, TLBIP VAE1OSNXS     | TLB Invalidate Pair by VA, EL1, Outer Shareable                       |
| TLBIP VAE2, TLBIP VAE2NXS         | TLB Invalidate Pair by VA, EL2                                        |
| TLBIP VAE2IS, TLBIP VAE2ISNXS     | TLB Invalidate Pair by VA, EL2, Inner Shareable                       |
| TLBIP VAE2OS, TLBIP VAE2OSNXS     | TLB Invalidate Pair by VA, EL2, Outer Shareable                       |
| TLBIP VAE3, TLBIP VAE3NXS         | TLB Invalidate Pair by VA, EL3                                        |
| TLBIP VAE3IS, TLBIP VAE3ISNXS     | TLB Invalidate Pair by VA, EL3, Inner Shareable                       |
| TLBIP VAE3OS, TLBIP VAE3OSNXS     | TLB Invalidate Pair by VA, EL3, Outer Shareable                       |
| TLBIP VALE1, TLBIP VALE1NXS       | TLB Invalidate Pair by VA, Last level, EL1                            |
| TLBIP VALE1IS, TLBIP VALE1ISNXS   | TLB Invalidate Pair by VA, Last level, EL1, Inner Shareable           |
| TLBIP VALE1OS, TLBIP VALE1OSNXS   | TLB Invalidate Pair by VA, Last level, EL1, Outer Shareable           |
| TLBIP VALE2, TLBIP VALE2NXS       | TLB Invalidate Pair by VA, Last level, EL2                            |
| TLBIP VALE2IS, TLBIP VALE2ISNXS   | TLB Invalidate Pair by VA, Last level, EL2, Inner Shareable           |
| TLBIP VALE2OS, TLBIP VALE2OSNXS   | TLB Invalidate Pair by VA, Last level, EL2, Outer Shareable           |
| TLBIP VALE3, TLBIP VALE3NXS       | TLB Invalidate Pair by VA, Last level, EL3                            |

| System instruction              | Description, see                                            |
|---------------------------------|-------------------------------------------------------------|
| TLBIP VALE3IS, TLBIP VALE3ISNXS | TLB Invalidate Pair by VA, Last level, EL3, Inner Shareable |
| TLBIP VALE3OS, TLBIP VALE3OSNXS | TLB Invalidate Pair by VA, Last level, EL3, Outer Shareable |

## K14.3.16 Prediction restriction System instructions

This section is an index to the registers in the Prediction restriction instructions functional group.

## Table K14-25 Cache maintenance system instructions

| System instruction   | Description, see                                          |
|----------------------|-----------------------------------------------------------|
| CFPRCTX              | Control Flow Prediction Restriction by Context            |
| COSPRCTX             | Clear Other Speculative Prediction Restriction by Context |
| CPPRCTX              | Cache Prefetch Prediction Restriction by Context          |
| DVPRCTX              | Data Value Prediction Restriction by Context              |

## K14.3.17 Base system registers

This section is an index to the registers in the functional group.

## Table K14-26 Base system registers

| Register       | Description, see                                      |
|----------------|-------------------------------------------------------|
| ACTLRMASK_EL1  | Auxiliary Control Masking Register (EL1)              |
| ACTLRMASK_EL2  | Auxiliary Control Masking Register (EL2)              |
| CPACR_EL1      | Architectural Feature Access Control Register         |
| CPACRMASK_EL1  | Architectural Feature Access Control Masking Register |
| CPTRMASK_EL2   | Architectural Feature Trap Masking Register           |
| HFGITR2_EL2    | Hypervisor Fine-Grained Instruction Trap Register 2   |
| SCTLR2_EL1     | System Control Register (EL1)                         |
| SCTLR2_EL2     | System Control Register (EL2)                         |
| SCTLR2_EL3     | System Control Register (EL3)                         |
| SCTLR2MASK_EL1 | Extended System Control Masking Register (EL1)        |
| SCTLR2MASK_EL2 | Extended System Control Masking Register (EL2)        |
| SCTLR_EL1      | System Control Register (EL1)                         |
| SCTLR_EL2      | System Control Register (EL2)                         |

| Register      | Description, see                                    |
|---------------|-----------------------------------------------------|
| SCTLR_EL3     | System Control Register (EL3)                       |
| SCTLRMASK_EL1 | System Control Masking Register (EL1)               |
| SCTLRMASK_EL2 | System Control Masking Register (EL2)               |
| SMCR_EL1      | SMEControl Register (EL1)                           |
| SMCR_EL2      | SMEControl Register (EL2)                           |
| SMCR_EL3      | SMEControl Register (EL3)                           |
| SMPRI_EL1     | Streaming Mode Priority Register                    |
| SMPRIMAP_EL2  | Streaming Mode Priority Mapping Register            |
| TCR2MASK_EL1  | Extended Translation Control Masking Register (EL1) |
| TCR2MASK_EL2  | Extended Translation Control Masking Register (EL2) |
| TCRMASK_EL1   | Translation Control Masking Register (EL1)          |
| TCRMASK_EL2   | Translation Control Masking Register (EL2)          |
| ZCR_EL1       | SVE Control Register (EL1)                          |
| ZCR_EL2       | SVE Control Register (EL2)                          |
| ZCR_EL3       | SVE Control Register (EL3)                          |