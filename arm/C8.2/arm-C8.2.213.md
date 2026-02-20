## C8.2.213 FMINQV

Floating-point minimum recursive reduction of quadword vector segments

This instruction computes a floating-point minimum of the same element numbers from each 128-bit source vector segment using a recursive pairwise reduction, and places each result into the corresponding element number of the 128-bit SIMD&amp;FP destination register. Inactive elements in the source vector are treated as +Infinity.

When FPCR.AH is 0, the behavior is as follows:

- Negative zero compares less than positive zero.
- When FPCR.DN is 0, if either value is a NaN, the result is a quiet NaN.
- When FPCR.DN is 1, if either value is a NaN, the result is Default NaN.

When FPCR.AH is 1, the behavior is as follows:

- If both values are zeros, regardless of the sign of either zero, the result is the second value.
- If either value is a NaN, regardless of the value of FPCR.DN, the result is the second value.

## SVE2

(FEAT\_SVE2p1 || FEAT\_SME2p1)

<!-- image -->

## Encoding

```
FMINQV <Vd>.<T>, <Pg>, <Zn>.<Tb>
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

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |
|     01 | 8H       |

&lt;Pg&gt;

&lt;Zn&gt;

## &lt;Tb&gt;

|   size | <T>   |
|--------|-------|
|     10 | 4S    |
|     11 | 2D    |

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

Is the name of the source scalable vector register, encoded in the 'Zn' field.

Is the size specifier, encoded in 'size':

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer segments = VL DIV 128; constant integer elempersegment = 128 DIV esize; constant integer segbits = segments*esize; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand = if AnyActiveElement(mask, esize) then Z[n, VL] else Zeros(VL); constant bits(esize) identity = FPInfinity('0', esize); bits(128) result = Zeros(128); for e = 0 to elempersegment-1 bits(segbits) stmp; for s = 0 to segments-1 if ActivePredicateElement(mask, s * elempersegment + e, esize) then Elem[stmp, s, esize] = Elem[operand, s * elempersegment + e, esize]; else Elem[stmp, s, esize] = identity; Elem[result, e, esize] = FPReduce(ReduceOp_FMIN, stmp, esize, FPCR); V[d, 128] = result;
```

|   size | <Tb>     |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |