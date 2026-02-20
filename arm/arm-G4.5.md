## G4.5 System register support for IMPLEMENTATION DEFINED memory features

The VMSAv8-32 defines the following registers for describing IMPLEMENTATION DEFINED features of the memory system:

- The TCM Type Register,TCMTR must be implemented on any implementation where EL1 or above supports AArch32. The format of this register is IMPLEMENTATION DEFINED.
- The System register encoding space with { coproc == 0b1111 , CRn == c9 , CRm == { c0 -c2 , c5 -c7 }} is IMPLEMENTATION DEFINED for all values of opc2 and opc1 . This space is reserved for branch predictor, cache and TCMfunctionality, for example maintenance, override behaviors and lockdown.
- In a VMSAv8-32 implementation, part of the System register encoding space with { coproc == 0b1111 , CRn == c10 } is IMPLEMENTATION DEFINED and reserved for TLB functionality, see TLB lockdown.
- The System register encoding space with { coproc == 0b1111 , CRn == c11 , CRm == { c0 -c8 , c15 }} is IMPLEMENTATION DEFINED for all values of opc2 and opc1 . This space is reserved for DMA operations to and from the TCMs.

In addition, the System register encoding space with { coproc == 0b1111 , CRn == c15 }is reserved for IMPLEMENTATION DEFINED registers, and can provide additional registers for the memory system. For more information, see Organization of registers in the ( coproc == 0b1111 ) encoding space.