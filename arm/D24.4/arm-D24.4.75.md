## D24.4.75 TRFCR\_EL2, Trace Filter Control Register (EL2)

The TRFCR\_EL2 characteristics are:

## Purpose

Provides EL2 controls for Trace.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

AArch64 System register TRFCR\_EL2 bits [31:0] are architecturally mapped to AArch32 System register HTRFCR[31:0].

This register is present only when FEAT\_TRF is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to TRFCR\_EL2 are UNDEFINED.

## Attributes

TRFCR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:12]

Reserved, RES0.

DnVM, bit [11]

## When FEAT\_TRBEv1p1 is implemented:

Disable use of physical address trace buffer pointers.

| DnVM   | Meaning                                                                                                 |
|--------|---------------------------------------------------------------------------------------------------------|
| 0b0    | Use of physical address trace buffer pointers is permitted.                                             |
| 0b1    | Use of physical address trace buffer pointers is disabled. The PE behaves as if TRBLIMITR_EL1.nVM is 0. |

If EL2 is disabled in the owning Security state, or the trace buffer owning Exception level is EL2, then the Effective value of this field is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## KE, bit [10]

## When FEAT\_TRBE\_EXC is implemented:

Kernel exception enable for TRBE Profiling exceptions taken to EL2.

| KE   | Meaning                                                                                                                |
|------|------------------------------------------------------------------------------------------------------------------------|
| 0b0  | TRBE Profiling exceptions taken to EL2 are always masked at EL2.                                                       |
| 0b1  | Enabled TRBE Profiling exceptions taken to EL2 are masked at EL2 when PSTATE.PM is 1 and unmasked when PSTATE.PM is 0. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

EE, bits [9:8]

## When FEAT\_TRBE\_EXC is implemented:

Exception Enable.

| EE   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00 | Disabled. TRBE Profiling exceptions for EL2 and EL1 are disabled. All of the following apply: • No trace buffer management events are recorded in TRBSR_EL2. • Unless enabled by a higher Exception level, TRBE Profiling exceptions are not generated. • TRBSR_EL1.IRQ drives the interrupt request signal TRBIRQ . • Accesses to TRBSR_EL1 at EL1 ignore the value of HCR_EL2.NV1 and accesses to TRBSR_EL1 at EL2 ignore the value of HCR_EL2.E2H. |
| 0b01 | Delegated. TRBE Profiling exceptions for EL2 are disabled, but might be enabled for EL1 by TRFCR_EL1.EE. All of the following apply: • No trace buffer management events are recorded in TRBSR_EL2. • TRBSR_EL2.IRQ is ignored and TRBE Profiling exceptions are not taken to EL2, other than the case when the Effective value of HCR_EL2.TGE is 1.                                                                                                  |

| EE   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b10 | Enabled. TRBE Profiling exceptions for EL2 are enabled for trace buffer management events targeting EL2, as follows: • Trace buffer management events due to a fault on a write to the trace buffer that would generate a Data Abort exception taken to EL2 if generated by a store instruction executed at the owning Exception level are recorded in TRBSR_EL2, unless they are configured to be recorded in TRBSR_EL3 by MDCR_EL3.TRBEE. If the trace buffer owning Exception level is EL2, then this means any fault on a write to the trace buffer. If the trace buffer owning Exception level is EL1, then this means any of the following faults on a write to the trace buffer: • Stage 2 faults. • If HCR_EL2.TEA is 1, synchronous External aborts. • If HCR_EL2.GPF is 1, Granule Protection Faults (GPFs). • Trace buffer management events due to Granule Protection Check faults other than GPFs on a write to the trace buffer are recorded in TRBSR_EL2, unless they are configured to be recorded in TRBSR_EL3 by MDCR_EL3.TRBEE. • TRBE Profiling exceptions are generated and taken to EL2 when unmasked and TRBSR_EL2.IRQ is 1. |
| 0b11 | Trap all. TRBE Profiling exceptions for EL2 are enabled for all trace buffer management events, as follows: • All trace buffer management events are recorded in TRBSR_EL2, unless they are configured to be recorded in TRBSR_EL3 by MDCR_EL3.TRBEE. • TRBE Profiling exceptions are generated and taken to EL2 when unmasked and TRBSR_EL2.IRQ is 1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

If the Effective value of MDCR\_EL3.TRBEE is 0b00 , then the Effective value of TRFCR\_EL2.EE is 0b00 . Otherwise, if EL2 is not implemented or the Effective value of SCR\_EL3.{NS, EEL2} is {0, 0}, then the Effective value of TRFCR\_EL2.EE is 0b01 .

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '00' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [7]

Reserved, RES0.

## TS, bits [6:5]

Timestamp Control. Controls which timebase is used for trace timestamps.

| TS   | Meaning                                                                                               | Applies when   |
|------|-------------------------------------------------------------------------------------------------------|----------------|
| 0b00 | Timestamp controlled by TRFCR_EL1.TS or TRFCR.TS.                                                     |                |
| 0b01 | Virtual timestamp. The traced timestamp is the physical counter value minus the value of CNTVOFF_EL2. |                |

| TS   | Meaning                                                                                                                                                                                                                                                                                                           | Applies when            |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| 0b10 | Guest physical timestamp. The traced timestamp is the physical counter value minus a physical offset. If any of the following are true, the physical offset is zero, otherwise the physical offset is the value of CNTPOFF_EL2: • SCR_EL3.ECVEn == 0. • CNTHCTL_EL2.ECV == 0. • FEAT_ECV_POFF is not implemented. | FEAT_ECV is implemented |
| 0b11 | Physical timestamp. The traced timestamp is the physical counter value.                                                                                                                                                                                                                                           |                         |

If SelfHostedTraceEnabled() == FALSE, then this field is ignored by the PE.

The reset behavior of this field is:

- On a Warm reset, this field resets to '00' .

## Bit [4]

Reserved, RES0.

## CX, bit [3]

CONTEXTIDR\_EL2 and VMID trace enable.

| CX   | Meaning                                  |
|------|------------------------------------------|
| 0b0  | CONTEXTIDR_EL2 and VMIDtrace prohibited. |
| 0b1  | CONTEXTIDR_EL2 and VMIDtrace allowed.    |

If SelfHostedTraceEnabled () == FALSE, then this field is ignored by the PE.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Bit [2]

Reserved, RES0.

## E2TRE, bit [1]

EL2 Trace Enable.

| E2TRE   | Meaning                     |
|---------|-----------------------------|
| 0b0     | Trace is prohibited at EL2. |
| 0b1     | Trace is allowed at EL2.    |

If SelfHostedTraceEnabled () == FALSE, then this field is ignored by the PE.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## E0HTRE, bit [0]

EL0 Trace Enable.

| E0HTRE   | Meaning                     |
|----------|-----------------------------|
| 0b0      | Trace is prohibited at EL0. |
| 0b1      | Trace is allowed at EL0.    |

If any of the following are true, then this field is ignored by the PE:

- SelfHostedTraceEnabled () == FALSE.
- The Effective value of HCR\_EL2.TGE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Accessing TRFCR\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRFCR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0010 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_TRF) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TTRF == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TTRF == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = TRFCR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = TRFCR_EL2;
```

MSR TRFCR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0010 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_TRF) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TTRF == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TTRF == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else TRFCR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then TRFCR_EL2 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, TRFCR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0010 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_TRF) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TTRF == '1' then UNDEFINED; elsif EL2Enabled() && MDCR_EL2.TTRF == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TTRF == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x880]; else X[t, 64] = TRFCR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TTRF == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TTRF == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = TRFCR_EL2;
```

<!-- formula-not-decoded -->

When FEAT\_VHE is implemented MSR TRFCR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0010 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_TRF) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TTRF == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGWTR_EL2.TRFCR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TTRF == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TTRF == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x880] = X[t, 64]; else TRFCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TTRF == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TTRF == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then TRFCR_EL2 = X[t, 64]; else TRFCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then TRFCR_EL1 = X[t, 64];
```
