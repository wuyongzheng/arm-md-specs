## H8.3 Synchronization of changes to the external debug registers

This section describes the synchronization requirements for the external debug interface.

For more information on how these requirements affect debug, see:

- Synchronization and debug exceptions for exceptions taken from AArch64 state.
- Synchronization and debug exceptions for exceptions taken from AArch32 state.
- Synchronization and Halting debug events.
- Synchronization of DCC and ITR accesses.

This section refers to accesses from the external debug interface as external reads and external writes. It refers to accesses to System registers as direct reads, direct writes, indirect reads, and indirect writes.

Note

Synchronization requirements for AArch64 System registers and Synchronization of changes to AArch32 System registers define direct read, direct write, indirect read, and indirect write, and classifies external reads as indirect reads, and external writes as indirect writes.

For general information about synchronization, access completion, ordering, and observability, see Synchronization of memory-mapped registers.

Writes to the same register are serialized, meaning they are observed in the same order by all observers, although some observers might not observe all of the writes. With the exception of DBGBCR&lt;n&gt;\_EL1, DBGBVR&lt;n&gt;\_EL1, DBGWCR&lt;n&gt;\_EL1, and DBGWVR&lt;n&gt;\_EL1, external writes to different registers are not necessarily observed in the same order by all observers as the order in which they complete.

Synchronization of DCC and ITR accesses describes the synchronization requirements for the DCC and ITR.

Changes to the IMPLEMENTATION DEFINED authentication interface are external writes to the authentication status registers by the Requester of the authentication interface. See Synchronization and the authentication interface.

The external agent must be able to guarantee completion of a write. For example by:

- Marking the memory as Device-nGnRnE and executing a DSB barrier, if the system supports this property.
- Reading back the value written.
- Some guaranteed property of the connection between the PE and the external agent.

Note

For an external Debug Access Port, access completion is an IMPLEMENTATION DEFINED property. For a CoreSight system using APB-AP to access a debug APB, accesses complete in order.

However, the external agent cannot force synchronization of completed writes without halting the PE. Executing an ISB instruction, either in Debug state or in Non-debug state, and exiting from Debug state forces synchronization. If the PE is in Debug state, executing an ISB instruction is guaranteed to explicitly synchronize any external reads, external writes, and changes to the authentication interface that are ordered before the external write to EDITR.

For any given observer, external writes to the following register groups are guaranteed to be observable in the same order in which they complete:

- The breakpoint registers, DBGBCR&lt;n&gt;\_EL1 and DBGBVR&lt;n&gt;\_EL1.
- The watchpoint registers, DBGWCR&lt;n&gt;\_EL1 and DBGWVR&lt;n&gt;\_EL1.

This guarantee applies only to external writes to registers within one of these groups. There is no guarantee regarding the ordering of the observability of external writes within these groups with respect to external writes to registers, for example EDSCR, or between breakpoints and watchpoints, including watchpoints linked to context matching breakpoints.

Note

This means that a debugger can rely on the external writes to be observed in the same order in which they complete. It does not mean that a debugger can rely on the external writes being observed in finite time.

In a simple sequential execution an indirect write that occurs as a side-effect of an access happens atomically with the access, meaning no other accesses are allowed between the register access and its side-effect.

If two or more interfaces simultaneously access a register, the behavior must be as if the accesses occurred atomically and in any order. This is described in Examples of the synchronization of changes to the external debug registers.

Note

Where simultaneous writes occur, once an order has been established by the implementation, some registers have behavior that is incompatible with the implementation simply dropping the older write and only performing the actions of the younger write. In these cases, the implementation must ensure that the register update is consistent with both writes having occurred. For example, writing one to write-one-to-clear or write-one-to-set fields in the older write can produce effects that persist even after writing zero to the same field in the younger write. Examples of registers with this behavior include DBGCLAIMSET\_EL1, DBGCLAIMCLR\_EL1, PMCR\_EL0, PMOVSSET\_EL0, PMOVSCLR\_EL0, PMCNTENSET\_EL0, PMCNTENCLR\_EL0, PMINTENSET\_EL1, PMINTENCLR\_EL1, PMSWINC\_EL0, and PMZR\_EL0, all of which are simultaneously accessible via external debug and System register access.

## H8.3.1 Synchronization and the authentication interface

Changes to the authentication interface are indirect writes to the state of the PE by the Requester of the authentication interface.

For an external debug interface read of any Authentication Status register, or an indirect read of the authentication interface made in determining the response to a subsequent external debug interface access, a change on the authentication interface must be observable following a subsequent explicit Context Synchronization event, and:

- It is IMPLEMENTATION DEFINED whether a change is guaranteed to be observable in finite time.
- It is IMPLEMENTATION DEFINED whether a change is guaranteed to be observable following an entry to Debug state.

For a System register read of DBGAUTHSTATUS\_EL1, a change on the authentication interface is guaranteed to be observable only after a Context Synchronization event.

Note

- In some systems, the authentication interface is fixed by configuration or is changed under the control of software. These systems can require explicit synchronization for any change to the authentication interface.
- In other systems, the authentication interface is controlled dynamically by an external agent. In these systems, it is desirable that changes to the authentication interface do not require explicit synchronization by software executing on the PE to be observable by subsequent external debug interface accesses, and are either observable in finite time or are synchronized by entry to Debug state. Otherwise, there are scenarios where a debugger is not able to halt and debug the system.

## H8.3.2 Examples of the synchronization of changes to the external debug registers

Example H8-1, Example H8-2, and Example H8-3 show the synchronization of changes to the external debug registers.

Example H8-1 Order of synchronization of Breakpoint and Watchpoint register writes

Initially DBGBVR&lt;n&gt;\_EL1 is 0x8000 and DBGBCR&lt;n&gt;\_EL1 is 0x0181 . This means that a breakpoint is enabled on the halfword T32 instruction at address 0x8000 .

Asequence of external writes occurs in the following order:

1. 0x0000 is written to DBGBCR&lt;n&gt;\_EL1, disabling the breakpoint.
2. 0x9000 is written to DBGBVR&lt;n&gt;\_EL1[31:0].
3. 0x0061 is written to DBGBCR&lt;n&gt;\_EL1, enabling a breakpoint on the halfword at address 0x9002 .

The external writes must be observable to indirect reads in the same order as the external writes complete. This means that at no point is there a breakpoint enabled on either of the halfwords at address 0x8002 and 0x9000 .

Similarly a breakpoint or watchpoint must be disabled:

- If both halves of a 64-bit address have to be updated.
- If any of the DBGBCR&lt;n&gt;\_EL1 or DBGWCR&lt;n&gt;\_EL1 fields are modified at the same time as updating the address.

Example H8-2 Simultaneous accesses to DTR registers

Initially EDSCR.{TXfull, TXU, ERR} are 0. Then:

- 0x0DCCDA7A is directly written to DBGDTRTX\_EL0 by an MSR instruction.
- DBGDTRTX\_EL0 is indirectly read by the external debug interface.

These accesses might happen at the same time and in any order.

If the direct write of 0x0DCCDA7A to DBGDTRTX\_EL0 is handled first, then:

- The external debug interface read of DBGDTRTX\_EL0 clears EDSCR.TXfull to 0.
- EDSCR.{TXU, ERR} are unchanged.
- The external debug interface read returns 0x0DCCDA7A .

If the indirect read of DBGDTRTX\_EL0 by the external debug interface is handled first, then:

- The external debug interface read of DBGDTRTX\_EL0 causes an underrun and as a result EDSCR.{TXU, ERR} are both set to 1.
- The external debug interface returns an UNKNOWN value.
- Writing 0x0DCCDA7A to DBGDTRTX\_EL0 sets DTRTX to 0x0DCCDA7A and EDSCR.TXfull to 1.

Initially all CLAIM tag bits are 0. Then:

- 0x01 is written to DBGCLAIMSET\_EL1 by a direct write, followed by an explicit Context Synchronization event.
- 0x02 is written to DBGCLAIMSET\_EL1 by an external write.

These events might happen at the same time and in either order.

After this:

- DBGCLAIMCLR\_EL1 is read by a direct read.
- DBGCLAIMCLR\_EL1 is read by an external read.

In this case, a direct read can return either 0x01 or 0x03 , and the external read can return either 0x02 or 0x03 .

The only permitted final result for the CLAIM tags is the value 0x03 , because this would be the result regardless of whether 0x01 or 0x02 is written first. This is because the external write is guaranteed to be observable to a direct read in finite time. See Synchronization requirements for AArch64 System registers.

It is not possible for a direct read to return 0x01 and the external read to return 0x02 , because the writes to DBGCLAIMCLR\_EL1 are serialized.

In the following scenario, there is only one permitted result. Both observers observe the value 0x03 , and then, at the same time, two writes occur:

- 0x04 is written to DBGCLAIMSET\_EL1 by a direct write, followed by an explicit Context Synchronization event.
- 0x01 is written to DBGCLAIMCLR\_EL1 by an external write.

In this case, the only permitted final result for the CLAIM tags is the value 0x06 .

Example H8-3 Simultaneous writes to CLAIM registers