## C8.2.502 PEXT (predicate)

Predicate extract from predicate-as-counter

This instruction converts the source predicate-as-counter into a four register wide predicate-as-mask, and copies the portion of the mask value selected by the portion index to the destination predicate register. A portion corresponds to a one predicate register fraction of the wider predicate-as-mask value.

## SVE2

(FEAT\_SME2 || FEAT\_SVE2p1)

<!-- image -->

|   31 | 29 28                      | 25 24 23 22 21 20 16 15 14 13 11 10 9 8 7 5 4 3   |
|------|----------------------------|---------------------------------------------------|
|    0 | 0 1 0 0 1 0 1 size 1 0 0 0 | 0 0 0 1 1 1 0 0 imm2 PNn 1 Pd                     |

## Encoding

```
PEXT <Pd>.<T>, <PNn>[<imm>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) && !IsFeatureImplemented(FEAT_SVE2p1) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt('1':PNn); constant integer d = UInt(Pd); constant integer part = UInt(imm2);
```

## Assembler Symbols

## &lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

Is the size specifier, encoded in 'size':

## &lt;PNn&gt;

Is the name of the first source scalable predicate register PN8-PN15, with predicate-as-counter encoding, encoded in the 'PNn' field.

## &lt;imm&gt;

Is the portion index, in the range 0 to 3, encoded in the 'imm2' field.

<!-- image -->

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

## Operation

```
if IsFeatureImplemented(FEAT_SVE2p1) then CheckSVEEnabled(); else CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) pred = P[n, PL]; constant bits(PL*4) mask = CounterToPredicate(pred<15:0>, PL*4); bits(PL) result; constant integer psize = esize DIV 8; for e = 0 to elements-1 constant bit pbit = PredicateElement(mask, part * elements + e, esize); Elem[result, e, psize] = ZeroExtend(pbit, psize); P[d, PL] = result;
```