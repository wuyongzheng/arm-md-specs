## D24.2.59 HACDBSCONS\_EL2, Hardware Accelerator for Cleaning Dirty State Consumer Register

The HACDBSCONS\_EL2 characteristics are:

## Purpose

Read index for HACDBS structure.

## Configuration

This register is present only when FEAT\_HACDBS is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to HACDBSCONS\_EL2 are UNDEFINED.

## Attributes

HACDBSCONS\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## ERR\_REASON, bits [63:62]

Reason for HACDBS error.

| ERR_REASON   | Meaning                                                                         |
|--------------|---------------------------------------------------------------------------------|
| 0b00         | The PE has not experienced an error while processing the HACDBS.                |
| 0b01         | STRUCTF - Aread of an entry from the HACDBShas experienced a fault.             |
| 0b10         | IPAF - Astage 2 walk of an IPA from a HACDBSentry has experienced an MMUfault.  |
| 0b11         | IPAHACF - An entry from the HACDBSexperienced an error that is not an MMUfault. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [61:19]

Reserved, RES0.

## INDEX, bits [18:0]

This field indicates the index of the HACDBS entry that will be read from next.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing HACDBSCONS\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, HACDBSCONS\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0010 | 0b0011 | 0b101 |

```
if !(IsFeatureImplemented(FEAT_HACDBS) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x308]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.HACDBSEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.HACDBSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = HACDBSCONS_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = HACDBSCONS_EL2;
```

MSR HACDBSCONS\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0010 | 0b0011 | 0b101 |

```
if !(IsFeatureImplemented(FEAT_HACDBS) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x308] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.HACDBSEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.HACDBSEn == '0' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); else HACDBSCONS_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then HACDBSCONS_EL2 = X[t, 64];
```