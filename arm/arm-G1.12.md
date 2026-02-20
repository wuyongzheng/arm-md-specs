## G1.12 Instruction set states

The instruction set states are described in The AArch32 Application Level Memory Model and application level operations on them are described there. This section supplies more information about how they interact with system level functionality, in the sections:

- Exceptions and instruction set state.
- Unimplemented instruction sets.

## G1.12.1 Exceptions and instruction set state

If an exception is taken to an EL1 mode, the SCTLR.TE bit for the Security state the exception is taken to determines the instruction set state that handles the exception, and if necessary, the PE changes to this instruction set state on exception entry.

If the exception is taken to Hyp mode, the HSCTLR.TE bit determines the instruction set state that handles the exception, and if necessary, the PE changes to this instruction set state on exception entry.

On coming out of reset, if the highest implemented Exception level is using AArch32:

- If the highest implemented Exception level is EL2, the PE starts execution in Hyp mode, in the instruction set state determined by the reset value of HSCTLR.TE.
- Otherwise, the PE starts execution in Supervisor mode, in the instruction set state determined by the reset value of SCTLR.TE. If the implementation includes EL3, this execution is in Secure Supervisor mode.

For more information about exception entry, see Overview of exception entry.

## G1.12.2 Unimplemented instruction sets

The PSTATE.T bit defines the current instruction set state, see Process state, PSTATE.

From the introduction of the Armv8 architecture, there is no support for the hardware acceleration of Java bytecodes, and the Jazelle Instruction set state is obsolete. Every AArch32 implementation must support the Trivial Jazelle implementation described in Trivial implementation of the Jazelle extension.

Note

In previous versions of the Arm architecture, the PSTATE.{J, T} bits determined the Instruction set state. From the introduction of Armv8, PSTATE.J is RES0.

## G1.12.2.1 Trivial implementation of the Jazelle extension

The implementation of AArch32 state is required to include the trivial Jazelle implementation.

In a trivial implementation of the Jazelle extension:

- At EL1, EL2, or EL3, if the Exception level is using AArch32:

- The JMCR and JOSCR are RAZ/WI.

- The JIDR is a RAZ read-only register.

- At EL0 when EL0 is using AArch32:

- It is IMPLEMENTATION DEFINED whether the JMCR and JOSCR are RAZ/WI or UNDEFINED.

- It is IMPLEMENTATION DEFINED whether JIDR is RAZ or UNDEFINED.

- The BXJ instruction behaves identically to the BX instruction in all circumstances.

Note

This is consistent with the JMCR.JE bit being RAZ, and means that the T32 and A32 instruction sets do not provide any mechanism for attempting to enter Jazelle state.

- Jazelle state, as defined in previous versions of the Arm architecture, is an unimplemented instruction set state.

These requirements ensure that operating systems that support an EJVM execute correctly.

Atrivial implementation is not required to extend the PC to 32 bits, that is, it can implement PC[0] as RAZ/WI.

Note

This is because the only way that PC[0] is visible in A32 or T32 state is as a result of an exception occurring during Jazelle state execution, and Jazelle state execution cannot occur on a trivial implementation.