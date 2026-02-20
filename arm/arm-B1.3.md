## B1.3 Process state, PSTATE

Process state, or PSTATE, is an abstraction of process state information. All of the instruction sets provide instructions that operate on elements of PSTATE.

For the system level view of PSTATE, see Process state, PSTATE in The AArch64 System Level Programmers' Model.

The following PSTATE information is accessible at EL0:

## The Condition flags

Flag-setting instructions set these. They are:

Negative Condition flag. If the result of the instruction is regarded as a two's

- N complement signed integer, the PE sets this to:
- 1 if the result is negative.
- 0 if the result is positive or zero.
- Z Zero Condition flag. Set to:
- 1 if the result of the instruction is zero.
- 0 otherwise.

Aresult of zero often indicates an equal result from a comparison.

- C Carry Condition flag. Set to:
- 1 if the instruction results in a carry condition, for example an unsigned overflow that is the result of an addition.
- 0 otherwise.
- V Overflow Condition flag. Set to:
- 1 if the instruction results in an overflow condition, for example a signed overflow that is the result of an addition.
- 0 otherwise.

Conditional instructions test the N, Z, C and V Condition flags, combining them with the Condition code for the instruction to determine whether the instruction must be executed. In this way, execution of the instruction is conditional on the result of a previous operation. For more information about conditional execution, see Condition flags and related instructions.

## The exception masking bits

| D                             | Debug exception mask bit. When EL0 is enabled to modify the mask bits, this bit is visible and can be modified. However, this bit is architecturally ignored at EL0.   |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A                             | SError mask bit.                                                                                                                                                       |
| I                             | IRQ interrupt mask bit.                                                                                                                                                |
| F                             | FIQ interrupt mask bit.                                                                                                                                                |
| For each bit, the values are: | For each bit, the values are:                                                                                                                                          |
| 0                             | Exception not masked.                                                                                                                                                  |
| 1                             | Exception masked.                                                                                                                                                      |

SMEenable controls

SM

Streaming SVE mode enable:

0

Streaming SVE mode not enabled.

1

Streaming SVE mode enabled.

See Streaming SVE mode.

ZA

ZA storage and ZT0 register enable:

0

ZAstorage and the ZT0 register are not enabled.

1

ZAstorage and the ZT0 register are enabled.

See About PSTATE.ZA, ZA storage and SME2 ZT0 register.

## B1.3.1 Accessing PSTATE fields at EL0

At EL0 using AArch64 state, PSTATE fields can be accessed using Special-purpose registers that can be directly read using the MRS instruction and directly written using the MSR (register) instructions. Table B1-1 shows the Special-purpose registers that access the PSTATE fields that hold AArch64 state when the PE is at EL0 using AArch64. All other PSTATE fields do not have direct read and write access at EL0.

Table B1-1 Accessing PSTATE fields at EL0 using MRS and MSR (register)

| Special-purpose register   | PSTATE fields   |
|----------------------------|-----------------|
| NZCV                       | N, Z, C,V       |
| DAIF                       | D, A, I, F      |
| SVCR                       | SM,ZA           |
| SSBS                       | SSBS            |
| DIT                        | DIT             |
| TCO                        | TCO             |

Software can also use the MSR (immediate) instruction to directly write to PSTATE.{D, A, I, F, SM, ZA, SSBS, DIT, TCO}. Table B1-2 shows the MSR (immediate) operands that can directly write to PSTATE.{D, A, I, F, SM, ZA, SSBS, DIT, TCO} when the PE is at EL0 using AArch64 state.

Table B1-2 Accessing PSTATE.{D, A, I, F, SM, ZA, SSBS, DIT, TCO} at EL0 using MSR (immediate)

| Operand   | PSTATE fields   | Notes                                                    |
|-----------|-----------------|----------------------------------------------------------|
| DAIFSet   | D, A, I, F      | Directly sets any of the PSTATE.{D,A, I, F} bits to 1    |
| DAIFClr   | D, A, I, F      | Directly clears any of the PSTATE.{D, A, I, F} bits to 0 |
| SVCRSM    | SM              | Directly sets the PSTATE.SM bit to CRm<0>.               |
| SVCRZA    | ZA              | Directly sets the PSTATE.ZA bit to CRm<0>.               |
| SVCRSMZA  | SM,ZA           | Directly sets the PSTATE.{SM, ZA} bits to CRm<0>.        |
| SSBS      | SSBS            | Directly sets the PSTATE.SSBS bit to CRm<0>              |
| DIT       | DIT             | Directly sets the PSTATE.DIT bit to CRm<0>               |
| TCO       | TCO             | Directly sets the PSTATE.TCO bit to CRm<0>               |

Access to the PSTATE.{D, A, I, F} fields at EL0 using AArch64 state depends on SCTLR\_EL1.UMA.

Software can more efficiently change PSTATE.{SM, ZA} by using SMSTART and SMSTOP instructions.

Writes to the PSTATE fields have side-effects on various aspects of the PE operation. All of these side-effects, are guaranteed:

- Not to be visible to earlier instructions in the execution stream.
- To be visible to later instructions in the execution stream.

## B1.3.2 SVE use of PSTATE N, Z, C, and V Condition flags

IWYXLS

This section describes the SVE-specific use of PSTATE.

IYZYCQ

PSTATE N, Z, C and V condition flags can be updated by any of the following:

- An SVE instruction that generates a predicate result and updates the PSTATE N, Z, C and V Condition flags based on the value of the result.
- An SVE instruction that updates the PSTATE N, Z, C and V Condition flags based on the value in its predicate source register or FFR:
- -PTEST.
- -RDFFRS (predicated).
- An SVE instruction that updates the PSTATE N, Z, C and V Condition flags based on the values in its general-purpose source registers:
- -CTERMEQ.
- -CTERMNE.

| R TPXTF   | When setting the PSTATE N, Z, Cand VCondition flags for SVE predicated flag-setting instructions, the instruction's Governing predicate determines which predicate elements are considered Active.   |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R QJBRW   | When setting the PSTATE N, Z, Cand VCondition flags for SVE unpredicated flag-setting instructions, all predicate elements are considered Active.                                                    |
| R ZMRXC   | Unless otherwise specified in an instruction description, the SVE flag-setting instructions update the PSTATE N, Z,C and VCondition flags as follows:                                                |

| Flag   | SVE Name   | SVE interpretation                                                     |
|--------|------------|------------------------------------------------------------------------|
| N      | First      | Set to 1 if the First active element was TRUE, otherwise cleared to 0. |
| Z      | None       | Cleared to 0 if any Active element was TRUE, otherwise set to 1.       |
| C      | Not last   | Cleared to 0 if the Last active element was TRUE, otherwise set to 1.  |
| V      | -          | Cleared to 0.                                                          |