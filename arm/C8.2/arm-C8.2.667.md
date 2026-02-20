## C8.2.667 SQRSHRUN

Signed saturating rounding shift right unsigned narrow by immediate and interleave

This instruction shifts right by an immediate value the signed integer value in each element of the two source vectors, and places the two-way interleaved rounded results in the half-width destination elements. Each result element is saturated to the half-width N-bit element's unsigned integer range 0 to (2 N )-1. The immediate shift amount is an unsigned value in the range 1 to 16.

This instruction is unpredicated.

```
16-bit
```

(FEAT\_SME2 || FEAT\_SVE2p1)

<!-- image -->

## Encoding

```
SQRSHRUN <Zd>.H, {
```

```
<Zn1>.S-<Zn2>.S }, #<const>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) && !IsFeatureImplemented(FEAT_SVE2p1) then EndOfDecode(Decode_UNDEF); constant integer esize = 16; constant integer n = UInt(Zn:'0'); constant integer d = UInt(Zd); constant integer shift = esize -UInt(imm4);
```

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

## &lt;Zn1&gt;

Is the name of the first scalable vector register of the source multi-vector group, encoded as 'Zn' times 2.

## &lt;Zn2&gt;

Is the name of the second scalable vector register of the source multi-vector group, encoded as 'Zn' times 2 plus 1.

## &lt;const&gt;

Is the immediate shift amount, in the range 1 to 16, encoded in the 'imm4' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV (2 * esize); bits(VL) result; for e = 0 to elements-1 for i = 0 to 1 constant bits(VL) operand = Z[n+i, VL]; constant bits(2 * esize) element = Elem[operand, e, 2 * esize];
```

```
constant integer res = (SInt(element) + (1 << (shift-1))) >> shift; Elem[result, 2*e + i, esize] = UnsignedSat(res, esize); Z[d, VL] = result;
```