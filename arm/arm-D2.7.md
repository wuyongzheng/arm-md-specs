## D2.7 Breakpoint Instruction exceptions

This section describes Breakpoint Instruction exceptions in an AArch64 translation regime.

The PE is using an AArch64 translation regime when it is executing one of the following:

- In an Exception level that is using AArch64.
- At EL0 using AArch32 when EL1 is using AArch64.
- At EL0 using AArch32 when FEAT\_VHE is implemented, EL2 is implemented and enabled in the current Security state, and the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}.

For software executing in an Exception level that is using AArch64, a Breakpoint Instruction exception results from the execution of an A64 BRK instruction. Within the AArch64 EL1&amp;0 or EL2&amp;0 translation regime, executing a T32 or A32 BKPT instruction at EL0 using AArch32 generates a Breakpoint Instruction exception.

For more information about the T32 and A32 BKPT instructions, see:

- Breakpoint instruction in the T32 and A32 instruction sets.
- BKPT instructions as the first instruction in an IT block.

The following subsections describe Breakpoint Instruction exceptions in an AArch64 translation regime:

- About Breakpoint Instruction exceptions.
- Breakpoint instructions.
- Exception syndrome information and preferred return address.
- Pseudocode description of Breakpoint Instruction exceptions.

## D2.7.1 About Breakpoint Instruction exceptions

A breakpoint is an event that results from the execution of an instruction, which is based on either:

- The instruction address, the PE context, or both. This type of breakpoint is called a hardware breakpoint.
- The instruction itself. That is, the instruction is a breakpoint instruction . These can be included in the program that the PE executes. This type of breakpoint is called a software breakpoint .

Breakpoint Instruction exceptions , which this section describes, are software breakpoints. Breakpoint exceptions describes hardware breakpoints.

There is no enable control for Breakpoint Instruction exceptions. They are always enabled, and cannot be masked.

ABreakpoint Instruction exception is generated whenever a breakpoint instruction is committed for execution, regardless of all of the following:

- The current Exception level.
- The current Security state.
- Whether the debug target Exception level , ELD, is using AArch64 or AArch32.

Note

Debuggers using breakpoint instructions must be aware of the rules for concurrent modification and execution of instructions. See Concurrent modification and execution of instructions.

## D2.7.2 Breakpoint instructions

The breakpoint instruction in the A64 instruction set is BRK #&lt;immediate&gt; . It is unconditional.

For details of the instruction encoding, see BRK.

The breakpoint instruction in the T32 and A32 instruction sets is BKPT #&lt;immediate&gt; .

For more information about the T32 and A32 breakpoint instruction, see Breakpoint instruction in the T32 and A32 instruction sets.

## D2.7.3 Exception syndrome information and preferred return address

See the following:

- Exception syndrome information.
- Preferred return address.

## D2.7.3.1 Exception syndrome information

On taking a Breakpoint Instruction exception, the PE records information about the exception in the Exception Syndrome Register (ESR) at the Exception level the exception is taken to in ESR\_ELx

Note

Breakpoint Instruction exceptions are the only debug exception that can be taken to EL3 using AArch64.

Table D2-7 shows the information that the PE records.

Table D2-7 Information recorded in the ESR\_ELx

| ESR_ELx field                       | Information recorded in ESR_EL1, ESR_EL2, or ESR_EL3.                                                                                                                       | Information recorded in ESR_EL1, ESR_EL2, or ESR_EL3.                                                                                                                       |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exception Class , EC                | Whether the breakpoint instruction was executed in AArch64 state or AArch32 state. The PE sets this to: • 0x3C for an A64 BRK instruction. • for an A32 or T32 instruction. | Whether the breakpoint instruction was executed in AArch64 state or AArch32 state. The PE sets this to: • 0x3C for an A64 BRK instruction. • for an A32 or T32 instruction. |
| Instruction Length , IL             | The PE sets this to:                                                                                                                                                        | The PE sets this to:                                                                                                                                                        |
| Instruction Specific Syndrome , ISS | ISS[24:16] ISS[15:0]                                                                                                                                                        | RES0. The PE copies the instruction Comment field value into here, zero extended as necessary.                                                                              |

Note

- If debug exceptions are routed to EL2, it is the exception that is routed, not the instruction that is trapped. Therefore, if a Breakpoint Instruction exception is routed to EL2, ESR\_EL2.EC is set to the same value as if the exception was taken to EL1.
- For information about how debug exceptions can be routed to EL2, see Routing debug exceptions.

## D2.7.3.2 Preferred return address

The preferred return address is the address of the breakpoint instruction, not the next instruction. This is different to the behavior of other exception-generating instructions, like SVC .

## D2.7.4 Pseudocode description of Breakpoint Instruction exceptions

AArch64.SoftwareBreakpoint() generates a Breakpoint Instruction exception that is taken to AArch64 state.

This function is defined in A-profile Architecture Pseudocode.