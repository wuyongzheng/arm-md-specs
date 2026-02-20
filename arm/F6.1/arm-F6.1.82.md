## F6.1.82 VDUP (scalar)

Duplicate vector element to vector duplicates a single element of a vector into every element of the destination vector.

The scalar, and the destination vector elements, can be any one of 8-bit, 16-bit, or 32-bit fields. There is no distinction between data types.

For more information about scalars see Advanced SIMD scalars.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
Applies when (Q == 0) VDUP{<c>}{<q>}.<size> <Dd>, <Dm[x]>
```

## Encoding

```
Applies when (Q == 1) VDUP{<c>}{<q>}.<size> <Qd>, <Dm[x]>
```

## Decode for all variants of this encoding

```
if imm4 == 'x000' then UNDEFINED; if Q == '1' && Vd<0> == '1' then UNDEFINED; constant integer lsb = LowestSetBit(imm4<2:0>); constant integer esize = 8 << lsb; constant integer index = UInt(imm4<3:lsb+1>); constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm); constant integer elements = 64 DIV esize; constant integer regs = if Q == '0' then 1 else 2;
```

T1

<!-- image -->

## Encoding

```
Applies when (Q == 0) VDUP{<c>}{<q>}.<size> <Dd>, <Dm[x]>
```

## Encoding

Applies when

```
(Q == 1)
```

```
VDUP{<c>}{<q>}.<size> <Qd>, <Dm[x]>
```

## Decode for all variants of this encoding

```
if imm4 == 'x000' then UNDEFINED; if Q == '1' && Vd<0> == '1' then UNDEFINED; constant integer lsb = LowestSetBit(imm4<2:0>); constant integer esize = 8 << lsb; constant integer index = UInt(imm4<3:lsb+1>); constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm); constant integer elements = 64 DIV esize; constant integer regs = if Q == '0' then 1 else
```

## Assembler Symbols

&lt;c&gt;

For the 'A1 Advanced SIMD duplicate (scalar)' variant: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 Advanced SIMD duplicate (scalar)' variant: see Standard assembler syntax fields.

See Standard assembler syntax fields.

## &lt;size&gt;

The data size. It must be one of:

```
8 Encoded as imm4<0> = '1'. imm4<3:1> encodes the index [x] of the scalar. 16 Encoded as imm4<1:0> = '10'. imm4<3:2> encodes the index [x] of the scalar. 32 Encoded as imm4<2:0> = '100'. imm4<3> encodes the index [x] of the scalar.
```

&lt;q&gt;

## &lt;Dd&gt;

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;Dm[x]&gt;

The scalar. For details of how [x] is encoded, see the description of &lt;size&gt; .

## &lt;Qd&gt;

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); constant bits(esize) scalar = for r = 0 to regs-1 for e = 0 to elements-1 Elem[D[d+r],e,esize] = scalar;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

```
2;
```

```
Elem[D[m],index,esize];
```