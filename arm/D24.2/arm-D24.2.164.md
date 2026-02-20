## D24.2.164 RVBAR\_EL2, Reset Vector Base Address Register (if EL3 not implemented)

The RVBAR\_EL2 characteristics are:

## Purpose

If EL2 is the highest Exception level implemented, contains the IMPLEMENTATION DEFINED address that execution starts from after reset when executing in AArch64 state.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register is present only when the highest implemented Exception level is EL2 and FEAT\_AA64 is implemented. Otherwise, direct accesses to RVBAR\_EL2 are UNDEFINED.

## Attributes

RVBAR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   |              | 32   |
|------|--------------|------|
|      | ResetAddress |      |
| 31   |              | 0    |
|      | ResetAddress |      |

## ResetAddress, bits [63:0]

The IMPLEMENTATION DEFINED address that execution starts from after reset when executing in 64-bit state. Bits[1:0] of this register are 00, as this address must be aligned, and the address must be within the physical address size supported by the PE.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing RVBAR\_EL2

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, RVBAR_EL2
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1100 | 0b0000 | 0b001 |

```
if !(IsHighestEL(EL2) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL1 && IsHighestEL(EL2) && EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif PSTATE.EL == EL2 && IsHighestEL(EL2) then X[t, 64] = RVBAR_EL2; else UNDEFINED;
```