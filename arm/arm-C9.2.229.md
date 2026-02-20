## C9.2.229 SQCVT (four registers)

Multi-vector signed saturating extract narrow

This instruction saturates the signed integer value in each element of the four source vectors to quarter the original source element width, and places the results in the quarter-width destination elements.

This instruction is unpredicated.

## SME2

(FEAT\_SME2)

<!-- image -->

## Encoding

```
SQCVT <Zd>.<T>, { <Zn1>.<Tb>-<Zn4>.<Tb> }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then constant integer esize = 8 << UInt(sz); constant integer n = UInt(Zn:'00'); constant integer d = UInt(Zd);
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'sz':

## &lt;Zn1&gt;

Is the name of the first scalable vector register of the source multi-vector group, encoded as 'Zn' times 4.

## &lt;Tb&gt;

```
EndOfDecode(Decode_UNDEF);
```

&lt;T&gt;

Is the size specifier, encoded in 'sz':

|   sz | <T>   |
|------|-------|
|    0 | B     |
|    1 | H     |

## &lt;Zn4&gt;

Is the name of the fourth scalable vector register of the source multi-vector group, encoded as 'Zn' times 4 plus 3.

## Operation

```
CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV (4 * esize); bits(VL) result; for r = 0 to 3 constant bits(VL) operand = Z[n+r, VL]; for e = 0 to elements-1 constant integer element = SInt(Elem[operand, e, 4 * esize]); Elem[result, r*elements + e, esize] = SignedSat(element, esize); Z[d, VL] = result;
```

|   sz | <Tb>   |
|------|--------|
|    0 | S      |
|    1 | D      |