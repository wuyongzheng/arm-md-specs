## F6.1.75 VCVTR

Convert floating-point to integer converts a value in a register from floating-point to a 32-bit integer, using the rounding mode specified by the FPSCR and places the result in a second register.

VCVT(between floating-point and fixed-point, floating-point) describes conversions between floating-point and 16-bit integers.

Depending on settings in the CPACR, NSACR, HCPTR, and FPEXC registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

## A1

<!-- image -->

## Encoding for the Half-precision scalar variant

```
(FEAT_FP16) Applies when (opc2 == 100 && size == 01) VCVTR{<c>}{<q>}.U32.F16 <Sd>, <Sm>
```

## Encoding for the Half-precision scalar variant

```
(FEAT_FP16) Applies when (opc2 == 101 &&
```

```
size == 01) VCVTR{<c>}{<q>}.S32.F16 <Sd>, <Sm>
```

## Encoding for the Single-precision scalar variant

```
Applies when (opc2 == 100 && size == 10) VCVTR{<c>}{<q>}.U32.F32 <Sd>, <Sm>
```

## Encoding for the Single-precision scalar variant

```
Applies when (opc2 == 101 && size ==
```

```
VCVTR{<c>}{<q>}.S32.F32 <Sd>,
```

```
10) <Sm>
```

## Encoding for the Double-precision scalar variant

```
Applies when
```

```
(opc2 == 100 && size == 11) VCVTR{<c>}{<q>}.U32.F64 <Sd>, <Dm>
```

## Encoding for the Double-precision scalar variant

```
Applies when (opc2 == 101 && size == VCVTR{<c>}{<q>}.S32.F64 <Sd>, <Dm>
```

```
11)
```

## Decode for all variants of this encoding

```
if opc2 != '000' && opc2 != '10x' then SEE "Related encodings"; if size == '00' then UNDEFINED; if size == '01' && !IsFeatureImplemented(FEAT_FP16) then UNDEFINED; if size == '01' && cond != '1110' then UNPREDICTABLE; constant integer esize = 8 << UInt(size); constant integer d = if size == '11' && opc2<2> == '0' then UInt(D:Vd) else UInt(Vd:D); constant integer m = if size == '11' && opc2<2> == '1' then UInt(M:Vm) else UInt(Vm:M); constant boolean to_integer = (opc2<2> == '1'); constant boolean unsigned = (if to_integer then opc2<0> else op) == '0'; constant boolean zero_rounding = to_integer && op == '1';
```

## CONSTRAINED UNPREDICTABLE behavior

If size == '01' &amp;&amp; cond != '1110' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

T1

<!-- image -->

## Encoding for the Half-precision scalar variant

```
(FEAT_FP16) Applies when (opc2 == 100 &&
```

```
VCVTR{<c>}{<q>}.U32.F16 <Sd>,
```

```
size == 01) <Sm>
```

## Encoding for the Half-precision scalar variant

```
(FEAT_FP16) Applies when (opc2 == 101 &&
```

```
size == 01) VCVTR{<c>}{<q>}.S32.F16 <Sd>, <Sm>
```

## Encoding for the Single-precision scalar variant

```
Applies when (opc2 == 100 && size == 10) VCVTR{<c>}{<q>}.U32.F32 <Sd>, <Sm>
```

## Encoding for the Single-precision scalar variant

```
Applies when (opc2 == 101 && size == 10) VCVTR{<c>}{<q>}.S32.F32 <Sd>, <Sm>
```

## Encoding for the Double-precision scalar variant

```
Applies when
```

```
(opc2 == 100 && size == 11) VCVTR{<c>}{<q>}.U32.F64 <Sd>, <Dm>
```

## Encoding for the Double-precision scalar variant

Applies when (opc2 == 101 &amp;&amp; size ==

```
VCVTR{<c>}{<q>}.S32.F64 <Sd>,
```

```
11) <Dm>
```

## Decode for all variants of this encoding

```
if opc2 != '000' && opc2 != '10x' then SEE "Related encodings"; if size == '00' then UNDEFINED; if size == '01' && !IsFeatureImplemented(FEAT_FP16) then UNDEFINED; if size == '01' && InITBlock() then UNPREDICTABLE; constant integer esize = 8 << UInt(size); constant integer m = if size == '11' && opc2<2> == '1' then UInt(M:Vm) else UInt(Vm:M); constant integer d = if size == '11' && opc2<2> == '0' then UInt(D:Vd) else UInt(Vd:D); constant boolean to_integer = (opc2<2> == '1'); constant boolean unsigned = (if to_integer then opc2<0> else op) == '0'; constant boolean zero_rounding = to_integer && op == '1';
```

## CONSTRAINED UNPREDICTABLE behavior

If size == '01' &amp;&amp; InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

Related encodings: See Floating-point data-processing for the T32 instruction set, or Floating-point data-processing for the A32 instruction set.

## Assembler Symbols

```
<c> See Standard assembler syntax fields. <q> See Standard assembler syntax fields. <Sd> Is the 32-bit name of the SIMD&FP destination register, encoded in the 'Vd:D' field. <Sm> Is the 32-bit name of the SIMD&FP source register, encoded in the 'Vm:M' field. <Dm> Is the 64-bit name of the SIMD&FP source register, encoded in the 'M:Vm' field.
```

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckVFPEnabled(TRUE); constant FPCR_Type fpcr = EffectiveFPCR(); constant FPRounding rounding = if zero_rounding then FPRounding_ZERO else FPRoundingMode(fpcr); if to_integer then case esize of when 16 S[d] = FPToFixed(H[m], 0, unsigned, fpcr, rounding, 32); when 32 S[d] = FPToFixed(S[m], 0, unsigned, fpcr, rounding, 32);
```

```
when 64 S[d] = FPToFixed(D[m], 0, unsigned, fpcr, rounding, 32); else case esize of when 16 H[d] = FixedToFP(S[m], 0, unsigned, fpcr, rounding, 16); when 32 S[d] = FixedToFP(S[m], 0, unsigned, fpcr, rounding, 32); when 64 D[d] = FixedToFP(S[m], 0, unsigned, fpcr, rounding, 64);
```