## F6.1.58 VCVT (between double-precision and single-precision)

Convert between double-precision and single-precision does one of the following:

- Converts the value in a double-precision register to single-precision and writes the result to a single-precision register.
- Converts the value in a single-precision register to double-precision and writes the result to a double-precision register.

Depending on settings in the CPACR, NSACR, HCPTR, and FPEXC registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the Single-precision to double-precision variant

```
Applies when (size == 10) VCVT{<c>}{<q>}.F64.F32 <Dd>,
```

```
<Sm>
```

## Encoding for the Double-precision to single-precision variant

```
Applies when (size == 11) VCVT{<c>}{<q>}.F32.F64 <Sd>, <Dm>
```

## Decode for all variants of this encoding

```
constant boolean double_to_single = (size == '11'); constant integer d = if double_to_single then UInt(Vd:D) constant integer m = if double_to_single then UInt(M:Vm) else
```

T1

<!-- image -->

## Encoding for the Single-precision to double-precision variant

```
Applies when (size == 10) VCVT{<c>}{<q>}.F64.F32 <Dd>,
```

```
<Sm>
```

```
else UInt(D:Vd); UInt(Vm:M);
```

## Encoding for the Double-precision to single-precision variant

Applies when (size ==

```
11)
```

```
VCVT{<c>}{<q>}.F32.F64 <Sd>,
```

```
<Dm>
```

## Decode for all variants of this encoding

```
constant boolean double_to_single = (size == '11'); constant integer d = if double_to_single then UInt(Vd:D) constant integer m = if double_to_single then UInt(M:Vm) else
```

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

&lt;q&gt;

## &lt;Dd&gt;

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;Sm&gt;

Is the 32-bit name of the SIMD&amp;FP source register, encoded in the 'Vm:M' field.

## &lt;Sd&gt;

Is the 32-bit name of the SIMD&amp;FP destination register, encoded in the 'Vd:D' field.

## &lt;Dm&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckVFPEnabled(TRUE); if double_to_single then S[d] = FPConvert(D[m], else D[d] = FPConvert(S[m],
```

```
EffectiveFPCR(), 32); EffectiveFPCR(), 64);
```

```
else UInt(D:Vd); UInt(Vm:M);
```