## F6.1.177 VQMOVN, VQMOVUN

Vector Saturating Move and Narrow copies each element of the operand vector to the corresponding element of the destination vector.

The operand is a quadword vector. The elements can be any one of:

- 16-bit, 32-bit, or 64-bit signed integers.
- 16-bit, 32-bit, or 64-bit unsigned integers.

The result is a doubleword vector. The elements are half the length of the operand vector elements. If the operand is unsigned, the results are unsigned. If the operand is signed, the results can be signed or unsigned.

If any of the results overflow, they are saturated. The cumulative saturation bit, FPSCR.QC, is set if saturation occurs. For details see Pseudocode details of saturation.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

This instruction is used by the pseudo-instructions VQRSHRN (zero), VQRSHRUN (zero), VQSHRN (zero), and VQSHRUN(zero).

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

## A1

<!-- image -->

## Encoding for the Signed result variant

```
Applies when (op == 1x) VQMOVN{<c>}{<q>}.<dt>
```

```
<Dd>, <Qm>
```

## Encoding for the Unsigned result variant

```
Applies when (op == 01) VQMOVUN{<c>}{<q>}.<dt> <Dd>, <Qm>
```

## Decode for all variants of this encoding

```
'1');
```

```
if op == '00' then SEE "VMOVN"; if size == '11' || Vm<0> == '1' then UNDEFINED; constant boolean src_unsigned = (op == '11'); constant boolean dest_unsigned = (op<0> == constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm);
```

T1

<!-- image -->

## Encoding for the Signed result variant

```
Applies when (op == 1x) VQMOVN{<c>}{<q>}.<dt>
```

```
<Dd>, <Qm>
```

## Encoding for the Unsigned result variant

```
Applies when (op == 01) VQMOVUN{<c>}{<q>}.<dt>
```

```
<Dd>, <Qm>
```

## Decode for all variants of this encoding

```
'1');
```

```
if op == '00' then SEE "VMOVN"; if size == '11' || Vm<0> == '1' then UNDEFINED; constant boolean src_unsigned = (op == '11'); constant boolean dest_unsigned = (op<0> == constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm);
```

## Assembler Symbols

&lt;c&gt;

For the 'A1 Signed result' and 'A1 Unsigned result' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 Signed result' and 'T1 Unsigned result' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

For the 'A1 Signed result' and 'T1 Signed result' variants: is the data type for the elements of the operand, encoded in 'op:size':

| op   |   size | <dt>     |
|------|--------|----------|
| 10   |     00 | S16      |
| 10   |     01 | S32      |
| 10   |     10 | S64      |
| 1x   |     11 | RESERVED |
| 11   |     00 | U16      |

<!-- image -->

<!-- image -->

## &lt;Dd&gt;

|   op |   size | <dt>   |
|------|--------|--------|
|   11 |     01 | U32    |
|   11 |     10 | U64    |

For the 'A1 Unsigned result' and 'T1 Unsigned result' variants: is the data type for the elements of the operand, encoded in 'size':

|   size | <dt>     |
|--------|----------|
|     00 | S16      |
|     01 | S32      |
|     10 | S64      |
|     11 | RESERVED |

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

&lt;Qm&gt;

Is the 128-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); for e = 0 to elements-1 constant bits(2*esize) opelt = Elem[Qin[m>>1],e,2*esize]; constant integer element = if src_unsigned then UInt(opelt) else SInt(opelt); bits(esize) res; boolean sat; (res, sat) = SatQ(element, esize, dest_unsigned); Elem[D[d],e,esize] = res; if sat then FPSCR.QC = '1';
```