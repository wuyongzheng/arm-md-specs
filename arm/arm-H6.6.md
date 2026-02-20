## H6.6 Debug OS Save and Restore sequences

From the introduction of Armv8-A, the following registers provide the OS Save and Restore mechanism:

- The OS Lock Access Register , OSLSR, locks the OS Lock to restrict access to debug registers before starting an OS Save sequence, and unlocks the OS Lock after an OS Restore sequence.
- The OS Lock Status Register , OSLSR, shows the status of the OS Lock.
- The PE can be configured to generate an OS Unlock Catch debug event when the OS Lock is unlocked.
- If FEAT\_DoubleLock is implemented, the OS Double Lock locks out an external debug interface entirely. This is only used immediately before a powerdown sequence.

## See also:

- FEAT\_DoubleLock
- Reset and debug
- Example OS Save and Restore sequences

## H6.6.1 EDPRSR.{DLK, SPD, PU} and the Core power domain

If FEAT\_DoPD is not implemented, a debugger uses EDPRSR.{DLK, SPD, PU} to determine whether registers in the Core power domain can be accessed, and whether their state has been lost since the last time the register was read.

Table H6-1 Interpretation of the EDPRSR.{DLK, SPD, PU} bits

| EDPRSR   | EDPRSR   |    | Core power domain   | Core power domain   |            | Notes                                                                                                                   |
|----------|----------|----|---------------------|---------------------|------------|-------------------------------------------------------------------------------------------------------------------------|
| DLK      | SPD      | PU | Power               | Accesses            | State lost | Notes                                                                                                                   |
| 0        | 0        | 1  | On                  | OK                  | No         | -                                                                                                                       |
| 0        | 1        | 1  | On                  | OK                  | Yes        | SPD is cleared to 0 following the read.                                                                                 |
| 1        | X        | 1  | On                  | Error               | Not known  | FEAT_DoubleLock is implemented and DoubleLockStatus() == TRUE. Software locks the OS Double Lock before removing power. |
| X        | 1        | 0  | Off                 | Error               | Yes        | ACold reset will be asserted on exiting powerdown state, but not on exiting low-power retention state.                  |
| X        | 0        | 0  | Not known           | Error               | Not known  | ACold reset will be asserted on exiting powerdown state, but not on exiting low-power retention state.                  |

If FEAT\_DoPD is implemented, accesses to EDPRSR return an error when the Core power domain is off or in a retention state, meaning successful reads of EDPRSR always return 1 for EDPRSR.PU.

When FEAT\_Debugv8p4 is implemented, and whenever FEAT\_DoubleLock is not implemented, EDPRSR.DLK is always 0.

If FEAT\_DoubleLock is not implemented, DoubleLockStatus() always returns FALSE.

If the Core power domain is powered up and DoubleLockStatus() == TRUE, then:

- When FEAT\_Debugv8p2 is not implemented, EDPRSR.{DLK, SPD, PU} can read either {1, UNKNOWN, 1} or {UNKNOWN,0, 0}.
- When FEAT\_Debugv8p2 is implemented, and FEAT\_Debugv8p4 is not implemented, EDPRSR.{DLK, SPD, PU} can only read {UNKNOWN, 0, 0}.

## H6.6.2 EDPRSR.SPD when the Core domain is in either retention or powerdown state

If FEAT\_DoPD is not implemented, when the Core power domain is in either the retention or powerdown state, EDPRSR.SPD is not cleared following a read of EDPRSR and it is IMPLEMENTATION DEFINED whether:

- EDPRSR.SPD shows whether the state of the debug registers in the Core power domain has been lost since the last time that EDPRSR was read. This means that:
- -When the Core power domain is in the powerdown state, EDPRSR.SPD is RAO, this indicates that the state of the debug registers has been lost.
- -When the Core power domain is in the retention state, EDPRSR.SPD indicates whether the state of the debug registers was lost before the Core power domain entered retention state.
- EDPRSR.SPD is RAZ, and:
- -On leaving the powerdown state, EDPRSR.SPD is set to 1 which indicates that the state of the debug registers has been lost.
- -On leaving the retention state, EDPRSR.SPD reverts the value it had on entering the retention state.

Note

If FEAT\_DoPD is implemented, accesses to EDPRSR return an error when the Core power domain is off or in a retention state.

## H6.6.3 EDPRSR.{DLK, R} and reset state

If FEAT\_DoPD is implemented, accesses to EDPRSR return an error when the Core power domain is off or in a retention state, meaning successful reads of EDPRSR always return 1 for EDPRSR.PU.

When FEAT\_Debugv8p4 is implemented, and whenever FEAT\_DoubleLock is not implemented, EDPRSR.DLK is always 0.

If FEAT\_DoubleLock is not implemented, DoubleLockStatus() always returns FALSE.

If FEAT\_DoubleLock is implemented and enabled, the behavior of all registers and fields except EDPRSR.DLK is the same as their behavior if FEAT\_Debugv8p4 is not implemented.

If FEAT\_Debugv8p4 is implemented EDPRSR.DLK is always 0 and does not give any information about the OS Double Lock.

EDPRSR.R is UNKNOWN when DoubleLockStatus() == TRUE. OSDLR\_EL1.DLK is cleared to 0 by a reset. If the Core power domain is powered up and entered reset state with the OS Double Lock locked, it is CONSTRAINED UNPREDICTABLE whether a read of EDPRSR while the PE is in reset state returns:

- EDPRSR.{DLK, R, PU} == {1, UNKNOWN, 1} indicating that the OS Double Lock is locked. This is not permitted from Armv8.2.
- EDPRSR.{DLK, R, PU} == {0, 1, 1} indicating that the PE is in reset state.
- EDPRSR.{DLK, R, PU} == {UNKNOWN, UNKNOWN, 0} indicating that the registers in the Core power domain cannot be accessed because the OS Double Lock is locked.

If the PE was powered up and the OS Double Lock was unlocked when the PE was reset, then EDPRSR.{DLK, R, PU} reads as {0, 1, 1} while the PE is in reset state.

On leaving reset state, EDPRSR.{DLK, R} reads as {0, 0}.

## H6.6.4 Debug registers to save over powerdown

Table H6-2 shows the different requirements for self-hosted debug over powerdown and external debug over powerdown:

- The column labeled Self-hosted lists registers that software must preserve over powerdown so that it can support self-hosted debug over powerdown. This does not require use of the OS Save and Restore mechanism.
- The column labeled External lists registers that software must preserve over powerdown so that it can support external debug over powerdown. This requires use of the OS Save and Restore mechanism:

- -Some external debug registers are not normally accessible to software executing on the PE. Additional debug registers are provided that give software the required access to save and restore these external debug registers when OSLSR.OSLK is locked. These registers include OSECCR, OSDTRRX, and OSDTRTX.
- Some registers might only present in some implementations, or might not be accessible at all Exception levels or in Non-secure state. DBGVCR32\_EL2 and SDER32\_EL3 are only required to support AArch32.

Table H6-2 does not include registers for the OPTIONAL Trace and Performance Monitor extensions.

Table H6-2 Debug registers to save over powerdown

| Register in AArch64 state       | Register in AArch32 state   | Self-hosted   | External   |
|---------------------------------|-----------------------------|---------------|------------|
| MDSCR_EL1                       | DBGDSCRext                  | Yes           | Yes        |
| DBGBVR<n>_EL1                   | DBGBVR<n>                   | Yes           | Yes        |
| DBGBCR<n>_EL1                   | DBGBCR<n>                   | Yes           | Yes        |
| DBGWVR<n>_EL1                   | DBGWVR<n>                   | Yes           | Yes        |
| DBGWCR<n>_EL1                   | DBGWCR<n>                   | Yes           | Yes        |
| DBGVCR32_EL2                    | DBGVCR                      | Yes           | -          |
| MDCR_EL2                        | HDCR                        | Yes           | -          |
| SDER32_EL3                      | SDER                        | Yes           | -          |
| MDCR_EL3                        | SDCR                        | Yes           | -          |
| MDCCINT_EL1                     | DBGDCCINT                   | -             | Yes        |
| DBGCLAIMSET_EL1 DBGCLAIMCLR_EL1 | DBGCLAIMSET, DBGCLAIMCLR    | -             | Yes        |
| OSECCR_EL1                      | DBGOSECCR                   | -             | Yes        |
| OSDTRRX_EL1 OSDTRTX_EL1         | DBGDTRRXext DBGDTRTXext     | -             | Yes        |

## H6.6.5 OS Save sequence

To preserve the debug logic state over a powerdown, the state must be saved to nonvolatile storage. This means the OS Save sequence must:

1. Lock the OS Lock by:
- Writing the key value 0xC5ACCE55 to the DBGOSLAR in AArch32 state.
- Writing 1 to OSLAR\_EL1.OSLK in AArch64 state.
2. Execute an ISB instruction.
3. Walk through the debug registers listed in Debug registers to save over powerdown and save the values to the nonvolatile storage.

If the FEAT\_DoubleLock is implemented, before removing power from the Core power domain, software must:

1. Lock the OS Double Lock by:
- Writing 1 to DBGOSDLR.DLK in AArch32 state.
- Writing 1 to OSDLR\_EL1.DLK in AArch64 state.

If FEAT\_DoubleLock is not implemented, OSDLR\_EL1 and DBGOSDLR ignore writes.

2. Execute a Context Synchronization event.

## H6.6.6 OS Restore sequence

After a powerdown, the OS Restore sequence must perform the following steps to restore the debug logic state from the non-volatile storage:

1. Lock the OS Lock, as described in OS Save sequence. The OS Lock is generally locked by the Cold reset, but this step ensures that it is locked.
2. Execute an ISB instruction.
3. To ensure that, if an external debugger clears the OS Lock before the end of this sequence, no debug exceptions are generated:
- Write 0 to MDSCR\_EL1 if executing in AArch64 state.
- Write 0 to DBGDSCRext if executing in AArch32 state.
4. Walk through the debug registers listed in Debug registers to save over powerdown, and restore the values from the nonvolatile storage. The last register to be restored must be:
- MDSCR\_EL1 if executing in AArch64 state.
- DBGDSCRext if executing in AArch32 state.
5. Execute an ISB instruction.
6. Unlock the OS Lock by:
- Writing 0 to OSLAR\_EL1.OSLK if executing in AArch64 state.
- Writing any non-key value to DBGOSLAR if executing in AArch32 state.
7. Execute a Context Synchronization event.

Note

The OS Restore sequence overwrites the debug registers with the values that were saved. If there are valid values in these registers immediately before the restore sequence, then those values are lost.

## H6.6.7 Debug behavior when the OS Lock is locked

The main purpose of the OS Lock is to prevent updates to debug registers during an OS Save or OS Restore operation. The OS Lock is locked on a Cold reset.

When the OS Lock is locked:

- Access to debug registers through the System register interface is mainly unchanged except that:
- -Certain registers are read and written without side-effects.
- -Fields in DSCR and OSECCR that are normally read-only become read/write.

This allows the state to be saved or restored. For more information, see the relevant register description in External Debug Register Descriptions.

- Access to debug registers by the external debug interface is restricted to prevent an external debugger modifying the registers that are being saved or restored. For more information, see External debug interface register access permissions summary.
- Debug exceptions, other than Breakpoint Instruction exceptions are not generated.
- Breakpoint and Watchpoint debug events are not generated. The OS Lock has no effect on Breakpoint Instruction exceptions and other debug events.

## H6.6.8 Debug behavior when the OS Lock is unlocked

When the OS Lock is unlocked, the PE sets EDESR.OSUC to 1 if the OS Unlock Catch debug event is enabled and the PE is in Non-debug state, meaning the OS Unlock Catch debug event becomes pending. See OS Unlock Catch debug event.

## H6.6.9 Debug behavior when the OS Double Lock is locked

If the FEAT\_DoubleLock is implemented, software locks the OS Double Lock immediately before a powerdown sequence.

The OS Double Lock ensures that it is safe to remove core power by forcing the debug interfaces to be quiescent.

When DoubleLockStatus() == TRUE:

- The external debug interface has only restricted access to the debug registers, so that it is quiescent before removing power. See External debug interface register access permissions summary.
- Debug exceptions, other than Breakpoint Instruction exceptions, are not generated.
- Halting is prohibited. See Halting allowed and halting prohibited.

Note

Pending Halting debug events might be lost when core power is removed.

- No asynchronous debug events are WF* wakeup events.

If the FEAT\_DoubleLock is not implemented, the PE ensures these conditions are met before allowing power to be removed.

Software must synchronize the update to OSDLR before it indicates to the system that core power can be removed. The interface between the PE and its power controller is IMPLEMENTATION DEFINED.

Typically software indicates that core power can be removed by entering the Wait For Interrupt state. This means that software must explicitly synchronize the OSDLR update before issuing the WFI instruction.

OSDLR.DLK is ignored and DoubleLockStatus() == FALSE if either:

- The PE is in Debug state.
- DBGPRCR.CORENPDRQ is set to 1.

Note

It is possible to enter Debug state with OSDLR.DLK set to 1. This is because a Context Synchronization event is required to ensure the OS Double Lock is locked, meaning that Debug state might be entered before the OSDLR update is synchronized.

Because OSDLR.DLK is ignored when DBGPRCR.CORENPDRQ is set to 1, an external debugger can write to DBGPRCR.CORENPDRQ, and the FEAT\_DoubleLock is not always implemented, software must not rely on using the OS Double Lock to disable debug exceptions or to prohibit halting, or both. Arm deprecates use of the OS Double Lock for these purposes, and instead recommends that software:

- Uses the OS Lock to disable debug exceptions during save or restore sequences.
- Uses the debug authentication interface to prohibit halting and external debug access to debug registers at times other than immediately prior to removing power.

As the purpose of the OS Double Lock is to ensure that it is safe to remove core power, if the FEAT\_DoubleLock is implemented, it is important to avoid race conditions that defeat this purpose. Arm recommends that:

- Once the write to OSDLR.DLK has been synchronized by a Context Synchronization event and DoubleLockStatus() == TRUE, a PE must:

- Not allow a debug event generated before the Context Synchronization event to cause an entry to Debug state or act as a wakeup event for a WFI or WFE instruction after the Context Synchronization event has completed.

Note

When FEAT\_WFxT is implemented, this also applies to the WFET and WFIT instructions.

- Complete any external debug access started before the Context Synchronization event by the time the Context Synchronization event completes.

Note

A debug register access might be in progress when software sets OSDLR.DLK to 1. An implementation must not permit the synchronization of locking the OS Double Lock to stall indefinitely while waiting for that access to complete. This means that any debug register access that is in progress when software sets OSDLR.DLK to 1 must complete or return an error in finite time.

- If a write to DBGPRCR or EDPRCR made when OSDLR.DLK == 1 changes DBGPRCR.CORENPDRQ or EDPRCR.CORENPDRQ from 1 to 0, meaning DoubleLockStatus() changes from FALSE to TRUE, then before signaling to the system that the CORENPDRQ field has been cleared and emulation of powerdown is no longer requested, meaning the system can remove core power, the PE must ensure that all the requirements for DoubleLockStatus() == TRUE listed in this section are met.

In a standard OS Save sequence, the OS Lock is locked before the OS Double Lock is locked. This means that writes to CORENPDRQare ignored by the time the OS Double Lock is locked. However, if DoubleLockStatus() == FALSE, an external debugger can clear the OS Lock at any time, and then write to EDPRCR.