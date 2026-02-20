## G8.2.123 REVIDR, Revision ID Register

The REVIDR characteristics are:

## Purpose

Provides implementation-specific minor revision information.

## Configuration

If REVIDR has the same value as MIDR, then its contents have no significance.

AArch32 System register REVIDR bits [31:0] are architecturally mapped to AArch64 System register REVIDR\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to REVIDR are UNDEFINED.

## Attributes

REVIDR is a 32-bit register.

## Field descriptions

| 31                     | 0                      |
|------------------------|------------------------|
| IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED |

## IMPLEMENTATIONDEFINED, bits [31:0]

IMPLEMENTATION DEFINED.

## Accessing REVIDR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0000 | 0b0000 | 0b110  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T0 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T0 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TID1 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TID1 == '1' ↪ → then
```

AArch32.TakeHypTrapException(0x03);

```
else R[t] = REVIDR; elsif PSTATE.EL == EL2 then R[t] = REVIDR; elsif PSTATE.EL == EL3 then R[t] = REVIDR;
```