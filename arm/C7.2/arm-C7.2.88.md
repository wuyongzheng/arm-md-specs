## C7.2.88 FCVTN (half-precision to 8-bit floating-point)

Half-precision convert to 8-bit floating-point (vector)

This instruction converts half-precision elements of the two source vectors to 8-bit floating-point while scaling the values by 2 SInt(FPMR.NSCALE[4:0]) , and places the in-order results in the 8-bit elements of the destination vector.

The 8-bit floating-point encoding format is selected by FPMR.F8D.

## Advanced SIMD

(FEAT\_FP8)

<!-- image -->

## Encoding

```
FCVTN <Vd>.<Ta>, <Vn>.<Tb>, <Vm>.<Tb>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_FP8) then EndOfDecode(Decode_UNDEF);
```

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer datasize = if Q == '1' then 128 else 64; constant integer elements = datasize DIV 16;
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'Q':

&lt;Ta&gt;

## &lt;Vn&gt;

&lt;Tb&gt;

|   Q | <Ta>   |
|-----|--------|
|   0 | 8B     |
|   1 | 16B    |

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

Is an arrangement specifier, encoded in 'Q':

&lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
CheckFPMREnabled(); AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand1 = V[n, datasize]; constant bits(datasize) operand2 = V[m, datasize]; bits(datasize) result; for e = 0 to elements-1 Elem[result, 0*elements + e, 8] = FPConvertFP8(Elem[operand1, e, 16], FPCR, FPMR, 8); Elem[result, 1*elements + e, 8] = FPConvertFP8(Elem[operand2, e, 16], FPCR, FPMR, 8); V[d, datasize] = result;
```

|   Q | <Tb>   |
|-----|--------|
|   0 | 4H     |
|   1 | 8H     |
