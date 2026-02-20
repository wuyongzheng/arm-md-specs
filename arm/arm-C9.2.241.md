## C9.2.241 SQRSHRUN

Multi-vector signed saturating rounding shift right narrow by immediate to interleaved unsigned integer

This instruction shifts right by an immediate value the signed integer value in each element of the four source vectors, and places the four-way interleaved rounded results in the quarter-width destination elements. Each result element is saturated to the quarter-width N-bit element's unsigned integer range 0 to (2 N )-1. The immediate shift amount is an unsigned value in the range 1 to number of bits per source element.

This instruction is unpredicated.

## SME2

(FEAT\_SME2)

<!-- image -->

## Encoding

```
SQRSHRUN <Zd>.<T>, { <Zn1>.<Tb>-<Zn4>.<Tb> }, #<const>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then if tsize == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << HighestSetBitNZ(tsize); constant integer n = UInt(Zn:'00'); constant integer d = UInt(Zd); constant integer shift = (8 * esize) UInt(tsize:imm5);
```

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'tsize':

## &lt;Zn1&gt;

Is the name of the first scalable vector register of the source multi-vector group, encoded as 'Zn' times 4.

<!-- image -->

&lt;T&gt;

```
EndOfDecode(Decode_UNDEF);
```

| tsize   | <T>      |
|---------|----------|
| 00      | RESERVED |
| 01      | B        |
| 1x      | H        |

## &lt;Tb&gt;

Is the size specifier, encoded in 'tsize':

## &lt;Zn4&gt;

Is the name of the fourth scalable vector register of the source multi-vector group, encoded as 'Zn' times 4 plus 3.

## &lt;const&gt;

Is the immediate shift amount, in the range 1 to number of bits per source element, encoded in 'tsize:imm5'.

## Operation

```
CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV (4 * esize); bits(VL) result; for e = 0 to elements-1 for i = 0 to 3 constant bits(VL) operand = Z[n+i, VL]; constant bits(4 * esize) element = Elem[operand, e, 4 * esize]; constant integer res = (SInt(element) + (1 << (shift-1))) >> shift; Elem[result, 4*e + i, esize] = UnsignedSat(res, esize); Z[d, VL] = result;
```

| tsize   | <Tb>     |
|---------|----------|
| 00      | RESERVED |
| 01      | S        |
| 1x      | D        |