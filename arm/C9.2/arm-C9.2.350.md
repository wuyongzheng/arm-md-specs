## C9.2.350 ZIP (two registers)

Interleave elements from two vectors

This instruction places the two-way interleaved elements from the first and second source vectors in the corresponding elements of the two destination vectors.

This instruction is unpredicated.

It has encodings from 2 classes: 8-bit to 64-bit elements and 128-bit element

```
8-bit to 64-bit elements (FEAT_SME2)
```

<!-- image -->

## Encoding

```
ZIP { <Zd1>.<T>-<Zd2>.<T> }, <Zn>.<T>, <Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd:'0');
```

## 128-bit element

(FEAT\_SME2)

<!-- image -->

## Encoding

```
ZIP { <Zd1>.Q-<Zd2>.Q }, <Zn>.Q, <Zm>.Q
```

## Decode for this encoding

```
EndOfDecode(Decode_UNDEF);
```

```
if !IsFeatureImplemented(FEAT_SME2) then if MaxImplementedSVL() < 256 then EndOfDecode(Decode_UNDEF); constant integer esize = 128; constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd:'0');
```

```
EndOfDecode(Decode_UNDEF);
```

## Assembler Symbols

## &lt;Zd1&gt;

Is the name of the first scalable vector register of the destination multi-vector group, encoded as 'Zd' times 2.

&lt;T&gt;

Is the size specifier, encoded in 'size':

&lt;Zd2&gt;

Is the name of the second scalable vector register of the destination multi-vector group, encoded as 'Zd' times 2 plus 1.

&lt;Zn&gt;

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

&lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; if VL < esize * 2 then EndOfDecode(Decode_UNDEF); constant integer pairs = VL DIV (esize * 2); constant bits(VL) operand0 = Z[n, VL]; constant bits(VL) operand1 = Z[m, VL]; bits(VL) result; for r = 0 to 1 constant integer base = r * pairs; for p = 0 to pairs-1 Elem[result, 2*p+0, esize] = Elem[operand0, base+p, esize]; Elem[result, 2*p+1, esize] = Elem[operand1, base+p, esize]; Z[d+r, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.