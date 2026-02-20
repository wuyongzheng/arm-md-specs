## G8.2.101 ID\_PFR2, Processor Feature Register 2

The ID\_PFR2 characteristics are:

## Purpose

Gives information about the AArch32 programmers' model.

Must be interpreted with ID\_PFR0 and ID\_PFR1.

For general information about the interpretation of the ID registers see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

AArch32 System register ID\_PFR2 bits [31:0] are architecturally mapped to AArch64 System register ID\_PFR2\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ID\_PFR2 are UNDEFINED.

## Attributes

ID\_PFR2 is a 32-bit register.

## Field descriptions

| 31   | 12 11    |      |      |
|------|----------|------|------|
| RES0 | RAS_frac | SSBS | CSV3 |

## Bits [31:12]

Reserved, RES0.

## RAS\_frac, bits [11:8]

RAS Extension fractional field.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| RAS_frac   | Meaning                                                                                                                                                                                                                                                                                         |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000     | If ID_PFR0.RAS == 0b0001 , support for the Reliability, Availability, and Serviceability Extension is implemented.                                                                                                                                                                              |
| 0b0001     | If ID_PFR0.RAS == 0b0001 , as 0b0000 and adds support for additional ERXMISC<m> System registers. Error records accessed through System registers conform to RAS System Architecture v1.1, which includes simplifications to ERR<n>STATUS and support for the optional RAS Timestamp Extension. |

All other values are reserved.

FEAT\_RAS implements the functionality identified by the value 0b0000 .

FEAT\_RASv1p1 implements the functionality identified by the value 0b0001 .

This field is valid only if ID\_PFR0.RAS == 0b0001 .

Access to this field is RO.

## SSBS, bits [7:4]

Speculative Store Bypassing controls in AArch64 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SSBS   | Meaning                                                                                            |
|--------|----------------------------------------------------------------------------------------------------|
| 0b0000 | AArch32 provides no mechanism to control the use of Speculative Store Bypassing.                   |
| 0b0001 | AArch32 provides the PSTATE.SSBS mechanism to mark regions that are Speculative Store Bypass Safe. |

In Armv8.0, the permitted values are 0b0000 and 0b0001 .

From Armv8.5, the only permitted value is 0b0001 .

All other values are reserved.

Access to this field is RO.

## CSV3, bits [3:0]

Speculative use of faulting data.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CSV3   | Meaning                                                                                                                                                                                                                                                                                                                                            |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | This PE does not disclose whether data loaded or read from a register under speculation where the data load or register read would not be permitted architecturally, can be used by instructions newer than the load or register read in a manner that allows the value of the inaccessible data to be recovered by code architecturally executed. |
| 0b0001 | Data loaded or read from a register under speculation where the data load or register read would not be permitted architecturally, cannot be used by instructions newer than the load or register read in a manner that allows the value of the inaccessible data to be recovered by code architecturally executed.                                |

All other values are reserved.

FEAT\_CSV3 implements the functionality identified by the value 0b0001 .

In Armv8.0, the permitted values are 0b0000 and 0b0001 .

From Armv8.5, the only permitted value is 0b0001 .

If FEAT\_E0PD is implemented, FEAT\_CSV3 must be implemented.

Access to this field is RO.

## Accessing ID\_PFR2

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0000 | 0b0011 | 0b100  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T0 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T0 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TID3 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TID3 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else R[t] = ID_PFR2; elsif PSTATE.EL == EL2 then R[t] = ID_PFR2; elsif PSTATE.EL == EL3 then R[t] = ID_PFR2;
```