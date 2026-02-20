## D24.2.4 ACTLR\_EL3, Auxiliary Control Register (EL3)

The ACTLR\_EL3 characteristics are:

## Purpose

Provides IMPLEMENTATION DEFINED configuration and control options for EL3.

## Configuration

This register is present only when EL3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to ACTLR\_EL3 are UNDEFINED.

## Attributes

ACTLR\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63                     | 32                     |
|------------------------|------------------------|
| IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED |
| 31                     | 0                      |
| IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED |

## IMPLEMENTATIONDEFINED, bits [63:0]

IMPLEMENTATION DEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing ACTLR\_EL3

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ACTLR\_EL3

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0001 | 0b0000 | 0b001 |

| if !(HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64)) UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then X[t, 64] = ACTLR_EL3;   | then   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|

MSR ACTLR\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0001 | 0b0000 | 0b001 |

```
if !(HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_FGWTE3) && FGWTE3_EL3.ACTLR_EL3 == '1' then AArch64.SystemAccessTrap(EL3, 0x18); else ACTLR_EL3 = X[t, 64];
```