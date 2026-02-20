## G1.20 The AArch32 System register interface

Most System registers are accessed using the instructions described in System register access instructions. The System register interface provides access to those instructions, and:

- These registers are encoded using the parameters { coproc , opc1 , CRn , CRm , opc2 }, with permitted coproc values of 0b1110 and 0b1111 .
- Some of these encodings provide the AArch32 System instructions.
- To maintain compatibility with previous versions of the Arm architecture, the access controls for the AArch32 System registers include the access controls for AArch32 Advanced SIMD and floating-point functionality.

Note

See Background to the System register interface for more information.

The following sections give more information about the AArch32 System register interface:

- System registers in the coproc == 0b111x encoding space.
- Access to System registers.
- Access controls for Advanced SIMD and floating-point functionality.
- Background to the System register interface.

## G1.20.1 System registers in the coproc == 0b111x encoding space

In AArch32 state:

- The coproc == 0b1110 encoding space is reserved for the configuration and control of:
- -Debug features, see Debug registers.
- -Trace features, see the Embedded Trace Macrocell Architecture Specification .
- -Identification registers for the Trivial Jazelle implementation, see Trivial implementation of the Jazelle extension.
- The coproc == 0b1111 encoding space is reserved for the control and configuration of the PE, including architecture and feature identification. This means these encodings provide access to the System registers that control and return status information for PE operation.

For more information, see AArch32 System Register Descriptions.

## G1.20.2 Access to System registers

Most System registers are accessible only from EL1 or higher. For possible accesses from EL0 the register descriptions in AArch32 System Register Descriptions indicate whether a register is accessible from EL0.

## G1.20.3 Access controls for Advanced SIMD and floating-point functionality

The CPACR controls access to Advanced SIMD and floating-point functionality from software executing at PL1 or EL0 in AArch32 state:

- The {cp10, cp11} fields control access to all Advanced SIMD and floating-point functionality, and can:
- -Disable EL0 and PL1 access to this functionality.
- -Enable access to this functionality at PL1 only.
- -Enable access to this functionality at EL0 and PL1.
- The ASEDIS field controls access to Advanced SIMD instructions that are not also floating-point instructions.

Initially on powerup or reset into AArch32 state, all access to all Advanced SIMD and floating-point functionality from PL1 and EL0 is disabled.

Note

The CPACR has no effect on accesses from Hyp mode.

If an implementation includes EL3, the NSACR determines whether Advanced SIMD and floating-point functionality can be accessed from Non-secure state:

- The {cp10, cp11} fields control Non-secure access to all Advanced SIMD and floating-point functionality.
- The NSASEDIS field controls Non-secure access to Advanced SIMD instructions that are not also floating-point instructions.

If an implementation includes EL2, the HCPTR provides additional controls on Non-secure accesses to Advanced SIMD and floating-point functionality. For accesses that are otherwise permitted by the CPACR and NSACR settings, setting HCPTR bits to 1:

- Traps otherwise-permitted accesses from EL1 or EL0 to EL2. When EL2 is using AArch32, these accesses are trapped to Hyp mode.
- Makes accesses from EL2 mode UNDEFINED. When EL2 is using AArch32, this makes accesses from Hyp mode UNDEFINED.

## In the HCPTR:

- The {TCP10, TCP11} fields control access to all Advanced SIMD and floating-point functionality.
- The TASE field controls access to Advanced SIMD instructions that are not also floating-point instructions.
- The TCPAC field traps Non-secure EL1 accesses to the CPACR to Hyp mode.

Note

Whenever a pair of fields control the access to the Advanced SIMD and floating-point functionality, the values of each field of the pair must be identical. If these settings are not identical the behavior of the Advanced SIMD and floating-point functionality is CONSTRAINED UNPREDICTABLE, see Handling of System register control fields for Advanced SIMD and floating-point operation.

For more information about Advanced SIMD and floating-point support, see Advanced SIMD and floating-point support.

## G1.20.4 Background to the System register interface

Note

This section is not part of the Architecture specification. It is included only to present the rationale of some aspects of the System register interface.

The interface to the System registers was originally defined as part of a generic coprocessor interface that gave access to 15 coprocessors, CP0 - CP15. Of these, CP8 - CP15 were reserved for use by Arm, while CP0 - CP7 were available for IMPLEMENTATION DEFINED coprocessors.

The coprocessors were accessed using coprocessor instructions. These instructions remain part of the T32 and A32 instruction sets, see System register access instructions.

In the Arm coprocessor model, a coprocessor included both:

- Primary and secondary coprocessor registers, which form part of the coprocessor interface.
- Anumber of internal registers.

When accessing a 32-bit internal coprocessor register, using an MCR or MRC instruction, the instruction specified:

- The target coprocessor, specified by the coproc parameter and taking a value between p0 for CP0 and p15 for CP15.

- The primary coprocessor register, specified by the CRn parameter and taking a value between c0 and c15 .
- The secondary coprocessor register, specified by the CRm parameter and taking a value between c0 and c15 .
- Up to two additional parameters, opc1 and opc2 , taking values between 0 and 7.

Other instructions in the group described in System register access instructions take a subset of these parameters:

- In the Armv7 definitions, LDC and STC instructions take parameters { coproc , CRd }, where CRd is the primary coprocessor register.
- MCRR and MRRC instructions take parameters { coproc , opc1 , CRm }, where CRm is the primary coprocessor register.

To maintain backward compatibility, the arguments to an MCR or MRC instruction remain { coproc , opc1 , CRn , CRm , opc2 }. Correspondingly, the encoding of the AArch64 System registers is described using the parameters { op0 , op1 , CRn , CRm , op2 }. However:

- The naming of these parameters no longer has any particular significance.
- While the coproc field is a 4-bit field, op0 is a 2-bit field.

Of the coprocessors reserved for use by Arm, in earlier versions of the architecture:

- CP15 provided access to the System registers relating to non-debug operation, and was originally called the System control coprocessor. From the introduction of Armv8, these registers are described as being in the coproc == 0b1111 encoding space.
- CP14 provided access to additional System registers, including those relating to debug and trace. From the introduction of Armv8, these registers are described as being in the coproc == 0b1110 encoding space.
- CP10 and CP11 were used for Advanced SIMD and floating-point control, and many coprocessor instruction encodings targeting CP10 and CP11 were used as floating-point instruction encodings:
- -Generally from the introduction of Armv8 the architecture does not relate these instructions to the coprocessor encoding space, but the naming of registers and register fields for Advanced SIMD and floating-point control reflects the historic coprocessor model.
- -Because the Advanced SIMD and floating-point functionality used both CP10 and CP11, some System register controls of this functionality have a pair of fields, for example NSACR.{cp10, cp11}. In these cases, both fields must be set to the same value. For more information, see Access controls for Advanced SIMD and floating-point functionality.

## From the introduction of Armv8:

- The AArch32 System registers include registers that were described as Special registers in Armv7 and earlier versions of the architecture. This means that the System registers include registers that are outside the earlier coprocessor model.
- The Armv7 AArch32 instruction encodings for LDC , STC , MCR , MRC , MCRR , and MRRC instructions with coproc field values other than { 1010 , 1011 , 1110 , 1111 } are available for reuse. Armv8.2 re-uses some encodings in this way.