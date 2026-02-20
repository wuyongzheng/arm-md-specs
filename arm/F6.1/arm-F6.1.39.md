## F6.1.39 VCADD

Vector Complex Add.

This instruction operates on complex numbers that are represented in SIMD&amp;FP registers as pairs of elements, with the more significant element holding the imaginary part of the number and the less significant element holding the real part of the number. Each element holds a floating-point value. It performs the following computation on the corresponding complex number element pairs from the two source registers:

- Considering the complex number from the second source register on an Argand diagram, the number is rotated counterclockwise by 90 or 270 degrees.
- The rotated complex number is added to the complex number from the first source register.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

## A1

(FEAT\_FCMA)

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VCADD{<q>}.<dt> <Dd>, <Dn>, <Dm>, #<rotate>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VCADD{<q>}.<dt> <Qd>, <Qn>,
```

```
<Qm>, #<rotate>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_FCMA) then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then UNDEFINED; if S == '0' && !IsFeatureImplemented(FEAT_FP16) then UNDEFINED; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer esize = 16 << UInt(S); constant integer elements = 64 DIV esize; constant integer regs = if Q == '0' then 1 else 2;
```

T1

(FEAT\_FCMA)

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when

```
(Q == 0)
```

```
VCADD{<q>}.<dt> <Dd>, <Dn>, <Dm>, #<rotate>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when
```

```
VCADD{<q>}.<dt> <Qd>, <Qn>,
```

```
(Q == 1) <Qm>, #<rotate>
```

## Decode for all variants of this encoding

```
if InITBlock() then UNPREDICTABLE; if !IsFeatureImplemented(FEAT_FCMA) then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then UNDEFINED; if S == '0' && !IsFeatureImplemented(FEAT_FP16) then UNDEFINED; constant integer esize = 16 << UInt(S); constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer elements = 64 DIV esize; constant integer regs = if Q == '0' then 1 else 2;
```

## Assembler Symbols

&lt;q&gt;

See Standard assembler syntax fields.

Is the data type for the elements of the vectors, encoded in 'S':

|   S | <dt>   |
|-----|--------|
|   0 | F16    |
|   1 | F32    |

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field.

&lt;dt&gt;

&lt;Dd&gt;

&lt;Dn&gt;

## &lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## &lt;rotate&gt;

Is the rotation to be applied to elements in the second SIMD&amp;FP source register, encoded in 'rot':

|   rot |   <rotate> |
|-------|------------|
|     0 |         90 |
|     1 |        270 |

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

## &lt;Qd&gt;

## &lt;Qn&gt;

Is the 128-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field as &lt;Qn&gt;*2.

## &lt;Qm&gt;

Is the 128-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

```
EncodingSpecificOperations(); CheckAdvSIMDEnabled(); for r = 0 to regs-1 constant bits(64) operand1 = D[n+r]; constant bits(64) operand2 = D[m+r]; constant FPCR_Type fpcr = StandardFPCR(); for e = 0 to (elements DIV 2)-1 bits(esize) element1; bits(esize) element3; case rot of when '0' element1 = FPNeg(Elem[operand2,e*2+1,esize], fpcr); element3 = Elem[operand2,e*2,esize]; when '1' element1 = Elem[operand2,e*2+1,esize]; element3 = FPNeg(Elem[operand2,e*2,esize], fpcr); constant bits(esize) result1 = FPAdd(Elem[operand1,e*2,esize],element1,fpcr); constant bits(esize) result2 = FPAdd(Elem[operand1,e*2+1,esize],element3,fpcr); Elem[D[d+r],e*2,esize] = result1; Elem[D[d+r],e*2+1,esize] = result2;
```