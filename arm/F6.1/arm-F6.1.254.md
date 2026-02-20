## F6.1.254 VTRN

Vector Transpose treats the elements of its operand vectors as elements of 2 x 2 matrices, and transposes the matrices.

The elements of the vectors can be 8-bit, 16-bit, or 32-bit. There is no distinction between data types.

Figure F6-9 VTRN doubleword operations

<!-- image -->

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

This instruction is used by the pseudo-instructions VUZP (alias) and VZIP (alias).

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VTRN{<c>}{<q>}.<dt> <Dd>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VTRN{<c>}{<q>}.<dt> <Qd>, <Qm>
```

## Decode for all variants of this encoding

```
if size == '11' then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vm<0> == '1') then constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

```
UNDEFINED;
```

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when

```
(Q == 0)
```

```
VTRN{<c>}{<q>}.<dt> <Dd>,
```

```
<Dm>
```

## Encoding for the 128-bit SIMD vector variant

Applies when

```
(Q == 1) VTRN{<c>}{<q>}.<dt> <Qd>,
```

```
<Qm>
```

## Decode for all variants of this encoding

```
if size == '11' then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vm<0> == '1') then constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

## Assembler Symbols

&lt;c&gt;

For the 'A1 128-bit SIMD vector' and 'A1 64-bit SIMD vector' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 128-bit SIMD vector' and 'T1 64-bit SIMD vector' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the data type for the elements of the vectors, encoded in 'size':

|   size | <dt>     |
|--------|----------|
|     00 | 8        |
|     01 | 16       |
|     10 | 32       |
|     11 | RESERVED |

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

<!-- image -->

&lt;dt&gt;

&lt;Dd&gt;

```
UNDEFINED;
```

## &lt;Dm&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field.

&lt;Qd&gt;

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

&lt;Qm&gt;

Is the 128-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); constant integer h = elements DIV 2; for r = 0 to regs-1 if d == m then D[d+r] = bits(64) UNKNOWN; else for e = 0 to h-1 Elem[D[d+r],2*e+1,esize] = Elem[Din[m+r],2*e,esize]; Elem[D[m+r],2*e,esize] = Elem[Din[d+r],2*e+1,esize];
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.