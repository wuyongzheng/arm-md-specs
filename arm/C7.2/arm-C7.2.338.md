## C7.2.338 SQRDMLAH (vector)

Signed saturating rounding doubling multiply accumulate returning high half (vector)

This instruction multiplies the vector elements of the first source SIMD&amp;FP register with the corresponding vector elements of the second source SIMD&amp;FP register without saturating the multiply results, doubles the results, and accumulates the most significant half of the final results with the vector elements of the destination SIMD&amp;FP register. The results are rounded.

If any of the results overflow, they are saturated. The cumulative saturation bit, FPSR.QC, is set if saturation occurs.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 2 classes: Scalar and Vector

## Scalar

(FEAT\_RDM)

<!-- image -->

## Encoding

```
SQRDMLAH <V><d>, <V><n>, <V><m>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_RDM) then EndOfDecode(Decode_UNDEF); if size == '11' || size == '00' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer esize = 8 << UInt(size); constant integer datasize = esize; constant integer elements = 1; constant boolean rounding = TRUE;
```

## Vector

(FEAT\_RDM)

<!-- image -->

## Encoding

```
SQRDMLAH <Vd>.<T>, <Vn>.<T>, <Vm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_RDM) then EndOfDecode(Decode_UNDEF); if size == '11' || size == '00' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer esize = 8 << UInt(size); constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize; constant boolean rounding = TRUE;
```

## Assembler Symbols

&lt;V&gt;

Is a width specifier, encoded in 'size':

&lt;d&gt;

&lt;n&gt;

&lt;m&gt;

&lt;Vd&gt;

&lt;T&gt;

|   size | <V>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | RESERVED |

Is the number of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the number of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

Is the number of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'size:Q':

|   size | Q   | <T>      |
|--------|-----|----------|
|     00 | x   | RESERVED |
|     01 | 0   | 4H       |
|     01 | 1   | 8H       |
|     10 | 0   | 2S       |
|     10 | 1   | 4S       |
|     11 | x   | RESERVED |

&lt;Vn&gt;

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

&lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand1 = V[n, datasize]; constant bits(datasize) operand2 = V[m, datasize]; constant bits(datasize) operand3 = V[d, datasize]; bits(datasize) result; integer element1; integer element2; integer element3; integer accum; boolean sat; for e = 0 to elements-1 element1 = SInt(Elem[operand1, e, esize]); element2 = SInt(Elem[operand2, e, esize]); element3 = SInt(Elem[operand3, e, esize]); accum = (element3 << esize) + 2 * (element1 * element2); accum = RShr(accum, esize, rounding); (Elem[result, e, esize], sat) = SignedSatQ(accum, esize); if sat then FPSR.QC = '1'; V[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
