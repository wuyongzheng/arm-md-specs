## G8.2.44 DCIMVAC, Data Cache line Invalidate by VA to PoC

The DCIMVAC characteristics are:

## Purpose

Invalidate data or unified cache line by virtual address to PoC.

## Configuration

AArch32 System instruction DCIMVAC bits [31:0] performs the same function as bits [31:0].

This system instruction is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to DCIMVAC are UNDEFINED.

## Attributes

DCIMVAC is a 32-bit System instruction.

## Field descriptions

```
Virtual address to use 31 0
```

## VA, bits [31:0]

Virtual address to use. No alignment restrictions apply to this V A.

## Executing DCIMVAC

It is IMPLEMENTATION DEFINED whether, when this instruction is executed, it can generate a watchpoint. If this instruction can generate a watchpoint this is prioritized in the same way as other watchpoints.

Execution of this instruction might require an address translation from V A to PA, and that translation might fault. For more information, see 'AArch32 data cache maintenance instructions (DC*)'.

Accesses to this instruction use the following encodings in the System instruction encoding space:

```
MCR{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0111 | 0b0110 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if AArch32.TreatDCAsNOP(CacheOp_Invalidate, CacheOpScope_PoC) && ↪ → !AArch32.CanTrapDC(CacheOp_Invalidate, CacheOpScope_PoC) then ExecuteAsNOP(); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T7 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T7 == '1' ↪ → then
```

```
AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TPCP == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TPC == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else if AArch32.TreatDCAsNOP(CacheOp_Invalidate, CacheOpScope_PoC) then ExecuteAsNOP(); else AArch32.DC(R[t], CacheOp_Invalidate, CacheOpScope_PoC); elsif PSTATE.EL == EL2 then if AArch32.TreatDCAsNOP(CacheOp_Invalidate, CacheOpScope_PoC) && ↪ → !AArch32.CanTrapDC(CacheOp_Invalidate, CacheOpScope_PoC) then ExecuteAsNOP(); else if AArch32.TreatDCAsNOP(CacheOp_Invalidate, CacheOpScope_PoC) then ExecuteAsNOP(); else AArch32.DC(R[t], CacheOp_Invalidate, CacheOpScope_PoC); elsif PSTATE.EL == EL3 then if AArch32.TreatDCAsNOP(CacheOp_Invalidate, CacheOpScope_PoC) then ExecuteAsNOP(); else AArch32.DC(R[t], CacheOp_Invalidate, CacheOpScope_PoC);
```