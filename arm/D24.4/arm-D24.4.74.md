## D24.4.74 TRFCR\_EL1, Trace Filter Control Register (EL1)

The TRFCR\_EL1 characteristics are:

## Purpose

Provides EL1 controls for Trace.

## Configuration

AArch64 System register TRFCR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register TRFCR[31:0].

This register is present only when FEAT\_TRF is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to TRFCR\_EL1 are UNDEFINED.

## Attributes

TRFCR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:12]

Reserved, RES0.

## DnVM, bit [11]

## When FEAT\_TRBEv1p1 is implemented and FEAT\_NV is implemented:

Reserved for software use in nested virtualization. See also TRFCR\_EL2.DnVM.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## KE, bit [10]

## When FEAT\_TRBE\_EXC is implemented:

Kernel exception enable for TRBE Profiling exceptions taken to EL1.

| KE   | Meaning                                                                                                                |
|------|------------------------------------------------------------------------------------------------------------------------|
| 0b0  | TRBE Profiling exceptions taken to EL1 are always masked at EL1.                                                       |
| 0b1  | Enabled TRBE Profiling exceptions taken to EL1 are masked at EL1 when PSTATE.PM is 1 and unmasked when PSTATE.PM is 0. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

EE, bits [9:8]

## When FEAT\_TRBE\_EXC is implemented:

Exception Enable.

| EE   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Applies when           |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| 0b00 | Disabled. TRBE Profiling exceptions for EL1 are disabled. All of the following apply: • Unless enabled by a higher Exception level, TRBE Profiling exceptions are not generated. • TRBSR_EL1.IRQ drives the interrupt request signal TRBIRQ . • Accesses to TRBSR_EL1 at EL1 ignore the value of HCR_EL2.NV1.                                                                                                                                                                                   |                        |
| 0b01 | Reserved for software use in nested virtualization. Behaves as 0b00 for the purpose of controlling the TRBE Profiling exception and interrupt request signal TRBIRQ , and as 0b11 for the purpose of accesses to TRBSR_EL1.                                                                                                                                                                                                                                                                     | FEAT_NV is implemented |
| 0b10 | Reserved for software use in nested virtualization. Behaves as 0b11 for the purposes of controlling the TRBE Profiling exception and interrupt request signal TRBIRQ , and accesses to TRBSR_EL1.                                                                                                                                                                                                                                                                                               | FEAT_NV is implemented |
| 0b11 | Enabled. TRBE Profiling exceptions for EL1 are enabled, as follows: • All trace buffer management events are recorded in TRBSR_EL1, unless they are configured to be recorded in TRBSR_EL3 by MDCR_EL3.TRBEE or TRBSR_EL2 by TRFCR_EL2.EE. • TRBE Profiling exceptions are generated and taken to EL1 when unmasked and TRBSR_EL1.IRQ is 1, unless the Effective value of HCR_EL2.TGE is 1, in which case the exception is taken to EL2. • The interrupt request signal TRBIRQ is not asserted. |                        |

For more information on the values reserved for software use in nested virtualization, see TRFCR\_EL2.EE.

If the Effective value of TRFCR\_EL2.EE is 0b00 , then the Effective value of TRFCR\_EL1.EE is 0b00 .

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '00' .

- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [7]

Reserved, RES0.

## TS, bits [6:5]

Timestamp Control. Controls which timebase is used for trace timestamps.

| TS   | Meaning                                                                                                                                                                                                                                                                                                                | Applies when              |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| 0b00 | Reserved for software use in nested virtualization. Behaves as 0b01 . See also TRFCR_EL2.TS,                                                                                                                                                                                                                           | FEAT_NV2p1 is implemented |
| 0b01 | Virtual timestamp. The traced timestamp is the physical counter value minus the value of CNTVOFF_EL2.                                                                                                                                                                                                                  |                           |
| 0b10 | Guest physical timestamp. The traced timestamp is the physical counter value minus a physical offset. If any of the following are true, then the physical offset is zero, otherwise the physical offset is the value of CNTPOFF_EL2: • SCR_EL3.ECVEn == 0. • CNTHCTL_EL2.ECV == 0. • FEAT_ECV_POFF is not implemented. | FEAT_ECV is implemented   |
| 0b11 | Physical timestamp. The traced timestamp is the physical counter value.                                                                                                                                                                                                                                                |                           |

All other values are reserved.

If any of the following are true, then this field is ignored by the PE:

- EL2 is implemented and TRFCR\_EL2.TS is not 0b00 .
- SelfHostedTraceEnabled() == FALSE.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [4]

Reserved, RES0.

## CX, bit [3]

## When FEAT\_NV2p1 is implemented:

Reserved for software use in nested virtualization. See also TRFCR\_EL2.CX.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [2]

Reserved, RES0.

## E1TRE, bit [1]

EL1 Trace Enable.

| E1TRE   | Meaning                     |
|---------|-----------------------------|
| 0b0     | Trace is prohibited at EL1. |
| 0b1     | Trace is allowed at EL1.    |

If any of the following are true, then this field is ignored by the PE:

- SelfHostedTraceEnabled () == FALSE.
- The Effective value of HCR\_EL2.TGE is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## E0TRE, bit [0]

EL0 Trace Enable.

| E0TRE   | Meaning                     |
|---------|-----------------------------|
| 0b0     | Trace is prohibited at EL0. |
| 0b1     | Trace is allowed at EL0.    |

If any of the following are true, then this field is ignored by the PE:

- SelfHostedTraceEnabled () == FALSE.
- The Effective value of HCR\_EL2.TGE is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Accessing TRFCR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, TRFCR_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0010 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_TRF) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TTRF == '1' then UNDEFINED;
```

```
elsif EL2Enabled() && MDCR_EL2.TTRF == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TTRF == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x880]; else X[t, 64] = TRFCR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TTRF == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TTRF == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = TRFCR_EL2; else X[t, 64] = TRFCR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = TRFCR_EL1;
```

MSR TRFCR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0010 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_TRF) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TTRF == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRFCR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TTRF == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TTRF == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x880] = X[t, 64]; else TRFCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TTRF == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TTRF == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18);
```

```
elsif ELIsInHost(EL2) then TRFCR_EL2 = X[t, 64]; else TRFCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then TRFCR_EL1 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, TRFCR\_EL12

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0001 | 0b0010 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_TRF) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then X[t, 64] = NVMem[0x880]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TTRF == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TTRF == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = TRFCR_EL1; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, 64] = TRFCR_EL1; else UNDEFINED;
```

When FEAT\_VHE is implemented MSR TRFCR\_EL12, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0001 | 0b0010 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_TRF) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then NVMem[0x880] = X[t, 64];
```

```
elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TTRF == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TTRF == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else TRFCR_EL1 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then TRFCR_EL1 = X[t, 64]; else UNDEFINED;
```
