## F5.1.266 UADD16

Unsigned Add 16 performs two 16-bit unsigned integer additions, and writes the results to the destination register. It sets PSTATE.GE according to the results of the additions.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
UADD16{<c>}{<q>} {<Rd>, }<Rn>, <Rm>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); if d == 15 || n == 15 || m == 15 then UNPREDICTABLE;
```

T1

<!-- image -->

## Encoding

```
UADD16{<c>}{<q>} {<Rd>, }<Rn>, <Rm>
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
if ConditionPassed() then EncodingSpecificOperations(); constant integer sum1 = UInt(R[n]<15:0>) + UInt(R[m]<15:0>); constant integer sum2 = UInt(R[n]<31:16>) + UInt(R[m]<31:16>); R[d]<15:0> = sum1<15:0>; R[d]<31:16> = sum2<15:0>; PSTATE.GE<1:0> = if sum1 >= \texttt{0x10000} then '11' else '00'; PSTATE.GE<3:2> = if sum2 >= \texttt{0x10000} then '11' else '00';
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

Is the general-purpose destination register, encoded in the 'Rd' field.