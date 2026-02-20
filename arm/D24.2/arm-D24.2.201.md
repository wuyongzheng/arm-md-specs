## D24.2.201 TFSR\_EL3, Tag Fault Status Register (EL3)

The TFSR\_EL3 characteristics are:

## Purpose

Holds accumulated Tag Check Faults occurring in EL3 that are not taken precisely.

## Configuration

This register is present only when FEAT\_MTE\_ASYNC is implemented. Otherwise, direct accesses to TFSR\_EL3 are UNDEFINED.

## Attributes

TFSR\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:1]

Reserved, RES0.

## TF0, bit [0]

## When FEAT\_MTE\_ASYNC is implemented:

Tag Check Fault. Asynchronously set to 1 when a Tag Check Fault using a virtual address with bit[55] == 0b0 occurs.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Accessing TFSR\_EL3

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0101 | 0b0110 | 0b000 |

```
if !IsFeatureImplemented(FEAT_MTE_ASYNC) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then X[t, 64] = TFSR_EL3;
```

MSR TFSR\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0101 | 0b0110 | 0b000 |

```
if !IsFeatureImplemented(FEAT_MTE_ASYNC) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then TFSR_EL3 = X[t, 64];
```