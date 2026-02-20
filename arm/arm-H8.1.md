## H8.1 Relationship between external debug and System registers

Table H8-1 shows the relationship between external debug registers and System registers. Where no relationship exists, the registers are not listed.

Table H8-1 Equivalence between external debug and System registers

| External debug register                  | System register AArch64                  | AArch32              | Notes                                      |
|------------------------------------------|------------------------------------------|----------------------|--------------------------------------------|
| DBGDTRRX_EL0                             | DBGDTRRX_EL0                             | DBGDTRRXint          | See also Summary of System register        |
| DBGDTRTX_EL0                             | DBGDTRTX_EL0                             | DBGDTRTXint          | accesses to theDCC                         |
| OSLAR_EL1                                | OSLAR_EL1                                | DBGOSLAR             | -                                          |
| DBGBVR<n>_EL1[31:0] DBGBVR<n>_EL1[63:32] | DBGBVR<n>_EL1[31:0] DBGBVR<n>_EL1[63:32] | DBGBVR<n> DBGBXVR<n> | -                                          |
| DBGBCR<n>_EL1[31:0] DBGBCR<n>_EL1[63:32] | DBGBCR<n>_EL1[31:0] DBGBCR<n>_EL1[63:32] | DBGBCR<n>            | -                                          |
| DBGWVR<n>_EL1[31:0] DBGWVR<n>_EL1[63:32] | DBGWVR<n>_EL1[31:0] DBGWVR<n>_EL1[63:32] | DBGWVR<n>            | -                                          |
| DBGWCR<n>_EL1[31:0] DBGWCR<n>_EL1[63:32] | DBGWCR<n>_EL1[31:0] DBGWCR<n>_EL1[63:32] | DBGWCR<n>            | -                                          |
| DBGCLAIMSET_EL1                          | DBGCLAIMSET_EL1                          | DBGCLAIMSET          | -                                          |
| DBGCLAIMCLR_EL1                          | DBGCLAIMCLR_EL1                          | DBGCLAIMCLR          | -                                          |
| DBGAUTHSTATUS_EL1                        | DBGAUTHSTATUS_EL1                        | DBGAUTHSTATUS        | Read-only                                  |
| EDSCR                                    | MDSCR_EL1                                | DBGDSCRext           | Only some fields map                       |
| EDECCR                                   | OSECCR_EL1                               | DBGOSECCR            | Applies when the OS Lock is locked         |
| MIDR_EL1                                 | MIDR_EL1                                 | MIDR                 | Read-only copies of Processor ID Registers |
| EDDEVAFF0 EDDEVAFF1                      | MPIDR_EL1[31:0] a MPIDR_EL1[63:32] a     | MPIDR                | Read-only copies of system ID registers    |

## In addition:

- EDSCR.{TXfull, RXfull} are read-only aliases for DCCSR.{TXfull, RXfull}.
- EDPRCR.CORENPDRQ is a read/write alias for DBGPRCR.CORENPDRQ.
- EDPRSR.OSLK is a read-only alias for OSLSR.OSLK.
- If the FEAT\_DoubleLock is implemented, EDPRSR.DLK is a read-only function of OSDLR.DLK.