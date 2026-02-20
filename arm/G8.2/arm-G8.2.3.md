## G8.2.3 ADFSR, Auxiliary Data Fault Status Register

The ADFSR characteristics are:

## Purpose

Provides additional IMPLEMENTATION DEFINED fault status information for Data Abort exceptions taken to EL1 modes, and EL3 modes when EL3 is implemented and is using AArch32.

## Configuration

AArch32 System register ADFSR bits [31:0] are architecturally mapped to AArch64 System register AFSR0\_EL1[31:0].

This register is banked between ADFSR and ADFSR\_S and ADFSR\_NS.

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ADFSR are UNDEFINED.

## Attributes

ADFSR is a 32-bit register.

This register has the following instances:

- ADFSR, when EL3 is not implemented or FEAT\_AA64 is implemented.
- ADFSR\_S, when FEAT\_AA32EL3 is implemented.
- ADFSR\_NS, when FEAT\_AA32EL3 is implemented.

## Field descriptions

31

IMPLEMENTATION DEFINED

## IMPLEMENTATIONDEFINED, bits [31:0]

IMPLEMENTATION DEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing ADFSR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0001 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then
```

0

```
if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TRVM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TRVM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = ADFSR_NS; else R[t] = ADFSR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = ADFSR_NS; else R[t] = ADFSR; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then R[t] = ADFSR_S; else R[t] = ADFSR_NS;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0001 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TVM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TVM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then ADFSR_NS = R[t]; else ADFSR = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then ADFSR_NS = R[t]; else ADFSR = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then
```

<!-- formula-not-decoded -->