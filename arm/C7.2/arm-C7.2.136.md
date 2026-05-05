## C7.2.136 FMINNMP (vector)

Floating-point minimum number pairwise (vector)

This instruction creates a vector by concatenating the vector elements of the first source SIMD&amp;FP register after the vector elements of the second source SIMD&amp;FP register, reads each pair of adjacent vector elements in the two source SIMD&amp;FP registers, writes the smallest of each pair of floating-point values into a vector, and writes the vector to the destination SIMD&amp;FP register. All the values in this instruction are floating-point values.

Regardless of the value of FPCR.AH, the behavior is as follows for each pairwise operation:

- Negative zero compares less than positive zero.
- If one element is numeric and the other is a quiet NaN, the result is the numeric value.
- When FPCR.DN is 0, if either element is a signaling NaN or if both elements are NaNs, the result is a quiet NaN.
- When FPCR.DN is 1, if either element is a signaling NaN or if both elements are NaNs, the result is Default NaN.

This instruction can generate a floating-point exception. Depending on the settings in FPCR, the exception results in either a flag being set in FPSR or a synchronous exception being generated. For more information, see Floating-point exceptions and exception traps.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 2 classes: Half-precision and Single-precision and double-precision

## Half-precision

(FEAT\_AdvSIMD &amp;&amp; FEAT\_FP16)

<!-- image -->

## Encoding

```
FMINNMP <Vd>.<T>, <Vn>.<T>, <Vm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) || !IsFeatureImplemented(FEAT_FP16) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer esize = 16; constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize;
```

## Single-precision and double-precision

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
FMINNMP <Vd>.<T>, <Vn>.<T>, <Vm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if sz:Q == '10' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer esize = 32 << UInt(sz); constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize;
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

For the 'Half-precision' variant: is an arrangement specifier, encoded in 'Q':

|   Q | <T>   |
|-----|-------|
|   0 | 4H    |
|   1 | 8H    |

For the 'Single-precision and double-precision' variant: is an arrangement specifier, encoded in 'sz:Q':

|   sz |   Q | <T>      |
|------|-----|----------|
|    0 |   0 | 2S       |
|    0 |   1 | 4S       |
|    1 |   0 | RESERVED |
|    1 |   1 | 2D       |

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand1 = V[n, datasize]; constant bits(datasize) operand2 = V[m, datasize]; bits(datasize) result; constant bits(2*datasize) concat bits(esize) element1;
```

```
= operand2:operand1; bits(esize) element2;
```

<!-- image -->

&lt;Vn&gt;

```
for e = 0 to elements-1 element1 = Elem[concat, 2*e, esize]; element2 = Elem[concat, (2*e)+1, esize]; Elem[result, e, esize] = FPMinNum(element1, element2, FPCR); V[d, datasize] = result;
```
