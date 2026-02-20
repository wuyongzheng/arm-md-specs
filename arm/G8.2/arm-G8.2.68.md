## G8.2.68 HIFAR, Hyp Instruction Fault Address Register

The HIFAR characteristics are:

## Purpose

Holds the virtual address of the faulting address that caused a synchronous Prefetch Abort exception that is taken to Hyp mode.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

AArch32 System register HIFAR bits [31:0] are architecturally mapped to AArch64 System register FAR\_EL2[63:32].

When EL2 is implemented and EL3 is implemented, AArch32 System register HIFAR bits [31:0] are architecturally mapped to AArch32 System register IFAR[31:0].

This register is present only when FEAT\_AA32EL2 is implemented. Otherwise, direct accesses to HIFAR are UNDEFINED.

## Attributes

HIFAR is a 32-bit register.

## Field descriptions

```
VA of faulting address of synchronous Prefetch Abort exception taken to Hyp mode 31 0
```

## VA, bits [31:0]

VA of faulting address of synchronous Prefetch Abort exception taken to Hyp mode.

On a Data Abort exception, this register is UNKNOWN.

Any execution in a Non-secure EL1 or Non-secure EL0 mode makes this register UNKNOWN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing HIFAR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b0110 | 0b0000 | 0b010  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then
```

```
if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T6 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T6 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then R[t] = HIFAR; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else R[t] = HIFAR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b0110 | 0b0000 | 0b010  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T6 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T6 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then HIFAR = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else HIFAR = R[t];
```