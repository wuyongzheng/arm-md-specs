## C8.2.847 UQADD (vectors, unpredicated)

Unsigned saturating add (unpredicated)

This instruction performs an unsigned saturating addition of all elements of the second source vector to the corresponding elements of the first source vector and places the results in the corresponding elements of the destination vector. Each result element is saturated to the N-bit element's unsigned integer range 0 to (2 N )-1. This instruction is unpredicated.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
UQADD <Zd>.<T>, <Zn>.<T>, <Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd); constant boolean unsigned = TRUE;
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

<!-- image -->

&lt;T&gt;

&lt;Zn&gt;

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

<!-- image -->

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result; for e = 0 to elements-1 constant bits(esize) op1elt = Elem[operand1, e, esize]; constant bits(esize) op2elt = Elem[operand2, e, esize]; if unsigned then constant integer element1 = UInt(op1elt); constant integer element2 = UInt(op2elt); (Elem[result, e, esize], -) = UnsignedSatQ(element1 + element2, else constant integer element1 = SInt(op1elt); constant integer element2 = SInt(op2elt); (Elem[result, e, esize], -) = SignedSatQ(element1 + element2, esize); Z[d, VL] = result;
```

```
esize);
```