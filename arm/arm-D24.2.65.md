## D24.2.65 HDBSSPROD\_EL2, Hardware Dirty State Tracking Structure Producer Register

The HDBSSPROD\_EL2 characteristics are:

## Purpose

Allows producer to update write index for HDBSS.

## Configuration

This register is present only when FEAT\_HDBSS is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to HDBSSPROD\_EL2 are UNDEFINED.

## Attributes

HDBSSPROD\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## FSC, bits [31:26]

Fault Status Code.

| FSC      | Meaning                                                      | Applies when            |
|----------|--------------------------------------------------------------|-------------------------|
| 0b000000 | The PE has not experienced any error on writes to the HDBSS. |                         |
| 0b010000 | External Abort on write to HDBSS.                            |                         |
| 0b101000 | Granule Protection Fault on write to HDBSS.                  | FEAT_RME is implemented |

If this field is non-zero then one or more HDBSS writes have experienced a fault since this field was last set to zero, and the associated HDBSS entries have been lost.

All other values are reserved.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [25:19]

Reserved, RES0.

## INDEX, bits [18:0]

This field indicates the index of the HDBSS entry that will be written to next.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing HDBSSPROD\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, HDBSSPROD\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0010 | 0b0011 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_HDBSS) && IsFeatureImplemented(FEAT_AA64)) UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x300]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.HDBSSEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.HDBSSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = HDBSSPROD_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = HDBSSPROD_EL2;
```

MSR HDBSSPROD\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0010 | 0b0011 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_HDBSS) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x300] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.HDBSSEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.HDBSSEn == '0' then
```

```
then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else HDBSSPROD_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then HDBSSPROD_EL2 = X[t, 64];
```