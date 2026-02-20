## D24.2.163 RVBAR\_EL1, Reset Vector Base Address Register (if EL2 and EL3 not implemented)

The RVBAR\_EL1 characteristics are:

## Purpose

If EL1 is the highest Exception level implemented, contains the IMPLEMENTATION DEFINED address that execution starts from after reset when executing in AArch64 state.

## Configuration

This register is present only when the highest implemented Exception level is EL1 and FEAT\_AA64 is implemented. Otherwise, direct accesses to RVBAR\_EL1 are UNDEFINED.

## Attributes

RVBAR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## ResetAddress, bits [63:0]

The IMPLEMENTATION DEFINED address that execution starts from after reset when executing in 64-bit state. Bits[1:0] of this register are 00, as this address must be aligned, and the address must be within the physical address size supported by the PE.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing RVBAR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, RVBAR_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1100 | 0b0000 | 0b001 |

```
if !(IsHighestEL(EL1) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL1 && IsHighestEL(EL1) then X[t, 64] = RVBAR_EL1; else UNDEFINED;
```