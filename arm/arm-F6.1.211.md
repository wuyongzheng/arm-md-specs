## F6.1.211 VRINTZ (floating-point)

Round floating-point to integer towards Zero rounds a floating-point value to an integral floating-point value of the same size, using the Round towards Zero rounding mode. A zero input gives a zero result with the same sign, an infinite input gives an infinite result with the same sign, and a NaN is propagated as for normal arithmetic.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the Half-precision scalar variant

```
(size == 01)
```

```
(FEAT_FP16) Applies when VRINTZ{<c>}{<q>}.F16 <Sd>, <Sm>
```

## Encoding for the Single-precision scalar variant

```
Applies when (size == 10) VRINTZ{<c>}{<q>}.F32
```

```
<Sd>, <Sm>
```

## Encoding for the Double-precision scalar variant

```
Applies when (size == 11) VRINTZ{<c>}{<q>}.F64
```

```
<Dd>, <Dm>
```

## Decode for all variants of this encoding

```
if size == '00' || (size == '01' && !IsFeatureImplemented(FEAT_FP16)) then UNDEFINED; if size == '01' && cond != '1110' then UNPREDICTABLE; constant boolean zero_rounding = (op == '1'); constant boolean exact = FALSE; constant integer esize = 8 << UInt(size); constant integer d = if size == '11' then UInt(D:Vd) else UInt(Vd:D); constant integer m = if size == '11' then UInt(M:Vm) else UInt(Vm:M);
```

T1

<!-- image -->

## Encoding for the Half-precision scalar variant

```
(FEAT_FP16) Applies when (size == 01) VRINTZ{<c>}{<q>}.F16 <Sd>, <Sm>
```

## Encoding for the Single-precision scalar variant

```
Applies when (size == 10) VRINTZ{<c>}{<q>}.F32
```

```
<Sd>, <Sm>
```

## Encoding for the Double-precision scalar variant

```
Applies when (size == 11) VRINTZ{<c>}{<q>}.F64
```

```
<Dd>, <Dm>
```

## Decode for all variants of this encoding

```
if size == '00' || (size == '01' && !IsFeatureImplemented(FEAT_FP16)) then UNDEFINED; if size == '01' && InITBlock() then UNPREDICTABLE; constant boolean zero_rounding = (op == '1'); constant boolean exact = FALSE; constant integer esize = 8 << UInt(size); constant integer d = if size == '11' then UInt(D:Vd) else UInt(Vd:D); constant integer m = if size == '11' then UInt(M:Vm) else UInt(Vm:M);
```

## CONSTRAINED UNPREDICTABLE behavior

If InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

## Assembler Symbols

```
<c> See Standard assembler syntax fields. <q> See Standard assembler syntax fields. <Sd> Is the 32-bit name of the SIMD&FP destination register, encoded in the 'Vd:D' field. <Sm> Is the 32-bit name of the SIMD&FP source register, encoded in the 'Vm:M' field. <Dd> Is the 64-bit name of the SIMD&FP destination register, encoded in the 'D:Vd' field. <Dm>
```

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckVFPEnabled(TRUE); constant FPCR_Type fpcr = EffectiveFPCR(); constant FPRounding rounding = if zero_rounding then FPRounding_ZERO else FPRoundingMode(fpcr); case esize of when 16 H[d] = FPRoundInt(H[m], fpcr, rounding, exact); when 32 S[d] = FPRoundInt(S[m], fpcr, rounding, exact); when 64 D[d] = FPRoundInt(D[m], fpcr, rounding, exact);
```