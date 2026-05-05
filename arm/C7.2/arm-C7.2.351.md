## C7.2.351 SQSUB

Signed saturating subtract

This instruction subtracts the element values of the second source SIMD&amp;FP register from the corresponding element values of the first source SIMD&amp;FP register, places the results into a vector, and writes the vector to the destination SIMD&amp;FP register.

If overflow occurs with any of the results, those results are saturated. If saturation occurs, the cumulative saturation bit FPSR.QC is set.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 2 classes: Scalar and Vector

## Scalar

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
SQSUB <V><d>, <V><n>, <V><m>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer esize = 8 << UInt(size); constant integer datasize = esize; constant integer elements = 1; constant boolean unsigned = FALSE;
```

## Vector

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
SQSUB <Vd>.<T>, <Vn>.<T>, <Vm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if size:Q == '110' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer esize = 8 << UInt(size); constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize; constant boolean unsigned = FALSE;
```

## Assembler Symbols

&lt;V&gt;

Is a width specifier, encoded in 'size':

&lt;d&gt;

&lt;n&gt;

&lt;m&gt;

&lt;Vd&gt;

&lt;T&gt;

|   size | <V>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

Is the number of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the number of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

Is the number of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'size:Q':

|   size |   Q | <T>   |
|--------|-----|-------|
|     00 |   0 | 8B    |
|     00 |   1 | 16B   |
|     01 |   0 | 4H    |
|     01 |   1 | 8H    |
|     10 |   0 | 2S    |
|     10 |   1 | 4S    |

&lt;Vn&gt;

|   size |   Q | <T>      |
|--------|-----|----------|
|     11 |   0 | RESERVED |
|     11 |   1 | 2D       |

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

&lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand1 = V[n, datasize]; constant bits(datasize) operand2 = V[m, datasize]; bits(datasize) result; integer element1; integer element2; integer diff; boolean sat; for e = 0 to elements-1 element1 = SInt(Elem[operand1, e, esize]); element2 = SInt(Elem[operand2, e, esize]); diff = element1 -element2; (Elem[result, e, esize], sat) = SatQ(diff, esize, unsigned); if sat then FPSR.QC = '1'; V[d, datasize] = result;
```
