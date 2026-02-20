## C8.2.848 UQCVTN

Unsigned 32-bit integer saturating extract narrow to interleaved 16-bit integer

This instruction saturates the unsigned integer value in each element of the pair of source vectors to half the original source element width, and places the two-way interleaved results in the half-width destination elements.

This instruction is unpredicated.

```
SVE2
```

(FEAT\_SME2 || FEAT\_SVE2p1)

<!-- image -->

## Encoding

```
UQCVTN <Zd>.H, { <Zn1>.S-<Zn2>.S }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) && !IsFeatureImplemented(FEAT_SVE2p1) then EndOfDecode(Decode_UNDEF); constant integer esize = 16; constant integer n = UInt(Zn:'0'); constant integer d = UInt(Zd);
```

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

## &lt;Zn1&gt;

Is the name of the first scalable vector register of the source multi-vector group, encoded as 'Zn' times 2.

## &lt;Zn2&gt;

Is the name of the second scalable vector register of the source multi-vector group, encoded as 'Zn' times 2 plus 1.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV (2 * esize); bits(VL) result; for e = 0 to elements-1 for i = 0 to 1 constant bits(VL) operand = Z[n+i, VL]; constant integer element = UInt(Elem[operand, e, 2 * esize]); Elem[result, 2*e + i, esize] = UnsignedSat(element, esize); Z[d, VL] = result;
```