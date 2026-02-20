## D24.2.146 PIR\_EL2, Permission Indirection Register 2 (EL2)

The PIR\_EL2 characteristics are:

## Purpose

Stage 1 Permission Indirection Register for privileged access of the EL2 or EL2&amp;0 translation regime.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register is present only when FEAT\_S1PIE is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PIR\_EL2 are UNDEFINED.

## Attributes

PIR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63     | 60 59   | 56 55   | 52 51   | 48 47   | 44 43   | 40 39   | 36    | 35    | 32   |
|--------|---------|---------|---------|---------|---------|---------|-------|-------|------|
| Perm15 | Perm14  | Perm13  | Perm12  | Perm11  | Perm10  |         | Perm9 | Perm8 |      |
| 31     | 28 27   | 24 23   | 20 19   | 16 15   | 12 11   | 8 7     | 4     | 3     | 0    |
| Perm7  | Perm6   | Perm5   | Perm4   |         | Perm3   | Perm2   | Perm1 | Perm0 |      |

## Perm&lt;m&gt; , bits [4m+3:4m], for m = 15 to 0

Represents stage 1 Base Permissions.

| Perm<m>   | Meaning                                                        |
|-----------|----------------------------------------------------------------|
| 0b0000    | No access. Overlay applied.                                    |
| 0b0001    | Read. Overlay applied.                                         |
| 0b0010    | Execute. Overlay applied.                                      |
| 0b0011    | Read and Execute. Overlay applied.                             |
| 0b0100    | Reserved - treated as No access. Overlay applied.              |
| 0b0101    | Read and Write. Overlay applied.                               |
| 0b0110    | Read, Write, and Execute. Overlay applied. WXNcontrol applied. |
| 0b0111    | Read, Write, and Execute. Overlay applied.                     |
| 0b1000    | Read. Overlay not applied.                                     |
| 0b1001    | Read, GCS Read, and GCS Write. Overlay not applied.            |
| 0b1010    | Read and Execute. Overlay not applied.                         |
| 0b1011    | Reserved - treated as No access. Overlay not applied.          |
| 0b1100    | Read and Write. Overlay not applied.                           |
| 0b1101    | Reserved - treated as No access. Overlay not applied.          |
| 0b1110    | Read, Write, and Execute. Overlay not applied.                 |

| Perm<m>   | Meaning                                               |
|-----------|-------------------------------------------------------|
| 0b1111    | Reserved - treated as No access. Overlay not applied. |

This field is permitted to be cached in a TLB.

When stage 1 Indirect Permission mechanism is disabled, this register is ignored.

Unless otherwise specified, the WXN control is not applied.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing PIR\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name PIR\_EL2 or PIR\_EL1 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, PIR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0010 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_S1PIE) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.PIEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.PIEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PIR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = PIR_EL2;
```

MSR PIR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0010 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_S1PIE) && IsFeatureImplemented(FEAT_AA64)) UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.PIEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.PIEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PIR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then PIR_EL2 = X[t, 64];
```

MRS &lt;Xt&gt;, PIR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0010 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_S1PIE) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.PIEn == '0' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TRVM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.nPIR_EL1 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.PIEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x2A0]; else X[t, 64] = PIR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.PIEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.PIEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = PIR_EL2; else
```

```
then
```

```
X[t, 64] = PIR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = PIR_EL1;
```

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0010 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_S1PIE) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.PIEn == '0' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TVM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.nPIR_EL1 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.PIEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x2A0] = X[t, 64]; else PIR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.PIEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.PIEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then PIR_EL2 = X[t, 64]; else PIR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then PIR_EL1 = X[t, 64];
```