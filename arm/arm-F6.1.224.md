## F6.1.224 VSHL (immediate)

Vector Shift Left (immediate) takes each element in a vector of integers, left shifts them by an immediate value, and places the results in the destination vector.

Bits shifted out of the left of each element are lost.

The elements must all be the same size, and can be 8-bit, 16-bit, 32-bit, or 64-bit integers. There is no distinction between signed and unsigned integers.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0 && !(imm6[5:3] == 000 && L == 0)) VSHL{<c>}{<q>}.I<size> {<Dd>, }<Dm>, #<imm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1 && !(imm6[5:3] == 000 && L == VSHL{<c>}{<q>}.I<size> {<Qd>, }<Qm>, #<imm>
```

## Decode for all variants of this encoding

```
UNDEFINED; HighestSetBitNZ((L:imm6)<6:3>);
```

```
if (L:imm6) == '0000xxx' then SEE "Related encodings"; if Q == '1' && (Vd<0> == '1' || Vm<0> == '1') then constant integer esize = 8 << constant integer elements = 64 DIV esize; constant integer shift_amount = UInt(L:imm6) esize; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0 && !(imm6[5:3] == 000 && L == 0)) VSHL{<c>}{<q>}.I<size> {<Dd>, }<Dm>, #<imm>
```

```
0))
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1 && !(imm6[5:3] == 000 && L ==
```

```
VSHL{<c>}{<q>}.I<size>
```

```
0)) {<Qd>, }<Qm>, #<imm>
```

## Decode for all variants of this encoding

```
if (L:imm6) == '0000xxx' then SEE "Related encodings"; if Q == '1' && (Vd<0> == '1' || Vm<0> == '1') then UNDEFINED; constant integer esize = 8 << HighestSetBitNZ((L:imm6)<6:3>); constant integer elements = 64 DIV esize; constant integer shift_amount = UInt(L:imm6) esize; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

Related encodings: See Advanced SIMD one register and modified immediate for the T32 instruction set, or Advanced SIMD one register and modified immediate for the A32 instruction set.

## Assembler Symbols

&lt;c&gt;

For the 'A1 128-bit SIMD vector' and 'A1 64-bit SIMD vector' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 128-bit SIMD vector' and 'T1 64-bit SIMD vector' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

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

&lt;q&gt;

## &lt;Dd&gt;

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); for r = 0 to regs-1 for e = 0 to elements-1 Elem[D[d+r],e,esize] =
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

```
LSL(Elem[D[m+r],e,esize], shift_amount);
```