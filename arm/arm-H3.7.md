## H3.7 Reset Catch debug events

AReset Catch debug event is generated when enabled, and the PE exits reset state. When the Reset Catch debug event is generated, it is recorded by setting EDESR.RC to 1. When FEAT\_DoPD is implemented, CTIDEVCTL.RCE enables a Reset Catch debug event, otherwise EDECR.RCE enables a Reset Catch debug event.

If halting is allowed when the event is generated, the Reset Catch debug event is taken immediately and synchronously. On entering Debug state, DLR has the address of the reset vector. The PE must not fetch any instructions from memory.

Otherwise, the Reset Catch debug event is pended and taken when halting is allowed. See Synchronization and Halting debug events for more information.

This means that EDESR.RC is set to the value of EDECR.RCE or CTIDEVCTL.RCE on a Warm reset. EDESR.RC is cleared to 0 on exiting Debug state.

## H3.7.1 Pseudocode description of Reset Catch debug event

The CheckResetCatch() function is called after reset before executing any instruction.

The CheckPendingResetCatch() function is called before an instruction is executed. If a Reset Catch is pending, it generates the Reset Catch debug event.