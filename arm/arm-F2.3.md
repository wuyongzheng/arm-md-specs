## F2.3 Branch instructions

Table F2-1 summarizes the branch instructions in the T32 and A32 instruction sets. In addition to providing for changes in the flow of execution, some branch instructions can change instruction set.

Table F2-1 Branch instructions

| Instruction                                                   | See                | Range, T32                 | Range, A32   |
|---------------------------------------------------------------|--------------------|----------------------------|--------------|
| Branch to target address                                      | B                  | ±16MB                      | ±32MB        |
| Compare and Branch on Nonzero Compare and Branch on Zero      | CBNZ, CBZ          | 0-126 bytes                | - a          |
| Call a subroutine Call a subroutine, change instruction set b | BL, BLX(immediate) | ±16MB ±16MB                | ±32MB ±32MB  |
| Call a subroutine, optionally change instruction set          | BLX(register)      | Any                        | Any          |
| Branch to target address, change instruction set              | BX                 | Any                        | Any          |
| Change to Jazelle state                                       | BXJ                | -                          | -            |
| Table Branch (byte offsets) Table Branch (halfword offsets)   | TBB,TBH            | 0-510 bytes 0-131070 bytes | - a          |

Branches to loaded and calculated addresses can be performed by LDR , LDM and data-processing instructions. For details, see Load/store instructions, Load/store multiple instructions, Standard data-processing instructions, and Shift instructions.

In addition to the branch instructions shown in Table F2-1:

- In the A32 instruction set, a data-processing instruction that targets the PC behaves as a branch instruction. For more information, see Data-processing instructions.
- In the T32 and A32 instruction sets, a load instruction that targets the PC behaves as a branch instruction. For more information, see Load/store instructions.