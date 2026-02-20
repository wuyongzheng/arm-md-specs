## G8.2.86 ID\_ISAR0, Instruction Set Attribute Register 0

The ID\_ISAR0 characteristics are:

## Purpose

Provides information about the instruction sets implemented by the PE in AArch32 state.

Must be interpreted with ID\_ISAR1, ID\_ISAR2, ID\_ISAR3, ID\_ISAR4, and ID\_ISAR5.

For general information about the interpretation of the ID registers see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

AArch32 System register ID\_ISAR0 bits [31:0] are architecturally mapped to AArch64 System register ID\_ISAR0\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ID\_ISAR0 are UNDEFINED.

## Attributes

ID\_ISAR0 is a 32-bit register.

## Field descriptions

| 31   | 28 27   | 24 23   | 20 19   | 16 15     | 12 11    | 8 7      | 4 3   | 0    |
|------|---------|---------|---------|-----------|----------|----------|-------|------|
| RES0 | Divide  | Debug   | Coproc  | CmpBranch | BitField | BitCount |       | Swap |

## Bits [31:28]

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

Indicates support for BitField instructions BFC , BFI , SBFX , and UBFX .

| Debug   | Meaning           |
|---------|-------------------|
| 0b0000  | None implemented. |
| 0b0001  | Adds BKPT .       |

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

## Accessing ID\_ISAR0

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0000 | 0b0010 | 0b000  |

if !IsFeatureImplemented(FEAT\_AA32EL1) then

UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() &amp;&amp; IsFeatureImplemented(FEAT\_AA64EL2) &amp;&amp; !ELUsingAArch32(EL2) &amp;&amp; HSTR\_EL2.T0 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() &amp;&amp; IsFeatureImplemented(FEAT\_AA32EL2) &amp;&amp; ELUsingAArch32(EL2) &amp;&amp; HSTR.T0 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() &amp;&amp; IsFeatureImplemented(FEAT\_AA64EL2) &amp;&amp; !ELUsingAArch32(EL2) &amp;&amp; HCR\_EL2.TID3 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() &amp;&amp; IsFeatureImplemented(FEAT\_AA32EL2) &amp;&amp; ELUsingAArch32(EL2) &amp;&amp; HCR.TID3 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else R[t] = ID\_ISAR0; elsif PSTATE.EL == EL2 then R[t] = ID\_ISAR0; elsif PSTATE.EL == EL3 then R[t] = ID\_ISAR0;