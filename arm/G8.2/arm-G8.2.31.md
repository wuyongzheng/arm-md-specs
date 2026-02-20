## G8.2.31 CP15DSB, Data Synchronization Barrier System instruction

The CP15DSB characteristics are:

## Purpose

Performs a Data Synchronization Barrier.

Arm deprecates any use of this System instruction, and strongly recommends that software use the DSB instruction instead.

## Configuration

This system instruction is present only when FEAT\_AA32 is implemented. Otherwise, direct accesses to CP15DSB are UNDEFINED.

## Attributes

CP15DSB is a 32-bit System instruction.

## Field descriptions

This instruction has no applicable fields.

The value in the register specified by &lt;Rt&gt; is ignored.

## Executing CP15DSB

Accesses to this instruction use the following encodings in the System instruction encoding space:

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0111 | 0b1010 | 0b100  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → SCTLR_EL1.CP15BEN == '0' then UNDEFINED; elsif ELIsInHost(EL0) && SCTLR_EL2.CP15BEN == '0' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && SCTLR.CP15BEN == '0' then UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T7 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T7 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else CP15DSB(); elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T7 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T7 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif SCTLR.CP15BEN == '0' then UNDEFINED;
```

```
else CP15DSB(); elsif PSTATE.EL == EL2 then if HSCTLR.CP15BEN == '0' then UNDEFINED; else CP15DSB(); elsif PSTATE.EL == EL3 then if SCTLR.CP15BEN == '0' then UNDEFINED; else CP15DSB();
```