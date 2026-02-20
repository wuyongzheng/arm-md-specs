## F6.1.223 VSELEQ, VSELGE, VSELGT, VSELVS

Floating-point conditional select allows the destination register to take the value in either one or the other source register according to the condition codes in the APSR.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the Equal, half-precision scalar variant

```
(FEAT_FP16) Applies when (cc == 00 && size == 01) VSELEQ.F16 <Sd>, <Sn>, <Sm> // (Cannot be conditional)
```

## Encoding for the Equal, single-precision scalar variant

```
Applies when (cc == 00 && size == 10) VSELEQ.F32 <Sd>, <Sn>, <Sm> // (Cannot be conditional)
```

## Encoding for the Equal, double-precision scalar variant

```
Applies when (cc == 00 && size == 11) VSELEQ.F64 <Dd>, <Dn>, <Dm> // (Cannot be
```

```
conditional)
```

## Encoding for the Greater than or Equal, half-precision scalar variant

```
(FEAT_FP16) Applies when (cc == 10 && size == 01) VSELGE.F16 <Sd>, <Sn>, <Sm> // (Cannot be conditional)
```

## Encoding for the Greater than or Equal, single-precision scalar variant

```
Applies when (cc == 10 && size == 10) VSELGE.F32 <Sd>, <Sn>, <Sm> // (Cannot be
```

```
conditional)
```

## Encoding for the Greater than or Equal, double-precision scalar variant

```
Applies when (cc == 10 && size == 11) VSELGE.F64 <Dd>, <Dn>, <Dm> // (Cannot be
```

```
conditional)
```

## Encoding for the Greater than, half-precision scalar variant

```
(FEAT_FP16) Applies when (cc == 11 && size == 01) VSELGT.F16 <Sd>, <Sn>, <Sm> // (Cannot be conditional)
```

## Encoding for the Greater than, single-precision scalar variant

```
Applies when (cc == 11 && size == 10) VSELGT.F32 <Sd>, <Sn>, <Sm> // (Cannot be conditional)
```

## Encoding for the Greater than, double-precision scalar variant

```
Applies when (cc == 11 && size == 11) VSELGT.F64 <Dd>, <Dn>, <Dm> // (Cannot be conditional)
```

## Encoding for the Unordered, half-precision scalar variant

```
(FEAT_FP16) Applies when (cc == 01 && size == 01)
```

```
VSELVS.F16 <Sd>, <Sn>, <Sm> // (Cannot be conditional)
```

## Encoding for the Unordered, single-precision scalar variant

```
Applies when
```

```
(cc == 01 && size == 10) VSELVS.F32 <Sd>, <Sn>, <Sm> // (Cannot be conditional)
```

## Encoding for the Unordered, double-precision scalar variant

```
Applies when (cc == 01 && size == 11) VSELVS.F64 <Dd>, <Dn>, <Dm> // (Cannot be conditional)
```

## Decode for all variants of this encoding

```
if size == '00' || (size == '01' && !IsFeatureImplemented(FEAT_FP16)) then UNDEFINED; constant integer esize = 8 << UInt(size); constant integer d = if size == '11' then UInt(D:Vd) else UInt(Vd:D); constant integer n = if size == '11' then UInt(N:Vn) else UInt(Vn:N); constant integer m = if size == '11' then UInt(M:Vm) else UInt(Vm:M); constant bits(4) condition = cc:(cc<1> EOR cc<0>):'0';
```

T1

<!-- image -->

## Encoding for the Equal, half-precision scalar variant

```
(FEAT_FP16) Applies when (cc == 00 && size == 01) VSELEQ.F16 <Sd>, <Sn>, <Sm> // (Not permitted in IT block)
```

## Encoding for the Equal, single-precision scalar variant

```
Applies when (cc == 00 && size == 10) VSELEQ.F32 <Sd>, <Sn>, <Sm> // (Not permitted in IT
```

```
block)
```

## Encoding for the Equal, double-precision scalar variant

```
Applies when (cc == 00 && size == 11) VSELEQ.F64 <Dd>, <Dn>, <Dm> // (Not permitted in IT
```

```
block)
```

## Encoding for the Greater than or Equal, half-precision scalar variant

```
(FEAT_FP16) Applies when (cc == 10 && size == 01) VSELGE.F16 <Sd>, <Sn>, <Sm> // (Not permitted in IT
```

```
block)
```

## Encoding for the Greater than or Equal, single-precision scalar variant

```
Applies when (cc == 10 && size == 10) VSELGE.F32 <Sd>, <Sn>, <Sm> // (Not permitted in IT block)
```

## Encoding for the Greater than or Equal, double-precision scalar variant

```
Applies when (cc == 10 && size == 11) VSELGE.F64 <Dd>, <Dn>, <Dm> // (Not permitted in IT block)
```

## Encoding for the Greater than, half-precision scalar variant

```
(FEAT_FP16) Applies when (cc == 11 && size == 01) VSELGT.F16 <Sd>, <Sn>, <Sm> // (Not permitted in IT
```

```
block)
```

## Encoding for the Greater than, single-precision scalar variant

```
Applies when (cc == 11 && size == 10)
```

```
VSELGT.F32 <Sd>, <Sn>, <Sm> // (Not permitted in IT block)
```

## Encoding for the Greater than, double-precision scalar variant

```
Applies when (cc == 11 && size == 11) VSELGT.F64 <Dd>, <Dn>, <Dm> // (Not permitted in IT block)
```

## Encoding for the Unordered, half-precision scalar variant

```
(FEAT_FP16) Applies when (cc == 01 && size == 01) VSELVS.F16 <Sd>, <Sn>, <Sm> // (Not permitted in IT block)
```

## Encoding for the Unordered, single-precision scalar variant

```
Applies when
```

```
(cc == 01 && size == 10)
```

```
VSELVS.F32 <Sd>, <Sn>, <Sm> // (Not permitted in IT block)
```

## Encoding for the Unordered, double-precision scalar variant

```
Applies when (cc == 01 && size == 11) VSELVS.F64 <Dd>, <Dn>, <Dm> // (Not permitted in IT
```

## Decode for all variants of this encoding

```
if InITBlock() then UNPREDICTABLE; if size == '00' || (size == '01' && !IsFeatureImplemented(FEAT_FP16)) then UNDEFINED; constant integer esize = 8 << UInt(size); constant integer d = if size == '11' then UInt(D:Vd) else UInt(Vd:D); constant integer n = if size == '11' then UInt(N:Vn) else UInt(Vn:N); constant integer m = if size == '11' then UInt(M:Vm) else UInt(Vm:M); constant bits(4) condition = cc:(cc<1> EOR cc<0>):'0';
```

```
block)
```

## CONSTRAINED UNPREDICTABLE behavior

If InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

## Assembler Symbols

## &lt;Sd&gt;

Is the 32-bit name of the SIMD&amp;FP destination register, encoded in the 'Vd:D' field.

## &lt;Sn&gt;

Is the 32-bit name of the first SIMD&amp;FP source register, encoded in the 'Vn:N' field.

## &lt;Sm&gt;

Is the 32-bit name of the second SIMD&amp;FP source register, encoded in the 'Vm:M' field.

## &lt;Dd&gt;

## &lt;Dn&gt;

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field.

## &lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## Operation

```
EncodingSpecificOperations(); CheckVFPEnabled(TRUE); case esize of when 16 H[d] = if ConditionHolds(condition) then H[n] else H[m]; when 32 S[d] = if ConditionHolds(condition) then S[n] else S[m]; when 64 D[d] = if ConditionHolds(condition) then D[n] else D[m];
```

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.