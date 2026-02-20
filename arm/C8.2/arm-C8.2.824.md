## C8.2.824 UMAXV

Unsigned maximum reduction to scalar

This instruction performs an unsigned maximum horizontally across all lanes of a vector, and places the result in the SIMD&amp;FP scalar destination register. Inactive elements in the source vector are treated as zero.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
UMAXV <V><d>, <Pg>, <Zn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Vd); constant boolean unsigned = TRUE;
```

## Assembler Symbols

<!-- image -->

Is a width specifier, encoded in 'size':

<!-- image -->

&lt;Pg&gt;

&lt;Zn&gt;

|   size | <V>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

Is the number [0-31] of the destination SIMD&amp;FP register, encoded in the 'Vd' field.

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

Is the name of the source scalable vector register, encoded in the 'Zn' field.

&lt;T&gt;

Is the size specifier, encoded in 'size':

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand = if AnyActiveElement(mask, esize) then Z[n, VL] else Zeros(VL); integer maximum = if unsigned then 0 else -(2^(esize-1)); for e = 0 to elements-1 if ActivePredicateElement(mask, e, esize) then constant bits(esize) opelt = Elem[operand, e, esize]; constant integer element = if unsigned then UInt(opelt) else SInt(opelt); maximum = Max(maximum, element); V[d, esize] = maximum<esize-1:0>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |