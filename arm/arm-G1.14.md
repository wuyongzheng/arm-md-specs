## G1.14 Routing of aborts taken to AArch32 state

Amemory abort is either a Data Abort exception or a Prefetch Abort exception. When executing in AArch32 state, depending on the cause of the abort, and possibly on configuration settings, an abort is taken either:

- To the Exception level of the PE mode from which the abort is taken. In this case the abort is taken to AArch32 state.

- To a higher Exception level. In this case the Exception level to which the abort is taken is either:

- Using AArch32. In this case, this chapter describes how the abort is handled.

- Using AArch64. In this case, The AArch64 Virtual Memory System Architecture describes how the abort is handled.

For an abort taken to an Exception level that is using AArch32, the mode to which a memory abort is taken depends on the reason for the exception, the mode the PE is in when it takes the exception, and configuration settings, as follows:

## Memory aborts taken to Monitor mode

If an implementation includes EL3, when the value of SCR.EA is 1, all External aborts are taken to EL3, and if EL3 is using AArch32 they are taken to Monitor mode. This applies to aborts taken from Secure modes and from Non-secure modes.

## Memory aborts taken to Secure Abort mode

If an implementation includes EL3, when the PE is executing in Secure state, all memory aborts that are not routed to Monitor mode are taken to Secure Abort mode.

Note

The only memory aborts that can be routed to Monitor mode are External aborts.

## Memory aborts taken to Hyp mode

If an implementation includes EL2, when the PE is executing in Non-secure state, the following aborts are taken to EL2. If EL2 is using AArch32 this means they are taken to Hyp mode:

- Alignment faults taken:

- When the PE is in Hyp mode.

- When the PE is in a Non-secure PL1 or EL0 mode and the exception is generated because the Non-secure PL1&amp;0 stage 2 translation identifies the target of an unaligned access as any type of Device memory.

- When the PE is in Non-secure User mode and HCR.TGE is set to 1. For more information, see Abort exceptions, when the value of HCR.TGE is 1.

- When the PE is using the Non-secure PL1&amp;0 translation regime:

- MMUfaults from stage 2 translations, for which the stage 1 translation did not cause an MMUfault.

- Any abort taken during the stage 2 translation of an address accessed in a stage 1 translation table walk that is not routed to Secure Monitor mode, see Stage 2 fault on a stage 1 translation table walk.

- When the PE is using the Non-secure EL2 translation regime, MMU faults from stage 1 translations.

Note

The Non-secure EL2 translation regime has only one stage of translation.

- External aborts, if SCR.EA is set to 0 and any of the following applies:

- The PE was executing in Hyp mode when it took the exception.

- The PE was executing in a Non-secure PL1 or EL0 mode when it took the exception, the abort is asynchronous, and HCR.AMO is set to 1. For more information, see Asynchronous exception routing controls.

- The PE was executing in the Non-secure User mode when it took the exception, the abort is synchronous, and HCR.TGE is set to 1. For more information, see Abort exceptions, when the value of HCR.TGE is 1.

- -FEAT\_RAS is implemented, the PE was executing in a Non-secure PL1 or EL0 mode when it took the exception, the abort is synchronous, and the value of HCR2.TEA is 1.
- -The abort occurred on a stage 2 translation table walk.
- Debug exceptions, if HDCR.TDE is set to 1. For more information, see Routing debug exceptions to EL2 using AArch32.

## Memory aborts taken to Non-secure Abort mode

In an implementation that does not include EL3, all memory aborts that are taken to an Exception level that is using AArch32 are taken to Abort mode.

Otherwise, when the PE is executing in Non-secure state, the following aborts are taken to Non-secure Abort mode:

- When the PE is in a Non-secure PL1 or EL0 mode, Alignment faults taken for any of the following reasons:
- -SCTLR.A is set to 1.
- -An instruction that does not support unaligned accesses is committed for execution, and the instruction accesses an unaligned address.
- -The PL1&amp;0 stage 1 translation identifies the target of an unaligned access as any type of Device memory.

Note

In an implementation that does not include EL2, this case results in a CONSTRAINED UNPREDICTABLE memory access, see Cases where unaligned accesses are CONSTRAINED UNPREDICTABLE and Loads and Stores to unaligned locations.

If an implementation includes EL2 and the PE is in Non-secure User mode, these exceptions are taken to Abort mode only if the value of HCR.TGE is 0.

- When the PE is using the Non-secure PL1&amp;0 translation regime, an MMU fault from a stage 1 translation.
- External aborts, if the PE was executing in a Non-secure PL1 or EL0 mode when it took the exception and both:
- -The value of SCR.EA is 0, meaning the abort is not taken to EL3.
- -The abort is not taken to EL2 for one of the reasons defined in Memory aborts taken to Hyp mode.
- Virtual Aborts, see Virtual exceptions when an implementation includes EL2.
- When the value of HDCR.TDE is 0, Debug exceptions. For more information, see Routing debug exceptions to EL2 using AArch32.

Note

If EL0 is using AArch32 and EL1 is using AArch64, then any of these memory aborts taken from User mode are taken to EL1, as described in The AArch64 Virtual Memory System Architecture.

## Memory aborts with IMPLEMENTATION DEFINED behavior

In addition, a PE can generate an abort for an IMPLEMENTATION DEFINED reason associated with lockdown. In an implementation that includes EL2, whether such an abort is taken to Non-secure Abort mode or is taken to EL2 is IMPLEMENTATION DEFINED, and an implementation might include a mechanism to select whether the abort is routed to Non-secure Abort mode or to EL2.

When the PE is in a Non-secure mode other than Hyp mode, if multiple factors cause an Alignment fault, the abort is taken to Non-secure Abort mode if any of the factors require the abort to be taken to Abort mode. For example, if the SCTLR.A bit is set to 1, and the access is an unaligned access to an address that the stage 2 translation tables mark as Device-nGnRnE, then the abort is taken to Non-secure Abort mode.

For more information, see Handling exceptions that are taken to an Exception level using AArch32.