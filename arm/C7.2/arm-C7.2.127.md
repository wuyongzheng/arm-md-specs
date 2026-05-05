## C7.2.127 FMAXNMV

Floating-point maximum number across vector

This instruction compares all the vector elements in the source SIMD&amp;FP register, and writes the largest of the values as a scalar to the destination SIMD&amp;FP register. All the values in this instruction are floating-point values.

Regardless of the value of FPCR.AH, the behavior is as follows:

- Negative zero compares less than positive zero.
- If one value is numeric and the other is a quiet NaN, the result is the numeric value.
- When FPCR.DN is 0, if either value is a signaling NaN or if both values are NaNs, the result is a quiet NaN.
- When FPCR.DN is 1, if either value is a signaling NaN or if both values are NaNs, the result is Default NaN.

This instruction can generate a floating-point exception. Depending on the settings in FPCR, the exception results in either a flag being set in FPSR or a synchronous exception being generated. For more information, see Floating-point exceptions and exception traps.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 2 classes: Half-precision and Single-precision

## Half-precision

(FEAT\_AdvSIMD &amp;&amp; FEAT\_FP16)

<!-- image -->

## Encoding

```
FMAXNMV <V><d>, <Vn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) || !IsFeatureImplemented(FEAT_FP16) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 16; constant integer datasize = 64 << UInt(Q);
```

## Single-precision

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

FMAXNMV

S&lt;d&gt;,

&lt;Vn&gt;.4S

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); end if sz:Q != '01' then EndOfDecode(Decode_UNDEF); end // .4S only constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer{} esize = 32; constant integer{} datasize = 64 << UInt(Q);
```

## Assembler Symbols

&lt;V&gt;

Is the destination width specifier, H.

Is the number of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

Is an arrangement specifier, encoded in 'Q':

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand = V[n, datasize]; V[d, esize] =
```

<!-- image -->

&lt;Vn&gt;

&lt;T&gt;

|   Q | <T>   |
|-----|-------|
|   0 | 4H    |
|   1 | 8H    |

```
FPReduce(ReduceOp_FMAXNUM, operand, esize, FPCR);
```
