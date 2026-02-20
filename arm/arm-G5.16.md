## G5.16 Functional grouping of VMSAv8-32 System registers

This section describes how the System registers in an VMSAv8-32 implementation divide into functional groups. The functional groups of AArch32 registers are:

- Special-purpose registers.
- VMSA-specific registers.
- ID registers.
- Performance monitors registers.
- Activity monitors registers.
- Debug registers.
- RAS registers.
- Generic timer registers.
- Cache maintenance System instructions.
- Address translation System instructions.
- TLB maintenance System instructions.
- Base system registers.
- Legacy feature registers and System instructions.

For a list of these functional groups and the registers in each group, see Functional index of AArch32 registers and System instructions.

AArch32 System Register Descriptions describes each of these registers.

Note

- The functional groups defined in this section mainly consist of the VMSAv8-32 System registers, but include some additional System registers.
- Some registers belong to more than one functional group.

For other related information, see:

- The AArch32 System register interface for general information about the access to the AArch32 System registers, including the main register access instructions MRC and MCR .
- About the System registers for VMSAv8-32.
- Organization of registers in the ( coproc == 0b1110 ) encoding space.
- Organization of registers in the ( coproc == 0b1111 ) encoding space.
- About the AArch32 System registers.

The register descriptions in AArch32 System Register Descriptions, assume you are familiar with these functional groups, and use conventions and other information from them without any explanation.

## Chapter G6 The Generic Timer in AArch32 state

This chapter describes the implementation of the Arm Generic Timer as an extension to an Armv8 AArch32 implementation. It includes an overview of the AArch32 System register interface to an Arm Generic Timer.

It contains the following sections:

- About the Generic Timer in AArch32 state.
- The AArch32 view of the Generic Timer.

The Generic Timer in AArch64 state describes the AArch64 view of the Generic Timer, including additional timers that can be implemented in AArch64 state, and System Level Implementation of the Generic Timer describes the system level implementation of the Generic Timer.