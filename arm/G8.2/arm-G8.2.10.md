## G8.2.10 ATS12NSOPW, Address Translate Stages 1 and 2 Non-secure Only PL1 Write

The ATS12NSOPW characteristics are:

## Purpose

Performs stage 1 and 2 address translations as defined for PL1 and the Non-secure state, with permissions as if writing to the given virtual address.

## Configuration

This system instruction is present only when FEAT\_AA32EL2 is implemented. Otherwise, direct accesses to ATS12NSOPW are UNDEFINED.

## Attributes

ATS12NSOPW is a 32-bit System instruction.

## Field descriptions

```
Input address for translation 31 0
```

## IA, bits [31:0]

Input address for translation. The resulting address can be read from the PAR.

This System instruction takes a V A as input. The resulting address is the PA that is the output address of the stage 2 translation.

## Executing ATS12NSOPW

Accesses to this instruction use the following encodings in the System instruction encoding space:

```
MCR{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0111 | 0b1000 | 0b101  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T7 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T7 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsCurrentSecurityState(SS_Secure) then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsCurrentSecurityState(SS_Secure) then AArch64.AArch32SystemAccessTrap(EL3, 0x03);
```

else

```
UNDEFINED; elsif PSTATE.EL == EL2 then AArch32.AT(R[t], TranslationStage_12, EL1, ATAccess_Write); elsif PSTATE.EL == EL3 then AArch32.AT(R[t], TranslationStage_12, EL1, ATAccess_Write);
```