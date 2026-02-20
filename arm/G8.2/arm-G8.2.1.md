## G8.2.1 ACTLR, Auxiliary Control Register

The ACTLR characteristics are:

## Purpose

Provides IMPLEMENTATION DEFINED configuration and control options for execution at EL1 and EL0.

## Configuration

Some bits might define global configuration settings, and be common to the Secure and Non-secure instances of the register.

AArch32 System register ACTLR bits [31:0] are architecturally mapped to AArch64 System register ACTLR\_EL1[31:0].

This register is banked between ACTLR and ACTLR\_S and ACTLR\_NS.

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ACTLR are UNDEFINED.

## Attributes

ACTLR is a 32-bit register.

This register has the following instances:

- ACTLR, when EL3 is not implemented or FEAT\_AA64 is implemented.
- ACTLR\_S, when FEAT\_AA32EL3 is implemented.
- ACTLR\_NS, when FEAT\_AA32EL3 is implemented.

## Field descriptions

| 31                     | 0                      |
|------------------------|------------------------|
| IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED |

## IMPLEMENTATIONDEFINED, bits [31:0]

IMPLEMENTATION DEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing ACTLR

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0001 | 0b0000 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T1 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TACR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TAC == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = ACTLR_NS; else R[t] = ACTLR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = ACTLR_NS; else R[t] = ACTLR; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then R[t] = ACTLR_S; else R[t] = ACTLR_NS;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0001 | 0b0000 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T1 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TACR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TAC == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then ACTLR_NS = R[t]; else ACTLR = R[t]; elsif PSTATE.EL == EL2 then
```

```
if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then ACTLR_NS = R[t]; else ACTLR = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then ACTLR_S = R[t]; else ACTLR_NS = R[t];
```