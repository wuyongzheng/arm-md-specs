## D24.2.87 ID\_AA64ISAR3\_EL1, AArch64 Instruction Set Attribute Register 3

The ID\_AA64ISAR3\_EL1 characteristics are:

## Purpose

Provides information about the features and instructions implemented in AArch64 state.

For general information about the interpretation of the ID registers, see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

## Note

Prior to the introduction of the features described by this register, this register was unnamed and reserved, RES0 from EL1, EL2, and EL3.

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_AA64ISAR3\_EL1 are UNDEFINED.

## Attributes

ID\_AA64ISAR3\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## FPRCVT, bits [31:28]

Indicates support for the following conversion between floating-point and integer instructions with only scalar SIMD&amp;FP register operands and results, and with different input and output register sizes, when the PE is not in Streaming SVE mode:

- FCVTAS (scalar SIMD&amp;FP), FCVTAU (scalar SIMD&amp;FP).
- FCVTMS (scalar SIMD&amp;FP), FCVTMU (scalar SIMD&amp;FP).
- FCVTNS (scalar SIMD&amp;FP), FCVTNU (scalar SIMD&amp;FP).
- FCVTPS (scalar SIMD&amp;FP), FCVTPU (scalar SIMD&amp;FP).
- FCVTZS (scalar SIMD&amp;FP), FCVTZU (scalar SIMD&amp;FP).
- SCVTF (scalar SIMD&amp;FP), UCVTF (scalar SIMD&amp;FP).

If FEAT\_SME is implemented, indicates support for the above instructions, as well as the following conversion between floating-point and integer instructions with only scalar SIMD&amp;FP register operands and results, and with the same input and output register sizes, when the PE is in Streaming SVE mode:

- FCVTAS (vector), FCVTAU (vector).
- FCVTMS (vector), FCVTMU (vector).
- FCVTNS (vector), FCVTNU (vector).
- FCVTPS (vector), FCVTPU (vector).
- FCVTZS (vector), FCVTZU (vector).
- SCVTF (vector), UCVTF (vector).

The value of this field is an IMPLEMENTATION DEFINED choice of:

| FPRCVT   | Meaning                                         |
|----------|-------------------------------------------------|
| 0b0000   | The specified instructions are not implemented. |
| 0b0001   | The specified instructions are implemented.     |

FEAT\_FPRCVT implements the functionality identified by the value 0b0001 .

From Armv9.6, if FEAT\_FP is implemented, the value 0b0000 is not permitted.

Access to this field is RO.

## LSUI, bits [27:24]

Support for the following load and store unprivileged instructions:

- LDTXR , STTXR .
- LDATXR , STLTXR .
- CAST , CASAT , CASALT , CASLT .
- CASPT , CASPAT , CASPALT , CASPLT .
- LDTP , STTP .
- LDTP (SIMD&amp;FP) , STTP (SIMD&amp;FP) .
- LDTNP , STTNP .
- LDTNP (SIMD&amp;FP) , STTNP (SIMD&amp;FP) .
- SWPT , SWPTA , SWPTL , SWPTAL .
- LDTADD , LDTADDA , LDTADDAL , LDTADDL .
- LDTSET , LDTSETA , LDTSETAL , LDTSETL .
- LDTCLR , LDTCLRA , LDTCLRAL , LDTCLRL .
- STTADD , STTADDL .
- STTSET , STTSETL .
- STTCLR , STTCLRL .

The value of this field is an IMPLEMENTATION DEFINED choice of:

| LSUI   | Meaning                                         |
|--------|-------------------------------------------------|
| 0b0000 | The specified instructions are not implemented. |
| 0b0001 | The specified instructions are implemented.     |

FEAT\_LSUI implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## OCCMO,bits [23:20]

Indicates support for the following cache maintenance operation to the Outer cache level instructions:

- DC CIVAOC .
- DC CVAOC .

## If FEAT\_MTE is implemented:

- DC CIGDVAOC .
- DC CGDVAOC .

The value of this field is an IMPLEMENTATION DEFINED choice of:

| OCCMO   | Meaning                                         |
|---------|-------------------------------------------------|
| 0b0000  | The specified instructions are not implemented. |
| 0b0001  | The specified instructions are implemented.     |

FEAT\_OCCMO implements the functionality identified by the value 0b0001 .

From Armv9.6, the value 0b0000 is not permitted.

Access to this field is RO.

## LSFE, bits [19:16]

Indicates support for the following A64 Base atomic floating-point in-memory instructions:

- Floating-point atomic add in memory: LDFADD , LDFADDA , LDFADDAL , and LDFADDL .
- BFloat16 atomic add in memory: LDBFADD , LDBFADDA , LDBFADDAL , and LDBFADDL .
- Floating-point atomic maximum in memory: LDFMAX , LDFMAXA , LDFMAXAL , and LDFMAXL .
- BFloat16 atomic maximum in memory: LDBFMAX , LDBFMAXA , LDBFMAXAL , and LDBFMAXL .
- Floating-point atomic maximum number in memory: LDFMAXNM , LDFMAXNMA , LDFMAXNMAL , and LDFMAXNML .
- BFloat16 atomic maximum number in memory: LDBFMAXNM , LDBFMAXNMA , LDBFMAXNMAL , and LDBFMAXNML .
- Floating-point atomic minimum in memory: LDFMIN , LDFMINA , LDFMINAL , and LDFMINL .
- BFloat16 atomic minimum in memory: LDBFMIN , LDBFMINA , LDBFMINAL , and LDBFMINL .
- Floating-point atomic minimum number in memory: LDFMINNM , LDFMINNMA , LDFMINNMAL , and LDFMINNML .
- BFloat16 atomic minimum number in memory: LDBFMINNM , LDBFMINNMA , LDBFMINNMAL , and LDBFMINNML .
- Floating-point atomic add in memory, without return: STFADD and STFADDL .
- BFloat16 atomic add in memory, without return: STBFADD and STBFADDL .
- Floating-point atomic maximum in memory, without return: STFMAX and STFMAXL .
- BFloat16 atomic maximum in memory, without return: STBFMAX and STBFMAXL .
- Floating-point atomic maximum number in memory, without return: STFMAXNM and STFMAXNML .
- BFloat16 atomic maximum number in memory, without return: STBFMAXNM and STBFMAXNML .
- Floating-point atomic minimum in memory, without return: STFMIN and STFMINL .
- BFloat16 atomic minimum in memory, without return: STBFMIN and STBFMINL .
- Floating-point atomic minimum number in memory, without return: STFMINNM and STFMINNML .
- BFloat16 atomic minimum number in memory, without return: STBFMINNM and STBFMINNML .

The value of this field is an IMPLEMENTATION DEFINED choice of:

| LSFE   | Meaning                                                                     |
|--------|-----------------------------------------------------------------------------|
| 0b0000 | Atomic floating-point in-memory instructions are not implemented.           |
| 0b0001 | The specified Atomic floating-point in-memory instructions are implemented. |

FEAT\_LSFE implements the functionality identified by the value 0b0001

Access to this field is RO.

## PACM, bits [15:12]

Indicates the implementation of PSTATE.PACM.

The value of this field is an IMPLEMENTATION DEFINED choice of:

All other values are reserved.

FEAT\_PAuth\_LR implements the functionality identified by the values 0b0001 and 0b0010 .

If FEAT\_PAuth\_LR is implemented, the value 0b0000 is not permitted.

If ID\_AA64ISAR1\_EL1.API is 0b0000 , the value 0b0001 is not permitted.

If one of FEAT\_PACQARMA3 or FEAT\_PACQARMA5 are implemented, the value 0b0001 is not permitted.

Access to this field is RO.

## TLBIW, bits [11:8]

Support for TLBI VMALL for Dirty state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TLBIW   | Meaning                                      |
|---------|----------------------------------------------|
| 0b0000  | TLBI VMALL for Dirty state is not supported. |
| 0b0001  | TLBI VMALL for Dirty state is supported.     |

All other values are reserved.

FEAT\_TLBIW implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## FAMINMAX, bits [7:4]

Indicates support for the following Advanced SIMD, SVE2, and SME2 instructions that compute maximum and minimum absolute value:

- When Advanced SIMD is implemented, the Advanced SIMD instructions FAMAX and FAMIN .
- When FEAT\_SVE2 or FEAT\_SME2 is implemented, the SVE2 instructions FAMAX and FAMIN .
- When FEAT\_SME2 is implemented, the SME2 instructions FAMAX (multiple and single vectors), FAMIN (multiple and single vectors), FAMAX (multiple vectors), and FAMIN (multiple vectors).

The value of this field is an IMPLEMENTATION DEFINED choice of:

| FAMINMAX   | Meaning                                         |
|------------|-------------------------------------------------|
| 0b0000     | The specified instructions are not implemented. |
| 0b0001     | The specified instructions are implemented.     |

All other values are reserved.

| PACM   | Meaning                                |
|--------|----------------------------------------|
| 0b0000 | PSTATE.PACM is not implemented.        |
| 0b0001 | Trivial implementation of PSTATE.PACM. |
| 0b0010 | Full implementation of PSTATE.PACM.    |

FEAT\_FAMINMAX implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## CPA, bits [3:0]

Indicates support for Checked Pointer Arithmetic instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CPA    | Meaning                                                                                                 |
|--------|---------------------------------------------------------------------------------------------------------|
| 0b0000 | Checked Pointer Arithmetic instructions are not implemented.                                            |
| 0b0001 | Checked Pointer Arithmetic instructions are implemented.                                                |
| 0b0010 | Checked Pointer Arithmetic instructions are implemented, and Checked Pointer Arithmetic can be enabled. |

All other values are reserved.

FEAT\_CPA implements the functionality identified by the value 0b0001 .

FEAT\_CPA2 implements the functionality identified by the value 0b0010 .

From Armv9.5, the value 0b0000 is not permitted.

Access to this field is RO.

## Accessing ID\_AA64ISAR3\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ID\_AA64ISAR3\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0110 | 0b011 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_FGT) || !IsZero(ID_AA64ISAR3_EL1) || boolean ↪ → IMPLEMENTATION_DEFINED "ID_AA64ISAR3_EL1 trapped by HCR_EL2.TID3") && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else
```

```
AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64ISAR3_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64ISAR3_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_AA64ISAR3_EL1;
```