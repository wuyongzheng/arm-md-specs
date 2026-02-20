## F6.1.191 VQSUB

Vector Saturating Subtract subtracts the elements of the second operand vector from the corresponding elements of the first operand vector, and places the results in the destination vector. Signed and unsigned operations are distinct.

The operand and result elements must all be the same type, and can be any one of:

- 8-bit, 16-bit, 32-bit, or 64-bit signed integers.
- 8-bit, 16-bit, 32-bit, or 64-bit unsigned integers.

If any of the results overflow, they are saturated. The cumulative saturation bit, FPSCR.QC, is set if saturation occurs. For details see Pseudocode details of saturation.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when

(Q == 0)

VQSUB{&lt;c&gt;}{&lt;q&gt;}.&lt;dt&gt;

{&lt;Dd&gt;, }&lt;Dn&gt;,

&lt;Dm&gt;

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VQSUB{<c>}{<q>}.<dt> {<Qd>, }<Qn>, <Qm>
```

## Decode for all variants of this encoding

```
if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then UNDEFINED; constant boolean unsigned = (U == '1'); constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when (Q == 0)

```
VQSUB{<c>}{<q>}.<dt> {<Dd>, }<Dn>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VQSUB{<c>}{<q>}.<dt> {<Qd>, }<Qn>, <Qm>
```

## Decode for all variants of this encoding

```
if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then UNDEFINED; constant boolean unsigned = (U == '1'); constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

## Assembler Symbols

&lt;c&gt;

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
|   1 |     10 | U32    |
|   1 |     11 | U64    |

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field.

&lt;q&gt;

&lt;dt&gt;

&lt;Dd&gt;

&lt;Dn&gt;

```
<Dm> Is the 64-bit name of the second SIMD&FP source register, encoded in the 'M:Vm' field. <Qd> Is the 128-bit name of the SIMD&FP destination register, encoded in the 'D:Vd' field as <Qd>*2. <Qn> Is the 128-bit name of the first SIMD&FP source register, encoded in the 'N:Vn' field as <Qn>*2. <Qm> Is the 128-bit name of the second SIMD&FP source register, encoded in the 'M:Vm' field as <Qm>*2.
```

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); for r = 0 to regs-1 for e = 0 to elements-1 constant bits(esize) op1elt = Elem[D[n+r],e,esize]; constant bits(esize) op2elt = Elem[D[m+r],e,esize]; constant integer element1 = if unsigned then UInt(op1elt) else SInt(op1elt); constant integer element2 = if unsigned then UInt(op2elt) else SInt(op2elt); constant integer diff = element1 - element2; bits(esize) res; boolean sat; (res, sat) = SatQ(diff, esize, unsigned); Elem[D[d+r],e,esize] = res; if sat then FPSCR.QC = '1';
```