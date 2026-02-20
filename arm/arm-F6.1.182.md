## F6.1.182 VQRSHL

Vector Saturating Rounding Shift Left takes each element in a vector, shifts them by a value from the least significant byte of the corresponding element of a second vector, and places the results in the destination vector. If the shift value is positive, the operation is a left shift. Otherwise, it is a right shift.

For truncated results see VQSHL (register).

The first operand and result elements are the same data type, and can be any one of:

- 8-bit, 16-bit, 32-bit, or 64-bit signed integers.
- 8-bit, 16-bit, 32-bit, or 64-bit unsigned integers.

The second operand is a signed integer of the same size.

If any of the results overflow, they are saturated. The cumulative saturation bit, FPSCR.QC, is set if saturation occurs. For details see Pseudocode details of saturation.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VQRSHL{<c>}{<q>}.<dt> {<Dd>, }<Dm>, <Dn>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VQRSHL{<c>}{<q>}.<dt> {<Qd>, }<Qm>, <Qn>
```

## Decode for all variants of this encoding

```
if Q == '1' && (Vd<0> == '1' || Vm<0> == '1' || Vn<0> == '1') then UNDEFINED; constant boolean unsigned = (U == '1'); constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm); constant integer n = UInt(N:Vn); constant integer regs = if Q == '0' then 1 else 2;
```

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VQRSHL{<c>}{<q>}.<dt> {<Dd>, }<Dm>, <Dn>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VQRSHL{<c>}{<q>}.<dt> {<Qd>, }<Qm>,
```

```
<Qn>
```

## Decode for all variants of this encoding

```
if Q == '1' && (Vd<0> == '1' || Vm<0> == '1' || Vn<0> == '1') then UNDEFINED; constant boolean unsigned = (U == '1'); constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm); constant integer n = UInt(N:Vn); constant integer regs = if Q == '0' then 1 else 2;
```

## Assembler Symbols

<!-- image -->

For the 'A1 128-bit SIMD vector' and 'A1 64-bit SIMD vector' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 128-bit SIMD vector' and 'T1 64-bit SIMD vector' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the data type for the elements of the vectors, encoded in 'U:size':

|   U |   size | <dt>   |
|-----|--------|--------|
|   0 |     00 | S8     |
|   0 |     01 | S16    |
|   0 |     10 | S32    |
|   0 |     11 | S64    |
|   1 |     00 | U8     |
|   1 |     01 | U16    |

<!-- image -->

<!-- image -->

## &lt;Dd&gt;

|   U |   size | <dt>   |
|-----|--------|--------|
|   1 |     10 | U32    |
|   1 |     11 | U64    |

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## &lt;Dn&gt;

&lt;Qd&gt;

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

## &lt;Qm&gt;

Is the 128-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

- &lt;Qn&gt;

Is the 128-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field as &lt;Qn&gt;*2.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); bits(esize) result; boolean sat; for r = 0 to regs-1 for e = 0 to elements-1 constant bits(esize) opelt = Elem[D[m+r], e, esize]; integer element = if unsigned then UInt(opelt) else SInt(opelt); integer shift = SInt(Elem[D[n+r], e, esize]<7:0>); if shift >= 0 then // left shift element = element << shift; else // rounding right shift shift = -shift; element = (element + (1 << (shift - 1))) >> shift; (result, sat) = SatQ(element, esize, unsigned); Elem[D[d+r], e, esize] = result; if sat then FPSCR.QC = '1';
```

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field.