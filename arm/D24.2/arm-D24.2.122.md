## D24.2.122 LORN\_EL1, LORegion Number (EL1)

The LORN\_EL1 characteristics are:

## Purpose

Holds the number of the LORegion described in the current LORegion descriptor selected by LORC\_EL1.DS.

## Configuration

This register is RES0 if any of the following apply:

- No LORegion descriptors are supported by the PE.
- LORC\_EL1.DS points to a LORegion that is not supported by the PE.

This register is present only when FEAT\_LOR is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to LORN\_EL1 are UNDEFINED.

## Attributes

LORN\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

Any of the fields in this register are permitted to be cached in a TLB.

## Bits [63:8]

Reserved, RES0.

## Num, bits [7:0]

Number of the LORegion described in the current LORegion descriptor selected by LORC\_EL1.DS.

The maximum number of LORegions supported by the PE is 256. If the maximum number is less than 256, then bits[8:N] are RES0, where N is (Log2(Number of LORegions supported by the PE)).

If this field points to a LORegion that is not supported by the PE, then the current LORegion descriptor does not match any LORegion.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing LORN\_EL1

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, LORN_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0100 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_LOR) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TLOR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.NS == '0' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TLOR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.LORN_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TLOR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = LORN_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TLOR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TLOR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = LORN_EL1; elsif PSTATE.EL == EL3 then if SCR_EL3.NS == '0' then UNDEFINED; else X[t, 64] = LORN_EL1;
```

MSR LORN\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0100 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_LOR) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TLOR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.NS == '0' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TLOR == '1' then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.LORN_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TLOR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else LORN_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TLOR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TLOR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else LORN_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then if SCR_EL3.NS == '0' then UNDEFINED; else LORN_EL1 = X[t, 64];
```