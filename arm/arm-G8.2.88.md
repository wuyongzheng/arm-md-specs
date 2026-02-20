## G8.2.88 ID\_ISAR2, Instruction Set Attribute Register 2

The ID\_ISAR2 characteristics are:

## Purpose

Provides information about the instruction sets implemented by the PE in AArch32 state.

Must be interpreted with ID\_ISAR0, ID\_ISAR1, ID\_ISAR3, ID\_ISAR4, and ID\_ISAR5.

For general information about the interpretation of the ID registers see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

AArch32 System register ID\_ISAR2 bits [31:0] are architecturally mapped to AArch64 System register ID\_ISAR2\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ID\_ISAR2 are UNDEFINED.

## Attributes

ID\_ISAR2 is a 32-bit register.

## Field descriptions

<!-- image -->

## Reversal, bits [31:28]

Indicates the implemented Reversal instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Reversal   | Meaning                                        |
|------------|------------------------------------------------|
| 0b0000     | None implemented.                              |
| 0b0001     | Adds the REV , REV16 , and REVSH instructions. |
| 0b0010     | As for 0b0001 , and adds the RBIT instruction. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0010 .

Access to this field is RO.

## PSR\_AR, bits [27:24]

Indicates the implemented A and R-profile instructions to manipulate the PSR.

The value of this field is an IMPLEMENTATION DEFINED choice of:

MultiAccessInt

| PSR_AR   | Meaning                                                                                            |
|----------|----------------------------------------------------------------------------------------------------|
| 0b0000   | None implemented.                                                                                  |
| 0b0001   | Adds the MRS and MSR instructions, and the exception return forms of data-processing instructions. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0001 .

The exception return forms of the data-processing instructions are:

- In the A32 instruction set, data-processing instructions with the PC as the destination and the S bit set. These instructions might be affected by the WithShifts attribute.
- In the T32 instruction set, the SUBS PC , LR , #N instruction.

Access to this field is RO.

## MultU, bits [23:20]

Indicates the implemented advanced unsigned Multiply instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MultU   | Meaning                                         |
|---------|-------------------------------------------------|
| 0b0000  | None implemented.                               |
| 0b0001  | Adds the UMULL and UMLAL instructions.          |
| 0b0010  | As for 0b0001 , and adds the UMAAL instruction. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0010 .

Access to this field is RO.

## MultS, bits [19:16]

Indicates the implemented advanced signed Multiply instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MultS   | Meaning                                                                                                                                                                                                                          |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000  | None implemented.                                                                                                                                                                                                                |
| 0b0001  | Adds the SMULL and SMLAL instructions.                                                                                                                                                                                           |
| 0b0010  | As for 0b0001 , and adds the SMLABB , SMLABT , SMLALBB , SMLALBT , SMLALTB , SMLALTT , SMLATB , SMLATT , SMLAWB , SMLAWT , SMULBB , SMULBT , SMULTB , SMULTT , SMULWB , and SMULWT instructions. Also adds the Qbit in the PSRs. |
| 0b0011  | As for 0b0010 , and adds the SMLAD , SMLADX , SMLALD , SMLALDX , SMLSD , SMLSDX , SMLSLD , SMLSLDX , SMMLA , SMMLAR , SMMLS , SMMLSR , SMMUL , SMMULR , SMUAD , SMUADX SMUSD , and SMUSDX instructions.                          |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0011 .

Access to this field is RO.

## Mult, bits [15:12]

Indicates the implemented additional Multiply instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Mult   | Meaning                                                                     |
|--------|-----------------------------------------------------------------------------|
| 0b0000 | No additional instructions implemented. This means only MUL is implemented. |
| 0b0001 | Adds the MLA instruction.                                                   |
| 0b0010 | As for 0b0001 , and adds the MLS instruction.                               |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0010 .

Access to this field is RO.

## MultiAccessInt, bits [11:8]

Indicates the support for interruptible multi-access instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MultiAccessInt   | Meaning                                                                    |
|------------------|----------------------------------------------------------------------------|
| 0b0000           | No support. This means the LDM and STM instructions are not interruptible. |
| 0b0001           | LDM and STM instructions are restartable.                                  |
| 0b0010           | LDM and STM instructions are continuable.                                  |

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

| MemHint   | Meaning                                                   |
|-----------|-----------------------------------------------------------|
| 0b0011    | As for 0b0001 (or 0b0010 ), and adds the PLI instruction. |
| 0b0100    | As for 0b0011 , and adds the PLDW instruction.            |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0100 .

Access to this field is RO.

## LoadStore, bits [3:0]

Indicates the implemented additional load/store instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| LoadStore   | Meaning                                                                                                                                                                                     |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000      | No additional load/store instructions implemented.                                                                                                                                          |
| 0b0001      | Adds the LDRD and STRD instructions.                                                                                                                                                        |
| 0b0010      | As for 0b0001 , and adds the Load Acquire ( LDAB , LDAH , LDA , LDAEXB , LDAEXH , LDAEX , LDAEXD ) and Store Release ( STLB , STLH , STL , STLEXB , STLEXH , STLEX , STLEXD ) instructions. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0010 .

Access to this field is RO.

## Accessing ID\_ISAR2

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0000 | 0b0010 | 0b010  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T0 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T0 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TID3 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TID3 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else R[t] = ID_ISAR2; elsif PSTATE.EL == EL2 then R[t] = ID_ISAR2; elsif PSTATE.EL == EL3 then R[t] = ID_ISAR2;
```