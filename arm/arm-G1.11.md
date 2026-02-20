## G1.11 Process state, PSTATE

Process state or PSTATE is an abstraction of process state information. All of the instruction sets provide instructions that operate on elements of PSTATE.

PSTATE includes all of the following:

- Fields that are meaningful only in AArch32 state.
- Fields that are meaningful only in AArch64 state.
- Fields that are meaningful in both Execution states.

PSTATE is defined in pseudocode as the PSTATE structure, of type ProcState . ProcState is defined in A-profile Architecture Pseudocode.

The PSTATE fields that are meaningful in AArch32 state are:

## The Condition flags

| N   | Negative Condition flag.   |
|-----|----------------------------|
| Z   | Zero Condition flag.       |
| C   | Carry Condition flag.      |
| V   | Overflow Condition flag.   |

Process state, PSTATE gives more information about these.

## The overflow or saturation flag

Q

The greater than or equal flags

GE[3:0]

The PE state controls

J, T

- IT[7:0]

E

See Process state, PSTATE.

See Process state, PSTATE.

Instruction set state. See PSTATE. J is RES0. On a Warm reset to AArch32 state, T is set to an IMPLEMENTATION DEFINED value. On taking an exception to:

- APL1 mode using AArch32, T is set to SCTLR.TE.
- EL2 using AArch32, T is set to HSCTLR.TE.

IT block state bits. See Process state, PSTATE. On a Warm reset or taking an exception to AArch32 state, these bits are set to 0.

- Endianness of data accesses. See Process state, PSTATE. If an implementation

provides both Big-endian and Little-endian support, then:

- On a Warm reset to AArch32 state this bit is set to the IMPLEMENTATION DEFINED reset value of:
- -SCTLR.EE if the highest implemented Exception level is not EL2.
- -HSCTLR.EE if the highest implemented Exception level is EL2.
- On taking an exception to:
- -APL1 mode using AArch32, this bit is set to SCTLR.EE.
- -EL2 using AArch32, this bit is set to HSCTLR.EE
- IL Illegal Execution state bit. See The Illegal Execution state exception. On a Warm reset or taking an exception to AArch32 state, this bit is set to 0.

## The mode bits

For information on how the J, T, IT[7:0], E, and IL fields can be accessed, see Accessing the PE state controls, the Execution state bit, and the Undefined Instruction exception injection bit.

## The asynchronous exception mask bits

A SError mask bit.

I

IRQ interrupt mask bit.

F FIQ interrupt mask bit.

For each bit, the values are:

0

Exception not masked.

1

Exception masked.

On a Warm reset to AArch32 state, these bits are set to 1.

On taking an exception to AArch32 state, one or more of these bits are set to 1.

For more information, see both:

- Asynchronous exception masking controls.
- PE state on exception entry.

M[4:0]

Current mode of the PE. Table G1-5 lists the permitted values of this field. All other values are reserved. Illegal changes to PSTATE.M describes the effect of setting M[4:0] to a reserved value.

M[4] is:

## M[4], Execution state

The current Execution state:

0 AArch64 state.

1 AArch32 state.

Note

This is consistent with the use of M[4:0] in previous versions of the architecture.

On a Warm reset to AArch32 state, M[4:0] is set to:

- 0b10011 , meaning Supervisor mode, if the highest implemented Exception level is not EL2.
- 0b11010 , meaning Hyp mode, if the highest implemented Exception level is EL2.

On taking an exception to AArch32 state, M[4:0] is set to the target mode for the exception type.

For more information about the PE modes, see:

- AArch32 state PE modes.
- PE state on exception entry.

## Inject Undefined Instruction exception bit, if FEAT\_UINJ is implemented.

UINJ

On a Warm reset, this bit is set to 0. On taking an exception, this bit is set to 0.

For information on how this bit can be accessed, see Accessing the PE state controls, the Execution state bit, and the Undefined Instruction exception injection bit.

## Access control bits, from Armv8.1

PAN

Privileged Access Never (PAN) state bit, see About the PAN bit.

Timing control bits

DIT

Data Independent Timing (DIT) bit. For more information, see About the DIT bit.

This bit is implemented only when FEAT\_DIT is implemented.

On a Warm reset to AArch32 state, this bit is set to 0.

Speculation control bits

SSBS

Speculative Store Bypass Safe (SSBS) bit. For more information, see AArch32 Speculative Store Bypass Safe.

This bit is implemented only when FEAT\_SSBS is implemented.

On a Warm reset to AArch32 state, this bit is set to an IMPLEMENTATION DEFINED value.

## G1.11.1 Accessing PSTATE fields

The PSTATE fields can be accessed as described in the following subsections:

- The Current Program Status Register, CPSR.
- Accessing the PE state controls, the Execution state bit, and the Undefined Instruction exception injection bit.
- The CPS instruction.
- The SETEND instruction.
- The SETPAN instruction.

## G1.11.1.1 The Current Program Status Register, CPSR

Some PSTATE fields can be accessed using the Special-purpose Current Program Status Register (CPSR). The CPSR can be directly read using the MRS instruction, and directly written using the MSR (register) and MSR (immediate) instructions.

The CPSR bit assignments are:

<!-- image -->

## N, Z, C, V, bits [31:28]

The PSTATE Condition flags.

Q, bit [27]

The PSTATE overflow or saturation flag.

Bits[26:23, 20, 15:10, 5]

Reserved, RES0.

SSBS, bit [23]

Speculative Store Bypass Safe (SSBS) bit, see Access permissions for instruction execution.

Bit[22]

In Armv8.0, Reserved, RES0.

In Armv8.1, Privileged Access Never (PAN) state bit, see About the PAN bit.

DIT, bit [21]

Shows the value of CPSR.DIT immediately before the exception was taken.

## GE[3:0], bits [19:16]

The PSTATE greater than or equal flags.

E, bit [9] The PSTATE endianness bit.

## A, I, F, bits [8:6]

The PSTATE asynchronous exception mask bits.

## M[4:0], bits [4:0]

The PSTATE mode bits.

The other PSTATE fields cannot be accessed by using the CPSR. For information on how to access them, see Accessing the PE state controls, the Execution state bit, and the Undefined Instruction exception injection bit.

The application level alias for the CPSR is the APSR. The APSR is a subset of the CPSR. See The Application Program Status Register, APSR.

Writes to the CPSR have side-effects on various aspects of PE operation. All of these side-effects, except side-effects on memory accesses associated with fetching instructions, are synchronous to the CPSR write. This means that they are guaranteed:

- Not to be visible to earlier instructions in the execution stream.
- To be visible to later instructions in the execution stream.

The privilege level and address space of memory accesses associated with fetching instructions depend on the current Exception level and Security state. Writes to PSTATE.M can change one or both of the Exception level and Security state. The effect, on memory accesses associated with fetching instructions, of a change of Exception level or Security state is:

- Synchronous to the change of Exception level or Security state, if that change is caused by an exception entry or exception return.
- Guaranteed not to be visible to any memory access caused by fetching an earlier instruction in the execution stream.
- Guaranteed to be visible to any memory access caused by fetching any instruction after the next Context Synchronization event in the execution stream.
- Might or might not affect memory accesses caused by fetching instructions between the mode change instruction and the point where the mode change is guaranteed to be visible.

See Exception return to an Exception level using AArch32 for the definition of exception return instructions.

## G1.11.1.2 Accessing the PE state controls, the Execution state bit, and the Undefined Instruction exception injection bit

The PE state controls are the PSTATE.{IL, IT[7:0], J, E, T} fields. Software can read or write these in an SPSR.

In the CPSR:

- The PE state controls, other than PSTATE.E, are RAZ when read by an MRS instruction.
- Writes to the PE state controls, other than PSTATE.E, by MSR (register) or MSR (immediate), are ignored in all modes.

Instructions other than MRS, MSR (register), or MSR (immediate) that access the PE state controls can read and write them in any mode.

Unlike the other PSTATE PE state controls, PSTATE.E can be read by an MRS instruction and might be written by MSR (register) or MSR (immediate). However, Arm deprecates PSTATE.E having a different value from the equivalent System register EE bit, see Mixed-endian support in AArch32.

Note

To determine the current endianness, software can use an LDR instruction to load a word from memory with a known value that differs if the endianness is reversed. For example, using an LDR instruction to load a word whose four bytes are 0x01 , 0x00 , 0x00 , and 0x00 in ascending order of memory address loads the destination register with:

- 0x0000\_0001 if the current endianness is little-endian.
- 0x0100\_0000 if the current endianness is big-endian.

The PSTATE.M[4] bit is the Execution state bit. When read by an MRS instruction in AArch32 state, this bit always reads as 1. When written by an MSR (register) instruction or MSR (immediate) instruction, writing a value other than 1 is an illegal change to the PSTATE.M field. See Illegal changes to PSTATE.M.

The PSTATE.UINJ bit is the Undefined Instruction exception injection bit, implemented when FEAT\_UINJ is implemented. Software can read or write this bit in AArch64 state in SPSR\_ELx. See Undefined Instruction exception and Undefined Instruction exceptions injected by PSTATE.UINJ.

## G1.11.1.3 The CPS instruction

The T32 and A32 instruction sets both include an instruction to manipulate PSTATE.{A, I, F} and PSTATE.M:

CPSIE &lt;iflags&gt; {, #&lt;mode&gt;} Sets the specified PSTATE. {A, I, F} exception masks to 0, enabling the exception, and optionally changes to the specified mode.

CPSID &lt;iflags&gt; {, #&lt;mode&gt;} Sets the specified PSTATE.{A, I, F} exception masks to 1, disabling the exception, and optionally changes to the specified mode.

CPS #&lt;mode&gt; Changes to the specified mode without affecting the PSTATE.{A, I, F} exception masks.

The CPS instruction is unconditional. For more information, see CPS, CPSID, CPSIE.

## G1.11.1.4 The SETEND instruction

The T32 and A32 instruction sets both include an instruction to manipulate PSTATE.E:

SETEND BE Sets PSTATE.E to 1, for big-endian operation.

SETEND LE Sets PSTATE.E to 0, for little-endian operation.

The SETEND instruction is unconditional. For more information, see SETEND. Arm deprecates use of the SETEND instruction.

## G1.11.1.5 The SETPAN instruction

FEAT\_PAN adds the SETPAN instruction to the T32 and A32 instruction sets, to manipulate PSTATE.PAN:

SETPAN #0 Sets PSTATE.PAN to 0, disabling Privileged access-never operation.

SETPAN #1 Sets PSTATE.PAN to 1, enabling Privileged access-never operation.

The SETPAN instruction is unconditional.

- SETPAN.
- About the PAN bit.

## G1.11.2 The Saved Program Status Registers (SPSRs)

On taking an exception, PSTATE is preserved in the SPSR of the mode to which the exception is taken. The SPSRs are described in Saved Program Status Registers (SPSRs).

## G1.11.3 Illegal changes to PSTATE.M

In AArch32 PE modes other than User mode, MSR and CPS instructions can explicitly change PSTATE.M. The following changes to PSTATE.M by MSR or CPS instructions are illegal:

- Achange to an encoding that Table G1-5 does not show.
- Achange to a mode that is not implemented.
- Achange to a mode that is not accessible from the context the MRS or CPS instruction is executed in, as follows:
- -Achange to a mode that would cause entry to a higher Exception level.
- -When executing in Non-secure state, a change to Monitor mode.
- -When executing in Secure EL1, a change to Monitor mode when EL3 is using AArch64.
- -Achange to Hyp mode from any other mode.
- -Achange from Hyp mode to any other mode.
- -When the value of HCR.TGE is 1, attempting to change from Monitor mode to a Non-secure PL1 mode, see Trapping of general exceptions to Hyp mode.

On executing an instruction that attempts an illegal change to PSTATE.M:

- PSTATE.M is unchanged, and the current mode remains unchanged.
- PSTATE.IL is set to 1.
- All other PSTATE fields are written to as normal.

Note

For the PSTATE fields that MSR and CPS instructions update, see the instruction descriptions:

- MSR(register).
- MSR(immediate).
- CPS, CPSID, CPSIE.

When the value of PSTATE.IL is 1, any attempt to execute any instruction results in an Illegal Execution state exception. See The Illegal Execution state exception.

Note

The PE ignores writes to PSTATE.M when executing at PL0.

## G1.11.4 Pseudocode description of PSTATE operations

The CPSRWriteByInstr() function is used by the MSR (register) and MSR (immediate) instructions to update PSTATE.

The SetPSTATEFromPSR() function updates PSTATE from a CPSR or SPSR.

A-profile Architecture Pseudocode defines these functions.