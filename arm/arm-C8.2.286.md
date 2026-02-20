## C8.2.286 INDEX (scalar, immediate)

Create index starting from general-purpose register and incremented by immediate

This instruction populates the destination vector by setting the first element to the first signed scalar integer operand and monotonically incrementing the value by the second signed immediate integer operand for each subsequent element. The scalar source operand is a general-purpose register in which only the least significant bits corresponding to the vector element size are used and any remaining bits are ignored. This instruction is unpredicated.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
INDEX <Zd>.<T>, <R><n>, #<imm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Rn); constant integer d = UInt(Zd); constant integer imm = SInt(imm5);
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

Is a width specifier, encoded in 'size':

<!-- image -->

&lt;R&gt;

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

&lt;n&gt;

Is the number [0-30] of the source general-purpose register or the name ZR (31), encoded in the 'Rn' field.

## &lt;imm&gt;

Is the signed immediate operand, in the range -16 to 15, encoded in the 'imm5' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(esize) operand1 = X[n, esize]; constant integer element1 = SInt(operand1); bits(VL) result; for e = 0 to elements-1 constant integer index = element1 + e * imm; Elem[result, e, esize] = index<esize-1:0>; Z[d, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

|   size | <R>   |
|--------|-------|
|     00 | W     |
|     01 | W     |
|     10 | W     |
|     11 | X     |