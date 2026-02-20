## D24.2.30 APIBKeyLo\_EL1, Pointer Authentication Key B for Instruction (bits[63:0])

The APIBKeyLo\_EL1 characteristics are:

## Purpose

Holds bits[63:0] of key B used for authentication of instruction pointer values.

Note

The term APIBKey\_EL1 is used to describe the concatenation of APIBKeyHi\_EL1: APIBKeyLo\_EL1.

## Configuration

This register is present only when FEAT\_PAuth is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to APIBKeyLo\_EL1 are UNDEFINED.

## Attributes

APIBKeyLo\_EL1 is a 64-bit register.

## Field descriptions

```
64 bit value, bits[63:0] of the 128 bit pointer authentication key value 63 32 64 bit value, bits[63:0] of the 128 bit pointer authentication key value 31 0
```

## APIBKeyLo, bits [63:0]

64 bit value, bits[63:0] of the 128 bit pointer authentication key value.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing APIBKeyLo\_EL1

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, APIBKeyLo_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0010 | 0b0001 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_PAuth) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.APK == '0' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.APK == '0' then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.APIBKey == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.APK == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = APIBKeyLo_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.APK == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.APK == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = APIBKeyLo_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = APIBKeyLo_EL1;
```

MSR APIBKeyLo\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0010 | 0b0001 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_PAuth) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.APK == '0' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.APK == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.APIBKey == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.APK == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else APIBKeyLo_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.APK == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.APK == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else APIBKeyLo_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then APIBKeyLo_EL1 = X[t, 64];
```