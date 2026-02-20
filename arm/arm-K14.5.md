## K14.5 Functional index of AArch32 registers and System instructions

This section is an index of the AArch32 registers and System instructions, divided by functional group. Each of the following sections lists the registers for a functional group:

- Special-purpose registers.
- VMSA-specific registers.
- ID registers.
- Performance monitors registers.
- Activity Monitors registers.
- Debug registers.
- RAS registers.
- Generic timer registers.
- Cache maintenance system instructions.
- Address translation system instructions.
- TLB maintenance system instructions.
- Legacy feature registers and system instructions.
- Base system registers.

## K14.5.1 Special-purpose registers

This section is an index to the registers in the Processor state registers functional group.

## Table K14-28 Special-purpose registers

| Register   | Description, see                                |
|------------|-------------------------------------------------|
| DLR        | Debug Link Register                             |
| DSPSR      | Debug Saved Program Status Register             |
| ELR_hyp    | Exception Link Register (Hyp mode)              |
| SPSR       | Saved Program Status Register                   |
| SPSR_abt   | Saved Program Status Register (Abort mode)      |
| SPSR_fiq   | Saved Program Status Register (FIQ mode)        |
| SPSR_hyp   | Saved Program Status Register (Hyp mode)        |
| SPSR_irq   | Saved Program Status Register (IRQ mode)        |
| SPSR_mon   | Saved Program Status Register (Monitor mode)    |
| SPSR_svc   | Saved Program Status Register (Supervisor mode) |
| SPSR_und   | Saved Program Status Register (Undefined mode)  |

## K14.5.2 VMSA-specific registers

This section is an index to the registers in the Virtual memory control registers functional group.

## K14.5.3 ID registers

This section is an index to the registers in the Identification registers functional group.

## Table K14-29 VMSA-specific registers

| Register   | Description, see                                      |
|------------|-------------------------------------------------------|
| AMAIR0     | Auxiliary Memory Attribute Indirection Register 0     |
| AMAIR1     | Auxiliary Memory Attribute Indirection Register 1     |
| CONTEXTIDR | Context ID Register                                   |
| DACR       | Domain Access Control Register                        |
| HAMAIR0    | Hyp Auxiliary Memory Attribute Indirection Register 0 |
| HAMAIR1    | Hyp Auxiliary Memory Attribute Indirection Register 1 |
| HMAIR0     | Hyp Memory Attribute Indirection Register 0           |
| HMAIR1     | Hyp Memory Attribute Indirection Register 1           |
| HTCR       | Hyp Translation Control Register                      |
| HTTBR      | Hyp Translation Table Base Register                   |
| MAIR0      | Memory Attribute Indirection Register 0               |
| MAIR1      | Memory Attribute Indirection Register 1               |
| NMRR       | Normal Memory Remap Register                          |
| PRRR       | Primary Region Remap Register                         |
| TTBCR      | Translation Table Base Control Register               |
| TTBCR2     | Translation Table Base Control Register 2             |
| TTBR0      | Translation Table Base Register 0                     |
| TTBR1      | Translation Table Base Register 1                     |
| VTCR       | Virtualization Translation Control Register           |
| VTTBR      | Virtualization Translation Table Base Register        |

## Table K14-30 ID registers

| Register   | Description, see                  |
|------------|-----------------------------------|
| CCSIDR     | Current Cache Size ID Register    |
| CCSIDR2    | Current Cache Size ID Register 2  |
| CLIDR      | Cache Level ID Register           |
| CSSELR     | Cache Size Selection Register     |
| CTR        | Cache Type Register               |
| FPSID      | Floating-Point System ID register |
| ID_AFR0    | Auxiliary Feature Register 0      |
| ID_DFR0    | Debug Feature Register 0          |
| ID_DFR1    | Debug Feature Register 1          |

## K14.5.4 Performance monitors registers

This section is an index to the registers in the Performance Monitors registers functional group.

| Register   | Description, see                                            |
|------------|-------------------------------------------------------------|
| PMCCFILTR  | Performance Monitors Cycle Count Filter Register            |
| PMCCNTR    | Performance Monitors Cycle Count Register                   |
| PMCEID0    | Performance Monitors Common Event Identification register 0 |
| PMCEID1    | Performance Monitors Common Event Identification register 1 |
| PMCEID2    | Performance Monitors Common Event Identification register 2 |

Table K14-31 Performance monitors registers

| Register   | Description, see                          |
|------------|-------------------------------------------|
| ID_ISAR0   | Instruction Set Attribute Register 0      |
| ID_ISAR1   | Instruction Set Attribute Register 1      |
| ID_ISAR2   | Instruction Set Attribute Register 2      |
| ID_ISAR3   | Instruction Set Attribute Register 3      |
| ID_ISAR4   | Instruction Set Attribute Register 4      |
| ID_ISAR5   | Instruction Set Attribute Register 5      |
| ID_ISAR6   | Instruction Set Attribute Register 6      |
| ID_MMFR0   | Memory Model Feature Register 0           |
| ID_MMFR1   | Memory Model Feature Register 1           |
| ID_MMFR2   | Memory Model Feature Register 2           |
| ID_MMFR3   | Memory Model Feature Register 3           |
| ID_MMFR4   | Memory Model Feature Register 4           |
| ID_MMFR5   | Memory Model Feature Register 5           |
| ID_PFR0    | Processor Feature Register 0              |
| ID_PFR1    | Processor Feature Register 1              |
| ID_PFR2    | Processor Feature Register 2              |
| MIDR       | Main ID Register                          |
| MPIDR      | Multiprocessor Affinity Register          |
| MVFR0      | Media and VFP Feature Register 0          |
| MVFR1      | Media and VFP Feature Register 1          |
| MVFR2      | Media and VFP Feature Register 2          |
| REVIDR     | Revision ID Register                      |
| TCMTR      | TCMType Register                          |
| TLBTR      | TLB Type Register                         |
| VMPIDR     | Virtualization Multiprocessor ID Register |
| VPIDR      | Virtualization Processor ID Register      |

| Register   | Description, see                                            |
|------------|-------------------------------------------------------------|
| PMCEID3    | Performance Monitors Common Event Identification register 3 |
| PMCNTENCLR | Performance Monitors Count Enable Clear register            |
| PMCNTENSET | Performance Monitors Count Enable Set register              |
| PMCR       | Performance Monitors Control Register                       |
| PMINTENCLR | Performance Monitors Interrupt Enable Clear register        |
| PMINTENSET | Performance Monitors Interrupt Enable Set register          |
| PMMIR      | Performance Monitors Machine Identification Register        |
| PMOVSR     | Performance Monitors Overflow Flag Status Register          |
| PMOVSSET   | Performance Monitors Overflow Flag Status Set register      |
| PMSELR     | Performance Monitors Event Counter Selection Register       |
| PMSWINC    | Performance Monitors Software Increment register            |
| PMUSERENR  | Performance Monitors User Enable Register                   |
| PMXEVCNTR  | Performance Monitors Selected Event Count Register          |
| PMXEVTYPER | Performance Monitors Selected Event Type Register           |

## K14.5.5 Activity Monitors registers

This section is an index to the registers in the Activity Monitors registers functional group.

## Table K14-32 Activity monitors registers

| Register    | Description, see                                       |
|-------------|--------------------------------------------------------|
| AMCFGR      | Activity Monitors Configuration Register               |
| AMCGCR      | Activity Monitors Counter Group Configuration Register |
| AMCNTENCLR0 | Activity Monitors Count Enable Clear Register 0        |
| AMCNTENCLR1 | Activity Monitors Count Enable Clear Register 1        |
| AMCNTENSET0 | Activity Monitors Count Enable Set Register 0          |
| AMCNTENSET1 | Activity Monitors Count Enable Set Register 1          |
| AMCR        | Activity Monitors Control Register                     |
| AMUSERENR   | Activity Monitors User Enable Register                 |

## K14.5.6 Debug registers

This section is an index to the registers in the Debug registers functional group.

## Table K14-33 Debug registers

| Register      | Description, see                                             |
|---------------|--------------------------------------------------------------|
| DBGAUTHSTATUS | Debug Authentication Status register                         |
| DBGCLAIMCLR   | Debug CLAIM Tag Clear register                               |
| DBGCLAIMSET   | Debug CLAIM Tag Set register                                 |
| DBGDCCINT     | DCCInterrupt Enable Register                                 |
| DBGDEVID      | Debug Device ID register 0                                   |
| DBGDEVID1     | Debug Device ID register 1                                   |
| DBGDEVID2     | Debug Device ID register 2                                   |
| DBGDIDR       | Debug ID Register                                            |
| DBGDRAR       | Debug ROMAddress Register                                    |
| DBGDSAR       | Debug Self Address Register                                  |
| DBGDSCRext    | Debug Status and Control Register, External View             |
| DBGDSCRint    | Debug Status and Control Register, Internal View             |
| DBGDTRRXext   | Debug OS Lock Data Transfer Register, Receive, External View |
| DBGDTRRXint   | Debug Data Transfer Register, Receive                        |
| DBGDTRTXext   | Debug OS Lock Data Transfer Register, Transmit               |
| DBGDTRTXint   | Debug Data Transfer Register, Transmit                       |
| DBGOSDLR      | Debug OS Double Lock Register                                |
| DBGOSECCR     | Debug OS Lock Exception Catch Control Register               |
| DBGOSLAR      | Debug OS Lock Access Register                                |
| DBGOSLSR      | Debug OS Lock Status Register                                |
| DBGPRCR       | Debug Power Control Register                                 |
| DBGVCR        | Debug Vector Catch Register                                  |
| DBGWFAR       | Debug Watchpoint Fault Address Register                      |
| HDCR          | Hyp Debug Control Register                                   |
| HTRFCR        | Hyp Trace Filter Control Register                            |
| TRFCR         | Trace Filter Control Register                                |

## K14.5.7 RAS registers

This section is an index to the registers in the RAS registers functional group.

## Table K14-34 RAS registers

| Register   | Description, see                   |
|------------|------------------------------------|
| DISR       | Deferred Interrupt Status Register |
| ERRIDR     | Error Record ID Register           |
| ERRSELR    | Error Record Select Register       |

## K14.5.8 Generic timer registers

This section is an index to the registers in the Generic Timer registers functional group.

## Table K14-35 Generic timer registers

| Register    | Description, see                                                |
|-------------|-----------------------------------------------------------------|
| CNTFRQ      | Counter-timer Frequency register                                |
| CNTHCTL     | Counter-timer Hyp Control register                              |
| CNTHP_CTL   | Counter-timer Hyp Physical Timer Control register               |
| CNTHP_CVAL  | Counter-timer Hyp Physical CompareValue register                |
| CNTHP_TVAL  | Counter-timer Hyp Physical Timer TimerValue register            |
| CNTHPS_CTL  | Counter-timer Secure Physical Timer Control Register (EL2)      |
| CNTHPS_CVAL | Counter-timer Secure Physical Timer CompareValue Register (EL2) |
| CNTHPS_TVAL | Counter-timer Secure Physical Timer TimerValue Register (EL2)   |
| CNTHV_CTL   | Counter-timer Virtual Timer Control register (EL2)              |
| CNTHV_CVAL  | Counter-timer Virtual Timer CompareValue register (EL2)         |
| CNTHV_TVAL  | Counter-timer Virtual Timer TimerValue register (EL2)           |
| CNTHVS_CTL  | Counter-timer Secure Virtual Timer Control Register (EL2)       |
| CNTHVS_CVAL | Counter-timer Secure Virtual Timer CompareValue Register (EL2)  |
| CNTHVS_TVAL | Counter-timer Secure Virtual Timer TimerValue Register (EL2)    |

| Register   | Description, see                               |
|------------|------------------------------------------------|
| ERXADDR    | Selected Error Record Address Register         |
| ERXADDR2   | Selected Error Record Address Register 2       |
| ERXCTLR    | Selected Error Record Control Register         |
| ERXCTLR2   | Selected Error Record Control Register 2       |
| ERXFR      | Selected Error Record Feature Register         |
| ERXFR2     | Selected Error Record Feature Register 2       |
| ERXMISC0   | Selected Error Record Miscellaneous Register 0 |
| ERXMISC1   | Selected Error Record Miscellaneous Register 1 |
| ERXMISC2   | Selected Error Record Miscellaneous Register 2 |
| ERXMISC3   | Selected Error Record Miscellaneous Register 3 |
| ERXMISC4   | Selected Error Record Miscellaneous Register 4 |
| ERXMISC5   | Selected Error Record Miscellaneous Register 5 |
| ERXMISC6   | Selected Error Record Miscellaneous Register 6 |
| ERXMISC7   | Selected Error Record Miscellaneous Register 7 |
| ERXSTATUS  | Selected Error Record Primary Status Register  |
| VDFSR      | Virtual SError Exception Syndrome Register     |
| VDISR      | Virtual Deferred Interrupt Status Register     |

| Register   | Description, see                                        |
|------------|---------------------------------------------------------|
| CNTKCTL    | Counter-timer Kernel Control register                   |
| CNTP_CTL   | Counter-timer Physical Timer Control register           |
| CNTP_CVAL  | Counter-timer Physical Timer CompareValue register      |
| CNTP_TVAL  | Counter-timer Physical Timer TimerValue register        |
| CNTPCT     | Counter-timer Physical Count register                   |
| CNTPCTSS   | Counter-timer Self-Synchronized Physical Count register |
| CNTV_CTL   | Counter-timer Virtual Timer Control register            |
| CNTV_CVAL  | Counter-timer Virtual Timer CompareValue register       |
| CNTV_TVAL  | Counter-timer Virtual Timer TimerValue register         |
| CNTVCT     | Counter-timer Virtual Count register                    |
| CNTVCTSS   | Counter-timer Self-Synchronized Virtual Count register  |
| CNTVOFF    | Counter-timer Virtual Offset register                   |

## K14.5.9 Cache maintenance system instructions

This section is an index to the registers in the Cache maintenance instructions functional group.

## Table K14-36 Cache maintenance system instructions

| System instruction   | Description, see                                         |
|----------------------|----------------------------------------------------------|
| BPIALL               | Branch Predictor Invalidate All                          |
| BPIALLIS             | Branch Predictor Invalidate All, Inner Shareable         |
| BPIMVA               | Branch Predictor Invalidate by VA                        |
| DCCIMVAC             | Data Cache line Clean and Invalidate by VA to PoC        |
| DCCISW               | Data Cache line Clean and Invalidate by Set-Way          |
| DCCMVAC              | Data Cache line Clean by VA to PoC                       |
| DCCMVAU              | Data Cache line Clean by VA to PoU                       |
| DCCSW                | Data Cache line Clean by Set-Way                         |
| DCIMVAC              | Data Cache line Invalidate by VA to PoC                  |
| DCISW                | Data Cache line Invalidate by Set-Way                    |
| ICIALLU              | Instruction Cache Invalidate All to PoU                  |
| ICIALLUIS            | Instruction Cache Invalidate All to PoU, Inner Shareable |
| ICIMVAU              | Instruction Cache line Invalidate by VA to PoU           |

## K14.5.10 Address translation system instructions

This section is an index to the registers in the Address translation instructions functional group.

## Table K14-37 Address translation system instructions

| System instruction   | Description, see                                                    |
|----------------------|---------------------------------------------------------------------|
| ATS12NSOPR           | Address Translate Stages 1 and 2 Non-secure Only PL1 Read           |
| ATS12NSOPW           | Address Translate Stages 1 and 2 Non-secure Only PL1 Write          |
| ATS12NSOUR           | Address Translate Stages 1 and 2 Non-secure Only Unprivileged Read  |
| ATS12NSOUW           | Address Translate Stages 1 and 2 Non-secure Only Unprivileged Write |
| ATS1CPR              | Address Translate Stage 1 Current state PL1 Read                    |
| ATS1CPRP             | Address Translate Stage 1 Current state PL1 Read PAN                |
| ATS1CPW              | Address Translate Stage 1 Current state PL1 Write                   |
| ATS1CPWP             | Address Translate Stage 1 Current state PL1 Write PAN               |
| ATS1CUR              | Address Translate Stage 1 Current state Unprivileged Read           |
| ATS1CUW              | Address Translate Stage 1 Current state Unprivileged Write          |
| ATS1HR               | Address Translate Stage 1 Hyp mode Read                             |
| ATS1HW               | Address Translate Stage 1 Hyp mode Write                            |

## K14.5.11 TLB maintenance system instructions

This section is an index to the registers in the TLB maintenance instructions functional group.

## Table K14-38 TLB maintenance system instructions

| System instruction   | Description, see                                          |
|----------------------|-----------------------------------------------------------|
| COSPRCTX             | Clear Other Speculative Prediction Restriction by Context |
| DTLBIALL             | Data TLB Invalidate All                                   |
| DTLBIASID            | Data TLB Invalidate by ASID match                         |
| DTLBIMVA             | Data TLB Invalidate by VA                                 |
| ITLBIALL             | Instruction TLB Invalidate All                            |
| ITLBIASID            | Instruction TLB Invalidate by ASID match                  |
| ITLBIMVA             | Instruction TLB Invalidate by VA                          |
| TLBIALL              | TLB Invalidate All                                        |
| TLBIALLH             | TLB Invalidate All, Hyp mode                              |
| TLBIALLHIS           | TLB Invalidate All, Hyp mode, Inner Shareable             |
| TLBIALLIS            | TLB Invalidate All, Inner Shareable                       |
| TLBIALLNSNH          | TLB Invalidate All, Non-Secure Non-Hyp                    |
| TLBIALLNSNHIS        | TLB Invalidate All, Non-Secure Non-Hyp, Inner Shareable   |
| TLBIASID             | TLB Invalidate by ASID match                              |
| TLBIASIDIS           | TLB Invalidate by ASID match, Inner Shareable             |
| TLBIIPAS2            | TLB Invalidate by Intermediate Physical Address, Stage 2  |

| System instruction   | Description, see                                                                      |
|----------------------|---------------------------------------------------------------------------------------|
| TLBIIPAS2IS          | TLB Invalidate by Intermediate Physical Address, Stage 2, Inner Shareable             |
| TLBIIPAS2L           | TLB Invalidate by Intermediate Physical Address, Stage 2, Last level                  |
| TLBIIPAS2LIS         | TLB Invalidate by Intermediate Physical Address, Stage 2, Last level, Inner Shareable |
| TLBIMVA              | TLB Invalidate by VA                                                                  |
| TLBIMVAA             | TLB Invalidate by VA, All ASID                                                        |
| TLBIMVAAIS           | TLB Invalidate by VA, All ASID, Inner Shareable                                       |
| TLBIMVAAL            | TLB Invalidate by VA, All ASID, Last level                                            |
| TLBIMVAALIS          | TLB Invalidate by VA, All ASID, Last level, Inner Shareable                           |
| TLBIMVAH             | TLB Invalidate by VA, Hyp mode                                                        |
| TLBIMVAHIS           | TLB Invalidate by VA, Hyp mode, Inner Shareable                                       |
| TLBIMVAIS            | TLB Invalidate by VA, Inner Shareable                                                 |
| TLBIMVAL             | TLB Invalidate by VA, Last level                                                      |
| TLBIMVALH            | TLB Invalidate by VA, Last level, Hyp mode                                            |
| TLBIMVALHIS          | TLB Invalidate by VA, Last level, Hyp mode, Inner Shareable                           |
| TLBIMVALIS           | TLB Invalidate by VA, Last level, Inner Shareable                                     |

## K14.5.12 Prediction restriction instructions

This section is an index to the registers in the Prediction restriction instructions functional group.

## Table K14-39 Cache maintenance system instructions

| System instruction   | Description, see                                 |
|----------------------|--------------------------------------------------|
| CFPRCTX              | Control Flow Prediction Restriction by Context   |
| CPPRCTX              | Cache Prefetch Prediction Restriction by Context |
| DVPRCTX              | Data Value Prediction Restriction by Context     |

## K14.5.13 Legacy feature registers and system instructions

This section is an index to the registers in the Legacy feature registers functional group.

## Table K14-40 Legacy feature registers and system instructions

| Register   | Description, see                                |
|------------|-------------------------------------------------|
| CP15DMB    | Data Memory Barrier System instruction          |
| CP15DSB    | Data Synchronization Barrier System instruction |

| Register   | Description, see                                       |
|------------|--------------------------------------------------------|
| CP15ISB    | Instruction Synchronization Barrier System instruction |
| FCSEIDR    | FCSE Process ID register                               |
| JIDR       | Jazelle ID Register                                    |
| JMCR       | Jazelle Main Configuration Register                    |
| JOSCR      | Jazelle OS Control Register                            |

## K14.5.14 Base system registers

This section is an index to the registers in the functional group.

## Table K14-41 Base system registers

| Register   | Description, see                              |
|------------|-----------------------------------------------|
| CPACR      | Architectural Feature Access Control Register |
| FCSEIDR    | FCSE Process ID register                      |
| JIDR       | Jazelle ID Register                           |
| JMCR       | Jazelle Main Configuration Register           |
| JOSCR      | Jazelle OS Control Register                   |
| SCTLR      | System Control Register                       |