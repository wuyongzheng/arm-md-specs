## D24.2.120 LOREA\_EL1, LORegion End Address (EL1)

The LOREA\_EL1 characteristics are:

## Purpose

Holds the physical address of the end of the LORegion described in the current LORegion descriptor selected by LORC\_EL1.DS.

## Configuration

This register is RES0 if any of the following apply:

- No LORegion descriptors are supported by the PE.
- LORC\_EL1.DS points to a LORegion that is not supported by the PE.

This register is present only when FEAT\_LOR is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to LOREA\_EL1 are UNDEFINED.

## Attributes

LOREA\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

Any of the fields in this register are permitted to be cached in a TLB.

## Bits [63:56]

Reserved, RES0.

## EA[55:52], bits [55:52]

## When FEAT\_D128 is implemented:

Extension to EA[47:16]. For more information, see EA[47:16].

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

EA[51:48], bits [51:48]

## When FEAT\_LPA is implemented:

Extension to EA[47:16]. For more information, see EA[47:16].

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EA[47:16], bits [47:16]

Bits [47:16] of the end physical address of an LORegion described in the current LORegion descriptor selected by LORC\_EL1.DS. Bits[15:0] of this address are 0xFFFF . For implementations with fewer than 48 bits, the upper bits of this field are RES0.

When FEAT\_LPA is implemented and 52-bit addresses are in use, EA[51:48] form bits [51:48] of the end physical address of the LORegion. Otherwise, when 52-bit addresses are not in use, EA[51:48] is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [15:0]

Reserved, RES0.

## Accessing LOREA\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, LOREA\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0100 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_LOR) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TLOR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.NS == '0' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TLOR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.LOREA_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TLOR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = LOREA_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TLOR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TLOR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else
```

```
X[t, 64] = LOREA_EL1; elsif PSTATE.EL == EL3 then if SCR_EL3.NS == '0' then UNDEFINED; else X[t, 64] = LOREA_EL1;
```

MSR LOREA\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0100 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_LOR) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TLOR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.NS == '0' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TLOR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.LOREA_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TLOR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else LOREA_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TLOR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TLOR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else LOREA_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then if SCR_EL3.NS == '0' then UNDEFINED; else LOREA_EL1 = X[t, 64];
```