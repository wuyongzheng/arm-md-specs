## F6.1.131 VMMLA

BFloat16 floating-point matrix multiply-accumulate. This instruction multiplies the 2x4 matrix of BF16 values in the first 128-bit source vector by the 4x2 BF16 matrix in the second 128-bit source vector. The resulting 2x2 single-precision matrix product is then added destructively to the 2x2 single-precision matrix in the 128-bit destination vector. This is equivalent to performing a 4-way dot product per destination element. The instruction does not update the FPSCR exception status.

Note

Arm expects that the VMMLA instruction will deliver a peak BF16 multiply throughput that is at least as high as can be achieved using two VDOT instructions, with a goal that it should have significantly higher throughput.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

## A1

## (FEAT\_AA32BF16)

<!-- image -->

## Encoding

```
VMMLA{<q>}.BF16 <Qd>, <Qn>, <Qm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AA32BF16) then UNDEFINED; if Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1' then constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer regs = 2;
```

## T1

## (FEAT\_AA32BF16)

<!-- image -->

## Encoding

```
VMMLA{<q>}.BF16 <Qd>, <Qn>, <Qm>
```

```
UNDEFINED;
```

## Decode for this encoding

```
if InITBlock() then UNPREDICTABLE; if !IsFeatureImplemented(FEAT_AA32BF16) then UNDEFINED; if Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1' then constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer regs = 2;
```

## Assembler Symbols

&lt;q&gt;

See Standard assembler syntax fields.

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

&lt;Qd&gt;

&lt;Qn&gt;

Is the 128-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field as &lt;Qn&gt;*2.

## &lt;Qm&gt;

Is the 128-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

```
CheckAdvSIMDEnabled(); constant bits(128) operand1 = Q[n>>1]; constant bits(128) operand2 = Q[m>>1]; constant bits(128) acc = Q[d>>1]; constant FPCR_Type fpcr = EffectiveFPCR(); Q[d>>1] = BFMatMulAddH(acc,
```

```
UNDEFINED;
```

```
operand1, operand2, fpcr);
```