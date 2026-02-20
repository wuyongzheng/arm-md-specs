## D24.2.119 LORC\_EL1, LORegion Control (EL1)

The LORC\_EL1 characteristics are:

## Purpose

Enables and disables LORegions, and selects the current LORegion descriptor.

## Configuration

If no LORegion descriptors are supported by the PE, then this register is RES0.

This register is present only when FEAT\_LOR is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to LORC\_EL1 are UNDEFINED.

## Attributes

LORC\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:10]

Reserved, RES0.

## DS, bits [9:2]

Descriptor Select. Selects the current LORegion descriptor accessed by LORSA\_EL1, LOREA\_EL1, and LORN\_EL1.

If this field points to an LORegion descriptor that is not supported by an implementation, then the registers LORN\_EL1, LOREA\_EL1, and LORSA\_EL1 are RES0.

The number of LORegion descriptors in IMPLEMENTATION DEFINED. The maximum number of LORegion descriptors supported is 256. If the number is less than 256, then bits[63:M+2] are RES0, where M is Log2(Number of LORegion descriptors supported by the implementation).

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [1]

Reserved, RES0.

## EN, bit [0]

Enable. Indicates whether LORegions are enabled.

| EN   | Meaning                                               |
|------|-------------------------------------------------------|
| 0b0  | Disabled. Memory accesses do not match any LORegions. |
| 0b1  | Enabled. Memory accesses may match a LORegion.        |

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Accessing LORC\_EL1

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, LORC_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0100 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_LOR) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TLOR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.NS == '0' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TLOR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.LORC_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TLOR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = LORC_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TLOR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TLOR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = LORC_EL1; elsif PSTATE.EL == EL3 then if SCR_EL3.NS == '0' then UNDEFINED; else X[t, 64] = LORC_EL1;
```

MSR LORC\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0100 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_LOR) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TLOR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.NS == '0' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TLOR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.LORC_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TLOR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else LORC_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TLOR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TLOR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else LORC_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then if SCR_EL3.NS == '0' then UNDEFINED; else LORC_EL1 = X[t, 64];
```