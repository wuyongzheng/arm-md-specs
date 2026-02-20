## G8.2.39 DCCIMVAC, Data Cache line Clean and Invalidate by VA to PoC

The DCCIMVAC characteristics are:

## Purpose

Clean and Invalidate data or unified cache line by virtual address to PoC.

## Configuration

AArch32 System instruction DCCIMVAC bits [31:0] performs the same function as bits [31:0].

This system instruction is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to DCCIMVAC are UNDEFINED.

## Attributes

DCCIMVAC is a 32-bit System instruction.

## Field descriptions

<!-- image -->

## VA, bits [31:0]

Virtual address to use. No alignment restrictions apply to this V A.

## Executing DCCIMVAC

Execution of this instruction might require an address translation from V A to PA, and that translation might fault.

For more information about faults, see 'Permission fault'.

For more information about data cache maintenance instructions, see 'AArch32 data cache maintenance instructions (DC*)'.

Accesses to this instruction use the following encodings in the System instruction encoding space:

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0111 | 0b1110 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if AArch32.TreatDCAsNOP(CacheOp_CleanInvalidate, CacheOpScope_PoC) && ↪ → !AArch32.CanTrapDC(CacheOp_CleanInvalidate, CacheOpScope_PoC) then ExecuteAsNOP(); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T7 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T7 == '1' ↪ → then
```

```
AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TPCP == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TPC == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else if AArch32.TreatDCAsNOP(CacheOp_CleanInvalidate, CacheOpScope_PoC) then ExecuteAsNOP(); else AArch32.DC(R[t], CacheOp_CleanInvalidate, CacheOpScope_PoC); elsif PSTATE.EL == EL2 then if AArch32.TreatDCAsNOP(CacheOp_CleanInvalidate, CacheOpScope_PoC) && ↪ → !AArch32.CanTrapDC(CacheOp_CleanInvalidate, CacheOpScope_PoC) then ExecuteAsNOP(); else if AArch32.TreatDCAsNOP(CacheOp_CleanInvalidate, CacheOpScope_PoC) then ExecuteAsNOP(); else AArch32.DC(R[t], CacheOp_CleanInvalidate, CacheOpScope_PoC); elsif PSTATE.EL == EL3 then if AArch32.TreatDCAsNOP(CacheOp_CleanInvalidate, CacheOpScope_PoC) then ExecuteAsNOP(); else AArch32.DC(R[t], CacheOp_CleanInvalidate, CacheOpScope_PoC);
```