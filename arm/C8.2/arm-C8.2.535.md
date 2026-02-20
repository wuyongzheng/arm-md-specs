## C8.2.535 PUNPKHI, PUNPKLO

Unpack and widen half of predicate

This instruction unpacks elements from the lowest or highest half of the source predicate and places them in elements of twice their size within the destination predicate. This instruction is unpredicated.

It has encodings from 2 classes: High half and Low half

## High half

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
PUNPKHI <Pd>.H, <Pn>.B
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 16; constant integer n = UInt(Pn); constant integer d = UInt(Pd); constant boolean hi = TRUE;
```

## Low half

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
PUNPKLO <Pd>.H, <Pn>.B
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 16; constant integer n = UInt(Pn); constant integer d = UInt(Pd); constant boolean hi = FALSE;
```

## Assembler Symbols

&lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

## &lt;Pn&gt;

Is the name of the source scalable predicate register, encoded in the 'Pn' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) operand = P[n, PL]; bits(PL) result; constant integer psize = esize DIV 8; for e = 0 to elements-1 constant bit pbit = PredicateElement(operand, if hi then e + elements else e, esize DIV 2); Elem[result, e, psize] = ZeroExtend(pbit, psize); P[d, PL] = result;
```