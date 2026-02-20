## G8.2.21 BPIALL, Branch Predictor Invalidate All

The BPIALL characteristics are:

## Purpose

Invalidate all entries from branch predictors.

## Configuration

In an implementation where the branch predictors are architecturally invisible, this instruction can execute as a NOP.

This system instruction is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to BPIALL are UNDEFINED.

## Attributes

BPIALL is a 32-bit System instruction.

## Field descriptions

This instruction has no applicable fields.

The value in the register specified by &lt;Rt&gt; is ignored.

## Executing BPIALL

The PE ignores the value of &lt;Rt&gt;. Software does not have to write a value to this register before issuing this instruction.

When HCR.FB is 1, at Non-secure EL1 this instruction executes as a BPIALLIS.

Accesses to this instruction use the following encodings in the System instruction encoding space:

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0111 | 0b0101 | 0b110  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T7 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T7 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.FB == '1' then BPIALLIS(); else BPIALL(); elsif PSTATE.EL == EL2 then BPIALL(); elsif PSTATE.EL == EL3 then BPIALL();
```