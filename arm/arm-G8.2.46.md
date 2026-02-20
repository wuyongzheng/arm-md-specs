## G8.2.46 DFAR, Data Fault Address Register

The DFAR characteristics are:

## Purpose

Holds the virtual address of the faulting address that caused a synchronous Data Abort exception.

## Configuration

AArch32 System register DFAR bits [31:0] are architecturally mapped to AArch64 System register FAR\_EL1[31:0].

When FEAT\_AA32EL2 is implemented and FEAT\_AA32EL3 is implemented, AArch32 System register DFAR bits [31:0] are architecturally mapped to AArch32 System register HDFAR[31:0].

This register is banked between DFAR and DFAR\_S and DFAR\_NS.

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to DFAR are UNDEFINED.

## Attributes

DFAR is a 32-bit register.

This register has the following instances:

- DFAR, when EL3 is not implemented or FEAT\_AA64 is implemented.
- DFAR\_S, when FEAT\_AA32EL3 is implemented.
- DFAR\_NS, when FEAT\_AA32EL3 is implemented.

## Field descriptions

VA of faulting address of synchronous Data Abort exception

## VA, bits [31:0]

VA of faulting address of synchronous Data Abort exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing DFAR

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0110 | 0b0000 | 0b000  |

31

0

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T6 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T6 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TRVM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TRVM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = DFAR_NS; else R[t] = DFAR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = DFAR_NS; else R[t] = DFAR; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then R[t] = DFAR_S; else R[t] = DFAR_NS;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0110 | 0b0000 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T6 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T6 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TVM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TVM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then DFAR_NS = R[t]; else DFAR = R[t]; elsif PSTATE.EL == EL2 then
```

```
if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && DFAR_NS = R[t]; else DFAR = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then DFAR_S = R[t]; else DFAR_NS = R[t];
```

```
ELUsingAArch32(EL3) then
```