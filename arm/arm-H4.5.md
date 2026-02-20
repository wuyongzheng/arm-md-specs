## H4.5 Synchronization of DCC and ITR accesses

In addition to the standard synchronization requirements for register accesses, the following subsections describe additional requirements that apply for the DCC and ITR registers:

- Summary of System register accesses to the DCC.
- DCCaccesses in Non-debug state.
- Synchronization of DCC interrupt request signals.
- DCCand ITR access in Debug state.

In these sections, accesses by the external debug interface are referred to as external reads and external writes. Accesses to System registers are referred to as direct reads, direct writes, indirect reads, and indirect writes.

Note

In Synchronization requirements for AArch64 System registers external reads and external writes are described as forms of indirect access. This whole section uses more explicit terminology.

The DTR registers and the DCC flags, TXfull and RXfull, form a communication channel, with one end operating asynchronously to the other. Implementations must respect the ordering of accesses to these registers in order to maintain the correct behavior of the channel.

External reads of, and external writes to DBGDTRRX\_EL0 and DBGDTRTX\_EL0 are asynchronous to direct reads of, and direct writes to, DBGDTRRX, DBGDTRTX, and in AArch64 state DBGDTR\_EL0, made by software using System register access instructions. The direct reads and direct writes indirectly write to the DCC flags. The external reads and external writes indirectly read the DCC flags to check for underrun and overrun.

Throughout this section:

DCCflags

Means any or all of the following:

- The EDSCR.{RXfull.TXfull} ready flags.
- The EDSCR.RXO overrun flag.
- The EDSCR.TXU underrun flag.
- The EDSCR.ERR cumulative error flag.

ITR flags Means any or all of the following:

- The EDSCR.ITE ready flag.
- The EDSCR.ITO overrun flag.
- The EDSCR.ERR cumulative error flag.

## H4.5.1 Summary of System register accesses to the DCC

System register accesses to the DTR registers are direct reads and writes of those registers, as shown in Table H4-3. Several of these instructions access the same registers using different encodings.

DBGDTRRX\_EL0 and DBGDTRTX\_EL0 are encoded as MRS and MSR accesses respectively to the same System register, even though they access different underlying register values. DBGDTRRX and DBGDTRTX are similarly encoded as MRC and MCR accesses respectively to the same System register. The encoding means that direct reads and writes using these encodings must be ordered with respect to each other. For more information, see Synchronization requirements for AArch64 System registers and Synchronization of changes to AArch32 System registers.

Table H4-3 shows a summary of System register accesses to the DCC.

## Table H4-3 Summary of System register accesses to the DCC

| Operation   | OS Lock   | AArch64 (MRS/MSR)   | AArch32 (MRC/MCR)   | Description                                                                                                                                                           |
|-------------|-----------|---------------------|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Read        | -         | DBGDTRRX_EL0        | DBGDTRRXint         | Direct read of DTRRX. Indirect write to the DCCflags. An STC instruction that reads DBGDTRRXint makes an indirect write to DBGDSCRint.RXfull.                         |
| Write       | -         | DBGDTRTX_EL0        | DBGDTRTXint         | Direct write of DTRTX. Indirect write to the DCCflags. An LDC instruction that writes to DBGDTRTXint using a value read from memory is a direct write to DBGDTRTXint. |
| Read/write  | -         | DBGDTR_EL0          | -                   | Direct read/write of both DTRRXand DTRTX. Indirect write to the DCCflags.                                                                                             |
| Read        | -         | MDCCSR_EL0          | DBGDSCRint          | Direct read of the DCCflags.                                                                                                                                          |
| Read/write  | -         | OSDTRRX_EL1         | DBGDTRRXext         | Direct read/write of DTRRX.                                                                                                                                           |
| Read/write  | -         | OSDTRTX_EL1         | DBGDTRTXext         | Direct read/write of DTRTX.                                                                                                                                           |
| Read        | Unlocked  | MDSCR_EL1           | DBGDSCRext          | Direct read of DCCflags.                                                                                                                                              |
| Read/write  | Locked    | MDSCR_EL1           | DBGDSCRext          | Direct read/write of DCCflags.                                                                                                                                        |

## H4.5.2 DCC accesses in Non-debug state

In Non-debug state DCC accesses are as described in Normal access mode:

- If a direct read of DCCSR returns RXfull == 1, then a following direct read of DBGDTRRX, or in AArch64 state of DBGDTR\_EL0, returns valid data and indirectly writes 0 to DCCSR.RXfull as a side-effect.
- If a direct read of DCCSR returns TXfull == 0, then a following direct write to DBGDTRTX, or in AArch64 state to DBGDTR\_EL0, writes the intended value, and indirectly writes 1 to DCCSR.TXfull as a side-effect.

No Context Synchronization event is required between these two instructions. Overrun and underrun detection prevents intervening external reads and external writes affecting the outcome of the second instruction.

The indirect write to the DCC flags as part of the DTR access instruction is made atomically with the DTR access.

Because a direct read of DBGDTRRX is an indirect write to DCCSR.RXfull, it must occur in program order with respect to the direct read of DCCSR, meaning it must not return a speculative value for DTTRX that predates the RXfull flag returned by the read of DCCSR. The direct write to DBGDTRTX must not be executed speculatively.

Direct reads of DBGDTRRX, or in AArch64 state DBGDTR\_EL0, and DCCSR, must occur in program order with respect to other direct reads of the same register using the same encoding.

The following accesses have an implied order within the atomic access:

- In the simple sequential execution of the program the indirect write of the DCC flags occurs immediately after the direct DTR access.

Note

For an access to DBGDTR\_EL0, this means the indirect write happens after both DBGDTRRX\_EL0 and DBGDTRTX\_EL0 have been accessed.

- In the simple sequential execution model, for an external read of DBGDTRTX\_EL0 or an external write of DBGDTRRX\_EL0:
- -The check of the DCC flags for overrun or underrun occurs immediately before the access.
- -If there is no underrun or overrun, the update of the DCC flags occurs immediately after the access.
- -If there is underrun or overrun, the update of the DCC underrun or overrun flags occurs immediately after the access.

All observers must observe the same order for accesses.

Note

These requirements do not create order where order does not otherwise exist. It applies only for ordered accesses.

Without explicit synchronization following external writes and external reads:

- The value written by the external write to DBGDTRRX\_EL0 that does not overrun, must be observable to direct reads of DBGDTRRX and DBGDTR\_EL0 in finite time.
- The DCC flags that are updated as a side-effect of the external write or external read must be observable:
- -To subsequent external reads of EDSCR.
- -To subsequent external reads of DBGDTRRX\_EL0 when checking for underrun.
- -To subsequent external writes to DBGDTRTX\_EL0 when checking for overrun.
- -To direct reads of DCCSR in finite time.

However, explicit synchronization is required to guarantee that a direct read of DCCSR returns up-to-date DCC flags. This means that if a signal is received from another agent that indicates that DCCSR must be read, an ISB is required to ensure that the direct read of DCCSR occurs after the signal has been received. This also synchronizes the value in DBGDTRRX, if applicable. However, if that signal is an interrupt exception triggered by COMMIRQ , COMMTX , or COMMRX , the exception entry is sufficient synchronization. See Synchronization of DCC interrupt request signals.

Explicit synchronization is required following a direct read or direct write:

- To ensure that a value directly written to DBGDTRTX is observable to external reads of DBGDTRTX\_EL0.
- To ensure that a value directly written to DBGDTR\_EL0 is observable to external reads of DBGDTRTX\_EL0 and DBGDTRRX\_EL0.
- To guarantee that the indirect writes to the DCC flags that were a side-effect of the direct read or direct write have occurred, and therefore that the updated values are:
- -Observable to external reads of EDSCR.
- -Observable to external reads of DBGDTRRX\_EL0 when checking for underrun.
- -Observable to external writes of DBGDTRTX\_EL0 when checking for overrun.
- -Returned by a following direct read of DCCSR.

See also Memory-mapped accesses to the DCC and ITR and Synchronization of changes to the external debug registers.

Note

These ordering rules mean that software:

- Must not read DBGDTRRX without first checking DCCSR.RXfull or if the previously-read value of DCCSR.RXfull is 0.

It is not sufficient to read both registers and then later decide whether to discard the read value, as there might be an intervening write from the external debug interface.

- Must not write DBGDTRTX without first checking DCCSR.TXfull or if the previously-read value of DCCSR.TXfull is 1.

The write to DBGDTRTX overwrites the value in DTRTX, and the external debugger might or might not have read this value.

- Must ensure there is an explicit Context Synchronization event following a DTR access, even if not immediately returning to read DCCSR again. This synchronization operation can be an exception return.

## H4.5.2.1 Derived requirements

The rules for DCC accesses in Non-debug state are as follows:

- Following a direct read of DBGDTRRX when RXfull is 1:
- -If an external write to DBGDTRRX checks the RXfull flag for overrun and observes that the value of RXfull is 0, the value returned by the previous direct read must not be affected by the external write.

- -If an external read of EDSCR returns a RXfull value of 0, then the value returned by the previous direct read must not be affected by a following external write to DBGDTRRX, and the following external write does not overrun.
- Following a direct read of DBGDTR\_EL0, when RXfull is 1:
- -If an external write to DBGDTRRX checks the RXfull flag for overrun and observes that the value of RXfull is 0, the value returned by the previous direct read must not be affected by the external write nor by a following direct write to DBGDTRTX.
- -If an external read of EDSCR returns a RXfull value of 0, then the value returned by the previous direct read must not be affected by subsequent external writes to DBGDTRRX and DBGDTRTX in any order, and the following external write of DBGDTRRX will not overrun.
- Following a direct write to DBGDTRTX, when TXfull is 0:

- [ ] -If an external read of DBGDTRTX checks the TXfull flag for underrun and observes that the value of TXfull is 1, the value returned by the external read must be the value written by the previous direct write.

- -If an external read of EDSCR returns a TXfull value of 1, then the value returned by a following external read of DBGDTRRX must be the value written by the previous direct read, and the subsequent external read will not underrun.
- Following a direct write to DBGDTR\_EL0, when TXfull is 0:
- -If an external read of DBGDTRTX checks the TXfull flag for underrun and observes that the value of TXfull is 1, the values returned by the external read and by a subsequent external read of DBGDTRRX must be the value written by the previous direct write.
- -If an external read of EDSCR returns a TXfull value of 1, then the value returned by subsequent external reads of DBGDTRRX and DBGDTRTX, in any order, must be the value written by the previous direct read, and the subsequent external read of DBGDTRTX does not underrun.
- Following an external read of DBGDTRTX that does not underrun, if a direct read of DCCSR returns a TXfull value of 0, then the value returned by the external read must not be affected by a following direct write to DBGDTRTX.
- Following a first external read DBGDTRRX and a following second external read of DBGDTRTX that does not underrun, if a direct read of DCCSR returns a TXfull value of 0, then the values returned by the external reads must not be affected by a following direct write to DBGDTR\_EL0.
- Following an external write to DBGDTRRX that does not overrun, if a direct read of DCCSR returns an RXfull value of 1, then the value returned by a following direct read of DBGDTRRX or DBGDTR\_EL0 must be the value written by the previous external write.
- Following a first external write to DBGDTRTX and a following second external write to DBGDTRRX that does not overrun, if a direct read of DCCSR returns an RXfull value of 1, then the value returned by a subsequent direct read of DBGDTR\_EL0 must return the values written by the previous external writes.

## H4.5.3 Synchronization of DCC interrupt request signals

Following an external read or external write access to the DTR registers, the interrupt request signals, COMMIRQ , COMMTX , and COMMRX , must be updated in finite time without explicit synchronization.

The updated values must be observable to a direct read of DCCSR or DBGDTRRX, or a direct write of DBGDTRTX executed after taking an interrupt exception generated by the interrupt request. The updated values must also be observable to a direct write of DBGDTRTX executed after taking an interrupt exception generated by the interrupt request.

Note

The requirement that indirect writes to registers are observable to direct reads in finite time does not imply that all observers will observe the indirect write at the same time. For more information, see Synchronization requirements for AArch64 System registers and Synchronization of changes to AArch32 System registers.

Following a direct read of DBGDTRRX or a direct write to DBGDTRRX, software must execute a Context Synchronization event to guarantee the interrupt request signals have been updated in finite time. This synchronization operation can be an exception return.

## H4.5.4 DCC and ITR access in Debug state

In Debug state, stricter observability rules apply for instructions issued through the ITR, to maintain communication between a debugger and the PE, without requiring excessive explicit synchronization.

In Normal access mode, without explicit synchronization:

- Adirect read or direct write of the DTR registers by an instruction written to EDITR must be observable to an external write or an external read in finite time:
- -Adirect read of DBGDTRRX must be observable to an external write of DBGDTRRX\_EL0.
- -Adirect read of DBGDTR\_EL0 must be observable to an external write of DBGDTRRX\_EL0 and DBGDTRTX\_EL0.
- -Adirect write of DBGDTRTX must be observable to an external read of DBGDTRTX\_EL0.
- -Adirect write of DBGDTR\_EL0 must be observable to an external read of DBGDTRRX\_EL0 and DBGDTRTX\_EL0.

This includes the indirect write to the DCC flags that occurs atomically with the access as described in DCC accesses in Non-debug state.

The subsequent external write or external read must observe either the old or the new values of both the DTR contents and DCC flags. If the old values are observed, this typically results in overrun or underrun, assuming the old values of the DCC flags indicate an overrun or underrun condition, as would normally be the case.

This means the debugger can observe the direct read or direct write without explicit synchronization and without explicitly testing the DCC flags in EDSCR, because it can rely on overrun and underrun tests.

- External reads of DBGDTRTX\_EL0 that do not underrun and external writes to DBGDTRRX\_EL0 that do not overrun must be observable to an instruction subsequently written to EDITR on completion of the first external access. This includes the indirect write to the DCC flags.

This means that without explicit synchronization and without the need to first check the DCC flags in DCCSR:

- -If the instruction is a direct read of DBGDTRRX, it observes the external write.
- -If the instruction is a direct write of DBGDTRTX, it observes the external read.
- Writes to EDITR that do not overrun commit an instruction for execution immediately. The instruction must complete execution in finite time without requiring any further operation by the debugger.
- After an external write to the EDITR, the ITR flags that are updated as a side effect of that write must be observable by:
- -An external read of the EDSCR that follows the external write to the EDITR.
- -When checking for overrun, another external write to the EDITR that follows the original external write to the EDITR.

In Memory access mode, these requirements shift to the instructions implicitly executed by external reads and external writes of the DTR registers, as described in Memory access mode.