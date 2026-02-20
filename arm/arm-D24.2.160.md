## D24.2.160 RMR\_EL3, Reset Management Register (EL3)

The RMR\_EL3 characteristics are:

## Purpose

If EL3 is implemented and this register is implemented:

- Awrite to the register at EL3 can request a Warm reset.
- If EL3 can use all Execution states, this register specifies the Execution state that the PE boots into on a Warm reset.

## Configuration

When EL3 is implemented:

- If EL3 can use all Execution states then this register must be implemented.
- If EL3 cannot use AArch32, then it is IMPLEMENTATION DEFINED whether the register is implemented.

Otherwise, direct accesses to RMR\_EL3 are UNDEFINED.

When EL3 is implemented, AArch64 System register RMR\_EL3 bits [31:0] are architecturally mapped to AArch32 System register RMR[31:0].

This register is present only when EL3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to RMR\_EL3 are UNDEFINED.

## Attributes

RMR\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:2]

Reserved, RES0.

## RR, bit [1]

Reset Request. Setting this bit to 1 requests a Warm reset.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## AA64, bit [0]

When EL3 can use AArch32, determines which Execution state the PE boots into after a Warm reset:

| AA64   | Meaning   |
|--------|-----------|
| 0b0    | AArch32.  |
| 0b1    | AArch64.  |

On coming out of the Warm reset, execution starts at the IMPLEMENTATION DEFINED reset vector address of the specified Execution state.

If EL3 can only use AArch64 state, this bit is RAO/WI.

The reset behavior of this field is:

- On a Cold reset, this field resets to '1' .

## Accessing RMR\_EL3

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, RMR\_EL3

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1100 | 0b0000 | 0b010 |

```
IsFeatureImplemented(FEAT_AA64)) then
```

```
if !(HaveEL(EL3) && UNDEFINED; elsif PSTATE.EL == EL3 && IsHighestEL(EL3) then X[t, 64] = RMR_EL3; else UNDEFINED;
```

MSR RMR\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1100 | 0b0000 | 0b010 |

```
if !(HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL3 && IsHighestEL(EL3) then RMR_EL3 = X[t, 64]; else UNDEFINED;
```