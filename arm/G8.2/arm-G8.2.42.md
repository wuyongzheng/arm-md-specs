## G8.2.42 DCCMVAU, Data Cache line Clean by VA to PoU

The DCCMVAU characteristics are:

## Purpose

Clean data or unified cache line by virtual address to PoU.

## Configuration

AArch32 System instruction DCCMVAU bits [31:0] performs the same function as bits [31:0].

This system instruction is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to DCCMVAUareUNDEFINED.

## Attributes

DCCMVAUis a 32-bit System instruction.

## Field descriptions

```
Virtual address to use 31 0
```

## VA, bits [31:0]

Virtual address to use. No alignment restrictions apply to this V A.

## Executing DCCMVAU

Execution of this instruction might require an address translation from V A to PA, and that translation might fault. For more information, see 'AArch32 data cache maintenance instructions (DC*)'.

Accesses to this instruction use the following encodings in the System instruction encoding space:

```
MCR{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0111 | 0b1011 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T7 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T7 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TPU == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TOCU == ↪ → '1' then
```

```
AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TPU == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TOCU == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else AArch32.DC(R[t], CacheOp_Clean, CacheOpScope_PoU); elsif PSTATE.EL == EL2 then AArch32.DC(R[t], CacheOp_Clean, CacheOpScope_PoU); elsif PSTATE.EL == EL3 then AArch32.DC(R[t], CacheOp_Clean, CacheOpScope_PoU);
```