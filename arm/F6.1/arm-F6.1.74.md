## F6.1.74 VCVTP (floating-point)

Convert floating-point to integer with Round towards +Infinity converts a value in a register from floating-point to a 32-bit integer using the Round towards +Infinity rounding mode, and places the result in a second register.

Depending on settings in the CPACR, NSACR, HCPTR, and FPEXC registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the Half-precision scalar variant

```
(FEAT_FP16) Applies when (size == 01) VCVTP{<q>}.<dt>.F16 <Sd>, <Sm>
```

## Encoding for the Single-precision scalar variant

```
Applies when (size == 10) VCVTP{<q>}.<dt>.F32 <Sd>,
```

```
<Sm>
```

## Encoding for the Double-precision scalar variant

```
Applies when (size == 11) VCVTP{<q>}.<dt>.F64 <Sd>,
```

```
<Dm>
```

## Decode for all variants of this encoding

```
if size == '00' then UNDEFINED; if size == '01' && !IsFeatureImplemented(FEAT_FP16) then UNDEFINED; constant FPRounding rounding = FPDecodeRM(RM); constant boolean unsigned = (op == '0'); constant integer esize = 8 << UInt(size); constant integer d = UInt(Vd:D); constant integer m = if size == '11' then UInt(M:Vm) else UInt(Vm:M);
```

T1

<!-- image -->

## Encoding for the Half-precision scalar variant

```
(FEAT_FP16) Applies when (size == 01) VCVTP{<q>}.<dt>.F16 <Sd>, <Sm>
```

## Encoding for the Single-precision scalar variant

```
Applies when (size == 10) VCVTP{<q>}.<dt>.F32 <Sd>,
```

```
<Sm>
```

## Encoding for the Double-precision scalar variant

```
Applies when (size == 11) VCVTP{<q>}.<dt>.F64 <Sd>,
```

```
<Dm>
```

## Decode for all variants of this encoding

```
if InITBlock() then UNPREDICTABLE; if size == '00' then UNDEFINED; if size == '01' && !IsFeatureImplemented(FEAT_FP16) then UNDEFINED; constant FPRounding rounding = FPDecodeRM(RM); constant boolean unsigned = (op == '0'); constant integer esize = 8 << UInt(size); constant integer d = UInt(Vd:D); constant integer m = if size == '11' then UInt(M:Vm) else UInt(Vm:M);
```

## CONSTRAINED UNPREDICTABLE behavior

If InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

## Assembler Symbols

&lt;q&gt;

See Standard assembler syntax fields.

Is the data type for the elements of the destination, encoded in 'op':

|   op | <dt>   |
|------|--------|
|    0 | U32    |
|    1 | S32    |

Is the 32-bit name of the SIMD&amp;FP destination register, encoded in the 'Vd:D' field.

## &lt;Sm&gt;

Is the 32-bit name of the SIMD&amp;FP source register, encoded in the 'Vm:M' field.

## &lt;Dm&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field.

&lt;dt&gt;

&lt;Sd&gt;

## Operation

```
EncodingSpecificOperations(); CheckVFPEnabled(TRUE); constant FPCR_Type fpcr = EffectiveFPCR(); case esize of when 16 S[d] = FPToFixed(H[m], 0, unsigned, fpcr, when 32 S[d] = FPToFixed(S[m], 0, unsigned, fpcr, when 64 S[d] = FPToFixed(D[m], 0, unsigned, fpcr,
```

```
rounding, 32); rounding, 32); rounding, 32);
```