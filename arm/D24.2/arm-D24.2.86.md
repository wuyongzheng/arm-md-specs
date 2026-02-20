## D24.2.86 ID\_AA64ISAR2\_EL1, AArch64 Instruction Set Attribute Register 2

The ID\_AA64ISAR2\_EL1 characteristics are:

## Purpose

Provides information about the features and instructions implemented in AArch64 state.

For general information about the interpretation of the ID registers, see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

Note

Prior to the introduction of the features described by this register, this register was unnamed and reserved, RES0 from EL1, EL2, and EL3.

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_AA64ISAR2\_EL1 are UNDEFINED.

## Attributes

ID\_AA64ISAR2\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63     | 60 59    | 56 55   | 52 51   | 48 47    | 44 43   | 40 39        | 36 35      | 32   |
|--------|----------|---------|---------|----------|---------|--------------|------------|------|
| ATS1A  | LUT      | CSSC    | RPRFM   | PCDPHINT | PRFMSLC | SYSINSTR_128 | SYSREG_128 |      |
| 31     | 28 27    | 24 23   | 20 19   | 16 15    | 12 11   | 8 7          | 4 3        | 0    |
| CLRBHB | PAC_frac | BC      | MOPS    | APA3     | GPA3    | RPRES        |            | WFxT |

## ATS1A, bits [63:60]

Indicates support for address translation instructions, which perform stage 1 address translation for the given virtual address without checking for stage 1 permissions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| ATS1A   | Meaning                                                                               |
|---------|---------------------------------------------------------------------------------------|
| 0b0000  | Address Translate Stage 1 instructions without Permissions Checks are not implemented |
| 0b0001  | Address Translate Stage 1 instructions without Permissions Checks are implemented.    |

All other values are reserved.

Access to this field is RO.

## LUT, bits [59:56]

Indicates support for:

- Advanced SIMD lookup table instructions with 2-bit and 4-bit indices.
- If FEAT\_SVE2 or FEAT\_SME2 is implemented, SVE lookup table instructions with 2-bit and 4-bit indices.

## The value of this field is an IMPLEMENTATION DEFINED choice of:

| LUT    | Meaning                                                                                     |
|--------|---------------------------------------------------------------------------------------------|
| 0b0000 | The specified instructions are not implemented.                                             |
| 0b0001 | Lookup table instructions with 2-bit indices LUTI2 and 4-bit indices LUTI4 are implemented. |

All other values are reserved.

FEAT\_LUT implements the functionality identified by the value 0b0001 .

From Armv9.5, if FEAT\_AdvSIMD is implemented, the value 0b0000 is not permitted.

Access to this field is RO.

## CSSC, bits [55:52]

Indicates support for common short sequence compression instructions.

If FEAT\_CMPBR is implemented, indicates support for compare and branch instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CSSC   | Meaning                                                                                                                                                                                                                                                                                                         |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | Common short sequence compression instructions are not implemented.                                                                                                                                                                                                                                             |
| 0b0001 | The following common short sequence compression instructions are implemented: • 32-bit and 64-bit ABS , CNT , CTZ • 32-bit SMAX , UMAX , SMIN , UMIN (immediate). • 64-bit SMAX , UMAX , SMIN , UMIN (immediate). • 32-bit SMAX , UMAX , SMIN , UMIN (register). • 64-bit SMAX , UMAX , SMIN , UMIN (register). |
| 0b0010 | As 0b0001 , and adds compare and branch instructions: • CBB <cc>. • CB <cc> (immediate), CB <cc> (register). • CBH <cc>.                                                                                                                                                                                        |

All other values are reserved.

FEAT\_CSSC implements the functionality identified by the value 0b0001 .

FEAT\_CMPBR implements the functionality identified by the value 0b0010 .

From Armv9.4, the value 0b0000 is not permitted.

From Armv9.6, the value 0b0001 is not permitted.

Access to this field is RO.

## RPRFM, bits [51:48]

RPRFMhint instruction.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| RPRFM   | Meaning                                                            |
|---------|--------------------------------------------------------------------|
| 0b0000  | RPRFM hint instruction is not implemented and is treated as a NOP. |
| 0b0001  | RPRFM hint instruction is implemented.                             |

All other values are reserved.

FEAT\_RPRFM implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## PCDPHINT, bits [47:44]

Indicates support for producer-consumer data placement hints.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| PCDPHINT   | Meaning                                                      |
|------------|--------------------------------------------------------------|
| 0b0000     | The STSHH and PRFM IR hint instructions are not implemented. |
| 0b0001     | The STSHH and PRFM IR hint instructions are implemented.     |

FEAT\_PCDPHINT implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## PRFMSLC, bits [43:40]

Indicates whether the PRFM and PRFUM instructions support a system level cache option.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| PRFMSLC   | Meaning                                                        |
|-----------|----------------------------------------------------------------|
| 0b0000    | The PRFM and PRFUM instructions do not support the SLC target. |
| 0b0001    | The PRFM and PRFUM instructions support the SLC target.        |

All other values are reserved.

FEAT\_PRFMSLC implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## SYSINSTR\_128, bits [39:36]

SYSINSTR\_128. Indicates support for System instructions that can take 128-bit inputs.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SYSINSTR_128   | Meaning                                                             |
|----------------|---------------------------------------------------------------------|
| 0b0000         | System instructions that can take 128-bit inputs are not supported. |
| 0b0001         | System instructions that can take 128-bit inputs are supported.     |

All other values are reserved.

FEAT\_SYSINSTR128 implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## SYSREG\_128, bits [35:32]

SYSREG\_128. Indicates support for instructions to access 128-bit System Registers.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SYSREG_128   | Meaning                                                            |
|--------------|--------------------------------------------------------------------|
| 0b0000       | Instructions to access 128-bit System Registers are not supported. |
| 0b0001       | Instructions to access 128-bit System Registers are supported.     |

All other values are reserved.

FEAT\_SYSREG128 implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## CLRBHB, bits [31:28]

Indicates support for the CLRBHB instruction in AArch64 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CLRBHB   | Meaning                                |
|----------|----------------------------------------|
| 0b0000   | CLRBHB instruction is not implemented. |
| 0b0001   | CLRBHB instruction is implemented.     |

All other values are reserved.

FEAT\_CLRBHB implements the functionality identified by the value 0b0001 .

From Armv8.9, the value 0b0000 is not permitted.

Access to this field is RO.

## PAC\_frac, bits [27:24]

Indicates which address bit is used to determine the size of the PAC field.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| PAC_frac   | Meaning                                                                                                            |
|------------|--------------------------------------------------------------------------------------------------------------------|
| 0b0000     | The address bit which is used to define the size of the PAC field is dependent on whether address tagging is used. |
| 0b0001     | The address bit which is used to define the size of the PAC field is fixed.                                        |

All other values are reserved.

FEAT\_CONSTPACFIELD implements the functionality identified by the value 0b0001 .

From Armv8.3, the permitted values are 0b0000 and 0b0001 .

Access to this field is RO.

## BC, bits [23:20]

Indicates support for the BC instruction in AArch64 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| BC     | Meaning                            |
|--------|------------------------------------|
| 0b0000 | BC instruction is not implemented. |
| 0b0001 | BC instruction is implemented.     |

All other values are reserved.

FEAT\_HBC implements the functionality identified by the value 0b0001 .

From Armv8.8, the value 0b0000 is not permitted.

Access to this field is RO.

## MOPS, bits [19:16]

Indicates support for the Memory Copy and Memory Set instructions in AArch64 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MOPS   | Meaning                                                                                                                                                                                                 |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | The Memory Copy and Memory Set instructions are not implemented in AArch64 state.                                                                                                                       |
| 0b0001 | The Memory Copy and Memory Set instructions are implemented in AArch64 state with the following exception. If FEAT_MTE is implemented, then SETGP* , SETGM* and SETGE* instructions are also supported. |

All other values are reserved.

FEAT\_MOPS implements the functionality identified by the value 0b0001 .

From Armv8.8, the value 0b0000 is not permitted.

Access to this field is RO.

## APA3, bits [15:12]

Indicates whether the QARMA3 algorithm is implemented in the PE for address authentication in AArch64 state. This applies to all Pointer Authentication instructions other than the PACGA instruction.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| APA3   | Meaning                                                                                                                                                                                                                                                      |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | Address Authentication using the QARMA3algorithm is not implemented.                                                                                                                                                                                         |
| 0b0001 | Address Authentication using the QARMA3algorithm is implemented, FEAT_EPAC and FEAT_PAuth2 are not implemented.                                                                                                                                              |
| 0b0010 | Address Authentication using the QARMA3algorithm is implemented, FEAT_EPAC is implemented, and FEAT_PAuth2 is not implemented.                                                                                                                               |
| 0b0011 | Address Authentication using the QARMA3algorithm is implemented, FEAT_EPAC is not implemented, and FEAT_PAuth2 is implemented.                                                                                                                               |
| 0b0100 | Address Authentication using the QARMA3algorithm is implemented, FEAT_EPAC is not implemented, FEAT_PAuth2 and FEAT_FPAC are implemented.                                                                                                                    |
| 0b0101 | Address Authentication using the QARMA3algorithm is implemented, FEAT_EPAC is not implemented, FEAT_PAuth2, FEAT_FPAC, and FEAT_FPACCOMBINE are implemented.                                                                                                 |
| 0b0110 | Address Authentication using the QARMA3algorithm is implemented, including instructions that allow signing of LR using SP and PC as diversifiers, FEAT_EPAC is not implemented, FEAT_PAuth2, FEAT_FPAC, FEAT_FPACCOMBINE, and FEAT_PAuth_LR are implemented. |

All other values are reserved.

FEAT\_PAuth implements the functionality identified by the value 0b0001 .

FEAT\_EPAC implements the functionality identified by the value 0b0010 .

FEAT\_PAuth2 implements the functionality identified by the value 0b0011 .

FEAT\_FPAC implements the functionality identified by the value 0b0100 .

FEAT\_FPACCOMBINE implements the functionality identified by the value 0b0101 .

FEAT\_PAuth\_LR implements the functionality identified by the value 0b0110 .

When this field is nonzero, FEAT\_PACQARMA3 is implemented.

In Armv8.3, the permitted values are 0b0000 , 0b0001 , 0b0010 , 0b0011 , 0b0100 , and 0b0101 .

From Armv8.6, the permitted values are 0b0000 , 0b0011 , 0b0100 , and 0b0101 .

From Armv9.5, the permitted values are 0b0000 , 0b0011 , 0b0100 , 0b0101 , and 0b0110 .

If the value of ID\_AA64ISAR1\_EL1.API is nonzero, or the value of ID\_AA64ISAR1\_EL1.APA is nonzero, this field must have the value 0b0000 .

Access to this field is RO.

## GPA3, bits [11:8]

Indicates whether the QARMA3 algorithm is implemented in the PE for generic code authentication in AArch64 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| GPA3   | Meaning                                                                                               |
|--------|-------------------------------------------------------------------------------------------------------|
| 0b0000 | Generic Authentication using the QARMA3algorithm is not implemented.                                  |
| 0b0001 | Generic Authentication using the QARMA3algorithm is implemented. This includes the PACGA instruction. |

All other values are reserved.

FEAT\_PACQARMA3 implements the functionality identified by the value 0b0001 .

When this field is nonzero, FEAT\_PACQARMA3 is implemented.

From Armv8.3, the permitted values are 0b0000 and 0b0001 .

If the value of ID\_AA64ISAR1\_EL1.GPI is nonzero, or the value of ID\_AA64ISAR1\_EL1.GPA is nonzero, this field must have the value 0b0000 .

Access to this field is RO.

## RPRES, bits [7:4]

Indicates support for 12 bits of mantissa in single-precision reciprocal and reciprocal square root instructions in AArch64 state, when FPCR.AH is 1.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| RPRES   | Meaning                                                                                                       |
|---------|---------------------------------------------------------------------------------------------------------------|
| 0b0000  | Single-precision reciprocal and reciprocal square root estimates give 8 bits of mantissa, when FPCR.AH is 1.  |
| 0b0001  | Single-precision reciprocal and reciprocal square root estimates give 12 bits of mantissa, when FPCR.AH is 1. |

All other values are reserved.

FEAT\_RPRES implements the functionality identified by the value 0b0001 .

When FPCR.AH is 0, the floating-point reciprocal estimate and reciprocal square root estimate instructions give 8 bits of mantissa.

Access to this field is RO.

## WFxT, bits [3:0]

Indicates support for the WFET and WFIT instructions in AArch64 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| WFxT   | Meaning                                                                                        |
|--------|------------------------------------------------------------------------------------------------|
| 0b0000 | WFET and WFIT are not supported.                                                               |
| 0b0010 | WFET and WFIT are supported, and the register number is reported in the ESR_ELx on exceptions. |

All other values are reserved.

FEAT\_WFxT implements the functionality identified by the value 0b0010 .

From Armv8.7, the only permitted value is 0b0010 .

Access to this field is RO.

## Accessing ID\_AA64ISAR2\_EL1

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, ID_AA64ISAR2_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0110 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_FGT) || !IsZero(ID_AA64ISAR2_EL1) || boolean ↪ → IMPLEMENTATION_DEFINED "ID_AA64ISAR2_EL1 trapped by HCR_EL2.TID3") && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64ISAR2_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64ISAR2_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_AA64ISAR2_EL1;
```