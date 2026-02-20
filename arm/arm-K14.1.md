## K14.1 Introduction and register disambiguation

In some sections of this manual, registers are referred to by a general name , where the description applies to more than one context. Generally, this is one of the following:

- The description applies to both AArch32 state and AArch64 state, and therefore the register names could apply to either AArch32 System registers or AArch64 System registers.
- The description applies to multiple Exception levels, and therefore at a particular Exception level the register names need to take the appropriate Exception level suffix, \_EL0, \_EL1, \_EL2, or \_EL3.

The following sections disambiguate the general register names:

- Register name disambiguation by Execution state.
- Register name disambiguation by Exception level.

## K14.1.1 Register name disambiguation by Execution state

Table K14-1 disambiguates the general names of the registers by Execution state.

Table K14-1 Disambiguation of general names of registers by Execution state

| General name   | Short description                             | AArch64 register                  | AArch32 register                      |
|----------------|-----------------------------------------------|-----------------------------------|---------------------------------------|
| CONTEXTIDR     | Context ID                                    | CONTEXTIDR_EL1                    | CONTEXTIDR                            |
| DBGAUTHSTATUS  | Debug Authentication Status                   | DBGAUTHSTATUS_EL1                 | DBGAUTHSTATUS                         |
| DBGBCR         | Debug Breakpoint Control Registers            | DBGBCR<n>_EL1                     | DBGBCR<n>                             |
| DBGBVR         | Debug Breakpoint Value Registers              | DBGBVR<n>_EL1                     | DBGBVR<n> DBGBXVR<n>                  |
| DBGCLAIMCLR    | Debug CLAIM Tag Clear register                | DBGCLAIMCLR_EL1                   | DBGCLAIMCLR                           |
| DBGCLAIMSET    | Debug CLAIM Tag Set register                  | DBGCLAIMSET_EL1                   | DBGCLAIMSET                           |
| DBGDTRRX       | Debug Data Transfer Register, Receive         | DBGDTRRX_EL0                      | DBGDTRRXint                           |
| DBGDTRTX       | Debug Data Transfer Register, Transmit        | DBGDTRTX_EL0                      | DBGDTRTXint                           |
| DBGPRCR        | Debug Power Control Register                  | DBGPRCR_EL1                       | DBGPRCR                               |
| DBGVCR         | Debug Vector Catch Register                   | DBGVCR32_EL2                      | DBGVCR                                |
| DBGWCR         | Debug Watchpoint Control Registers            | DBGWCR<n>_EL1                     | DBGWCR<n>                             |
| DBGWVR         | Debug Watchpoint Value Registers              | DBGWVR<n>_EL1                     | DBGWVR<n>                             |
| DCCINT         | Debug Comms Channel Interrupt Enable Register | MDCCINT_EL1                       | DBGDCCINT                             |
| DCCSR          | Debug Comms Channel Status Register           | MDCCSR_EL0                        | DBGDSCRint                            |
| DLR            | Debug Link Register                           | DLR_EL0[31:0]                     | DLR                                   |
| DSCR           | Debug System Control Register                 | MDSCR_EL1                         | DBGDSCRext                            |
| DSPSR          | Debug Saved PE State Register                 | DSPSR_EL0                         | DSPSR, DSPSR2                         |
| FAR            | Fault Address Register                        | FAR_EL1 FAR_EL2 FAR_EL3 HPFAR_EL2 | DFAR, IFAR HDFAR, HIFAR FAR_EL3 HPFAR |
| HCR            | Hypervisor Configuration Register             | HCR_EL2                           | HCR HCR2                              |

Table K14-2 disambiguates the general names of the System registers that provide access to the Performance Monitors by Execution state.

| General name   | Short description                                    | AArch64 register                                  | AArch32 register                                                                 |
|----------------|------------------------------------------------------|---------------------------------------------------|----------------------------------------------------------------------------------|
| HDCR           | Hyp or EL2 Debug Control Register                    | MDCR_EL2                                          | HDCR                                                                             |
| HSCTLR         | Hypervisor System Control Register                   | SCTLR_EL2                                         | HSCTLR                                                                           |
| HTTBR          | EL2 Translation Table Base Register                  | TTBR0_EL2                                         | HTTBR                                                                            |
| ISR            | Interrupt Status Register                            | ISR_EL1                                           | ISR                                                                              |
| MPIDR          | Multiprocessor Affinity Register                     | MPIDR_EL1                                         | MPIDR                                                                            |
| OSDLR          | OS Double-Lock Register                              | OSDLR_EL1                                         | DBGOSDLR                                                                         |
| OSDTRRX        | OS Lock Data Transfer Register, Receive              | OSDTRRX_EL1                                       | DBGDTRRXext                                                                      |
| OSDTRTX        | OS Lock Data Transfer Register, Transmit             | OSDTRTX_EL1                                       | DBGDTRTXext                                                                      |
| OSECCR         | OS Lock Exception Catch Control Register             | OSECCR_EL1                                        | DBGOSECCR                                                                        |
| OSLAR          | OS Lock Access Register                              | OSLAR_EL1                                         | DBGOSLAR                                                                         |
| OSLSR          | OS Lock Status Register                              | OSLSR_EL1                                         | DBGOSLSR                                                                         |
| PMMIR          | Performance Monitors Machine Identification Register | PMMIR_EL1                                         | PMMIR                                                                            |
| SCR            | Secure Configuration Register                        | SCR_EL3                                           | SCR                                                                              |
| SCTLR          | System Control Register                              | SCTLR_EL1 SCTLR_EL2 SCTLR_EL3                     | SCTLR (NS) HSCTLR SCTLR (S)                                                      |
| SDCR           | Secure or EL3 Debug Configuration Register           | MDCR_EL3                                          | SDCR                                                                             |
| SDER           | Secure Debug Enable Register                         | SDER32_EL3                                        | SDER                                                                             |
| SPSR           | Saved Program Status Register                        | SPSR_EL1 SPSR_EL2 SPSR_EL3                        | SPSR (general description) SPSR_abt SPSR_fiq SPSR_hyp SPSR_irq SPSR_mon SPSR_svc |
| TCR            | Translation Control Register                         | TCR_EL1 TCR_EL2 TCR_EL3 VTCR_EL2                  | TTBCR(NS) HTCR TTBCR(S) VTCR                                                     |
| TTBR           | Translation Table Base Register                      | TTBR0_EL1 TTBR0_EL2 TTBR0_EL3 TTBR1_EL1 VTTBR_EL2 | TTBR0 TTBR1 HTTBR VTTBR                                                          |
| VBAR           | Vector Base Address Register                         | VBAR_EL1 VBAR_EL2 VBAR_EL3                        | VBAR HVBAR MVBAR                                                                 |
| VTCR           | PL1&0 stage 2 Translation Control Register           | VTCR_EL2                                          | VTCR                                                                             |
| VTTBR          | PL1&0 stage 2 Translation Table Base Register        | VTTBR_EL2                                         | VTTBR                                                                            |

Table K14-2 Disambiguation of general names of the Performance Monitors System registers by Execution state

| General name   | Short description                                           | AArch64 register   | AArch32 register   |
|----------------|-------------------------------------------------------------|--------------------|--------------------|
| PMCCFILTR      | Cycle Count Filter Register                                 | PMCCFILTR_EL0      | PMCCFILTR          |
| PMCCNTR        | Cycle Count Register                                        | PMCCNTR_EL0        | PMCCNTR            |
| PMCEID0        | Performance Monitors Common Event Identification Register 0 | PMCEID0_EL0        | PMCEID0            |
| PMCEID1        | Performance Monitors Common Event Identification Register 1 | PMCEID1_EL0        | PMCEID1            |
| PMCEID2        | Performance Monitors Common Event Identification Register 2 | PMCEID0_EL0        | PMCEID2            |
| PMCEID3        | Performance Monitors Common Event Identification Register 3 | PMCEID1_EL0        | PMCEID3            |
| PMCNTENCLR     | Performance Monitors Count Enable Clear register            | PMCNTENCLR_EL0     | PMCNTENCLR         |
| PMCNTENSET     | Performance Monitors Count Enable Set register              | PMCNTENSET_EL0     | PMCNTENSET         |
| PMCR           | Performance Monitors Control Register                       | PMCR_EL0           | PMCR               |
| PMEVCNTR<n>    | Performance Monitors Event Count Registers, n = 0-30        | PMEVCNTR<n>_EL0    | PMEVCNTR<n>        |
| PMEVTYPER<n>   | Performance Monitors Event Type Registers, n = 0-30         | PMEVTYPER<n>_EL0   | PMEVTYPER<n>       |
| PMINTENCLR     | Performance Monitors Interrupt Enable Clear register        | PMINTENCLR_EL1     | PMINTENCLR         |
| PMINTENSET     | Performance Monitors Interrupt Enable Set register          | PMINTENSET_EL1     | PMINTENSET         |
| PMMIR          | Performance Monitors Machine Identification Register        | PMMIR_EL1          | PMMIR              |
| PMOVSCLR       | Performance Monitors Overflow Flag Status Register          | PMOVSCLR_EL0       | PMOVSR             |
| PMOVSSET       | Performance Monitors Overflow Flag Status Set register      | PMOVSSET_EL0       | PMOVSSET           |
| PMSELR         | Performance Monitors Event Counter Selection Register       | PMSELR_EL0         | PMSELR             |
| PMSWINC        | Performance Monitors Software Increment register            | PMSWINC_EL0        | PMSWINC            |
| PMUSERENR      | Performance Monitors User Enable Register                   | PMUSERENR_EL0      | PMUSERENR          |
| PMXEVCNTR      | Performance Monitors Selected Event Count Register          | PMXEVCNTR_EL0      | PMXEVCNTR          |
| PMXEVTYPER     | Performance Monitors Selected Event Type Register           | PMXEVTYPER_EL0     | PMXEVTYPER         |

Table K14-3 disambiguates the general names of the System registers that provide access to the Activity Monitors by Execution state.

Table K14-3 Disambiguation of general names of the Activity Monitors System registers by Execution state

| General name   | Short description                                      | AArch64 register   | AArch32 register   |
|----------------|--------------------------------------------------------|--------------------|--------------------|
| AMCFGR         | Activity Monitors Configuration Register               | AMCFGR_EL0         | AMCFGR             |
| AMCGCR         | Activity Monitors Counter Group Configuration Register | AMCGCR_EL0         | AMCGCR             |
| AMCNTENCLR0    | Activity Monitors Count Enable Clear Register 0        | AMCNTENCLR0_EL0    | AMCNTENCLR0        |
| AMCNTENCLR1    | Activity Monitors Count Enable Clear Register 1        | AMCNTENCLR1_EL0    | AMCNTENCLR1        |
| AMCNTENSET0    | Activity Monitors Count Enable Set Register 0          | AMCNTENSET0_EL0    | AMCNTENSET0        |
| AMCNTENSET1    | Activity Monitors Count Enable Set Register 1          | AMCNTENSET1_EL0    | AMCNTENSET1        |

| General name   | Short description                                     | AArch64 register   | AArch32 register   |
|----------------|-------------------------------------------------------|--------------------|--------------------|
| AMCR           | Activity Monitors Control Register                    | AMCR_EL0           | AMCR               |
| AMEVCNTR0<n>   | Activity Monitors Event Counter Registers 0, n = 0-15 | AMEVCNTR0<n>_EL0   | AMEVCNTR0<n>       |
| AMEVCNTR1<n>   | Activity Monitors Event Counter Registers 1, n = 0-15 | AMEVCNTR1<n>_EL0   | AMEVCNTR1<n>       |
| AMEVTYPER0<n>  | Activity Monitors Event Type Registers 0, n = 0-15    | AMEVTYPER0<n>_EL0  | AMEVTYPER0<n>      |
| AMEVTYPER1<n>  | Activity Monitors Event Type Registers 1, n = 0-15    | AMEVTYPER1<n>_EL0  | AMEVTYPER1<n>      |
| AMUSERENR      | Activity Monitors User Enable Register                | AMUSERENR_EL0      | AMUSERENR          |

Table K14-4 disambiguates the general names of the System registers that provide access to the Generic Timer System by Execution state.

Table K14-4 Disambiguation of general names of the Generic Timer System registers by Execution state

| General name   | Short description                                             | AArch64 register   | AArch32 register   |
|----------------|---------------------------------------------------------------|--------------------|--------------------|
| CNTFRQ         | Counter-timer Frequency register                              | CNTFRQ_EL0         | CNTFRQ             |
| CNTHCTL        | Counter-timer Hypervisor Control register                     | CNTHCTL_EL2        | CNTHCTL            |
| CNTHP_CTL      | Counter-timer Hypervisor Physical Timer Control register      | CNTHP_CTL_EL2      | CNTHP_CTL          |
| CNTHP_CVAL     | Counter-timer Hypervisor Physical Timer CompareValue register | CNTHP_CVAL_EL2     | CNTHP_CVAL         |
| CNTHP_TVAL     | Counter-timer Hypervisor Physical Timer TimerValue register   | CNTHP_TVAL_EL2     | CNTHP_TVAL         |
| CNTKCTL        | Counter-timer Kernel Control register                         | CNTKCTL_EL1        | CNTKCTL            |
| CNTP_CTL       | Counter-timer Physical Timer Control register                 | CNTP_CTL_EL0       | CNTP_CTL           |
| CNTP_CVAL      | Counter-timer Physical Timer CompareValue register            | CNTP_CVAL_EL0      | CNTP_CVAL          |
| CNTP_TVAL      | Counter-timer Physical Timer TimerValue register              | CNTP_TVAL_EL0      | CNTP_TVAL          |
| CNTPCT         | Counter-timer Physical Count register                         | CNTPCT_EL0         | CNTPCT             |
| CNTPS_CTL      | Counter-timer Physical Secure Timer Control register          | CNTPS_CTL_EL1      | -                  |
| CNTPS_CVAL     | Counter-timer Physical Secure Timer CompareValue register     | CNTPS_CVAL_EL1     | -                  |
| CNTPS_TVAL     | Counter-timer Physical Secure Timer TimerValue register       | CNTPS_TVAL_EL1     | -                  |
| CNTV_CTL       | Counter-timer Virtual Timer Control register                  | CNTV_CTL_EL0       | CNTV_CTL           |
| CNTV_CVAL      | Counter-timer Virtual Timer CompareValue register             | CNTV_CVAL_EL0      | CNTV_CVAL          |
| CNTV_TVAL      | Counter-timer Virtual Timer TimerValue register               | CNTV_TVAL_EL0      | CNTV_TVAL          |
| CNTVCT         | Counter-timer Virtual Count register                          | CNTVCT_EL0         | CNTVCT             |
| CNTVOFF        | Counter-timer Virtual Offset register                         | CNTVOFF_EL2        | CNTVOFF            |

Table K14-5 shows the mappings between the writable AArch64 System registers and the AArch32 System registers.

Table K14-5 Mapping of writable AArch64 System registers to the AArch32 System registers

| AArch64 register     | AArch32 register        |
|----------------------|-------------------------|
| ACTLR_EL1[31:0]      | ACTLR a                 |
| ACTLR_EL1[63:32]     | ACTLR2 a if implemented |
| AFSR0_EL1[31:0]      | ADFSR a                 |
| AFSR1_EL1[31:0]      | AIFSR a                 |
| AMAIR_EL1[31:0]      | AMAIR0 a                |
| AMAIR_EL1[63:32]     | AMAIR1 a                |
| CONTEXTIDR_EL1[31:0] | CONTEXTIDR a            |
| CPACR_EL1[31:0]      | CPACR                   |
| CSSELR_EL1[31:0]     | CSSELR a                |
| DACR32_EL2[31:0]     | DACR a                  |
| FAR_EL1[31:0]        | DFAR a                  |
| ESR_EL1[31:0]        | DFSR a                  |
| HACR_EL2[31:0]       | HACR                    |
| ACTLR_EL1[31:0]      | HACTLR                  |
| ACTLR_EL2[63:32]     | HACTLR2 if implemented  |
| AFSR0_EL1[31:0]      | HADFSR                  |
| AFSR1_EL1[31:0]      | HAIFSR                  |
| AMAIR_EL2[31:0]      | HAMAIR0                 |
| AMAIR_EL2[63:32]     | HAMAIR1                 |
| CPTR_EL2[31:0]       | HCPTR                   |
| HCR_EL2[31:0]        | HCR                     |
| HCR_EL2[63:32]       | HCR2                    |
| MDCR_EL2[31:0]       | HDCR                    |
| FAR_EL2[31:0]        | HDFAR                   |
| FAR_EL2[63:32]       | HIFAR                   |
| MAIR_EL2[31:0]       | HMAIR0                  |
| MAIR_EL2[63:32]      | HAMAIR1                 |
| HPFAR_EL2[31:0]      | HPFAR                   |
| SCTLR_EL2[31:0]      | HSCTLR                  |
| ESR_EL2[31:0]        | HSR                     |
| HSTR_EL2[31:0]       | HSTR                    |
| TCR_EL3[31:0]        | HTCR                    |
| TPIDR_EL2[31:0]      | HTPIDR                  |
| TTBR0_EL2[47:1]      | HTTBR                   |
| VBAR_EL2[31:0]       | HVBAR                   |
| FAR_EL1[63:32]       | IFAR a                  |
| IFSR32_EL2[31:0]     | IFSR a                  |
| MAIR_EL1[63:32]      | NMRRorMAIR1 a           |

| AArch64 register     | AArch32 register        |
|----------------------|-------------------------|
| PAR_EL1[63:0]        | PAR a                   |
| MAIR_EL1[31:0]       | PRRR or MAIR0 a         |
| RMR_EL1[31:0]        | RMR(at EL1)             |
| RMR_EL2[31:0]        | HRMR                    |
| RMR_EL3[31:0]        | RMR(at EL3)             |
| SCTLR_EL1[31:0]      | SCTLR a                 |
| SDER32_EL3[31:0]     | SDER                    |
| TPIDR_EL1[31:0]      | TPIDRPRW a              |
| TPIDRRO_EL0[31:0]    | TPIDRURO a              |
| TPIDR_EL0[31:0]      | TPIDRURW a              |
| TCR_EL1[31:0]        | TTBCR a                 |
| TCR_EL1[63:32]       | TTBCR2 a if implemented |
| TTBR0_EL1[63:0]      | TTBR0 a                 |
| TTBR1_EL1[63:0]      | TTBR1 a                 |
| VBAR_EL1[31:0]       | VBAR a                  |
| VMPIDR_EL2[31:0]     | VMPIDR                  |
| VPIDR_EL2[31:0]      | VPIDR                   |
| VTCR_EL2[31:0]       | VTCR                    |
| VTTBR_EL2[63:0]      | VTTBR                   |
| Timer registers      |                         |
| CNTFRQ_EL0           | CNTFRQ                  |
| CNTHCTL_EL2          | CNTHCTL                 |
| CNTHP_CTL_EL2        | CNTP_CTL                |
| CNTHP_CVAL_EL2       | CNTHP_CVAL              |
| CNTHP_TVAL_EL2       | CNTHVS_TVAL             |
| CNTHPS_CTL_EL2       | CNTHPS_CTL              |
| CNTHPS_CVAL_EL2      | CNTHPS_CVAL             |
| CNTHPS_TVAL_EL2      | CNTHPS_TVAL             |
| CNTKCTL_EL1          | CNTKCTL                 |
| CNTP_CTL_EL0         | CNTP_CTL a              |
| CNTP_CVAL_EL0        | CNTP_CVAL a             |
| CNTP_TVAL_EL0        | CNTP_TVAL a             |
| CNTPCT_EL0[63:0]     | CNTPCT                  |
| CNTV_CTL_EL0[31:0]   | CNTV_CTL                |
| CNTV_CVAL_EL0[63:0]  | CNTV_CVAL               |
| CNTV_TVAL_EL0[31:0]  | CNTV_TVAL               |
| CNTHV_CTL_EL2[63:0]  | CNTHV_CTL               |
| CNTHV_CVAL_EL2[63:0] | CNTHV_CVAL              |
| CNTHV_TVAL_EL2[63:0] | CNTHV_TVAL              |
| CNTHVS_CTL_EL2[31:0] | CNTHVS_CTL              |

| AArch64 register                      | AArch32 register   |
|---------------------------------------|--------------------|
| CNTHVS_CVAL_EL2[63:0]                 | CNTHVS_CVAL        |
| CNTHVS_TVAL_EL2[63:0]                 | CNTHVS_TVAL        |
| CNTVCT_EL0[63:0]                      | CNTVCT             |
| CNTVOFF_EL2[63:0]                     | CNTVOFF            |
| Debug System registers                |                    |
| DBGAUTHSTATUS_EL1[31:0]               | DBGAUTHSTATUS      |
| DBGBCR<n>_EL1[31:0]                   | DBGBCR<n>          |
| DBGBVR<n>_EL1[31:0]                   | DBGBVR<n>          |
| DBGBVR<n>_EL1[63:32]                  | DBGBXVR<n>         |
| DBGCLAIMCLR_EL1[31:0]                 | DBGCLAIMCLR        |
| DBGCLAIMSET_EL1[31:0]                 | DBGCLAIMSET        |
| DBGDTR_EL0[63:32]                     | DBGDTRRXint        |
| DBGDTR_EL0[31:0]                      | DBGDTRTXint        |
| DBGDTRRX_EL0[31:0]                    | DBGDTRRXint        |
| DBGDTRTX_EL0[31:0]                    | DBGDTRTXint        |
| DBGPRCR_EL1[31:0]                     | DBGPRCR            |
| DBGVCR32_EL2[31:0]                    | DBGVCR             |
| DBGWCR<n>_EL1[31:0]                   | DBGWCR<n>          |
| DBGWVR<n>_EL1[31:0]                   | DBGWVR<n>          |
| ID_DFR0_EL1[31:0]                     | ID_DFR0            |
| MDCCSR_EL0 b [30:29]                  | DBGDSCRint b       |
| MDCR_EL2[31:0]                        | HDCR               |
| MDRAR_EL1[63:0]                       | DBGDRAR            |
| MDSCR_EL1 b [31:0]                    | DBGDSCRext b       |
| OSDLR_EL1[31:0]                       | DBGOSDLR           |
| OSDTRRX_EL1 b [31:0]                  | DBGDTRRXext b      |
| OSDTRTX_EL1 b [31:0]                  | DBGDTRTXext b      |
| OSECCR_EL1[31:0]                      | DBGOSECCR          |
| OSLAR_EL1[31:0]                       | DBGOSLAR           |
| OSLSR_EL1[31:0]                       | DBGOSLSR           |
| SDER32_EL3[31:0]                      | SDER               |
| Performance Monitors System registers |                    |
| PMCCNTR_EL0[31:0]                     | PMCCNTR(MRC/MCR)   |
| PMCEID0_EL0[31:0]                     | PMCEID0            |
| PMCEID0_EL0[63:32]                    | PMCEID2            |
| PMCEID1_EL0[31:0]                     | PMCEID1            |
| PMCEID1_EL0[63:32]                    | PMCEID3            |
| PMCNTENCLR_EL0[31:0]                  | PMCNTENCLR         |
| PMCNTENSET_EL0[31:0]                  | PMCNTENSET         |
| PMCR_EL0[31:0]                        | PMCR               |

| AArch64 register                   | AArch32 register   |
|------------------------------------|--------------------|
| PMEVCNTR<n>_EL0[31:0]              | PMEVCNTR<n>        |
| PMEVTYPER<n>_EL0[31:0]             | PMEVTYPER<n>       |
| PMINTENCLR_EL1[31:0]               | PMINTENCLR         |
| PMINTENSET_EL1[31:0]               | PMINTENSET         |
| PMSELR_EL0[31:0]                   | PMSELR             |
| PMSWINC_EL0[31:0]                  | PMSWINC            |
| PMUSERENR_EL0[31:0]                | PMUSERENR          |
| PMXEVCNTR_EL0[31:0]                | PMXEVCNTR          |
| PMXEVTYPER_EL0[31:0]               | PMXEVTYPER         |
| Activity Monitors System registers |                    |
| AMCNTENCLR0_EL0[31:0]              | AMCNTENCLR0        |
| AMCNTENCLR1_EL0[31:0]              | AMEVCNTR1<n>       |
| AMCNTENSET0_EL0[31:0]              | AMCNTENSET0        |
| AMCNTENSET1_EL0[31:0]              | AMCNTENSET1        |
| AMCR_EL0[31:0]                     | AMCR               |
| AMEVCNTR0<n>_EL0[63:0]             | AMEVCNTR0<n>       |
| AMEVCNTR1<n>_EL0[63:0]             | AMEVCNTR1<n>       |
| AMEVCNTR1<n>_EL0[31:0]             | AMEVTYPER1<n>      |
| RAS System registers               |                    |
| DISR_EL1[31:0]                     | DISR               |
| ERRIDR_EL1[31:0]                   | ERRIDR             |
| ERRSELR_EL1[31:0]                  | ERRSELR            |
| ERXADDR_EL1[31:0]                  | ERXADDR            |
| ERXADDR_EL1[63:32]                 | ERXADDR2           |
| ERXCTLR_EL1[31:0]                  | ERXCTLR            |
| ERXCTLR_EL1[63:32]                 | ERXCTLR2           |
| ERXFR_EL1[31:0]                    | ERXFR              |
| ERXFR_EL1[63:32]                   | ERXFR2             |
| ERXMISC0_EL1[31:0]                 | ERXMISC0           |
| ERXMISC0_EL1[63:32]                | ERXMISC1           |
| ERXMISC1_EL1[31:0]                 | ERXMISC2           |
| ERXMISC1_EL1[63:32]                | ERXMISC3           |
| ERXMISC2_EL1[31:0]                 | ERXMISC4           |
| ERXMISC2_EL1[63:32]                | ERXMISC5           |
| ERXMISC3_EL1[31:0]                 | ERXMISC6           |
| ERXMISC3_EL1[63:32]                | ERXMISC7           |
| ERXSTATUS_EL1[31:0]                | ERXSTATUS          |
| VDISR_EL2[31:0]                    | VDISR              |
| VSESR_EL2[31:0]                    | VDFSR              |

b. These registers have overlapping register content. One or more bits of one register appear in the other register.

There are a small number of AArch32 System registers that are not mapped to any AArch64 System registers. The AArch64 registers listed in Table K14-6 can be used to access these from a higher Exception level that is using AArch64. The registers shown in the table are UNDEFINED if EL1 cannot use AArch32.

Table K14-6 AArch64 registers for accessing registers that are only used in AArch32 state

| AArch32 register   | Register for access from AArch64 state   | Short description                         |
|--------------------|------------------------------------------|-------------------------------------------|
| DACR               | DACR32_EL2                               | Domain Access Control Register            |
| DBGVCR             | DBGVCR32_EL2                             | Debug Vector Catch Register               |
| FPEXC              | FPEXC32_EL2                              | Floating-Point Exception Control Register |
| IFSR               | IFSR32_EL2                               | Instruction Fault Status Register         |
| SDER               | SDER32_EL3                               | AArch32 Secure Debug Enable Register      |

Table K14-7 shows the AArch64 System registers that allow access from AArch64 state to the AArch32 ID registers. These AArch64 registers are UNKNOWN if no Exception level can use AArch32.

Table K14-7 AArch64 registers that access the AArch32 ID registers

| AArch32 register   | Register for access from AArch64 state   | Short description                                 |
|--------------------|------------------------------------------|---------------------------------------------------|
| ID_AFR0            | ID_AFR0_EL1                              | AArch32 Auxiliary Feature Register 0              |
| ID_DFR0            | ID_DFR0_EL1                              | AArch32 Debug Feature Register 0                  |
| ID_DFR1            | ID_DFR1_EL1                              | AArch32 Debug Feature Register 1                  |
| ID_ISAR0           | ID_ISAR0_EL1                             | EL1, AArch32 Instruction Set Attribute Register 0 |
| ID_ISAR1           | ID_ISAR1_EL1                             | EL1, AArch32 Instruction Set Attribute Register 1 |
| ID_ISAR2           | ID_ISAR2_EL1                             | EL1, AArch32 Instruction Set Attribute Register 2 |
| ID_ISAR3           | ID_ISAR3_EL1                             | EL1, AArch32 Instruction Set Attribute Register 3 |
| ID_ISAR4           | ID_ISAR4_EL1                             | EL1, AArch32 Instruction Set Attribute Register 4 |
| ID_ISAR5           | ID_ISAR5_EL1                             | EL1, AArch32 Instruction Set Attribute Register 5 |
| ID_ISAR6           | ID_ISAR6_EL1                             | EL1, AArch32 Instruction Set Attribute Register 6 |
| ID_MMFR0           | ID_MMFR0_EL1                             | AArch32 Memory Model Feature Register 0           |
| ID_MMFR1           | ID_MMFR1_EL1                             | AArch32 Memory Model Feature Register 1           |
| ID_MMFR2           | ID_MMFR2_EL1                             | AArch32 Memory Model Feature Register 2           |
| ID_MMFR3           | ID_MMFR3_EL1                             | AArch32 Memory Model Feature Register 3           |
| ID_MMFR4           | ID_MMFR4_EL1                             | AArch32 Memory Model Feature Register 4           |
| ID_MMFR5           | ID_MMFR5_EL1                             | AArch32 Memory Model Feature Register 5           |
| ID_PFR0            | ID_PFR0_EL1                              | AArch32 PE Feature Register 0                     |
| ID_PFR1            | ID_PFR1_EL1                              | AArch32 PE Feature Register 1                     |
| ID_PFR2            | ID_PFR2_EL1                              | AArch32 PE Feature Register 2                     |

## K14.1.2 Register name disambiguation by Exception level

Table K14-8 disambiguates the general names of the AArch64 System registers by Exception level.

## Table K14-8 Disambiguation of AArch64 System registers by Exception level

| General form   | EL0         | EL1                      | EL2                                                                                                            | EL3         |
|----------------|-------------|--------------------------|----------------------------------------------------------------------------------------------------------------|-------------|
| AFSR0_ELx      | -           | AFSR0_EL1                | AFSR0_EL2                                                                                                      | AFSR0_EL3   |
| AFSR1_ELx      | -           | AFSR1_EL1                | AFSR1_EL2                                                                                                      | AFSR1_EL3   |
| AMAIR2_ELx     | -           | AMAIR2_EL1               | AMAIR2_EL2                                                                                                     | AMAIR2_EL3  |
| AMAIR_ELx      | -           | AMAIR_EL1                | AMAIR_EL2                                                                                                      | AMAIR_EL3   |
| CONTEXTIDR_ELx | -           | CONTEXTIDR_EL1           | CONTEXTIDR_EL2                                                                                                 | -           |
| CPTR_ELx       | -           | -                        | CPTR_EL2                                                                                                       | CPTR_EL3    |
| ELR_ELx        | -           | ELR_EL1                  | ELR_EL2                                                                                                        | ELR_EL3     |
| ESR_ELx        | -           | ESR_EL1                  | ESR_EL2                                                                                                        | ESR_EL3     |
| FAR_ELx        | -           | FAR_EL1                  | FAR_EL2                                                                                                        | FAR_EL3     |
| GCSCR_ELx      | -           | GCSCR_EL1                | GCSCR_EL2                                                                                                      | GCSCR_EL3   |
| GCSPR_ELx      | GCSPR_EL0   | GCSPR_EL1                | GCSPR_EL2                                                                                                      | GCSPR_EL3   |
| MAIR2_ELx      | -           | MAIR2_EL1                | MAIR2_EL2                                                                                                      | MAIR2_EL3   |
| MAIR_ELx       | -           | MAIR_EL1                 | MAIR_EL2                                                                                                       | MAIR_EL3    |
| MPAMn_ELx      | -           | MPAM0_EL1, MPAM1_EL1     | MPAM2_EL2                                                                                                      | MPAM3_EL3   |
| MPAMVPMn_ELx   | -           | -                        | MPAMVPM0_EL2, MPAMVPM1_EL2, MPAMVPM2_EL2, MPAMVPM3_EL2, MPAMVPM4_EL2, MPAMVPM5_EL2, MPAMVPM6_EL2, MPAMVPM7_EL2 | -           |
| MPAMBWn_ELx    | -           | MPAMBW0_EL1, MPAMBW1_EL1 | MPAMBW2_EL2                                                                                                    | MPAMBW3_EL3 |
| PFAR_ELx       | -           | PFAR_EL1                 | PFAR_EL2                                                                                                       | -           |
| PIR_ELx        | -           | PIR_EL1                  | PIR_EL2                                                                                                        | PIR_EL3     |
| PIRE0_ELx      | -           | PIRE0_EL1                | PIRE0_EL2                                                                                                      | -           |
| PMBSR_ELx      | -           | PMBSR_EL1                | PMBSR_EL2                                                                                                      | PMBSR_EL3   |
| POR_ELx        | POR_EL0     | POR_EL1                  | POR_EL2                                                                                                        | POR_EL3     |
| RMR_ELx        | -           | RMR_EL1                  | RMR_EL2                                                                                                        | RMR_EL3     |
| RVBAR_ELx      | -           | RVBAR_EL1                | RVBAR_EL2                                                                                                      | RVBAR_EL3   |
| SCTLR2_ELx     | -           | SCTLR2_EL1               | SCTLR2_EL2                                                                                                     | SCTLR2_EL3  |
| SCTLR_ELx      | -           | SCTLR_EL1                | SCTLR_EL2                                                                                                      | SCTLR_EL3   |
| SCXTNUM_ELx    | SCXTNUM_EL0 | SCXTNUM_EL1              | SCXTNUM_EL2                                                                                                    | SCXTNUM_EL3 |
| SMCR_ELx       | -           | SMCR_EL1                 | SMCR_EL2                                                                                                       | SMCR_EL3    |
| SP_ELx         | SP_EL0      | SP_EL1                   | SP_EL2                                                                                                         | SP_EL3      |
| SPSR_ELx       | -           | SPSR_EL1                 | SPSR_EL2                                                                                                       | SPSR_EL3    |

| General form   | EL0        | EL1                  | EL2                                         | EL3       |
|----------------|------------|----------------------|---------------------------------------------|-----------|
| TCR2_ELx       | -          | TCR2_EL1             | TCR2_EL2                                    | -         |
| TCR_ELx        | -          | TCR_EL1              | TCR_EL2                                     | TCR_EL3   |
| TFSR_ELx       | TFSRE0_EL1 | TFSR_EL1             | TFSR_EL2                                    | TFSR_EL3  |
| TRBSR_ELx      | -          | TRBSR_EL1            | TRBSR_EL2                                   | TRBSR_EL3 |
| TRFCR_ELx      | -          | TRFCR_EL1            | TRFCR_EL2                                   | -         |
| TTBR_ELx       | -          | TTBR0_EL1, TTBR1_EL1 | TTBR0_EL2, TTBR1_EL2, VTTBR_EL2, VSTTBR_EL2 | TTBR0_EL3 |
| TTBRn_ELx      | -          | TTBR0_EL1, TTBR1_EL1 | TTBR0_EL2, TTBR1_EL2                        | TTBR0_EL3 |
| TTBR0_ELx      | -          | TTBR0_EL1            | TTBR0_EL2                                   | TTBR0_EL3 |
| TTBR1_ELx      | -          | TTBR1_EL1            | -                                           | -         |
| VBAR_ELx       | -          | VBAR_EL1             | VBAR_EL2                                    | VBAR_EL3  |
| ZCR_ELx        | -          | ZCR_EL1              | ZCR_EL2                                     | ZCR_EL3   |