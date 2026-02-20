## D24.2.88 ID\_AA64MMFR0\_EL1, AArch64 Memory Model Feature Register 0

The ID\_AA64MMFR0\_EL1 characteristics are:

## Purpose

Provides information about the implemented memory model and memory management support in AArch64 state.

For general information about the interpretation of the ID registers, see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_AA64MMFR0\_EL1 are UNDEFINED.

## Attributes

ID\_AA64MMFR0\_EL1 is a 64-bit register.

## Field descriptions

| 63     | 60 59   | 56 55   |           | 48 47   | 44 43    | 40 39   | 36 35     |           | 32      |
|--------|---------|---------|-----------|---------|----------|---------|-----------|-----------|---------|
| ECV    | FGT     |         | RES0      | ExS     | TGran4_2 |         | TGran64_2 | TGran16_2 |         |
| 31     | 28 27   | 24 23   | 20 19     | 16 15   | 12 11    | 8 7     | 4         | 3         | 0       |
| TGran4 | TGran64 | TGran16 | BigEndEL0 |         | SNSMem   | BigEnd  | ASIDBits  |           | PARange |

## ECV, bits [63:60]

Indicates presence of Enhanced Counter Virtualization.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| ECV    | Meaning                                                                                                                                                                                                                                                                              |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | Enhanced Counter Virtualization is not implemented.                                                                                                                                                                                                                                  |
| 0b0001 | Enhanced Counter Virtualization is implemented. Supports CNTHCTL_EL2.{EL1TVT, EL1TVCT, EL1NVPCT, EL1NVVCT, EVNTIS}, CNTKCTL_EL1.EVNTIS, CNTPCTSS_EL0 counter views, and CNTVCTSS_EL0 counter views. Extends the PMSCR_EL1.PCT, PMSCR_EL2.PCT, TRFCR_EL1.TS, and TRFCR_EL2.TS fields. |
| 0b0010 | As 0b0001 , and the CNTPOFF_EL2 register and the CNTHCTL_EL2.ECV and SCR_EL3.ECVEn fields are implemented.                                                                                                                                                                           |

All other values are reserved.

FEAT\_ECV implements the functionality identified by the value 0b0001 .

FEAT\_ECV\_POFF implements the functionality identified by the value 0b0010 .

From Armv8.6, the value 0b0000 is not permitted.

Access to this field is RO.

## FGT, bits [59:56]

Indicates presence of the Fine-Grained Trap controls.

## The value of this field is an IMPLEMENTATION DEFINED choice of:

| FGT    | Meaning                                                                                                                                                                                                                                                                                                                                      |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | Fine-grained trap controls are not implemented.                                                                                                                                                                                                                                                                                              |
| 0b0001 | Fine-grained trap controls are implemented. Supports: • If EL2 is implemented, the HAFGRTR_EL2, HDFGRTR_EL2, HDFGWTR_EL2, HFGRTR_EL2, HFGITR_EL2 and HFGWTR_EL2 registers, and their associated traps. • If EL2 is implemented, MDCR_EL2.TDCC. • If EL3 is implemented, MDCR_EL3.TDCC. • If both EL2 and EL3 are implemented, SCR_EL3.FGTEn. |
| 0b0010 | As 0b0001 , and also includes support for: • If EL2 is implemented, the HDFGRTR2_EL2, HDFGWTR2_EL2, HFGITR2_EL2, HFGRTR2_EL2, and HFGWTR2_EL2 registers, and their associated traps. • If both EL2 and EL3 are implemented, SCR_EL3.FGTEn2.                                                                                                  |

All other values are reserved.

FEAT\_FGT implements the functionality identified by the value 0b0001 .

FEAT\_FGT2 implements the functionality identified by the value 0b0010 .

From Armv8.6, the value 0b0000 is not permitted.

From Armv8.9, the value 0b0001 is not permitted.

Access to this field is RO.

## Bits [55:48]

Reserved, RES0.

## ExS, bits [47:44]

Indicates support for disabling context synchronizing exception entry and exit.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| ExS    | Meaning                                                             |
|--------|---------------------------------------------------------------------|
| 0b0000 | All exception entries and exits are context synchronization events. |
| 0b0001 | Non-context synchronizing exception entry and exit are supported.   |

All other values are reserved.

FEAT\_ExS implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## TGran4\_2, bits [43:40]

Indicates support for 4KB memory granule size at stage 2.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TGran4_2   | Meaning                                                                                          | Applies when             |
|------------|--------------------------------------------------------------------------------------------------|--------------------------|
| 0b0000     | Support for 4KB granule at stage 2 is identified in the ID_AA64MMFR0_EL1.TGran4 field.           |                          |
| 0b0001     | 4KB granule not supported at stage 2.                                                            |                          |
| 0b0010     | 4KB granule supported at stage 2.                                                                |                          |
| 0b0011     | 4KB granule at stage 2 supports 52-bit input addresses and can describe 52-bit output addresses. | FEAT_LPA2 is implemented |

All other values are reserved.

If EL2 is not implemented, this field is 0b0000 . Otherwise, the value 0b0000 is deprecated.

Note

This field does not follow the standard ID scheme. See Alternative ID scheme used for ID\_AA64MMFR0\_EL1 stage 2 granule sizes for more information.

Access to this field is RO.

## TGran64\_2, bits [39:36]

Indicates support for 64KB memory granule size at stage 2.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TGran64_2   | Meaning                                                                                  |
|-------------|------------------------------------------------------------------------------------------|
| 0b0000      | Support for 64KB granule at stage 2 is identified in the ID_AA64MMFR0_EL1.TGran64 field. |
| 0b0001      | 64KB granule not supported at stage 2.                                                   |
| 0b0010      | 64KB granule supported at stage 2.                                                       |

All other values are reserved.

If EL2 is not implemented, this field is 0b0000 . Otherwise, the value 0b0000 is deprecated.

Note

This field does not follow the standard ID scheme. See Alternative ID scheme used for ID\_AA64MMFR0\_EL1 stage 2 granule sizes for more information.

Access to this field is RO.

## TGran16\_2, bits [35:32]

Indicates support for 16KB memory granule size at stage 2.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TGran16_2   | Meaning                                                                                           | Applies when             |
|-------------|---------------------------------------------------------------------------------------------------|--------------------------|
| 0b0000      | Support for 16KB granule at stage 2 is identified in the ID_AA64MMFR0_EL1.TGran16 field.          |                          |
| 0b0001      | 16KB granule not supported at stage 2.                                                            |                          |
| 0b0010      | 16KB granule supported at stage 2.                                                                |                          |
| 0b0011      | 16KB granule at stage 2 supports 52-bit input addresses and can describe 52-bit output addresses. | FEAT_LPA2 is implemented |

All other values are reserved.

If EL2 is not implemented, this field is 0b0000 . Otherwise, the value 0b0000 is deprecated.

Note

This field does not follow the standard ID scheme. See Alternative ID scheme used for ID\_AA64MMFR0\_EL1 stage 2 granule sizes for more information.

Access to this field is RO.

## TGran4, bits [31:28]

Indicates support for 4KB memory translation granule size.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TGran4   | Meaning                                                                               | Applies when             |
|----------|---------------------------------------------------------------------------------------|--------------------------|
| 0b0000   | 4KB granule supported.                                                                |                          |
| 0b0001   | 4KB granule supports 52-bit input addresses and can describe 52-bit output addresses. | FEAT_LPA2 is implemented |
| 0b1111   | 4KB granule not supported.                                                            |                          |

All other values are reserved.

Access to this field is RO.

## TGran64, bits [27:24]

Indicates support for 64KB memory translation granule size.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TGran64   | Meaning                     |
|-----------|-----------------------------|
| 0b0000    | 64KB granule supported.     |
| 0b1111    | 64KB granule not supported. |

All other values are reserved.

Access to this field is RO.

## TGran16, bits [23:20]

Indicates support for 16KB memory translation granule size.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TGran16   | Meaning                                                                                | Applies when             |
|-----------|----------------------------------------------------------------------------------------|--------------------------|
| 0b0000    | 16KB granule not supported.                                                            |                          |
| 0b0001    | 16KB granule supported.                                                                |                          |
| 0b0010    | 16KB granule supports 52-bit input addresses and can describe 52-bit output addresses. | FEAT_LPA2 is implemented |

All other values are reserved.

Access to this field is RO.

## BigEndEL0, bits [19:16]

Indicates support for mixed-endian at EL0 only.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| BigEndEL0   | Meaning                                                                  |
|-------------|--------------------------------------------------------------------------|
| 0b0000      | No mixed-endian support at EL0. The SCTLR_EL1.E0E bit has a fixed value. |
| 0b0001      | Mixed-endian support at EL0. The SCTLR_EL1.E0E bit can be configured.    |

FEAT\_MixedEndEL0 implements the functionality identified by the value 0b0001 .

All other values are reserved.

This field is invalid and is RES0 if ID\_AA64MMFR0\_EL1.BigEnd is not 0b0000 .

Access to this field is RO.

## SNSMem, bits [15:12]

Indicates support for a distinction between Secure and Non-secure Memory.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SNSMem   | Meaning                                                              |
|----------|----------------------------------------------------------------------|
| 0b0000   | Does not support a distinction between Secure and Non-secure Memory. |
| 0b0001   | Does support a distinction between Secure and Non-secure Memory.     |

| Note                                                      |
|-----------------------------------------------------------|
| If EL3 is implemented, the value 0b0000 is not permitted. |

All other values are reserved.

Access to this field is RO.

## BigEnd, bits [11:8]

Indicates support for mixed-endian configuration.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| BigEnd   | Meaning                                                                                                                                         |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000   | No mixed-endian support. The SCTLR_ELx.EE bits have a fixed value. See the BigEndEL0 field, bits[19:16], for whether EL0 supports mixed-endian. |
| 0b0001   | Mixed-endian support. The SCTLR_ELx.EE and SCTLR_EL1.E0E bits can be configured.                                                                |

FEAT\_MixedEnd implements the functionality identified by the value 0b0001 .

If this field is 0b0001 , FEAT\_MixedEndEL0 is also implemented.

All other values are reserved.

Access to this field is RO.

## ASIDBits, bits [7:4]

Number of ASID bits.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| ASIDBits   | Meaning   |
|------------|-----------|
| 0b0000     | 8 bits.   |
| 0b0010     | 16 bits.  |

All other values are reserved.

Access to this field is RO.

## PARange, bits [3:0]

Physical Address range supported.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| PARange   | Meaning         | Applies when            |
|-----------|-----------------|-------------------------|
| 0b0000    | 32 bits, 4GB.   |                         |
| 0b0001    | 36 bits, 64GB.  |                         |
| 0b0010    | 40 bits, 1TB.   |                         |
| 0b0011    | 42 bits, 4TB.   |                         |
| 0b0100    | 44 bits, 16TB.  |                         |
| 0b0101    | 48 bits, 256TB. |                         |
| 0b0110    | 52 bits, 4PB.   | FEAT_LPA is implemented |

0b0111

All other values are reserved.

Access to this field is RO.

## Accessing ID\_AA64MMFR0\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ID\_AA64MMFR0\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0111 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64MMFR0_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64MMFR0_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_AA64MMFR0_EL1;
```

56 bits, 64PB.

FEAT\_D128 is implemented