## G8.2.90 ID\_ISAR4, Instruction Set Attribute Register 4

The ID\_ISAR4 characteristics are:

## Purpose

Provides information about the instruction sets implemented by the PE in AArch32 state.

Must be interpreted with ID\_ISAR0, ID\_ISAR1, ID\_ISAR2, ID\_ISAR3, and ID\_ISAR5.

For general information about the interpretation of the ID registers, see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

AArch32 System register ID\_ISAR4 bits [31:0] are architecturally mapped to AArch64 System register ID\_ISAR4\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ID\_ISAR4 are UNDEFINED.

## Attributes

ID\_ISAR4 is a 32-bit register.

## Field descriptions

<!-- image -->

## SWP\_frac, bits [31:28]

Indicates support for the memory system locking the bus for SWP or SWPB instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SWP_frac   | Meaning                                                                                                                                                                                                                          |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000     | SWP or SWPB instructions not implemented.                                                                                                                                                                                        |
| 0b0001     | SWP or SWPB implemented but only in a uniprocessor context. SWP and SWPB do not guarantee whether memory accesses from other Requesters can come between the load memory access and the store memory access of the SWP or SWPB . |

All other values are reserved. This field is valid only if ID\_ISAR0.Swap is 0b0000 .

In Armv8-A, the only permitted value is 0b0000 .

Access to this field is RO.

## PSR\_M, bits [27:24]

Indicates the implemented M-profile instructions to modify the PSRs.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| PSR_M   | Meaning                                                           |
|---------|-------------------------------------------------------------------|
| 0b0000  | None implemented.                                                 |
| 0b0001  | Adds the M-profile forms of the CPS , MRS , and MSR instructions. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0000 .

Access to this field is RO.

## SynchPrim\_frac, bits [23:20]

Used in conjunction with ID\_ISAR3.SynchPrim to indicate the implemented Synchronization Primitive instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SynchPrim_frac   | Meaning                                                                                                                                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000           | If SynchPrim == 0b0000 , no Synchronization Primitives implemented. If SynchPrim == 0b0001 , adds the LDREX and STREX instructions. If SynchPrim == 0b0010 , also adds the CLREX , LDREXB , LDREXH , STREXB , STREXH , LDREXD , and STREXD instructions. |
| 0b0011           | If SynchPrim == 0b0001 , adds the LDREX , STREX , CLREX , LDREXB , LDREXH , STREXB , and STREXH instructions.                                                                                                                                            |

All other combinations of SynchPrim and SynchPrim\_frac are reserved.

In Armv8-A, the only permitted value is 0b0000 .

Access to this field is RO.

## Barrier, bits [19:16]

Indicates support for Barrier instructions DMB , DSB , and ISB in the T32 and A32 instruction sets.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Barrier   | Meaning                                                                                                                 |
|-----------|-------------------------------------------------------------------------------------------------------------------------|
| 0b0000    | None implemented. Barrier operations are provided only as System instructions in the (coproc== 0b1111 ) encoding space. |
| 0b0001    | The specified instructions are implemented.                                                                             |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0001 .

Access to this field is RO.

## SMC, bits [15:12]

Indicates the implemented SMC instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SMC    | Meaning                   |
|--------|---------------------------|
| 0b0000 | None implemented.         |
| 0b0001 | Adds the SMC instruction. |

All other values are reserved.

In Armv8-A, the permitted values are:

- If EL3 is implemented, the only permitted value is 0b0001 .
- If neither EL3 nor EL2 is implemented, the only permitted value is 0b0000 .

Access to this field is RO.

## Writeback, bits [11:8]

Indicates the support for Writeback addressing modes.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Writeback   | Meaning                                                                                                                                                                             |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000      | Basic support. Only the LDM , STM , PUSH , POP , SRS , and RFE instructions support writeback addressing modes. These instructions support all of their writeback addressing modes. |
| 0b0001      | Adds support for all of the writeback addressing modes.                                                                                                                             |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0001 .

Access to this field is RO.

## WithShifts, bits [7:4]

Indicates the support for instructions with shifts.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| WithShifts   | Meaning                                                                                                       |
|--------------|---------------------------------------------------------------------------------------------------------------|
| 0b0000       | Nonzero shifts supported only in MOV and shift instructions.                                                  |
| 0b0001       | Adds support for shifts of loads and stores over the range LSL 0-3.                                           |
| 0b0011       | As for 0b0001 , and adds support for other constant shift options, both on load/store and other instructions. |
| 0b0100       | As for 0b0011 , and adds support for register-controlled shift options.                                       |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0100 .

Access to this field is RO.

## Unpriv, bits [3:0]

Indicates the implemented unprivileged instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Unpriv   | Meaning                                                                        |
|----------|--------------------------------------------------------------------------------|
| 0b0000   | None implemented. No T variant instructions are implemented.                   |
| 0b0001   | Adds the LDRBT , LDRT , STRBT , and STRT instructions.                         |
| 0b0010   | As for 0b0001 , and adds the LDRHT , LDRSBT , LDRSHT , and STRHT instructions. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0010 .

Access to this field is RO.

## Accessing ID\_ISAR4

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0000 | 0b0010 | 0b100  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T0 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T0 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TID3 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TID3 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else R[t] = ID_ISAR4; elsif PSTATE.EL == EL2 then R[t] = ID_ISAR4; elsif PSTATE.EL == EL3 then R[t] = ID_ISAR4;
```