## H8.8 External debug register resets

Each register or field has a defined reset domain:

- Registers and fields in the Warm reset domain are also reset by a Cold reset and unchanged by an External Debug reset that is not coincident with a Cold reset or a Warm reset.
- Registers and fields in the Cold reset domain are unchanged by a Warm reset or an External Debug reset that is not coincident with a Cold reset.
- Registers and fields in the External Debug reset domain are unchanged by a Cold reset or a Warm reset that is not coincident with an External Debug reset.

Areset might change the value of a register. Specific rules apply to the observability of registers in the External Debug reset domain by indirect reads from the Core power domain when an External Debug reset is asserted without a coincident Cold reset. For more information, see Synchronization of changes to the external debug registers.

Table H8-2 and Table H8-5 show the external debug register and CTI register resets. For other debug registers, see Management register resets.

Note

By reference to Figure H6-1 the power domain can be deduced from the reset domain. Table K5-10 also shows reset power domains.

Table H8-2 and Table H8-5 do not include:

- Read-only identification registers, such as Processor ID Registers and PMCFGR, that have a fixed value from reset.
- Read-only status registers, such as EDSCR.RW, that are evaluated each time the register is read and that have no meaningful reset value.
- Write-only registers, such as EDRCR, that only have an effect on writes, and have no meaningful reset value.
- Read/write registers, such as breakpoint and watchpoint registers, and EDPRCR.CORENPDRQ, that alias other registers. The reset values are described by the descriptions of those other registers.
- IMPLEMENTATION DEFINED registers. The reset values and reset domains of these registers are also IMPLEMENTATION DEFINED and might be UNKNOWN.

All other fields in the registers are set to an IMPLEMENTATION DEFINED value that can be UNKNOWN. The register is in the specified reset domain.

Note

AnIMPLEMENTATION DEFINED reset value, which can be UNKNOWN, means that hardware is not required to reset the register on the specified reset, but software must not rely on the register being preserved over reset.

Table H8-7 Summary of external debug register resets, debug registers

| Register                               | Reset domain            | Field     | Value                              | Description                         |
|----------------------------------------|-------------------------|-----------|------------------------------------|-------------------------------------|
| DBGPRCR_EL1                            | Cold into AArch64 state | CORENPDRQ | The value of the powerup request a | Debug Power Control Register.       |
| DBGPRCR                                | Cold into AArch32 state | CORENPDRQ | The value of the powerup request a | Debug Power Control Register.       |
| EDESR, if FEAT_DoPD is not implemented | Warm                    | SS        | EDECR.SS                           | Halting Step debug event pending    |
| EDESR, if FEAT_DoPD is not implemented | Warm                    | RC        | EDECR.RCE                          | Reset Catch debug event pending     |
| EDESR, if FEAT_DoPD is not implemented | Warm                    | OSUC      | 0                                  | OS Unlock Catch debug event pending |

| Register                                | Reset domain   | Field      | Value         | Description                                       |
|-----------------------------------------|----------------|------------|---------------|---------------------------------------------------|
| EDESR, if FEAT_DoPD is implemented      | Cold           | SS         | 0             | Halting Step debug event pending                  |
| EDESR, if FEAT_DoPD is implemented      | Warm           | RC         | CTIDEVCTL.RCE | Reset Catch debug event pending                   |
| EDESR, if FEAT_DoPD is implemented      | Warm           | OSUC       | 0             | OS Unlock Catch debug event pending               |
| EDECR, if FEAT_DoPD is implemented      | Cold           | SS         | 0             | Halting Step debug event enable                   |
| EDECR, if FEAT_DoPD is not implemented  | External debug | SS         | 0             | Halting Step debug event enable                   |
| EDECR, if FEAT_DoPD is not implemented  | External debug | RCE        | 0             | Reset Catch debug event enable                    |
| EDECR, if FEAT_DoPD is not implemented  | External debug | OSUCE      | 0             | OS Unlock Catch debug event enable                |
| EDWAR                                   | Cold           | -          | -             | All fields                                        |
| EDSCR                                   | Cold           | RXfull     | 0             | DTRRXregister full                                |
| EDSCR                                   | Cold           | TXfull     | 0             | DTRTX register full                               |
| EDSCR                                   | Cold           | RXO        | 0             | DTRRXoverrun                                      |
| EDSCR                                   | Cold           | TXU        | 0             | DTRTX underrun                                    |
| EDSCR                                   | Cold           | INTdis     | 0             | Interrupt disable                                 |
| EDSCR                                   | Cold           | TDA        | 0             | Trap debug register accesses to Debug state       |
| EDSCR                                   | Cold           | MA         | 0             | Memory access mode in Debug state                 |
| EDSCR                                   | Cold           | HDE        | 0             | Halting debug mode enable                         |
| EDSCR                                   | Cold           | ERR        | 0             | Cumulative error flag                             |
| EDSCR2                                  | Cold           | EHBWE      | 0             | Extended Halting Breakpoint and Watchpoint Enable |
| EDSCR2                                  | Cold           | TTA        | 0             | Trap Trace Accesses                               |
| EDECCR                                  | Cold           | NSE[2:1]   | 0b00          | Coarse-grained Non-secure Exception Catch         |
| EDECCR                                  | Cold           | SE[3,1]    | 0b00          | Coarse-grained Secure Exception Catch             |
| EDPCSR                                  | Cold           | -          | -             | All fields                                        |
| EDCIDSR                                 | Cold           | -          | -             | All fields                                        |
| EDVIDSR                                 | Cold           | -          | -             | All fields                                        |
| EDPRCR, if FEAT_DoPD is implemented     | Cold           | -          | -             | -                                                 |
| EDPRCR, if FEAT_DoPD is not implemented | External debug | COREPURQ b | -             | Core powerup request                              |
| EDPRSR                                  | Warm           | SDR        | -             | Sticky debug restart                              |
| EDPRSR                                  | Cold           | SPMAD      | 0             | Sticky EPMADerror                                 |
| EDPRSR                                  | Cold           | SDAD       | 0             | Sticky EDADerror                                  |
| EDPRSR                                  | Warm           | SR         | 1             | Sticky reset status                               |
| EDPRSR                                  | Cold           | SPD        | 1             | Sticky powerdown status                           |

b. If FEAT\_DoPD is not implemented, on a Cold reset into AArch64 state, DBGPRCR\_EL1.CORENPDRQ resets to the value of EDPRCR.COREPURQ. On a Cold reset into AArch32 state, DBGPRCR.CORENPDRQ resets to the value of EDPRCR.COREPURQ. If an External Debug reset and a Cold reset coincide, both EDPRCR.COREPURQ and the CORENPDRQ field of the appropriate System register are

reset to 0.

Table H8-5 shows the reset values for the CTI registers

## Table H8-8 Summary of external debug register resets, CTI registers

| Register    | Reset domain           | Field   | Value                  | Description                                                     |
|-------------|------------------------|---------|------------------------|-----------------------------------------------------------------|
| CTICONTROL  | External debug         | GLBEN   | 0                      | CTI global enable                                               |
| CTIDEVCTL   | External debug         | RCE     | 0                      | If FEAT_DoPD is implemented, Reset Catch debug event enable     |
| CTIDEVCTL   | External debug         | OSUCE   | 0                      | If FEAT_DoPD is implemented, OS Unlock Catch debug event enable |
| CTIAPPSET   | External debug         | -       | -                      | All fields                                                      |
| CTIINEN<n>  | External debug         | -       | -                      | All fields                                                      |
| CTIOUTEN<n> | External debug         | -       | -                      | All fields                                                      |
| CTIGATE     | External debug         | -       | -                      | All fields                                                      |
| ASICCTL     | IMPLEMENTATION DEFINED | -       | IMPLEMENTATION DEFINED | All of register                                                 |

## Chapter H9 External Debug Register Descriptions

This chapter provides a description of the external debug registers. It contains the following sections:

- About the external debug registers.
- External debug registers.
- External trace registers.
- External Trace Buffer registers.
- Cross-Trigger Interface registers.