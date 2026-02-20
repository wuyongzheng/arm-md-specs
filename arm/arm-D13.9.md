## D13.9 PMU snapshots

IVZCDM

The PMU snapshot extension provides a mechanism to take a snapshot of the PMU state at a given cycle on request.

RSCLCQ

If all of the following are true, then a Capture event is generated:

- FEAT\_PMUv3\_SS is implemented.
- Capture events are enabled.
- Any of the following occur:
- -The value 1 is written to PMSSCR\_EL1.SS.
- -The assertion of an IMPLEMENTATION DEFINED external snapshot request mechanism. This indirectly writes 1 to PMSSCR\_EL1.SS.
- The Core power domain is powered on.

RMFJWS If Capture events are disabled, then PMSSCR\_EL1.SS ignores writes.

RYWLFL If any of the following are true, then Capture events are disabled:

- EL3 is implemented and MDCR\_EL3.PMSSE is 0b00 .
- All of the following are true:
- -EL3 is not implemented or MDCR\_EL3.PMSSE is 0b01 .
- -EL2 is implemented.
- -MDCR\_EL2.PMSSE is 0b00 .

This applies even when EL2 is disabled in the current Security state.

- All of the following are true:
- -EL3 is not implemented or MDCR\_EL3.PMSSE is 0b01 .
- -EL2 is not implemented or MDCR\_EL2.PMSSE is 0b01 . This applies even when EL2 is disabled in the current Security state.
- -PMECR\_EL1.SSE is 0b00 .

Otherwise, Capture events are enabled.

The pseudocode function PMUCaptureEventEnabled() shows this.

RTSYTY If all of the following are true, then Capture events are allowed:

- Capture events are enabled.
- The OS Lock is unlocked.
- Any of the following are true:
- -EL3 is implemented and MDCR\_EL3.PMSSE is 0b11 .
- -All of the following are true:
- -EL3 is not implemented or MDCR\_EL3.PMSSE is 0b01 .
- -EL2 is implemented.
- -MDCR\_EL2.PMSSE is 0b11 .

This applies even when EL2 is disabled in the current Security state.

- -All of the following are true:
- -EL3 is not implemented or MDCR\_EL3.PMSSE is 0b01 .
- -EL2 is not implemented or MDCR\_EL2.PMSSE is 0b01 . This applies even when EL2 is disabled in the current Security state.
- -PMECR\_EL1.SSE is 0b11 .
- Either the PE is in Non-debug state or the PE allows Capture events in Debug state.

Otherwise, Capture events are prohibited.

It is IMPLEMENTATION DEFINED whether the PE allows Capture events in Debug state.

The pseudocode function PMUCaptureEventAllowed() shows this.

Table D13-10 summarizes the effect of the controls on PMU Capture events. In this table:

Disabled

Means Capture events are disabled.

Prohibited

Means Capture events are enabled and prohibited.

Allowed

Means Capture events are enabled and allowed.

IMRCSY

IWHYSQ

RVPZHN

RDBRSV

## Table D13-10 PMU Capture events

| MDCR_EL3.PMSSE   | MDCR_EL2.PMSSE   | PMECR_EL1.SSE   | Capture Events   |
|------------------|------------------|-----------------|------------------|
| 0b00             | xx               | xx              | Disabled         |
| 0b01             | 0b00             | xx              | Disabled         |
| 0b01             | 0b01             | 0b00            | Disabled         |
| 0b01             | 0b01             | 0b10            | Prohibited       |
| 0b01             | 0b01             | 0b11            | Allowed          |
| 0b01             | 0b10             | xx              | Prohibited       |
| 0b01             | 0b11             | xx              | Allowed          |
| 0b10             | xx               | xx              | Prohibited       |
| 0b11             | xx               | xx              | Allowed          |

## Note

Whenall of the following apply, an EL3 Secure or Root monitor switching to Secure state should set MDCR\_EL2.PMSSE to 0b01 :

- SCR\_EL3.EEL2 is 0, disabling EL2 in Secure state.
- MDCR\_EL3.PMSSE is 0b01 , enabling use of PMU snapshot by lower Exception levels.
- MDCR\_EL3.{MPMX, SPME} is not {0, 0}, meaning Secure state uses the PMU.

This ensures that control over PMU snapshot moves to PMECR\_EL1. In such a scenario, the EL3 monitor might have to rewrite other MDCR\_EL2 fields. For example setting MDCR\_EL2.HPMN to PMCR\_EL0.N so that Secure EL1 has full control over the PMU counters. Alternatively, if Secure EL1 does not support PMU snapshot, then the EL3 monitor could set MDCR\_EL3.PMSSE or MDCR\_EL2.PMSSE to 0b00 , and avoid also context switching PMECR\_EL1. If Secure state is not using the PMU (MDCR\_EL3.SPME is 0), then the EL3 monitor should leave MDCR\_EL2.PMSSE

and PMECR\_EL1 unchanged, so that external snapshot requests can be serviced.

If a Capture event occurs when allowed, then the PE writes all of the following snapshot registers:

- Event counters PMEVCNTR&lt;n&gt;\_EL0 are written to PMEVCNTSVR&lt;n&gt;\_EL1.
- Cycle counter PMCCNTR\_EL0 is written to PMCCNTSVR\_EL1.
- If FEAT\_PMUv3\_ICNTR is implemented, instruction counter PMICNTR\_EL0 is written to PMICNTSVR\_EL1.
- If FEAT\_PCSRv8p9 is implemented and sampling on PMU snapshot Capture events is enabled by PMPCSCTL.SS, then all of the following:
- -If PC sampling is allowed and the PE is in Non-debug state, then all of the following:
- -The address of a recently-executed instruction and the execution state are written to PMPCSR.
- -If FEAT\_PMUv3\_EXT32 is implemented, then the Context ID registers CONTEXTIDR\_EL2 and CONTEXTIDR\_EL1 are written to PMCID2SR and PMCID1SR, respectively, and the Virtual machine identifier (VMID) is written to PMVIDSR.
- -If FEAT\_PMUv3\_EXT64 is implemented, CONTEXTIDR\_EL2 and CONTEXTIDR\_EL1 are written to PMCCIDSR, and VMID and CONTEXTIDR\_EL1 are written to PMVCIDSR.

In some circumstances, the address of a Recently-executed instruction is not available or UNKNOWN.

- -Otherwise, PMPCSR[31:0] is set to 0xFFFF\_FFFF , and PMPCSR[63:32], PMCID1SR, PMCID2SR, PMVIDSR, PMCCIDSR, and PMVCIDSR are unchanged.

If sampling on PMU snapshot is disabled then PMPCSR, PMCID1SR, PMCID2SR, PMVIDSR, PMCCIDSR, and PMVCIDSR are unchanged.

After these writes are completed, PMSSCR\_EL1.{NC, SS} is set to {0, 0} to indicate that a Capture event has completed successfully.

PC sampling is allowed is defined by Controlling the PC Sample-based Profiling Extension.

RTYNSW

RWSVYM

IYSWSD

IMXCMM

RPLPCY

IWRNBL

IHHHDQ

RMPZSB

Recently-executed means any instruction executed between the current and previous successful Capture events.

The sampled recently-executed instruction address and context values follow the same rules and constraints described by The PC Sample-based Profiling Extension when PMPCSR is read with PMPCSCTL.SS set to 0. For example:

- When any of the following are true, the sampled instruction address and context might be unknown:
- -The PE is in reset state.
- -No branch instruction has retired since the PE left reset state, Debug state, or a state where PC Sample-based Profiling is prohibited.
- -No branch instruction has retired since the previous Capture event.
- -No branch instruction has retired since PMPCSCTL.SS was set to 1.
- When any of the following are true, it is permitted but not required for bits [31:0] of the sampled instruction address to be recorded as 0xFFFF\_FFFF , and for PMPCSR[63:32], PMCID1SR, PMCID2SR, PMVIDSR, PMCCIDSR, and PMVCIDSR to be unchanged:
- -The PE has not retired any branch instruction since leaving a state where PC Sample-based profiling was suspended.
- -The first Capture event after PMPCSCTL.SS was set to 1.

The recently-executed instruction sampled in PMPCSR is captured before PMSSCR\_EL1.{NC, SS} is set to {0, 0}.

For a Capture event triggered by System register write, explicit synchronization is required between observing the Capture event has completed and reading the snapshot registers. That is, for the following sequence, instruction C observes the snapshot registers have been updated by the Capture event, when enabled:

1. An instruction A observes that a Capture event is complete.
2. Software executes a Context synchronization event B in program order after A.
3. An instruction C reads a snapshot register in program order after B.

Example D13-8 Synchronization between Capture event observation and snapshot register reads

The following sequence sets PMSSCR\_EL1.SS to 1 to initiate a Capture event, and polls PMSSCR\_EL1.SS to detect whether the Capture event has completed:

```
; Set PMSSCR_EL1.SS to initiate Capture event request MOV X0, #1 MSR PMSSCR_EL1, X0 loop: ; Test PMSSCR_EL1.SS to check whether the Capture event has completed MRS X0, PMSSCR_EL1 ISB TBNZ X0, #0, loop ; Read snapshot registers
```

When the PE sets PMSSCR\_EL1.{NC, SS} to {0, 0} on a successful Capture event:

- If the PE is in Non-debug state then the PMU\_SNAPSHOT event is generated. This means that the PMU event is generated after any event counter that might be counting the event has been captured.
- If the PE is in Debug state, it is CONSTRAINED UNPREDICTABLE whether the PMU\_SNAPSHOT event is generated.

On a successful Capture event, a BRBE freeze event might occur. See RLBQZR in Branch record buffer operation.

When PMPCSCTL.SS is 1, the architecture does not require any relationship between the PC value captured by PMPCSR and the branches captured in the frozen Branch records.

If a Capture event occurs when prohibited, then:

- PMCCNTSVR\_EL1, PMICNTSVR\_EL1, and PMEVCNTSVR&lt;n&gt;\_EL1 are unchanged.
- The PC sample registers are unchanged.
- PMSSCR\_EL1.{NC, SS} is set to {1, 0} to indicate that a Capture event has completed unsuccessfully.
- Generation of Branch records is unaffected.

## The Performance Monitors Extension D13.9 PMU snapshots

IKGJMV

Accesses to the snapshot registers are not affected by the OS Lock.

ILXYBX

ACapture event can occur when the PE is executing in AArch32 state.

RVLKCZ

The number of implemented PMU event counter snapshot registers, &lt;n&gt;, is IMPLEMENTATION DEFINED, and is the same as the number of implemented PMU event counters.