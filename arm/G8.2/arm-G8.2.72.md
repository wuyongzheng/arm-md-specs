## G8.2.72 HRMR, Hyp Reset Management Register

The HRMR characteristics are:

## Purpose

If EL2 is the highest implemented Exception level and this register is implemented:

- Awrite to the register at EL2 can request a Warm reset.
- If EL2 can use AArch32 and AArch64, this register specifies the Execution state that the PE boots into on a Warm reset.

## Configuration

Only implemented if EL2 is the highest implemented Exception level. In this case:

- If EL2 can use AArch32 and AArch64 then this register must be implemented.
- If EL2 cannot use AArch64 then it is IMPLEMENTATION DEFINED whether the register is implemented.

AArch32 System register HRMR bits [31:0] are architecturally mapped to AArch64 System register RMR\_EL2[31:0].

This register is present only when FEAT\_AA32 is implemented. Otherwise, direct accesses to HRMR are UNDEFINED.

## Attributes

HRMRis a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:2]

Reserved, RES0.

## RR, bit [1]

Reset Request. Setting this bit to 1 requests a Warm reset.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## AA64, bit [0]

When EL2 can use AArch64, determines which Execution state the PE boots into after a Warm reset:

| AA64   | Meaning   |
|--------|-----------|
| 0b0    | AArch32.  |
| 0b1    | AArch64.  |

On coming out of the Warm reset, execution starts at the IMPLEMENTATION DEFINED reset vector address of the specified Execution state.

If EL2 cannot use AArch64 this bit is RAZ/WI.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Accessing HRMR

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b1100 | 0b0000 | 0b010  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL1 && EL2Enabled() && IsHighestEL(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && ↪ → !ELUsingAArch32(EL2) && HSTR_EL2.T12 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif PSTATE.EL == EL1 && EL2Enabled() && IsHighestEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) && ↪ → ELUsingAArch32(EL2) && HSTR.T12 == '1' then AArch32.TakeHypTrapException(0x03); elsif PSTATE.EL == EL2 && IsHighestEL(EL2) then R[t] = HRMR; else UNDEFINED;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b1100 | 0b0000 | 0b010  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL1 && EL2Enabled() && IsHighestEL(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && ↪ → !ELUsingAArch32(EL2) && HSTR_EL2.T12 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif PSTATE.EL == EL1 && EL2Enabled() && IsHighestEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) && ↪ → ELUsingAArch32(EL2) && HSTR.T12 == '1' then AArch32.TakeHypTrapException(0x03); elsif PSTATE.EL == EL2 && IsHighestEL(EL2) then HRMR = R[t]; else UNDEFINED;
```