## C8.2.545 REV (vector)

Reverse all elements in a vector (unpredicated)

This instruction reads all elements in the source vector, reverses the order of all the elements, and places the result in the destination vector. This instruction is unpredicated.

```
SVE
```

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
REV <Zd>.<T>, <Zn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn); constant integer d = UInt(Zd);
```

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

<!-- image -->

<!-- image -->

&lt;Zn&gt;

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

Is the name of the source scalable vector register, encoded in the 'Zn' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant bits(VL) operand = Z[n, VL]; constant bits(VL) result = Reverse(operand, esize); Z[d, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.