## G8.2.80 ICIALLU, Instruction Cache Invalidate All to PoU

The ICIALLU characteristics are:

## Purpose

Invalidate all instruction caches of the PE executing the instruction to the Point of Unification. If branch predictors are architecturally visible, also flush branch predictors.

## Configuration

AArch32 System instruction ICIALLU bits [31:0] performs the same function as bits [31:0].

This system instruction is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ICIALLU are UNDEFINED.

## Attributes

ICIALLU is a 32-bit System instruction.

## Field descriptions

This instruction has no applicable fields.

The value in the register specified by &lt;Rt&gt; is ignored.

## Executing ICIALLU

The PE ignores the value of &lt;Rt&gt;. Software does not have to write a value to this register before issuing this instruction.

When HCR.FB is 1, at Non-secure EL1 this instruction executes as a ICIALLUIS.

Accesses to this instruction use the following encodings in the System instruction encoding space:

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0111 | 0b0101 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if AArch32.TreatICAsNOP(CacheOp_Invalidate, CacheOpScope_PoU) && ↪ → !AArch32.CanTrapIC(CacheOp_Invalidate, CacheOpScope_PoU) then ExecuteAsNOP(); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T7 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T7 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TPU == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TOCU == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TPU == '1' ↪ → then AArch32.TakeHypTrapException(0x03);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TOCU == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.FB == '1' then AArch32.IC(CacheOpScope_ALLUIS); else if AArch32.TreatICAsNOP(CacheOp_Invalidate, CacheOpScope_PoU) then ExecuteAsNOP(); else AArch32.IC(CacheOpScope_ALLU); elsif PSTATE.EL == EL2 then if AArch32.TreatICAsNOP(CacheOp_Invalidate, CacheOpScope_PoU) && ↪ → !AArch32.CanTrapIC(CacheOp_Invalidate, CacheOpScope_PoU) then ExecuteAsNOP(); else if AArch32.TreatICAsNOP(CacheOp_Invalidate, CacheOpScope_PoU) then ExecuteAsNOP(); else AArch32.IC(CacheOpScope_ALLU); elsif PSTATE.EL == EL3 then if AArch32.TreatICAsNOP(CacheOp_Invalidate, CacheOpScope_PoU) then ExecuteAsNOP(); else AArch32.IC(CacheOpScope_ALLU);
```