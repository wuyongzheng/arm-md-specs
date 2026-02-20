## D24.2.158 RMR\_EL1, Reset Management Register (EL1)

The RMR\_EL1 characteristics are:

## Purpose

When this register is implemented:

- Awrite to the register at EL1 can request a Warm reset.
- If EL1 can use all Execution states, this register specifies the Execution state that the PE boots into on a Warm reset.

## Configuration

When EL1 is the highest implemented Exception level:

- If EL1 can use all Execution states then this register must be implemented.
- If EL1 cannot use AArch32 then it is IMPLEMENTATION DEFINED whether the register is implemented.

When the highest implemented Exception level is EL1, AArch64 System register RMR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register RMR[31:0].

This register is present only when the highest implemented Exception level is EL1 and FEAT\_AA64 is implemented. Otherwise, direct accesses to RMR\_EL1 are UNDEFINED.

## Attributes

RMR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:2]

Reserved, RES0.

## RR, bit [1]

Reset Request. Setting this bit to 1 requests a Warm reset.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## AA64, bit [0]

When EL1 can use AArch32, determines which Execution state the PE boots into after a Warm reset:

| AA64   | Meaning   |
|--------|-----------|
| 0b0    | AArch32.  |

| AA64   | Meaning   |
|--------|-----------|
| 0b1    | AArch64.  |

On coming out of the Warm reset, execution starts at the IMPLEMENTATION DEFINED reset vector address of the specified Execution state.

If EL1 can only use AArch64 state, this bit is RAO/WI.

The reset behavior of this field is:

- On a Cold reset, this field resets to '1' .

## Accessing RMR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, RMR_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1100 | 0b0000 | 0b010 |

```
if !(IsHighestEL(EL1) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL1 && IsHighestEL(EL1) then X[t, 64] = RMR_EL1; else UNDEFINED;
```

```
MSR RMR_EL1, <Xt>
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1100 | 0b0000 | 0b010 |

```
if !(IsHighestEL(EL1) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL1 && IsHighestEL(EL1) then RMR_EL1 = X[t, 64]; else UNDEFINED;
```