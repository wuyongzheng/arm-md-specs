## F6.1.135 VMOV (register)

Copy between FP registers copies the contents of one FP register to another.

Depending on settings in the CPACR, NSACR, HCPTR, and FPEXC registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A2) and T32 (T2).

A2

<!-- image -->

## Encoding for the Single-precision scalar variant

```
Applies when (size == 10) VMOV{<c>}{<q>}.F32 <Sd>,
```

```
<Sm>
```

## Encoding for the Double-precision scalar variant

```
Applies when (size == 11) VMOV{<c>}{<q>}.F64 <Dd>,
```

```
<Dm>
```

## Decode for all variants of this encoding

```
if FPSCR.Len != '000' || FPSCR.Stride != '00' then UNDEFINED; constant integer d = if size == '11' then UInt(D:Vd) else constant integer m = if size == '11' then UInt(M:Vm) constant boolean single_register = (size == '10'); constant boolean advsimd = FALSE;
```

T2

<!-- image -->

## Encoding for the Single-precision scalar variant

```
Applies when (size == 10) VMOV{<c>}{<q>}.F32 <Sd>,
```

```
<Sm>
```

## Encoding for the Double-precision scalar variant

```
Applies when (size == 11) VMOV{<c>}{<q>}.F64 <Dd>, <Dm>
```

```
UInt(Vd:D); else UInt(Vm:M);
```

## Decode for all variants of this encoding

```
if FPSCR.Len != '000' || FPSCR.Stride != '00' then UNDEFINED; constant integer d = if size == '11' then UInt(D:Vd) else constant integer m = if size == '11' then UInt(M:Vm) constant boolean single_register = (size == '10'); constant boolean advsimd = FALSE;
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

## Operation

```
if CheckAdvSIMDOrVFPEnabled(TRUE, advsimd);
```

```
ConditionPassed() then EncodingSpecificOperations(); if single_register then S[d] = S[m]; else D[d] = D[m];
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

```
UInt(Vd:D); else UInt(Vm:M);
```