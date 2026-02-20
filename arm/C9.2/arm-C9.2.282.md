## C9.2.282 SUVDOT

Multi-vector signed by unsigned 8-bit integer vertical dot product by indexed element to 32-bit integer

This instruction computes the vertical dot product of the corresponding signed 8-bit elements from the four first source vectors and four unsigned 8-bit integer values in the corresponding indexed 32-bit element of the second source vector. The widened dot product result is destructively added to the corresponding 32-bit element of the ZA single-vector groups.

The groups within the second source vector are specified using an immediate element index that selects the same group position within each 128-bit vector segment. The index range is from 0 to 3.

The single-vector group within each quarter of the ZA array is selected by the sum of the vector select register and offset, modulo quarter the number of ZA array vectors.

The vector group symbol VGx4 indicates that the ZA operand consists of four ZA single-vector groups. The vector group symbol is preferred for disassembly, but optional in assembler source code.

This instruction is unpredicated.

## SME2

(FEAT\_SME2)

<!-- image -->

## Encoding

```
SUVDOT ZA.S[<Wv>, <offs>{, VGx4}], { <Zn1>.B-<Zn4>.B },
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); constant integer v = UInt('010':Rv); constant integer esize = 32; constant integer n = UInt(Zn:'00'); constant integer m = UInt('0':Zm); constant integer offset = UInt(off3); constant integer index = UInt(i2);
```

## Assembler Symbols

## &lt;Wv&gt;

Is the 32-bit name of the vector select register W8-W11, encoded in the 'Rv' field.

## &lt;offs&gt;

Is the vector select offset, in the range 0 to 7, encoded in the 'off3' field.

## &lt;Zn1&gt;

Is the name of the first scalable vector register of the first source multi-vector group, encoded as 'Zn' times 4.

## &lt;Zn4&gt;

Is the name of the fourth scalable vector register of the first source multi-vector group, encoded as 'Zn' times 4 plus 3.

```
<Zm>.B[<index>]
```

## &lt;Zm&gt;

Is the name of the second source scalable vector register Z0-Z15, encoded in the 'Zm' field.

## &lt;index&gt;

Is the immediate index of a 32-bit group of four 8-bit values within each 128-bit vector segment, in the range 0 to 3, encoded in the 'i2' field.

## Operation

```
CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant integer vectors = VL DIV 8; constant integer vstride = vectors DIV 4; constant integer eltspersegment = 128 DIV esize; constant bits(32) vbase = X[v, 32]; integer vec = (UInt(vbase) + offset) MOD vstride; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result; for r = 0 to 3 constant bits(VL) operand3 = ZAvector[vec, VL]; for e = 0 to elements-1 constant integer segmentbase = e - (e MOD eltspersegment); constant integer s = segmentbase + index; bits(esize) sum = Elem[operand3, e, esize]; for i = 0 to 3 constant bits(VL) operand1 = Z[n+i, VL]; constant integer element1 = SInt(Elem[operand1, 4 * e + r, esize DIV 4]); constant integer element2 = UInt(Elem[operand2, 4 * s + i, esize DIV 4]); sum = sum + element1 * element2; Elem[result, e, esize] = sum; ZAvector[vec, VL] = result; vec = vec + vstride;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.