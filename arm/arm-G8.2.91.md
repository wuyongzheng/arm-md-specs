## G8.2.91 ID\_ISAR5, Instruction Set Attribute Register 5

The ID\_ISAR5 characteristics are:

## Purpose

Provides information about the instruction sets implemented by the PE in AArch32 state.

Must be interpreted with ID\_ISAR0, ID\_ISAR1, ID\_ISAR2, ID\_ISAR3, and ID\_ISAR4.

For general information about the interpretation of the ID registers see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

AArch32 System register ID\_ISAR5 bits [31:0] are architecturally mapped to AArch64 System register ID\_ISAR5\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ID\_ISAR5 are UNDEFINED.

## Attributes

ID\_ISAR5 is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 28 27   | 24 23   | 20 19   | 16 15   | 12 11   | 8 7   | 4 3   | 0   |
|------|---------|---------|---------|---------|---------|-------|-------|-----|
| VCMA | RDM     | RES0    | CRC32   | SHA2    | SHA1    | AES   | SEVL  |     |

## VCMA,bits [31:28]

Indicates AArch32 support for complex number addition and multiplication where numbers are stored in vectors. The value of this field is an IMPLEMENTATION DEFINED choice of:

| VCMA   | Meaning                                                          |
|--------|------------------------------------------------------------------|
| 0b0000 | The VCMLA and VCADD instructions are not implemented in AArch32. |
| 0b0001 | The VCMLA and VCADD instructions are implemented in AArch32.     |

All other values are reserved.

FEAT\_FCMA implements the functionality identified by 0b0001 .

From Armv8.3, the value 0b0000 is not permitted.

Access to this field is RO.

## RDM,bits [27:24]

Indicates support for the VQRDMLAH and VQRDMLSH instructions in AArch32 state.

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

Indicates support for the CRC32 instructions CRC32B , CRC32H , CRC32W , CRC32CB , CRC32CH , and CRC32CW in AArch32 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CRC32   | Meaning                                     |
|---------|---------------------------------------------|
| 0b0000  | CRC32 instructions are not implemented.     |
| 0b0001  | The specified instructions are implemented. |

All other values are reserved.

FEAT\_CRC32 implements the functionality identified by the value 0b0001 .

From Armv8.1, the value 0b0000 is not permitted.

Access to this field is RO.

## SHA2, bits [15:12]

Indicates support for the SHA2 instructions SHA256H , SHA256H2 , SHA256SU0 , and SHA256SU1 in AArch32 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SHA2   | Meaning                                     |
|--------|---------------------------------------------|
| 0b0000 | No SHA2 instructions implemented.           |
| 0b0001 | The specified instructions are implemented. |

All other values are reserved.

In Armv8-A, the permitted values are 0b0000 and 0b0001 .

Access to this field is RO.

## SHA1, bits [11:8]

Indicates support for the SHA1 instructions SHA1C , SHA1P , SHA1M , SHA1H , SHA1SU0 , and SHA1SU1 in AArch32 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SHA1   | Meaning                                     |
|--------|---------------------------------------------|
| 0b0000 | No SHA1 instructions implemented.           |
| 0b0001 | The specified instructions are implemented. |

All other values are reserved.

In Armv8-A, the permitted values are 0b0000 and 0b0001 .

Access to this field is RO.

## AES, bits [7:4]

Indicates support for the AES instructions in AArch32 state.

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

Indicates support for the SEVL instruction in AArch32 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SEVL   | Meaning                                  |
|--------|------------------------------------------|
| 0b0000 | SEVL is implemented as a NOP.            |
| 0b0001 | SEVL is implemented as Send Event Local. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0001 .

Access to this field is RO.

## Accessing ID\_ISAR5

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0000 | 0b0010 | 0b101  |

if !IsFeatureImplemented(FEAT\_AA32EL1) then

UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() &amp;&amp; IsFeatureImplemented(FEAT\_AA64EL2) &amp;&amp; !ELUsingAArch32(EL2) &amp;&amp; HSTR\_EL2.T0 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() &amp;&amp; IsFeatureImplemented(FEAT\_AA32EL2) &amp;&amp; ELUsingAArch32(EL2) &amp;&amp; HSTR.T0 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() &amp;&amp; IsFeatureImplemented(FEAT\_AA64EL2) &amp;&amp; !ELUsingAArch32(EL2) &amp;&amp; HCR\_EL2.TID3 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() &amp;&amp; IsFeatureImplemented(FEAT\_AA32EL2) &amp;&amp; ELUsingAArch32(EL2) &amp;&amp; HCR.TID3 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else R[t] = ID\_ISAR5; elsif PSTATE.EL == EL2 then R[t] = ID\_ISAR5; elsif PSTATE.EL == EL3 then R[t] = ID\_ISAR5;