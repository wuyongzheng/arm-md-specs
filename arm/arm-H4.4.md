## H4.4 Flow control of the DCC and ITR registers

- Ready flags.
- Buffering writes to EDITR.
- Overrun and underrun flags.
- Cumulative error flag.

## H4.4.1 Ready flags

In Normal access mode:

- For the DTR registers there are two ready flags:
- -EDSCR.RXfull == 1 indicates that DBGDTRRX\_EL0 contains a valid value that has been written by the external debugger and not yet read by software running on the target.
- -EDSCR.TXfull == 1 indicates that DBGDTRTX\_EL0 contains a valid value that has been written by software running on the target and not yet read by an external debugger.
- For the ITR register there is a single ready flag:
- -EDSCR.ITE == 1 indicates that the PE is ready to accept an instruction to the ITR.

Note

The architecture permits a PE to continue to accept and buffer instructions when previous instructions have not completed their architecturally defined behavior, as long as those instructions are discarded if EDSCR.ERR is 1, either by an underrun or overrun or by any of the other error conditions described in this architecture, such as an instruction generating an abort.

In Memory access mode:

- EDSCR.{RXfull, ITE} == {0,1} indicates that DBGDTRRX\_EL0 is empty and the PE is ready to accept a word external write to DBGDTRRX\_EL0.
- EDSCR.{TXfull, ITE} == {1,1} indicates that DBGDTRTX\_EL0 is full and the PE is ready to accept a word external read from DBGDTRTX\_EL0.

All other values indicate that the PE is not ready, and result in a DTR overrun or underrun error, an ITR overrun error, or both, as defined in Overrun and underrun flags.

EDSCR.{ITE, RXfull, TXfull} shows the status of the ITR and DCC registers. It ignores the question of whether a read or write cannot be accepted because, for example, EDSCR.ERR is set or the OPTIONAL Software Lock is locked for memory-mapped accesses (EDLSR.SLK == 1).

## H4.4.2 Buffering writes to EDITR

The architecture permits a processor to continue to accept and buffer instructions when previous instructions have not completed their architecturally defined behavior, provided that:

- Those instructions are discarded if EDSCR.ERR is set to 1, either by an underrun or an overrun, or by any other error conditions described in this architecture, such as an instruction generating an abort.
- The PE maintains the simple sequential execution model with the order of instructions determined by the order in which the PE accepts the EDITR writes. In particular, the buffered instructions must be executed in the Execution state consistent with a simple sequential execution of the instructions, even if one of the previous instructions is a state changing operation, such as DCPS or DRPS .

## H4.4.3 Overrun and underrun flags

Each of the ready flags has a corresponding overrun or a corresponding underrun flag. These are sticky status flags that are set if the register is accessed using the external debug interface when the corresponding ready flag is not in the ready state.

If the PE is in Debug state and Memory access mode, the corresponding error flag is also set if the PE is not ready to accept an operation because a previous load or store is still in progress. The sticky status flag remains set until cleared by writing 1 to EDRCR.CSE.

Note

The architecture permits a PE to continue to accept and buffer data to write to memory in Memory access mode.

Table H4-2 shows DCC and ITR ready flags and the overrun and underrun flags associated with them.

Table H4-2 DCC and ITR ready flags and the associated overrun/underrun flags

| External debug interface access   | Overrun/Underrun condition                                                          | EDSCR flag   |
|-----------------------------------|-------------------------------------------------------------------------------------|--------------|
| Write DBGDTRRX_EL0                | EDSCR.RXfull == '1' &#124;&#124; (Halted() && EDSCR.MA == '1' && EDSCR.ITE == '0')  | RXO          |
| Read DBGDTRTX_EL0                 | EDSCR.TXfull == '0' &#124;&#124; (Halted() && EDSCR.MA == '1' && EDSCR.ITE == '0' ) | TXU          |
| Write EDITR                       | Halted() && (EDSCR.ITE == '0' &#124;&#124; EDSCR.MA == '1')                         | ITO          |

When an overrun or underrun flag is set to 1, the cumulative error flag, EDSCR.ERR, described in Cumulative error flag, is also set to 1.

In the event of an external write to DBGDTRRX\_EL0 or EDITR generating an overrun, or an external read from DBGDTRTX\_EL0 generating an underrun:

- For a write, the written value is ignored.
- For a read, an UNKNOWN value is returned.
- EDSCR.TXfull, EDSCR.RXfull or EDSCR.ITE, as applicable, are not updated.

There is no overrun or underrun detection on external reads of DBGDTRRX\_EL0 or external writes of DBGDTRTX\_EL0.

There is no overrun or underrun detection of direct reads and direct writes of the DTR System registers by software:

- If RXfull == 0, a direct read of DBGDTRRX or DBGDTR\_EL0 returns UNKNOWN.
- If TXfull == 1, a direct write of:
- -DBGDTRTXsets DTRTX to UNKNOWN.
- -DBGDTR\_EL0 sets DTRRX and DTRTX to UNKNOWN.

See DCC accesses in Non-debug state for more information.

## H4.4.3.1 Accessing 64-bit data

In AArch64 state, a software access to the DBGDTR\_EL0 register and an external debugger access to both DBGDTRRX\_EL0 and DBGDTRTX\_EL0 can perform a 64-bit half-duplex operation.

However, there is only overrun and underrun detection on one of the external debug registers. That is:

- If software directly writes a 64-bit value to DBGDTR\_EL0, only TXfull is set to 1, meaning:
- -Asubsequent external write to DBGDTRRX\_EL0 would not be detected as an overrun.

- -If the external debugger reads DBGDTRTX\_EL0 first, software might observe MDCCSR\_EL0.TXfull == 0 and send a second value before the external debugger reads DBGDTRRX\_EL0, leading to an undetected overrun.
- On external writes to both DBGDTRRX\_EL0 and DBGDTRTX\_EL0, only RXfull is set to 1, meaning:
- -Asubsequent direct write of DBGDTRTX\_EL0 would not be detected as an overrun.
- -If the external debugger writes to DBGDTRRX\_EL0 first, software might observe MDCCSR\_EL0.RXfull == 1 and read a full 64-bit value, before the external debugger writes to DBGDTRTX\_EL0, leading to an undetected underrun.

To avoid this, debuggers need to be aware of the data size used by software for transfers and ensure that 64-bit data is read or written in the correct order. If the PE is in Non-debug state, this order is as follows:

- The external debugger must check EDSCR.{RXfull, TXfull} before each transfer.
- To receive a 64-bit value from the target, the external debugger must read DBGDTRRX\_EL0 before reading DBGDTRTX\_EL0.
- To send a 64-bit value to the target, the external debugger must write to DBGDTRTX\_EL0 before writing DBGDTRRX\_EL0.

Because three accesses are required to transfer 64 bits of data, 64-bit transfers are not recommended for regular communication between host and target. The use of underrun and overrun detection means that only one access is required for 32 bits of data when using 32-bit transfers.

In Debug state, the debugger controls the instructions executed by the PE, so these limitations do not apply. 64-bit transfers provide a means to transfer a 64-bit general register between the host and the target in Debug state.

## H4.4.4 Cumulative error flag

The cumulative error flag, EDSCR.ERR, is set to 1:

- On taking an exception from Debug state.
- On any signaled overrun or underrun in the DCC or ITR.

When EDSCR.ERR == 1:

- External reads of DBGDTRTX\_EL0 do not have any side-effects.
- External writes to DBGDTRRX\_EL0 are ignored.
- External writes to EDITR are ignored.
- No further instructions can be issued in Debug state. This includes any instructions previously accepted as external writes to EDITR that occur in program order after the instruction or access that caused the error.

This allows a debugger to stream data, or, in Debug state, instructions, to the target without having to:

- Check EDSCR.{RXfull, TXfull, ITE} before each access.
- Check EDSCR.{ITO, RXO, TXU} following each access, for overrun or underrun.
- Check PSTATE or other syndrome registers, or both, for an exception following each instruction executed in Debug state that might generate a synchronous exception.

The cumulative error flag remains set until cleared to 0 by writing 1 to EDRCR.CSE. However, the effect of writing 1 to EDRCR.CSE to clear EDSCR.ERR is CONSTRAINED UNPREDICTABLE when both of the following apply:

- The PE is in Debug state.
- The value of EDSCR.ITE is 0.

When these conditions apply and a value of 1 is written to EDRCR.CSE, either or both of the following might occur:

- EDSCR.ERR is not cleared to 0.
- Any instructions in EDITR that have not been executed might be executed subsequently, rather than being ignored.

Note

This means that a debugger must poll EDSCR.ITE until it has the value 1, indicating that EDITR is empty, before writing to EDRCR.CSE to clear the EDSCR.ERR flag to 0.

For overruns and underruns, EDSCR.{ITO, RXO, TXU} record the error type.

## H4.4.4.1 Pseudocode description of clearing the error flag

The ClearStickyErrors() pseudocode function is described in A-profile Architecture Pseudocode.