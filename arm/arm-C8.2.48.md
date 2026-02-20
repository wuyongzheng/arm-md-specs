## C8.2.48 BFCVTNT

Single-precision convert to BFloat16 (top, predicated)

This instruction converts each active floating-point element of the source vector from single-precision to BFloat16 floating-point, and places the results in the odd-numbered 16-bit elements of the destination vector, leaving the even-numbered elements unchanged. Inactive elements in the destination vector register remain unmodified or are set to zero, depending on whether merging or zeroing predication is selected.

ID\_AA64ZFR0\_EL1.BF16 indicates whether this instruction is implemented.

It has encodings from 2 classes: Merging and Zeroing

## Merging

((FEAT\_SVE || FEAT\_SME) &amp;&amp; FEAT\_BF16)

<!-- image -->

## Encoding

```
BFCVTNT <Zd>.H, <Pg>/M, <Zn>.S
```

## Decode for this encoding

```
if ((!IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME)) || !IsFeatureImplemented(FEAT_BF16)) then EndOfDecode(Decode_UNDEF); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant boolean merging = TRUE;
```

## Zeroing

(FEAT\_SVE2p2 || FEAT\_SME2p2)

<!-- image -->

## Encoding

```
BFCVTNT <Zd>.H, <Pg>/Z, <Zn>.S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p2) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant boolean merging = FALSE;
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

&lt;Pg&gt;

&lt;Zn&gt;

Is the name of the source scalable vector register, encoded in the 'Zn' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV 32; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand = if AnyActiveElement(mask, 32) then Z[n, VL] else Zeros(VL); bits(VL) result = Z[d, VL]; for e = 0 to elements-1 if ActivePredicateElement(mask, e, 32) then constant bits(32) element = Elem[operand, e, 32]; Elem[result, 2*e+1, 16] = FPConvertBF(element, FPCR); elsif !merging then Elem[result, 2*e+1, 16] = Zeros(16); Z[d, VL] = result;
```