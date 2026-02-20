## F6.1.64 VCVT (between floating-point and fixed-point, floating-point)

Convert between floating-point and fixed-point converts a value in a register from floating-point to fixed-point, or from fixed-point to floating-point. Software can specify the fixed-point value as either signed or unsigned.

The fixed-point value can be 16-bit or 32-bit. Conversions from fixed-point values take their operand from the low-order bits of the source register and ignore any remaining bits. Signed conversions to fixed-point values sign-extend the result value to the destination register width. Unsigned conversions to fixed-point values zero-extend the result value to the destination register width.

The floating-point to fixed-point operation uses the Round towards Zero rounding mode. The fixed-point to floating-point operation uses the Round to Nearest rounding mode.

Depending on settings in the CPACR, NSACR, HCPTR, and FPEXC registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the Half-precision scalar variant

== 01)

```
(FEAT_FP16) Applies when (op == 0 && sf VCVT{<c>}{<q>}.F16.<dt> <Sdm>, <Sdm>, #<fbits>
```

## Encoding for the Half-precision scalar variant

== 01)

```
(FEAT_FP16) Applies when (op == 1 && sf VCVT{<c>}{<q>}.<dt>.F16 <Sdm>, <Sdm>, #<fbits>
```

## Encoding for the Single-precision scalar variant

Applies when (op

```
== 0 && sf == 10) VCVT{<c>}{<q>}.F32.<dt>
```

```
<Sdm>, <Sdm>, #<fbits>
```

## Encoding for the Single-precision scalar variant

```
Applies when (op == 1 && sf == 10) VCVT{<c>}{<q>}.<dt>.F32
```

```
<Sdm>, <Sdm>, #<fbits>
```

## Encoding for the Double-precision scalar variant

Applies when

```
(op == 0 && sf == 11) VCVT{<c>}{<q>}.F64.<dt> <Ddm>, <Ddm>, #<fbits>
```

## Encoding for the Double-precision scalar variant

Applies when (op

```
== 1 && sf == 11) VCVT{<c>}{<q>}.<dt>.F64 <Ddm>, <Ddm>, #<fbits>
```

## Decode for all variants of this encoding

```
if sf == '00' || (sf == '01' && !IsFeatureImplemented(FEAT_FP16)) then UNDEFINED; if sf == '01' && cond != '1110' then UNPREDICTABLE; constant boolean to_fixed = (op == '1'); constant boolean unsigned = (U == '1'); constant integer size = if sx == '0' then 16 else 32; constant integer frac_bits = size -UInt(imm4:i); constant integer fp_size = 8 << UInt(sf); constant integer d = if sf == '11' then UInt(D:Vd) else UInt(Vd:D); if frac_bits < 0 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If frac\_bits &lt; 0 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The value in the destination register is UNKNOWN.

T1

<!-- image -->

## Encoding for the Half-precision scalar variant

```
(FEAT_FP16) Applies when (op == 0 && sf == 01) VCVT{<c>}{<q>}.F16.<dt> <Sdm>, <Sdm>, #<fbits>
```

## Encoding for the Half-precision scalar variant

== 01)

```
(FEAT_FP16) Applies when (op == 1 && sf VCVT{<c>}{<q>}.<dt>.F16 <Sdm>, <Sdm>, #<fbits>
```

## Encoding for the Single-precision scalar variant

```
Applies when (op == 0 && sf == 10) VCVT{<c>}{<q>}.F32.<dt>
```

```
<Sdm>, <Sdm>, #<fbits>
```

## Encoding for the Single-precision scalar variant

Applies when

```
(op == 1 && sf == 10)
```

```
VCVT{<c>}{<q>}.<dt>.F32 <Sdm>, <Sdm>, #<fbits>
```

## Encoding for the Double-precision scalar variant

```
Applies when (op == 0 && sf == 11) VCVT{<c>}{<q>}.F64.<dt> <Ddm>, <Ddm>, #<fbits>
```

## Encoding for the Double-precision scalar variant

```
Applies when (op == 1 && sf == 11) VCVT{<c>}{<q>}.<dt>.F64 <Ddm>, <Ddm>, #<fbits>
```

## Decode for all variants of this encoding

```
if sf == '00' || (sf == '01' && !IsFeatureImplemented(FEAT_FP16)) then UNDEFINED; if sf == '01' && InITBlock() then UNPREDICTABLE; constant boolean to_fixed = (op == '1'); constant boolean unsigned = (U == '1'); constant integer size = if sx == '0' then 16 else 32; constant integer frac_bits = size -UInt(imm4:i); constant integer fp_size = 8 << UInt(sf); constant integer d = if sf == '11' then UInt(D:Vd) else UInt(Vd:D); if frac_bits < 0 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If frac\_bits &lt; 0 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The value in the destination register is UNKNOWN.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors, and particularly VCVT (between floating-point and fixed-point).

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the data type for the fixed-point number, encoded in 'U:sx':

|   U |   sx | <dt>   |
|-----|------|--------|
|   0 |    0 | S16    |
|   0 |    1 | S32    |
|   1 |    0 | U16    |
|   1 |    1 | U32    |

## &lt;Sdm&gt;

Is the 32-bit name of the SIMD&amp;FP destination and source register, encoded in the 'Vd:D' field.

## &lt;fbits&gt;

The number of fraction bits in the fixed-point number:

- If &lt;dt&gt; is S16 or U16 , &lt;fbits&gt; must be in the range 0-16. (16 &lt;fbits&gt; ) is encoded in [imm4, i]

&lt;q&gt;

&lt;dt&gt;

## &lt;Ddm&gt;

Is the 64-bit name of the SIMD&amp;FP destination and source register, encoded in the 'D:Vd' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckVFPEnabled(TRUE); constant FPCR_Type fpcr = EffectiveFPCR(); if to_fixed then bits(size) result; case fp_size of when 16 result = FPToFixed(H[d], frac_bits, unsigned, fpcr, FPRounding_ZERO, size); S[d] = Extend(result, 32, unsigned); when 32 result = FPToFixed(S[d], frac_bits, unsigned, fpcr, FPRounding_ZERO, size); S[d] = Extend(result, 32, unsigned); when 64 result = FPToFixed(D[d], frac_bits, unsigned, fpcr, FPRounding_ZERO, size); D[d] = Extend(result, 64, unsigned); else case fp_size of when 16 H[d] = FixedToFP(S[d]<size-1:0>, frac_bits, unsigned, fpcr, FPRounding_TIEEVEN, 16); when 32 S[d] = FixedToFP(S[d]<size-1:0>, frac_bits, unsigned, fpcr, FPRounding_TIEEVEN, 32); when 64 D[d] = FixedToFP(D[d]<size-1:0>, frac_bits, unsigned, fpcr, FPRounding_TIEEVEN, 64);
```

- If &lt;dt&gt; is S32 or U32 , &lt;fbits&gt; must be in the range 1-32. (32 &lt;fbits&gt; ) is encoded in [imm4, i] .