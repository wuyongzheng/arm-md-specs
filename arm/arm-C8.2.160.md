## C8.2.160 FADDV

Floating-point add recursive reduction to scalar

This instruction adds horizontally the floating-point values over all lanes of a vector using a recursive pairwise reduction, and places the result in the SIMD&amp;FP scalar destination register. Inactive elements in the source vector are treated as +0.0.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FADDV <V><d>, <Pg>, <Zn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Vd);
```

## Assembler Symbols

<!-- image -->

&lt;V&gt;

Is a width specifier, encoded in 'size':

<!-- image -->

&lt;Pg&gt;

<!-- image -->

&lt;Zn&gt;

|   size | <V>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |

Is the number [0-31] of the destination SIMD&amp;FP register, encoded in the 'Vd' field.

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

Is the name of the source scalable vector register, encoded in the 'Zn' field.

&lt;T&gt;

Is the size specifier, encoded in 'size':

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand = if AnyActiveElement(mask, esize) then Z[n, VL] else Zeros(VL); constant bits(esize) identity = FPZero('0', esize); V[d, esize] = FPReducePredicated(ReduceOp_FADD, operand, mask, identity, FPCR);
```

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |