## F6.1.262 VUZP

Vector Unzip de-interleaves the elements of two vectors.

The elements of the vectors can be 8-bit, 16-bit, or 32-bit. There is no distinction between data types.

VUZP.8, doubleword

|    | Register state before operation   | Register state before operation   | Register state before operation   | Register state before operation   | Register state before operation   | Register state before operation   | Register state before operation   | Register state before operation   | Register state after operation   | Register state after operation   | Register state after operation   | Register state after operation   | Register state after operation   | Register state after operation   | Register state after operation   | Register state after operation   |
|----|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|
| Dd | A7                                | A6                                | A5                                | A4                                | A3                                | A2                                | A1                                | A0                                | B6                               | B4                               | B2                               | B0                               | A6                               | A4                               | A2                               | A0                               |
| Dm | B7                                | B6                                | B5                                | B4                                | B3                                | B2                                | B1                                | B0                                | B7                               | B5                               | B3                               | B1                               | A7                               | A5                               | A3                               | A1                               |

Figure F6-10 VUZP doubleword operation for data type 8

## VUZP.32, quadword

Figure F6-11 VUZP quadword operation for data type 32

|    | Register state before operation   | Register state before operation   | Register state before operation   | Register state before operation   | Register state after operation   | Register state after operation   | Register state after operation   | Register state after operation   |
|----|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|
| Qd | A3                                | A2                                | A1                                | A0                                | B2                               | B0                               | A2                               | A0                               |
| Qm | B3                                | B2                                | B1                                | B0                                | B3                               | B1                               | A3                               | A1                               |

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when

```
(Q == 0) VUZP{<c>}{<q>}.<dt> <Dd>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VUZP{<c>}{<q>}.<dt> <Qd>,
```

```
<Qm>
```

## Decode for all variants of this encoding

```
if size == '11' || (Q == '0' && size == '10') then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vm<0> == '1') then UNDEFINED; constant boolean quadword_operation = (Q == '1'); constant integer esize = 8 << UInt(size); constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm);
```

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VUZP{<c>}{<q>}.<dt> <Dd>,
```

```
<Dm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VUZP{<c>}{<q>}.<dt> <Qd>, <Qm>
```

## Decode for all variants of this encoding

```
if size == '11' || (Q == '0' && size == '10') then if Q == '1' && (Vd<0> == '1' || Vm<0> == '1') then constant boolean quadword_operation = (Q == '1'); constant integer esize = 8 << UInt(size); constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm);
```

## Assembler Symbols

&lt;c&gt;

For the 'A1 128-bit SIMD vector' and 'A1 64-bit SIMD vector' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 128-bit SIMD vector' and 'T1 64-bit SIMD vector' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

For the 'A1 64-bit SIMD vector' and 'T1 64-bit SIMD vector' variants: is the data type for the elements of the vectors, encoded in 'size':

| size   | <dt>     |
|--------|----------|
| 00     | 8        |
| 01     | 16       |
| 1x     | RESERVED |

For the 'A1 128-bit SIMD vector' and 'T1 128-bit SIMD vector' variants: is the data type for the elements of the vectors, encoded in 'size':

&lt;q&gt;

&lt;dt&gt;

```
UNDEFINED; UNDEFINED;
```

## &lt;Dd&gt;

|   size | <dt>     |
|--------|----------|
|     00 | 8        |
|     01 | 16       |
|     10 | 32       |
|     11 | RESERVED |

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;Dm&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field.

&lt;Qd&gt;

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

## &lt;Qm&gt;

Is the 128-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); if quadword_operation then if d == m then Q[d>>1] = bits(128) UNKNOWN; else constant bits(256) zipped_q = Q[m>>1]:Q[d>>1]; for e = 0 to (128 DIV esize) 1 Elem[Q[d>>1],e,esize] = Elem[zipped_q,2*e,esize]; Elem[Q[m>>1],e,esize] = Elem[zipped_q,2*e+1,esize]; else if d == m then D[d] = bits(64) UNKNOWN; else constant bits(128) zipped_d = D[m]:D[d]; for e = 0 to (64 DIV esize) - 1 Elem[D[d],e,esize] = Elem[zipped_d,2*e,esize]; Elem[D[m],e,esize] = Elem[zipped_d,2*e+1,esize];
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.