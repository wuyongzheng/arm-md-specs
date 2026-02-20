## C9.2.317 UQCVT (two registers)

Multi-vector unsigned 32-bit integer saturating extract narrow to 16-bit integer

This instruction saturates the unsigned 32-bit integer value in each element of the two source vectors to half the original source element width, and places the 16-bit results in the half-width destination elements.

This instruction is unpredicated.

```
SME2 (FEAT_SME2)
```

<!-- image -->

## Encoding

```
UQCVT <Zd>.H, { <Zn1>.S-<Zn2>.S }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); constant integer esize = 16; constant integer n = UInt(Zn:'0'); constant integer d = UInt(Zd);
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

## &lt;Zn1&gt;

Is the name of the first scalable vector register of the source multi-vector group, encoded as 'Zn' times 2.

## &lt;Zn2&gt;

Is the name of the second scalable vector register of the source multi-vector group, encoded as 'Zn' times 2 plus 1.

## Operation

```
CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV (2 * esize); bits(VL) result; for r = 0 to 1 constant bits(VL) operand = Z[n+r, VL]; for e = 0 to elements-1 constant integer element = UInt(Elem[operand, e, 2 * esize]); Elem[result, r*elements + e, esize] = UnsignedSat(element, esize); Z[d, VL] = result;
```