## F6.1.264 VZIP

Vector Zip interleaves the elements of two vectors.

The elements of the vectors can be 8-bit, 16-bit, or 32-bit. There is no distinction between data types.

VZIP.8, doubleword

|    | Register state before operation   | Register state before operation   | Register state before operation   | Register state before operation   | Register state before operation   | Register state before operation   | Register state before operation   | Register state before operation   | Register state after operation   | Register state after operation   | Register state after operation   | Register state after operation   | Register state after operation   | Register state after operation   | Register state after operation   | Register state after operation   |
|----|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|
| Dd | A7                                | A6                                | A5                                | A4                                | A3                                | A2                                | A1                                | A0                                | B3                               | A3                               | B2                               | A2                               | B1                               | A1                               | B0                               | A0                               |
| Dm | B7                                | B6                                | B5                                | B4                                | B3                                | B2                                | B1                                | B0                                | B7                               | A7                               | B6                               | A6                               | B5                               | A5                               | B4                               | A4                               |

Figure F6-12 VZIP doubleword operation for data type 8

## VZIP.32, quadword

Figure F6-13 VZIP quadword operation for data type 32

|    | Register state before operation   | Register state before operation   | Register state before operation   | Register state before operation   | Register state after operation   | Register state after operation   | Register state after operation   | Register state after operation   |
|----|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|
| Qd | A3                                | A2                                | A1                                | A0                                | B1                               | A1                               | B0                               | A0                               |
| Qm | B3                                | B2                                | B1                                | B0                                | B3                               | A3                               | B2                               | A2                               |

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VZIP{<c>}{<q>}.<dt> <Dd>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VZIP{<c>}{<q>}.<dt> <Qd>,
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
Applies when (Q == 0) VZIP{<c>}{<q>}.<dt> <Dd>,
```

```
<Dm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VZIP{<c>}{<q>}.<dt> <Qd>, <Qm>
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
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); if quadword_operation then if d == m then Q[d>>1] = bits(128) UNKNOWN; else bits(256) zipped_q; for e = 0 to (128 DIV esize) 1 Elem[zipped_q,2*e,esize] = Elem[Q[d>>1],e,esize]; Elem[zipped_q,2*e+1,esize] = Elem[Q[m>>1],e,esize]; Q[d>>1] = zipped_q<127:0>; Q[m>>1] = zipped_q<255:128>; else if d == m then D[d] = bits(64) UNKNOWN; else bits(128) zipped_d; for e = 0 to (64 DIV esize) - 1 Elem[zipped_d,2*e,esize] = Elem[D[d],e,esize]; Elem[zipped_d,2*e+1,esize] = Elem[D[m],e,esize]; D[d] = zipped_d<63:0>; D[m] = zipped_d<127:64>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.