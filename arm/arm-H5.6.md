## H5.6 Examples

The CTI is fully programmable and allows for flexible cross-triggering of events within a PE and between PEs in a multiprocessor system. For example:

- The Cross-halt trigger event and the Debug request trigger event can be used for cross-triggering in a multiprocessor system.
- The Cross-halt trigger event and the Generic interrupt trigger event can be used for event-driven debugging in a multiprocessor system.
- The Performance Monitors overflow trigger event and the Debug request trigger event can force entry to Debug state on overflow of a Performance Monitors event counter, for event-driven profiling.

Note

This does not replace the recommended connection of Performance Monitors overflow trigger events to an interrupt controller. Software must be able to program an interrupt on Performance Monitors overflow without programming the CTI. Arm recommends that the Performance Monitors overflow signal is directly available as a local interrupt source.

- The Generic trace external input and Generic trace external output trigger events can pass trace events into and out of the event logic of the trace unit. They can do this:
- -To pass trace events between Trace Units.
- -In conjunction with the Performance Monitors overflow trigger event, to couple the Performance Monitors to the PE trace unit.
- -In conjunction with the Debug request trigger event, to trigger entry to Debug state on a trace event.
- -In conjunction with other CTIs, to signal a trace trigger event onto a CoreSight trace interconnect.

The following sections describe some examples in more detail:

- Example H5-1.
- Example H5-2.
- Example H5-3.
- Example H5-4.

To halt a single PE, set:

1. CTIGATE[0] to 0, so that the CTI does not pass channel events on internal channel 0 to the CTM.
2. CTIOUTEN0[0] to 1, so that the CTI generates a Debug request trigger event in response to a channel event on channel 0.

Note

The Cross-halt trigger event is input trigger 0, meaning it is controlled by the instance of CTIOUTEN&lt;n&gt; for which &lt;n&gt; is 0.

3. CTIAPPPULSE[0] to 1, to generate a channel event on channel 0.

Whenthe PE has entered Debug state, clear the Debug request trigger event by writing 1 to CTIINTACK[0], before restarting the PE.

Example H5-1 Halting a single PE

## Example H5-2 Halting all PEs in a group when any one PE halts

To program a group of PEs so that when one PE in the group halts, all of the PEs in that group halt, set the following registers for each PE in the group:

1. CTIGATE[2] to 1, so that each CTI passes channel events on internal channel 2 to the CTM.
2. CTIINEN0[2] to 1, so that each CTI generates a channel event on channel 2 in response to a Cross-halt trigger event.
3. CTIOUTEN0[2]to 1, so that each CTI generates a Debug request trigger event in response to a channel event on channel 2.

Note

The Cross-halt trigger event is input trigger 0, meaning it is controlled by the instances of CTIINEN&lt;n&gt; and CTIOUTEN&lt;n&gt; for which &lt;n&gt; is 0.

When a PE has halted, clear the Debug request trigger event by writing a value of 1to CTIINTACK[0], before restarting the PE.

## Example H5-3 Synchronously restarting a group of PEs

To restart a group of PEs, for each PE in the group:

1. If the PE was halted because of a Debug request trigger event, the debugger must ensure the trigger event is deasserted. It can do this by:
- a. Writing 1 to CTIINTACK[0] to clear the Debug request trigger event.
- b. Polling CTITRIGOUTSTATUS[0], until it reads as 0, to confirm that the trigger event has been deasserted.
2. Set CTIGATE[1] to 1, so that each CTI passes channel events on internal channel 1 to the CTM.
3. Set CTIOUTEN1[1] to 1, so that each CTI generates a Restart request trigger event in response to a channel event on channel 1.

Note

This example must use the instance of CTIOUTEN&lt;n&gt; for which &lt;n&gt; is 1.

4. Set CTIAPPPULSE[1] to 1 on any one PE in the group, to generate a channel event on channel 1.

## Example H5-4 Halting a single PE on Performance Monitors overflow

To halt a single PE on a Performance Monitors overflow set:

1. CTIGATE[3] to 0, so that the CTI does not pass channel events on internal channel 3 to the CTM.
2. CTIINEN1[3] to 1, so that the CTI generates a channel event on channel 3 in response to a Performance Monitors overflow trigger event.

Note

This step of this example must use the instance of CTIINEN&lt;n&gt; for which &lt;n&gt; is 1.

3. CTIOUTEN0[3] to 1, so that the CTI generates a Debug request trigger event in response to a channel event on channel 3.

Note

This step of this example must use the instance of CTIOUTEN&lt;n&gt; for which &lt;n&gt; is 0.

Whenthe PE has entered Debug state, clear the Debug request trigger event by writing 1 to CTIINTACK[0], before restarting the PE. Clear the overflow status by writing to PMOVSCLR\_EL0.

## Chapter H6 Debug Reset and Powerdown Support

This chapter describes the reset and powerdown support in the Debug architecture. It contains the following sections:

- About Debug over powerdown.
- Power domains and debug.
- Core power domain power states.
- Emulating low-power states.
- Powerup request mechanism.
- Debug OS Save and Restore sequences.
- Reset and debug.

Note

Where necessary, Table K14-1 disambiguates the general register references used in this chapter.