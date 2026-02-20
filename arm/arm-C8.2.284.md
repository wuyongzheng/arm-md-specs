## C8.2.284 INDEX (immediates)

Create index starting from and incremented by immediate

This instruction populates the destination vector by setting the first element to the first signed immediate integer operand and monotonically incrementing the value by the second signed immediate integer operand for each subsequent element. This instruction is unpredicated.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
INDEX <Zd>.<T>, #<imm1>, #<imm2>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer d = UInt(Zd); constant integer imm1 = SInt(imm5); constant integer imm2 = SInt(imm5b);
```

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

## &lt;imm1&gt;

Is the first signed immediate operand, in the range -16 to 15, encoded in the 'imm5' field.

## &lt;imm2&gt;

Is the second signed immediate operand, in the range -16 to 15, encoded in the 'imm5b' field.

<!-- image -->

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; bits(VL) result; for e = 0 to elements-1 constant integer index = imm1 + e * imm2; Elem[result, e, esize] = index<esize-1:0>; Z[d, VL] = result;
```