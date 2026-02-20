## C8.2.285 INDEX (immediate, scalar)

Create index starting from immediate and incremented by general-purpose register

This instruction populates the destination vector by setting the first element to the first signed immediate integer operand and monotonically incrementing the value by the second signed scalar integer operand for each subsequent element. The scalar source operand is a general-purpose register in which only the least significant bits corresponding to the vector element size are used and any remaining bits are ignored. This instruction is unpredicated.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
INDEX <Zd>.<T>, #<imm>, <R><m>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer m = UInt(Rm); constant integer d = UInt(Zd); constant integer imm = SInt(imm5);
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

## &lt;imm&gt;

Is the signed immediate operand, in the range -16 to 15, encoded in the 'imm5' field.

<!-- image -->

&lt;R&gt;

<!-- image -->

Is a width specifier, encoded in 'size':

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

&lt;m&gt;

Is the number [0-30] of the source general-purpose register or the name ZR (31), encoded in the 'Rm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(esize) operand2 = X[m, esize]; constant integer element2 = SInt(operand2); bits(VL) result; for e = 0 to elements-1 constant integer index = imm + e * element2; Elem[result, e, esize] = index<esize-1:0>; Z[d, VL] = result;
```

|   size | <R>   |
|--------|-------|
|     00 | W     |
|     01 | W     |
|     10 | W     |
|     11 | X     |