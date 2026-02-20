## H3.8 Software Access debug event

When the value of EDSCR.TDA is 1, software access to the following AArch64 and AArch32 debug System registers generate a Software Access debug event:

- The Breakpoint Value Registers, DBGBVR.
- The Breakpoint Control Registers, DBGBCR.
- The Watchpoint Value Registers, DBGWVR.
- The Watchpoint Control Registers, DBGWCR.

However, EDSCR.TDA is ignored if any of the following applies:

- The value of OSLSR.OSLK == 1, meaning that the OS Lock is locked.
- Halting is prohibited. See Halting allowed and halting prohibited.
- The register access generates a higher priority synchronous exception or debug event.

If FEAT\_TRBE\_EXT or FEAT\_ETEv1p3 is implemented, then when all of the following apply, MRS and MSR accesses to ETE and TRBE System registers generate a Software Access debug event:

- EDSCR2.TTA is 1.
- The value of OSLSR\_EL1.OSLK == 0, meaning that the OS Lock is unlocked.
- Halting is allowed.
- The instruction does not generate any higher priority synchronous exception or debug event.

## Note

- The only accesses to the specified registers that generate a Software Access debug event are:
- -Accesses to System registers in AArch64 state.
- -Accesses to System registers in the ( coproc == 0b1110 ) encoding space in AArch32 state.
- Accesses by a PE using the external debug interface never generate a Software Access debug event.

## H3.8.1 Pseudocode description of Software Access debug event

The CheckSoftwareAccessToDebugRegisters() function is described in A-profile Architecture Pseudocode.