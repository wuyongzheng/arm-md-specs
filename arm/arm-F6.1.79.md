## F6.1.79 VDOT (vector)

BFloat16 floating-point (BF16) dot product (vector). This instruction delimits the source vectors into pairs of 16-bit BF16 elements. Within each pair, the elements in the first source vector are multiplied by the corresponding elements in the second source vector. The resulting single-precision products are then summed and added destructively to the single-precision element in the destination vector which aligns with the pair of BF16 values in the first source vector. The instruction does not update the FPSCR exception status.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

(FEAT\_AA32BF16)

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VDOT{<q>}.BF16
```

```
<Dd>, <Dn>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VDOT{<q>}.BF16
```

```
<Qd>, <Qn>, <Qm>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_AA32BF16) then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then UNDEFINED; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer regs = if Q == '1' then 2 else 1;
```

T1

(FEAT\_AA32BF16)

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VDOT{<q>}.BF16
```

```
<Dd>, <Dn>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

Applies when

```
(Q == 1)
```

```
VDOT{<q>}.BF16
```

```
<Qd>, <Qn>, <Qm>
```

## Decode for all variants of this encoding

```
if InITBlock() then UNPREDICTABLE; if !IsFeatureImplemented(FEAT_AA32BF16) then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then UNDEFINED; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer regs = if Q == '1' then 2 else 1;
```

## Assembler Symbols

## &lt;q&gt;

See Standard assembler syntax fields.

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;Dd&gt;

- &lt;Dn&gt;

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field.

## &lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field.

- &lt;Qd&gt;
- &lt;Qn&gt;

Is the 128-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field as &lt;Qn&gt;*2.

## &lt;Qm&gt;

Is the 128-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

```
CheckAdvSIMDEnabled(); constant FPCR_Type fpcr = StandardFPCR(); bits(64) operand1; bits(64) operand2; bits(64) result; for r = 0 to regs-1 operand1 = Din[n+r]; operand2 = Din[m+r]; result = Din[d+r]; for e = 0 to 1 constant bits(16) elt1_a = Elem[operand1, 2 * e + 0, 16]; constant bits(16) elt1_b = Elem[operand1, 2 * e + 1, 16]; constant bits(16) elt2_a = Elem[operand2, 2 * e + 0, 16]; constant bits(16) elt2_b = Elem[operand2, 2 * e + 1, 16]; constant bits(32) sum = FPAdd_BF16(BFMulH(elt1_a, elt2_a, fpcr), BFMulH(elt1_b, elt2_b,
```

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

```
fpcr), fpcr);
```

```
Elem[result, e, 32] = FPAdd_BF16(Elem[result, e, 32], sum, fpcr); D[d+r] = result;
```