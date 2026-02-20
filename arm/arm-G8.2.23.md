## G8.2.23 BPIMVA, Branch Predictor Invalidate by VA

The BPIMVA characteristics are:

## Purpose

Invalidate virtual address from branch predictors.

## Configuration

In an implementation where the branch predictors are architecturally invisible, this instruction can execute as a NOP.

This system instruction is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to BPIMVA are UNDEFINED.

## Attributes

BPIMVA is a 32-bit System instruction.

## Field descriptions

```
Virtual address to use 31 0
```

## VA, bits [31:0]

Virtual address to use.

## Executing BPIMVA

Accesses to this instruction use the following encodings in the System instruction encoding space:

```
MCR{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0111 | 0b0101 | 0b111  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T7 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T7 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else BPIMVA(R[t]); elsif PSTATE.EL == EL2 then BPIMVA(R[t]); elsif PSTATE.EL == EL3 then BPIMVA(R[t]);
```