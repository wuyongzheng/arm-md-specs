## F6.1.188 VQSHRN, VQSHRUN

Vector Saturating Shift Right, Narrow takes each element in a quadword vector of integers, right shifts them by an immediate value, and places the truncated results in a doubleword vector.

For rounded results, see VQRSHRN and VQRSHRUN.

The operand elements must all be the same size, and can be any one of:

- 16-bit, 32-bit, or 64-bit signed integers.
- 16-bit, 32-bit, or 64-bit unsigned integers.

The result elements are half the width of the operand elements. If the operand elements are signed, the results can be either signed or unsigned. If the operand elements are unsigned, the result elements must also be unsigned.

If any of the results overflow, they are saturated. The cumulative saturation bit, FPSCR.QC, is set if saturation occurs. For details see Pseudocode details of saturation.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the Signed result variant

```
Applies when (op == 1) VQSHRN{<c>}{<q>}.<type><size> <Dd>,
```

```
<Qm>, #<imm>
```

## Encoding for the Unsigned result variant

```
Applies when (U == 1 && op == 0) VQSHRUN{<c>}{<q>}.<type><size> <Dd>, <Qm>, #<imm>
```

## Decode for all variants of this encoding

```
if imm6 == '000xxx' then SEE "Related encodings"; if U == '0' && op == '0' then SEE "VSHRN"; if Vm<0> == '1' then UNDEFINED; constant integer esize = 8 << HighestSetBitNZ(imm6<5:3>); constant integer elements = 64 DIV esize; constant integer shift_amount = (2 * esize) UInt(imm6); constant boolean src_unsigned = (U == '1' && op == '1'); constant boolean dest_unsigned = (U == '1'); constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm);
```

T1

<!-- image -->

## Encoding for the Signed result variant

Applies when (op ==

```
1)
```

```
VQSHRN{<c>}{<q>}.<type><size> <Dd>,
```

```
<Qm>, #<imm>
```

## Encoding for the Unsigned result variant

```
Applies when (U == 1 && op ==
```

```
<Qm>, #<imm>
```

```
0) VQSHRUN{<c>}{<q>}.<type><size> <Dd>,
```

## Decode for all variants of this encoding

```
if imm6 == '000xxx' then SEE "Related encodings"; if U == '0' && op == '0' then SEE "VSHRN"; if Vm<0> == '1' then UNDEFINED; constant integer esize = 8 << HighestSetBitNZ(imm6<5:3>); constant integer elements = 64 DIV esize; constant integer shift_amount = (2 * esize) UInt(imm6); constant boolean src_unsigned = (U == '1' && op == '1'); constant boolean dest_unsigned = (U == '1'); constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm);
```

Related encodings: See Advanced SIMD one register and modified immediate for the T32 instruction set, or Advanced SIMD one register and modified immediate for the A32 instruction set.

## Assembler Symbols

<!-- image -->

For the 'A1 Signed result' and 'A1 Unsigned result' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 Signed result' and 'T1 Unsigned result' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

## &lt;type&gt;

For the 'A1 Signed result' and 'T1 Signed result' variants: is the data type for the elements of the vectors, encoded in 'U':

|   U | <type>   |
|-----|----------|
|   0 | S        |

<!-- image -->

## &lt;Dd&gt;

1

U

For the 'A1 Unsigned result' and 'T1 Unsigned result' variants: is S when 'U' is 1, and is encoded in 'U'.

## &lt;size&gt;

Is the data size for the elements of the vectors, encoded in 'imm6':

| imm6   |   <size> |
|--------|----------|
| 001xxx |       16 |
| 01xxxx |       32 |
| 1xxxxx |       64 |

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;Qm&gt;

Is the 128-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## &lt;imm&gt;

Is an immediate value, in the range 1 to &lt;size&gt; /2, encoded in the 'imm6' field as &lt;size&gt; /2 &lt;imm&gt; .

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); for e = 0 to elements-1 constant bits(2*esize) opelt = Elem[Qin[m>>1],e,2*esize]; constant integer element = if src_unsigned then UInt(opelt) else SInt(opelt); bits(esize) result; boolean sat; (result, sat) = SatQ(element >> shift_amount, esize, dest_unsigned); Elem[D[d],e,esize] = result; if sat then FPSCR.QC = '1';
```