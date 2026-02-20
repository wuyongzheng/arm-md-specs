## F6.1.206 VRINTP (floating-point)

Round floating-point to integer towards +Infinity rounds a floating-point value to an integral floating-point value of the same size using the Round towards +Infinity rounding mode. A zero input gives a zero result with the same sign, an infinite input gives an infinite result with the same sign, and a NaN is propagated as for normal arithmetic.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the Half-precision scalar variant

```
(FEAT_FP16) Applies when (size == 01) VRINTP{<q>}.F16 <Sd>, <Sm>
```

## Encoding for the Single-precision scalar variant

Applies when

```
(size == 10) VRINTP{<q>}.F32 <Sd>, <Sm>
```

## Encoding for the Double-precision scalar variant

```
Applies when (size == 11) VRINTP{<q>}.F64 <Dd>, <Dm>
```

## Decode for all variants of this encoding

```
if size == '00' || (size == '01' && !IsFeatureImplemented(FEAT_FP16)) then constant FPRounding rounding = FPDecodeRM(RM); constant boolean exact = FALSE; constant integer esize = 8 << UInt(size); constant integer d = if size == '11' then UInt(D:Vd) else UInt(Vd:D); constant integer m = if size == '11' then UInt(M:Vm) else UInt(Vm:M);
```

T1

<!-- image -->

## Encoding for the Half-precision scalar variant

(FEAT\_FP16) Applies when

```
(size == 01) VRINTP{<q>}.F16 <Sd>, <Sm>
```

```
UNDEFINED;
```

## Encoding for the Single-precision scalar variant

```
Applies when (size == 10) VRINTP{<q>}.F32 <Sd>, <Sm>
```

## Encoding for the Double-precision scalar variant

```
Applies when (size == 11) VRINTP{<q>}.F64 <Dd>, <Dm>
```

## Decode for all variants of this encoding

```
if InITBlock() then UNPREDICTABLE; if size == '00' || (size == '01' && !IsFeatureImplemented(FEAT_FP16)) then UNDEFINED; constant FPRounding rounding = FPDecodeRM(RM); constant boolean exact = FALSE; constant integer esize = 8 << UInt(size); constant integer d = if size == '11' then UInt(D:Vd) else UInt(Vd:D); constant integer m = if size == '11' then UInt(M:Vm) else UInt(Vm:M);
```

## CONSTRAINED UNPREDICTABLE behavior

If InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;q&gt;

See Standard assembler syntax fields.

## &lt;Sd&gt;

Is the 32-bit name of the SIMD&amp;FP destination register, encoded in the 'Vd:D' field.

## &lt;Sm&gt;

Is the 32-bit name of the SIMD&amp;FP source register, encoded in the 'Vm:M' field.

## &lt;Dd&gt;

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;Dm&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## Operation

```
EncodingSpecificOperations(); CheckVFPEnabled(TRUE); constant FPCR_Type fpcr = EffectiveFPCR(); case esize of when 16 H[d] = FPRoundInt(H[m], fpcr, rounding, when 32 S[d] = FPRoundInt(S[m], fpcr, rounding, when 64 D[d] = FPRoundInt(D[m], fpcr, rounding,
```

```
exact); exact); exact);
```