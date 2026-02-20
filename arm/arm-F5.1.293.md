## F5.1.293 USUB8

Unsigned Subtract 8 performs four 8-bit unsigned integer subtractions, and writes the results to the destination register. It sets PSTATE.GE according to the results of the subtractions.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
USUB8{<c>}{<q>} {<Rd>, }<Rn>, <Rm>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); if d == 15 || n == 15 || m == 15 then UNPREDICTABLE;
```

T1

<!-- image -->

## Encoding

```
USUB8{<c>}{<q>} {<Rd>, }<Rn>, <Rm>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); // Armv8-A removes UNPREDICTABLE for R13 if d == 15 || n == 15 || m == 15 then
```

```
UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

H

## Assembler Symbols

&lt;c&gt; See Standard assembler syntax fields. &lt;q&gt; See Standard assembler syntax fields.

&lt;Rd&gt;

&lt;Rn&gt;

Is the first general-purpose source register, encoded in the 'Rn' field.

&lt;Rm&gt;

Is the second general-purpose source register, encoded in the 'Rm' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant integer diff1 = UInt(R[n]<7:0>) UInt(R[m]<7:0>); constant integer diff2 = UInt(R[n]<15:8>) UInt(R[m]<15:8>); constant integer diff3 = UInt(R[n]<23:16>) UInt(R[m]<23:16>); constant integer diff4 = UInt(R[n]<31:24>) UInt(R[m]<31:24>); R[d]<7:0> = diff1<7:0>; R[d]<15:8> = diff2<7:0>; R[d]<23:16> = diff3<7:0>; R[d]<31:24> = diff4<7:0>; PSTATE.GE<0> = if diff1 >= 0 then '1' else '0'; PSTATE.GE<1> = if diff2 >= 0 then '1' else '0'; PSTATE.GE<2> = if diff3 >= 0 then '1' else '0'; PSTATE.GE<3> = if diff4 >= 0 then '1' else '0';
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

Is the general-purpose destination register, encoded in the 'Rd' field.