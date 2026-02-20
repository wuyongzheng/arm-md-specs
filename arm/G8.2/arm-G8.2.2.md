## G8.2.2 ACTLR2, Auxiliary Control Register 2

The ACTLR2 characteristics are:

## Purpose

Provides additional space to the ACTLR register to hold IMPLEMENTATION DEFINED trap functionality for execution at EL1 and EL0.

## Configuration

In Armv8.0 and Armv8.1, it is IMPLEMENTATION DEFINED whether this register is implemented, or whether it causes UNDEFINED exceptions when accessed. The implementation of this register can be detected by examining ID\_MMFR4.AC2.

From Armv8.2 this register must be implemented.

AArch32 System register ACTLR2 bits [31:0] are architecturally mapped to AArch64 System register ACTLR\_EL1[63:32].

This register is banked between ACTLR2 and ACTLR2\_S and ACTLR2\_NS.

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ACTLR2 are UNDEFINED.

## Attributes

ACTLR2 is a 32-bit register.

This register has the following instances:

- ACTLR2, when EL3 is not implemented or FEAT\_AA64 is implemented.
- ACTLR2\_S, when FEAT\_AA32EL3 is implemented.
- ACTLR2\_NS, when FEAT\_AA32EL3 is implemented.

## Field descriptions

31

IMPLEMENTATION DEFINED

## IMPLEMENTATIONDEFINED, bits [31:0]

IMPLEMENTATION DEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing ACTLR2

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0001 | 0b0000 | 0b011  |

0

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T1 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TACR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TAC == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = ACTLR2_NS; else R[t] = ACTLR2; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = ACTLR2_NS; else R[t] = ACTLR2; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then R[t] = ACTLR2_S; else R[t] = ACTLR2_NS;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0001 | 0b0000 | 0b011  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T1 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TACR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TAC == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then ACTLR2_NS = R[t]; else ACTLR2 = R[t]; elsif PSTATE.EL == EL2 then
```

```
if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ACTLR2_NS = R[t]; else ACTLR2 = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then ACTLR2_S = R[t]; else ACTLR2_NS = R[t];
```

```
ELUsingAArch32(EL3) then
```