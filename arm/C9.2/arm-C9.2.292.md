## C9.2.292 UDOT (4-way, multiple vectors)

Multi-vector unsigned integer dot product

This instruction computes the dot product of four unsigned 8-bit or 16-bit integer values held in each 32-bit or 64-bit element of the two or four first source vectors and four unsigned 8-bit or 16-bit integer values in the corresponding 32-bit or 64-bit element of the two or four second source vectors. The widened dot product result is destructively added to the corresponding 32-bit or 64-bit element of the ZA single-vector groups.

The single-vector group within each half of or each quarter of the ZA array is selected by the sum of the vector select register and offset, modulo half or quarter the number of ZA array vectors.

The vector group symbol, VGx2 or VGx4 , indicates that the ZA operand consists of two or four ZA single-vector groups respectively. The vector group symbol is preferred for disassembly, but optional in assembler source code.

This instruction is unpredicated.

ID\_AA64SMFR0\_EL1.I16I64 indicates whether the 16-bit integer variant is implemented.

It has encodings from 2 classes: Two ZA single-vectors and Four ZA single-vectors

## Two ZA single-vectors

(FEAT\_SME2)

<!-- image -->

## Encoding

```
UDOT ZA.<T>[<Wv>, <offs>{, VGx2}], { <Zn1>.<Tb>-<Zn2>.<Tb> }, { <Zm1>.<Tb>-<Zm2>.<Tb> }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); if sz == '1' && !IsFeatureImplemented(FEAT_SME_I16I64) then EndOfDecode(Decode_UNDEF); constant integer v = UInt('010':Rv); constant integer esize = 32 << UInt(sz); constant integer n = UInt(Zn:'0'); constant integer m = UInt(Zm:'0'); constant integer offset = UInt(off3); constant integer nreg = 2;
```

## Four ZA single-vectors

(FEAT\_SME2)

<!-- image -->

## Encoding

```
UDOT ZA.<T>[<Wv>, <offs>{, VGx4}], { <Zn1>.<Tb>-<Zn4>.<Tb> }, { <Zm1>.<Tb>-<Zm4>.<Tb> }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); if sz == '1' && !IsFeatureImplemented(FEAT_SME_I16I64) then EndOfDecode(Decode_UNDEF); constant integer v = UInt('010':Rv); constant integer esize = 32 << UInt(sz); constant integer n = UInt(Zn:'00'); constant integer m = UInt(Zm:'00'); constant integer offset = UInt(off3); constant integer nreg = 4;
```

## Assembler Symbols

## &lt;T&gt;

Is the size specifier, encoded in 'sz':

## &lt;Wv&gt;

Is the 32-bit name of the vector select register W8-W11, encoded in the 'Rv' field.

## &lt;offs&gt;

Is the vector select offset, in the range 0 to 7, encoded in the 'off3' field.

## &lt;Zn1&gt;

For the 'Two ZA single-vectors' variant: is the name of the first scalable vector register of the first source multi-vector group, encoded as 'Zn' times 2.

For the 'Four ZA single-vectors' variant: is the name of the first scalable vector register of the first source multi-vector group, encoded as 'Zn' times 4.

Is the size specifier, encoded in 'sz':

## &lt;Zn2&gt;

Is the name of the second scalable vector register of the first source multi-vector group, encoded as 'Zn' times 2 plus 1.

## &lt;Zm1&gt;

For the 'Two ZA single-vectors' variant: is the name of the first scalable vector register of the second source multi-vector group, encoded as 'Zm' times 2.

For the 'Four ZA single-vectors' variant: is the name of the first scalable vector register of the second source multi-vector group, encoded as 'Zm' times 4.

## &lt;Tb&gt;

|   sz | <T>   |
|------|-------|
|    0 | S     |
|    1 | D     |

|   sz | <Tb>   |
|------|--------|
|    0 | B      |
|    1 | H      |

## &lt;Zm2&gt;

Is the name of the second scalable vector register of the second source multi-vector group, encoded as 'Zm' times 2 plus 1.

## &lt;Zn4&gt;

Is the name of the fourth scalable vector register of the first source multi-vector group, encoded as 'Zn' times 4 plus 3.

## &lt;Zm4&gt;

Is the name of the fourth scalable vector register of the second source multi-vector group, encoded as 'Zm' times 4 plus 3.

## Operation

```
CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant integer vectors = VL DIV 8; constant integer vstride = vectors DIV nreg; constant bits(32) vbase = X[v, 32]; integer vec = (UInt(vbase) + offset) MOD vstride; bits(VL) result; for r = 0 to nreg-1 constant bits(VL) operand1 = Z[n+r, VL]; constant bits(VL) operand2 = Z[m+r, VL]; constant bits(VL) operand3 = ZAvector[vec, VL]; for e = 0 to elements-1 bits(esize) sum = Elem[operand3, e, esize]; for i = 0 to 3 constant integer element1 = UInt(Elem[operand1, 4 * e + i, esize DIV 4]); constant integer element2 = UInt(Elem[operand2, 4 * e + i, esize DIV 4]); sum = sum + element1 * element2; Elem[result, e, esize] = sum; ZAvector[vec, VL] = result; vec = vec + vstride;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.