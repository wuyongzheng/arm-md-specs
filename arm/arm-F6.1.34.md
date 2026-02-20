## F6.1.34 VBIC (immediate)

Vector Bitwise Bit Clear (immediate) performs a bitwise AND between a register value and the complement of an immediate value, and returns the result into the destination vector.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

This instruction is used by the pseudo-instruction V AND (immediate).

It has encodings from the following instruction sets: A32 (A1 and A2) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when

(Q == 0)

VBIC{&lt;c&gt;}{&lt;q&gt;}.I32

{&lt;Dd&gt;, }&lt;Dd&gt;, #&lt;imm&gt;

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VBIC{<c>}{<q>}.I32 {<Qd>, }<Qd>, #<imm>
```

## Decode for all variants of this encoding

```
if cmode<0> == '0' || cmode<3:2> == '11' then SEE "Related encodings"; if Q == '1' && Vd<0> == '1' then UNDEFINED; constant bits(64) imm64 = AdvSIMDExpandImm('1', cmode, i:imm3:imm4); constant integer d = UInt(D:Vd); constant integer regs = if Q == '0' then 1 else 2;
```

A2

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VBIC{<c>}{<q>}.I16 {<Dd>, }<Dd>, #<imm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VBIC{<c>}{<q>}.I16 {<Qd>, }<Qd>, #<imm>
```

## Decode for all variants of this encoding

```
if cmode<0> == '0' || cmode<3:2> == '11' then SEE "Related encodings"; if Q == '1' && Vd<0> == '1' then UNDEFINED; constant bits(64) imm64 = AdvSIMDExpandImm('1', cmode, i:imm3:imm4); constant integer d = UInt(D:Vd); constant integer regs = if Q == '0' then 1 else 2;
```

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when

(Q == 0)

```
VBIC{<c>}{<q>}.I32 {<Dd>, }<Dd>, #<imm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VBIC{<c>}{<q>}.I32 {<Qd>, }<Qd>, #<imm>
```

## Decode for all variants of this encoding

```
if cmode<0> == '0' || cmode<3:2> == '11' then SEE "Related encodings"; if Q == '1' && Vd<0> == '1' then UNDEFINED; constant bits(64) imm64 = AdvSIMDExpandImm('1', cmode, i:imm3:imm4); constant integer d = UInt(D:Vd); constant integer regs = if Q == '0' then 1 else 2;
```

T2

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VBIC{<c>}{<q>}.I16 {<Dd>, }<Dd>, #<imm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VBIC{<c>}{<q>}.I16 {<Qd>, }<Qd>, #<imm>
```

## Decode for all variants of this encoding

```
if cmode<0> == '0' || cmode<3:2> == '11' then SEE "Related encodings"; if Q == '1' && Vd<0> == '1' then UNDEFINED; constant bits(64) imm64 = AdvSIMDExpandImm('1', cmode, i:imm3:imm4); constant integer d = UInt(D:Vd); constant integer regs = if Q == '0' then 1 else 2;
```

Related encodings: See Advanced SIMD one register and modified immediate for the T32 instruction set, or Advanced SIMD one register and modified immediate for the A32 instruction set.

## Assembler Symbols

&lt;c&gt;

For the 'A1 128-bit SIMD vector', 'A1 64-bit SIMD vector', 'A2 128-bit SIMD vector', and 'A2 64-bit SIMD vector' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 128-bit SIMD vector', 'T1 64-bit SIMD vector', 'T2 128-bit SIMD vector', and 'T2 64-bit SIMD vector' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

&lt;q&gt;

## &lt;Dd&gt;

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;imm&gt;

Is a constant of the specified type that is replicated to fill the destination register. For details of the range of constants available and the encoding of &lt;imm&gt; , see Modified immediate constants in T32 and A32 Advanced SIMD instructions.

## &lt;Qd&gt;

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

The I8, I64, and F32 data types are permitted as pseudo-instructions, if the immediate can be represented by this instruction, and are encoded using a permitted encoding of the I16 or I32 data type.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); for r = 0 to regs-1 D[d+r] = D[d+r]
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

```
AND NOT(imm64);
```