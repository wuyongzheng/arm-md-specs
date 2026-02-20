## F6.1.76 VCVTT

Convert to or from a half-precision value in the top half of a single-precision register

Convert to or from a half-precision value in the top half of a single-precision register does one of the following:

- Converts the half-precision value in the top half of a single-precision register to single-precision and writes the result to a single-precision register.
- Converts the half-precision value in the top half of a single-precision register to double-precision and writes the result to a double-precision register.
- Converts the single-precision value in a single-precision register to half-precision and writes the result into the top half of a single-precision register, preserving the other half of the destination register.
- Converts the double-precision value in a double-precision register to half-precision and writes the result into the top half of a single-precision register, preserving the other half of the destination register.

Depending on settings in the CPACR, NSACR, HCPTR, and FPEXC registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the Half-precision to single-precision variant

```
Applies when (op == 0 && sz == 0) VCVTT{<c>}{<q>}.F32.F16 <Sd>, <Sm>
```

## Encoding for the Half-precision to double-precision variant

```
== 1)
```

```
Applies when (op == 0 && sz VCVTT{<c>}{<q>}.F64.F16 <Dd>, <Sm>
```

## Encoding for the Single-precision to half-precision variant

```
== 0)
```

```
Applies when (op == 1 && sz VCVTT{<c>}{<q>}.F16.F32 <Sd>, <Sm>
```

## Encoding for the Double-precision to half-precision variant

```
Applies when == 1)
```

```
(op == 1 && sz VCVTT{<c>}{<q>}.F16.F64 <Sd>, <Dm>
```

## Decode for all variants of this encoding

```
constant integer d = if sz == '1' && op == '0' then UInt(D:Vd) constant integer m = if sz == '1' && op == '1' then UInt(M:Vm) else constant boolean uses_double = (sz == '1'); constant boolean convert_from_half = (op == '0'); constant integer lowbit = (if T == '1' then 16 else 0);
```

```
else UInt(Vd:D); UInt(Vm:M);
```

T1

<!-- image -->

## Encoding for the Half-precision to single-precision variant

```
== 0)
```

```
Applies when (op == 0 && sz VCVTT{<c>}{<q>}.F32.F16 <Sd>, <Sm>
```

## Encoding for the Half-precision to double-precision variant

```
Applies when == 1)
```

```
(op == 0 && sz VCVTT{<c>}{<q>}.F64.F16 <Dd>, <Sm>
```

## Encoding for the Single-precision to half-precision variant

```
== 0)
```

```
Applies when (op == 1 && sz VCVTT{<c>}{<q>}.F16.F32 <Sd>, <Sm>
```

## Encoding for the Double-precision to half-precision variant

```
== 1)
```

```
Applies when (op == 1 && sz VCVTT{<c>}{<q>}.F16.F64 <Sd>, <Dm>
```

## Decode for all variants of this encoding

```
constant integer d = if sz == '1' && op == '0' then UInt(D:Vd) constant integer m = if sz == '1' && op == '1' then UInt(M:Vm) else constant boolean uses_double = (sz == '1'); constant boolean convert_from_half = (op == '0'); constant integer lowbit = (if T == '1' then 16 else 0);
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

## &lt;Dd&gt;

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;Dm&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field.

```
else UInt(Vd:D); UInt(Vm:M);
```

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckVFPEnabled(TRUE); bits(16) hp; constant FPCR_Type fpcr = EffectiveFPCR(); if convert_from_half then hp = S[m]<lowbit+15:lowbit>; if uses_double then D[d] = FPConvert(hp, fpcr, 64); else S[d] = FPConvert(hp, fpcr, 32); else if uses_double then hp = FPConvert(D[m], fpcr, 16); else hp = FPConvert(S[m], fpcr, 16); S[d]<lowbit+15:lowbit> = hp;
```