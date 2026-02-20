## C3.1 Branches, Exception generating, and System instructions

This section describes the branch, exception generating, and System instructions. It contains the following subsections:

- Conditional branch.
- Unconditional branch (immediate).
- Unconditional branch (register).
- Direct and indirect branch.
- Exception generation and return.
- System register instructions.
- System instructions.
- Hint instructions.
- Barriers and CLREX instructions.
- Pointer authentication instructions.

## Note

## Software must:

- Use only BLR or BL to perform a nested subroutine call when that subroutine is expected to return to the immediately following instruction, that is, the instruction with the address of the BLR or BL instruction incremented by four.
- Use only RET to perform a subroutine return, when that subroutine is expected to have been entered by a BL or BLR instruction.
- Use only B , BR , or the instructions listed in Table C3-1 to perform a control transfer that is not a subroutine call or subroutine return described in this Note .

## C3.1.1 Conditional branch

Conditional branches change the flow of execution depending on the following:

- The current state of the Condition flags.
- The result of comparison between 0 and a value or a bit in a general purpose register.
- The result of comparison between values in two general purpose registers.
- The result of comparison between an immediate value and a value in a general purpose register.

See Table C1-1 for a list of the Condition codes that can be used for cond .

Table C3-1 shows the Conditional branch instructions.

Table C3-1 Conditional branch instructions

| Mnemonic   | Instruction                                                  | Branch offset range from the PC   | See                |
|------------|--------------------------------------------------------------|-----------------------------------|--------------------|
| B.cond     | Branch conditionally                                         | ±1MB                              | B.cond             |
| BC.cond    | Branch Consistent conditionally                              | ±1MB                              | BC.cond            |
| CBEQ       | Compare equal to immediate and branch                        | ±1KB                              | CB<cc> (immediate) |
|            | Compare equal to register and branch                         |                                   | CB<cc> (register)  |
| CBGE       | Compare signed greater than or equal to immediate and branch | ±1KB                              | CBGE(immediate)    |

| Mnemonic   | Instruction                                                  | Branch offset range from the PC   | See                |
|------------|--------------------------------------------------------------|-----------------------------------|--------------------|
|            | Compare signed greater than or equal to register and branch  |                                   | CB<cc> (register)  |
| CBGT       | Compare signed greater than immediate and branch             | ±1KB                              | CB<cc> (immediate) |
|            | Compare signed greater than register and branch              |                                   | CB<cc> (register)  |
| CBHI       | Compare unsigned higher than immediate and branch            | ±1KB                              | CB<cc> (immediate) |
|            | Compare unsigned higher than register and branch             |                                   | CB<cc> (register)  |
| CBHS       | Compare unsigned higher than or same as immediate and branch | ±1KB                              | CBHS (immediate)   |
|            | Compare unsigned higher than or same as register and branch  |                                   | CB<cc> (register)  |
| CBLE       | Compare signed less than or equal to immediate and branch    | ±1KB                              | CBLE (immediate)   |
|            | Compare signed less than or equal to register and branch     |                                   | CBLE (register)    |
| CBLO       | Compare unsigned lower than immediate and branch             | ±1KB                              | CB<cc> (immediate) |
|            | Compare unsigned lower than register and branch              |                                   | CBLO(register)     |
| CBLS       | Compare unsigned lower than or same as immediate and branch  | ±1KB                              | CBLS (immediate)   |
|            | Compare unsigned lower than or same as register and branch   |                                   | CBLS (register)    |
| CBLT       | Compare signed less than immediate and branch                | ±1KB                              | CB<cc> (immediate) |
|            | Compare signed less than register and branch                 |                                   | CBLT (register)    |
| CBNE       | Compare not equal to immediate and branch                    | ±1KB                              | CB<cc> (immediate) |
|            | Compare not equal to register and branch                     |                                   | CB<cc> (register)  |
| CBBEQ      | Compare equal to bytes and branch                            | ±1KB                              | CBB<cc>            |
| CBBGE      | Compare signed greater than or equal to bytes and branch     |                                   |                    |
| CBBGT      | Compare signed greater than bytes and branch                 |                                   |                    |
| CBBHI      | Compare unsigned higher than bytes and branch                |                                   |                    |
| CBBHS      | Compare unsigned higher than or same as bytes and branch     |                                   |                    |
| CBBLE      | Compare signed less than or equal to bytes and branch        | ±1KB                              | CBBLE              |
| CBBLO      | Compare unsigned lower than bytes and branch                 | ±1KB                              | CBBLO              |
| CBBLS      | Compare unsigned lower than or same as bytes and branch      | ±1KB                              | CBBLS              |
| CBBLT      | Compare signed less than bytes and branch                    | ±1KB                              | CBBLT              |
| CBBNE      | Compare not equal to bytes and branch                        | ±1KB                              | CBB<cc>            |
| CBHEQ      | Compare equal to halfwords and branch                        | ±1KB                              | CBH<cc>            |
| CBHGE      | Compare signed greater than or equal to halfwords and branch |                                   |                    |

| Mnemonic   | Instruction                                                  | Branch offset range from the PC   | See     |
|------------|--------------------------------------------------------------|-----------------------------------|---------|
| CBHGT      | Compare signed greater than halfwords and branch             |                                   |         |
| CBHHI      | Compare unsigned higher than halfwords and branch            |                                   |         |
| CBHHS      | Compare unsigned higher than or same as halfwords and branch |                                   |         |
| CBHLE      | Compare signed less than or equal halfwords and branch       | ±1KB                              | CBHLE   |
| CBHLO      | Compare unsigned lower than halfwords and branch             | ±1KB                              | CBHLO   |
| CBHLS      | Compare unsigned lower than or same as halfwords and branch  | ±1KB                              | CBHLS   |
| CBHLT      | Compare signed less than halfwords and branch                | ±1KB                              | CBHLT   |
| CBHNE      | Compare not equal to halfwords and branch                    | ±1KB                              | CBH<cc> |
| CBNZ       | Compare and branch if nonzero                                | ±1MB                              | CBNZ    |
| CBZ        | Compare and branch if zero                                   | ±1MB                              | CBZ     |
| TBNZ       | Test bit and branch if nonzero                               | ±32KB                             | TBNZ    |
| TBZ        | Test bit and branch if zero                                  | ±32KB                             | TBZ     |

## C3.1.2 Unconditional branch (immediate)

Unconditional branch (immediate) instructions change the flow of execution unconditionally by adding an immediate offset with a range of ±128MB to the value of the program counter that fetched the instruction. The BL instruction also writes the address of the sequentially following instruction to general-purpose register, X30.

Table C3-2 shows the Unconditional branch instructions with an immediate branch offset.

Table C3-2 Unconditional branch instructions (immediate)

| Mnemonic   | Instruction            | Immediate branch offset range from the PC   | See   |
|------------|------------------------|---------------------------------------------|-------|
| B          | Branch unconditionally | ±128MB                                      | B     |
| BL         | Branch with link       | ±128MB                                      | BL    |

## C3.1.3 Unconditional branch (register)

Unconditional branch (register) instructions change the flow of execution unconditionally by setting the program counter to the value in a general-purpose register. The BLR instruction also writes the address of the sequentially following instruction to general-purpose register X30. The RET instruction behaves identically to BR , but provides an additional hint to the PE that this is a return from a subroutine. Table C3-3 shows Unconditional branch instructions that jump directly to an address held in a general-purpose register.

## Table C3-3 Unconditional branch instructions (register)

| Mnemonic   | Instruction                  | See   |
|------------|------------------------------|-------|
| BLR        | Branch with link to register | BLR   |
| BR         | Branch to register           | BR    |
| RET        | Return from subroutine       | RET   |

## C3.1.4 Direct and indirect branch

Table C3-4 and Table C3-5 shows the Direct branch and Indirect branch instructions.

## Table C3-4 Direct branch instructions

| Mnemonic   | Instruction                                | See                |
|------------|--------------------------------------------|--------------------|
| B          | Unconditional branch                       | B                  |
| B.cond     | Conditional branch                         | B.cond             |
| BC.cond    | Branch consistent conditionally            | BC.cond            |
| BL         | Branch with link                           | BL                 |
| CB < cc >  | Compare register with immediate and branch | CB<cc> (immediate) |
| CB < cc >  | Compare registers and branch               | CB<cc> (register)  |
| CBB < cc > | Compare bytes and branch                   | CBB<cc>            |
| CBH < cc > | Compare halfwords and branch               | CBH<cc>            |
| CBZ        | Compare and branch on zero                 | CBZ                |
| CBNZ       | Compare and branch on nonzero              | CBNZ               |
| TBZ        | Test bit and branch if zero                | TBZ                |
| TBNZ       | Test bit and branch if nonzero             | TBZ                |

## Table C3-5 Indirect branch instructions

| Mnemonic   | Instruction                                               | See                          |
|------------|-----------------------------------------------------------|------------------------------|
| BLR        | Branch with link to register                              | BLR                          |
| BLRAA      | Branch with link to register, with pointer authentication | BLRAA, BLRAAZ, BLRAB, BLRABZ |
| BLRAAZ     | Branch with link to register, with pointer authentication | BLRAA, BLRAAZ, BLRAB, BLRABZ |
| BLRAB      | Branch with link to register, with pointer authentication | BLRAA, BLRAAZ, BLRAB, BLRABZ |
| BLRABZ     | Branch with link to register, with pointer authentication | BLRAA, BLRAAZ, BLRAB, BLRABZ |
| BR         | Branch to register                                        | BR                           |
| BRAA       | Branch to register, with pointer authentication           | BRAA, BRAAZ, BRAB,BRABZ      |
| BRAAZ      | Branch to register, with pointer authentication           | BRAA, BRAAZ, BRAB,BRABZ      |
| BRAB       | Branch to register, with pointer authentication           | BRAA, BRAAZ, BRAB,BRABZ      |

| Mnemonic              | Instruction                                                                            | See                    |
|-----------------------|----------------------------------------------------------------------------------------|------------------------|
| BRABZ                 |                                                                                        |                        |
| ERET                  | Exception return                                                                       | ERET                   |
| ERETAA ERETAB         | Exception return, with pointer authentication                                          | ERETAA, ERETAB         |
| RET                   | Return from subroutine                                                                 | RET                    |
| RETAA RETAB           | Return from subroutine, with pointer authentication                                    | RETAA, RETAB           |
| RETAASPPC RETABSPPC   | Return from subroutine, with enhanced pointer authentication using an immediate offset | RETAASPPC, RETABSPPC   |
| RETAASPPCR RETABSPPCR | Return from subroutine, with enhanced pointer authentication using a register          | RETAASPPCR, RETABSPPCR |

## C3.1.5 Exception generation and return

This section describes the following exceptions:

- Exception generating.
- Exception return.
- Debug state.

## C3.1.5.1 Exception generating

Table C3-6 shows the Exception generating instructions.

## Table C3-6 Exception generating instructions

| Mnemonic   | Instruction                                    | See   |
|------------|------------------------------------------------|-------|
| BRK        | Breakpoint Instruction                         | BRK   |
| HLT        | Halt Instruction                               | HLT   |
| HVC        | Generate exception targeting Exception level 2 | HVC   |
| SMC        | Generate exception targeting Exception level 3 | SMC   |
| SVC        | Generate exception targeting Exception level 1 | SVC   |

## C3.1.5.2 Exception return

Table C3-7 shows the Exception return instructions.

## Table C3-7 Exception return instructions

| Mnemonic   | Instruction                                 | See   |
|------------|---------------------------------------------|-------|
| ERET       | Exception return using current ELR and SPSR | ERET  |

| Mnemonic        | Instruction                                   | See            |
|-----------------|-----------------------------------------------|----------------|
| ERETAA , ERETAB | Exception return, with pointer authentication | ERETAA, ERETAB |

## C3.1.5.3 Debug state

Table C3-8 shows the Debug state instructions.

## Table C3-8 Debug state instructions

| Mnemonic   | Instruction                       | See   |
|------------|-----------------------------------|-------|
| DCPS1      | Debug switch to Exception level 1 | DCPS1 |
| DCPS2      | Debug switch to Exception level 2 | DCPS2 |
| DCPS3      | Debug switch to Exception level 3 | DCPS3 |
| DRPS       | Debug restore PE state            | DRPS  |

## C3.1.6 System register instructions

For detailed information about the System register instructions, see The A64 System Instruction Class. Table C3-9 shows the System register instructions.

If FEAT\_SYSREG128 is implemented, the following instructions are added that allow the PE to move values between a 128-bit System register and two adjacent 64-bit general-purpose registers:

- MRRS.
- MSRR.

## Table C3-9 System register instructions

| Mnemonic   | Instruction                                                                   | See            |
|------------|-------------------------------------------------------------------------------|----------------|
| MRS        | Move System register to general-purpose register                              | MRS            |
| MSR        | Move general-purpose register to System register                              | MSR(register)  |
|            | Move immediate to PE state field                                              | MSR(immediate) |
| MRRS       | Move 128-bit System register to two adjacent 64-bit general-purpose registers | MRRS           |
| MSRR       | Move two adjacent 64-bit general-purpose registers to 128-bit System register | MSRR           |

## C3.1.7 System instructions

For detailed information about the System instructions, see The A64 System Instruction Class.

If FEAT\_SYSINSTR128 is implemented, the 128-bit System instruction, SYSP, is supported.

Table C3-10 shows the System instructions.

## Table C3-10 System instructions

| Mnemonic   | Instruction                    | See                 |
|------------|--------------------------------|---------------------|
| SYS        | System instruction             | SYS                 |
| SYSL       | System instruction with result | SYSL                |
| SYSP       | 128-bit System instruction     | SYSP                |
| IC         | Instruction cache maintenance  | IC and Table C5-1   |
| DC         | Data cache maintenance         | DCand Table C5-1    |
| AT         | Address translation            | AT and Table C5-3   |
| TLBI       | TLB Invalidate                 | TLBI and Table C5-4 |

## C3.1.8 Hint instructions

Table C3-11 shows the Hint instructions.

## Table C3-11 Hint instructions

| Mnemonic   | Instruction                     | See     |
|------------|---------------------------------|---------|
| NOP        | No operation                    | NOP     |
| YIELD      | Yield hint                      | YIELD   |
| WFE        | Wait for event                  | WFE     |
| WFET       | Wait for event with timeout     | WFET    |
| WFI        | Wait for interrupt              | WFI     |
| WFIT       | Wait for interrupt with timeout | WFIT    |
| SEV        | Send event                      | SEV     |
| SEVL       | Send event local                | SEVL    |
| HINT       | Unallocated hint                | HINT    |
| DGH        | Data Gathering Hint             | DGH     |
| CLRBHB     | Clear Branch History            | CLRBHB  |
| CHKFEAT    | Check Feature                   | CHKFEAT |
| STSHH      | Store Shared Hint               | STSHH   |

## C3.1.9 Barriers and CLREX instructions

Table C3-12 shows the barrier and CLREX instructions.

## Table C3-12 Barriers and CLREX instructions

| Mnemonic   | Instruction                         | See   |
|------------|-------------------------------------|-------|
| CLREX      | Clear Exclusives monitor            | CLREX |
| DMB        | Data memory barrier                 | DMB   |
| DSB        | Data synchronization barrier        | DSB   |
| ISB        | Instruction synchronization barrier | ISB   |

For more information about DSB , DMB , and ISB , see Memory barriers.

Table C3-13 shows the speculation and synchronization barriers. If these instructions are not implemented, then these instructions execute as a NOP .

Table C3-13 Speculation and synchronization barriers

| Mnemonic   | Instruction                               | See   |
|------------|-------------------------------------------|-------|
| CSDB       | Consumption of Speculative Data Barrier   | CSDB  |
| ESB        | Error synchronization barrier             | ESB   |
| PSB        | Profiling synchronization barrier         | PSB   |
| PSSBB      | Physical Speculative Store Bypass Barrier | PSSBB |
| SB         | Speculation Barrier                       | SB    |
| SSBB       | Speculative Store Bypass Barrier          | SSBB  |
| TSB        | Trace Synchronization Barrier             | TSB   |
| GCSB       | Guarded Control Stack Barrier             | GCSB  |

## For more information about:

- CSDB , PSSBB , SB , SSBB , TSB , see Memory barriers.
- ESB , see Error synchronization event.
- PSB , see The Statistical Profiling Extension.
- GCSB , see Guarded Control Stack data accesses.

## C3.1.10 Pointer authentication instructions

FEAT\_PAuth adds support for pointer authentication, see Pointer authentication. This functionality includes the A64 instructions described in this section. These instructions fall into two groups, see:

- Basic pointer authentication instructions.
- Combined instructions that include pointer authentication.

## C3.1.10.1 Basic pointer authentication instructions

Each of these instructions only performs an operation that supports pointer authentication.

Table C3-14 shows the instructions that add a Pointer Authentication Code (PAC) to the address in a register:

| Mnemonic    | Instruction                                                         | See                                       |
|-------------|---------------------------------------------------------------------|-------------------------------------------|
| PACIASP     | Add PAC to instruction address using APIAKey_EL1 and SP             | PACIA, PACIA1716, PACIASP, PACIAZ, PACIZA |
| PACIAZ      | Add PAC to instruction address using APIAKey_EL1 and zero           | PACIA, PACIA1716, PACIASP, PACIAZ, PACIZA |
| PACIA1716   | Add PAC to instruction address X17 using APIAKey_EL1 and X16        | PACIA, PACIA1716, PACIASP, PACIAZ, PACIZA |
| PACIA171615 | Add PAC to instruction address X17 using APIAKey_EL1, X16, X15      | PACIA171615                               |
| PACIASPPC   | Add PAC to instruction address LR using APIAKey_EL1, SP, PC         | PACIASPPC                                 |
| PACNBIASPPC | Add PAC to instruction address LR using APIAKey_EL1, SP, PC         | PACNBIASPPC                               |
| PACIBSP     | Add PAC to instruction address using APIBKey_EL1 and SP             | PACIB, PACIB1716, PACIBSP, PACIBZ, PACIZB |
| PACIBZ      | Add PAC to instruction address using APIBKey_EL1 and zero           | PACIB, PACIB1716, PACIBSP, PACIBZ, PACIZB |
| PACIB1716   | Add PAC to instruction address X17 using APIBKey_EL1 and X16        | PACIB, PACIB1716, PACIBSP, PACIBZ, PACIZB |
| PACIB171615 | Add PAC to instruction address X17 using APIBKey_EL1, X16, X15      | PACIB171615                               |
| PACIBSPPC   | Add PAC to instruction address LR using APIBKey_EL1, SP, PC         | PACIBSPPC                                 |
| PACNBIBSPPC | Add PAC to instruction address LR using APIBKey_EL1, SP, PC         | PACNBIBSPPC                               |
| PACIA       | Add PAC to instruction address using APIAKey_EL1, registers         | PACIA, PACIA1716, PACIASP, PACIAZ, PACIZA |
| PACDA       | Add PAC to data address using APDAKey_EL1, registers                | PACDA, PACDZA                             |
| PACIB       | Add PAC to instruction address using APIBKey_EL1, registers         | PACIB, PACIB1716, PACIBSP, PACIBZ, PACIZB |
| PACDB       | Add PAC to data address using APDBKey_EL1, registers                | PACDB, PACDZB                             |
| PACIZA      | Add PAC to instruction address using APIAKey_EL1, register and zero | PACIA, PACIA1716, PACIASP, PACIAZ, PACIZA |
| PACDZA      | Add PAC to data address using APDAKey_EL1, register and zero        | PACDA, PACDZA                             |
| PACIZB      | Add PAC to instruction address using APIBKey_EL1, register and zero | PACIB, PACIB1716, PACIBSP, PACIBZ, PACIZB |
| PACDZB      | Add PAC to data address using APDBKey_EL1, register and zero        | PACDB, PACDZB                             |
| PACGA       | Add generic PAC using APGAKey_EL1, registers                        | PACGA                                     |

Table C3-15 shows the instructions that authenticate a PAC in a register:

| Mnemonic    | Instruction                                                                                        | See                                       |
|-------------|----------------------------------------------------------------------------------------------------|-------------------------------------------|
| AUTIASP     | Authenticate PAC for instruction address using APIAKey_EL1 and SP                                  | AUTIA, AUTIA1716, AUTIASP, AUTIAZ, AUTIZA |
| AUTIAZ      | Authenticate PAC for instruction address using APIAKey_EL1 and zero                                | AUTIA, AUTIA1716, AUTIASP, AUTIAZ, AUTIZA |
| AUTIA1716   | Authenticate PAC for instruction address X17 using APIAKey_EL1 and X16                             | AUTIA, AUTIA1716, AUTIASP, AUTIAZ, AUTIZA |
| AUTIA171615 | Authenticate PAC for instruction address X17 using APIAKey_EL1, X16, and X15                       | AUTIA171615                               |
| AUTIASPPC   | Authenticate PAC for instruction address LR using APIAKey_EL1, SP, and PC with an immediate offset | AUTIASPPC                                 |
| AUTIASPPCR  | Authenticate PAC for instruction address LR using APIAKey_EL1, SP, and a register                  | AUTIASPPCR                                |
| AUTIBSP     | Authenticate PAC for instruction address using APIBKey_EL1 and SP                                  | AUTIB, AUTIB1716, AUTIBSP, AUTIBZ, AUTIZB |
| AUTIBZ      | Authenticate PAC for instruction address using APIBKey_EL1 and zero                                | AUTIB, AUTIB1716, AUTIBSP, AUTIBZ, AUTIZB |
| AUTIB1716   | Authenticate PAC for instruction address X17 using APIBKey_EL1 and X16                             | AUTIB, AUTIB1716, AUTIBSP, AUTIBZ, AUTIZB |
| AUTIB171615 | Authenticate PAC for instruction address X17 using APIBKey_EL1, X16, X15                           | AUTIB171615                               |
| AUTIBSPPC   | Authenticate PAC for instruction address LR using APIBKey_EL1, SP, and PC with an immediate offset | AUTIBSPPC                                 |
| AUTIBSPPCR  | Authenticate PAC for instruction address LR using APIBKey_EL1, SP, and a register                  | AUTIBSPPCR                                |
| AUTIA       | Authenticate PAC for instruction address using APIAKey_EL1, registers                              | AUTIA, AUTIA1716, AUTIASP, AUTIAZ, AUTIZA |
| AUTDA       | Authenticate PAC for data address using APDAKey_EL1, registers                                     | AUTDA,AUTDZA                              |
| AUTIB       | Authenticate PAC for instruction address using APIBKey_EL1, registers                              | AUTIB, AUTIB1716, AUTIBSP, AUTIBZ, AUTIZB |
| AUTDB       | Authenticate PAC for data address using APDBKey_EL1, registers                                     | AUTDB,AUTDZB                              |
| AUTIZA      | Authenticate PAC for instruction address using APIAKey_EL1, register and zero                      | AUTIA, AUTIA1716, AUTIASP, AUTIAZ, AUTIZA |
| AUTDZA      | Authenticate PAC for data address using APDAKey_EL1, register and zero                             | AUTDA,AUTDZA                              |
| AUTIZB      | Authenticate PAC for instruction address using APIBKey_EL1, register and zero                      | AUTIB, AUTIB1716, AUTIBSP, AUTIBZ, AUTIZB |
| AUTDZB      | Authenticate PAC for data address using APDBKey_EL1, register and zero                             | AUTDB,AUTDZB                              |

Table C3-15 shows the instructions that authenticate a PAC in a register:

## Table C3-16 Instructions that authenticate a PAC

| Mnemonic   | Instruction                                                                   | See                                       |
|------------|-------------------------------------------------------------------------------|-------------------------------------------|
| AUTIASP    | Authenticate PAC for instruction address using APIAKey_EL1 and SP             | AUTIA, AUTIA1716, AUTIASP, AUTIAZ, AUTIZA |
| AUTIAZ     | Authenticate PAC for instruction address using APIAKey_EL1 and zero           | AUTIA, AUTIA1716, AUTIASP, AUTIAZ, AUTIZA |
| AUTIA1716  | Authenticate PAC for instruction address X17 using APIAKey_EL1 and X16        | AUTIA, AUTIA1716, AUTIASP, AUTIAZ, AUTIZA |
| AUTIBSP    | Authenticate PAC for instruction address using APIBKey_EL1 and SP             | AUTIB, AUTIB1716, AUTIBSP, AUTIBZ, AUTIZB |
| AUTIBZ     | Authenticate PAC for instruction address using APIBKey_EL1 and zero           | AUTIB, AUTIB1716, AUTIBSP, AUTIBZ, AUTIZB |
| AUTIB1716  | Authenticate PAC for instruction address X17 using APIBKey_EL1 and X16        | AUTIB, AUTIB1716, AUTIBSP, AUTIBZ, AUTIZB |
| AUTIA      | Authenticate PAC for instruction address using APIAKey_EL1, registers         | AUTIA, AUTIA1716, AUTIASP, AUTIAZ, AUTIZA |
| AUTDA      | Authenticate PAC for data address using APDAKey_EL1, registers                | AUTDA,AUTDZA                              |
| AUTIB      | Authenticate PAC for instruction address using APIBKey_EL1, registers         | AUTIB, AUTIB1716, AUTIBSP, AUTIBZ, AUTIZB |
| AUTDB      | Authenticate PAC for data address using APDBKey_EL1, registers                | AUTDB,AUTDZB                              |
| AUTIZA     | Authenticate PAC for instruction address using APIAKey_EL1, register and zero | AUTIA, AUTIA1716, AUTIASP, AUTIAZ, AUTIZA |
| AUTDZA     | Authenticate PAC for data address using APDAKey_EL1, register and zero        | AUTDA,AUTDZA                              |
| AUTIZB     | Authenticate PAC for instruction address using APIBKey_EL1, register and zero | AUTIB, AUTIB1716, AUTIBSP, AUTIBZ, AUTIZB |
| AUTDZB     | Authenticate PAC for data address using APDBKey_EL1, register and zero        | AUTDB,AUTDZB                              |

Table C3-17 shows the instructions that strip a PAC from a register, without performing any authentication:

## Table C3-17 Instructions that strip a PAC

| Mnemonic   | Instruction                             | See                   |
|------------|-----------------------------------------|-----------------------|
| XPACLRI    | Strip instruction address PAC from LR   | XPACD, XPACI, XPACLRI |
| XPACI      | Strip instruction address PAC, register |                       |
| XPACD      | Strip data address PAC, register        |                       |

Table C3-18 shows the instructions that set PSTATE.PACM to 1:

| Mnemonic   | Instruction                     | See   |
|------------|---------------------------------|-------|
| PACM       | Pointer authentication modifier | PACM  |

## C3.1.10.2 Combined instructions that include pointer authentication

Each of these instructions combines a pointer authentication with another operation that uses the authenticated pointer. Table C3-19 shows these instructions:

## Table C3-19 Combined pointer authentication instructions

| Mnemonic   | Instruction                                                                                | See                          |
|------------|--------------------------------------------------------------------------------------------|------------------------------|
| RETAA      | Authenticate PAC for LR using APIAKey_EL1 and SP, and return                               | RETAA, RETAB                 |
| RETAB      | Authenticate PAC for LR using APIBKey_EL1 and SP, and return                               |                              |
| RETAASPPC  | Authenticate PAC for LR using APIAKey_EL1, SP, and PC with an immediate offset, and return | RETAASPPC, RETABSPPC         |
| RETABSPPC  | Authenticate PAC for LR using APIBKey_EL1, SP, and PC with an immediate offset, and return |                              |
| RETAASPPCR | Authenticate PAC for LR using APIAKey_EL1, SP, and a register, and return                  | RETAASPPCR, RETABSPPCR       |
| RETABSPPCR | Authenticate PAC for LR using APIBKey_EL1, SP, and a register, and return                  |                              |
| BRAA       | Authenticate PAC using APIAKey_EL1 (registers), and branch                                 | BRAA, BRAAZ, BRAB,BRABZ      |
| BRAB       | Authenticate PAC using APIBKey_EL1 (registers), and branch                                 |                              |
| BLRAA      | Authenticate PAC using APIAKey_EL1 (registers), and branch with link                       | BLRAA, BLRAAZ, BLRAB, BLRABZ |
| BLRAB      | Authenticate PAC using APIBKey_EL1 (registers), and branch with link                       |                              |
| BRAAZ      | Authenticate PAC using APIAKey_EL1 (register and zero), and branch                         | BRAA, BRAAZ, BRAB,BRABZ      |
| BRABZ      | Authenticate PAC using APIBKey_EL1 (register and zero), and branch                         |                              |
| BLRAAZ     | Authenticate PAC using APIAKey_EL1 (register and zero), and branch with link               | BLRAA, BLRAAZ, BLRAB, BLRABZ |
| BLRABZ     | Authenticate PAC using APIBKey_EL1 (register and zero), and branch with link               |                              |
| ERETAA     | Authenticate PAC for ELR using APIAKey_EL1 and SP, and exception return                    | ERETAA, ERETAB               |
| ERETAB     | Authenticate PAC for ELR using APIBKey_EL1 and SP, and exception return                    |                              |
| LDRAA      | Authenticate PAC for data address using APDAKey_EL1 (register and zero) and Load           | LDRAA,LDRAB                  |
| LDRAB      | Authenticate PAC for data address using APDBKey_EL1 (register and zero) and Load           |                              |

## C3.1.11 Checked Pointer Arithmetic instructions

FEAT\_CPA adds support for Checked Pointer Arithmetic, see Checked Pointer Arithmetic.

If FEAT\_CPA is implemented, the instructions shown in Table C3-20 are implemented.

## Table C3-20 Checked Pointer Arithmetic instructions

| Mnemonic   | Instruction                                                    | See    |
|------------|----------------------------------------------------------------|--------|
| ADDPT      | Scalar add checked pointer                                     | ADDPT  |
| ADDPT      | SVE add checked pointer (predicated)                           | ADDPT  |
| ADDPT      | SVE add checked pointer (unpredicated)                         | ADDPT  |
| SUBPT      | Scalar subtract checked pointer                                | SUBPT  |
| SUBPT      | SVE subtract checked pointer (predicated)                      | SUBPT  |
| SUBPT      | SVE subtract checked pointer (unpredicated)                    | SUBPT  |
| MADDPT     | Scalar multiply-add checked pointer                            | MADDPT |
| MADPT      | SVE multiply-add checked pointer vectors, writing multiplicand | MADPT  |
| MLAPT      | SVE Multiply-add checked pointer vectors, writing addend       | MLAPT  |
| MSUBPT     | Scalar multiply-subtract checked pointer                       | MSUBPT |