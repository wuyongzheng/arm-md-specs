## D23.1 The System register encoding space

The A64 instruction set includes instructions that access the System register encoding space. These instructions provide:

- Access to System registers , including the debug registers, that provide system control, and system status information.
- Access to Special-purpose registers such as SPSR\_ELx, ELR\_ELx, and the equivalent fields of the Process State.
- The cache and TLB maintenance instructions and address translation instructions.
- Barriers and the CLREX instruction.
- Architectural hint instructions.

This section describes the parts of the System register encoding space that provides access to the System registers described in AArch64 System Register Descriptions.

Note

- See Fixed values in AArch64 instruction and System register descriptions for information about abbreviations used in the System instruction descriptions.
- In AArch32 state, much of this functionality is provided through the System register interface described in The AArch32 System register interface. In AArch64 state, the parameters used to characterize the System register encoding space are { op0 , op1 , CRn , CRm , op2 }. These are based on the parameters that characterize the AArch32 System register encoding space, which reflect the original implementation of these registers, as described in Background to the System register interface. There is no particular significance to the naming of these parameters, and no functional distinction between the opn parameters and the CRx parameters.

Principles of the System instruction class encoding describes some general properties of these encodings. System instruction class encoding overview then describes the top-level encoding of these instructions, identifying that:

- Entries in the encoding space are characterized by the parameter set { op0 , op1 , CRn , CRm , op2 }.
- op0 is the most significant parameter for determining allocations in this space.

Much of this encoding space is used for System instructions, as described in The A64 System Instruction Class. This chapter describes only the part of the encoding space that is used for System registers, in the following sections:

- Moves to and from debug and trace System registers.
- Moves to and from non-debug System registers, Special-purpose registers.