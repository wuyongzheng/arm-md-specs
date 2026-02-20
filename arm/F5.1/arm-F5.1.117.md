## F5.1.117 MRRC

Move to two general-purpose registers from System register. This instruction copies the value of a System register to two general-purpose registers.

The System register descriptions identify valid encodings for this instruction. Other encodings are UNDEFINED. For more information see About the AArch32 System register interface and General behavior of System registers.

In an implementation that includes EL2, MRRC accesses to System registers can be trapped to Hyp mode, meaning that an attempt to execute an MRRC instruction in a Non-secure mode other than Hyp mode, that would be permitted in the absence of the Hyp trap controls, generates a Hyp Trap exception. For more information, see EL2 configurable instruction enables, disables, and traps.

Because of the range of possible traps to Hyp mode, the MRRC pseudocode does not show these possible traps.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
MRRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <Rt2>, <CRm>
```

## Decode for this encoding

```
constant integer t = UInt(Rt); constant integer t2 = UInt(Rt2); constant integer cp = if cp15 == '0' then 14 else // Armv8-A removes UNPREDICTABLE for R13 if t == 15 || t2 == 15 || t == t2 then
```

```
15; UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If t == t2 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The value in the destination register is UNKNOWN.

T1

<!-- image -->

## Encoding

```
MRRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <Rt2>, <CRm>
```

## Decode for this encoding

```
constant integer t = UInt(Rt); constant integer t2 = UInt(Rt2); constant integer cp = if cp15 == '0' then 14 else // Armv8-A removes UNPREDICTABLE for R13 if t == 15 || t2 == 15 || t == t2 then
```

```
15; UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If t == t2 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The value in the destination register is UNKNOWN.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

&lt;q&gt;

See Standard assembler syntax fields.

## &lt;coproc&gt;

Is the System register encoding space, encoded in 'cp15':

|   cp15 | <coproc>   |
|--------|------------|
|      0 | p14        |
|      1 | p15        |

## &lt;opc1&gt;

Is the opc1 parameter within the System register encoding space, in the range 0 to 15, encoded in the 'opc1' field.

## &lt;Rt&gt;

Is the first general-purpose register that is transferred into, encoded in the 'Rt' field.

## &lt;Rt2&gt;

Is the second general-purpose register that is transferred into, encoded in the 'Rt2' field.

## &lt;CRm&gt;

Is the CRm parameter within the System register encoding space, in the range c0 to c15, encoded in the 'CRm' field.

The possible values of { &lt;coproc&gt; , &lt;opc1&gt; , &lt;CRm&gt; } encode the entire System register encoding space. Not all of this space is allocated, and the System register descriptions identify the allocated encodings.

For the permitted uses of these instructions, as described in this manual, &lt;Rt2&gt; transfers bits[63:32] of the selected System register, while &lt;Rt&gt; transfers bits[31:0].

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); AArch32.SysRegRead64(cp, ThisInstr(), t, t2);
```