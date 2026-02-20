## G8.2.20 ATS1HW, Address Translate Stage 1 Hyp mode Write

The ATS1HW characteristics are:

## Purpose

Performs stage 1 address translation as defined for PL2 and the Non-secure state, with permissions as if writing to the given virtual address.

## Configuration

This system instruction is present only when FEAT\_AA32EL2 is implemented. Otherwise, direct accesses to ATS1HW are UNDEFINED.

## Attributes

ATS1HW is a 32-bit System instruction.

## Field descriptions

```
Input address for translation 31 0
```

## IA, bits [31:0]

Input address for translation. The resulting address can be read from the PAR.

This System instruction takes a V A as input. The resulting address is the PA that is the output address of the translation.

## Executing ATS1HW

If this instruction is executed in a Secure privileged mode other than Monitor mode, then the behavior is CONSTRAINED UNPREDICTABLE, and one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction is treated as a NOP.
- The instruction executes as if it had been executed in Monitor mode.

Accesses to this instruction use the following encodings in the System instruction encoding space:

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b0111 | 0b1000 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T7 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T7 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then AArch32.AT(R[t], TranslationStage_1, EL2, ATAccess_Write); elsif PSTATE.EL == EL3 then AArch32.AT(R[t], TranslationStage_1, EL2, ATAccess_Write);
```