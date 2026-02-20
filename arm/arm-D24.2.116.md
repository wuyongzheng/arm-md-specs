## D24.2.116 ID\_PFR2\_EL1, AArch32 Processor Feature Register 2

The ID\_PFR2\_EL1 characteristics are:

## Purpose

Gives information about the AArch32 programmers' model.

Must be interpreted with ID\_PFR0\_EL1 and ID\_PFR1\_EL1.

For general information about the interpretation of the ID registers see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

Note

Prior to the introduction of the features described by this register, this register was unnamed and reserved, RES0 from EL1, EL2, and EL3.

AArch64 System register ID\_PFR2\_EL1 bits [31:0] are architecturally mapped to AArch32 System register ID\_PFR2[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_PFR2\_EL1 are UNDEFINED.

## Attributes

ID\_PFR2\_EL1 is a 64-bit register.

## Field descriptions

When FEAT\_AA32 is implemented:

<!-- image -->

## Bits [63:12]

Reserved, RES0.

## RAS\_frac, bits [11:8]

RAS Extension fractional field.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| RAS_frac   | Meaning                                                                                                                |
|------------|------------------------------------------------------------------------------------------------------------------------|
| 0b0000     | If ID_PFR0_EL1.RAS == 0b0001 , Support for the Reliability, Availability, and Serviceability Extension is implemented. |

| RAS_frac   | Meaning                                                                                                                                                                                                                                                                                             |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0001     | If ID_PFR0_EL1.RAS == 0b0001 , as 0b0000 and adds support for additional ERXMISC<m> System registers. Error records accessed through System registers conform to RAS System Architecture v1.1, which includes simplifications to ERR<n>STATUS and support for the optional RAS Timestamp Extension. |

All other values are reserved.

FEAT\_RAS implements the functionality identified by the value 0b0000 .

FEAT\_RASv1p1 implements the functionality identified by the value 0b0001 .

This field is valid only if ID\_PFR0\_EL1.RAS == 0b0001 .

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

| CSV3   | Meaning                                                                                                                                                                                                                                                                                                                                                        |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | This PE does not disclose whether data loaded under speculation with a permission or domain fault can be used to form an address or generate condition codes or SVE predicate values to be used by other instructions in the speculative sequence.                                                                                                             |
| 0b0001 | Data loaded under speculation with a permission or domain fault cannot be used to form an address, generate condition codes, or generate SVE predicate values to be used by other instructions in the speculative sequence. The execution timing of any other instructions in the speculative sequence is not a function of the data loaded under speculation. |

All other values are reserved.

FEAT\_CSV3 implements the functionality identified by the value 0b0001 .

In Armv8.0, the permitted values are 0b0000 and 0b0001 .

From Armv8.5, the only permitted value is 0b0001 .

If FEAT\_E0PD is implemented, FEAT\_CSV3 must be implemented.

Access to this field is RO.

## Otherwise:

<!-- image -->

## Bits [63:0]

Reserved, UNKNOWN.

## Accessing ID\_PFR2\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ID\_PFR2\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0011 | 0b100 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_FGT) || !IsZero(ID_PFR2_EL1) || boolean ↪ → IMPLEMENTATION_DEFINED "ID_PFR2_EL1 trapped by HCR_EL2.TID3") && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_PFR2_EL1; elsif PSTATE.EL == EL2 then
```

```
if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_PFR2_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_PFR2_EL1;
```