## C9.2.203 SEL

Multi-vector conditional select

This instruction selects consecutive elements from the two or four first source vectors where predicate elements are true, and places them in the corresponding elements of the two or four destination vectors. The corresponding elements from the two or four second source vectors are placed in the remaining elements of the destination vectors.

It has encodings from 2 classes: Two registers and Four registers

Two registers (FEAT\_SME2)

<!-- image -->

## Encoding

```
SEL { <Zd1>.<T>-<Zd2>.<T> }, <PNg>, { <Zn1>.<T>-<Zn2>.<T> }, { <Zm1>.<T>-<Zm2>.<T> }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn:'0'); constant integer m = UInt(Zm:'0'); constant integer d = UInt(Zd:'0'); constant integer g = UInt('1':PNg); constant integer nreg = 2;
```

## Four registers

(FEAT\_SME2)

<!-- image -->

## Encoding

```
SEL { <Zd1>.<T>-<Zd4>.<T> }, <PNg>, { <Zn1>.<T>-<Zn4>.<T> }, { <Zm1>.<T>-<Zm4>.<T> }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn:'00'); constant integer m = UInt(Zm:'00'); constant integer d = UInt(Zd:'00'); constant integer g = UInt('1':PNg); constant integer nreg = 4;
```

## Assembler Symbols

## &lt;Zd1&gt;

For the 'Two registers' variant: is the name of the first scalable vector register of the destination multi-vector group, encoded as 'Zd' times 2.

For the 'Four registers' variant: is the name of the first scalable vector register of the destination multi-vector group, encoded as 'Zd' times 4.

Is the size specifier, encoded in 'size':

## &lt;Zd2&gt;

Is the name of the second scalable vector register of the destination multi-vector group, encoded as 'Zd' times 2 plus 1.

## &lt;PNg&gt;

Is the name of the governing scalable predicate register PN8-PN15, with predicate-as-counter encoding, encoded in the 'PNg' field.

## &lt;Zn1&gt;

For the 'Two registers' variant: is the name of the first scalable vector register of the first source multi-vector group, encoded as 'Zn' times 2.

For the 'Four registers' variant: is the name of the first scalable vector register of the first source multi-vector group, encoded as 'Zn' times 4.

## &lt;Zn2&gt;

Is the name of the second scalable vector register of the first source multi-vector group, encoded as 'Zn' times 2 plus 1.

## &lt;Zm1&gt;

For the 'Two registers' variant: is the name of the first scalable vector register of the second source multi-vector group, encoded as 'Zm' times 2.

For the 'Four registers' variant: is the name of the first scalable vector register of the second source multi-vector group, encoded as 'Zm' times 4.

## &lt;Zm2&gt;

Is the name of the second scalable vector register of the second source multi-vector group, encoded as 'Zm' times 2 plus 1.

## &lt;Zd4&gt;

Is the name of the fourth scalable vector register of the destination multi-vector group, encoded as 'Zd' times 4 plus 3.

## &lt;T&gt;

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

## &lt;Zn4&gt;

Is the name of the fourth scalable vector register of the first source multi-vector group, encoded as 'Zn' times 4 plus 3.

## &lt;Zm4&gt;

Is the name of the fourth scalable vector register of the second source multi-vector group, encoded as 'Zm' times 4 plus 3.

## Operation

```
CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; array [0..3] of bits(VL) results; constant bits(PL) pred = P[g, PL]; constant bits(PL * nreg) mask = CounterToPredicate(pred<15:0>, PL * nreg); for r = 0 to nreg-1 constant bits(VL) operand1 = Z[n+r, VL]; constant bits(VL) operand2 = Z[m+r, VL]; for e = 0 to elements-1 if ActivePredicateElement(mask, r * elements + e, esize) then Elem[results[r], e, esize] = Elem[operand1, e, esize]; else Elem[results[r], e, esize] = Elem[operand2, e, esize]; for r = 0 to nreg-1 Z[d+r, VL] = results[r];
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.