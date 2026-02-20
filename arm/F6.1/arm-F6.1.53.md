## F6.1.53 VCMLA (by element)

Vector Complex Multiply Accumulate (by element).

This instruction operates on complex numbers that are represented in SIMD&amp;FP registers as pairs of elements, with the more significant element holding the imaginary part of the number and the less significant element holding the real part of the number. Each element holds a floating-point value. It performs the following computation on complex numbers from the first source register and the destination register with the specified complex number from the second source register:

- Considering the complex number from the second source register on an Argand diagram, the number is rotated counterclockwise by 0, 90, 180, or 270 degrees.
- The two elements of the transformed complex number are multiplied by:
- The real element of the complex number from the first source register, if the transformation was a rotation by 0 or 180 degrees.
- The imaginary element of the complex number from the first source register, if the transformation was a rotation by 90 or 270 degrees.
- The complex number resulting from that multiplication is added to the complex number from the destination register.

The multiplication and addition operations are performed as a fused multiply-add, without any intermediate rounding.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

(FEAT\_FCMA)

<!-- image -->

Encoding for the 64-bit SIMD vector of half-precision floating-point variant

```
Applies when (S == 0 && Q == 0) VCMLA{<q>}.F16 <Dd>, <Dn>, <Dm>[<index>], #<rotate>
```

Encoding for the 64-bit SIMD vector of single-precision floating-point variant

```
Applies when (S == 1 && Q == 0) VCMLA{<q>}.F32 <Dd>, <Dn>, <Dm>[0], #<rotate>
```

Encoding for the 128-bit SIMD vector of half-precision floating-point variant

```
Applies when (S == 0 && Q == 1) VCMLA{<q>}.F16 <Qd>, <Qn>, <Dm>[<index>], #<rotate>
```

Encoding for the 128-bit SIMD vector of single-precision floating-point variant

```
Applies when (S == 1 && Q == 1) VCMLA{<q>}.F32 <Qd>, <Qn>, <Dm>[0], #<rotate>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_FCMA) then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vn<0> == '1') then UNDEFINED; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = if S == '1' then UInt(M:Vm) else UInt(Vm); constant integer index = if S == '1' then 0 else UInt(M); constant integer esize = 16 << UInt(S); if !IsFeatureImplemented(FEAT_FP16) && esize == 16 then constant integer elements = 64 DIV esize; constant integer regs = if Q == '0' then 1 else 2;
```

```
UNDEFINED;
```

<!-- image -->

```
T1 (FEAT_FCMA) 1 1 1 1 0 8 S 7 D 6 rot 5 4 Vn 3 0 Vd 15 12 1 0 0 0 11 8 N 7 Q 6 M 5 0 4 Vm 3 0 U Encoding for the 64-bit SIMD vector of half-precision floating-point variant Applies when (S == 0 && Q == 0) VCMLA{<q>}.F16 <Dd>, <Dn>, <Dm>[<index>], #<rotate> Encoding for the 64-bit SIMD vector of single-precision floating-point variant Applies when (S == 1 && Q == 0) VCMLA{<q>}.F32 <Dd>, <Dn>, <Dm>[0], #<rotate> Encoding for the 128-bit SIMD vector of half-precision floating-point variant Applies when (S == 0 && Q == 1) VCMLA{<q>}.F16 <Qd>, <Qn>, <Dm>[<index>], #<rotate> Encoding for the 128-bit SIMD vector of single-precision floating-point variant Applies when (S == 1 && Q == 1) VCMLA{<q>}.F32 <Qd>, <Qn>, <Dm>[0], #<rotate> Decode for all variants of this encoding
```

```
UNDEFINED;
```

```
if InITBlock() then UNPREDICTABLE; if !IsFeatureImplemented(FEAT_FCMA) then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vn<0> == '1') then UNDEFINED; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = if S == '1' then UInt(M:Vm) else UInt(Vm); constant integer index = if S == '1' then 0 else UInt(M); constant integer esize = 16 << UInt(S); if !IsFeatureImplemented(FEAT_FP16) && esize == 16 then constant integer elements = 64 DIV esize; constant integer regs = if Q == '0' then 1 else 2;
```

## Assembler Symbols

## &lt;q&gt;

See Standard assembler syntax fields.

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;Dd&gt;

## &lt;Dn&gt;

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field.

## &lt;Dm&gt;

For the 'A1 128-bit SIMD vector of half-precision floating-point', 'A1 64-bit SIMD vector of half-precision floating-point', 'T1 128-bit SIMD vector of half-precision floating-point', and 'T1 64-bit SIMD vector of half-precision floating-point' variants: is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'Vm' field.

For the 'A1 128-bit SIMD vector of single-precision floating-point', 'A1 64-bit SIMD vector of single-precision floating-point', 'T1 128-bit SIMD vector of single-precision floating-point', and 'T1 64-bit SIMD vector of single-precision floating-point' variants: is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## &lt;index&gt;

Is the element index in the range 0 to 1, encoded in the 'M' field.

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

## Operation

```
EncodingSpecificOperations(); CheckAdvSIMDEnabled(); constant FPCR_Type fpcr = StandardFPCR(); for r = 0 to regs-1 constant bits(64) operand1 = D[n+r]; constant bits(64) operand2 = Din[m]; constant bits(64) operand3 = D[d+r]; for e = 0 to (elements DIV 2)-1 bits(esize) element1; bits(esize) element2; bits(esize) element3;
```

```
bits(esize) element4; case rot of when '00' element1 = Elem[operand2,index*2,esize]; element2 = Elem[operand1,e*2,esize]; element3 = Elem[operand2,index*2+1,esize]; element4 = Elem[operand1,e*2,esize]; when '01' element1 = FPNeg(Elem[operand2,index*2+1,esize], fpcr); element2 = Elem[operand1,e*2+1,esize]; element3 = Elem[operand2,index*2,esize]; element4 = Elem[operand1,e*2+1,esize]; when '10' element1 = FPNeg(Elem[operand2,index*2,esize], fpcr); element2 = Elem[operand1,e*2,esize]; element3 = FPNeg(Elem[operand2,index*2+1,esize], fpcr); element4 = Elem[operand1,e*2,esize]; when '11' element1 = Elem[operand2,index*2+1,esize]; element2 = Elem[operand1,e*2+1,esize]; element3 = FPNeg(Elem[operand2,index*2,esize], fpcr); element4 = Elem[operand1,e*2+1,esize]; constant bits(esize) result1 = FPMulAdd(Elem[operand3,e*2,esize],element2,element1, fpcr); constant bits(esize) result2 = FPMulAdd(Elem[operand3,e*2+1,esize],element4,element3,fpcr); Elem[D[d+r],e*2,esize] = result1; Elem[D[d+r],e*2+1,esize] = result2;
```