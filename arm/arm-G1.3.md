## G1.3 Exception terminology

The following subsections define the terms that are used when describing exceptions:

- Terminology for taking an exception.
- Terminology for returning from an exception.
- Exception levels.
- Definition of a precise exception.
- Definitions of synchronous and asynchronous exceptions.

## G1.3.1 Terminology for taking an exception

An exception is generated when the PE first responds to an exceptional condition. The PE state at this time is the state that the exception is taken from . The PE state immediately after taking the exception is the state that the exception is taken to .

## G1.3.2 Terminology for returning from an exception

To return from an exception, the PE must execute an exception return instruction. The PE state when an exception return instruction is committed for execution is the state the exception returns from . The PE state immediately after the execution of that instruction is the state that the exception returns to .

## G1.3.3 Exception levels

An Exception level, EL n , with a larger value of n than another Exception level, is described as being a higher Exception level than the other Exception level. For example, EL3 is a higher Exception level than EL1.

An Exception level with a smaller value of n than another Exception level is described as being a lower Exception level than the other Exception level. For example, EL0 is a lower Exception level than EL1.

An Exception level is described as:

- Using AArch64 when execution in that Exception level is in the AArch64 Execution state.
- Using AArch32 when execution in that Exception level is in the AArch32 Execution state.

## G1.3.4 Definition of a precise exception

An exception is described as precise when the exception handler receives the PE state and memory system state that is consistent with the PE having executed all of the instructions up to but not including the point in the instruction stream where the exception was taken, and none afterwards.

An exception is described as imprecise if it is not precise.

Other than the SError exception all exceptions that are taken to AArch32 state are required to be precise. For each occurrence of an SError exception, whether the interrupt is precise or imprecise is IMPLEMENTATION DEFINED.

The terms precise and imprecise can also apply to Debug entry state. See Imprecise entry to Debug state.

Where a synchronous exception that is taken to AArch32 state is generated as part of an instruction that performs more than one single-copy atomic memory access, the definition of precise permits that the values in registers or memory affected by those instructions can be UNKNOWN, provided that:

- The accesses affecting those registers or memory locations do not, themselves, generate exceptions.
- The registers are not involved in the calculation of the memory address that is used by the instruction.

In AArch32 state, examples of instructions that perform more than one single-copy atomic memory access are the LDM and STM instructions.

Note

For the definition of a single-copy atomic access, see Properties of single-copy atomic accesses.

## G1.3.5 Definitions of synchronous and asynchronous exceptions

An exception is described as synchronous if all of the following apply:

- The exception is generated as a result of direct execution or attempted execution of an instruction.
- The return address presented to the exception handler is guaranteed to indicate the instruction that caused the exception.
- The exception is precise.

An exception is described as asynchronous if any of the following apply:

- The exception is not generated as a result of direct execution or attempted execution of the instruction stream.
- The return address presented to the exception handler is not guaranteed to indicate the instruction that caused the exception.
- The exception is imprecise.

For more information about exceptions, see Handling exceptions that are taken to an Exception level using AArch32.