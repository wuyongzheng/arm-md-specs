## D24.2.108 ID\_MMFR0\_EL1, AArch32 Memory Model Feature Register 0

The ID\_MMFR0\_EL1 characteristics are:

## Purpose

Provides information about the implemented memory model and memory management support in AArch32 state.

For general information about the interpretation of the ID registers see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

AArch64 System register ID\_MMFR0\_EL1 bits [31:0] are architecturally mapped to AArch32 System register ID\_MMFR0[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_MMFR0\_EL1 are UNDEFINED.

## Attributes

ID\_MMFR0\_EL1 is a 64-bit register.

## Field descriptions

When FEAT\_AA32 is implemented:

<!-- image -->

| 63   |
|------|

## Bits [63:32]

Reserved, RES0.

## InnerShr, bits [31:28]

Innermost Shareability. Indicates the innermost shareability domain implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| InnerShr   | Meaning                                      |
|------------|----------------------------------------------|
| 0b0000     | Implemented as Non-cacheable.                |
| 0b0001     | Implemented with hardware coherency support. |
| 0b1111     | Shareability ignored.                        |

All other values are reserved.

From Armv8 the permitted values are 0b0000 , 0b0001 , and 0b1111 .

This field is valid only if the implementation supports two levels of shareability, as indicated by ID\_MMFR0\_EL1.ShareLvl having the value 0b0001 .

When ID\_MMFR0\_EL1.ShareLvl is zero, this field is UNKNOWN.

Access to this field is RO.

## FCSE, bits [27:24]

Indicates whether the implementation includes the FCSE.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| FCSE   | Meaning           |
|--------|-------------------|
| 0b0000 | Not supported.    |
| 0b0001 | Support for FCSE. |

All other values are reserved.

From Armv8 the only permitted value is 0b0000 .

Access to this field is RO.

## AuxReg, bits [23:20]

Auxiliary Registers. Indicates support for Auxiliary registers.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| AuxReg   | Meaning                                                                                        |
|----------|------------------------------------------------------------------------------------------------|
| 0b0000   | None supported.                                                                                |
| 0b0001   | Support for Auxiliary Control Register only.                                                   |
| 0b0010   | Support for Auxiliary Fault Status Registers (AIFSR and ADFSR) and Auxiliary Control Register. |

All other values are reserved.

From Armv8 the only permitted value is 0b0010 .

Note

Accesses to unimplemented Auxiliary registers are UNDEFINED.

Access to this field is RO.

## TCM, bits [19:16]

Indicates support for TCMs and associated DMAs.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TCM    | Meaning                                    |
|--------|--------------------------------------------|
| 0b0000 | Not supported.                             |
| 0b0001 | Support is IMPLEMENTATION DEFINED.         |
| 0b0010 | Support for TCMonly, Armv6 implementation. |

0b0011

All other values are reserved.

In Armv8-A the only permitted value is 0b0000 .

Access to this field is RO.

## ShareLvl, bits [15:12]

Shareability Levels. Indicates the number of shareability levels implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| ShareLvl   | Meaning                                 |
|------------|-----------------------------------------|
| 0b0000     | One level of shareability implemented.  |
| 0b0001     | Two levels of shareability implemented. |

All other values are reserved.

From Armv8 the only permitted value is 0b0001 .

Access to this field is RO.

## OuterShr, bits [11:8]

Outermost Shareability. Indicates the outermost shareability domain implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| OuterShr   | Meaning                                      |
|------------|----------------------------------------------|
| 0b0000     | Implemented as Non-cacheable.                |
| 0b0001     | Implemented with hardware coherency support. |
| 0b1111     | Shareability ignored.                        |

All other values are reserved.

From Armv8 the permitted values are 0b0000 , 0b0001 , and 0b1111 .

Access to this field is RO.

## PMSA, bits [7:4]

Indicates support for a PMSA.

The value of this field is an IMPLEMENTATION DEFINED choice of:

Support for TCM and DMA, Armv6 implementation.

| PMSA   | Meaning                                                                   |
|--------|---------------------------------------------------------------------------|
| 0b0000 | Not supported.                                                            |
| 0b0001 | Support for IMPLEMENTATION DEFINED PMSA.                                  |
| 0b0010 | Support for PMSAv6, with a Cache Type Register implemented.               |
| 0b0011 | Support for PMSAv7, with support for memory subsections. Armv7-R profile. |

All other values are reserved.

In Armv8-A the only permitted value is 0b0000 .

Access to this field is RO.

## VMSA, bits [3:0]

Indicates support for a VMSA.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| VMSA   | Meaning                                                                                                       |
|--------|---------------------------------------------------------------------------------------------------------------|
| 0b0000 | Not supported.                                                                                                |
| 0b0001 | Support for IMPLEMENTATION DEFINED VMSA.                                                                      |
| 0b0010 | Support for VMSAv6, with Cache and TLB Type Registers implemented.                                            |
| 0b0011 | Support for VMSAv7, with support for remapping and the Access flag. Armv7-A profile.                          |
| 0b0100 | As for 0b0011 , and adds support for the PXNbit in the Short-descriptor translation table format descriptors. |
| 0b0101 | As for 0b0100 , and adds support for the Long-descriptor translation table format.                            |

All other values are reserved.

In Armv8-A the only permitted value is 0b0101 .

Access to this field is RO.

## Otherwise:

<!-- image -->

| 63      | 32      |
|---------|---------|
| UNKNOWN | UNKNOWN |
| 31      | 0       |
| UNKNOWN | UNKNOWN |

## Bits [63:0]

Reserved, UNKNOWN.

## Accessing ID\_MMFR0\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ID\_MMFR0\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0001 | 0b100 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_MMFR0_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_MMFR0_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_MMFR0_EL1;
```