## G8.2.124 RMR, Reset Management Register

The RMR characteristics are:

## Purpose

If EL1 or EL3 is the highest implemented Exception level and this register is implemented:

- Awrite to the register at the highest implemented Exception level can request a Warm reset.
- If the highest implemented Exception level can use AArch32 and AArch64, this register specifies the Execution state that the PE boots into on a Warm reset.

## Configuration

Only implemented if EL1 or EL3 is the highest implemented Exception level. In this case:

- If the highest implemented Exception level can use AArch32 and AArch64 then this register must be implemented.
- If the highest implemented Exception level cannot use AArch64 then it is IMPLEMENTATION DEFINED whether the register is implemented.

When the highest implemented Exception level is EL1, AArch32 System register RMR bits [31:0] are architecturally mapped to AArch64 System register RMR\_EL1[31:0].

When EL3 is implemented, AArch32 System register RMR bits [31:0] are architecturally mapped to AArch64 System register RMR\_EL3[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to RMR are UNDEFINED.

## Attributes

RMRis a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:2]

Reserved, RES0.

## RR, bit [1]

Reset Request. Setting this bit to 1 requests a Warm reset.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## AA64, bit [0]

When the highest implemented Exception level can use AArch64, determines which Execution state the PE boots into after a Warm reset:

| AA64   | Meaning   |
|--------|-----------|
| 0b0    | AArch32.  |
| 0b1    | AArch64.  |

On coming out of the Warm reset, execution starts at the IMPLEMENTATION DEFINED reset vector address of the specified Execution state.

If the highest implemented Exception level cannot use AArch64 this bit is RAZ/WI.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Accessing RMR

When EL3 is implemented, Arm deprecates accessing this register from any PE mode other than Monitor mode.

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1100 | 0b0000 | 0b010  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL IN {EL1, EL3} && IsHighestEL(PSTATE.EL) then R[t] = RMR; else UNDEFINED;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1100 | 0b0000 | 0b010  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if IsHighestEL(EL1) then RMR = R[t]; else UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if CP15SDISABLE == HIGH then UNDEFINED; elsif CP15SDISABLE2 == HIGH then UNDEFINED; else RMR = R[t];
```