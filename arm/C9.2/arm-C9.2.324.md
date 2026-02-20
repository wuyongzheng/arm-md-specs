## C9.2.324 URSHL (multiple vectors)

Multi-vector unsigned rounding shift left

This instruction shifts the unsigned elements of the two or four first source vectors by corresponding elements of the two or four second source vectors and destructively places the rounded results in the corresponding elements of the two or four first source vectors. A positive shift amount performs a left shift, otherwise a right shift by the negated shift amount is performed.

This instruction is unpredicated.

It has encodings from 2 classes: Two registers and Four registers

```
Two registers (FEAT_SME2)
```

<!-- image -->

## Encoding

```
URSHL { <Zdn1>.<T>-<Zdn2>.<T> }, { <Zdn1>.<T>-<Zdn2>.<T> }, { <Zm1>.<T>-<Zm2>.<T> }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer dn = UInt(Zdn:'0'); constant integer m = UInt(Zm:'0'); constant integer nreg = 2;
```

## Four registers

```
(FEAT_SME2)
```

<!-- image -->

## Encoding

```
URSHL { <Zdn1>.<T>-<Zdn4>.<T> }, { <Zdn1>.<T>-<Zdn4>.<T> }, { <Zm1>.<T>-<Zm4>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer dn = UInt(Zdn:'00'); constant integer m = UInt(Zm:'00'); constant integer nreg = 4;
```

```
}
```

## Assembler Symbols

## &lt;Zdn1&gt;

For the 'Two registers' variant: is the name of the first scalable vector register of the destination and first source multi-vector group, encoded as 'Zdn' times 2.

For the 'Four registers' variant: is the name of the first scalable vector register of the destination and first source multi-vector group, encoded as 'Zdn' times 4.

Is the size specifier, encoded in 'size':

## &lt;Zdn2&gt;

Is the name of the second scalable vector register of the destination and first source multi-vector group, encoded as 'Zdn' times 2 plus 1.

## &lt;Zm1&gt;

For the 'Two registers' variant: is the name of the first scalable vector register of the second source multi-vector group, encoded as 'Zm' times 2.

For the 'Four registers' variant: is the name of the first scalable vector register of the second source multi-vector group, encoded as 'Zm' times 4.

## &lt;Zm2&gt;

Is the name of the second scalable vector register of the second source multi-vector group, encoded as 'Zm' times 2 plus 1.

## &lt;Zdn4&gt;

Is the name of the fourth scalable vector register of the destination and first source multi-vector group, encoded as 'Zdn' times 4 plus 3.

## &lt;Zm4&gt;

Is the name of the fourth scalable vector register of the second source multi-vector group, encoded as 'Zm' times 4 plus 3.

## Operation

```
CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; array [0..3] of bits(VL) results; for r = 0 to nreg-1 constant bits(VL) operand1 = Z[dn+r, VL]; constant bits(VL) operand2 = Z[m+r, VL]; for e = 0 to elements-1 constant integer element = UInt(Elem[operand1, e, esize]); integer shift = ShiftSat(SInt(Elem[operand2, e,
```

## &lt;T&gt;

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

```
esize]), esize);
```

```
integer res; if shift >= 0 then res = element << shift; else shift = -shift; res = (element + (1 << (shift - 1))) >> shift; Elem[results[r], e, esize] = res<esize-1:0>; for r = 0 to nreg-1 Z[dn+r, VL] = results[r];
```