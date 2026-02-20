## F2.6 Load/store instructions

Table F2-12 summarizes the general-purpose register load/store instructions in the T32 and A32 instruction sets. Some of these instructions can also operate on the PC. See also:

- Load/store multiple instructions.
- Synchronization and semaphores, for more information about the Load-Exclusive and Store-Exclusive instructions.
- Load-Acquire, Store-Release, for more information about the Load-Acquire/Store-Release and Load-Acquire Exclusive/Store-Release Exclusive instructions.
- Advanced SIMD and floating-point load/store instructions.

Load/store instructions have several options for addressing memory. For more information, see Addressing modes.

Table F2-12 Load/store instructions

|                          | Load   | Store   | Unprivileged   | Unprivileged   | Exclusive   | Exclusive   | Load- Acquire   | Store- Release   | Exclusive Load- Acquire   | Store- Release   |
|--------------------------|--------|---------|----------------|----------------|-------------|-------------|-----------------|------------------|---------------------------|------------------|
| Data type                |        |         | Load           | Store          | Load        | Store       |                 |                  |                           |                  |
| 32-bit word              | LDR    | STR     | LDRT           | STRT           | LDREX       | STREX       | LDA             | STL              | LDAEX                     | STLEX            |
| 16-bit halfword          | -      | STRH    | -              | STRHT          | -           | STREXH      | LDAH            | STLH             | LDAEXH                    | STLEXH           |
| 16-bit unsigned halfword | LDRH   | -       | LDRHT          | -              | LDREXH      | -           | -               | -                | -                         | -                |
| 16-bit signed halfword   | LDRSH  | -       | LDRSHT         | -              | -           | -           | -               | -                | -                         | -                |
| 8-bit byte               | -      | STRB    | -              | STRBT          | -           | STREXB      | LDAB            | STLB             | LDAEXB                    | STLEXB           |
| 8-bit unsigned byte      | LDRB   | -       | LDRBT          | -              | LDREXB      | -           | -               | -                | -                         | -                |
| 8-bit signed byte        | LDRSB  | -       | LDRSBT         | -              | -           | -           | -               | -                | -                         | -                |
| Two 32-bit words         | LDRD   | STRD    | -              | -              | -           | -           | -               | -                | -                         | -                |
| 64-bit doubleword        | -      | -       | -              | -              | LDREXD      | STREXD      | -               | -                | LDAEXD                    | STLEXD           |

## F2.6.1 Loads to the PC

The LDR instruction can load a value into the PC. The value loaded is treated as an interworking address, as described by the LoadWritePC() pseudocode function in Pseudocode description of operations on the AArch32 general-purpose registers and the PC.

## F2.6.2 Halfword and byte loads and stores

Halfword and byte stores store the least significant halfword or byte from the register, to 16 or 8 bits of memory respectively. There is no distinction between signed and unsigned stores.

Halfword and byte loads load 16 or 8 bits from memory into the least significant halfword or byte of a register. Unsigned loads zero-extend the loaded value to 32 bits, and signed loads sign-extend the value to 32 bits.

## F2.6.3 Load unprivileged and Store unprivileged

When executing at EL0, a Load unprivileged or Store unprivileged instruction operates in the same way as the corresponding ordinary load or store instruction. For example, an LDRT instruction executes in exactly the same way as the equivalent LDR instruction. When executed at PL1, Load unprivileged and Store unprivileged instructions behave as they would if they were executed at EL0. For example, an LDRT instruction executes in exactly the way that the equivalent LDR instruction would execute at EL0. In particular, the instructions make unprivileged memory accesses.

Note

As described in Security state, Exception levels, and AArch32 execution privilege, execution at PL1 describes all of the following:

- Execution at Non-secure EL1 using AArch32.
- Execution at Secure EL1 using AArch32 when EL3 is not implemented.
- Execution at Secure EL1 using AArch32 when EL3 is implemented and is using AArch64.
- Execution at Secure EL3 when EL3 is implemented and is using AArch32.

The Load unprivileged and Store unprivileged instructions are CONSTRAINED UNPREDICTABLE if executed at EL2.

For more information about execution privilege, see About access permissions.

## F2.6.4 Load-Exclusive and Store-Exclusive

Load-Exclusive and Store-Exclusive instructions provide shared memory synchronization. For more information, see Synchronization and semaphores.

## F2.6.5 Load-Acquire and Store-Release

Load-Acquire and Store-Release instructions provide memory barriers. Load-Acquire Exclusive and Store-Release Exclusive instructions provide memory barriers with shared memory synchronization. For more information, see Load-Acquire, Store-Release.

## F2.6.6 Addressing modes

The address for a load or store is formed from two parts: a value from a base register, and an offset.

The base register can be any one of the general-purpose registers R0-R12, SP, or LR.

For loads, the base register can be the PC. This provides PC-relative addressing for position-independent code. Instructions marked (literal) in their title in About the T32 and A32 Instruction Descriptions are PC-relative loads.

The offset takes one of three formats:

| Immediate       | The offset is an unsigned number that can be added to or subtracted from the base register value. Immediate offset addressing is useful for accessing data elements that are a fixed distance from the start of the data object, such as structure fields, stack offsets, and input/output registers.   |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Register        | The offset is a value from a general-purpose register. The value can be added to, or subtracted from, the base register value. Register offsets are useful for accessing arrays or blocks of data.                                                                                                      |
| Scaled register | The offset is a general-purpose register, shifted by an immediate value, then added to or subtracted from the base register. This means an array index can be scaled by the size of each array element.                                                                                                 |

The offset and base register can be used in three different ways to form the memory address. The addressing modes are described as follows:

| Offset       | The offset is added to or subtracted from the base register to form the memory address.                                                                                                                                                              |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Pre-indexed  | The offset is added to or subtracted from the base register to form the memory address. The base register is then updated with this new address, to permit automatic indexing through an array or memory block.                                      |
| Post-indexed | The value of the base register alone is used as the memory address. The offset is then added to or subtracted from the base register. The result is stored back in the base register, to permit automatic indexing through an array or memory block. |

Note

Not every variant is available for every instruction, and the range of permitted immediate values and the options for scaled registers vary from instruction to instruction. See About the T32 and A32 Instruction Descriptions for full details for each instruction.