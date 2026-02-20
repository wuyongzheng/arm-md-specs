## C8.2.100 CLASTB (SIMD&amp;FP scalar)

Conditionally extract last element to SIMD&amp;FP scalar register

This instruction extracts, from the source vector register, the Last active element, and then zero-extends that element to destructively place in the destination and first source SIMD &amp; floating-point scalar register. If there are no Active elements, the least significant element-size bits of the destination and first source SIMD &amp; floating-point scalar register are destructively zero-extended.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
CLASTB <V><dn>, <Pg>, <V><dn>, <Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer dn = UInt(Vdn); constant integer m = UInt(Zm); constant boolean isBefore = TRUE;
```

## Assembler Symbols

&lt;V&gt;

Is a width specifier, encoded in 'size':

## &lt;dn&gt;

&lt;Pg&gt;

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

<!-- image -->

Is the name of the source scalable vector register, encoded in the 'Zm' field.

|   size | <V>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

Is the number [0-31] of the source and destination SIMD&amp;FP register, encoded in the 'Vdn' field.

&lt;T&gt;

Is the size specifier, encoded in 'size':

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(esize) operand1 = V[dn, esize]; constant bits(VL) operand2 = Z[m, VL]; bits(esize) result; integer last = LastActiveElement(mask, esize); if last < 0 then result = ZeroExtend(operand1, esize); else if !isBefore then last = last + 1; if last >= elements then last = 0; result = Elem[operand2, last, esize]; V[dn, esize] = result;
```

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |