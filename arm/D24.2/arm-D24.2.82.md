## D24.2.82 ID\_AA64DFR2\_EL1, AArch64 Debug Feature Register 2

The ID\_AA64DFR2\_EL1 characteristics are:

## Purpose

Provides top-level information about the debug system in AArch64.

For general information about the interpretation of the ID registers, see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

Note

Prior to the introduction of the features described by this register, this register was unnamed and reserved, RES0 from EL1, EL2, and EL3.

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_AA64DFR2\_EL1 are UNDEFINED.

## Attributes

ID\_AA64DFR2\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:28]

Reserved, RES0.

## TRBE\_EXC, bits [27:24]

TRBE Profiling exception extension. Describes support for reporting trace buffer management events as TRBE Profiling exceptions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TRBE_EXC   | Meaning                                   |
|------------|-------------------------------------------|
| 0b0000     | TRBE Profiling exception not implemented. |
| 0b0001     | TRBE Profiling exception implemented.     |

All other values are reserved.

FEAT\_TRBE\_EXC implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## SPE\_nVM, bits [23:20]

Profiling Buffer physical address mode supported. Describes support for defining the Profiling Buffer using physical addresses or intermediate physical addresses.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SPE_nVM   | Meaning                                                 |
|-----------|---------------------------------------------------------|
| 0b0000    | Profiling Buffer physical address mode not implemented. |
| 0b0001    | Profiling Buffer physical address mode implemented.     |

All other values are reserved.

FEAT\_SPE\_nVM implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## SPE\_EXC, bits [19:16]

SPE Profiling exception extension. Describes support for reporting Profiling Buffer management events as SPE Profiling exceptions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SPE_EXC   | Meaning                                  |
|-----------|------------------------------------------|
| 0b0000    | SPE Profiling exception not implemented. |
| 0b0001    | SPE Profiling exception implemented.     |

All other values are reserved.

FEAT\_SPE\_EXC implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## Bits [15:8]

Reserved, RES0.

## BWE, bits [7:4]

Breakpoints and watchpoint enhancements.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| BWE    | Meaning                                                                                                   |
|--------|-----------------------------------------------------------------------------------------------------------|
| 0b0000 | This field does not indicate whether DBGBCR<n>_EL1.MASK and address mismatch breakpoints are implemented. |
| 0b0001 | DBGBCR<n>_EL1.MASK and address mismatch breakpoints are implemented.                                      |
| 0b0010 | As 0b0001 , and address mismatch watchpoints are implemented.                                             |

All other values are reserved.

FEAT\_BWE implements the functionality identified by the value 0b0001 .

FEAT\_BWE2 implements the functionality identified by the value 0b0010 .

When this field is 0b0000 , ID\_AA64DFR1\_EL1.ABLE might indicate the presence of support for DBGBCR&lt;n&gt;\_EL1.MASK and address mismatch breakpoints.

From Armv9.5, the value 0b0001 is not permitted.

Access to this field is RO.

## STEP, bits [3:0]

Enhanced Software Step Extension.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| STEP   | Meaning                                                         |
|--------|-----------------------------------------------------------------|
| 0b0000 | Execution from MDSTEPOP_EL1 is not supported for Software Step. |
| 0b0001 | Execution from MDSTEPOP_EL1 is supported for Software Step.     |

All other values are reserved.

FEAT\_STEP2 implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## Accessing ID\_AA64DFR2\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ID\_AA64DFR2\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0101 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_FGT) || !IsZero(ID_AA64DFR2_EL1) || boolean ↪ → IMPLEMENTATION_DEFINED "ID_AA64DFR2_EL1 trapped by HCR_EL2.TID3") && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else
```

```
AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64DFR2_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64DFR2_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_AA64DFR2_EL1;
```