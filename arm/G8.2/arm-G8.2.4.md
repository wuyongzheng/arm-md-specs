## G8.2.4 AIDR, Auxiliary ID Register

The AIDR characteristics are:

## Purpose

Provides IMPLEMENTATION DEFINED identification information.

The value of this register must be used in conjunction with the value of MIDR.

## Configuration

AArch32 System register AIDR bits [31:0] are architecturally mapped to AArch64 System register AIDR\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to AIDR are UNDEFINED.

## Attributes

AIDR is a 32-bit register.

## Field descriptions

| 31                     | 0                      |
|------------------------|------------------------|
| IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED |

## IMPLEMENTATIONDEFINED, bits [31:0]

IMPLEMENTATION DEFINED.

## Accessing AIDR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b001  | 0b0000 | 0b0000 | 0b111  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T0 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T0 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TID1 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TID1 == '1' ↪ → then
```

AArch32.TakeHypTrapException(0x03);

```
else R[t] = AIDR; elsif PSTATE.EL == EL2 then R[t] = AIDR; elsif PSTATE.EL == EL3 then R[t] = AIDR;
```