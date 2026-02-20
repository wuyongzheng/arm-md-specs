## F6.1.134 VMOV (immediate)

Copy immediate value to a SIMD&amp;FP register places an immediate constant into every element of the destination register.

Depending on settings in the CPACR, NSACR, HCPTR, and FPEXC registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1, A2, A3, A4, and A5) and T32 (T1, T2, T3, T4, and T5).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VMOV{<c>}{<q>}.I32 <Dd>, #<imm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VMOV{<c>}{<q>}.I32 <Qd>, #<imm>
```

## Decode for all variants of this encoding

```
if op == '0' && cmode<0> == '1' && cmode<3:2> != '11' then SEE "VORR (immediate)"; if op == '1' && cmode != '1110' then SEE "Related encodings"; if Q == '1' && Vd<0> == '1' then UNDEFINED; constant boolean advsimd = TRUE; constant integer esize = 64; constant bits(esize) imm = AdvSIMDExpandImm(op, cmode, i:imm3:imm4); constant integer d = UInt(D:Vd); constant integer regs = if Q == '0' then 1 else 2;
```

A2

<!-- image -->

## Encoding for the Half-precision scalar variant

```
(size == 01)
```

```
(FEAT_FP16) Applies when VMOV{<c>}{<q>}.F16 <Sd>, #<imm>
```

## Encoding for the Single-precision scalar variant

```
Applies when (size == 10) VMOV{<c>}{<q>}.F32
```

```
<Sd>, #<imm>
```

## Encoding for the Double-precision scalar variant

```
Applies when (size == 11) VMOV{<c>}{<q>}.F64 <Dd>, #<imm>
```

## Decode for all variants of this encoding

```
if FPSCR.Len != '000' || FPSCR.Stride != '00' then UNDEFINED; if size == '00' || (size == '01' && !IsFeatureImplemented(FEAT_FP16)) then UNDEFINED; if size == '01' && cond != '1110' then UNPREDICTABLE; constant integer esize = 8 << UInt(size); constant bits(esize) imm = VFPExpandImm(imm4H:imm4L, esize); constant boolean advsimd = FALSE; constant integer d = if size == '11' then UInt(D:Vd) else UInt(Vd:D); constant integer regs = if size == '11' then 1 else 0;
```

## CONSTRAINED UNPREDICTABLE behavior

If size == '01' &amp;&amp; cond != '1110' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

## A3

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VMOV{<c>}{<q>}.I16 <Dd>, #<imm>
```

## Encoding for the 128-bit SIMD vector variant

Applies when

```
(Q == 1) VMOV{<c>}{<q>}.I16 <Qd>, #<imm>
```

## Decode for all variants of this encoding

```
if op == '0' && cmode<0> == '1' && cmode<3:2> != '11' then SEE "VORR (immediate)"; if op == '1' && cmode != '1110' then SEE "Related encodings"; if Q == '1' && Vd<0> == '1' then UNDEFINED; constant boolean advsimd = TRUE; constant integer esize = 64; constant bits(esize) imm = AdvSIMDExpandImm(op, cmode, i:imm3:imm4); constant integer d = UInt(D:Vd); constant integer regs = if Q == '0' then 1 else 2;
```

## A4

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VMOV{<c>}{<q>}.<dt>
```

```
<Dd>, #<imm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VMOV{<c>}{<q>}.<dt>
```

```
<Qd>, #<imm>
```

## Decode for all variants of this encoding

```
if op == '0' && cmode<0> == '1' && cmode<3:2> != '11' then SEE "VORR (immediate)"; if op == '1' && cmode != '1110' then SEE "Related encodings"; if Q == '1' && Vd<0> == '1' then UNDEFINED; constant boolean advsimd = TRUE; constant integer esize = 64; constant bits(esize) imm = AdvSIMDExpandImm(op, cmode, i:imm3:imm4); constant integer d = UInt(D:Vd); constant integer regs = if Q == '0' then 1 else 2;
```

## A5

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VMOV{<c>}{<q>}.I64 <Dd>, #<imm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VMOV{<c>}{<q>}.I64 <Qd>, #<imm>
```

## Decode for all variants of this encoding

```
if op == '0' && cmode<0> == '1' && cmode<3:2> != '11' then SEE "VORR (immediate)"; if op == '1' && cmode != '1110' then SEE "Related encodings"; if Q == '1' && Vd<0> == '1' then UNDEFINED; constant boolean advsimd = TRUE; constant integer esize = 64; constant bits(esize) imm = AdvSIMDExpandImm(op, cmode, i:imm3:imm4); constant integer d = UInt(D:Vd); constant integer regs = if Q == '0' then 1 else 2;
```

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VMOV{<c>}{<q>}.I32 <Dd>, #<imm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VMOV{<c>}{<q>}.I32
```

```
<Qd>, #<imm>
```

## Decode for all variants of this encoding

```
if op == '0' && cmode<0> == '1' && cmode<3:2> != '11' then SEE "VORR (immediate)"; if op == '1' && cmode != '1110' then SEE "Related encodings"; if Q == '1' && Vd<0> == '1' then UNDEFINED; constant boolean advsimd = TRUE; constant integer esize = 64; constant bits(esize) imm = AdvSIMDExpandImm(op, cmode, i:imm3:imm4); constant integer d = UInt(D:Vd); constant integer regs = if Q == '0' then 1 else 2;
```

T2

<!-- image -->

## Encoding for the Half-precision scalar variant

```
(FEAT_FP16) Applies when (size == 01) VMOV{<c>}{<q>}.F16 <Sd>, #<imm>
```

## Encoding for the Single-precision scalar variant

```
Applies when (size == 10) VMOV{<c>}{<q>}.F32
```

```
<Sd>, #<imm>
```

## Encoding for the Double-precision scalar variant

```
Applies when (size == 11) VMOV{<c>}{<q>}.F64 <Dd>, #<imm>
```

## Decode for all variants of this encoding

```
if FPSCR.Len != '000' || FPSCR.Stride != '00' then UNDEFINED; if size == '00' || (size == '01' && !IsFeatureImplemented(FEAT_FP16)) then UNDEFINED; if size == '01' && InITBlock() then UNPREDICTABLE; constant integer esize = 8 << UInt(size); constant bits(esize) imm = VFPExpandImm(imm4H:imm4L, esize); constant boolean advsimd = FALSE; constant integer d = if size == '11' then UInt(D:Vd) else UInt(Vd:D); constant integer regs = if size == '11' then 1 else 0;
```

## CONSTRAINED UNPREDICTABLE behavior

If size == '01' &amp;&amp; InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

T3

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VMOV{<c>}{<q>}.I16 <Dd>, #<imm>
```

## Encoding for the 128-bit SIMD vector variant

Applies when

```
(Q == 1) VMOV{<c>}{<q>}.I16 <Qd>, #<imm>
```

## Decode for all variants of this encoding

```
if op == '0' && cmode<0> == '1' && cmode<3:2> != '11' then SEE "VORR (immediate)"; if op == '1' && cmode != '1110' then SEE "Related encodings"; if Q == '1' && Vd<0> == '1' then UNDEFINED; constant boolean advsimd = TRUE; constant integer esize = 64; constant bits(esize) imm = AdvSIMDExpandImm(op, cmode, i:imm3:imm4); constant integer d = UInt(D:Vd); constant integer regs = if Q == '0' then 1 else 2;
```

T4

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VMOV{<c>}{<q>}.<dt>
```

```
<Dd>, #<imm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VMOV{<c>}{<q>}.<dt>
```

```
<Qd>, #<imm>
```

## Decode for all variants of this encoding

```
if op == '0' && cmode<0> == '1' && cmode<3:2> != '11' then SEE "VORR (immediate)"; if op == '1' && cmode != '1110' then SEE "Related encodings"; if Q == '1' && Vd<0> == '1' then UNDEFINED; constant boolean advsimd = TRUE; constant integer esize = 64; constant bits(esize) imm = AdvSIMDExpandImm(op, cmode, i:imm3:imm4); constant integer d = UInt(D:Vd); constant integer regs = if Q == '0' then 1 else 2;
```

T5

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VMOV{<c>}{<q>}.I64 <Dd>, #<imm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VMOV{<c>}{<q>}.I64 <Qd>, #<imm>
```

## Decode for all variants of this encoding

```
if op == '0' && cmode<0> == '1' && cmode<3:2> != '11' then SEE "VORR (immediate)"; if op == '1' && cmode != '1110' then SEE "Related encodings"; if Q == '1' && Vd<0> == '1' then UNDEFINED; constant boolean advsimd = TRUE; constant integer esize = 64; constant bits(esize) imm = AdvSIMDExpandImm(op, cmode, i:imm3:imm4); constant integer d = UInt(D:Vd); constant integer regs = if Q == '0' then 1 else 2;
```

Related encodings: See Advanced SIMD one register and modified immediate for the T32 instruction set, or Advanced SIMD one register and modified immediate for the A32 instruction set.

## Assembler Symbols

<!-- image -->

For the 'A1 128-bit SIMD vector', 'A1 64-bit SIMD vector', 'A3 128-bit SIMD vector', 'A3 64-bit SIMD vector', 'A4 128-bit SIMD vector', 'A4 64-bit SIMD vector', 'A5 128-bit SIMD vector', and 'A5 64-bit SIMD vector' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'A2 Double-precision scalar', 'A2 Half-precision scalar', 'A2 Single-precision scalar', 'T1 128-bit SIMD vector', 'T1 64-bit SIMD vector', 'T2 Double-precision scalar', 'T2 Half-precision scalar', 'T2 Single-precision scalar', 'T3 128-bit SIMD vector', 'T3 64-bit SIMD vector', 'T4 128-bit SIMD vector', 'T4 64-bit SIMD vector', 'T5 128-bit SIMD vector', and 'T5 64-bit SIMD vector' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

&lt;q&gt;

## &lt;Dd&gt;

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;imm&gt;

```
For the 'A1 128-bit SIMD vector', 'A1 64-bit SIMD vector', 'A3 128-bit SIMD vector', 'A3 64-bit SIMD vector', 'A4 128-bit SIMD vector', 'A4 64-bit SIMD vector', 'A5 128-bit SIMD vector', 'A5 64-bit SIMD vector', 'T1 128-bit SIMD vector', 'T1 64-bit SIMD vector', 'T3 128-bit SIMD vector', 'T3 64-bit SIMD vector', 'T4 128-bit SIMD vector', 'T4 64-bit SIMD vector', 'T5 128-bit SIMD vector', and 'T5 64-bit SIMD vector' variants: is a constant of the specified type that is replicated to fill the destination register. For details of the range of constants available and the encoding of <imm> , see Modified immediate constants in T32 and A32 Advanced SIMD instructions.
```

For the 'A2 Double-precision scalar', 'A2 Half-precision scalar', 'A2 Single-precision scalar', 'T2 Double-precision scalar', 'T2 Half-precision scalar', and 'T2 Single-precision scalar' variants: is a signed floating-point constant with 3-bit exponent and normalized 4 bits of precision, encoded in 'imm4H:imm4L'. For details of the range of constants available and the encoding of &lt;imm&gt; , see Modified immediate constants in T32 and A32 floating-point instructions.

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

Is the 32-bit name of the SIMD&amp;FP destination register, encoded in the 'Vd:D' field.

The data type, encoded in 'cmode':

## &lt;Qd&gt;

## &lt;Sd&gt;

&lt;dt&gt;

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDOrVFPEnabled(TRUE, advsimd); if esize <= 32 then S[d] = ZeroExtend(imm, 32); else for r = 0 to regs-1 D[d+r] = ZeroExtend(imm, 64);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

| cmode   | <dt>   |
|---------|--------|
| 110x    | I32    |
| 1110    | I8     |
| 1111    | F32    |