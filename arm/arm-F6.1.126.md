## F6.1.126 VMLS (floating-point)

Vector Multiply Subtract (floating-point)

Vector Multiply Subtract multiplies corresponding elements in two vectors, subtracts the products from corresponding elements of the destination vector, and places the results in the destination vector.

Note

Arm recommends that software does not use the VMLS instruction in the Round towards Plus Infinity and Round towards Minus Infinity rounding modes, because the rounding of the product and of the sum can change the result of the instruction in opposite directions, defeating the purpose of these rounding modes.

Depending on settings in the CPACR, NSACR, HCPTR, and FPEXC registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1 and A2) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0)
```

```
VMLS{<c>}{<q>}.<dt> <Dd>,
```

```
<Dn>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VMLS{<c>}{<q>}.<dt> <Qd>, <Qn>, <Qm>
```

## Decode for all variants of this encoding

```
if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then UNDEFINED; if sz == '1' && !IsFeatureImplemented(FEAT_FP16) then UNDEFINED; constant boolean advsimd = TRUE; constant boolean add = (op == '0'); constant integer esize = 32 >> UInt(sz); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

A2

<!-- image -->

## Encoding for the Half-precision scalar variant

```
(FEAT_FP16) Applies when (size == 01) VMLS{<c>}{<q>}.F16 <Sd>, <Sn>, <Sm>
```

## Encoding for the Single-precision scalar variant

```
Applies when (size == 10) VMLS{<c>}{<q>}.F32 <Sd>, <Sn>,
```

```
<Sm>
```

## Encoding for the Double-precision scalar variant

```
Applies when (size == 11) VMLS{<c>}{<q>}.F64 <Dd>, <Dn>, <Dm>
```

## Decode for all variants of this encoding

```
if size == '00' || (size == '01' && !IsFeatureImplemented(FEAT_FP16)) then UNDEFINED; if size == '01' && cond != '1110' then UNPREDICTABLE; if FPSCR.Len != '000' || FPSCR.Stride != '00' then UNDEFINED; constant boolean advsimd = FALSE; constant boolean add = (op == '0'); constant integer esize = 8 << UInt(size); constant integer d = if size == '11' then UInt(D:Vd) else UInt(Vd:D); constant integer n = if size == '11' then UInt(N:Vn) else UInt(Vn:N); constant integer m = if size == '11' then UInt(M:Vm) else UInt(Vm:M); constant boolean floating_point = boolean UNKNOWN; constant integer regs = integer UNKNOWN; constant integer elements = integer UNKNOWN;
```

## CONSTRAINED UNPREDICTABLE behavior

If size == '01' &amp;&amp; cond != '1110' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VMLS{<c>}{<q>}.<dt> <Dd>, <Dn>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VMLS{<c>}{<q>}.<dt> <Qd>, <Qn>, <Qm>
```

## Decode for all variants of this encoding

```
if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then if sz == '1' && !IsFeatureImplemented(FEAT_FP16) then UNDEFINED; if sz == '1' && InITBlock() then UNPREDICTABLE; constant boolean advsimd = TRUE; constant boolean add = (op == '0'); constant integer esize = 32 >> UInt(sz); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

## CONSTRAINED UNPREDICTABLE behavior

If sz == '1' &amp;&amp; InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

## T2

<!-- image -->

## Encoding for the Half-precision scalar variant

```
(FEAT_FP16) Applies when (size == 01) VMLS{<c>}{<q>}.F16 <Sd>, <Sn>, <Sm>
```

## Encoding for the Single-precision scalar variant

```
Applies when (size == 10) VMLS{<c>}{<q>}.F32 <Sd>, <Sn>, <Sm>
```

## Encoding for the Double-precision scalar variant

```
Applies when (size == 11) VMLS{<c>}{<q>}.F64 <Dd>, <Dn>, <Dm>
```

## Decode for all variants of this encoding

```
if size == '00' || (size == '01' && !IsFeatureImplemented(FEAT_FP16)) then if size == '01' && InITBlock() then UNPREDICTABLE; if FPSCR.Len != '000' || FPSCR.Stride != '00' then UNDEFINED; constant boolean advsimd = FALSE; constant boolean add = (op == '0'); constant integer esize = 8 << UInt(size); constant integer d = if size == '11' then UInt(D:Vd) else UInt(Vd:D); constant integer n = if size == '11' then UInt(N:Vn) else UInt(Vn:N); constant integer m = if size == '11' then UInt(M:Vm) else UInt(Vm:M); constant boolean floating_point = boolean UNKNOWN; constant integer regs = integer UNKNOWN; constant integer elements = integer UNKNOWN;
```

```
UNDEFINED;
```

```
UNDEFINED;
```

## CONSTRAINED UNPREDICTABLE behavior

If size == '01' &amp;&amp; InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

## Assembler Symbols

&lt;c&gt;

For the 'A1 128-bit SIMD vector' and 'A1 64-bit SIMD vector' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'A2 Double-precision scalar', 'A2 Half-precision scalar', 'A2 Single-precision scalar', 'T1 128-bit SIMD vector', 'T1 64-bit SIMD vector', 'T2 Double-precision scalar', 'T2 Half-precision scalar', and 'T2 Single-precision scalar' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the data type for the elements of the vectors, encoded in 'sz':

|   sz | <dt>   |
|------|--------|
|    0 | F32    |
|    1 | F16    |

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

&lt;q&gt;

## &lt;dt&gt;

## &lt;Dd&gt;

## &lt;Dn&gt;

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field.

## &lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## &lt;Qd&gt;

## &lt;Qn&gt;

Is the 128-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field as &lt;Qn&gt;*2.

## &lt;Qm&gt;

Is the 128-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## &lt;Sd&gt;

## &lt;Sn&gt;

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

Is the 32-bit name of the SIMD&amp;FP destination register, encoded in the 'Vd:D' field.

Is the 32-bit name of the first SIMD&amp;FP source register, encoded in the 'Vn:N' field.

## &lt;Sm&gt;

Is the 32-bit name of the second SIMD&amp;FP source register, encoded in the 'Vm:M' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDOrVFPEnabled(TRUE, advsimd); if advsimd then // Advanced SIMD instruction constant FPCR_Type fpcr = StandardFPCR(); for r = 0 to regs-1 for e = 0 to elements-1 bits(esize) addend = FPMul(Elem[D[n+r],e,esize], Elem[D[m+r],e,esize], fpcr); if !add then addend = FPNeg(addend, fpcr); Elem[D[d+r],e,esize] = FPAdd(Elem[D[d+r],e,esize], addend, fpcr); else // VFP instruction constant FPCR_Type fpcr = EffectiveFPCR(); case esize of when 16 bits(16) addend16 = FPMul(H[n], H[m], fpcr); if !add then addend16 = FPNeg(addend16, fpcr); H[d] = FPAdd(H[d], addend16, fpcr); when 32 bits(32) addend32 = FPMul(S[n], S[m], fpcr); if !add then addend32 = FPNeg(addend32, fpcr); S[d] = FPAdd(S[d], addend32, fpcr); when 64 bits(64) addend64 = FPMul(D[n], D[m], fpcr); if !add then addend64 = FPNeg(addend64, fpcr); D[d] = FPAdd(D[d], addend64, fpcr);
```