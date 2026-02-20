## C8.2.925 WHILELS (predicate)

While incrementing unsigned scalar lower than or same as scalar

This instruction generates a predicate that starting from the lowest numbered element is true while the incrementing value of the first, unsigned scalar operand is lower than or the same as the second scalar operand and false thereafter up to the highest numbered element.

If the second scalar operand is equal to the maximum unsigned integer value, then a condition that includes an equality test can never fail and the result will be an all-true predicate.

The full width of the scalar operands is significant for the purposes of comparison, and the full width first operand is incremented by one for each destination predicate element, irrespective of the predicate result element size. The first general-purpose source register is not itself updated.

The predicate result is placed in the predicate destination register. This instruction sets the First (N), None (Z), and !Last (C) condition flags based on the predicate result, and sets the V flag to zero.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
WHILELS <Pd>.<T>, <R><n>, <R><m>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer rsize = 32 << UInt(sf); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer d = UInt(Pd); constant boolean unsigned = TRUE; constant CmpOp op = Cmp_LE;
```

## Assembler Symbols

## &lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

Is the size specifier, encoded in 'size':

<!-- image -->

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |

&lt;R&gt;

&lt;n&gt;

&lt;m&gt;

Is the number [0-30] of the source general-purpose register or the name ZR (31), encoded in the 'Rm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = Ones(PL); bits(rsize) operand1 = X[n, rsize]; constant bits(rsize) operand2 = X[m, rsize]; bits(PL) result; boolean last = TRUE; constant integer psize = esize DIV 8; constant integer element2 = if unsigned then UInt(operand2) else SInt(operand2); for e = 0 to elements-1 constant integer element1 = if unsigned then UInt(operand1) else SInt(operand1); boolean cond; case op of when Cmp_LT cond = (element1 < element2); when Cmp_LE cond = (element1 <= element2); last = last && cond; constant bit pbit = if last then '1' else '0'; Elem[result, e, psize] = ZeroExtend(pbit, psize); operand1 = operand1 + 1; PSTATE.<N,Z,C,V> = PredTest(mask, result, esize); P[d, PL] = result;
```

Is a width specifier, encoded in 'sf':

|   size | <T>   |
|--------|-------|
|     11 | D     |

|   sf | <R>   |
|------|-------|
|    0 | W     |
|    1 | X     |

Is the number [0-30] of the source general-purpose register or the name ZR (31), encoded in the 'Rn' field.