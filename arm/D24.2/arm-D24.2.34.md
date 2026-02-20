## D24.2.34 CONTEXTIDR\_EL1, Context ID Register (EL1)

The CONTEXTIDR\_EL1 characteristics are:

## Purpose

Identifies the current Process Identifier.

The value of the whole of this register is called the Context ID and is used by:

- The debug logic, for Linked and Unlinked Context ID matching.
- The trace logic, to identify the current process.

The significance of this register is for debug and trace use only.

## Configuration

AArch64 System register CONTEXTIDR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register CONTEXTIDR[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to CONTEXTIDR\_EL1 are UNDEFINED.

## Attributes

CONTEXTIDR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63     | 32   |
|--------|------|
| RES0   |      |
| 31     | 0    |
| PROCID |      |

## Bits [63:32]

Reserved, RES0.

## PROCID, bits [31:0]

Process Identifier. This field must be programmed with a unique value that identifies the current process.

Note

In AArch32 state, when TTBCR.EAE is set to 0, CONTEXTIDR.ASID holds the ASID.

In AArch64 state, CONTEXTIDR\_EL1 is independent of the ASID, and for the EL1&amp;0 translation regime either TTBR0\_EL1 or TTBR1\_EL1 holds the ASID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CONTEXTIDR\_EL1

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL3 using the accessor name CONTEXTIDR\_EL1 or CONTEXTIDR\_EL12 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

## MRS &lt;Xt&gt;, CONTEXTIDR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1101 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TRVM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.CONTEXTIDR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x108]; else X[t, 64] = CONTEXTIDR_EL1; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then X[t, 64] = CONTEXTIDR_EL2; else X[t, 64] = CONTEXTIDR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = CONTEXTIDR_EL1;
```

MSR CONTEXTIDR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1101 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TVM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.CONTEXTIDR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x108] = X[t, 64]; else CONTEXTIDR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then CONTEXTIDR_EL2 = X[t, 64]; else CONTEXTIDR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then CONTEXTIDR_EL1 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, CONTEXTIDR\_EL12

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b1101 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then X[t, 64] = NVMem[0x108]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then X[t, 64] = CONTEXTIDR_EL1; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, 64] = CONTEXTIDR_EL1; else UNDEFINED;
```

When FEAT\_VHE is implemented MSR CONTEXTIDR\_EL12, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b1101 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then NVMem[0x108] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then CONTEXTIDR_EL1 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then CONTEXTIDR_EL1 = X[t, 64]; else UNDEFINED;
```