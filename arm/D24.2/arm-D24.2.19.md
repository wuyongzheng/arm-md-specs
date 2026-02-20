## D24.2.19 AMAIR\_EL3, Auxiliary Memory Attribute Indirection Register (EL3)

The AMAIR\_EL3 characteristics are:

## Purpose

Provides IMPLEMENTATION DEFINED memory attributes for the memory regions specified by MAIR\_EL3.

## Configuration

This register is present only when EL3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to AMAIR\_EL3 are UNDEFINED.

## Attributes

AMAIR\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63                     | 32                     |
|------------------------|------------------------|
| IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED |
| 31                     | 0                      |
| IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED |

AMAIR\_EL3 is permitted to be cached in a TLB.

## IMPLEMENTATIONDEFINED, bits [63:0]

IMPLEMENTATION DEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing AMAIR\_EL3

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, AMAIR_EL3
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1010 | 0b0011 | 0b000 |

```
if !(HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then X[t, 64] = AMAIR_EL3;
```

MSR AMAIR\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1010 | 0b0011 | 0b000 |

```
if !(HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_FGWTE3) && FGWTE3_EL3.AMAIR_EL3 == '1' then AArch64.SystemAccessTrap(EL3, 0x18); else AMAIR_EL3 = X[t, 64];
```