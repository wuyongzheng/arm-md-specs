## C9.2.286 UCVTF

Multi-vector unsigned 32-bit integer convert to single-precision

This instruction converts each element of the two or four source vectors from unsigned 32-bit integer to single-precision, and places the results in the corresponding elements of the two or four destination vectors.

This instruction follows SME2 floating-point numerical behaviors corresponding to instructions that place their results in one or more SVE Z vectors.

This instruction is unpredicated.

It has encodings from 2 classes: Two registers and Four registers

## Two registers

(FEAT\_SME2)

<!-- image -->

## Encoding

```
UCVTF { <Zd1>.S-<Zd2>.S }, { <Zn1>.S-<Zn2>.S }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then constant integer n = UInt(Zn:'0'); constant integer d = UInt(Zd:'0'); constant integer nreg = 2; constant boolean unsigned = TRUE; constant FPRounding rounding = FPRoundingMode(FPCR);
```

## Four registers

(FEAT\_SME2)

<!-- image -->

## Encoding

```
UCVTF { <Zd1>.S-<Zd4>.S }, {
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then constant integer n = UInt(Zn:'00'); constant integer d = UInt(Zd:'00'); constant integer nreg = 4; constant boolean unsigned = TRUE; constant FPRounding rounding = FPRoundingMode(FPCR);
```

```
EndOfDecode(Decode_UNDEF);
```

```
<Zn1>.S-<Zn4>.S }
```

```
EndOfDecode(Decode_UNDEF);
```

U

## Assembler Symbols

## &lt;Zd1&gt;

For the 'Two registers' variant: is the name of the first scalable vector register of the destination multi-vector group, encoded as 'Zd' times 2.

For the 'Four registers' variant: is the name of the first scalable vector register of the destination multi-vector group, encoded as 'Zd' times 4.

## &lt;Zd2&gt;

Is the name of the second scalable vector register of the destination multi-vector group, encoded as 'Zd' times 2 plus 1.

## &lt;Zn1&gt;

For the 'Two registers' variant: is the name of the first scalable vector register of the source multi-vector group, encoded as 'Zn' times 2.

For the 'Four registers' variant: is the name of the first scalable vector register of the source multi-vector group, encoded as 'Zn' times 4.

## &lt;Zn2&gt;

Is the name of the second scalable vector register of the source multi-vector group, encoded as 'Zn' times 2 plus 1.

## &lt;Zd4&gt;

Is the name of the fourth scalable vector register of the destination multi-vector group, encoded as 'Zd' times 4 plus 3.

## &lt;Zn4&gt;

Is the name of the fourth scalable vector register of the source multi-vector group, encoded as 'Zn' times 4 plus 3.

## Operation

```
CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV 32; array [0..3] of bits(VL) results; for r = 0 to nreg-1 constant bits(VL) operand = Z[n+r, VL]; for e = 0 to elements-1 constant bits(32) element = Elem[operand, e, 32]; Elem[results[r], e, 32] = FixedToFP(element, 0, unsigned, FPCR, rounding, 32); for r = 0 to nreg-1 Z[d+r, VL] = results[r];
```