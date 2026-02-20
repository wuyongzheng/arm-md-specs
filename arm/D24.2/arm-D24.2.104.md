## D24.2.104 ID\_ISAR3\_EL1, AArch32 Instruction Set Attribute Register 3

The ID\_ISAR3\_EL1 characteristics are:

## Purpose

Provides information about the instruction sets implemented by the PE in AArch32 state.

Must be interpreted with ID\_ISAR0\_EL1, ID\_ISAR1\_EL1, ID\_ISAR2\_EL1, ID\_ISAR4\_EL1, and ID\_ISAR5\_EL1.

For general information about the interpretation of the ID registers see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

AArch64 System register ID\_ISAR3\_EL1 bits [31:0] are architecturally mapped to AArch32 System register ID\_ISAR3[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_ISAR3\_EL1 are UNDEFINED.

## Attributes

ID\_ISAR3\_EL1 is a 64-bit register.

## Field descriptions

When FEAT\_AA32 is implemented:

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## T32EE, bits [31:28]

Indicates the implemented T32EE instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| T32EE   | Meaning                                                                                          |
|---------|--------------------------------------------------------------------------------------------------|
| 0b0000  | None implemented.                                                                                |
| 0b0001  | Adds the ENTERXand LEAVEX instructions, and modifies the load behavior to include null checking. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0000 .

Access to this field is RO.

## TrueNOP, bits [27:24]

Indicates the implemented true NOP instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TrueNOP   | Meaning                                                                                                                |
|-----------|------------------------------------------------------------------------------------------------------------------------|
| 0b0000    | None implemented. This means there are no NOPinstructions that do not have any register dependencies.                  |
| 0b0001    | Adds true NOPinstructions in both the T32 and A32 instruction sets. This also permits additional NOP-compatible hints. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0001 .

Access to this field is RO.

## T32Copy, bits [23:20]

Indicates the support for T32 non flag-setting MOV instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| T32Copy   | Meaning                                                                                                                                                                |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000    | Not supported. This means that in the T32 instruction set, encoding T1 of the MOV(register) instruction does not support a copy from a low register to a low register. |
| 0b0001    | Adds support for T32 instruction set encoding T1 of the MOV(register) instruction, copying from a low register to a low register.                                      |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0001 .

Access to this field is RO.

## TabBranch, bits [19:16]

Indicates the implemented Table Branch instructions in the T32 instruction set.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TabBranch   | Meaning                           |
|-------------|-----------------------------------|
| 0b0000      | None implemented.                 |
| 0b0001      | Adds the TBB and TBHinstructions. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0001 .

Access to this field is RO.

## SynchPrim, bits [15:12]

Used in conjunction with ID\_ISAR4.SynchPrim\_frac to indicate the implemented Synchronization Primitive instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SynchPrim   | Meaning                                                                                                                                                         |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000      | If SynchPrim_frac == 0b0000 , no Synchronization Primitives implemented.                                                                                        |
| 0b0001      | If SynchPrim_frac == 0b0000 , adds the LDREXand STREX instructions. If SynchPrim_frac == 0b0011 , also adds the CLREX, LDREXB, STREXB, and STREXH instructions. |
| 0b0010      | If SynchPrim_frac == 0b0000 , as for [ 0b0001 , 0b0011 ] and also adds the LDREXDand STREXD instructions.                                                       |

All other combinations of SynchPrim and SynchPrim\_frac are reserved.

In Armv8-A, the only permitted value is 0b0010 .

Access to this field is RO.

## SVC, bits [11:8]

Indicates the implemented SVC instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SVC    | Meaning                   |
|--------|---------------------------|
| 0b0000 | Not implemented.          |
| 0b0001 | Adds the SVC instruction. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0001 .

Access to this field is RO.

## SIMD, bits [7:4]

Indicates the implemented SIMD instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SIMD   | Meaning                                                        |
|--------|----------------------------------------------------------------|
| 0b0000 | None implemented.                                              |
| 0b0001 | Adds the SSAT and USAT instructions, and the Qbit in the PSRs. |

| SIMD   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0011 | As for 0b0001 , and adds the PKHBT, PKHTB, QADD16, QADD8, QASX, QSUB16, QSUB8, QSAX, SADD16, SADD8, SASX, SEL, SHADD16, SHADD8, SHASX, SHSUB16, SHSUB8, SHSAX, SSAT16, SSUB16, SSUB8, SSAX, SXTAB16, SXTB16, UADD16, UADD8, UASX, UHADD16, UHADD8, UHASX, UHSUB16, UHSUB8, UHSAX, UQADD16, UQADD8, UQASX, UQSUB16, UQSUB8, UQSAX, USAD8, USADA8, USAT16, USUB16, USUB8, USAX, UXTAB16, and UXTB16 instructions. Also adds support for the GE[3:0] bits in the PSRs. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0011 .

The SIMD field relates only to implemented instructions that perform SIMD operations on the general-purpose registers. In an implementation that supports Advanced SIMD and floating-point instructions, MVFR0, MVFR1, and MVFR2 give information about the implemented Advanced SIMD instructions.

Access to this field is RO.

## Saturate, bits [3:0]

Indicates the implemented Saturate instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Saturate   | Meaning                                                                                  |
|------------|------------------------------------------------------------------------------------------|
| 0b0000     | None implemented. This means no non-Advanced SIMD saturate instructions are implemented. |
| 0b0001     | Adds the QADD, QDADD, QDSUB, and QSUBinstructions, and the Qbit in the PSRs.             |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0001 .

Access to this field is RO.

## Otherwise:

<!-- image -->

| 63      | 32   |
|---------|------|
| UNKNOWN |      |
| 31      | 0    |
| UNKNOWN |      |

## Bits [63:0]

Reserved, UNKNOWN.

## Accessing ID\_ISAR3\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ID\_ISAR3\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0010 | 0b011 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_ISAR3_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_ISAR3_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_ISAR3_EL1;
```