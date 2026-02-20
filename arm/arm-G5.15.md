## G5.15 About the System registers for VMSAv8-32

The System registers and System instructions that are accessible in AArch32 state are almost all in the encoding space described in The AArch32 System register interface. This section gives general information about these registers, which comprise:

- Registers in the ( coproc == 0b1111 ) encoding space, that provide control and status information for the PE in Non-debug state.
- Registers in the ( coproc == 0b1110 ) encoding space, including:
- -Debug registers.
- -Trace registers.
- -Legacy execution environment registers.

Organization of registers in the ( coproc == 0b1110 ) encoding space summarizes the registers in the ( coproc == 0b1110 ) encoding space, and indicates where these registers are described, either in this manual or in other architecture specifications.

Organization of registers in the ( coproc == 0b1111 ) encoding space summarizes the registers in the ( coproc == 0b1111 ) encoding space, and indicates where in this manual these registers are described.

Note

Many implementations include other interfaces to some System registers, for example a memory-mapped interface to some debug System registers. These are described in the appropriate sections of this manual.

## G5.15.1 Classification of System registers

Features provided by EL3 and EL2 integrate with many features of the architecture. Therefore, the descriptions of the individual System registers include information about how these Exception levels affect the register. This section:

- Summarizes how EL3 and EL2 affect the implementation of the System registers, and the classification of those registers.
- Summarizes how EL3 controls access to the System registers.
- Describes an EL3 signal that can control access to some registers in the ( coproc == 0b1111 ) encoding space.

It contains the following subsections:

- Banked System registers.
- Restricted access System registers.
- Configurable access System registers.
- EL2-mode System registers.
- Common System registers.
- Access to registers from Monitor mode.
- The CP15SDISABLE and CP15SDISABLE2 input signals.

Note

EL3 defines the register classifications of Banked, Restricted access, Configurable, and Common. EL2 defines the EL2mode classification.

It is IMPLEMENTATION DEFINED whether each IMPLEMENTATION DEFINED register is Banked, Restricted access, Configurable, EL2-mode, or Common.

## G5.15.1.1 Banked System registers

In an implementation that includes EL3 using AArch32, some System registers are banked. Banked System registers have two copies, one Secure and one Non-secure. The SCR.NS bit selects the Secure or Non-secure instance of the register.

ABanked System register can contain a mixture of:

- Fields that are banked.
- Fields that are read-only in Non-secure PL1 or EL2 modes but read/write in the Secure state.

The System Control Register SCTLR is an example of a register of that contains this mixture of fields.

The Secure copies of the Banked System registers are sometimes referred to as the Secure Banked System registers. The Non-secure copies of the Banked System registers are sometimes referred to as the Non-secure Banked System registers.

## G5.15.1.2 Restricted access System registers

In an implementation that includes EL3, some System registers are present only in Secure state. These are called Restricted access registers, and their read/write access permissions are:

- In Non-secure state, software cannot modify Restricted access registers.
- For the NSACR, in Non-secure state:
- -Software running at PL1 or higher can read the register.
- -Unprivileged software, meaning software running at EL0, cannot read the register.

This means that Non-secure software running at PL1 or higher can read the access permissions for System registers that have Configurable access.

If EL3 is using AArch64, then any read of the NSACR from Non-secure EL2 using AArch32, or Non-secure EL1 using AArch32, returns the value 0x0000\_0C00 .

- For all other Restricted access registers, Non-secure software cannot read the register.

In an implementation that does not include EL3:

- SDER is implemented only in Secure state.
- Any read of the NSACR returns the value 0x0000\_0C00.
- All other accesses to Restricted access System registers are UNDEFINED.

## G5.15.1.3 Configurable access System registers

Secure software can configure the access to some System registers. These registers are called Configurable access registers, and the control can be:

- Abit in the control register determines whether the register is:
- -Accessible from Secure state only.
- -Accessible from both Secure and Non-secure states.
- Abit in the control register changes the accessibility of a register bit or field. For example, setting a bit in the control register might mean that an RW field behaves as RAZ/WI when accessed from Non-secure state.

Bits in the NSACR control access.

In an AArch32 implementation that includes EL3:

- There are no Configurable access System registers in the ( coproc == 0b1110 ) encoding space.
- The only required Configurable access register in the ( coproc == 0b1111 ) encoding space is the CPACR.
- -Floating-point Status and Control Register, FPSCR
- -Floating-point Exception register, FPEXC.
- -Floating-point System ID register, FPSID.
- -Media and VFP Feature Register 0, MVFR0.
- -Media and VFP Feature Register 1, MVFR1.
- -Media and VFP Feature Register 2, MVFR2.

## G5.15.1.4 EL2-mode System registers

In an implementation that includes EL2, if EL2 can use AArch32, the implementation provides a number of registers for use in the EL2 mode, Hyp mode. As with other System register encodings, some of these register encodings provide write-only operations. When the implementation includes EL3 and EL3 is using AArch32, these registers are also accessible from Monitor mode when the value of SCR.NS is 1.

The following subsections describe the EL2-mode registers:

- Hyp mode read/write registers in the ( coproc == 0b1111 ) encoding space.
- Hyp mode encodings for shared ( coproc == 0b1111 ) System registers.
- Hyp mode ( coproc == 0b1111 ) write-only System instructions.

There are no EL2-mode registers in the ( coproc == 0b1110 ) encoding space.

## G5.15.1.4.1 Hyp mode read/write registers in the ( coproc == 0b1111 ) encoding space

These registers are implemented only in Non-secure state, and in Non-secure state they are accessible only from Hyp mode.

Except for accesses to CNTVOFF in an implementation that includes EL3 but not EL2, the behavior of accesses to these registers is as follows:

- In Secure state, the registers can be accessed from EL3 when SCR.NS is set to 1, see Access to registers from Monitor mode.
- The following accesses are UNDEFINED:
- -Accesses from Non-secure PL1 modes.
- -Accesses in Secure state when SCR.NS is set to 0.

In an implementation that includes EL3 but not EL2, the behavior of accesses to CNTVOFF is as follows:

- Any access from Secure Monitor mode is CONSTRAINED UNPREDICTABLE, regardless of the value of SCR.NS. The CONSTRAINED UNPREDICTABLE behavior is that the access is UNDEFINED, see Unallocated System register access instructions.
- All other accesses are UNDEFINED.

Note

Except for CNTVOFF, the Hyp mode registers are part of EL2, meaning they are implemented only if the implementation includes EL2. However, conceptually, CNTVOFF is part of any implementation of the Generic Timer, see The virtual offset register. This means the behavior of CNTVOFF in an implementation that does not include EL2 is not covered by the general definition of the behavior of the Hyp mode ( coproc == 0b1111 ) read/write registers.

## G5.15.1.4.2 Hyp mode encodings for shared ( coproc == 0b1111 ) System registers

Some Hyp mode registers share the Secure instance of an existing banked register. In this case, the implementation includes an encoding for the register that is accessible only in Hyp mode, or in Monitor mode when SCR.NS is set to 1.

For these registers, the following accesses are UNDEFINED:

- Accesses from Non-secure PL1 modes.
- Accesses in Secure state when SCR.NS is set to 0.

In Monitor mode, the Secure copies of these registers can be accessed either:

- Using the DFAR or IFAR encoding with SCR.NS set to 0.
- Using the HDFAR or HIFAR encoding with SCR.NS set to 1.

However, between accessing a register using one alias and accessing the register using the other alias, a Context Synchronization event is required to ensure the ordering of the accesses.

## G5.15.1.4.3 Hyp mode ( coproc == 0b1111 ) write-only System instructions

Architecturally, these encodings are an extension of the banked register encodings described in Banked System registers, where:

- The implementation does not implement the operation in Secure state.
- In Non-secure state, the operation is accessible only at EL2, that is, only from Hyp mode.

In Secure state:

- These instructions can be accessed from Monitor mode regardless of the value of SCR.NS, see Access to registers from Monitor mode.
- Accesses to these instructions are CONSTRAINED UNPREDICTABLE if executed in a Secure mode other than Monitor mode.

Accesses to these instructions are UNDEFINED if accessed from a Non-secure PL1 mode.

## G5.15.1.5 Common System registers

Some System registers and operations are common to the Secure and Non-secure Security states. These are described as the Common access registers, or simply as the Common registers. These registers include:

- Read-only registers that hold configuration information.
- Register encodings used for various memory system operations, rather than to access registers.
- The ISR.
- All System registers in the ( coproc == 0b1110 ) encoding space.

## G5.15.1.6 Secure System registers for the ( coproc == 0b1111 ) encoding space

The Secure System registers in the ( coproc == 0b1111 ) encoding space comprise:

- The Secure copies of the Banked System registers in the ( coproc == 0b1111 ) encoding space.
- The Restricted access System registers in the ( coproc == 0b1111 ) encoding space.
- The Configurable access System registers in the ( coproc == 0b1111 ) encoding space that are configured to be accessible only from Secure state.

In an implementation that includes EL3, the Non-secure System registers are the System registers other than the Secure System registers.

## G5.15.1.7 Access to registers from Monitor mode

When the PE is in Monitor mode, the PE is in Secure state regardless of the value of the SCR.NS bit. In Monitor mode, the SCR.NS bit determines whether, for System registers in the ( coproc == 0b1111 ) encoding space, valid uses of the MRC , MCR , MRRC , and MCRR instructions access the Secure Banked System registers or the Non-secure Banked System registers. That is, when:

NS == 0

Common, Restricted access, and Secure Banked System registers are accessed by MRC , MCR , MRRC , and MCRR instructions that target the ( coproc == 0b1111 ) encoding space.

If the implementation includes EL2, the registers listed in Hyp mode read/write registers in the ( coproc == 0b1111 ) encoding space and Hyp mode encodings for shared ( coproc == 0b1111 ) System registers are not accessible, and any attempt to access them generates an Undefined Instruction exception.

Note

The operations listed in Hyp mode ( coproc == 0b1111 ) write-only System instructions are accessible in Monitor mode regardless of the value of SCR.NS.

System instructions in the ( coproc == 0b1111 ) encoding space use the Security state to determine all resources used, that is, all operations performed by these instructions are performed in Secure state.

NS == 1

Common, Restricted access and Non-secure Banked System registers are accessed by MRC , MCR , MRRC , and MCRR instructions that target the ( coproc == 0b1111 ) encoding space.

If the implementation includes EL2, all the registers and operations listed in the subsections of EL2-mode System registers are accessible, using the MRC , MCR , MRRC , or MCRR instructions required to access them from Hyp mode.

System instructions in the ( coproc == 0b1111 ) encoding space use the Security state to determine all resources used, that is, all operations by these instructions are performed in Secure state.

The Security state determines whether the Secure or Non-secure banked registers determine the control state.

Note

Where the contents of a register select the value accessed by an MRC or MCR access to a different register, then the register that is used for selection is being used as control state. For example, CSSELR selects the current Cache Size Identification Register, and therefore CSSELR is used as control state. Therefore, in Monitor mode:

- SCR.NS determines whether the Secure or Non-secure CSSELR is accessible.
- Because the PE is in Secure state, the Secure CSSELR selects the current Cache Size Identification Register.

From Armv8.3, it is possible to have multiple Cache Size Identification Registers. For more details, see Possible formats of the Cache Size Identification Registers, CCSIDR and CCSIDR2.

## G5.15.1.8 The CP15SDISABLE and CP15SDISABLE2 input signals

When EL3 is using AArch32, it provides an input signal, CP15SDISABLE , that disables write access to some of the Secure registers when asserted HIGH. The CP15SDISABLE signal has no effect on:

- Register accesses from AArch64 state.
- Register accesses from Secure EL1 when EL3 is using AArch64 and EL1 is using AArch32.

Note

When EL3 is using AArch32, the interaction between CP15SDISABLE and any IMPLEMENTATION DEFINED register is IMPLEMENTATION DEFINED.

On a Warm reset by the external system that resets the PE into EL3 using AArch32, the CP15SDISABLE input signal must be taken LOW. This permits the Reset code to set up the configuration of EL3 features. When the input is asserted HIGH, any attempt to write to the Secure registers that are affected by CP15SDISABLE results in an Undefined Instruction exception.

The CP15SDISABLE input does not affect reading Secure registers, or reading or writing Non-secure registers. It is IMPLEMENTATION DEFINED how the input is changed and when changes to this input are reflected in the PE, and an implementation might not provide any mechanism for driving the CP15SDISABLE input HIGH. However, in an implementation in which the CP15SDISABLE input can be driven HIGH, changes in the state of CP15SDISABLE must be reflected as quickly as possible. Any change must occur before completion of an Instruction Synchronization Barrier operation, issued after the change, is visible to the PE with respect to instruction execution boundaries. Software must perform an Instruction Synchronization Barrier operation meeting the above conditions to ensure all subsequent instructions are affected by the change to CP15SDISABLE .

When EL3 is using AArch32, use of CP15SDISABLE means key Secure features that are accessible only at PL1 can be locked in a known state. This provides an additional level of overall system security. Arm expects control of CP15SDISABLE to reside in the system, in a block dedicated to security.

When FEAT\_CP15SDISABLE2 is implemented and EL3 is using AArch32, EL3 provides a second input signal, CP15SDISABLE2 . CP15SDISABLE2 has all of the properties of CP15SDISABLE described above. The difference between CP15SDISABLE and CP15SDISABLE2 is only in the set of registers each signal affects.

Information on whether a given register is affected by CP15SDISABLE , or CP15SDISABLE2 when it is implemented, can be found in the access pseudocode for that register, as described in AArch32 System Register Descriptions.