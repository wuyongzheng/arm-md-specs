## D24.2.41 CSSELR\_EL1, Cache Size Selection Register

The CSSELR\_EL1 characteristics are:

## Purpose

Selects the current Cache Size ID Register, CCSIDR\_EL1, by specifying the required cache level and the cache type (either instruction or data cache).

## Configuration

AArch64 System register CSSELR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register CSSELR[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to CSSELR\_EL1 are UNDEFINED.

## Attributes

CSSELR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   |      |
|------|------|
|      | RES0 |
| 31   |      |
|      | RES0 |

## Bits [63:5]

Reserved, RES0.

## TnD, bit [4]

## When FEAT\_MTE2 is implemented:

Allocation Tag not Data bit.

| TnD   | Meaning                             |
|-------|-------------------------------------|
| 0b0   | Data, Instruction or Unified cache. |
| 0b1   | Separate Allocation Tag cache.      |

When CSSELR\_EL1.InD == 1, this bit is RES0.

If CSSELR\_EL1.{TnD, Level, InD} is programmed to a cache level that is not implemented, then the value for this field on a read of CSSELR\_EL1 is UNKNOWN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Level, bits [3:1]

Cache level of required cache.

All other values are reserved.

If CSSELR\_EL1.{TnD, Level, InD} is programmed to a cache level that is not implemented, then the value for this field on a read of CSSELR\_EL1 is UNKNOWN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## InD, bit [0]

Instruction not Data bit.

| Level   | Meaning        |
|---------|----------------|
| 0b000   | Level 1 cache. |
| 0b001   | Level 2 cache. |
| 0b010   | Level 3 cache. |
| 0b011   | Level 4 cache. |
| 0b100   | Level 5 cache. |
| 0b101   | Level 6 cache. |
| 0b110   | Level 7 cache. |

| InD   | Meaning                |
|-------|------------------------|
| 0b0   | Data or unified cache. |
| 0b1   | Instruction cache.     |

If CSSELR\_EL1.{TnD, Level, InD} is programmed to a cache level that is not implemented, then a read of CSSELR\_EL1 is CONSTRAINED UNPREDICTABLE, and returns UNKNOWN values for CSSELR\_EL1.{Level, InD}.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CSSELR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, CSSELR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b010 | 0b0000 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TID2 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_EVT) && HCR_EL2.TID4 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.CSSELR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else X[t, 64] = CSSELR_EL1; elsif PSTATE.EL == EL2 then X[t, 64] = CSSELR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = CSSELR_EL1;
```

MSR CSSELR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b010 | 0b0000 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TID2 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_EVT) && HCR_EL2.TID4 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.CSSELR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else CSSELR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then CSSELR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then CSSELR_EL1 = X[t, 64];
```