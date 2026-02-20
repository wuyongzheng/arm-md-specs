## G8.2.14 ATS1CPRP, Address Translate Stage 1 Current state PL1 Read PAN

The ATS1CPRP characteristics are:

## Purpose

Performs a stage 1 address translation at PL1 and in the current Security state, where the value of PSTATE.PAN determines if a read from a location will generate a Permission fault for a privileged access.

## Configuration

This system instruction is present only when FEAT\_AA32EL1 is implemented and FEAT\_PAN2 is implemented. Otherwise, direct accesses to ATS1CPRP are UNDEFINED.

## Attributes

ATS1CPRP is a 32-bit System instruction.

## Field descriptions

```
Input address for translation 31 0
```

## IA, bits [31:0]

Input address for translation. The resulting address can be read from the PAR.

This System instruction takes a V A as input. If EL2 is implemented and enabled in the current Security state, the resulting address is the IPA that is the output address of the stage 1 translation. Otherwise, the resulting address is a PA.

## Executing ATS1CPRP

Accesses to this instruction use the following encodings in the System instruction encoding space:

```
MCR{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0111 | 0b1001 | 0b000  |

```
if !(IsFeatureImplemented(FEAT_AA32EL1) && IsFeatureImplemented(FEAT_PAN2)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T7 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T7 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else AArch32.AT(R[t], TranslationStage_1, EL1, ATAccess_ReadPAN); elsif PSTATE.EL == EL2 then AArch32.AT(R[t], TranslationStage_1, EL1, ATAccess_ReadPAN); elsif PSTATE.EL == EL3 then
```

```
if SCR.NS == '0' then AArch32.AT(R[t], TranslationStage_1, EL3, ATAccess_ReadPAN); else AArch32.AT(R[t], TranslationStage_1, EL1, ATAccess_ReadPAN);
```