## C7.2.356 SRSHL

Signed rounding shift left (register)

This instruction takes each signed integer value in the vector of the first source SIMD&amp;FP register, shifts it by a value from the least significant byte of the corresponding element of the second source SIMD&amp;FP register, places the results in a vector, and writes the vector to the destination SIMD&amp;FP register.

If the shift value is positive, the operation is a left shift. If the shift value is negative, it is a rounding right shift. For a truncating shift, see SSHL.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 2 classes: Scalar and Vector

## Scalar

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
SRSHL D<d>, D<n>, D<m>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if S == '0' && size != '11' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean rounding = TRUE; constant integer esize = 8 << UInt(size); constant integer datasize = esize; constant integer elements = 1;
```

## Vector

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
SRSHL <Vd>.<T>, <Vn>.<T>, <Vm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF);
```

```
if size:Q == '110' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean rounding = TRUE; constant integer esize = 8 << UInt(size); constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize;
```

## Assembler Symbols

&lt;d&gt;

Is the number of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the number of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

Is the number of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'size:Q':

|   size |   Q | <T>      |
|--------|-----|----------|
|     00 |   0 | 8B       |
|     00 |   1 | 16B      |
|     01 |   0 | 4H       |
|     01 |   1 | 8H       |
|     10 |   0 | 2S       |
|     10 |   1 | 4S       |
|     11 |   0 | RESERVED |
|     11 |   1 | 2D       |

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

&lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

&lt;n&gt;

&lt;m&gt;

&lt;Vd&gt;

&lt;T&gt;

&lt;Vn&gt;

## Operation

```
ShiftSat(SInt(Elem[operand2, e, esize]<7:0>), esize);
```

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand1 = V[n, datasize]; constant bits(datasize) operand2 = V[m, datasize]; bits(datasize) result; for e = 0 to elements-1 integer element = SInt(Elem[operand1, e, esize]); integer shift = if shift >= 0 then // left shift element = element << shift; else // right shift shift = -shift; element = RShr(element, shift, rounding); Elem[result, e, esize] = element<esize-1:0>; V[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
