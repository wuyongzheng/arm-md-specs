## C8.2.533 PTRUE (predicate as counter)

Initialize predicate-as-counter to all active

This instruction sets the destination predicate as all-Active elements, using the predicate-as-counter encoding.

## SVE2

(FEAT\_SME2 || FEAT\_SVE2p1)

<!-- image -->

## Encoding

```
PTRUE <PNd>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) && !IsFeatureImplemented(FEAT_SVE2p1) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer d = UInt('1':PNd);
```

## Assembler Symbols

## &lt;PNd&gt;

Is the name of the destination scalable predicate register PN8-PN15, with predicate-as-counter encoding, encoded in the 'PNd' field.

&lt;T&gt;

Is the size specifier, encoded in 'size':

## Operation

```
if IsFeatureImplemented(FEAT_SVE2p1) then CheckSVEEnabled(); else CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) result = EncodePredCount(esize, elements, elements, FALSE, PL); P[d, PL] = result;
```

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |