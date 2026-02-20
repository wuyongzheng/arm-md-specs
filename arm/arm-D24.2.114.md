## D24.2.114 ID\_PFR0\_EL1, AArch32 Processor Feature Register 0

The ID\_PFR0\_EL1 characteristics are:

## Purpose

Gives top-level information about the instruction sets supported by the PE in AArch32 state.

Must be interpreted with ID\_PFR1\_EL1.

For general information about the interpretation of the ID registers, see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

AArch64 System register ID\_PFR0\_EL1 bits [31:0] are architecturally mapped to AArch32 System register ID\_PFR0[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_PFR0\_EL1 are UNDEFINED.

## Attributes

ID\_PFR0\_EL1 is a 64-bit register.

## Field descriptions

When FEAT\_AA32 is implemented:

<!-- image -->

| 63                                           | 32   | 32   | 32   | 32   | 32   | 32   | 32   | 32   | 32   |
|----------------------------------------------|------|------|------|------|------|------|------|------|------|
| RES0                                         |      |      |      |      |      |      |      |      |      |
| 31 28 27 24 23 20 19 16 15 12 11 8 7 4 3 0   |      |      |      |      |      |      |      |      |      |
| RAS DIT AMU CSV2 State3 State2 State1 State0 |      |      |      |      |      |      |      |      |      |

## Bits [63:32]

Reserved, RES0.

## RAS, bits [31:28]

RAS Extension version.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| RAS    | Meaning                                                                                                                                                                                                                                                                |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | No RAS Extension.                                                                                                                                                                                                                                                      |
| 0b0001 | Support for the Reliability, Availability, and Serviceability Extension is implemented. The ESB instruction and the Error synchronization event are supported.                                                                                                         |
| 0b0010 | As 0b0001 , and adds support for additional ERXMISC<m> System registers. Error records accessed through System registers conform to RAS System Architecture v1.1, which includes simplifications to ERR<n>STATUS and support for the optional RAS Timestamp Extension. |
| 0b0011 | As 0b0010 , and requires that error records accessed through System registers conform to either RAS System Architecture v1.1 or RAS System Architecture v2.                                                                                                            |

All other values are reserved.

FEAT\_RAS implements the functionality identified by the value 0b0001 .

FEAT\_RASv1p1 implements the functionality identified by the value 0b0010 .

FEAT\_RASv2 implements the functionality identified by the value 0b0011 .

In Armv8.0 and Armv8.1, the permitted values are 0b0000 and 0b0001 .

From Armv8.2, the value 0b0000 is not permitted.

From Armv8.4, if FEAT\_DoubleFault is implemented or ERRIDR\_EL1.NUM is nonzero, the value 0b0001 is not permitted.

Note

When the value of this field is 0b0001 , ID\_PFR2\_EL1.RAS\_frac indicates whether FEAT\_RASv1p1 is implemented.

From Armv8.9, if ERRIDR\_EL1.NUM is nonzero, the value 0b0010 is not permitted.

Access to this field is RO.

## DIT, bits [27:24]

Data Independent Timing.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| DIT    | Meaning                                                                                                 |
|--------|---------------------------------------------------------------------------------------------------------|
| 0b0000 | AArch32 does not guarantee constant execution time of any instructions.                                 |
| 0b0001 | AArch32 provides the PSTATE.DIT mechanism to guarantee constant execution time of certain instructions. |

All other values are reserved.

FEAT\_DIT implements the functionality identified by the value 0b0001 .

From Armv8.4, the only permitted value is 0b0001 .

Access to this field is RO.

## AMU,bits [23:20]

Indicates support for Activity Monitors Extension.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| AMU    | Meaning                                                                                                            |
|--------|--------------------------------------------------------------------------------------------------------------------|
| 0b0000 | Activity Monitors Extension is not implemented.                                                                    |
| 0b0001 | FEAT_AMUv1 is implemented.                                                                                         |
| 0b0010 | FEAT_AMUv1p1 is implemented. As 0b0001 and adds support for virtualization of the activity monitor event counters. |

All other values are reserved.

FEAT\_AMUv1 implements the functionality identified by the value 0b0001 .

FEAT\_AMUv1p1 implements the functionality identified by the value 0b0010 .

In Armv8.0, the only permitted value is 0b0000 .

In Armv8.4, the permitted values are 0b0000 and 0b0001 .

From Armv8.6, the permitted values are 0b0000 , 0b0001 , and 0b0010 .

Access to this field is RO.

## CSV2, bits [19:16]

Speculative use of out of context branch targets.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CSV2   | Meaning                                                                |
|--------|------------------------------------------------------------------------|
| 0b0000 | The implementation does not disclose whether FEAT_CSV2 is implemented. |
| 0b0001 | FEAT_CSV2 is implemented, but FEAT_CSV2_1p1 is not implemented.        |
| 0b0010 | FEAT_CSV2_1p1 is implemented.                                          |

All other values are reserved.

FEAT\_CSV2 implements the functionality identified by the value 0b0001 .

FEAT\_CSV2\_1p1 implements the functionality identified by the value 0b0010 .

From Armv8.5, the permitted values are 0b0001 and 0b0010 .

Access to this field is RO.

## State3, bits [15:12]

T32EE instruction set support.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| State3   | Meaning                            |
|----------|------------------------------------|
| 0b0000   | Not implemented.                   |
| 0b0001   | T32EE instruction set implemented. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0000 .

Access to this field is RO.

## State2, bits [11:8]

Jazelle extension support.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| State2   | Meaning                                                                         |
|----------|---------------------------------------------------------------------------------|
| 0b0000   | Not implemented.                                                                |
| 0b0001   | Jazelle extension implemented, without clearing of JOSCR.CV on exception entry. |
| 0b0010   | Jazelle extension implemented, with clearing of JOSCR.CV on exception entry.    |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0001 .

Access to this field is RO.

## State1, bits [7:4]

T32 instruction set support.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| State1   | Meaning                                                                                                                                                                                                            |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000   | T32 instruction set not implemented.                                                                                                                                                                               |
| 0b0001   | T32 encodings before the introduction of Thumb-2 technology implemented: • All instructions are 16-bit. • ABLor BLXis a pair of 16-bit instructions. • 32-bit instructions other than BL and BLXcannot be encoded. |
| 0b0011   | T32 encodings after the introduction of Thumb-2 technology implemented, for all 16-bit and 32-bit T32 basic instructions.                                                                                          |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0011 .

Access to this field is RO.

## State0, bits [3:0]

A32 instruction set support.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| State0   | Meaning                              |
|----------|--------------------------------------|
| 0b0000   | A32 instruction set not implemented. |
| 0b0001   | A32 instruction set implemented.     |

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

## Accessing ID\_PFR0\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ID\_PFR0\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0001 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_PFR0_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_PFR0_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_PFR0_EL1;
```