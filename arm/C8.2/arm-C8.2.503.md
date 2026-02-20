## C8.2.503 PEXT (predicate pair)

Predicate extract pair from predicate-as-counter

This instruction converts the source predicate-as-counter into a four register wide predicate-as-mask, and copies the two portions of the mask value selected by the portion index to the two destination predicate registers. A portion corresponds to a one predicate register fraction of the wider predicate-as-mask value.

## SVE2

(FEAT\_SME2 || FEAT\_SVE2p1)

<!-- image -->

| 31 29 28      | 25 24 23 22 21 20 16 15 14 13 11 10 9 8 7 5 4 3   |
|---------------|---------------------------------------------------|
| 0 0 1 0 0 1 0 | 1 size 1 0 0 0 0 0 0 1 1 1 0 1 0 i1 PNn 1 Pd      |

## Encoding

```
PEXT { <Pd1>.<T>, <Pd2>.<T> }, <PNn>[<imm>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) && !IsFeatureImplemented(FEAT_SVE2p1) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt('1':PNn); constant integer d0 = UInt(Pd); constant integer d1 = (UInt(Pd) + 1) MOD 16; constant integer part = UInt(i1);
```

## Assembler Symbols

## &lt;Pd1&gt;

Is the name of the first destination scalable predicate register, encoded in the 'Pd' field.

<!-- image -->

Is the size specifier, encoded in 'size':

## &lt;Pd2&gt;

Is the name of the second destination scalable predicate register, encoded in the 'Pd' field.

## &lt;PNn&gt;

Is the name of the first source scalable predicate register PN8-PN15, with predicate-as-counter encoding, encoded in the 'PNn' field.

## &lt;imm&gt;

Is the portion index, in the range 0 to 1, encoded in the 'i1' field.

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

## Operation

```
if IsFeatureImplemented(FEAT_SVE2p1) then CheckSVEEnabled(); else CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) pred = P[n, PL]; constant bits(PL*4) mask = CounterToPredicate(pred<15:0>, PL*4); bits(PL) result0; bits(PL) result1; constant integer psize = esize DIV 8; for e = 0 to elements-1 constant bit pbit = PredicateElement(mask, part * 2 * elements + e, esize); Elem[result0, e, psize] = ZeroExtend(pbit, psize); for e = 0 to elements-1 constant bit pbit = PredicateElement(mask, part * 2 * elements + elements + e, esize); Elem[result1, e, psize] = ZeroExtend(pbit, psize); P[d0, PL] = result0; P[d1, PL] = result1;
```