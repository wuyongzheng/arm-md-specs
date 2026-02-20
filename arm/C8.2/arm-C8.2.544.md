## C8.2.544 REV (predicate)

Reverse all elements in a predicate

This instruction reads all elements in the source predicate, reverses the order of all the elements, and places the result in the destination predicate. This instruction is unpredicated.

```
SVE
```

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
REV <Pd>.<T>, <Pn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Pn); constant integer d = UInt(Pd);
```

## Assembler Symbols

&lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

Is the size specifier, encoded in 'size':

<!-- image -->

<!-- image -->

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

Is the name of the source scalable predicate register, encoded in the 'Pn' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant bits(PL) operand = P[n, PL]; constant bits(PL) result = Reverse(operand, esize DIV 8); P[d, PL] = result;
```