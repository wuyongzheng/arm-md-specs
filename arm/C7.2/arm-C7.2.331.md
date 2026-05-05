## C7.2.331 SQDMLSL, SQDMLSL2 (vector)

Signed saturating doubling multiply-subtract long

This instruction multiplies corresponding signed integer values in the lower or upper half of the vectors of the two source SIMD&amp;FP registers, doubles the results, and subtracts the final results from the vector elements of the destination SIMD&amp;FP register. The destination vector elements are twice as long as the elements that are multiplied.

If overflow occurs with any of the results, those results are saturated. If saturation occurs, the cumulative saturation bit FPSR.QC is set.

The SQDMLSL instruction extracts each source vector from the lower half of each source register. The SQDMLSL2 instruction extracts each source vector from the upper half of each source register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 2 classes: Scalar and Vector

## Scalar

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
SQDMLSL <Va><d>, <Vb><n>, <Vb><m>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if size == '00' || size == '11' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer esize = 8 << UInt(size); constant integer datasize = esize; constant integer elements = 1; constant integer part = 0;
```

## Vector

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

SQDMLSL{2}

&lt;Vd&gt;.&lt;Ta&gt;, &lt;Vn&gt;.&lt;Tb&gt;, &lt;Vm&gt;.&lt;Tb&gt;

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if size == '00' || size == '11' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer esize = 8 << UInt(size); constant integer datasize = 64; constant integer part = UInt(Q); constant integer elements = datasize DIV esize;
```

## Assembler Symbols

&lt;Va&gt;

Is the destination width specifier, encoded in 'size':

&lt;d&gt;

&lt;Vb&gt;

&lt;n&gt;

&lt;m&gt;

2

|   size | <Va>     |
|--------|----------|
|     00 | RESERVED |
|     01 | S        |
|     10 | D        |
|     11 | RESERVED |

Is the number of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the source width specifier, encoded in 'size':

|   size | <Vb>     |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | RESERVED |

Is the number of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

Is the number of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

Is the second and upper half specifier. If present it causes the operation to be performed on the upper 64 bits of the registers holding the narrower elements, and is encoded in 'Q':

&lt;Vd&gt;

&lt;Ta&gt;

## &lt;Vn&gt;

&lt;Tb&gt;

|   Q | 2         |
|-----|-----------|
|   0 | [absent]  |
|   1 | [present] |

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'size':

|   size | <Ta>     |
|--------|----------|
|     00 | RESERVED |
|     01 | 4S       |
|     10 | 2D       |
|     11 | RESERVED |

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

Is an arrangement specifier, encoded in 'size:Q':

|   size | Q   | <Tb>     |
|--------|-----|----------|
|     00 | x   | RESERVED |
|     01 | 0   | 4H       |
|     01 | 1   | 8H       |
|     10 | 0   | 2S       |
|     10 | 1   | 4S       |
|     11 | x   | RESERVED |

## &lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand1 = constant bits(datasize) operand2 = constant bits(2*datasize) operand3 = V[d, 2*datasize]; bits(2*datasize) result; integer element1; integer element2; bits(2*esize) product; integer accum; boolean sat1;
```

```
Vpart[n, part, datasize]; Vpart[m, part, datasize];
```

```
boolean sat2; for e = 0 to elements-1 element1 = SInt(Elem[operand1, e, esize]); element2 = SInt(Elem[operand2, e, esize]); (product, sat1) = SignedSatQ(2 * element1 * element2, 2 * esize); accum = SInt(Elem[operand3, e, 2*esize]) SInt(product); (Elem[result, e, 2*esize], sat2) = SignedSatQ(accum, 2 * esize); if sat1 || sat2 then FPSR.QC = '1'; V[d, 2*datasize] = result;
```
