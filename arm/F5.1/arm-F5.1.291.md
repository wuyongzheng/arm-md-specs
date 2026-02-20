## F5.1.291 USAX

Unsigned Subtract and Add with Exchange exchanges the two halfwords of the second operand, performs one unsigned 16-bit integer subtraction and one unsigned 16-bit addition, and writes the results to the destination register. It sets PSTATE.GE according to the results.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
USAX{<c>}{<q>} {<Rd>, }<Rn>, <Rm>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); if d == 15 || n == 15 || m == 15 then UNPREDICTABLE;
```

T1

<!-- image -->

## Encoding

<!-- image -->

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); // Armv8-A removes UNPREDICTABLE for R13 if d == 15 || n == 15 || m == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt; See Standard assembler syntax fields. &lt;q&gt; See Standard assembler syntax fields.

## &lt;Rd&gt;

&lt;Rn&gt;

Is the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Rm&gt;

Is the second general-purpose source register, encoded in the 'Rm' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant integer sum = UInt(R[n]<15:0>) + UInt(R[m]<31:16>); constant integer diff = UInt(R[n]<31:16>) UInt(R[m]<15:0>); R[d]<15:0> = sum<15:0>; R[d]<31:16> = diff<15:0>; PSTATE.GE<1:0> = if sum >= \texttt{0x10000} then '11' else '00'; PSTATE.GE<3:2> = if diff >= 0 then '11' else '00';
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

Is the general-purpose destination register, encoded in the 'Rd' field.