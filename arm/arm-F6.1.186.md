## F6.1.186 VQSHL, VQSHLU (immediate)

Vector Saturating Shift Left (immediate) takes each element in a vector of integers, left shifts them by an immediate value, and places the results in a second vector.

The operand elements must all be the same size, and can be any one of:

- 8-bit, 16-bit, 32-bit, or 64-bit signed integers.
- 8-bit, 16-bit, 32-bit, or 64-bit unsigned integers.

The result elements are the same size as the operand elements. If the operand elements are signed, the results can be either signed or unsigned. If the operand elements are unsigned, the result elements must also be unsigned.

If any of the results overflow, they are saturated. The cumulative saturation bit, FPSCR.QC, is set if saturation occurs. For details see Pseudocode details of saturation.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector, signed result variant

```
Applies when (op == 1 && Q == 0 && !(imm6[5:3] == 000 && L ==
```

```
VQSHL{<c>}{<q>}.<type><size>
```

```
0)) {<Dd>, }<Dm>, #<imm>
```

## Encoding for the 64-bit SIMD vector, unsigned result variant

```
Applies when (U == 1 && op == 0 && Q == 0 && !(imm6[5:3] == 000 && L == 0))
```

```
VQSHLU{<c>}{<q>}.<type><size> {<Dd>, }<Dm>, #<imm>
```

## Encoding for the 128-bit SIMD vector, signed result variant

```
Applies when (op == 1 && Q == 1 && !(imm6[5:3] == 000 && L == 0)) VQSHL{<c>}{<q>}.<type><size> {<Qd>, }<Qm>, #<imm>
```

## Encoding for the 128-bit SIMD vector, unsigned result variant

```
Applies when (U == 1 && op == 0 && Q == 1 && !(imm6[5:3] == 000 && L == 0))
```

```
VQSHLU{<c>}{<q>}.<type><size> {<Qd>, }<Qm>, #<imm>
```

## Decode for all variants of this encoding

```
if (L:imm6) == '0000xxx' then SEE "Related encodings"; if U == '0' && op == '0' then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vm<0> == '1') then UNDEFINED; constant integer esize = 8 << HighestSetBitNZ((L:imm6)<6:3>); constant integer elements = 64 DIV esize; constant integer shift_amount = UInt(L:imm6) esize; constant boolean src_unsigned = (U == '1' && op == '1'); constant boolean dest_unsigned = (U == '1'); constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector, signed result variant

```
Applies when (op == 1 && Q == 0 && !(imm6[5:3] == 000 && L == 0))
```

```
VQSHL{<c>}{<q>}.<type><size> {<Dd>, }<Dm>, #<imm>
```

## Encoding for the 64-bit SIMD vector, unsigned result variant

```
Applies when (U == 1 && op == 0 && Q == 0 && !(imm6[5:3] == 000 && L == 0))
```

```
VQSHLU{<c>}{<q>}.<type><size> {<Dd>, }<Dm>, #<imm>
```

## Encoding for the 128-bit SIMD vector, signed result variant

```
Applies when (op == 1 && Q == 1 && !(imm6[5:3] == 000 && L ==
```

```
VQSHL{<c>}{<q>}.<type><size>
```

```
0)) {<Qd>, }<Qm>, #<imm>
```

## Encoding for the 128-bit SIMD vector, unsigned result variant

```
Applies when (U == 1 && op == 0 && Q == 1 && !(imm6[5:3] == 000 && L == 0)) VQSHLU{<c>}{<q>}.<type><size> {<Qd>, }<Qm>, #<imm>
```

## Decode for all variants of this encoding

```
if (L:imm6) == '0000xxx' then SEE "Related encodings"; if U == '0' && op == '0' then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vm<0> == '1') then UNDEFINED; constant integer esize = 8 << HighestSetBitNZ((L:imm6)<6:3>); constant integer elements = 64 DIV esize; constant integer shift_amount = UInt(L:imm6) esize; constant boolean src_unsigned = (U == '1' && op == '1'); constant boolean dest_unsigned = (U == '1'); constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

Related encodings: See Advanced SIMD one register and modified immediate for the T32 instruction set, or Advanced SIMD one register and modified immediate for the A32 instruction set.

## Assembler Symbols

## &lt;c&gt;

For the 'A1 128-bit SIMD vector, signed result', 'A1 128-bit SIMD vector, unsigned result', 'A1 64-bit SIMD vector, signed result', and 'A1 64-bit SIMD vector, unsigned result' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 128-bit SIMD vector, signed result', 'T1 128-bit SIMD vector, unsigned result', 'T1 64-bit SIMD vector, signed result', and 'T1 64-bit SIMD vector, unsigned result' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

## &lt;type&gt;

Is the data type for the elements of the vectors, encoded in 'U':

|   U | <type>   |
|-----|----------|
|   0 | S        |
|   1 | U        |

&lt;q&gt;

## &lt;size&gt;

Is the data size for the elements of the vectors, encoded in 'L:imm6':

|   L | imm6   |   <size> |
|-----|--------|----------|
|   0 | 001xxx |        8 |
|   0 | 01xxxx |       16 |
|   0 | 1xxxxx |       32 |
|   1 | xxxxxx |       64 |

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;Dm&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## &lt;imm&gt;

Is an immediate value, in the range 0 to &lt;size&gt; -1, encoded in the 'imm6' field.

## &lt;Qd&gt;

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

## &lt;Qm&gt;

Is the 128-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## &lt;Dd&gt;

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); for r = 0 to regs-1 for e = 0 to elements-1 constant bits(esize) opelt = Elem[D[m+r],e,esize]; constant integer element = if src_unsigned then UInt(opelt) else SInt(opelt); bits(esize) result; boolean sat; (result, sat) = SatQ(element << shift_amount, esize, dest_unsigned); Elem[D[d+r],e,esize] = result; if sat then FPSCR.QC = '1';
```