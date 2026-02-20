## G2.7 Breakpoint Instruction exceptions

This section describes Breakpoint Instruction exceptions in an AArch32 translation regime.

Note

When the PE is executing in EL0 using AArch32 and EL1 is using AArch64, it is using the AArch64 EL1&amp;0 translation regime. A T32 or A32 BKPT instruction executed at EL0 can generate a Breakpoint Instruction exception that is taken to an Exception level that is using AArch64. For more information about the handling of these exceptions, see Breakpoint Instruction exceptions.

It contains the following subsections:

- About Breakpoint Instruction exceptions.
- Breakpoint instruction in the T32 and A32 instruction sets.
- BKPT instructions as the first instruction in an IT block.
- Exception syndrome information and preferred return address for a BKPT instruction.
- Pseudocode description of Breakpoint Instruction exceptions.

## G2.7.1 About Breakpoint Instruction exceptions

A breakpoint is an event that results from the execution of an instruction, based on either:

- The instruction address, the PE context, or both. This type of breakpoint is called a hardware breakpoint.
- The instruction itself. That is, the instruction is a breakpoint instruction . These can be included in the program that the PE executes. This type of breakpoint is called a software breakpoint .

Breakpoint Instruction exceptions , that this section describes, are software breakpoints. Breakpoint exceptions describes hardware breakpoints.

There is no enable control for Breakpoint Instruction exceptions. They are always enabled, and cannot be masked.

ABreakpoint Instruction exception is generated whenever a breakpoint instruction is committed for execution, regardless of all of the following:

- The current Exception level.
- The current Security state.
- Whether the debug target Exception level , ELD, is using AArch64 or AArch32.

Note

- ELD is the Exception level that debug exceptions are targeting. See Enabling debug exceptions.
- Debuggers using breakpoint instructions must be aware of the rules for concurrent modification and execution of instructions. See Concurrent modification and execution of instructions.

## G2.7.2 Breakpoint instruction in the T32 and A32 instruction sets

The breakpoint instruction, in both instruction sets, is:

- BKPT #&lt;immediate&gt;

For details of the instruction encoding, see BKPT.

## G2.7.2.1 About whether the BKPT instruction is conditional

In the T32 instruction set, BKPT instructions are always unconditional.

In the A32 instruction set:

- If the Condition code field is AL, the BKPT instruction is unconditional.

- If the Condition code field is anything other than AL, behavior is CONSTRAINED UNPREDICTABLE, and is one of the following:

- [ ] - The instruction is UNDEFINED.

- The instruction is treated as a NOP instruction.

- The instruction is executed unconditionally.

- The instruction is executed conditionally.

## G2.7.3 BKPT instructions as the first instruction in an IT block

If the first instruction in an IT block is a T32 BKPT instruction, then in an implementation that supports the ITD control, if ITD field that applies to the current Exception level is:

- 0 The BKPT instruction generates a Breakpoint Instruction exception.

- 1 The combination of IT instruction and BKPT instruction is UNDEFINED. Either the IT instruction or the BKPT instruction generates an Undefined Instruction exception.

In such an implementation, to ensure consistent behavior when making the first instruction in one or more IT blocks a BKPT instruction, the debugger must replace the IT instruction.

An implementation that does not support the ITD control behaves as if the value of the ITD field is 0.

The ITD control fields are:

HSCTLR.ITD Applies to execution at EL2 when EL2 is using AArch32.

SCTLR.ITD Applies to execution at EL0 or EL1 when EL1 is using AArch32.

SCTLR\_EL1.ITD

Applies to execution at EL0 using AArch32 when EL1 is using AArch64.

Note

T32 BKPT instructions are always unconditional.

## G2.7.4 Exception syndrome information and preferred return address for a BKPT instruction

See the following:

- Exception syndrome information for a Breakpoint Instruction exception.

- Preferred return address for a Breakpoint Instruction exception.

Note

Usually, the term exception syndrome is used only for exceptions taken to Hyp mode, or to AArch64 state. The referenced section uses the term more generally, to include exception information reported in the IFSR.

## G2.7.4.1 Exception syndrome information for a Breakpoint Instruction exception

The PE takes a Breakpoint Instruction exception as either:

- APrefetch Abort exception if it is taken to PL1. In this case, it is taken to Abort mode.
- AHypTrap exception, if it is taken to PL2 because either HCR.TGE or HDCR.TDE is 1. In this case, it is taken to Hyp mode.

If the exception is taken to:

## PL1 Abort mode

The PE sets all of the following:

- DBGDSCRext.MOE to 0b0011 , to indicate a Breakpoint Instruction exception.
- IFSR.FS to the code for a debug, 0b00010 .
- The IFAR with an UNKNOWN value.

The PE does all of the following:

- Records information about the exception in the Hypervisor Syndrome Register , HSR. See Table G2-9.
- Sets DBGDSCRext.MOE to 0b0011 , to indicate a Breakpoint Instruction exception.
- Sets the HIFAR to an unknown value.

## PL2 Hyp mode

## Table G2-9 Information recorded in the HSR

| HSR field                           | Information recorded                                                                                                                                                                                  |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exception Class , EC                | The PE sets this to the code for a Prefetch Abort exception routed to Hyp mode, 0x20 .                                                                                                                |
| Instruction Length , IL             | The PE sets this to: • 0 for a T32 BKPT instruction. • 1 for an A32 BKPT instruction.                                                                                                                 |
| Instruction Specific Syndrome , ISS | ISS[24:10] RES0. ISS[9] External Abort type (EA). The PE sets this to 0. ISS[8:6] RES0. ISS[5:0] Instruction Fault Status Code (IFSC). The PE sets this to the code for a debug exception, 0b100010 . |

Note

For information about how debug exceptions can be routed to PL2, see Routing debug exceptions.

## G2.7.4.2 Preferred return address for a Breakpoint Instruction exception

The preferred return address is the address of the breakpoint instruction, not the next instruction. This is different to the behavior of other exception-generating instructions, like SVC .

## G2.7.5 Pseudocode description of Breakpoint Instruction exceptions

AArch32.SoftwareBreakpoint() generates a Prefetch Abort exception that is taken from AArch32 state.