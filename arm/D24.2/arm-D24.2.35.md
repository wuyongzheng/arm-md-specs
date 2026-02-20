## D24.2.35 CONTEXTIDR\_EL2, Context ID Register (EL2)

The CONTEXTIDR\_EL2 characteristics are:

## Purpose

Identifies the current Process Identifier for EL2.

The value of the whole of this register is called the Context ID and is used by:

- The debug logic, for Linked and Unlinked Context ID matching.
- The trace logic, to identify the current process.

The significance of this register is for debug and trace use only.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register has no effect if EL2 is not enabled in the current Security state.

This register is present only when FEAT\_Debugv8p1 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to CONTEXTIDR\_EL2 are UNDEFINED.

## Attributes

CONTEXTIDR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   |        | 32   |
|------|--------|------|
|      | RES0   |      |
| 31   |        | 0    |
|      | PROCID |      |

## Bits [63:32]

Reserved, RES0.

## PROCID, bits [31:0]

Process Identifier. This field must be programmed with a unique value that identifies the current process.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CONTEXTIDR\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name CONTEXTIDR\_EL2 or CONTEXTIDR\_EL1 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, CONTEXTIDR_EL2
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1101 | 0b0000 | 0b001 |

if !(IsFeatureImplemented(FEAT\_Debugv8p1) &amp;&amp; IsFeatureImplemented(FEAT\_AA64)) then if EffectiveHCR\_EL2\_NVx() IN {'xx1'} then

AArch64.SystemAccessTrap(EL2, 0x18);

UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then else UNDEFINED; elsif PSTATE.EL == EL2 then X[t, 64] = CONTEXTIDR\_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = CONTEXTIDR\_EL2;

MSR CONTEXTIDR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1101 | 0b0000 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_Debugv8p1) && UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then CONTEXTIDR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then CONTEXTIDR_EL2 = X[t, 64];
```

IsFeatureImplemented(FEAT\_AA64)) then

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, CONTEXTIDR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1101 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TRVM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HFGRTR_EL2.CONTEXTIDR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x108]; else X[t, 64] = CONTEXTIDR_EL1; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then X[t, 64] = CONTEXTIDR_EL2; else X[t, 64] = CONTEXTIDR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = CONTEXTIDR_EL1;
```

When FEAT\_VHE is implemented MSR CONTEXTIDR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1101 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TVM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HFGWTR_EL2.CONTEXTIDR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x108] = X[t, 64]; else CONTEXTIDR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then CONTEXTIDR_EL2 = X[t, 64]; else CONTEXTIDR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then CONTEXTIDR_EL1 = X[t, 64];
```