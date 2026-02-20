## D24.2.16 AMAIR2\_EL3, Extended Auxiliary Memory Attribute Indirection Register (EL3)

The AMAIR2\_EL3 characteristics are:

## Purpose

Provides IMPLEMENTATION DEFINED memory attributes for the memory regions specified by MAIR2\_EL3.

## Configuration

This register is present only when FEAT\_AIE is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to AMAIR2\_EL3 are UNDEFINED.

## Attributes

AMAIR2\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63                     | 32                     |
|------------------------|------------------------|
| IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED |
| 31                     | 0                      |
| IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED |

## IMPLEMENTATIONDEFINED, bits [63:0]

IMPLEMENTATION DEFINED.

## Accessing AMAIR2\_EL3

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, AMAIR2\_EL3

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1010 | 0b0011 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_AIE) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then X[t, 64] = AMAIR2_EL3;
```

MSR AMAIR2\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1010 | 0b0011 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_AIE) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_FGWTE3) && FGWTE3_EL3.AMAIR2_EL3 == '1' then AArch64.SystemAccessTrap(EL3, 0x18); else AMAIR2_EL3 = X[t, 64];
```