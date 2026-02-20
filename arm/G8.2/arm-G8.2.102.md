## G8.2.102 IFAR, Instruction Fault Address Register

The IFAR characteristics are:

## Purpose

Holds the virtual address of the faulting address that caused a synchronous Prefetch Abort exception.

## Configuration

AArch32 System register IFAR bits [31:0] are architecturally mapped to AArch64 System register FAR\_EL1[63:32].

When EL2 is implemented and EL3 is implemented, AArch32 System register IFAR bits [31:0] are architecturally mapped to AArch32 System register HIFAR[31:0].

This register is banked between IFAR and IFAR\_S and IFAR\_NS.

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to IFAR are UNDEFINED.

## Attributes

IFAR is a 32-bit register.

This register has the following instances:

- IFAR, when EL3 is not implemented or FEAT\_AA64 is implemented.
- IFAR\_S, when FEAT\_AA32EL3 is implemented.
- IFAR\_NS, when FEAT\_AA32EL3 is implemented.

## Field descriptions

VA of faulting address of synchronous Prefetch Abort exception

## VA, bits [31:0]

VA of faulting address of synchronous Prefetch Abort exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing IFAR

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0110 | 0b0000 | 0b010  |

31

0

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T6 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T6 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TRVM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TRVM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = IFAR_NS; else R[t] = IFAR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = IFAR_NS; else R[t] = IFAR; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then R[t] = IFAR_S; else R[t] = IFAR_NS;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0110 | 0b0000 | 0b010  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T6 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T6 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TVM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TVM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then IFAR_NS = R[t]; else IFAR = R[t]; elsif PSTATE.EL == EL2 then
```

```
if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && IFAR_NS = R[t]; else IFAR = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then IFAR_S = R[t]; else IFAR_NS = R[t];
```

```
ELUsingAArch32(EL3) then
```