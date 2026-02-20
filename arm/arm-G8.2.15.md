## G8.2.15 ATS1CPW, Address Translate Stage 1 Current state PL1 Write

The ATS1CPW characteristics are:

## Purpose

Performs stage 1 address translation as defined for PL1 and the current Security state, with permissions as if writing to the given virtual address.

## Configuration

This system instruction is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ATS1CPW are UNDEFINED.

## Attributes

ATS1CPW is a 32-bit System instruction.

## Field descriptions

```
Input address for translation 31 0
```

## IA, bits [31:0]

Input address for translation. The resulting address can be read from the PAR.

This System instruction takes a V A as input. If EL2 is implemented and enabled in the current Security state, the resulting address is the IPA that is the output address of the stage 1 translation. Otherwise, the resulting address is a PA.

## Executing ATS1CPW

Accesses to this instruction use the following encodings in the System instruction encoding space:

```
MCR{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0111 | 0b1000 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T7 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T7 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else AArch32.AT(R[t], TranslationStage_1, EL1, ATAccess_Write); elsif PSTATE.EL == EL2 then AArch32.AT(R[t], TranslationStage_1, EL1, ATAccess_Write); elsif PSTATE.EL == EL3 then
```

```
if SCR.NS == '0' then AArch32.AT(R[t], TranslationStage_1, EL3, ATAccess_Write); else AArch32.AT(R[t], TranslationStage_1, EL1, ATAccess_Write);
```