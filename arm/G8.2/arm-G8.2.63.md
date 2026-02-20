## G8.2.63 HAMAIR1, Hyp Auxiliary Memory Attribute Indirection Register 1

The HAMAIR1 characteristics are:

## Purpose

Provides IMPLEMENTATION DEFINED memory attributes for the memory attribute encodings defined by HMAIR1. These IMPLEMENTATION DEFINED attributes can only provide additional qualifiers for the memory attribute encodings, and cannot change the memory attributes defined in HMAIR1.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

AArch32 System register HAMAIR1 bits [31:0] are architecturally mapped to AArch64 System register AMAIR\_EL2[63:32].

This register is present only when FEAT\_AA32EL2 is implemented. Otherwise, direct accesses to HAMAIR1 are UNDEFINED.

## Attributes

HAMAIR1 is a 32-bit register.

## Field descriptions

IMPLEMENTATION DEFINED

If an implementation does not provide any IMPLEMENTATION DEFINED memory attributes, this register is RES0.

## IMPLEMENTATIONDEFINED, bits [31:0]

IMPLEMENTATION DEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing HAMAIR1

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b1010 | 0b0011 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T10 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03);
```

31

0

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T10 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then R[t] = HAMAIR1; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else R[t] = HAMAIR1;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b1010 | 0b0011 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T10 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T10 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then HAMAIR1 = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else HAMAIR1 = R[t];
```