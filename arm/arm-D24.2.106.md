## D24.2.106 ID\_ISAR5\_EL1, AArch32 Instruction Set Attribute Register 5

The ID\_ISAR5\_EL1 characteristics are:

## Purpose

Provides information about the instruction sets implemented by the PE in AArch32 state.

Must be interpreted with ID\_ISAR0\_EL1, ID\_ISAR1\_EL1, ID\_ISAR2\_EL1, ID\_ISAR3\_EL1, and ID\_ISAR4\_EL1.

For general information about the interpretation of the ID registers see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

AArch64 System register ID\_ISAR5\_EL1 bits [31:0] are architecturally mapped to AArch32 System register ID\_ISAR5[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_ISAR5\_EL1 are UNDEFINED.

## Attributes

ID\_ISAR5\_EL1 is a 64-bit register.

## Field descriptions

When FEAT\_AA32 is implemented:

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## VCMA,bits [31:28]

Indicates AArch32 support for complex number addition and multiplication where numbers are stored in vectors.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| VCMA   | Meaning                                                          |
|--------|------------------------------------------------------------------|
| 0b0000 | The VCMLA and VCADD instructions are not implemented in AArch32. |
| 0b0001 | The VCMLA and VCADD instructions are implemented in AArch32.     |

All other values are reserved.

FEAT\_FCMA implements the functionality identified by 0b0001 .

From Armv8.3, the value 0b0000 is not permitted.

Access to this field is RO.

## RDM,bits [27:24]

Indicates whether the VQRDMLAH and VQRDMLSH instructions are implemented in AArch32 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| RDM    | Meaning                                            |
|--------|----------------------------------------------------|
| 0b0000 | No VQRDMLAH and VQRDMLSH instructions implemented. |
| 0b0001 | VQRDMLAH and VQRDMLSH instructions implemented.    |

All other values are reserved.

FEAT\_RDM implements the functionality identified by the value 0b0001 .

From Armv8.1, the value 0b0000 is not permitted.

Access to this field is RO.

## Bits [23:20]

Reserved, RES0.

## CRC32, bits [19:16]

Indicates whether the CRC32 instructions CRC32B , CRC32H , CRC32W , CRC32CB , CRC32CH , and CRC32CW are implemented in AArch32 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CRC32   | Meaning                                     |
|---------|---------------------------------------------|
| 0b0000  | CRC32 instructions are not implemented.     |
| 0b0001  | The specified instructions are implemented. |

All other values are reserved.

FEAT\_CRC32 implements the functionality identified by the value 0b0001 .

In Armv8.0, the permitted values are 0b0000 and 0b0001 .

From Armv8.1, the value 0b0000 is not permitted.

Access to this field is RO.

## SHA2, bits [15:12]

Indicates whether the SHA2 instructions SHA256H , SHA256H2 , SHA256SU0 , and SHA256SU1 are implemented in AArch32 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SHA2   | Meaning                           |
|--------|-----------------------------------|
| 0b0000 | No SHA2 instructions implemented. |

| SHA2   | Meaning                                     |
|--------|---------------------------------------------|
| 0b0001 | The specified instructions are implemented. |

All other values are reserved.

In Armv8-A, the permitted values are 0b0000 and 0b0001 .

Access to this field is RO.

## SHA1, bits [11:8]

Indicates whether the SHA1 instructions SHA1C , SHA1P , SHA1M , SHA1H , SHA1SU0 , and SHA1SU1 are implemented in AArch32 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SHA1   | Meaning                                     |
|--------|---------------------------------------------|
| 0b0000 | No SHA1 instructions implemented.           |
| 0b0001 | The specified instructions are implemented. |

All other values are reserved.

In Armv8-A, the permitted values are 0b0000 and 0b0001 .

Access to this field is RO.

## AES, bits [7:4]

Indicates whether the AES instructions are implemented in AArch32 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| AES    | Meaning                                                                                   |
|--------|-------------------------------------------------------------------------------------------|
| 0b0000 | No AES instructions implemented.                                                          |
| 0b0001 | AESE , AESD , AESMC , and AESIMC implemented.                                             |
| 0b0010 | As for 0b0001 , plus VMULL (polynomial) instructions operating on 64-bit data quantities. |

All other values are reserved.

In Armv8-A, the permitted values are 0b0000 and 0b0010 .

Access to this field is RO.

## SEVL, bits [3:0]

Indicates whether the SEVL instruction is implemented in AArch32 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SEVL   | Meaning                                  |
|--------|------------------------------------------|
| 0b0000 | SEVL is implemented as a NOP.            |
| 0b0001 | SEVL is implemented as Send Event Local. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0001 .

Access to this field is RO.

## Otherwise:

<!-- image -->

## Bits [63:0]

Reserved, UNKNOWN.

## Accessing ID\_ISAR5\_EL1

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0010 | 0b101 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else
```

```
X[t, 64] = ID_ISAR5_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_ISAR5_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_ISAR5_EL1;
```