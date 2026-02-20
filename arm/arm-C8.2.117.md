## C8.2.117 CNTP (predicate as counter)

Set scalar to count from predicate-as-counter

This instruction counts the number of true elements in the source predicate, up to the total number of elements in two or four vectors, and places the scalar result in the destination general-purpose register.

## SVE2

(FEAT\_SME2 || FEAT\_SVE2p1)

<!-- image -->

## Encoding

```
CNTP <Xd>, <PNn>.<T>, <vl>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) && !IsFeatureImplemented(FEAT_SVE2p1) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(PNn); constant integer d = UInt(Rd); constant integer width = 2 << UInt(vl);
```

## Assembler Symbols

## &lt;Xd&gt;

Is the 64-bit name of the destination general-purpose register, encoded in the 'Rd' field.

## &lt;PNn&gt;

Is the name of the source scalable predicate register, with predicate-as-counter encoding, encoded in the 'PNn' field.

<!-- image -->

&lt;vl&gt;

Is the size specifier, encoded in 'size':

Is the vl specifier, encoded in 'vl':

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

## Operation

```
if IsFeatureImplemented(FEAT_SVE2p1) then CheckSVEEnabled(); else CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) pred = P[n, PL]; constant bits(PL*4) mask = CounterToPredicate(pred<15:0>, PL*4); bits(64) sum = Zeros(64); constant integer maxelements = elements * width; for e = 0 to maxelements-1 if ActivePredicateElement(mask, e, esize) then sum = sum + 1; X[d, 64] = sum;
```

|   vl | <vl>   |
|------|--------|
|    0 | VLx2   |
|    1 | VLx4   |