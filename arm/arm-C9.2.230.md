## C9.2.230 SQCVTN

Multi-vector signed saturating extract narrow to interleaved integer

This instruction saturates the signed integer value in each element of the four source vectors to quarter the original source element width, and places the four-way interleaved results in the quarter-width destination elements.

This instruction is unpredicated.

## SME2

(FEAT\_SME2)

<!-- image -->

## Encoding

SQCVTN

&lt;Zd&gt;.&lt;T&gt;, {

&lt;Zn1&gt;.&lt;Tb&gt;-&lt;Zn4&gt;.&lt;Tb&gt;

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

&lt;T&gt;

Is the size specifier, encoded in 'sz':

}

```
EndOfDecode(Decode_UNDEF);
```

|   sz | <T>   |
|------|-------|
|    0 | B     |
|    1 | H     |

## &lt;Zn4&gt;

Is the name of the fourth scalable vector register of the source multi-vector group, encoded as 'Zn' times 4 plus 3.

## Operation

```
CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV (4 * esize); bits(VL) result; for e = 0 to elements-1 for i = 0 to 3 constant bits(VL) operand = Z[n+i, VL]; constant integer element = SInt(Elem[operand, e, 4 * Elem[result, 4*e + i, esize] = SignedSat(element, esize); Z[d, VL] = result;
```

|   sz | <Tb>   |
|------|--------|
|    0 | S      |
|    1 | D      |

```
esize]);
```