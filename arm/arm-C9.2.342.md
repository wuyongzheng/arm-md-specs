## C9.2.342 UZP (four registers)

Concatenate elements from four vectors

This instruction concatenates every fourth element from each of the four source vectors and places them in the corresponding elements of the four destination vectors.

This instruction is unpredicated.

It has encodings from 2 classes: 8-bit to 64-bit elements and 128-bit element

```
8-bit to 64-bit elements (FEAT_SME2)
```

<!-- image -->

## Encoding

```
UZP { <Zd1>.<T>-<Zd4>.<T> }, { <Zn1>.<T>-<Zn4>.<T> }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); if size == '11' && MaxImplementedSVL() < 256 then constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn:'00'); constant integer d = UInt(Zd:'00');
```

## 128-bit element

(FEAT\_SME2)

<!-- image -->

## Encoding

```
UZP { <Zd1>.Q-<Zd4>.Q }, { <Zn1>.Q-<Zn4>.Q }
```

## Decode for this encoding

```
EndOfDecode(Decode_UNDEF);
```

```
if !IsFeatureImplemented(FEAT_SME2) then if MaxImplementedSVL() < 512 then EndOfDecode(Decode_UNDEF); constant integer esize = 128; constant integer n = UInt(Zn:'00'); constant integer d = UInt(Zd:'00');
```

```
EndOfDecode(Decode_UNDEF);
```

## Assembler Symbols

## &lt;Zd1&gt;

Is the name of the first scalable vector register of the destination multi-vector group, encoded as 'Zd' times 4.

&lt;T&gt;

Is the size specifier, encoded in 'size':

## &lt;Zd4&gt;

Is the name of the fourth scalable vector register of the destination multi-vector group, encoded as 'Zd' times 4 plus 3.

## &lt;Zn1&gt;

Is the name of the first scalable vector register of the source multi-vector group, encoded as 'Zn' times 4.

## &lt;Zn4&gt;

Is the name of the fourth scalable vector register of the source multi-vector group, encoded as 'Zn' times 4 plus 3.

## Operation

```
CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; if VL < esize * 4 then EndOfDecode(Decode_UNDEF); constant integer quads = VL DIV (esize * 4); bits(VL) result0; bits(VL) result1; bits(VL) result2; bits(VL) result3; for r = 0 to 3 constant bits(VL) operand = Z[n+r, VL]; constant integer base = r * quads; for q = 0 to quads-1 Elem[result0, base+q, esize] = Elem[operand, 4*q+0, esize]; Elem[result1, base+q, esize] = Elem[operand, 4*q+1, esize]; Elem[result2, base+q, esize] = Elem[operand, 4*q+2, esize]; Elem[result3, base+q, esize] = Elem[operand, 4*q+3, esize]; Z[d+0, VL] = result0; Z[d+1, VL] = result1; Z[d+2, VL] = result2; Z[d+3, VL] = result3;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |