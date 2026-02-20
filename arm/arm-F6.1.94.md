## F6.1.94 VFNMA

Vector Fused Negate Multiply Accumulate negates one floating-point register value and multiplies it by another floating-point register value, adds the negation of the floating-point value in the destination register to the product, and writes the result back to the destination register. The instruction does not round the result of the multiply before the addition.

Depending on settings in the CPACR, NSACR, HCPTR, and FPEXC registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

## A1

<!-- image -->

## Encoding for the Half-precision scalar variant

(size == 01)

```
(FEAT_FP16) Applies when VFNMA{<c>}{<q>}.F16 <Sd>, <Sn>, <Sm>
```

## Encoding for the Single-precision scalar variant

```
Applies when (size == 10) VFNMA{<c>}{<q>}.F32
```

```
<Sd>, <Sn>, <Sm>
```

## Encoding for the Double-precision scalar variant

```
Applies when (size == 11) VFNMA{<c>}{<q>}.F64
```

```
<Dd>, <Dn>, <Dm>
```

## Decode for all variants of this encoding

```
if FPSCR.Len != '000' || FPSCR.Stride != '00' then UNDEFINED; if size == '00' || (size == '01' && !IsFeatureImplemented(FEAT_FP16)) then UNDEFINED; if size == '01' && cond != '1110' then UNPREDICTABLE; constant boolean op1_neg = (op == '1'); constant integer esize = 8 << UInt(size); constant integer d = if size == '11' then UInt(D:Vd) else UInt(Vd:D); constant integer n = if size == '11' then UInt(N:Vn) else UInt(Vn:N); constant integer m = if size == '11' then UInt(M:Vm) else UInt(Vm:M);
```

## CONSTRAINED UNPREDICTABLE behavior

If size == '01' &amp;&amp; cond != '1110' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

T1

<!-- image -->

## Encoding for the Half-precision scalar variant

(FEAT\_FP16) Applies when

```
VFNMA{<c>}{<q>}.F16
```

```
(size == 01) <Sd>, <Sn>, <Sm>
```

## Encoding for the Single-precision scalar variant

```
Applies when (size == 10) VFNMA{<c>}{<q>}.F32
```

```
<Sd>, <Sn>, <Sm>
```

## Encoding for the Double-precision scalar variant

Applies when (size ==

```
11)
```

```
VFNMA{<c>}{<q>}.F64 <Dd>, <Dn>, <Dm>
```

## Decode for all variants of this encoding

```
if FPSCR.Len != '000' || FPSCR.Stride != '00' then UNDEFINED; if size == '00' || (size == '01' && !IsFeatureImplemented(FEAT_FP16)) then UNDEFINED; if size == '01' && InITBlock() then UNPREDICTABLE; constant boolean op1_neg = (op == '1'); constant integer esize = 8 << UInt(size); constant integer d = if size == '11' then UInt(D:Vd) else UInt(Vd:D); constant integer n = if size == '11' then UInt(N:Vn) else UInt(Vn:N); constant integer m = if size == '11' then UInt(M:Vm) else UInt(Vm:M);
```

## CONSTRAINED UNPREDICTABLE behavior

If size == '01' &amp;&amp; InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the 32-bit name of the SIMD&amp;FP destination register, encoded in the 'Vd:D' field.

Is the 32-bit name of the first SIMD&amp;FP source register, encoded in the 'Vn:N' field.

&lt;q&gt;

&lt;Sd&gt;

<!-- image -->

&lt;Sn&gt;

## &lt;Sm&gt;

Is the 32-bit name of the second SIMD&amp;FP source register, encoded in the 'Vm:M' field.

&lt;Dd&gt;

## &lt;Dn&gt;

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field.

## &lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckVFPEnabled(TRUE); constant FPCR_Type fpcr = EffectiveFPCR(); case esize of when 16 constant bits(16) op16 = if op1_neg then FPNeg(H[n], fpcr) else H[n]; H[d] = FPMulAdd(FPNeg(H[d], fpcr), op16, H[m], fpcr); when 32 constant bits(32) op32 = if op1_neg then FPNeg(S[n], fpcr) else S[n]; S[d] = FPMulAdd(FPNeg(S[d], fpcr), op32, S[m], fpcr); when 64 constant bits(64) op64 = if op1_neg then FPNeg(D[n], fpcr) else D[n]; D[d] = FPMulAdd(FPNeg(D[d], fpcr), op64, D[m], fpcr);
```

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.