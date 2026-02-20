## D19.2 Branch record filtering

INZWBP

For Branch records generated outside a BRBE Prohibited region, it is useful to reduce the number of records that are generated to match their use. Table D19-1 lists some different use cases.

## Table D19-1 Example use cases for filtering

| Use case     | Description                                                          |
|--------------|----------------------------------------------------------------------|
| Control path | • All branches • Subroutine returns • Exceptions • Exception returns |
| Call path    | • Branch with link instructions • Subroutine returns                 |
| Kernel calls | • Exceptions • Exception returns                                     |

## D19.2.1 Filtering on type

IFSNVG

RLYGJZ

The Branch records can be filtered by independently enabling the generation of the following types:

- Exception.
- Exception return.
- Direct Branch with link.
- Indirect Branch with link.
- Return from subroutine.
- Indirect Branches.
- Conditional Direct Branches.
- Unconditional Direct Branches.

Control of when Branch records for exceptions are generated is controlled by BRBCR\_EL1.EXCEPTION and BRBCR\_EL2.EXCEPTION. See Branch records for exceptions for details.

## Table D19-2 Exception mapping for exceptions taken to AArch64 state

| Reason                                     | Type       |
|--------------------------------------------|------------|
| Branch Target exception                    | Inst fault |
| Breakpoint                                 | Inst debug |
| Exceptions due to SMEfunctionality         | Trap       |
| EXLOCKexception                            | Inst fault |
| FIQ                                        | FIQ        |
| GPC exception due to data access           | Data fault |
| GPC exception due to instruction access    | Inst fault |
| Guarded Control Stack Data Check exception | Data fault |
| HVC                                        | Call       |

| Reason                                                         | Type         |
|----------------------------------------------------------------|--------------|
| Halting debug event                                            | Debug halt   |
| IRQ                                                            | IRQ          |
| Illegal execution state                                        | Trap         |
| Instruction Abort                                              | Inst fault   |
| Instruction or event trapped by a control bit                  | Trap         |
| MemCopy or MemSet                                              | Trap         |
| Misaligned PC                                                  | Alignment    |
| PAC Fail                                                       | Data fault   |
| PMUexception                                                   | Inst debug   |
| SError exception                                               | System Error |
| SMCdue to HCR_EL2.TSC                                          | Trap         |
| SMCother than due to HCR_EL2.TSC                               | Call         |
| SVC due to HFGITR_EL2.SVC_EL0 or HFGITR_EL2.SVC_EL1            | Trap         |
| SVC other than due to HFGITR_EL2.SVC_EL0 or HFGITR_EL2.SVC_EL1 | Call         |
| Software Breakpoint Instruction                                | Inst debug   |
| Software Step                                                  | Inst debug   |
| Stack Pointer Misalignment                                     | Alignment    |
| Synchronous Data Abort                                         | Data fault   |
| Traps of GCSSTR and GCSSTTR                                    | Trap         |
| UNDEFINED instruction                                          | Trap         |
| Watchpoint                                                     | Data debug   |

RRCGVB

Control of when Branch records for exception return instructions are generated is controlled by BRBCR\_EL1.ERTN and BRBCR\_EL2.ERTN. See Branch records for exception returns for details.

## Table D19-3 A64 return from exception instructions

| Instruction   | Description                       |
|---------------|-----------------------------------|
| ERET          | Return From Exception             |
| ERETAA        | Authenticate and Exception return |
| ERETAB        | Authenticate and Exception return |

RRBDXK

Each of the direct branch with link instructions only generates a Branch record when the instruction is executed in a BRBE Non-prohibited region and if any of the following are true:

- BRBFCR\_EL1.DIRCALL is 1 and BRBFCR\_EL1.EnI is 0.
- BRBFCR\_EL1.DIRCALL is 0 and BRBFCR\_EL1.EnI is 1.

| Instruction   | Description      |
|---------------|------------------|
| BL            | Branch with link |

RVBGTZ

Each of the indirect branch with link instructions only generates a Branch record when the instruction is executed in a BRBE Non-prohibited region and if any of the following are true:

- BRBFCR\_EL1.INDCALL is 1 and BRBFCR\_EL1.EnI is 0.
- BRBFCR\_EL1.INDCALL is 0 and BRBFCR\_EL1.EnI is 1.

## Table D19-5 A64 indirect branch with link instructions

| Instruction   | Description                       |
|---------------|-----------------------------------|
| BLR           | Branch with link to register      |
| BLRAA         | Authenticate and branch with link |
| BLRAAZ        | Authenticate and branch with link |
| BLRAB         | Authenticate and branch with link |
| BLRABZ        | Authenticate and branch with link |

RCKNBH

Each of the return from subroutine instructions only generates a Branch record, when the instruction is executed in a BRBE Non-prohibited region and if any of the following are true:

- BRBFCR\_EL1.RTN is 1 and BRBFCR\_EL1.EnI is 0.
- BRBFCR\_EL1.RTN is 0 and BRBFCR\_EL1.EnI is 1.

## Table D19-6 A64 return from subroutine instructions

| Instruction   | Description                      |
|---------------|----------------------------------|
| RET           | Return From subroutine           |
| RETAA         | Authenticate and function return |
| RETAASPPC     | Authenticate and function return |
| RETAASPPCR    | Authenticate and function return |
| RETAB         | Authenticate and function return |
| RETABSPPC     | Authenticate and function return |
| RETABSPPCR    | Authenticate and function return |

RKKLDV

Unless covered by other rules, each of the indirect branch instructions only generates a Branch record when the instruction is executed in a BRBE Non-prohibited region and if any of the following are true:

- BRBFCR\_EL1.INDIRECT is 1 and BRBFCR\_EL1.EnI is 0.
- BRBFCR\_EL1.INDIRECT is 0 and BRBFCR\_EL1.EnI is 1.

## Table D19-7 A64 indirect branch instructions

| Instruction   | Description             |
|---------------|-------------------------|
| BR            | Branch to register      |
| BRAA          | Authenticate and branch |
| BRAAZ         | Authenticate and branch |
| BRAB          | Authenticate and branch |
| BRABZ         | Authenticate and branch |

## RBBNSZ

Unless covered by other rules, each of the conditional direct branch instructions only generates a Branch record when the instruction is taken, is executed in a BRBE Non-prohibited region, and if any of the following are true:

- BRBFCR\_EL1.CONDDIR is 1 and BRBFCR\_EL1.EnI is 0.
- BRBFCR\_EL1.CONDDIR is 0 and BRBFCR\_EL1.EnI is 1.

## Table D19-8 A64 conditional direct branch instructions

| Instruction        | Description                                |
|--------------------|--------------------------------------------|
| B.cond             | Conditional Branch                         |
| BC.cond            | Branch Consistent conditionally            |
| CB<cc> (immediate) | Compare register with immediate and branch |
| CB<cc> (register)  | Compare registers and branch               |
| CBB<cc>            | Compare bytes and branch                   |
| CBH<cc>            | Compare halfwords and branch               |
| CBZ orCBNZ         | Compare with zero and branch               |
| TBZ or TBNZ        | Test and branch                            |

Note: BC.cond and B.cond instructions with the AL or NV condition code are considered conditional.

## RFJYVT

Unless covered by other rules, each of the unconditional direct branch instructions only generates a Branch record when the instructions are executed in a BRBE Non-prohibited region and if any of the following are true:

- BRBFCR\_EL1.DIRECT is 1 and BRBFCR\_EL1.EnI is 0.
- BRBFCR\_EL1.DIRECT is 0 and BRBFCR\_EL1.EnI is 1.

## Table D19-9 A64 unconditional direct branch instructions

| Instruction   | Description          |
|---------------|----------------------|
| B             | Unconditional Branch |

## RFJYDC

It is IMPLEMENTATION DEFINED whether Branch records are generated for each of the following taken unconditional direct branch instructions when the instruction is executed in a BRBE Non-prohibited region and if any of the following are true:

- BRBFCR\_EL1.DIRECT is 1 and BRBFCR\_EL1.EnI is 0.
- BRBFCR\_EL1.DIRECT is 0 and BRBFCR\_EL1.EnI is 1.

## Table D19-10 Optional A64 unconditional direct branch instructions

| Instruction   | Description                         |
|---------------|-------------------------------------|
| ISB           | Instruction Synchronization Barrier |

SXZRTW

Writing a value of 0b0000\_0001 to the filter controls, BRBFCR\_EL1&lt;23:16&gt;, ensures Branch records are generated for all branch instructions.