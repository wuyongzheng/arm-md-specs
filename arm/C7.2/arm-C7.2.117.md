## C7.2.117 FDOT (8-bit floating-point to single-precision, by element)

8-bit floating-point dot product to single-precision (vector, by element)

This instruction computes the fused sum-of-products of a group of four 8-bit floating-point values held in each 32-bit element of the first source vector and a group of four 8-bit floating-point values in an indexed 32-bit element of the second source vector. The single-precision sum-of-products are scaled by 2 -UInt(FPMR.LSCALE) , before being destructively added without intermediate rounding to the corresponding single-precision elements of the destination vector.

The 8-bit floating-point groups within the second source vector are specified using an immediate index.

The 8-bit floating-point encoding format for the elements of the first source vector is selected by FPMR.F8S1. The 8-bit floating-point encoding format for the elements of the second source vector is selected by FPMR.F8S2.

## Advanced SIMD

(FEAT\_FP8DOT4)

<!-- image -->

## Encoding

```
FDOT <Vd>.<Ta>, <Vn>.<Tb>, <Vm>.4B[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_FP8DOT4) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Rn); constant integer d = UInt(Rd); constant integer m = UInt(M:Rm); constant integer i = UInt(H:L); constant integer datasize = if Q == '1' then 128 else constant integer esize = 32; constant integer elements = datasize DIV esize;
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'Q':

<!-- image -->

&lt;Vn&gt;

```
64;
```

|   Q | <Ta>   |
|-----|--------|
|   0 | 2S     |
|   1 | 4S     |

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Tb&gt;

Is an arrangement specifier, encoded in 'Q':

## &lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'M:Rm' fields.

## &lt;index&gt;

Is the immediate index of a 32-bit group of four 8-bit values, in the range 0 to 3, encoded in the 'H:L' fields.

## Operation

```
CheckFPMREnabled(); AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand1 = V[n, datasize]; constant bits(128) operand2 = V[m, 128]; constant bits(datasize) operand3 = V[d, datasize]; bits(datasize) result; for e = 0 to elements-1 constant bits(esize) op1 = Elem[operand1, e, esize]; constant bits(esize) op2 = Elem[operand2, i, esize]; constant bits(esize) sum = Elem[operand3, e, esize]; Elem[result, e, esize] = FP8DotAddFP(sum, op1, op2, FPCR, FPMR); V[d, datasize] = result;
```

|   Q | <Tb>   |
|-----|--------|
|   0 | 8B     |
|   1 | 16B    |
