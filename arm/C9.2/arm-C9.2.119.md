## C9.2.119 FMUL (multiple and single vector)

Multi-vector floating-point multiply by vector

This instruction multiplies all the floating-point elements of the two or four first source vectors with the corresponding elements of the second source vector and places the results in the corresponding elements of the two or four destination vectors.

This instruction follows SME2 floating-point numerical behaviors corresponding to instructions that place their results in one or more SVE Z vectors.

This instruction is unpredicated.

It has encodings from 2 classes: Two registers and Four registers

```
Two registers
```

(FEAT\_SME2p2)

<!-- image -->

## Encoding

```
FMUL { <Zd1>.<T>-<Zd2>.<T> }, { <Zn1>.<T>-<Zn2>.<T> }, <Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2p2) then constant integer esize = 8 << UInt(size); constant integer d = UInt(Zd:'0'); constant integer n = UInt(Zn:'0'); constant integer m = UInt('0':Zm); constant integer nreg = 2;
```

## Four registers

(FEAT\_SME2p2)

<!-- image -->

## Encoding

```
FMUL { <Zd1>.<T>-<Zd4>.<T> }, { <Zn1>.<T>-<Zn4>.<T> }, <Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2p2) then constant integer esize = 8 << UInt(size); constant integer d = UInt(Zd:'00'); constant integer n = UInt(Zn:'00'); constant integer m = UInt('0':Zm); constant integer nreg = 4;
```

```
EndOfDecode(Decode_UNDEF);
```

```
EndOfDecode(Decode_UNDEF);
```

## Assembler Symbols

## &lt;Zd1&gt;

For the 'Two registers' variant: is the name of the first scalable vector register of the destination multi-vector group, encoded as 'Zd' times 2.

For the 'Four registers' variant: is the name of the first scalable vector register of the destination multi-vector group, encoded as 'Zd' times 4.

Is the size specifier, encoded in 'size':

## &lt;Zd2&gt;

Is the name of the second scalable vector register of the destination multi-vector group, encoded as 'Zd' times 2 plus 1.

## &lt;Zn1&gt;

For the 'Two registers' variant: is the name of the first scalable vector register of the first source multi-vector group, encoded as 'Zn' times 2.

For the 'Four registers' variant: is the name of the first scalable vector register of the first source multi-vector group, encoded as 'Zn' times 4.

## &lt;Zn2&gt;

Is the name of the second scalable vector register of the first source multi-vector group, encoded as 'Zn' times 2 plus 1.

## &lt;Zm&gt;

Is the name of the second source scalable vector register Z0-Z15, encoded in the 'Zm' field.

## &lt;Zd4&gt;

Is the name of the fourth scalable vector register of the destination multi-vector group, encoded as 'Zd' times 4 plus 3.

## &lt;Zn4&gt;

Is the name of the fourth scalable vector register of the first source multi-vector group, encoded as 'Zn' times 4 plus 3.

## Operation

```
CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; array [0..3] of bits(VL) results; for r = 0 to nreg-1 constant bits(VL) operand1 = Z[n+r, VL]; constant bits(VL) operand2 = Z[m, VL];
```

## &lt;T&gt;

|   size | <T>   |
|--------|-------|
|     01 | H     |
|     10 | S     |
|     11 | D     |

```
for e = 0 to elements-1 constant bits(esize) element1 = Elem[operand1, e, esize]; constant bits(esize) element2 = Elem[operand2, e, esize]; Elem[results[r], e, esize] = FPMul(element1, element2, FPCR); for r = 0 to nreg-1 Z[d+r, VL] = results[r];
```