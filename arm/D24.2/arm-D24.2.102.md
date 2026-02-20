## D24.2.102 ID\_ISAR1\_EL1, AArch32 Instruction Set Attribute Register 1

The ID\_ISAR1\_EL1 characteristics are:

## Purpose

Provides information about the instruction sets implemented by the PE in AArch32 state.

Must be interpreted with ID\_ISAR0\_EL1, ID\_ISAR2\_EL1, ID\_ISAR3\_EL1, ID\_ISAR4\_EL1, and ID\_ISAR5\_EL1.

For general information about the interpretation of the ID registers see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

AArch64 System register ID\_ISAR1\_EL1 bits [31:0] are architecturally mapped to AArch32 System register ID\_ISAR1[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_ISAR1\_EL1 are UNDEFINED.

## Attributes

ID\_ISAR1\_EL1 is a 64-bit register.

## Field descriptions

When FEAT\_AA32 is implemented:

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## Jazelle, bits [31:28]

Indicates the implemented Jazelle extension instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Jazelle   | Meaning                                                                                                                           |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------|
| 0b0000    | No support for Jazelle.                                                                                                           |
| 0b0001    | Adds the BXJ instruction and the J bit in the PSR. This setting might indicate a trivial implementation of the Jazelle extension. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0001 .

Access to this field is RO.

## Interwork, bits [27:24]

Indicates the implemented Interworking instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Interwork   | Meaning                                                                                                                                                               |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000      | None implemented.                                                                                                                                                     |
| 0b0001      | Adds the BX instruction, and the T bit in the PSR.                                                                                                                    |
| 0b0010      | As for 0b0001 , and adds the BLX instruction. PC loads have BX-like behavior.                                                                                         |
| 0b0011      | As for 0b0010 , and guarantees that data-processing instructions in the A32 instruction set with the PC as the destination and the S bit clear have BX-like behavior. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0011 .

Access to this field is RO.

## Immediate, bits [23:20]

Indicates support for the following data-processing instructions with long immediates:

- The MOVT instruction.
- The MOV instruction encodings with zero-extended 16-bit immediates.
- The T32 ADD and SUB instruction encodings with zero-extended 12-bit immediates, and the other ADD , ADR , and SUB encodings cross-referenced by the pseudocode for those encodings.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Immediate   | Meaning                                         |
|-------------|-------------------------------------------------|
| 0b0000      | The specified instructions are not implemented. |
| 0b0001      | The specified instructions are implemented.     |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0001 .

Access to this field is RO.

## IfThen, bits [19:16]

Indicates the implemented If-Then instructions in the T32 instruction set.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| IfThen   | Meaning           |
|----------|-------------------|
| 0b0000   | None implemented. |

| 0b0001   | Adds the IT instructions, and the IT bits in the PSRs.   |
|----------|----------------------------------------------------------|

All other values are reserved.

In Armv8-A, the only permitted value is 0b0001 .

Access to this field is RO.

## Extend, bits [15:12]

Indicates the implemented Extend instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Extend   | Meaning                                                                                                                            |
|----------|------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000   | No scalar sign-extend or zero-extend instructions are implemented, where scalar instructions means non-Advanced SIMD instructions. |
| 0b0001   | Adds the SXTB , SXTH , UXTB , and UXTH instructions.                                                                               |
| 0b0010   | As for 0b0001 , and adds the SXTB16 , SXTAB , SXTAB16 , SXTAH , UXTB16 , UXTAB , UXTAB16 , and UXTAH instructions.                 |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0010 .

Access to this field is RO.

## Except\_AR, bits [11:8]

Indicates the implemented A and R-profile exception-handling instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Except_AR   | Meaning                                                                                 |
|-------------|-----------------------------------------------------------------------------------------|
| 0b0000      | None implemented.                                                                       |
| 0b0001      | Adds the SRS and RFE instructions, and the Aand R-profile forms of the CPS instruction. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0001 .

Access to this field is RO.

## Except, bits [7:4]

Indicates the implemented exception-handling instructions in the A32 instruction set.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Except   | Meaning                                                                                                                            |
|----------|------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000   | Not implemented. This indicates that the User bank and Exception return forms of the LDM and STM instructions are not implemented. |
| 0b0001   | Adds the LDM (exception return), LDM (user registers), and STM (user registers) instruction versions.                              |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0001 .

Access to this field is RO.

## Endian, bits [3:0]

Indicates the implemented Endian instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Endian   | Meaning                                                 |
|----------|---------------------------------------------------------|
| 0b0000   | None implemented.                                       |
| 0b0001   | Adds the SETEND instruction, and the E bit in the PSRs. |

All other values are reserved.

In Armv8-A, the permitted values are 0b0000 and 0b0001 .

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

## Accessing ID\_ISAR1\_EL1

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0010 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_ISAR1_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_ISAR1_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_ISAR1_EL1;
```