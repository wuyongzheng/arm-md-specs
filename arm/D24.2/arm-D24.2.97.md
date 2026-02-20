## D24.2.97 ID\_AA64ZFR0\_EL1, SVE Feature ID Register 0

The ID\_AA64ZFR0\_EL1 characteristics are:

## Purpose

Provides additional information about the implemented features of the AArch64 Scalable Vector Extension instruction set, when FEAT\_SVE or FEAT\_SME is implemented.

For general information about the interpretation of the ID registers, see Principles of the ID scheme for fields in ID registers.

## Configuration

## Note

Prior to the introduction of the features described by this register, this register was unnamed and reserved, RES0 from EL1, EL2, and EL3.

If FEAT\_SME is implemented and FEAT\_SVE is not implemented, then SVE instructions can only be executed when the PE is in Streaming SVE mode and the instructions are legal for execution in Streaming SVE mode.

## Attributes

ID\_AA64ZFR0\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   | 60 59   | 56 55   | 52 51   | 48 47   | 44 43   | 40 39   | 36   | 35     | 32   |
|------|---------|---------|---------|---------|---------|---------|------|--------|------|
| RES0 | F64MM   | F32MM   | F16MM   |         | I8MM    | SM4     | RES0 | SHA3   |      |
| 31   | 28 27   | 24 23   | 20 19   | 16 15   | 12      | 11 8 7  | 4    | 3      | 0    |
| RES0 | B16B16  | BF16    | BitPerm |         | EltPerm | RES0    | AES  | SVEver |      |

## Bits [63:60]

Reserved, RES0.

## F64MM, bits [59:56]

Indicates support for the SVE double-precision floating-point matrix multiply-accumulate instruction FMMLA , the LD1RO* instructions, the 128-bit element variants of the SVE TRN1 , TRN2 , UZP1 , UZP2 , ZIP1 , and ZIP2 instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| F64MM   | Meaning                                                              |
|---------|----------------------------------------------------------------------|
| 0b0000  | This field does not indicate support for the specified instructions. |
| 0b0001  | The specified instructions are implemented.                          |

All other values are reserved.

FEAT\_F64MM implements the functionality identified by 0b0001 .

The instructions described by nonzero values of this field might not be legal when the PE is in Streaming SVE mode.

Access to this field is RO.

## F32MM, bits [55:52]

Indicates support for the SVE single-precision floating-point matrix multiply-accumulate instruction FMMLA .

The value of this field is an IMPLEMENTATION DEFINED choice of:

| F32MM   | Meaning                                                             |
|---------|---------------------------------------------------------------------|
| 0b0000  | This field does not indicate support for the specified instruction. |
| 0b0001  | The specified instruction is implemented.                           |

All other values are reserved.

FEAT\_F32MM implements the functionality identified by 0b0001 .

The instructions described by nonzero values of this field might not be legal when the PE is in Streaming SVE mode.

Access to this field is RO.

## F16MM, bits [51:48]

Indicates support for the SVE half-precision floating-point matrix multiply-accumulate to single-precision instruction FMMLA (widening, FP16 to FP32).

The value of this field is an IMPLEMENTATION DEFINED choice of:

| F16MM   | Meaning                                                             |
|---------|---------------------------------------------------------------------|
| 0b0000  | This field does not indicate support for the specified instruction. |
| 0b0001  | The specified instruction is implemented.                           |

FEAT\_SVE\_F16F32MM implements the functionality identified by 0b0001 .

The instructions described by nonzero values of this field might not be legal when the PE is in Streaming SVE mode.

Access to this field is RO.

## I8MM, bits [47:44]

Indicates support for the following SVE 8-bit integer sum-of-products and accumulate to 32-bit integer instructions SMMLA , SUDOT , UMMLA , USMMLA , and USDOT .

The value of this field is an IMPLEMENTATION DEFINED choice of:

| I8MM   | Meaning                                                              |
|--------|----------------------------------------------------------------------|
| 0b0000 | This field does not indicate support for the specified instructions. |
| 0b0001 | The specified instructions are implemented.                          |

All other values are reserved.

FEAT\_I8MM implements the functionality identified by 0b0001 .

When Advanced SIMD and SVE are both implemented, this field must return the same value as ID\_AA64ISAR1\_EL1.I8MM.

From Armv8.6, if SVE is implemented, the value 0b0000 is not permitted.

SVE SMMLA , UMMLA , and USMMLA instructions might not be legal when the PE is in Streaming SVE mode.

Access to this field is RO.

## SM4, bits [43:40]

Indicates support for SVE SM4 instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SM4    | Meaning                                                              |
|--------|----------------------------------------------------------------------|
| 0b0000 | This field does not indicate support for the specified instructions. |
| 0b0001 | SVE SM4E and SM4EKEY instructions are implemented.                   |

All other values are reserved.

FEAT\_SVE\_SM4 implements the functionality identified by 0b0001 .

The instructions described by nonzero values of this field might not be legal when the PE is in Streaming SVE mode.

Access to this field is RO.

## Bits [39:36]

Reserved, RES0.

## SHA3, bits [35:32]

Indicates support for the SVE SHA3 instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SHA3   | Meaning                                                              |
|--------|----------------------------------------------------------------------|
| 0b0000 | This field does not indicate support for the specified instructions. |
| 0b0001 | SVE RAX1 instruction is implemented.                                 |

All other values are reserved.

FEAT\_SVE\_SHA3 implements the functionality identified by 0b0001 .

If FEAT\_SME2p1 is not implemented, then the instructions described by nonzero values of this field might not be legal when the PE is in Streaming SVE mode.

Access to this field is RO.

## Bits [31:28]

Reserved, RES0.

B16B16, bits [27:24]

Indicates support for SVE non-widening BFloat16 instructions and SME multi-vector Z-targeting non-widening BFloat16 instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| B16B16   | Meaning                                                                                                                                                                                                                                                                                                  |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000   | This field does not indicate support for the specified instructions.                                                                                                                                                                                                                                     |
| 0b0001   | The following non-widening BFloat16 instructions are implemented: • SVE instructions: BFADD , BFCLAMP , BFMAX , BFMAXNM , BFMIN , BFMINNM , BFMLA BFMLS , BFMUL , and BFSUB . • If FEAT_SME2 is implemented, SMEmulti-vector Z-targeting instructions: BFCLAMP , BFMAX , BFMAXNM , BFMIN , and BFMINNM . |
| 0b0010   | As 0b0001 , and adds the following non-widening BFloat16 instructions: • SVE instruction BFSCALE . • If FEAT_SME2 is implemented, SMEmulti-vector Z-targeting instructions BFMUL and BFSCALE .                                                                                                           |

FEAT\_SVE\_B16B16 implements the functionality identified by 0b0001 .

FEAT\_SVE\_BFSCALE implements the functionality identified by 0b0010 .

Access to this field is RO.

## BF16, bits [23:20]

Indicates support for SVE BFloat16 instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| BF16   | Meaning                                                                                    |
|--------|--------------------------------------------------------------------------------------------|
| 0b0000 | SVE BFloat16 instructions are not implemented.                                             |
| 0b0001 | SVE BFCVT , BFCVTNT , BFDOT , BFMLALB , BFMLALT , and BFMMLA instructions are implemented. |
| 0b0010 | As 0b0001 , but the FPCR.EBF field is also supported.                                      |

All other values are reserved.

FEAT\_BF16 implements the functionality identified by 0b0001 .

FEAT\_EBF16 implements the functionality identified by 0b0010 .

This field must return the same value as ID\_AA64ISAR1\_EL1.BF16.

SVE BFMMLA instructions might not be legal when the PE is in Streaming SVE mode.

From Armv8.6 and Armv9.1, the value 0b0000 is not permitted.

Access to this field is RO.

## BitPerm, bits [19:16]

Indicates support for the SVE bit permute instructions BDEP , BEXT , and BGRP .

The value of this field is an IMPLEMENTATION DEFINED choice of:

| BitPerm   | Meaning                                                              |
|-----------|----------------------------------------------------------------------|
| 0b0000    | This field does not indicate support for the specified instructions. |
| 0b0001    | The specified instructions are implemented.                          |

All other values are reserved.

FEAT\_SVE\_BitPerm implements the functionality identified by 0b0001 when the PE is not in Streaming SVE mode.

FEAT\_SSVE\_BitPerm which is identified in ID\_AA64SMFR0\_EL1.SBitPerm, indicates whether the FEAT\_SVE\_BitPerm functionality is implemented when the PE is in Streaming SVE mode.

Access to this field is RO.

## EltPerm, bits [15:12]

## When FEAT\_SVE2p2 is implemented or FEAT\_SME2p2 is implemented:

If FEAT\_SVE2p2 is implemented, the following SVE instructions are implemented when the PE is not in Streaming SVE mode:

- 8-bit and 16-bit element COMPACT .
- 8-bit, 16-bit, 32-bit, and 64-bit element EXPAND .

If FEAT\_SME2p2 is implemented, the following SVE instructions are implemented when the PE is in Streaming SVE mode:

- 8-bit, 16-bit, 32-bit, and 64-bit element COMPACT and EXPAND .

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EltPerm   | Meaning                                                              |
|-----------|----------------------------------------------------------------------|
| 0b0000    | This field does not indicate support for the specified instructions. |
| 0b0001    | The specified instructions are implemented.                          |

If FEAT\_SVE2p2 or FEAT\_SME2p2 is implemented, the value 0b0000 is not permitted.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## Bits [11:8]

Reserved, RES0.

## AES, bits [7:4]

Indicates support for SVE Advanced Encryption Standard instructions and 128-bit polynomial multiply long instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| AES    | Meaning                                                                                                                                                                                                           |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | This field does not indicate support for the specified instructions.                                                                                                                                              |
| 0b0001 | The following instructions are implemented: • SVE single-vector AESD , AESE , AESIMC , and AESMC instructions. • The 128-bit destination element variant of the SVE single-vector PMULLB and PMULLT instructions. |
| 0b0010 | As 0b0001 .                                                                                                                                                                                                       |
| 0b0011 | As 0b0010 , and adds the following SVE instructions: • Multi-vector AESD , AESDIMC , AESE and AESEMC instructions. • Multi-vector 128-bit destination element PMULL and PMLAL instructions.                       |

All other values are reserved.

FEAT\_SVE\_AES implements the functionality identified by the value 0b0001 .

FEAT\_SVE\_PMULL128 implements the functionality identified by the value 0b0010 .

FEAT\_SVE\_AES2 implements the functionality identified by 0b0011 .

If FEAT\_SSVE\_AES is not implemented, then the instructions described by nonzero values of this field might not be legal when the PE is in Streaming SVE mode.

Access to this field is RO.

## SVEver, bits [3:0]

Indicates support for SVE instructions when FEAT\_SME or FEAT\_SVE is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SVEver   | Meaning                                                 |
|----------|---------------------------------------------------------|
| 0b0000   | The SVE instructions are implemented.                   |
| 0b0001   | As 0b0000 , and adds the mandatory SVE2 instructions.   |
| 0b0010   | As 0b0001 , and adds the mandatory SVE2.1 instructions. |
| 0b0011   | As 0b0010 , and adds the mandatory SVE2.2 instructions. |

All other values are reserved.

FEAT\_SVE2 implements the functionality identified by 0b0001 when the PE is not in Streaming SVE mode.

FEAT\_SME implements the functionality identified by 0b0001 when the PE is in Streaming SVE mode.

FEAT\_SME2p1 implements the functionality identified by 0b0010 when the PE is in Streaming SVE mode.

FEAT\_SVE2p1 implements the functionality identified by 0b0010 when the PE is not in Streaming SVE mode.

FEAT\_SVE2p2 implements the functionality identified by 0b0011 when the PE is not in Streaming SVE mode.

FEAT\_SME2p2 implements the functionality identified by 0b0011 when the PE is in Streaming SVE mode.

From Armv9, if this register is present, the value 0b0000 is not permitted.

From Armv9.4, the value 0b0001 is not permitted.

From Armv9.6, the value 0b0010 is not permitted.

Access to this field is RO.

## Accessing ID\_AA64ZFR0\_EL1

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, ID_AA64ZFR0_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0100 | 0b100 |

```
if PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_FGT) || !IsZero(ID_AA64ZFR0_EL1) || boolean ↪ → IMPLEMENTATION_DEFINED "ID_AA64ZFR0_EL1 trapped by HCR_EL2.TID3") && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64ZFR0_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64ZFR0_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_AA64ZFR0_EL1;
```