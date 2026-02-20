## E1.4 About the AArch32 System register interface

AArch32 state provides a System register encoding space, which is indexed by the parameter set { coproc , opc1 , CRn , CRm , opc2 }, and a set of System register access instructions. This encoding space is used for:

- System registers.
- System instructions, for:
- -Cache and branch predictor maintenance.
- -Address translation.
- -TLB maintenance.

This encoding space uses only the coproc values 0b111x .

Note

The encoding space with coproc values 0b101x is redefined to provide Advanced SIMD and floating-point functionality.

The coproc encodings provide access to System register encoding space as follows:

- The ( coproc == 0b1111 ) encodings provide system control functionality, by providing access to System registers and System instructions. This includes architecture and feature identification, as well as control, status information and configuration support.

The following sections give a general description of these encodings:

- -About the System registers for VMSAv8-32.
- -Organization of registers in the ( coproc == 0b1111 ) encoding space.
- -Functional grouping of VMSAv8-32 System registers.

These encodings also provide:

- -The Performance Monitor registers. For more information, see The Performance Monitors Extension. The Activity Monitor registers. For more information, see The Activity Monitors Extension.
- The ( coproc == 0b1110 ) encodings provide access to additional registers, which support:
- -Debug, see AArch32 Self-hosted Debug.
- -The Jazelle identification registers, see Jazelle support.

UNPREDICTABLE, CONSTRAINED UNPREDICTABLE, and UNDEFINED behavior for AArch32 System register accesses gives information more information about permitted accesses to the System registers in AArch32 state.

Most functionality in the ( coproc == 0b111x ) encoding space cannot be accessed by software executing at EL0. This manual clearly identifies those functions that can be accessed at EL0.

For more information:

- About this encoding space, including the naming of the parameters that index the space, see The AArch32 System register interface.
- About the System interface access instructions, see System register access instructions.