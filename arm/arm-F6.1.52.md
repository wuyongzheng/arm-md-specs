## F6.1.52 VCMLA

Vector Complex Multiply Accumulate.

This instruction operates on complex numbers that are represented in SIMD&amp;FP registers as pairs of elements, with the more significant element holding the imaginary part of the number and the less significant element holding the real part of the number. Each element holds a floating-point value. It performs the following computation on the corresponding complex number element pairs from the two source registers and the destination register:

- Considering the complex number from the second source register on an Argand diagram, the number is rotated counterclockwise by 0, 90, 180, or 270 degrees.
- The two elements of the transformed complex number are multiplied by:
- The real element of the complex number from the first source register, if the transformation was a rotation by 0 or 180 degrees.
- The imaginary element of the complex number from the first source register, if the transformation was a rotation by 90 or 270 degrees.
- The complex number resulting from that multiplication is added to the complex number from the destination register.

The multiplication and addition operations are performed as a fused multiply-add, without any intermediate rounding.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

## A1

(FEAT\_FCMA)

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VCMLA{<q>}.<dt> <Dd>, <Dn>,
```

```
<Dm>, #<rotate>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VCMLA{<q>}.<dt> <Qd>, <Qn>, <Qm>, #<rotate>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_FCMA) then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then UNDEFINED; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer esize = 16 << UInt(S); if !IsFeatureImplemented(FEAT_FP16) && esize == 16 then UNDEFINED; constant integer elements = 64 DIV esize; constant integer regs = if Q == '0' then 1 else 2;
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
VCMLA{<q>}.<dt> <Dd>, <Dn>,
```

```
<Dm>, #<rotate>
```

## Encoding for the 128-bit SIMD vector variant

Applies when

```
VCMLA{<q>}.<dt> <Qd>, <Qn>,
```

```
(Q == 1) <Qm>, #<rotate>
```

## Decode for all variants of this encoding

```
if InITBlock() then UNPREDICTABLE; if !IsFeatureImplemented(FEAT_FCMA) then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then UNDEFINED; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer esize = 16 << UInt(S); if !IsFeatureImplemented(FEAT_FP16) && esize == 16 then UNDEFINED; constant integer elements = 64 DIV esize; constant integer regs = if Q == '0' then 1 else 2;
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
|    00 |          0 |
|    01 |         90 |
|    10 |        180 |
|    11 |        270 |

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

## &lt;Qd&gt;

## &lt;Qn&gt;

Is the 128-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field as &lt;Qn&gt;*2.

## &lt;Qm&gt;

Is the 128-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

```
EncodingSpecificOperations(); CheckAdvSIMDEnabled(); constant FPCR_Type fpcr = StandardFPCR(); for r = 0 to regs-1 constant bits(64) operand1 = D[n+r]; constant bits(64) operand2 = D[m+r]; constant bits(64) operand3 = D[d+r]; for e = 0 to (elements DIV 2)-1 bits(esize) element1; bits(esize) element2; bits(esize) element3; bits(esize) element4; case rot of when '00' element1 = Elem[operand2,e*2,esize]; element2 = Elem[operand1,e*2,esize]; element3 = Elem[operand2,e*2+1,esize]; element4 = Elem[operand1,e*2,esize]; when '01' element1 = FPNeg(Elem[operand2,e*2+1,esize], fpcr); element2 = Elem[operand1,e*2+1,esize]; element3 = Elem[operand2,e*2,esize]; element4 = Elem[operand1,e*2+1,esize]; when '10' element1 = FPNeg(Elem[operand2,e*2,esize], fpcr); element2 = Elem[operand1,e*2,esize]; element3 = FPNeg(Elem[operand2,e*2+1,esize], fpcr); element4 = Elem[operand1,e*2,esize]; when '11' element1 = Elem[operand2,e*2+1,esize]; element2 = Elem[operand1,e*2+1,esize]; element3 = FPNeg(Elem[operand2,e*2,esize], fpcr);
```

```
element4 = Elem[operand1,e*2+1,esize]; constant bits(esize) result1 = FPMulAdd(Elem[operand3,e*2,esize],element2,element1, fpcr); constant bits(esize) result2 = FPMulAdd(Elem[operand3,e*2+1,esize],element4,element3, fpcr); Elem[D[d+r],e*2,esize] = result1; Elem[D[d+r],e*2+1,esize] = result2;
```