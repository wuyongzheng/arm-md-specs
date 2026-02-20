## C8.2.291 LASTA (SIMD&amp;FP scalar)

Extract element after last to SIMD&amp;FP scalar register

This instruction extracts the element after the Last active element to a SIMD&amp;FP scalar register. If there is an Active element, the element after the Last active element modulo the number of elements from the final source vector register is extracted. If there are no Active elements, element zero is extracted. Then the extracted element is placed in the destination SIMD&amp;FP scalar register.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
LASTA <V><d>, <Pg>, <Zn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Vd); constant boolean isBefore = FALSE;
```

## Assembler Symbols

&lt;V&gt;

Is a width specifier, encoded in 'size':

&lt;d&gt;

<!-- image -->

<!-- image -->

B

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
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand = Z[n, VL]; integer last = LastActiveElement(mask, esize); if isBefore then if last < 0 then last = elements - 1; else last = last + 1; if last >= elements then last = 0; V[d, esize] = Elem[operand, last, esize];
```

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |