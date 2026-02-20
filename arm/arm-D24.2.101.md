## D24.2.101 ID\_ISAR0\_EL1, AArch32 Instruction Set Attribute Register 0

The ID\_ISAR0\_EL1 characteristics are:

## Purpose

Provides information about the instruction sets implemented by the PE in AArch32 state.

Must be interpreted with ID\_ISAR1\_EL1, ID\_ISAR2\_EL1, ID\_ISAR3\_EL1, ID\_ISAR4\_EL1, and ID\_ISAR5\_EL1.

For general information about the interpretation of the ID registers see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

AArch64 System register ID\_ISAR0\_EL1 bits [31:0] are architecturally mapped to AArch32 System register ID\_ISAR0[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_ISAR0\_EL1 are UNDEFINED.

## Attributes

ID\_ISAR0\_EL1 is a 64-bit register.

## Field descriptions

When FEAT\_AA32 is implemented:

<!-- image -->

## Bits [63:28]

Reserved, RES0.

## Divide, bits [27:24]

Indicates the implemented Divide instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Divide   | Meaning                                                            |
|----------|--------------------------------------------------------------------|
| 0b0000   | None implemented.                                                  |
| 0b0001   | Adds SDIV and UDIV in the T32 instruction set.                     |
| 0b0010   | As for 0b0001 , and adds SDIV and UDIV in the A32 instruction set. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0010 .

Access to this field is RO.

## Debug, bits [23:20]

Indicates the implemented Debug instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Debug   | Meaning           |
|---------|-------------------|
| 0b0000  | None implemented. |
| 0b0001  | Adds BKPT .       |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0001 .

Access to this field is RO.

## Coproc, bits [19:16]

Indicates the implemented System register access instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Coproc   | Meaning                                                                                                                                                    |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000   | None implemented, except for instructions separately attributed by the architecture to provide access to AArch32 System registers and System instructions. |
| 0b0001   | Adds generic CDP , LDC , MCR , MRC , and STC .                                                                                                             |
| 0b0010   | As for 0b0001 , and adds generic CDP2 , LDC2 , MCR2 , MRC2 , and STC2 .                                                                                    |
| 0b0011   | As for 0b0010 , and adds generic MCRR and MRRC .                                                                                                           |
| 0b0100   | As for 0b0011 , and adds generic MCRR2 and MRRC2 .                                                                                                         |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0000 .

Access to this field is RO.

## CmpBranch, bits [15:12]

Indicates the implemented combined Compare and Branch instructions in the T32 instruction set.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CmpBranch   | Meaning             |
|-------------|---------------------|
| 0b0000      | None implemented.   |
| 0b0001      | Adds CBNZ and CBZ . |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0001 .

Access to this field is RO.

## BitField, bits [11:8]

Indicates support for the following BitField instructions BFC , BFI , SBFX , and UBFX .

The value of this field is an IMPLEMENTATION DEFINED choice of:

| BitField   | Meaning                                         |
|------------|-------------------------------------------------|
| 0b0000     | The specified instructions are not implemented. |
| 0b0001     | The specified instructions are implemented.     |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0001 .

Access to this field is RO.

## BitCount, bits [7:4]

Indicates the implemented Bit Counting instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| BitCount   | Meaning           |
|------------|-------------------|
| 0b0000     | None implemented. |
| 0b0001     | Adds CLZ .        |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0001 .

Access to this field is RO.

## Swap, bits [3:0]

Indicates the implemented Swap instructions in the A32 instruction set.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Swap   | Meaning             |
|--------|---------------------|
| 0b0000 | None implemented.   |
| 0b0001 | Adds SWP and SWPB . |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0000 .

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

## Accessing ID\_ISAR0\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ID\_ISAR0\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0010 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_ISAR0_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_ISAR0_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_ISAR0_EL1;
```