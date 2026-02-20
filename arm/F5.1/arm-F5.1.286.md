## F5.1.286 UQSUB8

Unsigned Saturating Subtract 8 performs four unsigned 8-bit integer subtractions, saturates the results to the 8-bit unsigned integer range 0 &lt;= x &lt;= 2 8 - 1, and writes the results to the destination register.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
UQSUB8{<c>}{<q>} {<Rd>, }<Rn>, <Rm>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); if d == 15 || n == 15 || m == 15 then UNPREDICTABLE;
```

T1

<!-- image -->

## Encoding

```
UQSUB8{<c>}{<q>} {<Rd>, }<Rn>, <Rm>
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
if ConditionPassed() then EncodingSpecificOperations(); constant integer diff1 = UInt(R[n]<7:0>) UInt(R[m]<7:0>); constant integer diff2 = UInt(R[n]<15:8>) UInt(R[m]<15:8>); constant integer diff3 = UInt(R[n]<23:16>) UInt(R[m]<23:16>); constant integer diff4 = UInt(R[n]<31:24>) UInt(R[m]<31:24>); R[d]<7:0> = UnsignedSat(diff1, 8); R[d]<15:8> = UnsignedSat(diff2, 8); R[d]<23:16> = UnsignedSat(diff3, 8); R[d]<31:24> = UnsignedSat(diff4, 8);
```

Is the general-purpose destination register, encoded in the 'Rd' field.