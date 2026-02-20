## D24.2.103 ID\_ISAR2\_EL1, AArch32 Instruction Set Attribute Register 2

The ID\_ISAR2\_EL1 characteristics are:

## Purpose

Provides information about the instruction sets implemented by the PE in AArch32 state.

Must be interpreted with ID\_ISAR0\_EL1, ID\_ISAR1\_EL1, ID\_ISAR3\_EL1, ID\_ISAR4\_EL1, and ID\_ISAR5\_EL1.

For general information about the interpretation of the ID registers see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

AArch64 System register ID\_ISAR2\_EL1 bits [31:0] are architecturally mapped to AArch32 System register ID\_ISAR2[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_ISAR2\_EL1 are UNDEFINED.

## Attributes

ID\_ISAR2\_EL1 is a 64-bit register.

## Field descriptions

When FEAT\_AA32 is implemented:

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## Reversal, bits [31:28]

Indicates the implemented Reversal instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Reversal   | Meaning                                        |
|------------|------------------------------------------------|
| 0b0000     | None implemented.                              |
| 0b0001     | Adds the REV, REV16, and REVSH instructions.   |
| 0b0010     | As for 0b0001 , and adds the RBIT instruction. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0010 .

Access to this field is RO.

## PSR\_AR, bits [27:24]

Indicates the implemented A and R-profile instructions to manipulate the PSR.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| PSR_AR   | Meaning                                                                                          |
|----------|--------------------------------------------------------------------------------------------------|
| 0b0000   | None implemented.                                                                                |
| 0b0001   | Adds the MRSand MSRinstructions, and the exception return forms of data-processing instructions. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0001 .

The exception return forms of the data-processing instructions are:

- In the A32 instruction set, data-processing instructions with the PC as the destination and the S bit set. These instructions might be affected by the WithShifts attribute.
- In the T32 instruction set, the SUBS PC,LR,#N instruction.

Access to this field is RO.

## MultU, bits [23:20]

Indicates the implemented advanced unsigned Multiply instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MultU   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0000  | None implemented.                              |
| 0b0001  | Adds the UMULLand UMLALinstructions.           |
| 0b0010  | As for 0b0001 , and adds the UMAALinstruction. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0010 .

Access to this field is RO.

## MultS, bits [19:16]

Indicates the implemented advanced signed Multiply instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MultS   | Meaning                              |
|---------|--------------------------------------|
| 0b0000  | None implemented.                    |
| 0b0001  | Adds the SMULLand SMLALinstructions. |

| MultS   | Meaning                                                                                                                                                                                                          |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0010  | As for 0b0001 , and adds the SMLABB, SMLABT, SMLALBB, SMLALBT, SMLALTB, SMLALTT, SMLATB, SMLATT, SMLAWB, SMLAWT, SMULBB, SMULBT, SMULTB, SMULTT, SMULWB, and SMULWTinstructions. Also adds the Qbit in the PSRs. |
| 0b0011  | As for 0b0010 , and adds the SMLAD, SMLADX, SMLALD, SMLALDX, SMLSD, SMLSDX, SMLSLD, SMLSLDX, SMMLA, SMMLAR, SMMLS, SMMLSR, SMMUL, SMMULR, SMUAD, SMUADX, SMUSD, and SMUSDXinstructions.                          |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0011 .

Access to this field is RO.

## Mult, bits [15:12]

Indicates the implemented additional Multiply instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Mult   | Meaning                                                                    |
|--------|----------------------------------------------------------------------------|
| 0b0000 | No additional instructions implemented. This means only MULis implemented. |
| 0b0001 | Adds the MLAinstruction.                                                   |
| 0b0010 | As for 0b0001 , and adds the MLSinstruction.                               |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0010 .

Access to this field is RO.

## MultiAccessInt, bits [11:8]

Indicates the support for interruptible multi-access instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MultiAccessInt   | Meaning                                                                  |
|------------------|--------------------------------------------------------------------------|
| 0b0000           | No support. This means the LDMand STMinstructions are not interruptible. |
| 0b0001           | LDMand STMinstructions are restartable.                                  |
| 0b0010           | LDMand STMinstructions are continuable.                                  |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0000 .

Access to this field is RO.

## MemHint, bits [7:4]

Indicates the implemented Memory Hint instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MemHint   | Meaning                                                                |
|-----------|------------------------------------------------------------------------|
| 0b0000    | None implemented.                                                      |
| 0b0001    | Adds the PLD instruction.                                              |
| 0b0010    | Adds the PLD instruction. ( 0b0001 and 0b0010 have identical effects.) |
| 0b0011    | As for 0b0001 (or 0b0010 ), and adds the PLI instruction.              |
| 0b0100    | As for 0b0011 , and adds the PLDWinstruction.                          |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0100 .

Access to this field is RO.

## LoadStore, bits [3:0]

Indicates the implemented additional load/store instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| LoadStore   | Meaning                                                                                                                                                                     |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000      | No additional load/store instructions implemented.                                                                                                                          |
| 0b0001      | Adds the LDRDand STRD instructions.                                                                                                                                         |
| 0b0010      | As for 0b0001 , and adds the Load Acquire (LDAB, LDAH, LDA, LDAEXB, LDAEXH, LDAEX, LDAEXD) and Store Release (STLB, STLH, STL, STLEXB, STLEXH, STLEX, STLEXD) instructions. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0010 .

Access to this field is RO.

## Otherwise:

<!-- image -->

## Bits [63:0]

Reserved, UNKNOWN.

## Accessing ID\_ISAR2\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ID\_ISAR2\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0010 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_ISAR2_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_ISAR2_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_ISAR2_EL1;
```