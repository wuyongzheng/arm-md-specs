## D24.2.121 LORID\_EL1, LORegionID (EL1)

The LORID\_EL1 characteristics are:

## Purpose

Indicates the number of LORegions and LORegion descriptors supported by the PE.

## Configuration

If no LORegion descriptors are implemented, then the registers LORC\_EL1, LORN\_EL1, LOREA\_EL1, and LORSA\_EL1 are RES0.

This register is present only when FEAT\_LOR is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to LORID\_EL1 are UNDEFINED.

## Attributes

LORID\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63       | 63       | 63       | 63    | 63    | 63   | 32   |
|----------|----------|----------|-------|-------|------|------|
| RES0     | RES0     | RES0     |       |       |      |      |
| 31 24 23 | 31 24 23 | 31 24 23 | 16 15 | 16 15 | 8 7  | 0    |
|          | RES0     | LD       |       | RES0  | LR   |      |

## Bits [63:24]

Reserved, RES0.

## LD, bits [23:16]

Number of LORegion descriptors supported by the PE. This is an 8-bit binary number.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| LD           | Meaning                                        |
|--------------|------------------------------------------------|
| 0x00 .. 0xFF | The number of LORegions descriptors supported. |

Access to this field is RO.

## Bits [15:8]

Reserved, RES0.

## LR, bits [7:0]

Number of LORegions supported by the PE. This is an 8-bit binary number.

Note

If LORID\_EL1 indicates that no LORegions are implemented, then LoadLOAcquire and StoreLORelease will behave as LoadAcquire and StoreRelease.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| LR           | Meaning                            |
|--------------|------------------------------------|
| 0x00 .. 0xFF | The number of LORegions supported. |

Access to this field is RO.

## Accessing LORID\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, LORID\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0100 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_LOR) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TLOR == '1' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TLOR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.LORID_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TLOR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = LORID_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TLOR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TLOR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = LORID_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = LORID_EL1;
```