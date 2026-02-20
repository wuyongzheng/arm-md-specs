## D24.2.84 ID\_AA64ISAR0\_EL1, AArch64 Instruction Set Attribute Register 0

The ID\_AA64ISAR0\_EL1 characteristics are:

## Purpose

Provides information about the instructions implemented in AArch64 state.

For general information about the interpretation of the ID registers, see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_AA64ISAR0\_EL1 are UNDEFINED.

## Attributes

ID\_AA64ISAR0\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   | 60 59   | 56 55   | 52 51   | 48 47   | 44 43   | 40 39   | 36 35   |      | 32   |
|------|---------|---------|---------|---------|---------|---------|---------|------|------|
| RNDR | RNDR    | TLB     | TS      | FHM     | DP      | SM4     | SM3     | SHA3 |      |
| 31   | 28 27   | 24 23   | 20 19   | 16 15   | 12      | 11 8    | 7       | 4 3  | 0    |
| RDM  |         | RES0    | Atomic  | CRC32   | SHA2    | SHA1    | AES     | RES0 |      |

## RNDR, bits [63:60]

Indicates support for Random Number instructions in AArch64 state.

When FEAT\_RNG\_TRAP is implemented, the value returned by a direct read of ID\_AA64ISAR0\_EL1.RNDR is further controlled by the value of SCR\_EL3.TRNDR.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| RNDR   | Meaning                                        |
|--------|------------------------------------------------|
| 0b0000 | No Random Number instructions are implemented. |
| 0b0001 | RNDRand RNDRRSregisters are implemented.       |

All other values are reserved.

FEAT\_RNG implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## TLB, bits [59:56]

Indicates support for Outer Shareable and TLB range maintenance instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TLB    | Meaning                                                                     |
|--------|-----------------------------------------------------------------------------|
| 0b0000 | Outer Shareable and TLB range maintenance instructions are not implemented. |
| 0b0001 | Outer Shareable TLB maintenance instructions are implemented.               |
| 0b0010 | Outer Shareable and TLB range maintenance instructions are implemented.     |

All other values are reserved.

FEAT\_TLBIOS implements the functionality identified by the values 0b0001 and 0b0010 .

FEAT\_TLBIRANGE implements the functionality identified by the value 0b0010 .

From Armv8.4, the values 0b0000 and 0b0001 are not permitted.

Access to this field is RO.

## TS, bits [55:52]

Indicates support for flag manipulation instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TS     | Meaning                                                                           |
|--------|-----------------------------------------------------------------------------------|
| 0b0000 | No flag manipulation instructions are implemented.                                |
| 0b0001 | CFINV , RMIF , SETF16 , and SETF8 instructions are implemented.                   |
| 0b0010 | CFINV , RMIF , SETF16 , SETF8 , AXFLAG , and XAFLAG instructions are implemented. |

All other values are reserved.

FEAT\_FlagM implements the functionality identified by the value 0b0001 .

FEAT\_FlagM2 implements the functionality identified by the value 0b0010 .

In Armv8.4, the value 0b0000 is not permitted.

From Armv8.5, the value 0b0001 is not permitted.

Access to this field is RO.

## FHM, bits [51:48]

Indicates support for the Advanced SIMD half-precision to single-precision multiply instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| FHM    | Meaning                                                                                         |
|--------|-------------------------------------------------------------------------------------------------|
| 0b0000 | The Advanced SIMD half-precision to single-precision multiply instructions are not implemented. |
| 0b0001 | FMLAL and FMLSL instructions are implemented.                                                   |

All other values are reserved.

FEAT\_FHM implements the functionality identified by the value 0b0001 .

From Armv8.4, if FEAT\_FP16 is implemented, the value 0b0000 is not permitted.

From Armv9.7, if FEAT\_AdvSIMD and FEAT\_SVE\_F16F32MM are both implemented, the value 0b0010 is not permitted.

Access to this field is RO.

## DP, bits [47:44]

Indicates support for Dot Product instructions in AArch64 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| DP     | Meaning                                  |
|--------|------------------------------------------|
| 0b0000 | No Dot Product instructions implemented. |
| 0b0001 | UDOT and SDOT instructions implemented.  |

All other values are reserved.

FEAT\_DotProd implements the functionality identified by the value 0b0001 .

From Armv8.4, if FEAT\_AdvSIMD is implemented, the value 0b0000 is not permitted.

Access to this field is RO.

## SM4, bits [43:40]

Indicates support for SM4 instructions in AArch64 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SM4    | Meaning                                    |
|--------|--------------------------------------------|
| 0b0000 | No SM4 instructions implemented.           |
| 0b0001 | SM4E and SM4EKEY instructions implemented. |

All other values are reserved.

If FEAT\_SM4 is not implemented, the value 0b0001 is reserved.

FEAT\_SM4 implements the functionality identified by the value 0b0001 .

This field must have the same value as ID\_AA64ISAR0\_EL1.SM3.

Access to this field is RO.

## SM3, bits [39:36]

Indicates support for the following SM3 instructions SM3SS1 , SM3TT1A , SM3TT1B , SM3TT2A , SM3TT2B , SM3PARTW1 , and SM3PARTW2 in AArch64 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SM3    | Meaning                                         |
|--------|-------------------------------------------------|
| 0b0000 | The specified instructions are not implemented. |

| SM3    | Meaning                                     |
|--------|---------------------------------------------|
| 0b0001 | The specified instructions are implemented. |

All other values are reserved.

If FEAT\_SM3 is not implemented, the value 0b0001 is reserved.

FEAT\_SM3 implements the functionality identified by the value 0b0001 .

This field must have the same value as ID\_AA64ISAR0\_EL1.SM4.

Access to this field is RO.

## SHA3, bits [35:32]

Indicates support for the following SHA3 instructions EOR3 , RAX1 , XAR , and BCAX in AArch64 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SHA3   | Meaning                                         |
|--------|-------------------------------------------------|
| 0b0000 | The specified instructions are not implemented. |
| 0b0001 | The specified instructions are implemented.     |

All other values are reserved.

If FEAT\_SHA3 is not implemented, the value 0b0001 is reserved.

FEAT\_SHA3 implements the functionality identified by the value 0b0001 .

If the value of ID\_AA64ISAR0\_EL1.SHA1 is 0b0000 , this field must have the value 0b0000 .

If the value of this field is 0b0001 , ID\_AA64ISAR0\_EL1.SHA2 must have the value 0b0010 .

Access to this field is RO.

## RDM,bits [31:28]

Indicates support for SQRDMLAH and SQRDMLSH instructions in AArch64 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| RDM    | Meaning                                         |
|--------|-------------------------------------------------|
| 0b0000 | No RDMA instructions implemented.               |
| 0b0001 | SQRDMLAH and SQRDMLSH instructions implemented. |

All other values are reserved.

FEAT\_RDM implements the functionality identified by the value 0b0001 .

From Armv8.1, the value 0b0000 is not permitted.

Access to this field is RO.

## Bits [27:24]

Reserved, RES0.

## Atomic, bits [23:20]

Indicates support for Atomic instructions in AArch64 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Atomic   | Meaning                                                                                                            |
|----------|--------------------------------------------------------------------------------------------------------------------|
| 0b0000   | No Atomic instructions implemented.                                                                                |
| 0b0010   | LDADD , LDCLR , LDEOR , LDSET , LDSMAX , LDSMIN , LDUMAX , LDUMIN , CAS , CASP , and SWP instructions implemented. |
| 0b0011   | As for 0b0010 , plus 128-bit instructions LDCLRP , LDSETP , and SWPP .                                             |

All other values are reserved.

FEAT\_LSE implements the functionality identified by the value 0b0010 .

FEAT\_LSE128 implements the functionality identified by the value 0b0011 .

From Armv8.1, the value 0b0000 is not permitted.

Access to this field is RO.

## CRC32, bits [19:16]

Indicates support for the following CRC32 instructions CRC32B , CRC32H , CRC32W , CRC32X , CRC32CB , CRC32CH , CRC32CW , and CRC32CX in AArch64 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CRC32   | Meaning                                         |
|---------|-------------------------------------------------|
| 0b0000  | The specified instructions are not implemented. |
| 0b0001  | The specified instructions are implemented.     |

All other values are reserved.

FEAT\_CRC32 implements the functionality identified by the value 0b0001 .

From Armv8.1, the value 0b0000 is not permitted.

Access to this field is RO.

## SHA2, bits [15:12]

Indicates support for SHA2 instructions in AArch64 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SHA2   | Meaning                                                                   |
|--------|---------------------------------------------------------------------------|
| 0b0000 | No SHA2 instructions implemented.                                         |
| 0b0001 | Implements instructions: SHA256H , SHA256H2 , SHA256SU0 , and SHA256SU1 . |

| SHA2   | Meaning                                            |
|--------|----------------------------------------------------|
| 0b0010 | Implements instructions:                           |
|        | • SHA256H , SHA256H2 , SHA256SU0 , and SHA256SU1 . |
|        | • SHA512H , SHA512H2 , SHA512SU0 , and SHA512SU1 . |

All other values are reserved.

FEAT\_SHA256 implements the functionality identified by the value 0b0001 .

FEAT\_SHA512 implements the functionality identified by the value 0b0010 .

If the value of ID\_AA64ISAR0\_EL1.SHA1 is 0b0000 , this field must have the value 0b0000 .

If the value of this field is 0b0010 , ID\_AA64ISAR0\_EL1.SHA3 must have the value 0b0001 .

Access to this field is RO.

## SHA1, bits [11:8]

Indicates support for the following SHA1 instructions SHA1C , SHA1P , SHA1M , SHA1H , SHA1SU0 , and SHA1SU1 in AArch64 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SHA1   | Meaning                                         |
|--------|-------------------------------------------------|
| 0b0000 | The specified instructions are not implemented. |
| 0b0001 | The specified instructions are implemented.     |

All other values are reserved.

FEAT\_SHA1 implements the functionality identified by the value 0b0001 .

If the value of ID\_AA64ISAR0\_EL1.SHA2 is 0b0000 , this field must have the value 0b0000 .

Access to this field is RO.

## AES, bits [7:4]

Indicates support for AES instructions in AArch64 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| AES    | Meaning                                                                                 |
|--------|-----------------------------------------------------------------------------------------|
| 0b0000 | No AES instructions implemented.                                                        |
| 0b0001 | AESE , AESD , AESMC , and AESIMC instructions implemented.                              |
| 0b0010 | As for 0b0001 , plus PMULL and PMULL2 instructions operating on 64-bit source elements. |

FEAT\_AES implements the functionality identified by the value 0b0001 .

FEAT\_PMULL implements the functionality identified by the value 0b0010 .

All other values are reserved.

Access to this field is RO.

## Bits [3:0]

Reserved, RES0.

## Accessing ID\_AA64ISAR0\_EL1

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, ID_AA64ISAR0_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0110 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64ISAR0_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64ISAR0_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_AA64ISAR0_EL1;
```