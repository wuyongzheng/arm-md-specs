## G8.2.109 JMCR, Jazelle Main Configuration Register

The JMCR characteristics are:

## Purpose

AJazelle register, which provides control of the Jazelle extension.

## Configuration

This register is present only when FEAT\_AA32 is implemented. Otherwise, direct accesses to JMCR are UNDEFINED.

## Attributes

JMCR is a 32-bit register.

## Field descriptions

| 31     | 0   |
|--------|-----|
| RAZ/WI |     |

## Bits [31:0]

Reserved, RAZ/WI.

## Accessing JMCR

For accesses from EL0 it is IMPLEMENTATION DEFINED whether the register is RW or UNDEFINED.

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b111  | 0b0010 | 0b0000 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if boolean IMPLEMENTATION_DEFINED "JMCR UNDEFINED at EL0" then UNDEFINED; else R[t] = JMCR; elsif PSTATE.EL == EL1 then R[t] = JMCR; elsif PSTATE.EL == EL2 then R[t] = JMCR; elsif PSTATE.EL == EL3 then R[t] = JMCR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b111  | 0b0010 | 0b0000 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if boolean IMPLEMENTATION_DEFINED "JMCR UNDEFINED at EL0" then UNDEFINED; else return; elsif PSTATE.EL == EL1 then return; elsif PSTATE.EL == EL2 then return; elsif PSTATE.EL == EL3 then return;
```