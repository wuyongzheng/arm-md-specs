## F6.1.84 VEXT (byte elements)

Vector Extract extracts elements from the bottom end of the second operand vector and the top end of the first, concatenates them and places the result in the destination vector.

The elements of the vectors are treated as being 8-bit fields. There is no distinction between data types.

Figure F6-1 VEXT doubleword operation for imm = 3

<!-- image -->

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

This instruction is used by the pseudo-instruction VEXT (multibyte elements).

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VEXT{<c>}{<q>}.8 {<Dd>, }<Dn>, <Dm>, #<imm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VEXT{<c>}{<q>}.8 {<Qd>, }<Qn>, <Qm>, #<imm>
```

## Decode for all variants of this encoding

```
if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then UNDEFINED; if Q == '0' && imm4<3> == '1' then UNDEFINED; constant boolean quadword_operation = (Q == '1'); constant integer position = 8 * UInt(imm4); constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm);
```

## T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when

```
(Q == 0)
```

```
VEXT{<c>}{<q>}.8
```

```
{<Dd>, }<Dn>, <Dm>, #<imm>
```

## Encoding for the 128-bit SIMD vector variant

Applies when

```
(Q == 1)
```

```
VEXT{<c>}{<q>}.8 {<Qd>, }<Qn>, <Qm>, #<imm>
```

## Decode for all variants of this encoding

```
if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then UNDEFINED; if Q == '0' && imm4<3> == '1' then UNDEFINED; constant boolean quadword_operation = (Q == '1'); constant integer position = 8 * UInt(imm4); constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm);
```

## Assembler Symbols

&lt;c&gt;

For the 'A1 128-bit SIMD vector' and 'A1 64-bit SIMD vector' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 128-bit SIMD vector' and 'T1 64-bit SIMD vector' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;q&gt;

## &lt;Dd&gt;

## &lt;Dn&gt;

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field.

## &lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## &lt;imm&gt;

For the 'A1 64-bit SIMD vector' and 'T1 64-bit SIMD vector' variants: is the location of the extracted result in the concatenation of the operands, as a number of bytes from the least significant end, in the range 0 to 7, encoded in the 'imm4' field.

For the 'A1 128-bit SIMD vector' and 'T1 128-bit SIMD vector' variants: is the location of the extracted result in the concatenation of the operands, as a number of bytes from the least significant end, in the range 0 to 15, encoded in the 'imm4' field.

&lt;Qd&gt;

&lt;Qn&gt;

Is the 128-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field as &lt;Qn&gt;*2.

&lt;Qm&gt;

Is the 128-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); if quadword_operation then Q[d>>1] = (Q[m>>1]:Q[n>>1])<position+127:position>; else D[d] = (D[m]:D[n])<position+63:position>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.