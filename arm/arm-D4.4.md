## D4.4 Instruction and exception classification

INMJBZ

This section defines all of the P0 instructions .

RPBVZM

P0 instructions comprise all of the following:

- All direct P0 instructions .

- All indirect P0 instructions .

RGFNRJ

Direct P0 instructions comprise all of the following:

- All direct branch instructions.

- ISB instructions.

- TSTART instructions.

- WFE , WFET , WFI , and WFIT instructions, when indicated by TRCIDR2.WFXMODE.

RDJMQM

Indirect P0 instructions comprise all of the following:

- All indirect branch instructions.

RKJTCL

All uses of ISB in this section apply to all variants of the ISB instruction, including the CP15ISB instruction.

## D4.4.1 AArch64 instructions

## D4.4.1.1 Direct P0 instructions

RTWTMK

The following table describes the A64 direct P0 instructions .

## Table D4-6 A64 direct P0 instructions

| Instruction        | Description                                |
|--------------------|--------------------------------------------|
| B                  | Unconditional Branch                       |
| B.cond             | Conditional Branch                         |
| BC.cond            | Branch Consistent conditionally            |
| BL                 | Branch with link                           |
| CB<cc> (immediate) | Compare register with immediate and branch |
| CB<cc> (register)  | Compare registers and branch               |
| CBB<cc>            | Compare bytes and branch                   |
| CBH<cc>            | Compare halfwords and branch               |
| CBZ orCBNZ         | Compare with zero and branch               |
| ISB                | Instruction Synchronization Barrier        |
| TBZ or TBNZ        | Test and branch                            |
| TSTART             | Initiates a new transaction                |
| WFE,WFET           | Wait For Event                             |
| WFI, WFIT          | Wait For Interrupt                         |

## D4.4.1.2 Indirect P0 instructions

RLTZGC

The following table describes the A64 indirect P0 instructions .

| Instruction   | Description                       |
|---------------|-----------------------------------|
| BLR           | Branch with link to register      |
| BLRAA         | Authenticate and branch with link |
| BLRAAZ        | Authenticate and branch with link |
| BLRAB         | Authenticate and branch with link |
| BLRABZ        | Authenticate and branch with link |
| BR            | Branch to register                |
| BRAA          | Authenticate and branch           |
| BRAAZ         | Authenticate and branch           |
| BRAB          | Authenticate and branch           |
| BRABZ         | Authenticate and branch           |
| ERET          | Return From Exception             |
| ERETAA        | Authenticate and Exception return |
| ERETAB        | Authenticate and Exception return |
| RET           | Return From subroutine            |
| RETAA         | Authenticate and function return  |
| RETAASPPC     | Authenticate and function return  |
| RETAASPPCR    | Authenticate and function return  |
| RETAB         | Authenticate and function return  |
| RETABSPPC     | Authenticate and function return  |
| RETABSPPCR    | Authenticate and function return  |

## D4.4.1.3 Return from exception instructions

The following table describes the A64 return from exception instructions.

## Table D4-8 A64 return from exception instructions

| Instruction   | Description                       |
|---------------|-----------------------------------|
| ERET          | Return From Exception             |
| ERETAA        | Authenticate and Exception return |
| ERETAB        | Authenticate and Exception return |

## D4.4.1.4 Branch with link instructions

The following table describes the A64 branch with link instructions.

RBVKWS

RDVKBK

| Instruction   | Description                       |
|---------------|-----------------------------------|
| BL            | Branch with link                  |
| BLR           | Branch with link to register      |
| BLRAA         | Authenticate and branch with link |
| BLRAAZ        | Authenticate and branch with link |
| BLRAB         | Authenticate and branch with link |
| BLRABZ        | Authenticate and branch with link |

## D4.4.1.5 Meaning of Atom elements

The following table describes the meaning of Atom elements in AArch64 A64.

## Table D4-10 Meaning of Atom elements in AArch64 A64

| Instruction        | E                                                                            | N                        |
|--------------------|------------------------------------------------------------------------------|--------------------------|
| B                  | The branch was taken                                                         | RESERVED                 |
| B.cond             | The branch was taken                                                         | The branch was not taken |
| BC.cond            | The branch was taken                                                         | The branch was not taken |
| BL                 | The branch was taken                                                         | RESERVED                 |
| BLR                | The branch was taken                                                         | RESERVED                 |
| BLRAA              | The branch was taken                                                         | RESERVED                 |
| BLRAAZ             | The branch was taken                                                         | RESERVED                 |
| BLRAB              | The branch was taken                                                         | RESERVED                 |
| BLRABZ             | The branch was taken                                                         | RESERVED                 |
| BR                 | The branch was taken                                                         | RESERVED                 |
| BRAA               | The branch was taken                                                         | RESERVED                 |
| BRAAZ              | The branch was taken                                                         | RESERVED                 |
| BRAB               | The branch was taken                                                         | RESERVED                 |
| BRABZ              | The branch was taken                                                         | RESERVED                 |
| CB<cc> (immediate) | The branch was taken                                                         | The branch was not taken |
| CB<cc> (register)  | The branch was taken                                                         | The branch was not taken |
| CBB<cc>            | The branch was taken                                                         | The branch was not taken |
| CBH<cc>            | The branch was taken                                                         | The branch was not taken |
| CBZ orCBNZ         | The branch was taken                                                         | The branch was not taken |
| ERET               | The branch was taken and the PE returned from the Exception                  | RESERVED                 |
| ERETAA             | The branch was taken and the PE returned from Exception                      | RESERVED                 |
| ERETAB             | The branch was taken and the PE returned from Exception                      | RESERVED                 |
| ISB                | The ISB performed a Context synchronization event and is considered as taken | RESERVED                 |
| RET                | The branch was taken and the PE returned from the subroutine                 | RESERVED                 |

RHGDNB

| Instruction   | E                                                              | N                        |
|---------------|----------------------------------------------------------------|--------------------------|
| RETAA         | The branch was taken and the PE returned from the subroutine   | RESERVED                 |
| RETAASPPC     | The branch was taken and the PE returned from the subroutine   | RESERVED                 |
| RETAASPPCR    | The branch was taken and the PE returned from the subroutine   | RESERVED                 |
| RETAB         | The branch was taken and the PE returned from the subroutine   | RESERVED                 |
| RETABSPPC     | The branch was taken and the PE returned from the subroutine   | RESERVED                 |
| RETABSPPCR    | The branch was taken and the PE returned from the subroutine   | RESERVED                 |
| TBZ or TBNZ   | The branch was taken                                           | The branch was not taken |
| TSTART        | Transaction started and the instruction is considered as taken | RESERVED                 |
| WFE,WFET      | The instruction was executed and is considered as taken        | RESERVED                 |
| WFI, WFIT     | The instruction was executed and is considered as taken        | RESERVED                 |

## D4.4.2 AArch32 A32 instructions

## D4.4.2.1 Direct P0 instructions

RGWKSD

The following table describes the A32 direct P0 instructions .

## Table D4-11 A32 direct P0 instructions

| Instruction   | Description                         |
|---------------|-------------------------------------|
| B{<c>}        | Branch                              |
| BL            | Branch with link                    |
| BLX<immed>    | Branch with link and exchange       |
| ISB           | Instruction Synchronization Barrier |
| WFE           | Wait For Event                      |
| WFI           | Wait For Interrupt                  |

## D4.4.2.2 Indirect P0 instructions

RDTZVJ

The following table describes the A32 indirect P0 instructions .

## Table D4-12 A32 indirect P0 instructions

| Instruction                                     | Description                   |
|-------------------------------------------------|-------------------------------|
| BLX<reg>                                        | Branch with Link and Exchange |
| BX                                              | Branch and Exchange           |
| BXJ                                             | Branch and Exchange           |
| Data processing instructions that modify the PC | -                             |
| ERET                                            | Exception Return              |
| LDMincluding the PC                             | Load Multiple to the PC       |
| LDRPC                                           | Load a word to the PC         |

| Instruction   | Description           |
|---------------|-----------------------|
| RFE           | Return From Exception |

## D4.4.2.3 Branch with link instructions

RPLXGS

The following table describes the A32 branch with link instructions.

## Table D4-13 A32 branch with link instructions

| Instruction   | Description                   |
|---------------|-------------------------------|
| BL            | Branch with link              |
| BLX<immed>    | Branch with link and exchange |
| BLX<reg>      | Branch with Link and Exchange |

## D4.4.2.4 Meaning of Atom elements

RYVVSN

The following table describes the meaning of Atom elements in AArch32 A32.

## Table D4-14 Meaning of Atom elements in AArch32 A32

| Instruction                                     | E                                                                                                                        | N                                                                                      |
|-------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| B{<c>}                                          | The branch was taken                                                                                                     | The branch was not taken                                                               |
| BL                                              | The branch was taken                                                                                                     | The branch was not taken                                                               |
| BLX<immed>                                      | The branch was taken                                                                                                     | The branch was not taken                                                               |
| BLX<reg>                                        | The branch was taken                                                                                                     | The branch was not taken                                                               |
| BX                                              | The branch was taken                                                                                                     | The branch was not taken                                                               |
| BXJ                                             | The branch was taken                                                                                                     | The branch was not taken                                                               |
| Data processing instructions that modify the PC | The branch was taken                                                                                                     | The branch was not taken                                                               |
| ERET                                            | The branch was taken and the PE returned from an Exception                                                               | The branch was not taken and the PE did not return from an Exception                   |
| ISB                                             | The ISB performed a Context synchronization event and is considered as taken                                             | The ISB did not perform a Context synchronization event and is considered as not taken |
| LDMincluding the PC                             | The branch was taken                                                                                                     | The branch was not taken                                                               |
| LDRPC                                           | The branch was taken                                                                                                     | The branch was not taken                                                               |
| RFE                                             | The branch was taken and the PE returned from the Exception                                                              | RESERVED.                                                                              |
| WFE                                             | The instruction either passed its condition code check or failed its condition code check, but it is considered as taken | The instruction failed its condition code check and is considered as not taken         |
| WFI                                             | The instruction either passed its condition code check or failed its condition code check, but it is considered as taken | The instruction failed its condition code check and is considered as not taken         |

## D4.4.3 AArch32 T32 instructions

## D4.4.3.1 Direct P0 instructions

RNRJKR

The following table describes the T32 direct P0 instructions.

## Table D4-15 T32 direct P0 instructions

| Instruction   | Description                                                   |
|---------------|---------------------------------------------------------------|
| B{<c>}        | Branch                                                        |
| BL            | Branch with Link                                              |
| BLX<immed>    | Branch with Link and Exchange                                 |
| CBNZ          | Compare and Branch on Nonzero                                 |
| CBZ           | Compare and Branch on Zero                                    |
| ISB           | Instruction Synchronization Barrier, including CP15 encodings |
| WFE           | Wait For Event                                                |
| WFI           | Wait For Interrupt                                            |

## D4.4.3.2 Indirect P0 instructions

RWXDRS

The following table describes the T32 indirect P0 instructions.

## Table D4-16 T32 indirect P0 instructions

| Instruction                                     | Description                       |
|-------------------------------------------------|-----------------------------------|
| BLX<reg>                                        | Branch with Link and Exchange     |
| BX                                              | Branch and Exchange               |
| BXJ                                             | Branch and Exchange               |
| Data processing instructions that modify the PC | -                                 |
| LDMincluding the PC                             | Load Multiple including to the PC |
| LDRto the PC                                    | Load to the PC                    |
| POP {..,PC}                                     | Load the PC from the stack        |
| RFE                                             | Return From Exception             |
| TBB                                             | Table Branch                      |
| TBH                                             | Table Branch                      |

## D4.4.3.3 Branch with link instructions

RBHLTJ

The following table describes the T32 branch with link instructions.

| Instruction   | Description                   |
|---------------|-------------------------------|
| BL            | Branch with Link              |
| BLX<immed>    | Branch with Link and Exchange |
| BLX<reg>      | Branch with Link and Exchange |

## D4.4.3.4 Meaning of Atom elements

RPLGZG

The following table describes the meaning of Atom elements in AArch32 T32.

## Table D4-18 Meaning of Atom elements in AArch32 T32

| Instruction                                     | E                                                                                                                        | N                                                                                      |
|-------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| B{<c>}                                          | The branch was taken                                                                                                     | The branch was not taken                                                               |
| BL                                              | The branch was taken                                                                                                     | The branch was not taken                                                               |
| BLX<immed>                                      | The branch was taken                                                                                                     | The branch was not taken                                                               |
| BLX<reg>                                        | The branch was taken                                                                                                     | The branch was not taken                                                               |
| BX                                              | The branch was taken                                                                                                     | The branch was not taken                                                               |
| BXJ                                             | The branch was taken                                                                                                     | The branch was not taken                                                               |
| CBNZ                                            | The branch was taken                                                                                                     | The branch was not taken                                                               |
| CBZ                                             | The branch was taken                                                                                                     | The branch was not taken                                                               |
| Data processing instructions that modify the PC | The branch was taken                                                                                                     | The branch was not taken                                                               |
| ISB                                             | The ISB performed a Context synchronization event and is considered as taken                                             | The ISB did not perform a Context synchronization event and is considered as not taken |
| LDMincluding the PC                             | The branch was taken                                                                                                     | The branch was not taken                                                               |
| LDRto the PC                                    | The branch was taken                                                                                                     | The branch was not taken                                                               |
| POP {..,PC}                                     | The branch was taken                                                                                                     | The branch was not taken                                                               |
| RFE                                             | The branch was taken and the PE returned from the Exception                                                              | The branch was not taken and the PE did not return from the Exception                  |
| TBB                                             | The branch was taken                                                                                                     | The branch was not taken                                                               |
| TBH                                             | The branch was taken                                                                                                     | The branch was not taken                                                               |
| WFE                                             | The instruction either passed its condition code check or failed its condition code check, but it is considered as taken | The instruction failed its condition code check and is considered as not taken         |
| WFI                                             | The instruction either passed its condition code check or failed its condition code check, but it is considered as taken | The instruction failed its condition code check and is considered as not taken         |

## D4.4.4 Exceptions to Exception element encoding

RGZQKS

The following table shows the Exception mapping for exceptions taken to AArch64 state.

Table D4-19 Exception mapping for exceptions taken to AArch64 state

| Reason                                                         | Type         |
|----------------------------------------------------------------|--------------|
| Branch Target exception                                        | Inst fault   |
| Breakpoint                                                     | Inst debug   |
| Exceptions due to SMEfunctionality                             | Trap         |
| EXLOCKexception                                                | Inst fault   |
| FIQ                                                            | FIQ          |
| GPC exception due to data access                               | Data fault   |
| GPC exception due to instruction access                        | Inst fault   |
| Guarded Control Stack Data Check exception                     | Data fault   |
| HVC                                                            | Call         |
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
| Traps due to GCSSTR and GCSSTTR                                | Trap         |
| UNDEFINED instruction                                          | Trap         |
| Watchpoint                                                     | Data debug   |

RGPYBB

The following table shows the Exception mapping for exceptions taken to AArch32 state.

## Table D4-20 Exception mapping for exceptions taken to AArch32 state

| Reason                                        | Type         |
|-----------------------------------------------|--------------|
| Breakpoint                                    | Inst fault   |
| FIQ                                           | FIQ          |
| HVC                                           | Call         |
| Halting debug event                           | Debug halt   |
| IRQ                                           | IRQ          |
| Illegal execution state                       | Trap         |
| Instruction or event trapped by a control bit | Trap         |
| Prefetch Abort                                | Inst fault   |
| SError exception                              | System Error |
| SMC                                           | Call         |
| SVC                                           | Call         |
| Software Breakpoint Instruction               | Inst fault   |
| Synchronous Data Abort                        | Data fault   |
| UNDEFINED instruction                         | Trap         |
| Vector Catch exception                        | Inst fault   |
| Watchpoint                                    | Data fault   |