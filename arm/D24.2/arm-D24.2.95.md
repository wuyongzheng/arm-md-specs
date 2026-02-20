## D24.2.95 ID\_AA64PFR2\_EL1, AArch64 Processor Feature Register 2

The ID\_AA64PFR2\_EL1 characteristics are:

## Purpose

Provides additional information about implemented PE features in AArch64 state.

For general information about the interpretation of the ID registers, see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

Note

Prior to the introduction of the features described by this register, this register was unnamed and reserved, RES0 from EL1, EL2, and EL3.

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_AA64PFR2\_EL1 are UNDEFINED.

## Attributes

ID\_AA64PFR2\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:36]

Reserved, RES0.

## FPMR, bits [35:32]

Indicates support for FPMR.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| FPMR   | Meaning                 |
|--------|-------------------------|
| 0b0000 | FPMRis not implemented. |
| 0b0001 | FPMRis implemented.     |

All other values are reserved.

FEAT\_FPMR implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## Bits [31:20]

Reserved, RES0.

## UINJ, bits [19:16]

Support for software injection of Undefined Instruction exceptions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| UINJ   | Meaning                                                                    |
|--------|----------------------------------------------------------------------------|
| 0b0000 | Software injection of Undefined Instruction exceptions is not implemented. |
| 0b0001 | Software injection of Undefined Instruction exceptions is implemented.     |

FEAT\_UINJ implements the functionality identified by the value 0b0001 .

From Armv9.6, the value 0b0000 is not permitted.

Access to this field is RO.

## Bits [15:12]

Reserved, RES0.

## MTEFAR, bits [11:8]

Indicates whether FAR\_ELx[63:60] are UNKNOWN on a synchronous exception due to a Tag Check Fault.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MTEFAR   | Meaning                                                                              |
|----------|--------------------------------------------------------------------------------------|
| 0b0000   | On a synchronous exception due to a Tag Check Fault, FAR_ELx[63:60] are UNKNOWN.     |
| 0b0001   | On a synchronous exception due to a Tag Check Fault, FAR_ELx[63:60] are not UNKNOWN. |

All other values are reserved.

FEAT\_MTE\_TAGGED\_FAR implements the functionality identified by the value 0b0001 .

If FEAT\_MTE2 is not implemented, the value 0b0001 is not permitted.

From Armv8.9, if FEAT\_MTE2 is implemented, the value 0b0000 is not permitted.

Access to this field is RO.

## MTESTOREONLY, bits [7:4]

Support for Store-only Tag checking.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MTESTOREONLY   | Meaning                                   |
|----------------|-------------------------------------------|
| 0b0000         | Store-only Tag checking is not supported. |
| 0b0001         | Store-only Tag checking is supported.     |

All other values are reserved.

FEAT\_MTE\_STORE\_ONLY implements the functionality identified by the value 0b0001 .

If FEAT\_MTE2 is not implemented, the value 0b0001 is not permitted.

From Armv8.9, if FEAT\_MTE2 is implemented, the value 0b0000 is not permitted.

Access to this field is RO.

## MTEPERM,bits [3:0]

Support for Allocation tag access permissions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MTEPERM   | Meaning                                                                                                        |
|-----------|----------------------------------------------------------------------------------------------------------------|
| 0b0000    | Allocation tag access permissions are not supported.                                                           |
| 0b0001    | Allocation tag access permissions are supported. Note NoTagAccess is supported at stage 2 of translation only. |

All other values are reserved.

FEAT\_MTE\_PERM implements the functionality identified by the value 0b0001

If FEAT\_MTE2 is not implemented, the value 0b0001 is not permitted.

From Armv8.9, if FEAT\_MTE2 is implemented, the value 0b0000 is not permitted.

Access to this field is RO.

## Accessing ID\_AA64PFR2\_EL1

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0100 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED;
```

```
elsif EL2Enabled() && (IsFeatureImplemented(FEAT_FGT) || !IsZero(ID_AA64PFR2_EL1) || boolean ↪ → IMPLEMENTATION_DEFINED "ID_AA64PFR2_EL1 trapped by HCR_EL2.TID3") && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64PFR2_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64PFR2_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_AA64PFR2_EL1;
```