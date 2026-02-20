## F6.1.57 VCVT (from single-precision to BFloat16, Advanced SIMD)

Vector Convert from single-precision to BFloat16 converts each 32-bit element in a vector from single-precision floating-point to BFloat16 format, and writes the result into a second vector. The result vector elements are half the width of the source vector elements.

Unlike the BFloat16 multiplication instructions, this instruction uses the Round to Nearest rounding mode, and can generate a floating-point exception that causes cumulative exception bits in the FPSCR to be set.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

## A1

(FEAT\_AA32BF16)

<!-- image -->

## Encoding

```
VCVT{<c>}{<q>}.BF16.F32 <Dd>, <Qm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AA32BF16) then UNDEFINED; if Vm<0> == '1' then UNDEFINED; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm);
```

## T1

(FEAT\_AA32BF16)

<!-- image -->

## Encoding

```
VCVT{<c>}{<q>}.BF16.F32 <Dd>, <Qm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AA32BF16) then UNDEFINED; if Vm<0> == '1' then UNDEFINED; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm);
```

## Assembler Symbols

&lt;c&gt;

For the 'A1' variant: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1' variant: see Standard assembler syntax fields.

See Standard assembler syntax fields.

&lt;q&gt;

## &lt;Dd&gt;

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;Qm&gt;

Is the 128-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

```
bits(128) operand; bits(64) result; if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); constant FPCR_Type fpcr = StandardFPCR(); operand = Q[m>>1]; for e = 0 to 3 constant bits(32) op = Elem[operand, Elem[result, e, 16] = D[d] = result;
```

```
e, 32]; FPConvertBF(op, fpcr);
```