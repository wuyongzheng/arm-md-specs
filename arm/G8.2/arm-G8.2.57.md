## G8.2.57 HACR, Hyp Auxiliary Configuration Register

The HACR characteristics are:

## Purpose

Controls trapping to Hyp mode of IMPLEMENTATION DEFINED aspects of Non-secure EL1 or EL0 operation.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

AArch32 System register HACR bits [31:0] are architecturally mapped to AArch64 System register HACR\_EL2[31:0].

This register is present only when FEAT\_AA32EL2 is implemented. Otherwise, direct accesses to HACR are UNDEFINED.

## Attributes

HACRis a 32-bit register.

## Field descriptions

31

IMPLEMENTATION DEFINED

## IMPLEMENTATIONDEFINED, bits [31:0]

IMPLEMENTATION DEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing HACR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b0001 | 0b0001 | 0b111  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T1 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else
```

0

```
UNDEFINED; elsif PSTATE.EL == EL2 then R[t] = HACR; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else R[t] = HACR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b0001 | 0b0001 | 0b111  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T1 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then HACR = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else HACR = R[t];
```