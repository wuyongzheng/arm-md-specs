## G8.2.162 TPIDRPRW, PL1 Software Thread ID Register

The TPIDRPRW characteristics are:

## Purpose

Provides a location where software executing at EL1 or higher can store thread identifying information that is not visible to software executing at EL0, for OS management purposes.

The PE makes no use of this register.

## Configuration

Note

The PE never updates this register.

AArch32 System register TPIDRPRW bits [31:0] are architecturally mapped to AArch64 System register TPIDR\_EL1[31:0].

This register is banked between TPIDRPRW and TPIDRPRW\_S and TPIDRPRW\_NS.

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to TPIDRPRW are UNDEFINED.

## Attributes

TPIDRPRW is a 32-bit register.

This register has the following instances:

- TPIDRPRW, when EL3 is not implemented or FEAT\_AA64 is implemented.
- TPIDRPRW\_S, when FEAT\_AA32EL3 is implemented.
- TPIDRPRW\_NS, when FEAT\_AA32EL3 is implemented.

## Field descriptions

Thread ID

31

0

## TID, bits [31:0]

Thread ID. Thread identifying information stored by software running at this Exception level.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing TPIDRPRW

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1101 | 0b0000 | 0b100  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T13 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T13 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = TPIDRPRW_NS; else R[t] = TPIDRPRW; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = TPIDRPRW_NS; else R[t] = TPIDRPRW; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then R[t] = TPIDRPRW_S; else R[t] = TPIDRPRW_NS;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1101 | 0b0000 | 0b100  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T13 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T13 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then TPIDRPRW_NS = R[t]; else TPIDRPRW = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then TPIDRPRW_NS = R[t]; else TPIDRPRW = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then TPIDRPRW_S = R[t]; else TPIDRPRW_NS = R[t];
```