## G8.2.92 ID\_ISAR6, Instruction Set Attribute Register 6

The ID\_ISAR6 characteristics are:

## Purpose

Provides information about the instruction sets implemented by the PE in AArch32 state.

Must be interpreted with ID\_ISAR0, ID\_ISAR1, ID\_ISAR2, ID\_ISAR3, ID\_ISAR4, and ID\_ISAR5.

For general information about the interpretation of the ID registers, see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

Note

Prior to the introduction of the features described by this register, this register was unnamed and reserved, RES0 from EL1, EL2, and EL3.

AArch32 System register ID\_ISAR6 bits [31:0] are architecturally mapped to AArch64 System register ID\_ISAR6\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ID\_ISAR6 are UNDEFINED.

## Attributes

ID\_ISAR6 is a 32-bit register.

## Field descriptions

| 31     | 28 27   | 24 23   | 20 19   | 16 15   | 12 11   | 8 7   | 4 3   | 0     |
|--------|---------|---------|---------|---------|---------|-------|-------|-------|
| CLRBHB | I8MM    | BF16    | SPECRES | SB      | FHM     | DP    |       | JSCVT |

## CLRBHB, bits [31:28]

Indicates support for the CLRBHB instruction in AArch32 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CLRBHB   | Meaning                                |
|----------|----------------------------------------|
| 0b0000   | CLRBHB instruction is not implemented. |
| 0b0001   | CLRBHB instruction is implemented.     |

All other values are reserved.

FEAT\_CLRBHB implements the functionality identified by 0b0001 .

From Armv8.9, the value 0b0000 is not permitted.

Access to this field is RO.

## I8MM, bits [27:24]

Indicates support for Advanced SIMD and floating-point Int8 matrix multiplication instructions VSMMLA , VSUDOT , VUMMLA , VUSMMLA , and VUSDOT in AArch32 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| I8MM   | Meaning                                                      |
|--------|--------------------------------------------------------------|
| 0b0000 | Int8 matrix multiplication instructions are not implemented. |
| 0b0001 | The specified instructions are implemented.                  |

All other values are reserved.

FEAT\_AA32I8MM implements the functionality identified by 0b0001 .

From Armv8.2, the permitted values are 0b0000 and 0b0001 .

Access to this field is RO.

## BF16, bits [23:20]

Indicates support for Advanced SIMD and floating-point BFloat16 instructions VCVT , VCVTB , VCVTT , VDOT , VFMAB , VFMAT , and VMMLA instructions with BF16 operand or result types in AArch32 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| BF16   | Meaning                                     |
|--------|---------------------------------------------|
| 0b0000 | BFloat16 instructions are not implemented.  |
| 0b0001 | The specified instructions are implemented. |

All other values are reserved.

FEAT\_AA32BF16 implements the functionality identified by 0b0001 .

From Armv8.2, the permitted values are 0b0000 and 0b0001 .

Access to this field is RO.

## SPECRES, bits [19:16]

Indicates support for prediction invalidation instructions in AArch32 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SPECRES   | Meaning                                                       |
|-----------|---------------------------------------------------------------|
| 0b0000    | Prediction invalidation instructions are not implemented.     |
| 0b0001    | CFPRCTX , DVPRCTX , and CPPRCTX instructions are implemented. |
| 0b0010    | As 0b0001 , and the COSPRCTX instruction is implemented.      |

All other values are reserved.

FEAT\_SPECRES implements the functionality identified by 0b0001 .

FEAT\_SPECRES2 implements the functionality identified by 0b0010 .

From Armv8.5, the value 0b0000 is not permitted.

From Armv8.9, the value 0b0001 is not permitted.

Access to this field is RO.

## SB, bits [15:12]

Indicates support for SB instruction in AArch32 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SB     | Meaning                            |
|--------|------------------------------------|
| 0b0000 | SB instruction is not implemented. |
| 0b0001 | SB instruction is implemented.     |

All other values are reserved.

From Armv8.5, the value 0b0000 is not permitted.

Access to this field is RO.

## FHM, bits [11:8]

Indicates support for Advanced SIMD and floating-point VFMAL and VMFSL instructions in AArch32 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| FHM    | Meaning                                       |
|--------|-----------------------------------------------|
| 0b0000 | VFMAL and VMFSL instructions not implemented. |
| 0b0001 | VFMAL and VMFSL instructions implemented.     |

FEAT\_FHM implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## DP, bits [7:4]

Indicates support for dot product instructions in AArch32 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| DP     | Meaning                                   |
|--------|-------------------------------------------|
| 0b0000 | No dot product instructions implemented.  |
| 0b0001 | VUDOT and VSDOT instructions implemented. |

All other values are reserved.

FEAT\_DotProd implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## JSCVT, bits [3:0]

Indicates support for the Javascript conversion instruction in AArch32 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| JSCVT   | Meaning                                   |
|---------|-------------------------------------------|
| 0b0000  | The VJCVT instruction is not implemented. |
| 0b0001  | The VJCVT instruction is implemented.     |

All other values are reserved.

In Armv8.0, the only permitted value is 0b0000 .

FEAT\_JSCVT implements the functionality identified by 0b0001 .

From Armv8.3, if Advanced SIMD or Floating-point is implemented, the value 0b0000 is not permitted.

From Armv8.3, if Advanced SIMD or Floating-point is not implemented, the only permitted value is 0b0000 .

Access to this field is RO.

## Accessing ID\_ISAR6

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0000 | 0b0010 | 0b111  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T0 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T0 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → (IsFeatureImplemented(FEAT_FGT) || !IsZero(ID_ISAR6) || boolean IMPLEMENTATION_DEFINED ↪ → "ID_ISAR6 trapped by HCR_EL2.TID3") && HCR_EL2.TID3 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && ↪ → (IsFeatureImplemented(FEAT_FGT) || !IsZero(ID_ISAR6) || boolean IMPLEMENTATION_DEFINED ↪ → "ID_ISAR6 trapped by HCR.TID3") && HCR.TID3 == '1' then AArch32.TakeHypTrapException(0x03); else R[t] = ID_ISAR6; elsif PSTATE.EL == EL2 then R[t] = ID_ISAR6; elsif PSTATE.EL == EL3 then R[t] = ID_ISAR6;
```