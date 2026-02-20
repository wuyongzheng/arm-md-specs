## D24.2.166 S2PIR\_EL2, Stage 2 Permission Indirection Register (EL2)

The S2PIR\_EL2 characteristics are:

## Purpose

Stage 2 Permission Indirection Register for EL1&amp;0 translation regime.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register is present only when FEAT\_S2PIE is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to S2PIR\_EL2 are UNDEFINED.

## Attributes

S2PIR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63     | 60 59   | 56 55   | 52 51   | 48 47   | 44 43   | 40 39   | 36 35   |       | 32   |
|--------|---------|---------|---------|---------|---------|---------|---------|-------|------|
| Perm15 | Perm14  | Perm13  | Perm12  | Perm11  | Perm10  |         | Perm9   | Perm8 |      |
| 31     | 28 27   | 24 23   | 20 19   | 16 15   | 12 11   | 8 7     | 4       | 3     | 0    |
| Perm7  | Perm6   | Perm5   | Perm4   |         | Perm3   | Perm2   | Perm1   | Perm0 |      |

## Perm&lt;m&gt; , bits [4m+3:4m], for m = 15 to 0

Represents stage 2 Base Permissions.

| Perm<m>   | Meaning                          |
|-----------|----------------------------------|
| 0b0000    | No Access.                       |
| 0b0001    | Reserved - treated as No Access. |
| 0b0010    | MRO.                             |
| 0b0011    | MRO-TL1.                         |
| 0b0100    | WO.                              |
| 0b0101    | Reserved - treated as No Access. |
| 0b0110    | MRO-TL0.                         |
| 0b0111    | MRO-TL01.                        |
| 0b1000    | RO.                              |
| 0b1001    | RO+uX.                           |
| 0b1010    | RO+pX.                           |
| 0b1011    | RO+puX.                          |
| 0b1100    | RW.                              |
| 0b1101    | RW+uX.                           |
| 0b1110    | RW+pX.                           |
| 0b1111    | RW+puX.                          |

| Perm<m>   | Meaning   |
|-----------|-----------|

This field is permitted to be cached in a TLB.

When stage 2 Indirect Permission mechanism is disabled, the contents of this register are ignored.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing S2PIR\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, S2PIR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0010 | 0b101 |

```
if !(IsFeatureImplemented(FEAT_S2PIE) && IsFeatureImplemented(FEAT_AA64)) UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x2B0]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.PIEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.PIEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = S2PIR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = S2PIR_EL2;
```

MSR S2PIR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0010 | 0b101 |

```
if !(IsFeatureImplemented(FEAT_S2PIE) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then
```

```
then
```

```
if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x2B0] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.PIEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.PIEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else S2PIR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then S2PIR_EL2 = X[t, 64];
```