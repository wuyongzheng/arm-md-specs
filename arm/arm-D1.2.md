## D1.2 Registers for instruction processing and exception handling

IBCVRH

In the Arm architecture, registers are split into two main categories:

- Registers that provide system control or status reporting.

- •

- Registers that are used in instruction processing, for example to accumulate a result, and in handling exceptions.

For more information, see AArch64 System Register Descriptions.

## D1.2.1 The general-purpose registers

RJBKTZ

The general-purpose register bank comprises the 31 general-purpose registers, R0-R30.

IRKTLT

The general-purpose register bank is associated with instructions in the base instruction set.

RYDKHJ The general-purpose registers can be accessed as either of the following:

- 31 64-bit registers, X0-X30.

- 31 32-bit registers, W0-W30.

IPVGXY

When a Warm reset is asserted, the general-purpose registers are reset to an architecturally UNKNOWN value.

For more information, see Register size and Registers in AArch64 Execution state.

## D1.2.2 The stack pointer registers

RBBRKH

If in AArch64 state, each implemented Exception level has a dedicated stack pointer register. The stack pointer registers are:

- SP\_EL0.

- SP\_EL1.

- If EL2 is implemented, SP\_EL2.

- If EL3 is implemented, SP\_EL3.

IYPMHQ

When a Warm reset is asserted, the stack pointers are reset to an architecturally UNKNOWN value.

For more information, see Special purpose registers and PC alignment checking.

## D1.2.2.1 Stack pointer register selection

RCNNQX

The PE uses the following stack pointers:

- If executing at EL0, then the PE uses the EL0 stack pointer, SP\_EL0.

- If executing at EL1, EL2, or EL3, then the PE uses the stack pointer determined by PSTATE.SP:

- If PSTATE.SP is 0, then the PE uses the EL0 stack pointer, SP\_EL0.

- If PSTATE.SP is 1, then the PE uses the stack pointer for the current Exception level.

ICSFMY

When an exception is taken, the stack pointer for the target Exception level is selected.

IVYNZY

The selected stack pointer can be indicated by a suffix to the Exception level:

- The t suffix, referring to thread, indicates use of the SP\_EL0 stack pointer.

- The h suffix, referring to handler, indicates use of the SP\_ELx stack pointer.

IQZDYD

The following are the AArch64 stack pointer options:

| Exception level (EL)   | Stack pointer (SP) option   |
|------------------------|-----------------------------|
| EL0                    | SP_EL0                      |
| EL1                    | SP_EL1                      |

| Exception level (EL)   | Stack pointer (SP) option   |
|------------------------|-----------------------------|
| EL2                    | SP_EL2                      |
| EL3                    | SP_EL3                      |

## D1.2.3 The SIMD and floating-point registers

RJSCYH

The SIMD and floating-point register bank comprises the 32 quadword (128-bit) SIMD and floating-point registers, V0-V31.

ILMMMW

The SIMD and floating-point register bank is used for floating-point, vector, and other SIMD-related scalar operations.

RLFCJZ

The SIMD and floating-point registers can be accessed as any of the following:

- 32 quadword (128-bit) registers, Q0-Q31.

- 32 doubleword (64-bit) registers, D0-D31.

- 32 word (32-bit) registers, S0-S31.

- 32 halfword (16-bit) registers, H0-H31.

- 32 byte (8-bit) registers, B0-B31.

- 128-bit vectors of elements.

- 64-bit vectors of elements.

IKFYJJ

When a Warm reset is asserted, the SIMD and floating-point registers are reset to an architecturally UNKNOWN value. For more information, see Registers in AArch64 Execution state.

## D1.2.4 Saved Program Status Registers

RPJSSD

In AArch64 state, each implemented Exception level to which an exception can be taken has a Saved Program Status Register (SPSR). The following are the SPSRs:

- For exceptions taken to EL1 using AArch64, SPSR\_EL1.

- For exceptions taken to EL2 using AArch64, SPSR\_EL2.

- For exceptions taken to EL3 using AArch64, SPSR\_EL3.

IDVBPS

When a Warm reset is asserted, the SPSRs are reset to an architecturally UNKNOWN value. For more information, see Process state, PSTATE.

## D1.2.5 Exception Link Registers

RJQBYN

Exception Link Registers hold preferred exception return addresses.

RVCLNF

In AArch64 state, each implemented Exception level to which an exception can be taken has an Exception Link Register (ELR). The following are the ELRs:

- For exceptions taken to EL1, ELR\_EL1.

- For exceptions taken to EL2, ELR\_EL2.

- For exceptions taken to EL3, ELR\_EL3.

ISHJSC

When a Warm reset is asserted, the ELRs are reset to an architecturally UNKNOWN value. For more information, see Preferred exception return address.