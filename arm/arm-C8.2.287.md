## C8.2.287 INDEX (scalars)

Create index starting from and incremented by general-purpose register

This instruction populates the destination vector by setting the first element to the first signed scalar integer operand and monotonically incrementing the value by the second signed scalar integer operand for each subsequent element. The scalar source operands are general-purpose registers in which only the least significant bits corresponding to the vector element size are used and any remaining bits are ignored. This instruction is unpredicated.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
INDEX <Zd>.<T>, <R><n>, <R><m>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer d = UInt(Zd);
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

&lt;m&gt;

Is the number [0-30] of the source general-purpose register or the name ZR (31), encoded in the 'Rm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(esize) operand1 = X[n, esize]; constant integer element1 = SInt(operand1); constant bits(esize) operand2 = X[m, esize]; constant integer element2 = SInt(operand2); bits(VL) result; for e = 0 to elements-1 constant integer index = element1 + e * element2; Elem[result, e, esize] = index<esize-1:0>; Z[d, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

|   size | <R>   |
|--------|-------|
|     00 | W     |
|     01 | W     |
|     10 | W     |
|     11 | X     |

Is the number [0-30] of the source general-purpose register or the name ZR (31), encoded in the 'Rn' field.