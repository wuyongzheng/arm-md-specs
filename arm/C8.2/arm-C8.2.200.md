## C8.2.200 FMAXNMQV

Floating-point maximum number recursive reduction of quadword vector segments

This instruction computes a floating-point maximum number of the same element numbers from each 128-bit source vector segment using a recursive pairwise reduction, and places each result into the corresponding element number of the 128-bit SIMD&amp;FP destination register. Inactive elements in the source vector are treated as the default NaN.

Regardless of the value of FPCR.AH, the behavior is as follows:

- Negative zero compares less than positive zero.
- If one value is numeric and the other is a quiet NaN, the result is the numeric value.
- When FPCR.DN is 0, if either value is a signaling NaN or if both values are NaNs, the result is a quiet NaN.
- When FPCR.DN is 1, if either value is a signaling NaN or if both values are NaNs, the result is Default NaN.

## SVE2

(FEAT\_SVE2p1 || FEAT\_SME2p1)

<!-- image -->

## Encoding

```
FMAXNMQV <Vd>.<T>, <Pg>, <Zn>.<Tb>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p1) && !IsFeatureImplemented(FEAT_SME2p1) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Vd);
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the destination SIMD&amp;FP register, encoded in the 'Vd' field.

Is an arrangement specifier, encoded in 'size':

<!-- image -->

&lt;T&gt;

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |
|     01 | 8H       |
|     10 | 4S       |
|     11 | 2D       |

## &lt;Pg&gt;

## &lt;Zn&gt;

## &lt;Tb&gt;

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

Is the name of the source scalable vector register, encoded in the 'Zn' field.

Is the size specifier, encoded in 'size':

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer segments = VL DIV 128; constant integer elempersegment = 128 DIV esize; constant integer segbits = segments*esize; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand = if AnyActiveElement(mask, esize) then Z[n, VL] else Zeros(VL); constant bits(esize) identity = FPDefaultNaN(FPCR, esize); bits(128) result = Zeros(128); for e = 0 to elempersegment-1 bits(segbits) stmp; for s = 0 to segments-1 if ActivePredicateElement(mask, s * elempersegment + e, esize) then Elem[stmp, s, esize] = Elem[operand, s * elempersegment + e, esize]; else Elem[stmp, s, esize] = identity; Elem[result, e, esize] = FPReduce(ReduceOp_FMAXNUM, stmp, esize, FPCR); V[d, 128] = result;
```

|   size | <Tb>     |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |