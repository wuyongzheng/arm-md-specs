## F6.1.233 VSQRT

Square Root calculates the square root of the value in a floating-point register and writes the result to another floating-point register.

Depending on settings in the CPACR, NSACR, HCPTR, and FPEXC registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the Half-precision scalar variant

(FEAT\_FP16) Applies when

```
(size == 01) VSQRT{<c>}{<q>}.F16 <Sd>, <Sm>
```

## Encoding for the Single-precision scalar variant

```
Applies when (size == 10) VSQRT{<c>}{<q>}.F32 <Sd>, <Sm>
```

## Encoding for the Double-precision scalar variant

```
Applies when (size == 11) VSQRT{<c>}{<q>}.F64
```

```
<Dd>, <Dm>
```

## Decode for all variants of this encoding

```
if size == '00' || (size == '01' && !IsFeatureImplemented(FEAT_FP16)) then UNDEFINED; if size == '01' && cond != '1110' then UNPREDICTABLE; if FPSCR.Len != '000' || FPSCR.Stride != '00' then UNDEFINED; constant integer esize = 8 << UInt(size); constant integer d = if size == '11' then UInt(D:Vd) else UInt(Vd:D); constant integer m = if size == '11' then UInt(M:Vm) else UInt(Vm:M);
```

## CONSTRAINED UNPREDICTABLE behavior

If size == '01' &amp;&amp; cond != '1110' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

T1

<!-- image -->

## Encoding for the Half-precision scalar variant

(FEAT\_FP16) Applies when (size == 01)

```
VSQRT{<c>}{<q>}.F16
```

```
<Sd>, <Sm>
```

## Encoding for the Single-precision scalar variant

Applies when (size ==

```
10) VSQRT{<c>}{<q>}.F32 <Sd>, <Sm>
```

## Encoding for the Double-precision scalar variant

Applies when (size ==

```
11)
```

```
VSQRT{<c>}{<q>}.F64 <Dd>, <Dm>
```

## Decode for all variants of this encoding

```
if size == '00' || (size == '01' && !IsFeatureImplemented(FEAT_FP16)) then if size == '01' && InITBlock() then UNPREDICTABLE; if FPSCR.Len != '000' || FPSCR.Stride != '00' then UNDEFINED; constant integer esize = 8 << UInt(size); constant integer d = if size == '11' then UInt(D:Vd) else UInt(Vd:D); constant integer m = if size == '11' then UInt(M:Vm) else UInt(Vm:M);
```

## CONSTRAINED UNPREDICTABLE behavior

If size == '01' &amp;&amp; InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

## Assembler Symbols

```
<c> See Standard assembler syntax fields. <q> See Standard assembler syntax fields. <Sd> Is the 32-bit name of the SIMD&FP destination register, encoded in the 'Vd:D' field. <Sm>
```

Is the 32-bit name of the SIMD&amp;FP source register, encoded in the 'Vm:M' field.

```
UNDEFINED;
```

&lt;Dd&gt;

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

&lt;Dm&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckVFPEnabled(TRUE); constant FPCR_Type fpcr = EffectiveFPCR(); case esize of when 16 H[d] = FPSqrt(H[m], fpcr); when 32 S[d] = FPSqrt(S[m], fpcr); when 64 D[d] = FPSqrt(D[m], fpcr);
```