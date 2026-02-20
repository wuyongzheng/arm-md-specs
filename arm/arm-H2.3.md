## H2.3 Entering Debug state

On entry to Debug state, the preferred restart address and PSTATE are saved in DLR and DSPSR. The PE remains in the mode and Security state from which it entered Debug state.

If EDRCR.CBRRQ has a value of 0, entry to Debug state is precise. If EDRCR.CBRRQ has a value of 1, then imprecise entry to Debug state is permitted.

If a Watchpoint debug event causes an entry to Debug state, the PE records all of the following:

- When FEAT\_EDHSR is not implemented or the PE sets EDHSR.FnV to 0, the address of the access that generated the Watchpoint debug event is recorded in EDWAR.
- When FEAT\_EDHSR is implemented, information about the access that generated the Watchpoint debug event is recorded in EDHSR.

For more information, see:

- Exception syndrome information, fault address information, and preferred return address for a debug event taken from AArch64 state.
- Exception syndrome information, fault address information, and preferred return address for a debug event taken from AArch32 state.

Other than the effect on PSTATE and EDSCR, entry to Debug state is not a Context Synchronization event. The effects of entry to Debug state on PSTATE and EDSCR are synchronized.

## H2.3.1 Entering Debug state from AArch32 state

When entering Debug state from AArch32 state, the PE remains in AArch32 state. In AArch32 Debug state the PE executes T32 instructions, regardless of the value of PSTATE.T before entering Debug state.

To allow the debugger to determine the state of the PE, the current Execution state for all four Exception levels can be read from EDSCR.RW, and the current Exception level can be read from EDSCR.EL.

The current endianness state, PSTATE.E, is unchanged on entry to Debug state.

Note

- If EL1 is using AArch32 state, the current endianness state can differ from that indicated by SCTLR.EE.
- If EL2 is using AArch32 state, the current endianness state can differ from that indicated by HSCTLR.EE.
- On entry to Debug state from AArch32 state, PSTATE.SS is copied to DSPSR.SS, even though the PE remains in AArch32 state.

See also Effect of entering Debug state on PSTATE.

## H2.3.2 Effect of Debug state entry on DLR and DSPSR

DLRis set to the preferred restart address for the debug event, which depends on the event type. The value of PSTATE is saved in DSPSR.

For entry to Debug state from AArch32 state, the values saved in DSPSR.IT are always correct for the preferred restart address.

For synchronous Halting debug events, the preferred restart address is the address of the instruction that generated the debug event.

It is CONSTRAINED UNPREDICTABLE whether DSPSR\_EL0.BTYPE is set to the value of PSTATE.BTYPE or 0 for synchronous debug events other than the following debug events:

- AHalting Step debug event.
- ABreakpoint debug event.
- AHalt Instruction debug event.

For asynchronous Halting debug events, including pending Halting debug events taken asynchronously, the preferred restart address is the address of the first instruction that must be executed on exit from Debug state.

This means that:

- For Breakpoint and Watchpoint debug events, the preferred restart address is the same as the preferred return address for a debug exception, as described in AArch64 Self-hosted Debug and AArch32 Self-hosted Debug.
- For Halt Instruction debug events, DLR is set to the address of the HLT instruction and DSPSR.IT is correct for the HLT instruction.
- For Software Access debug events, DLR is set to the address of the accessing instruction and DSPSR.IT is correct for this instruction.
- For Halting Step debug events taken synchronously, DLR and DSPSR are set as the ELR and SPSR would be set for a Software Step exception. This is usually the address of, and PSTATE for, the instruction after the one that was stepped.
- For Exception Catch debug events, DLR is set to the address of the first instruction that must be executed on exit from Debug state, and DSPSR is correct for this instruction. This is the exception vector or reset vector address.
- -If the debug event is generated on an exception return to a trapped Exception level, the DLR is set to the target address of the exception return and the DSPSR records the value of PSTATE after the exception return.
- Reset Catch debug events taken synchronously behave like Exception Catch debug events.
- For Reset Catch debug events and Exception Catch debug events generated on reset to a trapped Exception level, the DLR is set to is set to the reset address and the DSPSR records the reset value of PSTATE.
- For pending Halting debug events and External Debug Request debug events, DLR is set to the address of the first instruction that must be executed on exit from Debug state and DSPSR.IT is correct for this instruction. See Pending Halting debug events.

- If the debug event is generated on taking an exception to a trapped Exception level, the DLR is set to the address of the exception vector the PE would have started fetching from. This is UNKNOWN if the VBAR for the Exception level has never been initialized. The DSPSR records the value of PSTATE after taking the exception. The Exception Catch occurs after the SPSR and the Link register are set, and the debugger can use these registers to determine where in the application program the exception occurred.

Note

Depending on the target Exception level and Execution state for the exception, the Link register is one of ELR\_EL1, ELR\_EL2, ELR\_EL3, ELR\_hyp, or LR (R14).

Normally DLR is aligned according to the instruction set state indicated in DSPSR. However, a debug event might be taken at a point where the PC is not aligned.

## H2.3.3 Effect of Debug state entry on System registers, the Event register, and Exclusives monitors

Entering Debug state has no effect on System registers other than DLR and DSPSR. In particular, ESRs, FARs, and FSRs are not updated on entering Debug state. SCR is unchanged, even when entering Debug state from EL3 when EL3 is using AArch32.

Entering Debug state has no architecturally-defined effect on the Event Register and Exclusives monitors.

Note

Entry to Debug state might set the Event Register or clear the Exclusives monitors, or both. However, this is not a requirement, and debuggers must not rely on any IMPLEMENTATION SPECIFIC behavior.

Unless otherwise described in this reference manual, instructions executed in Debug state have their architecturally-defined effects on the System registers, the Event register, and Exclusives monitors.

## H2.3.4 Effect of entering Debug state on PSTATE

The effect of an entry to Debug state on PSTATE is described in Entering Debug state and Entering Debug state from AArch32 state.

On entry to Debug state after PSTATE is saved in DSPSR:

- PSTATE.{IL, PACM} is cleared to 0.
- PSTATE.UINJ is cleared to 0.
- PSTATE.TCO is set to 1.
- PSTATE.BTYPE is set to 0b00 .
- PSTATE.{IT, T, SS, D, A, I, F, SSBS, ALLINT, PM, PPEND} are set to UNKNOWN values

PSTATE.{N, Z, C, V, nRW, EL, SP, PAN, UAO, DIT, EXLOCK, DIT} are unchanged.

If FEAT\_AA32EL0 is implemented, then PSTATE.{Q, GE, E, M} are unchanged.

For more information, see PSTATE in Debug state.

## H2.3.5 Entering Debug state during loads and stores

The PE can enter Debug state during instructions that perform a sequence of memory accesses, as opposed to a single single-copy atomic access, because of a Watchpoint debug event. The effect of entering Debug state on such an instruction is the same as taking a Data Abort exception during such an instruction.

In addition, when executing in AArch64 state, the PE can enter Debug state because of an External Debug Request debug event during instructions that perform a sequence of memory accesses. The effect of entering Debug state on such an instruction is the same as taking an interrupt exception during such an instruction.

This applies to all memory types.

## H2.3.6 Entering Debug state and Software Step

When Software Step is active, a debug event that causes entry to Debug state behaves like an exception taken to an Exception level above the debug target Exception level. That is:

- If the instruction that is stepped generates a synchronous debug event that causes entry to Debug state, or an asynchronous debug event is taken before the step completes, the PE enters Debug state with DSPSR.SS set to 1.
- Apending Halting debug event or an asynchronous debug event can be taken after the step has completed. In this case the PE enters Debug state with DSPSR.SS set to 0.

## In addition:

- If the instruction that is stepped generates an exception trapped by an Exception Catch debug event, the PE enters Debug state at the exception vector with DSPSR.SS set to 0. This is because PSTATE.SS is set to 0 by taking the exception.
- If the PE is reset, PSTATE.SS is reset to 0. If the following debug events are enabled, and halting is allowed, the PE enters Debug state with DSPSR.SS set to 0:
- -Reset Catch debug event at the reset Exception level.
- -Exception Catch debug event at the reset Exception level.
- -Halting Step debug event.
- If Halting Step is also active, then Halting Step and Software Step operate in parallel and can both become active-pending. In this case Halting step has a higher priority than Software step. This means that the PE enters Debug state and DSPSR.SS is set to 0.

## H2.3.7 Pseudocode description of entering Debug state

The DebugHalt constants are described in shared/debug/halting/DebugHalt in the pseudocode. The UpdateEDSCRFields() and Halt() functions are described in A-profile Architecture Pseudocode.