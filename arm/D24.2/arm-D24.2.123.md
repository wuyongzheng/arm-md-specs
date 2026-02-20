## D24.2.123 LORSA\_EL1, LORegion Start Address (EL1)

The LORSA\_EL1 characteristics are:

## Purpose

Indicates whether the current LORegion descriptor selected by LORC\_EL1.DS is enabled, and holds the physical address of the start of the LORegion.

## Configuration

This register is RES0 if any of the following apply:

- No LORegion descriptors are supported by the PE.
- LORC\_EL1.DS points to a LORegion that is not supported by the PE.

This register is present only when FEAT\_LOR is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to LORSA\_EL1 are UNDEFINED.

## Attributes

LORSA\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

Any of the fields in this register are permitted to be cached in a TLB.

## Bits [63:56]

Reserved, RES0.

SA, bits [55:16]

When FEAT\_D128 is implemented:

<!-- image -->

## SA, bits [39:0]

Bits [55:16] of the start physical address of the LORegion described in the current LORegion descriptor selected by LORC\_EL1.DS.

Bits[15:0] of this address are 0x0000 .

For implementations with fewer than 56 physical address bits, the corresponding upper bits of this field are RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When FEAT\_LPA is implemented and FEAT\_D128 is not implemented:

<!-- image -->

## Bits [39:36]

Reserved, RES0.

## SA, bits [35:0]

Bits [51:16] of the start physical address of the LORegion described in the current LORegion descriptor selected by LORC\_EL1.DS.

Bits[15:0] of this address are 0x0000 .

For implementations with fewer than 52 physical address bits, the corresponding upper bits of this field are RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When FEAT\_LPA is not implemented:

<!-- image -->

## Bits [39:32]

Reserved, RES0.

## SA, bits [31:0]

Bits [47:16] of the start physical address of the LORegion described in the current LORegion descriptor selected by LORC\_EL1.DS.

Bits[15:0] of this address are 0x0000 .

For implementations with fewer than 48 physical address bits, the corresponding upper bits of this field are RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [15:1]

Reserved, RES0.

## Valid, bit [0]

Indicates whether the current LORegion descriptor is enabled.

| Valid   | Meaning                          |
|---------|----------------------------------|
| 0b0     | LORegion descriptor is disabled. |
| 0b1     | LORegion descriptor is enabled.  |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Accessing LORSA\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, LORSA\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0100 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_LOR) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TLOR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.NS == '0' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TLOR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.LORSA_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TLOR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = LORSA_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TLOR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TLOR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = LORSA_EL1; elsif PSTATE.EL == EL3 then
```

```
if SCR_EL3.NS == '0' then UNDEFINED; else X[t, 64] = LORSA_EL1;
```

MSR LORSA\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0100 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_LOR) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TLOR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.NS == '0' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TLOR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.LORSA_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TLOR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else LORSA_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TLOR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TLOR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else LORSA_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then if SCR_EL3.NS == '0' then UNDEFINED; else LORSA_EL1 = X[t, 64];
```