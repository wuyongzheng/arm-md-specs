## C7.2.66 FCMLA (by element)

Floating-point complex multiply accumulate (by element)

This instruction operates on complex numbers that are represented in SIMD&amp;FP registers as pairs of elements, with the more significant element holding the imaginary part of the number and the less significant element holding the real part of the number. Each element holds a floating-point value. It performs the following computation on complex numbers from the first source register and the destination register with the specified complex number from the second source register:

- Considering the complex number from the second source register on an Argand diagram, the number is rotated counterclockwise by 0, 90, 180, or 270 degrees.
- The two elements of the transformed complex number are multiplied by:
- The real element of the complex number from the first source register, if the transformation was a rotation by 0 or 180 degrees.
- The imaginary element of the complex number from the first source register, if the transformation was a rotation by 90 or 270 degrees.
- The complex number resulting from that multiplication is added to the complex number from the destination register.

The multiplication and addition operations are performed as a fused multiply-add, without any intermediate rounding.

This instruction can generate a floating-point exception. Depending on the settings in FPCR, the exception results in either a flag being set in FPSR or a synchronous exception being generated. For more information, see Floating-point exceptions and exception traps.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Vector

(FEAT\_FCMA)

<!-- image -->

## Encoding

```
FCMLA <Vd>.<T>, <Vn>.<T>, <Vm>.<Ts>[<index>], #<rotate>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_FCMA) then EndOfDecode(Decode_UNDEF); if size == '00' || size == '11' then EndOfDecode(Decode_UNDEF); if !IsFeatureImplemented(FEAT_FP16) && size == '01' then EndOfDecode(Decode_UNDEF); if size == '10' && (L == '1' || Q == '0') then EndOfDecode(Decode_UNDEF); if size == '01' && H == '1' && Q == '0' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(M:Rm); integer index; if size == '01' then index = UInt(H:L); if size == '10' then index = UInt(H); constant integer esize = 8 << UInt(size); constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize;
```

## Assembler Symbols

## &lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'size:Q':

|   size | Q   | <T>      |
|--------|-----|----------|
|     00 | x   | RESERVED |
|     01 | 0   | 4H       |
|     01 | 1   | 8H       |
|     10 | 0   | RESERVED |
|     10 | 1   | 4S       |
|     11 | x   | RESERVED |

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'M:Rm' fields.

## &lt;Ts&gt;

&lt;T&gt;

## &lt;Vn&gt;

Is an element size specifier, encoded in 'size':

## &lt;index&gt;

Is the element index, encoded in 'size:H:L':

|   size | <Ts>     |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | RESERVED |

|   size | <index>   |
|--------|-----------|
|     00 | RESERVED  |
|     01 | UInt(H:L) |
|     10 | UInt(H)   |
|     11 | RESERVED  |

## &lt;rotate&gt;

Is the rotation, encoded in 'rot':

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand1 = V[n, datasize]; constant bits(datasize) operand2 = V[m, datasize]; constant bits(datasize) operand3 = V[d, datasize]; bits(datasize) result; for e = 0 to (elements DIV 2)-1 bits(esize) element1; bits(esize) element2; bits(esize) element3; bits(esize) element4; case rot of when '00' element1 = Elem[operand2, index*2, esize]; element2 = Elem[operand1, e*2, esize]; element3 = Elem[operand2, index*2+1, esize]; element4 = Elem[operand1, e*2, esize]; when '01' element1 = FPNeg(Elem[operand2, index*2+1, esize], FPCR); element2 = Elem[operand1, e*2+1, esize]; element3 = Elem[operand2, index*2, esize]; element4 = Elem[operand1, e*2+1, esize]; when '10' element1 = FPNeg(Elem[operand2, index*2, esize], FPCR); element2 = Elem[operand1, e*2, esize]; element3 = FPNeg(Elem[operand2, index*2+1, esize], FPCR); element4 = Elem[operand1, e*2, esize]; when '11' element1 = Elem[operand2, index*2+1, esize]; element2 = Elem[operand1, e*2+1, esize]; element3 = FPNeg(Elem[operand2, index*2, esize], FPCR); element4 = Elem[operand1, e*2+1, esize]; Elem[result, e*2, esize] = FPMulAdd(Elem[operand3, e*2, esize], element2, element1, FPCR); Elem[result, e*2+1, esize] = FPMulAdd(Elem[operand3, e*2+1, esize], element4, element3, FPCR); V[d, datasize] = result;
```

|   rot |   <rotate> |
|-------|------------|
|    00 |          0 |
|    01 |         90 |
|    10 |        180 |
|    11 |        270 |
