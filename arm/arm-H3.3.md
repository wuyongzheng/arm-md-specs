## H3.3 Halt Instruction debug event

AHalt Instruction debug event is generated when EDSCR.HDE == 1, halting is allowed, and the PE executes the Halt instruction, HLT .

The pseudocode for Halt Instruction debug events is described in HLT for A64 and HLT for T32 and A32.

HLT never generates a debug exception. It is treated as UNDEFINED if EDSCR.HDE == 0, or if halting is prohibited.

<!-- image -->

Note

A debugger can replace a program instruction with a Halt instruction to generate a Halt Instruction debug event. Debuggers that use the HLT instruction must be aware of the rules for concurrent modification of executable code, CMODX. The rules for concurrent modification and execution of instructions do not allow one thread of execution or an external debugger to replace an instruction with an HLT instruction when these same instructions are being executed by a different thread of execution. See Concurrent modification and execution of instructions.

The T32 HLT instruction is unconditionally executed inside an IT block, even when it is treated as undefined. The A32 HLT instruction is CONSTRAINED UNPREDICTABLE if the Condition code field is not 0b1110 , with the set of behaviors the same as for BKPT . See Architectural Constraints on UNPREDICTABLE Behaviors.

Note

The HLT instruction is part of the external debug solution from the introduction of Armv8-A. As such, the presence of the HLT instruction is not indicated in the ID registers. In particular, the AArch32 System register ID\_ISAR0. Debug does not indicate the presence of the HLT instruction.

## H3.3.1 HLT instructions as the first instruction in a T32 IT block

In an implementation that supports the ITD control, the architecture permits a combination of one T32 IT instruction and certain other 16-bit T32 instruction to be treated as a single 32-bit instruction when the value of the ITD field that applies to the current Exception level is 1.

The T32 HLT instruction cannot be combined with an IT instruction in this way. In an implementation that supports the ITD control, if the first instruction in an IT block is an HLT instruction, then the behavior of the instruction depends on the value of the applicable ITD field:

- If the value of the ITD field is 1, then the combination is treated as undefined and an Undefined Instruction exception is generated either by the IT instruction or by the HLT instruction.
- If the value of the ITD field is 0, then the HLT instruction unconditionally executed.

An implementation that does not support the ITD control behaves as if the value of the ITD field is 0.

To set an Halt Instruction debug event on the first instruction of an IT block, debuggers must replace the IT instruction with an HLT instruction to ensure consistent behavior.

The ITD control fields are:

## HSCTLR.ITD

Applies to execution at EL2 when EL2 is using AArch32.

## SCTLR.ITD

Applies to execution at EL0 or EL1 when EL1 is using AArch32.

## SCTLR\_EL1.ITD

Applies to execution at EL0 using AArch32 when EL1 is using AArch64.

Note

An HLT instruction is always unconditional, even within an IT block.