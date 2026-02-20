## C9.2.270 SUB (to array, multiple and single vector)

Multi-vector subtract by vector to ZA array vectors

This instruction subtracts all the corresponding elements of the second source vector from the two or four first source vectors and places the results in the corresponding elements of the ZA single-vector groups.

The single-vector group within each half of or each quarter of the ZA array is selected by the sum of the vector select register and offset, modulo half or quarter the number of ZA array vectors.

The vector group symbol, VGx2 or VGx4 , indicates that the ZA operand consists of two or four ZA single-vector groups respectively. The vector group symbol is preferred for disassembly, but optional in assembler source code.

This instruction is unpredicated.

ID\_AA64SMFR0\_EL1.I16I64 indicates whether the 64-bit integer variant is implemented.

It has encodings from 2 classes: Two ZA single-vectors and Four ZA single-vectors

```
Two ZA single-vectors (FEAT_SME2)
```

<!-- image -->

## Encoding

```
SUB ZA.<T>[<Wv>, <offs>{, VGx2}], { <Zn1>.<T>-<Zn2>.<T> },
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); if sz == '1' && !IsFeatureImplemented(FEAT_SME_I16I64) then EndOfDecode(Decode_UNDEF); constant integer v = UInt('010':Rv); constant integer esize = 32 << UInt(sz); constant integer n = UInt(Zn); constant integer m = UInt('0':Zm); constant integer offset = UInt(off3); constant integer nreg = 2;
```

## Four ZA single-vectors

(FEAT\_SME2)

<!-- image -->

## Encoding

```
SUB ZA.<T>[<Wv>, <offs>{, VGx4}], { <Zn1>.<T>-<Zn4>.<T> },
```

```
<Zm>.<T>
```

```
<Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); if sz == '1' && !IsFeatureImplemented(FEAT_SME_I16I64) then EndOfDecode(Decode_UNDEF); constant integer v = UInt('010':Rv); constant integer esize = 32 << UInt(sz); constant integer n = UInt(Zn); constant integer m = UInt('0':Zm); constant integer offset = UInt(off3); constant integer nreg = 4;
```

## Assembler Symbols

## &lt;T&gt;

Is the size specifier, encoded in 'sz':

## &lt;Wv&gt;

Is the 32-bit name of the vector select register W8-W11, encoded in the 'Rv' field.

## &lt;offs&gt;

Is the vector select offset, in the range 0 to 7, encoded in the 'off3' field.

## &lt;Zn1&gt;

Is the name of the first scalable vector register of the first source multi-vector group, encoded as 'Zn'.

## &lt;Zn2&gt;

Is the name of the second scalable vector register of the first source multi-vector group, encoded as 'Zn' plus 1 modulo 32.

## &lt;Zm&gt;

Is the name of the second source scalable vector register Z0-Z15, encoded in the 'Zm' field.

## &lt;Zn4&gt;

Is the name of the fourth scalable vector register of the first source multi-vector group, encoded as 'Zn' plus 3 modulo 32.

## Operation

```
CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant integer vectors = VL DIV 8; constant integer vstride = vectors DIV nreg; constant bits(32) vbase = X[v, 32]; integer vec = (UInt(vbase) + offset) MOD vstride; bits(VL) result; for r = 0 to nreg-1 constant bits(VL) operand1 = Z[(n+r) MOD 32, constant bits(VL) operand2 = Z[m, VL];
```

|   sz | <T>   |
|------|-------|
|    0 | S     |
|    1 | D     |

```
VL];
```

```
for e = 0 to elements-1 constant bits(esize) element1 = Elem[operand1, e, esize]; constant bits(esize) element2 = Elem[operand2, e, esize]; Elem[result, e, esize] = element1 - element2; ZAvector[vec, VL] = result; vec = vec + vstride;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.