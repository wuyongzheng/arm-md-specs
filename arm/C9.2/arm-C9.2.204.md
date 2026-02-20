## C9.2.204 SMAX (multiple and single vector)

Multi-vector signed maximum by vector

This instruction determines the signed maximum of elements of the second source vector and the corresponding elements of the two or four first source vectors and destructively places the results in the corresponding elements of the two or four first source vectors.

This instruction is unpredicated.

It has encodings from 2 classes: Two registers and Four registers

Two registers

(FEAT\_SME2)

<!-- image -->

## Encoding

```
SMAX { <Zdn1>.<T>-<Zdn2>.<T> }, { <Zdn1>.<T>-<Zdn2>.<T> }, <Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer dn = UInt(Zdn:'0'); constant integer m = UInt('0':Zm); constant integer nreg = 2; constant boolean unsigned = FALSE;
```

## Four registers

```
(FEAT_SME2)
```

<!-- image -->

## Encoding

```
SMAX { <Zdn1>.<T>-<Zdn4>.<T> }, { <Zdn1>.<T>-<Zdn4>.<T> }, <Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer dn = UInt(Zdn:'00'); constant integer m = UInt('0':Zm); constant integer nreg = 4; constant boolean unsigned = FALSE;
```

## Assembler Symbols

## &lt;Zdn1&gt;

For the 'Two registers' variant: is the name of the first scalable vector register of the destination and first source multi-vector group, encoded as 'Zdn' times 2.

For the 'Four registers' variant: is the name of the first scalable vector register of the destination and first source multi-vector group, encoded as 'Zdn' times 4.

Is the size specifier, encoded in 'size':

## &lt;Zdn2&gt;

Is the name of the second scalable vector register of the destination and first source multi-vector group, encoded as 'Zdn' times 2 plus 1.

## &lt;Zm&gt;

Is the name of the second source scalable vector register Z0-Z15, encoded in the 'Zm' field.

## &lt;Zdn4&gt;

Is the name of the fourth scalable vector register of the destination and first source multi-vector group, encoded as 'Zdn' times 4 plus 3.

## Operation

```
CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; array [0..3] of bits(VL) results; for r = 0 to nreg-1 constant bits(VL) operand1 = Z[dn+r, VL]; constant bits(VL) operand2 = Z[m, VL]; for e = 0 to elements-1 constant bits(esize) op1elt = Elem[operand1, e, esize]; constant integer element1 = if unsigned then UInt(op1elt) else constant bits(esize) op2elt = Elem[operand2, e, esize]; constant integer element2 = if unsigned then UInt(op2elt) else constant integer res = Max(element1, element2); Elem[results[r], e, esize] = res<esize-1:0>; for r = 0 to nreg-1 Z[dn+r, VL] = results[r];
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

## &lt;T&gt;

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

```
SInt(op1elt); SInt(op2elt);
```