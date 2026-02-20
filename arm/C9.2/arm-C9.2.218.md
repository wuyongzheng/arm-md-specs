## C9.2.218 SMLSLL (multiple and single vector)

Multi-vector signed integer multiply-subtract long long by vector

This instruction multiplies each signed 8-bit or 16-bit element in the one, two, or four first source vectors with each signed 8-bit or 16-bit element in the second source vector, widens each product to 32 bits or 64 bits, and destructively subtracts these values from the corresponding 32-bit or 64-bit elements of the ZA quad-vector groups.

The quad-vector group within all of, each half of, or each quarter of the ZA array is selected by the sum of the vector select register and offset range, modulo all, half, or quarter the number of ZA array vectors.

The vector group symbol, VGx2 or VGx4 , indicates that the ZA operand consists of two or four ZA quad-vector groups respectively. The vector group symbol is preferred for disassembly, but optional in assembler source code.

This instruction is unpredicated.

ID\_AA64SMFR0\_EL1.I16I64 indicates whether the 16-bit integer variant is implemented.

It has encodings from 3 classes: One ZA quad-vector, Two ZA quad-vectors, and Four ZA quad-vectors

## One ZA quad-vector

(FEAT\_SME2)

<!-- image -->

## Encoding

```
SMLSLL ZA.<T>[<Wv>, <offs1>:<offs4>], <Zn>.<Tb>, <Zm>.<Tb>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); if sz == '1' && !IsFeatureImplemented(FEAT_SME_I16I64) then EndOfDecode(Decode_UNDEF); constant integer esize = 32 << UInt(sz); constant integer v = UInt('010':Rv); constant integer n = UInt(Zn); constant integer m = UInt('0':Zm); constant integer offset = UInt(off2:'00'); constant integer nreg = 1;
```

## Two ZA quad-vectors

(FEAT\_SME2)

<!-- image -->

## Encoding

```
SMLSLL ZA.<T>[<Wv>, <offs1>:<offs4>{, VGx2}], { <Zn1>.<Tb>-<Zn2>.<Tb> }, <Zm>.<Tb>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); if sz == '1' && !IsFeatureImplemented(FEAT_SME_I16I64) then EndOfDecode(Decode_UNDEF); constant integer esize = 32 << UInt(sz); constant integer v = UInt('010':Rv); constant integer n = UInt(Zn); constant integer m = UInt('0':Zm); constant integer offset = UInt(o1:'00'); constant integer nreg = 2;
```

## Four ZA quad-vectors

(FEAT\_SME2)

<!-- image -->

## Encoding

```
SMLSLL ZA.<T>[<Wv>, <offs1>:<offs4>{, VGx4}], { <Zn1>.<Tb>-<Zn4>.<Tb> }, <Zm>.<Tb>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); if sz == '1' && !IsFeatureImplemented(FEAT_SME_I16I64) then EndOfDecode(Decode_UNDEF); constant integer esize = 32 << UInt(sz); constant integer v = UInt('010':Rv); constant integer n = UInt(Zn); constant integer m = UInt('0':Zm); constant integer offset = UInt(o1:'00'); constant integer nreg = 4;
```

## Assembler Symbols

&lt;T&gt;

Is the size specifier, encoded in 'sz':

## &lt;Wv&gt;

Is the 32-bit name of the vector select register W8-W11, encoded in the 'Rv' field.

## &lt;offs1&gt;

For the 'One ZA quad-vector' variant: is the first vector select offset, encoded as 'off2' field times 4.

For the 'Four ZA quad-vectors' and 'Two ZA quad-vectors' variants: is the first vector select offset, encoded as 'o1' field times 4.

|   sz | <T>   |
|------|-------|
|    0 | S     |
|    1 | D     |

## &lt;offs4&gt;

For the 'One ZA quad-vector' variant: is the fourth vector select offset, encoded as 'off2' field times 4 plus 3.

For the 'Four ZA quad-vectors' and 'Two ZA quad-vectors' variants: is the fourth vector select offset, encoded as 'o1' field times 4 plus 3.

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

Is the size specifier, encoded in 'sz':

## &lt;Zm&gt;

Is the name of the second source scalable vector register Z0-Z15, encoded in the 'Zm' field.

## &lt;Zn1&gt;

Is the name of the first scalable vector register of the first source multi-vector group, encoded as 'Zn'.

## &lt;Zn2&gt;

Is the name of the second scalable vector register of the first source multi-vector group, encoded as 'Zn' plus 1 modulo 32.

## &lt;Zn4&gt;

Is the name of the fourth scalable vector register of the first source multi-vector group, encoded as 'Zn' plus 3 modulo 32.

## Operation

```
CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant integer vectors = VL DIV 8; constant integer vstride = vectors DIV nreg; constant bits(32) vbase = X[v, 32]; integer vec = (UInt(vbase) + offset) MOD vstride; bits(VL) result; vec = vec - (vec MOD 4); for r = 0 to nreg-1 constant bits(VL) operand1 = Z[(n+r) MOD 32, VL]; constant bits(VL) operand2 = Z[m, VL]; for i = 0 to 3 constant bits(VL) operand3 = ZAvector[vec + i, VL]; for e = 0 to elements-1 constant integer element1 = SInt(Elem[operand1, 4 * e + i, esize DIV 4]); constant integer element2 = SInt(Elem[operand2, 4 * e + i, esize DIV 4]); constant bits(esize) product = (element1 * element2)<esize-1:0>; Elem[result, e, esize] = Elem[operand3, e, esize] product; ZAvector[vec + i, VL] = result; vec = vec + vstride;
```

## &lt;Zn&gt;

## &lt;Tb&gt;

|   sz | <Tb>   |
|------|--------|
|    0 | B      |
|    1 | H      |

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.