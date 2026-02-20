## F5.1.108 MCR

Move to System register from general-purpose register or execute a System instruction. This instruction copies the value of a general-purpose register to a System register, or executes a System instruction.

The System register and System instruction descriptions identify valid encodings for this instruction. Other encodings are UNDEFINED. For more information see About the AArch32 System register interface and General behavior of System registers.

In an implementation that includes EL2, MCR accesses to System registers can be trapped to Hyp mode, meaning that an attempt to execute an MCR instruction in a Non-secure mode other than Hyp mode, that would be permitted in the absence of the Hyp trap controls, generates a Hyp Trap exception. For more information, see EL2 configurable instruction enables, disables, and traps.

Because of the range of possible traps to Hyp mode, the MCR pseudocode does not show these possible traps.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
MCR{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

## Decode for this encoding

```
constant integer t = UInt(Rt); constant integer cp = if cp15 == '0' then 14 else // Armv8-A removes UNPREDICTABLE for R13 if t == 15 then UNPREDICTABLE;
```

T1

<!-- image -->

## Encoding

```
MCR{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

## Decode for this encoding

```
constant integer t = UInt(Rt); constant integer cp = if cp15 == '0' then 14 else // Armv8-A removes UNPREDICTABLE for R13 if t == 15 then UNPREDICTABLE;
```

```
15;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

```
15;
```

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

<!-- image -->

See Standard assembler syntax fields.

## &lt;coproc&gt;

Is the System register encoding space, encoded in 'cp15':

|   cp15 | <coproc>   |
|--------|------------|
|      0 | p14        |
|      1 | p15        |

## &lt;opc1&gt;

Is the opc1 parameter within the System register encoding space, in the range 0 to 7, encoded in the 'opc1' field.

## &lt;Rt&gt;

Is the general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;CRn&gt;

Is the CRn parameter within the System register encoding space, in the range c0 to c15, encoded in the 'CRn' field.

## &lt;CRm&gt;

Is the CRm parameter within the System register encoding space, in the range c0 to c15, encoded in the 'CRm' field.

## &lt;opc2&gt;

Is the opc2 parameter within the System register encoding space, in the range 0 to 7, encoded in the 'opc2' field.

The possible values of { &lt;coproc&gt; , &lt;opc1&gt; , &lt;CRn&gt; , &lt;CRm&gt; , &lt;opc2&gt; } encode the entire System register and System instruction encoding space. Not all of this space is allocated, and the System register and System instruction descriptions identify the allocated encodings.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); AArch32.SysRegWrite(cp, ThisInstr(), t);
```