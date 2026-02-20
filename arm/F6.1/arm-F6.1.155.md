## F6.1.155 VNMLS

Vector Negate Multiply Subtract multiplies together two floating-point register values, adds the negation of the floating-point value in the destination register to the product, and writes the result back to the destination register.

Depending on settings in the CPACR, NSACR, HCPTR, and FPEXC registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the Half-precision scalar variant

```
(FEAT_FP16) Applies when (size == 01) VNMLS{<c>}{<q>}.F16 <Sd>, <Sn>, <Sm>
```

## Encoding for the Single-precision scalar variant

```
Applies when (size == 10) VNMLS{<c>}{<q>}.F32 <Sd>, <Sn>, <Sm>
```

## Encoding for the Double-precision scalar variant

```
Applies when (size == 11) VNMLS{<c>}{<q>}.F64
```

```
<Dd>, <Dn>, <Dm>
```

## Decode for all variants of this encoding

```
if FPSCR.Len != '000' || FPSCR.Stride != '00' then UNDEFINED; if size == '00' || (size == '01' && !IsFeatureImplemented(FEAT_FP16)) then UNDEFINED; if size == '01' && cond != '1110' then UNPREDICTABLE; constant VFPNegMul vtype = if op == '1' then VFPNegMul_VNMLA else VFPNegMul_VNMLS; constant integer esize = 8 << UInt(size); constant integer d = if size == '11' then UInt(D:Vd) else UInt(Vd:D); constant integer n = if size == '11' then UInt(N:Vn) else UInt(Vn:N); constant integer m = if size == '11' then UInt(M:Vm) else UInt(Vm:M);
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
(size == 01) VNMLS{<c>}{<q>}.F16 <Sd>, <Sn>, <Sm>
```

## Encoding for the Single-precision scalar variant

```
Applies when (size == 10) VNMLS{<c>}{<q>}.F32
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
VNMLS{<c>}{<q>}.F64
```

```
<Dd>, <Dn>, <Dm>
```

## Decode for all variants of this encoding

```
if FPSCR.Len != '000' || FPSCR.Stride != '00' then UNDEFINED; if size == '00' || (size == '01' && !IsFeatureImplemented(FEAT_FP16)) then UNDEFINED; if size == '01' && InITBlock() then UNPREDICTABLE; constant VFPNegMul vtype = if op == '1' then VFPNegMul_VNMLA else VFPNegMul_VNMLS; constant integer esize = 8 << UInt(size); constant integer d = if size == '11' then UInt(D:Vd) else UInt(Vd:D); constant integer n = if size == '11' then UInt(N:Vn) else UInt(Vn:N); constant integer m = if size == '11' then UInt(M:Vm) else UInt(Vm:M);
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

&lt;Dn&gt;

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field.

&lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckVFPEnabled(TRUE); constant FPCR_Type fpcr = EffectiveFPCR(); case esize of when 16 constant bits(16) product16 = FPMul(H[n], H[m], fpcr); case vtype of when VFPNegMul_VNMLA H[d] = FPAdd(FPNeg(H[d], fpcr), FPNeg(product16, fpcr), fpcr); when VFPNegMul_VNMLS H[d] = FPAdd(FPNeg(H[d], fpcr), product16, fpcr); when VFPNegMul_VNMUL H[d] = FPNeg(product16, fpcr); when 32 constant bits(32) product32 = FPMul(S[n], S[m], fpcr); case vtype of when VFPNegMul_VNMLA S[d] = FPAdd(FPNeg(S[d], fpcr), FPNeg(product32, fpcr), fpcr); when VFPNegMul_VNMLS S[d] = FPAdd(FPNeg(S[d], fpcr), product32, fpcr); when VFPNegMul_VNMUL S[d] = FPNeg(product32, fpcr); when 64 constant bits(64) product64 = FPMul(D[n], D[m], fpcr); case vtype of when VFPNegMul_VNMLA D[d] = FPAdd(FPNeg(D[d], fpcr), FPNeg(product64, fpcr), fpcr); when VFPNegMul_VNMLS D[d] = FPAdd(FPNeg(D[d], fpcr), product64, fpcr); when VFPNegMul_VNMUL D[d] = FPNeg(product64, fpcr);
```

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.