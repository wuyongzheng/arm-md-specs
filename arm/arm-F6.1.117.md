## F6.1.117 VMAXNM

Floating-point Maximum Number

This instruction determines the floating-point maximum number.

It handles NaNs in consistence with the IEEE754-2008 specification. It returns the numerical operand when one operand is numerical and the other is a quiet NaN, but otherwise the result is identical to floating-point VMAX .

This instruction is not conditional.

It has encodings from the following instruction sets: A32 (A1 and A2) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VMAXNM{<q>}.<dt> <Dd>, <Dn>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

Applies when

```
(Q == 1) VMAXNM{<q>}.<dt> <Qd>, <Qn>, <Qm>
```

## Decode for all variants of this encoding

```
if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then if sz == '1' && !IsFeatureImplemented(FEAT_FP16) then UNDEFINED; constant boolean maximum = (op == '0'); constant boolean advsimd = TRUE; constant integer esize = 32 >> UInt(sz); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

A2

<!-- image -->

## Encoding for the Half-precision scalar variant

```
(FEAT_FP16) Applies when (size == 01) VMAXNM{<q>}.F16 <Sd>, <Sn>, <Sm> // (Cannot be
```

```
conditional)
```

```
UNDEFINED;
```

## Encoding for the Single-precision scalar variant

Applies when (size ==

```
VMAXNM{<q>}.F32 <Sd>, <Sn>, <Sm> // (Cannot be
```

```
10) conditional)
```

## Encoding for the Double-precision scalar variant

```
Applies when (size == 11) VMAXNM{<q>}.F64 <Dd>, <Dn>, <Dm> // (Cannot be conditional)
```

## Decode for all variants of this encoding

```
if size == '00' || (size == '01' && !IsFeatureImplemented(FEAT_FP16)) then constant boolean advsimd = FALSE; constant boolean maximum = (op == '0'); constant integer esize = 8 << UInt(size); constant integer d = if size == '11' then UInt(D:Vd) else UInt(Vd:D); constant integer n = if size == '11' then UInt(N:Vn) else UInt(Vn:N); constant integer m = if size == '11' then UInt(M:Vm) else UInt(Vm:M); constant integer regs = integer UNKNOWN; constant integer elements = integer UNKNOWN;
```

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VMAXNM{<q>}.<dt> <Dd>, <Dn>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VMAXNM{<q>}.<dt>
```

```
<Qd>, <Qn>, <Qm>
```

## Decode for all variants of this encoding

```
if InITBlock() then UNPREDICTABLE; if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then if sz == '1' && !IsFeatureImplemented(FEAT_FP16) then UNDEFINED; constant boolean maximum = (op == '0'); constant boolean advsimd = TRUE; constant integer esize = 32 >> UInt(sz); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

```
UNDEFINED;
```

```
UNDEFINED;
```

## CONSTRAINED UNPREDICTABLE behavior

If InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

T2

<!-- image -->

## Encoding for the Half-precision scalar variant

```
(FEAT_FP16) Applies when (size == 01)
```

```
VMAXNM{<q>}.F16 <Sd>, <Sn>, <Sm> // (Not permitted in IT
```

```
block)
```

## Encoding for the Single-precision scalar variant

```
Applies when (size == 10) VMAXNM{<q>}.F32 <Sd>, <Sn>, <Sm> // (Not permitted in IT block)
```

## Encoding for the Double-precision scalar variant

Applies when (size ==

```
11)
```

```
VMAXNM{<q>}.F64 <Dd>, <Dn>, <Dm> // (Not permitted in IT
```

## Decode for all variants of this encoding

```
if InITBlock() then UNPREDICTABLE; if size == '00' || (size == '01' && !IsFeatureImplemented(FEAT_FP16)) then UNDEFINED; constant boolean advsimd = FALSE; constant boolean maximum = (op == '0'); constant integer esize = 8 << UInt(size); constant integer d = if size == '11' then UInt(D:Vd) else UInt(Vd:D); constant integer n = if size == '11' then UInt(N:Vn) else UInt(Vn:N); constant integer m = if size == '11' then UInt(M:Vm) else UInt(Vm:M); constant integer regs = integer UNKNOWN; constant integer elements = integer UNKNOWN;
```

## CONSTRAINED UNPREDICTABLE behavior

If InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

```
block)
```

## Assembler Symbols

## &lt;q&gt;

See Standard assembler syntax fields.

Is the data type for the elements of the vectors, encoded in 'sz':

|   sz | <dt>   |
|------|--------|
|    0 | F32    |
|    1 | F16    |

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;dt&gt;

## &lt;Dd&gt;

## &lt;Dn&gt;

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field.

## &lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field.

- &lt;Qd&gt;
- &lt;Qn&gt;

Is the 128-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field as &lt;Qn&gt;*2.

- &lt;Qm&gt;

Is the 128-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

- &lt;Sd&gt;

## &lt;Sn&gt;

Is the 32-bit name of the first SIMD&amp;FP source register, encoded in the 'Vn:N' field.

## &lt;Sm&gt;

Is the 32-bit name of the second SIMD&amp;FP source register, encoded in the 'Vm:M' field.

## Operation

```
EncodingSpecificOperations(); CheckAdvSIMDOrVFPEnabled(TRUE, advsimd); if advsimd then // Advanced SIMD instruction constant FPCR_Type fpcr = StandardFPCR(); for r = 0 to regs-1 for e = 0 to elements-1 constant bits(esize) operand1 = Elem[D[n+r], e, esize]; constant bits(esize) operand2 = Elem[D[m+r], e, esize]; if maximum then Elem[D[d+r], e, esize] = FPMaxNum(operand1, operand2, fpcr);
```

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

Is the 32-bit name of the SIMD&amp;FP destination register, encoded in the 'Vd:D' field.

```
else Elem[D[d+r], e, esize] = FPMinNum(operand1, operand2, fpcr); else // VFP instruction constant FPCR_Type fpcr = EffectiveFPCR(); case esize of when 16 if maximum then H[d] = FPMaxNum(H[n], H[m], fpcr); else H[d] = FPMinNum(H[n], H[m], fpcr); when 32 if maximum then S[d] = FPMaxNum(S[n], S[m], fpcr); else S[d] = FPMinNum(S[n], S[m], fpcr); when 64 if maximum then D[d] = FPMaxNum(D[n], D[m], fpcr); else D[d] = FPMinNum(D[n], D[m], fpcr);
```