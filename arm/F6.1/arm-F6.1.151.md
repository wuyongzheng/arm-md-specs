## F6.1.151 VMVN (immediate)

Vector Bitwise NOT (immediate) places the bitwise inverse of an immediate integer constant into every element of the destination register.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1, A2, and A3) and T32 (T1, T2, and T3).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VMVN{<c>}{<q>}.I32 <Dd>, #<imm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VMVN{<c>}{<q>}.I32 <Qd>, #<imm>
```

## Decode for all variants of this encoding

```
if (cmode<0> == '1' && cmode<3:2> != '11') || cmode<3:1> == '111' then SEE "Related encodings"; if Q == '1' && Vd<0> == '1' then UNDEFINED; constant bits(64) imm64 = AdvSIMDExpandImm('1', cmode, i:imm3:imm4); constant integer d = UInt(D:Vd); constant integer regs = if Q == '0' then 1 else 2;
```

A2

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VMVN{<c>}{<q>}.I16 <Dd>, #<imm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VMVN{<c>}{<q>}.I16 <Qd>, #<imm>
```

## Decode for all variants of this encoding

```
if (cmode<0> == '1' && cmode<3:2> != '11') || cmode<3:1> == '111' then SEE "Related encodings"; if Q == '1' && Vd<0> == '1' then UNDEFINED; constant bits(64) imm64 = AdvSIMDExpandImm('1', cmode, i:imm3:imm4); constant integer d = UInt(D:Vd); constant integer regs = if Q == '0' then 1 else 2;
```

A3

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VMVN{<c>}{<q>}.I32 <Dd>, #<imm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VMVN{<c>}{<q>}.I32
```

```
<Qd>, #<imm>
```

## Decode for all variants of this encoding

```
if (cmode<0> == '1' && cmode<3:2> != '11') || cmode<3:1> == '111' then SEE "Related encodings"; if Q == '1' && Vd<0> == '1' then UNDEFINED; constant bits(64) imm64 = AdvSIMDExpandImm('1', cmode, i:imm3:imm4); constant integer d = UInt(D:Vd); constant integer regs = if Q == '0' then 1 else 2;
```

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VMVN{<c>}{<q>}.I32 <Dd>, #<imm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VMVN{<c>}{<q>}.I32 <Qd>, #<imm>
```

## Decode for all variants of this encoding

```
if (cmode<0> == '1' && cmode<3:2> != '11') || cmode<3:1> == '111' then SEE "Related encodings"; if Q == '1' && Vd<0> == '1' then UNDEFINED; constant bits(64) imm64 = AdvSIMDExpandImm('1', cmode, i:imm3:imm4); constant integer d = UInt(D:Vd); constant integer regs = if Q == '0' then 1 else 2;
```

T2

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VMVN{<c>}{<q>}.I16 <Dd>, #<imm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VMVN{<c>}{<q>}.I16
```

```
<Qd>, #<imm>
```

## Decode for all variants of this encoding

```
if (cmode<0> == '1' && cmode<3:2> != '11') || cmode<3:1> == '111' then SEE "Related encodings"; if Q == '1' && Vd<0> == '1' then UNDEFINED; constant bits(64) imm64 = AdvSIMDExpandImm('1', cmode, i:imm3:imm4); constant integer d = UInt(D:Vd); constant integer regs = if Q == '0' then 1 else 2;
```

T3

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VMVN{<c>}{<q>}.I32 <Dd>, #<imm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VMVN{<c>}{<q>}.I32 <Qd>, #<imm>
```

## Decode for all variants of this encoding

```
if (cmode<0> == '1' && cmode<3:2> != '11') || cmode<3:1> == '111' then SEE "Related encodings"; if Q == '1' && Vd<0> == '1' then UNDEFINED; constant bits(64) imm64 = AdvSIMDExpandImm('1', cmode, i:imm3:imm4); constant integer d = UInt(D:Vd); constant integer regs = if Q == '0' then 1 else 2;
```

Related encodings: See Advanced SIMD one register and modified immediate for the T32 instruction set, or Advanced SIMD one register and modified immediate for the A32 instruction set.

## Assembler Symbols

&lt;c&gt;

For the 'A1 128-bit SIMD vector', 'A1 64-bit SIMD vector', 'A2 128-bit SIMD vector', 'A2 64-bit SIMD vector', 'A3 128-bit SIMD vector', and 'A3 64-bit SIMD vector' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 128-bit SIMD vector', 'T1 64-bit SIMD vector', 'T2 128-bit SIMD vector', 'T2 64-bit SIMD vector', 'T3 128-bit SIMD vector', and 'T3 64-bit SIMD vector' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

<!-- image -->

## &lt;Dd&gt;

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;imm&gt;

Is a constant of the specified type that is replicated to fill the destination register. For details of the range of constants available and the encoding of &lt;imm&gt; , see Modified immediate constants in T32 and A32 Advanced SIMD instructions.

<!-- image -->

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); for r = 0 to regs-1 D[d+r] = NOT(imm64);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.