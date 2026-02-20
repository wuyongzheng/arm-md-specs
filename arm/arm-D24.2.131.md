## D24.2.131 MECID\_A1\_EL2, Alternate MECID for EL2&amp;0 translation regimes.

The MECID\_A1\_EL2 characteristics are:

## Purpose

Alternate MECID for EL2&amp;0 accesses translated by TTBR1\_EL2.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register is present only when FEAT\_MEC is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to MECID\_A1\_EL2 are UNDEFINED.

## Attributes

MECID\_A1\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63       |       | 32   |
|----------|-------|------|
| RES0     |       |      |
| 31 16 15 |       | 0    |
| RES0     | MECID |      |

## Bits [63:16]

Reserved, RES0.

## MECID, bits [15:0]

If MECIDWidth is less than 16 bits, bits[15:MECIDWidth] are RES0.

Note

MECIDWidth is defined in MECIDR\_EL2.MECIDWidthm1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing MECID\_A1\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, MECID\_A1\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b1000 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_MEC) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then if !IsCurrentSecurityState(SS_Realm) then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.MECEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.MECEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MECID_A1_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = MECID_A1_EL2;
```

MSR MECID\_A1\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b1000 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_MEC) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then if !IsCurrentSecurityState(SS_Realm) then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.MECEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.MECEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else MECID_A1_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then MECID_A1_EL2 = X[t, 64];
```