## F6.1.77 VCVTT (BFloat16)

Converts from a single-precision value to a BFloat16 value in the top half of a single-precision register

Converts the single-precision value in a single-precision register to BFloat16 format and writes the result in the top half of a single-precision register, preserving the bottom 16 bits of the register.

Unlike the BFloat16 multiplication instructions, this instruction honors all the control bits in the FPSCR that apply to single-precision arithmetic, including the rounding mode. This instruction can generate a floating-point exception which causes a cumulative exception bit in the FPSCR to be set, or a synchronous exception to be taken, depending on the enable bits in the FPSCR.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

## A1

(FEAT\_AA32BF16)

<!-- image -->

## Encoding

```
VCVTT{<c>}{<q>}.BF16.F32 <Sd>, <Sm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AA32BF16) then constant integer d = UInt(Vd:D); constant integer m = UInt(Vm:M);
```

## T1

(FEAT\_AA32BF16)

<!-- image -->

## Encoding

```
VCVTT{<c>}{<q>}.BF16.F32 <Sd>, <Sm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AA32BF16) then UNDEFINED; constant integer d = UInt(Vd:D); constant integer m = UInt(Vm:M);
```

```
UNDEFINED;
```

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

&lt;q&gt;

&lt;Sd&gt;

Is the 32-bit name of the SIMD&amp;FP destination register, encoded in the 'Vd:D' field.

## &lt;Sm&gt;

Is the 32-bit name of the SIMD&amp;FP source register, encoded in the 'Vm:M' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckVFPEnabled(TRUE); S[d]<31:16> = FPConvertBF(S[m],
```

EffectiveFPCR());