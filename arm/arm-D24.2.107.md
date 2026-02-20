## D24.2.107 ID\_ISAR6\_EL1, AArch32 Instruction Set Attribute Register 6

The ID\_ISAR6\_EL1 characteristics are:

## Purpose

Provides information about the instruction sets implemented by the PE in AArch32 state.

Must be interpreted with ID\_ISAR0\_EL1, ID\_ISAR1\_EL1, ID\_ISAR2\_EL1, ID\_ISAR3\_EL1, ID\_ISAR4\_EL1 and ID\_ISAR5\_EL1.

For general information about the interpretation of the ID registers see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

Note

Prior to the introduction of the features described by this register, this register was unnamed and reserved, RES0 from EL1, EL2, and EL3.

AArch64 System register ID\_ISAR6\_EL1 bits [31:0] are architecturally mapped to AArch32 System register ID\_ISAR6[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_ISAR6\_EL1 are UNDEFINED.

## Attributes

ID\_ISAR6\_EL1 is a 64-bit register.

## Field descriptions

When FEAT\_AA32 is implemented:

<!-- image -->

| 63                                         | 32   |
|--------------------------------------------|------|
| RES0                                       |      |
| 31 28 27 24 23 20 19 16 15 12 11 8 7 4 3 0 |      |
| CLRBHB I8MM BF16 SPECRES SB FHM DP         |      |
| JSCVT                                      |      |

## Bits [63:32]

Reserved, RES0.

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

Indicates support for the following Advanced SIMD Int8 matrix multiplication instructions VSMMLA , VSUDOT , VUMMLA , VUSMMLA , and VUSDOT in AArch32 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| I8MM   | Meaning                                                      |
|--------|--------------------------------------------------------------|
| 0b0000 | Int8 matrix multiplication instructions are not implemented. |
| 0b0001 | The specified instructions are implemented.                  |

All other values are reserved.

FEAT\_AA32I8MM implements the functionality identified by 0b0001 .

Access to this field is RO.

## BF16, bits [23:20]

Indicates support for the following Advanced SIMD and floating-point BFloat16 instructions VCVT , VCVTB , VCVTT , VDOT , VFMAB , VFMAT , and VMMLA instructions with BF16 operand or result types in AArch32 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| BF16   | Meaning                                     |
|--------|---------------------------------------------|
| 0b0000 | BFloat16 instructions are not implemented.  |
| 0b0001 | The specified instructions are implemented. |

All other values are reserved.

FEAT\_AA32BF16 implements the functionality identified by 0b0001 .

Access to this field is RO.

## SPECRES, bits [19:16]

Indicates support for prediction invalidation instructions in AArch32 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SPECRES   | Meaning                                                     |
|-----------|-------------------------------------------------------------|
| 0b0000    | Prediction invalidation instructions are not implemented.   |
| 0b0001    | CFPRCTX, DVPRCTX, and CPPRCTX instructions are implemented. |
| 0b0010    | As 0b0001 , and COSPRCTX instruction is implemented.        |

All other values are reserved.

FEAT\_SPECRES implements the functionality identified by 0b0001 .

FEAT\_SPECRES2 implements the functionality identified by 0b0010 .

From Armv8.5, the value 0b0000 is not permitted.

From Armv8.9, the value 0b0001 is not permitted.

Access to this field is RO.

## SB, bits [15:12]

Indicates support for the SB instruction in AArch32 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SB     | Meaning                            |
|--------|------------------------------------|
| 0b0000 | SB instruction is not implemented. |
| 0b0001 | SB instruction is implemented.     |

All other values are reserved.

FEAT\_SB implements the functionality identified by 0b0001 .

From Armv8.5, value 0b0000 is not permitted.

Access to this field is RO.

## FHM, bits [11:8]

Indicates support for the following Advanced SIMD and floating-point VFMAL and VFMSL instructions in AArch32 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| FHM    | Meaning                                         |
|--------|-------------------------------------------------|
| 0b0000 | The specified instructions are not implemented. |
| 0b0001 | The specified instructions are implemented.     |

All other values are reserved.

FEAT\_FHM implements the functionality identified by 0b0001 .

From Armv8.2, the permitted values are 0b0000 and 0b0001 .

Access to this field is RO.

## DP, bits [7:4]

Indicates support for dot product instructions in AArch32 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| DP     | Meaning                                       |
|--------|-----------------------------------------------|
| 0b0000 | Dot product instructions are not implemented. |
| 0b0001 | VUDOT and VSDOT instructions are implemented. |

All other values are reserved.

FEAT\_DotProd implements the functionality identified by 0b0001 .

In Armv8.2, the permitted values are 0b0000 and 0b0001 .

From Armv8.4, the only permitted value is 0b0001 .

Access to this field is RO.

## JSCVT, bits [3:0]

Indicates support for the VJCVT instruction in AArch32 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| JSCVT   | Meaning                                   |
|---------|-------------------------------------------|
| 0b0000  | The VJCVT instruction is not implemented. |
| 0b0001  | The VJCVT instruction is implemented.     |

All other values are reserved.

FEAT\_JSCVT implements the functionality identified by 0b0001 .

In Armv8.0, Armv8.1, and Armv8.2, the only permitted value is 0b0000 .

From Armv8.3, if Advanced SIMD or Floating-point is implemented, the value 0b0000 is not implemented.

From Armv8.3, if Advanced SIMD or Floating-point is not implemented, the only permitted value is 0b0000 .

Access to this field is RO.

## Otherwise:

<!-- image -->

## Bits [63:0]

Reserved, UNKNOWN.

## Accessing ID\_ISAR6\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ID\_ISAR6\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0010 | 0b111 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_FGT) || !IsZero(ID_ISAR6_EL1) || boolean ↪ → IMPLEMENTATION_DEFINED "ID_ISAR6_EL1 trapped by HCR_EL2.TID3") && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_ISAR6_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_ISAR6_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_ISAR6_EL1;
```