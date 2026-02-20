## G8.2.108 JIDR, Jazelle ID Register

The JIDR characteristics are:

## Purpose

AJazelle register, which identified the Jazelle architecture version.

## Configuration

This register is present only when FEAT\_AA32 is implemented. Otherwise, direct accesses to JIDR are UNDEFINED.

## Attributes

JIDR is a 32-bit register.

## Field descriptions

## Bits [31:0]

Reserved, RAZ.

## Accessing JIDR

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b111  | 0b0000 | 0b0000 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if boolean IMPLEMENTATION_DEFINED "JIDR UNDEFINED at EL0" then UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HCR_EL2.TID0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TID0 == '1' ↪ → then AArch32.TakeHypTrapException(0x05); else R[t] = JIDR; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TID0 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TID0 == '1' ↪ → then AArch32.TakeHypTrapException(0x05); else
```

31

RAZ

0

```
R[t] = JIDR; elsif PSTATE.EL == EL2 then R[t] = JIDR; elsif PSTATE.EL == EL3 then R[t] = JIDR;
```