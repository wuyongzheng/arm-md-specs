## F5.1.267 UADD8

Unsigned Add 8 performs four unsigned 8-bit integer additions, and writes the results to the destination register. It sets PSTATE.GE according to the results of the additions.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
UADD8{<c>}{<q>} {<Rd>, }<Rn>, <Rm>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); if d == 15 || n == 15 || m == 15 then UNPREDICTABLE;
```

T1

<!-- image -->

## Encoding

```
UADD8{<c>}{<q>} {<Rd>, }<Rn>, <Rm>
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

- &lt;Rn&gt;

Is the first general-purpose source register, encoded in the 'Rn' field.

&lt;Rm&gt;

Is the second general-purpose source register, encoded in the 'Rm' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant integer sum1 = UInt(R[n]<7:0>) + UInt(R[m]<7:0>); constant integer sum2 = UInt(R[n]<15:8>) + UInt(R[m]<15:8>); constant integer sum3 = UInt(R[n]<23:16>) + UInt(R[m]<23:16>); constant integer sum4 = UInt(R[n]<31:24>) + UInt(R[m]<31:24>); R[d]<7:0> = sum1<7:0>; R[d]<15:8> = sum2<7:0>; R[d]<23:16> = sum3<7:0>; R[d]<31:24> = sum4<7:0>; PSTATE.GE<0> = if sum1 >= \texttt{0x100} then '1' else '0'; PSTATE.GE<1> = if sum2 >= \texttt{0x100} then '1' else '0'; PSTATE.GE<2> = if sum3 >= \texttt{0x100} then '1' else '0'; PSTATE.GE<3> = if sum4 >= \texttt{0x100} then '1' else '0';
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

Is the general-purpose destination register, encoded in the 'Rd' field.