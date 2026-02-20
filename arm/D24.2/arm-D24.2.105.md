## D24.2.105 ID\_ISAR4\_EL1, AArch32 Instruction Set Attribute Register 4

The ID\_ISAR4\_EL1 characteristics are:

## Purpose

Provides information about the instruction sets implemented by the PE in AArch32 state.

Must be interpreted with ID\_ISAR0\_EL1, ID\_ISAR1\_EL1, ID\_ISAR2\_EL1, ID\_ISAR3\_EL1, and ID\_ISAR5\_EL1.

For general information about the interpretation of the ID registers, see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

AArch64 System register ID\_ISAR4\_EL1 bits [31:0] are architecturally mapped to AArch32 System register ID\_ISAR4[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_ISAR4\_EL1 are UNDEFINED.

## Attributes

ID\_ISAR4\_EL1 is a 64-bit register.

## Field descriptions

When FEAT\_AA32 is implemented:

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## SWP\_frac, bits [31:28]

Indicates support for the memory system locking the bus for SWP or SWPB instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SWP_frac   | Meaning                                                                                                                                                                                                                    |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000     | SWPor SWPBinstructions not implemented.                                                                                                                                                                                    |
| 0b0001     | SWPor SWPBimplemented but only in a uniprocessor context. SWPand SWPBdo not guarantee whether memory accesses from other Requesters can come between the load memory access and the store memory access of the SWPor SWPB. |

All other values are reserved. This field is valid only if ID\_ISAR0.Swap is 0b0000 .

In Armv8-A, the only permitted value is 0b0000 .

Access to this field is RO.

## PSR\_M, bits [27:24]

Indicates the implemented M-profile instructions to modify the PSRs.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| PSR_M   | Meaning                                                        |
|---------|----------------------------------------------------------------|
| 0b0000  | None implemented.                                              |
| 0b0001  | Adds the M-profile forms of the CPS, MRS, and MSRinstructions. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0000 .

Access to this field is RO.

## SynchPrim\_frac, bits [23:20]

Used in conjunction with ID\_ISAR3.SynchPrim to indicate the implemented Synchronization Primitive instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SynchPrim_frac   | Meaning                                                                                                                                                                                                                                           |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000           | If SynchPrim == 0b0000 , no Synchronization Primitives implemented. If SynchPrim == 0b0001 , adds the LDREXand STREX instructions. If SynchPrim == 0b0010 , also adds the CLREX, LDREXB, LDREXH, STREXB, STREXH, LDREXD, and STREXD instructions. |
| 0b0011           | If SynchPrim == 0b0001 , adds the LDREX, STREX, CLREX, LDREXB, LDREXH, STREXB, and STREXH instructions.                                                                                                                                           |

All other combinations of SynchPrim and SynchPrim\_frac are reserved.

In Armv8-A, the only permitted value is 0b0000 .

Access to this field is RO.

## Barrier, bits [19:16]

Indicates the implemented Barrier instructions in the T32 and A32 instruction sets.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Barrier   | Meaning                                                                                                                 |
|-----------|-------------------------------------------------------------------------------------------------------------------------|
| 0b0000    | None implemented. Barrier operations are provided only as System instructions in the (coproc== 0b1111 ) encoding space. |
| 0b0001    | Adds the DMB, DSB, and ISB barrier instructions.                                                                        |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0001 .

Access to this field is RO.

## SMC, bits [15:12]

Indicates the implemented SMC instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SMC    | Meaning                  |
|--------|--------------------------|
| 0b0000 | None implemented.        |
| 0b0001 | Adds the SMCinstruction. |

All other values are reserved.

In Armv8-A, the permitted values are:

- If EL3 is implemented and EL1 can use AArch32, the only permitted value is 0b0001 .
- If neither EL3 nor EL2 is implemented, the only permitted value is 0b0000 .

If EL1 cannot use AArch32, this field has the value 0b0000 .

Access to this field is RO.

## Writeback, bits [11:8]

Indicates the support for Writeback addressing modes.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Writeback   | Meaning                                                                                                                                                                        |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000      | Basic support. Only the LDM, STM, PUSH, POP, SRS, and RFE instructions support writeback addressing modes. These instructions support all of their writeback addressing modes. |
| 0b0001      | Adds support for all of the writeback addressing modes.                                                                                                                        |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0001 .

Access to this field is RO.

## WithShifts, bits [7:4]

Indicates the support for instructions with shifts.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| WithShifts   | Meaning                                                                                                       |
|--------------|---------------------------------------------------------------------------------------------------------------|
| 0b0000       | Nonzero shifts supported only in MOVandshift instructions.                                                    |
| 0b0001       | Adds support for shifts of loads and stores over the range LSL 0-3.                                           |
| 0b0011       | As for 0b0001 , and adds support for other constant shift options, both on load/store and other instructions. |
| 0b0100       | As for 0b0011 , and adds support for register-controlled shift options.                                       |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0100 .

Access to this field is RO.

## Unpriv, bits [3:0]

Indicates the implemented unprivileged instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Unpriv   | Meaning                                                                     |
|----------|-----------------------------------------------------------------------------|
| 0b0000   | None implemented. No T variant instructions are implemented.                |
| 0b0001   | Adds the LDRBT, LDRT, STRBT, and STRT instructions.                         |
| 0b0010   | As for 0b0001 , and adds the LDRHT, LDRSBT, LDRSHT, and STRHT instructions. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0010 .

Access to this field is RO.

## Otherwise:

<!-- image -->

|   63 |   32 |
|------|------|
|   31 |    0 |

## Bits [63:0]

Reserved, UNKNOWN.

## Accessing ID\_ISAR4\_EL1

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0010 | 0b100 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_ISAR4_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_ISAR4_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_ISAR4_EL1;
```