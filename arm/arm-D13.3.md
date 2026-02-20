## D13.3 Behavior on overflow

RQZJKS

The event counters, PMEVCNTR&lt;n&gt; are either 32-bit or 64-bit unsigned counters:

- If FEAT\_PMUv3p5 is not implemented, then 32-bit event counters are implemented.
- If FEAT\_PMUv3p5 is implemented, then 64-bit event counters are implemented.

The event counters overflow in the following situations:

- If FEAT\_PMUv3p5 is not implemented and incrementing PMEVCNTR&lt;n&gt; causes an unsigned overflow of the event counter, then the PE sets PMOVSCLR[ n ] to 1.
- If FEAT\_PMUv3p5 is implemented and event counter PMEVCNTR&lt;n&gt; is in the first range, then event counter overflow is configured by PMCR.LP:
- -If the Effective value of PMCR.LP is 0 and incrementing PMEVCNTR&lt;n&gt; causes an unsigned overflow of bits [31:0] of the event counter, then the PE sets PMOVSCLR[ n ] to 1.
- -If the Effective value of PMCR.LP is 1 and incrementing PMEVCNTR&lt;n&gt; causes an unsigned overflow of bits [63:0] of the event counter, then the PE sets PMOVSCLR[ n ] to 1.

When FEAT\_EBEP is implemented and the PMU Profiling exception is enabled, the Effective value of PMCR.LP is 1.

- If FEAT\_PMUv3p5 is implemented and event counter PMEVCNTR&lt;n&gt; is in the second range, then event counter overflow is configured by HDCR.HLP:
- -If the Effective value of HDCR.HLP is 0 and incrementing PMEVCNTR&lt;n&gt; causes an unsigned overflow of bits [31:0] of the event counter, then the PE sets PMOVSCLR[ n ] to 1.
- -If the Effective value of HDCR.HLP is 1 and incrementing PMEVCNTR&lt;n&gt; causes an unsigned overflow of bits [63:0] of the event counter, then the PE sets PMOVSCLR[ n ] to 1.

When FEAT\_EBEP is implemented and the PMU Profiling exception is enabled, the Effective value of HDCR.HLP is 1.

- If event counter PMEVCNTR&lt;n&gt; is in the third range and incrementing PMEVCNTR&lt;n&gt; causes an unsigned overflow of bits [63:0] of the event counter, then the PE sets PMOVSCLR[ n ] to 1.
- RFBGFH If FEAT\_PMUv3\_ICNTR is implemented, then when incrementing PMICNTR\_EL0 causes an unsigned overflow of PMICNTR\_EL0[63:0], the PE sets PMOVSCLR.F0 to 1.

RNTZHW

The cycle counter, PMCCNTR, is a 64-bit unsigned counter, that is configured by PMCR.LC:

- When the Effective value of PMCR.LC is 0, if incrementing PMCCNTR causes an unsigned overflow of bits [31:0] of the cycle counter, the PE sets PMOVSCLR[31] to 1.
- When the Effective value of PMCR.LC is 1, if incrementing PMCCNTR causes an unsigned overflow of bits [63:0] of the cycle counter, the PE sets PMOVSCLR[31] to 1.

When FEAT\_EBEP is implemented and the PMU Profiling exception is enabled, the Effective value of PMCR.LC is 1.

- RHTPDY The update of PMOVSCLR occurs synchronously with the update of the counter.

IRYCLJ

The behavior of the PMU, and other functions that observe the PMU or are triggered by its state, such as the BRBE freeze events, ignore the values of PMUSERENR\_EL0 and PMUACR\_EL1. For example, a counter that is not currently accessible to EL0 might overflow and cause an unexpected PMU freeze-on-overflow or BRBE freeze event when executing at EL0.

- IFYVTD For all 64-bit counters, incrementing the counter is the same whether an unsigned overflow occurs at [31:0] or [63:0]. If the counter increments for an event, bits [63:0] are always incremented,
- IHRJFC APMUoverflow can generate an interrupt request. For more information, see Generating overflow interrupt requests.
- IYBSFJ If FEAT\_EBEP is implemented, then a PMU overflow can generate a PMU Profiling exception. For more information, see Exception-based event profiling.
- IYZZVC

If FEAT\_SEBEP is implemented, then a PMU Profiling exception can be taken synchronously. For more information, see Synchronous exception-based event profiling.

- IZWQTX

If FEAT\_BRBE is implemented, then a a PMU overflow can generate a BRBE freeze event. For more information, see Branch record buffer operation.

| I LMKZN   | If FEAT_PMUv3p9 and FEAT_Debugv8p9 are implemented, then a PMUoverflow can cause the PE to halt and enter Debug state. For more information, see PMUOverflow external debug request.                                                                                                                                                                                                                                                                     |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I PVBJQ   | APMUoverflow can be used as an input trigger event to the Cross Trigger Interface (CTI) for the PE. For more information, see Performance Monitors overflow trigger event.                                                                                                                                                                                                                                                                               |
| I XBXPG   | If FEAT_PMUv3p7 is implemented, then a PMUoverflow can cause event counting to be frozen. For more information, see Freezing PMUcounters.                                                                                                                                                                                                                                                                                                                |
| I ZNDRG   | Software executing at EL1 or higher must take care that setting PMCR.LP or HDCR.HLP does not cause software executing at lower Exception levels to malfunction. If legacy software accesses the PMUat lower Exception levels, software at the higher Exception levels should not set the PMCR.LP or HDCR.HLP fields to 1. However, if the legacy software does not use the counter overflow, it is not affected by setting the PMCR.LP or HDCR.HLP to 1. |

## D13.3.1 Generating overflow interrupt requests

Software can program the Performance Monitors so that an overflow interrupt request is generated when a counter overflows. See PMINTENSET and PMINTENCLR.

Note

- The mechanism by which an interrupt request from the Performance Monitors generates an FIQ or IRQ exception is IMPLEMENTATION DEFINED.
- Arm recommends that the overflow interrupt requests:
- -Translate into a PMUIRQ signal, so that they are observable to external devices.
- -Connect to inputs on an IMPLEMENTATION DEFINED Generic Interrupt Controller as a Private Peripheral Interrupt (PPI) for the originating processor. See the ARM Generic Interrupt Controller Architecture Specification for information about PPIs.
- -Connect to a CTI, see The Embedded Cross-Trigger Interface.
- Arm strongly discourages implementations from connecting overflow interrupt requests from multiple PEs to the same System Peripheral Interrupt (SPI) identifier.
- From GICv3, the ARM ® Generic Interrupt Controller Architecture Specification recommends that the Private Peripheral Interrupt (PPI) with ID 23 is used for overflow interrupt requests.

Software can write to the counters to control the frequency at which interrupt requests occur. For example, software might set a 32-bit counter to 0xFFFF\_0000 , to generate another counter overflow after 65 536 increments, and reset it to this value every time an overflow interrupt occurs.

Note

If an event can occur multiple times in a single clock cycle, then counter overflow can occur without the counter registering a value of zero.

The overflow interrupt request is a level-sensitive request. The PE signals a request for:

- Any implemented PMEVCNTR&lt;n&gt; counter, when the global enable control for the event counter is 1, the value of PMOVSSET.P&lt;n&gt; is 1, and the value of PMINTENSET.P&lt;n&gt; is 1.
- The cycle counter, when the values of PMCR.E, PMOVSSET.C and PMINTENSET.C are all 1.
- The instruction counter, when the values of PMCR.E, PMOVSSET\_EL0.F0, and PMINTENSET\_EL1.F0, are all 1.

The overflow interrupt request is active in all Security states. In particular, if EL3 and EL2 are both implemented, overflow events from PMEVCNTR&lt;n&gt; where n is greater than or equal to the value of HDCR.HPMN can be signaled from all modes and states but only if the value of HDCR.HPME is 1.

The interrupt handler for the counter overflow request must cancel the interrupt request, for example, by writing 1 to PMOVSCLR.P&lt;n&gt; to clear the overflow bit to 0.

IPPSLS

## D13.3.1.1 Pseudocode description of overflow interrupt requests

See A-profile Architecture Pseudocode for a pseudocode description of overflow interrupt requests. The CheckForPMUOverflow() pseudocode function signal PMU overflow interrupt requests to an interrupt controller and PMUoverflow trigger events to the cross-trigger interface.

## D13.3.2 Exception-based event profiling

| R CXBNL   | If FEAT_EBEP is implemented, a PMUProfiling exception is supported.                                                                                                                                                                                                                     |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I FNPMD   | If FEAT_SEBEP is not implemented, the PMUProfiling exception is always taken asynchronously.                                                                                                                                                                                            |
| I JMSPM   | FEAT_EBEP allows a PMUProfiling exception to be generated when a counter overflow bit is set to 1.                                                                                                                                                                                      |
| I PFDLQ   | For backward compatibility, software has to enable the PMUProfiling exception. The exception is enabled for all implemented counters. Enabling the PMUProfiling exception disables the PMUoverflow interrupt request. The CTI Performance Monitors overflow trigger event is unchanged. |

## RGWLVY APMUProfiling exception is enabled and taken to one of the following:

- EL1 if all of the following are true:
- -PMECR\_EL1.PMEE is 0b11 .
- -EL2 is not implemented, EL2 is disabled in the current Security State, or MDCR\_EL2.PMEE is 0b01 .
- -EL2 is not implemented, EL2 is disabled in the current Security State, or HCR\_EL2.TGE is 0.
- -EL3 is not implemented or MDCR\_EL3.PMEE is 0b01 .
- EL2 if all of the following are true:
- -EL2 is implemented and enabled in the current Security State.
- -One of the following is true:
- -MDCR\_EL2.PMEE is 0b11 .
- -PMECR\_EL1.PMEE is 0b11 , MDCR\_EL2.PMEE is 0b01 , and HCR\_EL2.TGE is 1.
- -EL3 is not implemented or MDCR\_EL3.PMEE is 0b01 .
- EL3 if all of the following are true:
- -EL3 is implemented.
- -MDCR\_EL3.PMEE is 0b11 .

The PMU Profiling exception is disabled otherwise.

The pseudocode function PMUExceptionEnabled() shows this.

An enabled PMU Profiling exception is when any of the following are true:

## RSCBDZ masked

- The PE is executing in Debug state.
- The PE is executing at a higher Exception level than the target Exception level of the PMU Profiling exception.
- The PE is executing at EL2, the target Exception level of the PMU Profiling exception is EL2, and MDCR\_EL2.PMEE is not 0b11 .
- The PE is executing at the target Exception level of the PMU Profiling exception, and PSTATE.PM is 1 or PMECR\_EL1.KPME is 0.

Otherwise an enabled PMU Profiling exception is unmasked .

The pseudocode function PMUExceptionMasked() shows this.

Table D13-1 shows the PMU Profiling exception enable and masking for each Exception level. For this table, EL2 is enabled in the current Security state.

Each column in the left side of the table represents the Effective value of a control bit. Each column in the right side of the table represents an Exception level the exception is taken from. In each cell for each of these columns on each row representing a combination of control bits:

IRQ

Dis

Means the exception is disabled and the PMU interrupt request ( PMUIRQ ) is enabled.

Means the exception is disabled and the PMU interrupt request is disabled.

Msk

Means the exception is enabled and masked.

ELx

Means the exception is enabled and taken to ELx.

## Table D13-1 PMU Profiling exception enable and masking for each Exception level

| MDCR_EL3. PMEE   | MDCR_EL2. PMEE   |   HCR_EL2. TGE | PMECR_EL1. PMEE   | PMECR_EL1. KPME   | PSTATE.PM   | EL3   | EL2   | EL1   | EL0   |
|------------------|------------------|----------------|-------------------|-------------------|-------------|-------|-------|-------|-------|
| 0b00             | XX               |              0 | XX                | X                 | X           | IRQ   | IRQ   | IRQ   | IRQ   |
| 0b00             | XX               |              1 | XX                | X                 | X           | IRQ   | IRQ   | n/a   | IRQ   |
| 0b01             | 0b00             |              0 | XX                | X                 | X           | IRQ   | IRQ   | IRQ   | IRQ   |
| 0b01             | 0b00             |              1 | XX                | X                 | X           | IRQ   | IRQ   | n/a   | IRQ   |
| 0b01             | 0b01             |              0 | 0b00              | X                 | X           | IRQ   | IRQ   | IRQ   | IRQ   |
| 0b01             | 0b01             |              0 | 0b10              | X                 | X           | Dis   | Dis   | Dis   | Dis   |
| 0b01             | 0b01             |              0 | 0b11              | 0                 | X           | Msk   | Msk   | Msk   | EL1   |
| 0b01             | 0b01             |              0 | 0b11              | 1                 | 0           | Msk   | Msk   | EL1   | EL1   |
| 0b01             | 0b01             |              0 | 0b11              | 1                 | 1           | Msk   | Msk   | Msk   | EL1   |
| 0b01             | 0b01             |              1 | 0b00              | X                 | X           | IRQ   | IRQ   | n/a   | IRQ   |
| 0b01             | 0b01             |              1 | 0b10              | X                 | X           | Dis   | Dis   | n/a   | Dis   |
| 0b01             | 0b01             |              1 | 0b11              | X                 | X           | Msk   | Msk   | n/a   | EL2   |
| 0b01             | 0b10             |              0 | XX                | X                 | X           | Dis   | Dis   | Dis   | Dis   |
| 0b01             | 0b10             |              1 | XX                | X                 | X           | Dis   | Dis   | n/a   | Dis   |
| 0b01             | 0b11             |              0 | XX                | 0                 | X           | Msk   | Msk   | EL2   | EL2   |
| 0b01             | 0b11             |              0 | XX                | 1                 | 0           | Msk   | EL2   | EL2   | EL2   |
| 0b01             | 0b11             |              0 | XX                | 1                 | 1           | Msk   | Msk   | EL2   | EL2   |
| 0b01             | 0b11             |              1 | XX                | 0                 | X           | Msk   | Msk   | n/a   | EL2   |
| 0b01             | 0b11             |              1 | XX                | 1                 | 0           | Msk   | EL2   | n/a   | EL2   |
| 0b01             | 0b11             |              1 | XX                | 1                 | 1           | Msk   | Msk   | n/a   | EL2   |
| 0b10             | XX               |              0 | XX                | X                 | X           | Dis   | Dis   | Dis   | Dis   |
| 0b10             | XX               |              1 | XX                | X                 | X           | Dis   | Dis   | n/a   | Dis   |
| 0b11             | XX               |              0 | XX                | 0                 | X           | Msk   | EL3   | EL3   | EL3   |
| 0b11             | XX               |              0 | XX                | 1                 | 0           | EL3   | EL3   | EL3   | EL3   |
| 0b11             | XX               |              0 | XX                | 1                 | 1           | Msk   | EL3   | EL3   | EL3   |
| 0b11             | XX               |              1 | XX                | 0                 | X           | Msk   | EL3   | n/a   | EL3   |
| 0b11             | XX               |              1 | XX                | 1                 | 0           | EL3   | EL3   | n/a   | EL3   |
| 0b11             | XX               |              1 | XX                | 1                 | 1           | Msk   | EL3   | n/a   | EL3   |

RKBPMJ

If the PMU Profiling exception is enabled and unmasked, and any of the following apply, then a PMUProfiling exception is taken asynchronously:

- An event counter &lt;n&gt; is implemented, the global enable control for the event counter is 1, PMINTENSET\_EL1.P&lt;n&gt; is 1, PMOVSSET\_EL0.P&lt;n&gt; is 1, and either FEAT\_SEBEP is not implemented or PMEVTYPER&lt;n&gt;\_EL0.SYNC is 0.
- PMCR\_EL0.E is 1, PMINTENSET\_EL1.C is 1, and PMOVSSET\_EL0.C is 1.

- FEAT\_PMUv3\_ICNTR is implemented, PMCR\_EL0.E is 1, PMINTENSET\_EL1.F0 is 1, PMOVSSET\_EL0.F0 is 1, and either FEAT\_SEBEP is not implemented or PMICFILTR\_EL0.SYNC is 0.

IGMXLL

The prioritization of the asynchronous PMU Profiling exception over other exceptions is IMPLEMENTATION DEFINED, as stated by RBKHSW in Asynchronous exception types.

RDKCTL

An unmasked and enabled PMU Profiling exception taken asynchronously is taken in finite time.

RHFTPJ

When all the following are true for a value &lt;n&gt;, a PMU Profiling exception will be taken before instruction C completes execution:

- Instruction A does one of the following:

- Directly reads PMOVSSET\_EL0 or PMOVSCLR\_EL0 and observes that bit &lt;n&gt; is 1.

- Directly writes PMOVSSET\_EL0 setting bit &lt;n&gt; to 1.

- AContext synchronization event B is in program order after A .

- C is the first instruction in program order after B .

- When C starts execution, the PMU Profiling exception is enabled and unmasked, and all other conditions for generating a PMU Profiling exception in RKBPMJ relating to bit &lt;n&gt; apply:

- If &lt;n&gt; is the index of an implemented event counter, then these are the conditions for event counter &lt;n&gt;.

- If &lt;n&gt; is 31, then these are the conditions for the cycle counter PMCCNTR\_EL0.

- If FEAT\_PMUv3\_ICNTR is implemented and &lt;n&gt; is 32, then these are the conditions for the instruction counter PMICNTR\_EL0.

Other values of &lt;n&gt; are not applicable in this rule.

IKLVCH

APMUProfiling exception is taken to the exception vector offset for non-interrupt exceptions at the target Exception level. This includes the asynchronous PMU Profiling exception.

## D13.3.3 Synchronous exception-based event profiling

RGHRZF All statements in this section require implementation of FEAT\_SEBEP.

RFHWMC If FEAT\_SEBEP is implemented, the PMU exception can be taken synchronously.

RSSVKV

For each event counter &lt;n&gt;, PMEVTYPER&lt;n&gt;\_EL0.SYNC controls whether a PMU exception generated by the event counter is synchronous or asynchronous . If all the following are true, then the event counter is in synchronous mode

- The Effective value of PMEVTYPER&lt;n&gt;\_EL0.SYNC is 1.

- The event configured by PMEVTYPER&lt;n&gt;\_EL0.evtCount supports synchronous mode.

Otherwise, the event counter is not in synchronous mode.

The instruction counter is in synchronous mode when the Effective value of PMEVTYPER&lt;n&gt;\_EL0.SYNC is 1. Otherwise, the instruction counter is not in synchronous mode.

RFCXWT

The cycle counter, PMCCNTR\_EL0, does not support synchronous mode.

RKYPTP

Events that can support synchronous mode and generate synchronous exceptions are called synchronous events.

Note

Both synchronous and asynchronous PMU exceptions are precise. See also RLSGJD in Exception entry terminology.

RXLMVX

It is IMPLEMENTATION DEFINED which events are synchronous events. See Synchronous events for the events that Arm recommends support synchronous mode when FEAT\_SEBEP is implemented.

ITSHPG

All of the following apply when a PMU exception is synchronous and precise:

- The instruction that caused the overflow was architecturally executed.

- The overflow flag was set as part of the instruction operation.

- If no higher priority or asynchronous exception is taken first, then the PMU exception is taken in place of the next instruction in the sequential execution order of the program.

| I GQSRL   | If FEAT_SEBEP is implemented, then when any precise exception is taken, including PMUexceptions, the value of all event counters counting at-retirement events and the instruction counter are precise. SeeR TNVSL in Definition of a precise exception and imprecise exception.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R NZLVW   | If all the following apply as an instruction retires, then, other than as permitted by Areasonable degree of inaccuracy, the instruction sets PSTATE.PPEND to 1 and records the instruction address in PMIAR_EL1: • The instruction generated an event counted by an event counter <n>, or is counted by the instruction counter ( n == 32). • The instruction does not generate an exception. • PMINTENSET_EL1[n] is 1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| I HMXCY   | PMOVSSET_EL0[n] is set to 1 when counting an event causes an unsigned overflow of the counter. However,R NZLVW does not require that the instruction generated the particular event which caused overflow, only that the instruction generated the same type of event and that overflow has occurred. If the instruction does generate the event that caused overflow, then the overflow is observed by the same instruction and the sequence of events described inR NZLVW all occur in the same instruction.                                                                                                                                                                                                                                                                                                                                                                                                 |
| R MQDPX   | If any of the following conditions inR NZLVW are changed by the instruction that generates the event, then it is UNPREDICTABLE whether the rule uses the old or new values: • PMINTENSET_EL1[n] is 1. • The counter is enabled and is in synchronous mode. • PMOVSSET_EL0[n] is 1, other than by the indirect write that occurs when the counter overflows. • The PMUexception is enabled. • The PMUexception is unmasked, other than the case of an exception return instruction executed when thePMU exception is enabled and masked, that changes Exception level and/or clears PSTATE.PM, such that thePMU exception becomes unmasked. For such an exception return,R NZLVW treats the PMUexception as masked. For example, the instruction writes to a System register or Special-purpose register. The counter might count the event but not set PSTATE.PPEND to 1. If PSTATE.PPEND is not set to 1 then |
| I HVZKZ   | When an instruction sets PSTATE.PPEND to 1, the updated value of PSTATE.PPEND is observed by the next instruction in the sequential execution order of the program.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| I NPRDL   | If the counter inR NZLVW is not in synchronous mode, then all the following apply: • The overflow is not guaranteed to be observed by the next instruction in the sequential execution order of the program. This means that the PMUexception generated by the counter is taken asynchronously, as described in Exception-based event profiling. • PSTATE.PPEND and PMIAR_EL1 remain unchanged. This includes counters counting events that are not synchronous events.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| R HLYTW   | If all the following apply for an instruction, then a PMUexception is taken synchronously by the instruction: • The PMUexception is enabled and unmasked. • The instruction observes PSTATE.PPEND is 1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| I HJQJP   | BetweenR NZLVW andR HLYTW , the PMUexception might be preempted by a higher priority or asynchronous exception.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| I BBFCX   | PSTATE.PPEND is ignored if the PMUexception is disabled or masked.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| R BVBYS   | When taking an exception to ELx using AArch64 in Non-debug state, all of the following apply: • PSTATE.PPEND is copied to SPSR_ELx[33]. • PSTATE.PPEND is set to 0. Unless a PMUevent generated by the exception return instruction causes the PMUto set PSTATE.PPEND to 1 as described byR NZLVW , then when an exception returns from ELx using AArch64 to ELy in Non-debug state, all of the following apply:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

IBHLTG

RGBQFX

RNHRCY

ICCQDC

- If all of the following apply, then PSTATE.PPEND is copied from SPSR\_ELx[33]:
- -The PMU exception is enabled.
- -The PMU exception is masked when the exception return executes.
- -The PMU exception will be unmasked after the exception return executes.
- Otherwise, PSTATE.PPEND is set to 0.

This includes an illegal exception return.

If the exception return instruction causes PSTATE.PPEND to be set to 1, then the PMU exception is taken before the instruction at the target of the exception return completes. The target instruction is the instruction that observes PSTATE.PPEND is 1.

When entering Debug state in AArch64 state, all of the following apply:

- PSTATE.PPEND is copied to DSPSR\_EL0[33].
- PSTATE.PPEND is set to 0.

When exiting Debug state from ELx using AArch64 to ELy, all of the following apply:

- If all of the following apply, then PSTATE.PPEND is copied from DSPSR\_EL0[33]:
- -The PMU exception is enabled.
- -The PMU exception will be unmasked in Non-debug state after the Debug state exit. For more information, see RSCBDZ.
- Otherwise, PSTATE.PPEND is set to 0.

This includes an illegal return from Debug state.

When entering Debug state in AArch32 state, all of the following apply:

- PSTATE.PPEND is copied to DSPSR2[1].
- PSTATE.PPEND is set to UNKNOWN.

When exiting Debug state from EL0 using AArch32, all of the following apply:

- If the PMU exception is enabled, then PSTATE.PPEND is copied from DSPSR2[1].
- Otherwise, PSTATE.PPEND is set to 0.

This includes an illegal return from Debug state.

Table D13-2 summarizes how the PE sets PSTATE.PPEND on an exception return, based on whether the PMU exception is enabled and unmasked or not before the exception return and after the exception return.

Table D13-2 Summary of setting PSTATE.PPEND on an exception return

|   Case | Before return      | After return       | Behavior of return                     |
|--------|--------------------|--------------------|----------------------------------------|
|      1 | Disabled or masked | Disabled or masked | PSTATE.PPEND is set to 0.              |
|      2 | Masked             | Unmasked           | PSTATE.PPEND is set to SPSR_ELx.PPEND. |
|      3 | Unmasked           | Masked             | Might be CONSTRAINED UNPREDICTABLE.    |
|      4 | Unmasked           | Unmasked           | PSTATE.PPEND might be set byR NZLVW .  |

For case 3, an exception return that causes the PMU exception to become masked:

- RMQDPX allows RNZLVW to treat the exception as either masked or unmasked.
- If the PE treats the exception as unmasked and the other conditions defined by RNZLVW apply, then the PE sets PSTATE.PPEND to 1.
- Otherwise, PSTATE.PPEND is 0.

Note

This means that the behavior is only CONSTRAINED UNPREDICTABLE if all of the other conditions defined by RNZLVW apply.

For case 4, an exception return where the PMU exception stays unmasked:

- If all the conditions defined by RNZLVW apply, then the PE sets PSTATE.PPEND to 1.
- Otherwise, PSTATE.PPEND is 0.

How the PE sets PSTATE.PPEND on Debug state exit is similar, noting that PMU exceptions are always masked in Debug state.