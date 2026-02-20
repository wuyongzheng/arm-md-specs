## G8.2.110 JOSCR, Jazelle OS Control Register

The JOSCR characteristics are:

## Purpose

AJazelle register, which provides operating system control of the Jazelle Extension.

## Configuration

This register is present only when FEAT\_AA32 is implemented. Otherwise, direct accesses to JOSCR are UNDEFINED.

## Attributes

JOSCR is a 32-bit register.

## Field descriptions

| 31     | 0   |
|--------|-----|
| RAZ/WI |     |

## Bits [31:0]

Reserved, RAZ/WI.

## Accessing JOSCR

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b111  | 0b0001 | 0b0000 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if boolean IMPLEMENTATION_DEFINED "JOSCR UNDEFINED UNDEFINED; else R[t] = JOSCR; elsif PSTATE.EL == EL1 then R[t] = JOSCR; elsif PSTATE.EL == EL2 then R[t] = JOSCR; elsif PSTATE.EL == EL3 then R[t] = JOSCR;
```

```
at EL0" then
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b111  | 0b0001 | 0b0000 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if boolean IMPLEMENTATION_DEFINED "JOSCR UNDEFINED UNDEFINED; else return; elsif PSTATE.EL == EL1 then return; elsif PSTATE.EL == EL2 then return; elsif PSTATE.EL == EL3 then return;
```

at EL0" then