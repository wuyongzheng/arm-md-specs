## D24.2.165 RVBAR\_EL3, Reset Vector Base Address Register (if EL3 implemented)

The RVBAR\_EL3 characteristics are:

## Purpose

If EL3 is the highest Exception level implemented, contains the IMPLEMENTATION DEFINED address that execution starts from after reset when executing in AArch64 state.

## Configuration

Only implemented if the highest Exception level implemented is EL3.

This register is present only when EL3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to RVBAR\_EL3 are UNDEFINED.

## Attributes

RVBAR\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

|   63 |   32 |
|------|------|
|   31 |    0 |

## ResetAddress, bits [63:0]

The IMPLEMENTATION DEFINED address that execution starts from after reset when executing in 64-bit state. Bits[1:0] of this register are 00, as this address must be aligned, and the address must be within the physical address size supported by the PE.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing RVBAR\_EL3

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, RVBAR_EL3
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1100 | 0b0000 | 0b001 |

```
if !(HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL3 && IsHighestEL(EL3) then X[t, 64] = RVBAR_EL3; else UNDEFINED;
```