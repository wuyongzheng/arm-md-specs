## D24.2.85 ID\_AA64ISAR1\_EL1, AArch64 Instruction Set Attribute Register 1

The ID\_AA64ISAR1\_EL1 characteristics are:

## Purpose

Provides information about the features and instructions implemented in AArch64 state.

For general information about the interpretation of the ID registers, see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_AA64ISAR1\_EL1 are UNDEFINED.

## Attributes

ID\_AA64ISAR1\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   | 60 59   | 56 55   | 52 51   | 48   | 44 43   | 40 39   | 36   | 35      | 32   |
|------|---------|---------|---------|------|---------|---------|------|---------|------|
| LS64 | LS64    | XS      | I8MM    | DGH  | BF16    | SPECRES | SB   | FRINTTS |      |
| 31   | 28 27   | 24 23   | 20 19   | 16   | 12      | 11 8    | 7    | 4 3     | 0    |
| GPI  |         | GPA     | LRCPC   | FCMA | JSCVT   | API     | APA  | DPB     |      |

## LS64, bits [63:60]

Indicates support for LD64B and ST64B* instructions, and the ACCDATA\_EL1 register.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| LS64   | Meaning                                                                                                                |
|--------|------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | No LD64B or ST64B instructions are supported.                                                                          |
| 0b0001 | The LD64B and ST64B instructions are supported.                                                                        |
| 0b0010 | As 0b0001 , and adds the ST64BV instruction and traps.                                                                 |
| 0b0011 | As 0b0010 , and adds the ST64BV0 instruction, ACCDATA_EL1 register, and traps.                                         |
| 0b0100 | As 0b0011 , and adds support for atomic accesses to Write-back Cacheable, Shareable memory using one of the following: |

- LD64B and ST64B instructions.
- SIMD&amp;FP instructions that load or store a pair of 128-bit registers by generating 32-byte single-copy atomic accesses.

All other values are reserved.

FEAT\_LS64 implements the functionality identified by 0b0001 .

FEAT\_LS64\_V implements the functionality identified by 0b0010 .

FEAT\_LS64\_ACCDATA implements the functionality identified by 0b0011 .

FEAT\_LS64WB implements the functionality identified by 0b0100 .

Access to this field is RO.

## XS, bits [59:56]

Indicates support for the XS attribute, the TLBI and DSB instructions with the nXS qualifier, and the HCRX\_EL2.{FGTnXS, FnXS} fields in AArch64 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| XS     | Meaning                                                                                                                           |
|--------|-----------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | The XS attribute, the TLBI and DSB instructions with the nXS qualifier, and the HCRX_EL2.{FGTnXS, FnXS} fields are not supported. |
| 0b0001 | The XS attribute, the TLBI and DSB instructions with the nXS qualifier, and the HCRX_EL2.{FGTnXS, FnXS} fields are supported.     |

All other values are reserved.

FEAT\_XS implements the functionality identified by 0b0001 .

From Armv8.7, the value 0b0000 is not permitted.

Access to this field is RO.

## I8MM, bits [55:52]

Indicates support for the following Advanced SIMD Int8 matrix multiplication instructions SMMLA , SUDOT , UMMLA , USMMLA , and USDOT in AArch64 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| I8MM   | Meaning                                         |
|--------|-------------------------------------------------|
| 0b0000 | The specified instructions are not implemented. |
| 0b0001 | The specified instructions are implemented.     |

All other values are reserved.

FEAT\_I8MM implements the functionality identified by 0b0001 .

When Advanced SIMD and SVE are both implemented, this field must return the same value as ID\_AA64ZFR0\_EL1.I8MM.

From Armv8.6, the value 0b0000 is not permitted.

Access to this field is RO.

## DGH, bits [51:48]

Indicates support for the Data Gathering Hint instruction.

The value of this field is an IMPLEMENTATION DEFINED choice of:

All other values are reserved.

FEAT\_DGH implements the functionality identified by 0b0001 .

From Armv8.0, the permitted values are 0b0000 and 0b0001 .

If the DGH instruction has no effect in preventing the merging of memory accesses, the value of this field is 0b0000 .

Access to this field is RO.

## BF16, bits [47:44]

Indicates support for Advanced SIMD and floating-point BFloat16 instructions in AArch64 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| BF16   | Meaning                                                                                        |
|--------|------------------------------------------------------------------------------------------------|
| 0b0000 | BFloat16 instructions are not implemented.                                                     |
| 0b0001 | BFCVT , BFCVTN, BFCVTN2 , BFDOT , BFMLALB , BFMLALT , and BFMMLA instructions are implemented. |
| 0b0010 | As 0b0001 , but the FPCR.EBF field is also supported.                                          |

All other values are reserved.

FEAT\_BF16 implements the functionality identified by 0b0001 .

FEAT\_EBF16 implements the functionality identified by 0b0010 .

When FEAT\_SVE or FEAT\_SME is implemented, this field must return the same value as ID\_AA64ZFR0\_EL1.BF16.

From Armv8.6 and Armv9.1, the value 0b0000 is not permitted.

Access to this field is RO.

## SPECRES, bits [43:40]

Indicates support for prediction invalidation instructions in AArch64 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SPECRES   | Meaning                                                    |
|-----------|------------------------------------------------------------|
| 0b0000    | Prediction invalidation instructions are not implemented.  |
| 0b0001    | CFP RCTX, DVPRCTXand CPP RCTXinstructions are implemented. |
| 0b0010    | As 0b0001 , and COSP RCTXinstruction is implemented.       |

All other values are reserved.

| DGH    | Meaning                                 |
|--------|-----------------------------------------|
| 0b0000 | Data Gathering Hint is not implemented. |
| 0b0001 | Data Gathering Hint is implemented.     |

FEAT\_SPECRES implements the functionality identified by 0b0001 .

FEAT\_SPECRES2 implements the functionality identified by 0b0010 .

From Armv8.5, the value 0b0000 is not permitted.

From Armv8.9, the value 0b0001 is not permitted.

Access to this field is RO.

## SB, bits [39:36]

Indicates support for SB instruction in AArch64 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SB     | Meaning                            |
|--------|------------------------------------|
| 0b0000 | SB instruction is not implemented. |
| 0b0001 | SB instruction is implemented.     |

All other values are reserved.

FEAT\_SB implements the functionality identified by 0b0001 .

From Armv8.5, the value 0b0000 is not permitted.

Access to this field is RO.

## FRINTTS, bits [35:32]

Indicates support for FRINT32Z , FRINT32X , FRINT64Z , and FRINT64X instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| FRINTTS   | Meaning                                         |
|-----------|-------------------------------------------------|
| 0b0000    | The specified instructions are not implemented. |
| 0b0001    | The specified instructions are implemented.     |

All other values are reserved.

FEAT\_FRINTTS implements the functionality identified by 0b0001 .

From Armv8.5, the value 0b0000 is not permitted.

Access to this field is RO.

## GPI, bits [31:28]

Indicates support for an IMPLEMENTATION DEFINED algorithm is implemented in the PE for generic code authentication in AArch64 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| GPI    | Meaning                                                                                                               |
|--------|-----------------------------------------------------------------------------------------------------------------------|
| 0b0000 | Generic Authentication using an IMPLEMENTATION DEFINED algorithm is not implemented.                                  |
| 0b0001 | Generic Authentication using an IMPLEMENTATION DEFINED algorithm is implemented. This includes the PACGA instruction. |

All other values are reserved.

When this field is nonzero, FEAT\_PACIMP is implemented.

From Armv8.3, the permitted values are 0b0000 and 0b0001 .

If the value of ID\_AA64ISAR1\_EL1.GPA is nonzero, or the value of ID\_AA64ISAR2\_EL1.GPA3 is nonzero, this field must have the value 0b0000 .

Access to this field is RO.

## GPA, bits [27:24]

Indicates whether the QARMA5 algorithm is implemented in the PE for generic code authentication in AArch64 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| GPA    | Meaning                                                                                               |
|--------|-------------------------------------------------------------------------------------------------------|
| 0b0000 | Generic Authentication using the QARMA5algorithm is not implemented.                                  |
| 0b0001 | Generic Authentication using the QARMA5algorithm is implemented. This includes the PACGA instruction. |

All other values are reserved.

FEAT\_PACQARMA5 implements the functionality identified by 0b0001 .

When this field is nonzero, FEAT\_PACQARMA5 is implemented.

From Armv8.3, the permitted values are 0b0000 and 0b0001 .

If the value of ID\_AA64ISAR1\_EL1.GPI is nonzero, or the value of ID\_AA64ISAR2\_EL1.GPA3 is nonzero, this field must have the value 0b0000 .

Access to this field is RO.

## LRCPC, bits [23:20]

Indicates support for weaker release consistency, RCpc, based model.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| LRCPC   | Meaning                                                                                                    |
|---------|------------------------------------------------------------------------------------------------------------|
| 0b0000  | RCpc instructions are not implemented.                                                                     |
| 0b0001  | The no offset LDAPR , LDAPRB , and LDAPRH instructions are implemented.                                    |
| 0b0010  | As 0b0001 , and the LDAPR (unscaled immediate) and STLR (unscaled immediate) instructions are implemented. |

| LRCPC   | Meaning                                                                                                                                                                                                                                                                                                        |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0011  | As 0b0010 , and the post-index LDAPR , LDIAPP , STILP , and pre-index STLR instructions are implemented. If Advanced SIMD and floating-point is implemented, then the LDAPUR (SIMD&FP), LDAP1 (SIMD&FP), STLUR (SIMD&FP), and STL1 (SIMD&FP) instructions are implemented in Advanced SIMD and floating-point. |

All other values are reserved.

FEAT\_LRCPC implements the functionality identified by the value 0b0001 .

FEAT\_LRCPC2 implements the functionality identified by the value 0b0010 .

FEAT\_LRCPC3 implements the functionality identified by the value 0b0011 .

From Armv8.3, the value 0b0000 is not permitted.

From Armv8.4, the value 0b0001 is not permitted.

Access to this field is RO.

## FCMA, bits [19:16]

Indicates support for complex number addition and multiplication, where numbers are stored in vectors.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| FCMA   | Meaning                                               |
|--------|-------------------------------------------------------|
| 0b0000 | The FCMLA and FCADD instructions are not implemented. |
| 0b0001 | The FCMLA and FCADD instructions are implemented.     |

All other values are reserved.

FEAT\_FCMA implements the functionality identified by the value 0b0001 .

From Armv8.3, if Advanced SIMD or floating-point is implemented, the value 0b0000 is not permitted.

From Armv8.3, if Advanced SIMD or floating-point is not implemented, the only permitted value is 0b0000 .

Access to this field is RO.

## JSCVT, bits [15:12]

Indicates support for JavaScript conversion from double-precision floating-point values to integers in AArch64 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| JSCVT   | Meaning                                     |
|---------|---------------------------------------------|
| 0b0000  | The FJCVTZS instruction is not implemented. |
| 0b0001  | The FJCVTZS instruction is implemented.     |

All other values are reserved.

FEAT\_JSCVT implements the functionality identified by 0b0001 .

From Armv8.3, if Advanced SIMD or floating-point is implemented, the value 0b0000 is not permitted.

From Armv8.3, if Advanced SIMD or floating-point is not implemented, the only permitted value is 0b0000 .

Access to this field is RO.

## API, bits [11:8]

Indicates whether an IMPLEMENTATION DEFINED algorithm is implemented in the PE for address authentication, in AArch64 state. This applies to all Pointer Authentication instructions other than the PACGA instruction.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| API    | Meaning                                                                                                                                                                                                                                                                      |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | Address Authentication using an IMPLEMENTATION DEFINED algorithm is not implemented.                                                                                                                                                                                         |
| 0b0001 | Address Authentication using an IMPLEMENTATION DEFINED algorithm is implemented, FEAT_EPAC and FEAT_PAuth2 are not implemented.                                                                                                                                              |
| 0b0010 | Address Authentication using an IMPLEMENTATION DEFINED algorithm is implemented, FEAT_EPAC is implemented, and FEAT_PAuth2 is not implemented.                                                                                                                               |
| 0b0011 | Address Authentication using an IMPLEMENTATION DEFINED algorithm is implemented, FEAT_EPAC is not implemented, and FEAT_PAuth2 is implemented.                                                                                                                               |
| 0b0100 | Address Authentication using an IMPLEMENTATION DEFINED algorithm is implemented, FEAT_EPAC is not implemented, FEAT_PAuth2 and FEAT_FPAC are implemented.                                                                                                                    |
| 0b0101 | Address Authentication using an IMPLEMENTATION DEFINED algorithm is implemented, FEAT_EPAC is not implemented, FEAT_PAuth2, FEAT_FPAC, and FEAT_FPACCOMBINE are implemented.                                                                                                 |
| 0b0110 | Address Authentication using an IMPLEMENTATION DEFINED algorithm is implemented, including instructions that allow signing of LR using SP and PC as diversifiers, FEAT_EPAC is not implemented, FEAT_PAuth2, FEAT_FPAC, FEAT_FPACCOMBINE, and FEAT_PAuth_LR are implemented. |

All other values are reserved.

FEAT\_PAuth implements the functionality identified by 0b0001 .

FEAT\_EPAC implements the functionality identified by 0b0010 .

FEAT\_PAuth2 implements the functionality identified by 0b0011 .

FEAT\_FPAC implements the functionality identified by 0b0100 .

FEAT\_FPACCOMBINE implements the functionality identified by 0b0101 .

FEAT\_PAuth\_LR implements the functionality identified by 0b0110 .

When this field is nonzero, FEAT\_PACIMP is implemented.

In Armv8.3, the permitted values are 0b0000 , 0b0001 , 0b0010 , 0b0011 , 0b0100 , and 0b0101 .

From Armv8.6, the permitted values are 0b0000 , 0b0011 , 0b0100 , and 0b0101 .

From Armv9.5, the permitted values are 0b0000 , 0b0011 , 0b0100 , 0b0101 , and 0b0110 .

If the value of ID\_AA64ISAR1\_EL1.APA is nonzero, or the value of ID\_AA64ISAR2\_EL1.APA3 is nonzero, this field must have the value 0b0000 .

Access to this field is RO.

## APA, bits [7:4]

Indicates whether the QARMA5 algorithm is implemented in the PE for address authentication, in AArch64 state. This applies to all Pointer Authentication instructions other than the PACGA instruction.

## The value of this field is an IMPLEMENTATION DEFINED choice of:

| APA    | Meaning                                                                                                                                                                                                                                                      |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | Address Authentication using the QARMA5algorithm is not implemented.                                                                                                                                                                                         |
| 0b0001 | Address Authentication using the QARMA5algorithm is implemented, FEAT_EPAC and FEAT_PAuth2 are not implemented.                                                                                                                                              |
| 0b0010 | Address Authentication using the QARMA5algorithm is implemented, FEAT_EPAC is implemented, and FEAT_PAuth2 is not implemented.                                                                                                                               |
| 0b0011 | Address Authentication using the QARMA5algorithm is implemented, FEAT_EPAC is not implemented, and FEAT_PAuth2 is implemented.                                                                                                                               |
| 0b0100 | Address Authentication using the QARMA5algorithm is implemented, FEAT_EPAC is not implemented, FEAT_PAuth2 and FEAT_FPAC are implemented.                                                                                                                    |
| 0b0101 | Address Authentication using the QARMA5algorithm is implemented, FEAT_EPAC is not implemented, FEAT_PAuth2, FEAT_FPAC, and FEAT_FPACCOMBINE are implemented.                                                                                                 |
| 0b0110 | Address Authentication using the QARMA5algorithm is implemented, including instructions that allow signing of LR using SP and PC as diversifiers, FEAT_EPAC is not implemented, FEAT_PAuth2, FEAT_FPAC, FEAT_FPACCOMBINE, and FEAT_PAuth_LR are implemented. |

All other values are reserved.

FEAT\_PAuth implements the functionality identified by 0b0001 .

FEAT\_EPAC implements the functionality identified by 0b0010 .

FEAT\_PAuth2 implements the functionality identified by 0b0011 .

FEAT\_FPAC implements the functionality identified by 0b0100 .

FEAT\_FPACCOMBINE implements the functionality identified by 0b0101 .

FEAT\_PAuth\_LR implements the functionality identified by 0b0110 .

When this field is nonzero, FEAT\_PACQARMA5 is implemented.

In Armv8.3, the permitted values are 0b0000 , 0b0001 , 0b0010 , 0b0011 , 0b0100 , and 0b0101 .

From Armv8.6, the permitted values are 0b0000 , 0b0011 , 0b0100 , and 0b0101 .

From Armv9.5, the permitted values are 0b0000 , 0b0011 , 0b0100 , 0b0101 , and 0b0110 .

If the value of ID\_AA64ISAR1\_EL1.API is nonzero, or the value of ID\_AA64ISAR2\_EL1.APA3 is nonzero, this field must have the value 0b0000 .

Access to this field is RO.

## DPB, bits [3:0]

Data Persistence writeback. Indicates support for the DC CV AP and DC CV ADP instructions in AArch64 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| DPB    | Meaning              |
|--------|----------------------|
| 0b0000 | DCCVAPnot supported. |
| 0b0001 | DCCVAPsupported.     |

All other values are reserved.

FEAT\_DPB implements the functionality identified by the value 0b0001 .

FEAT\_DPB2 implements the functionality identified by the value 0b0010 .

From Armv8.2, the value 0b0000 is not permitted.

From Armv8.5, the value 0b0001 is not permitted.

Access to this field is RO.

## Accessing ID\_AA64ISAR1\_EL1

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, ID_AA64ISAR1_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0110 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64ISAR1_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64ISAR1_EL1;
```

| DPB    | Meaning                     |
|--------|-----------------------------|
| 0b0010 | DCCVAPandDCCVADP supported. |

elsif PSTATE.EL == EL3 then X[t, 64] = ID\_AA64ISAR1\_EL1;