## G8.2.53 FCSEIDR, FCSE Process ID register

The FCSEIDR characteristics are:

## Purpose

Identifies whether the Fast Context Switch Extension (FCSE) is implemented.

From Armv8.0, the FCSE is not implemented, so this register is RAZ/WI. Software can access this register to determine that the implementation does not include the FCSE.

## Configuration

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to FCSEIDR are UNDEFINED.

## Attributes

FCSEIDR is a 32-bit register.

## Field descriptions

## Bits [31:0]

Reserved, RAZ/WI.

## Accessing FCSEIDR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1101 | 0b0000 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T13 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T13 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else R[t] = FCSEIDR; elsif PSTATE.EL == EL2 then R[t] = FCSEIDR; elsif PSTATE.EL == EL3 then R[t] = FCSEIDR;
```

31

RAZ/WI

0

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1101 | 0b0000 | 0b000  |

if !IsFeatureImplemented(FEAT\_AA32EL1) then

UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() &amp;&amp; IsFeatureImplemented(FEAT\_AA64EL2) &amp;&amp; !ELUsingAArch32(EL2) &amp;&amp; HSTR\_EL2.T13 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() &amp;&amp; IsFeatureImplemented(FEAT\_AA32EL2) &amp;&amp; ELUsingAArch32(EL2) &amp;&amp; HSTR.T13 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else FCSEIDR = R[t]; elsif PSTATE.EL == EL2 then FCSEIDR = R[t]; elsif PSTATE.EL == EL3 then FCSEIDR = R[t];