## C8.2.927 WHILELS (predicate pair)

While incrementing unsigned scalar lower than or same as scalar (pair of predicates)

This instruction generates a pair of predicates that starting from the lowest numbered element of the pair is true while the incrementing value of the first, unsigned scalar operand is lower than or the same as the second scalar operand and false thereafter up to the highest numbered element of the pair.

If the second scalar operand is equal to the maximum unsigned integer value, then a condition that includes an equality test can never fail and the result will be an all-true predicate.

The full width of the scalar operands is significant for the purposes of comparison, and the full width first operand is incremented by one for each destination predicate element, irrespective of the predicate result element size. The first general-purpose source register is not itself updated.

The lower-numbered elements are placed in the first predicate destination register, and the higher-numbered elements in the second predicate destination register. This instruction sets the First (N), None (Z), and !Last (C) condition flags based on the predicate result, and sets the V flag to zero.

## SVE2

(FEAT\_SME2 || FEAT\_SVE2p1)

<!-- image -->

## Encoding

```
WHILELS { <Pd1>.<T>, <Pd2>.<T> }, <Xn>, <Xm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) && !IsFeatureImplemented(FEAT_SVE2p1) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer rsize = 64; constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer d0 = UInt(Pd:'0'); constant integer d1 = UInt(Pd:'1'); constant boolean unsigned = TRUE; constant CmpOp op = Cmp_LE;
```

## Assembler Symbols

## &lt;Pd1&gt;

Is the name of the first destination scalable predicate register, encoded as 'Pd' times 2.

&lt;T&gt;

Is the size specifier, encoded in 'size':

|   size | <T>   |
|--------|-------|
|     00 | B     |

## &lt;Pd2&gt;

Is the name of the second destination scalable predicate register, encoded as 'Pd' times 2 plus 1.

&lt;Xn&gt;

Is the 64-bit name of the first source general-purpose register, encoded in the 'Rn' field.

## &lt;Xm&gt;

Is the 64-bit name of the second source general-purpose register, encoded in the 'Rm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL*2) mask = Ones(PL*2); bits(rsize) operand1 = X[n, rsize]; constant bits(rsize) operand2 = X[m, rsize]; bits(PL*2) result; boolean last = TRUE; constant integer psize = esize DIV 8; constant integer element2 = if unsigned then UInt(operand2) else SInt(operand2); for e = 0 to (elements*2)-1 constant integer element1 = if unsigned then UInt(operand1) else SInt(operand1); boolean cond; case op of when Cmp_LT cond = (element1 < element2); when Cmp_LE cond = (element1 <= element2); last = last && cond; constant bit pbit = if last then '1' else '0'; Elem[result, e, psize] = ZeroExtend(pbit, psize); operand1 = operand1 + 1; PSTATE.<N,Z,C,V> = PredTest(mask, result, esize); P[d0, PL] = result<PL-1:0>; P[d1, PL] = result<PL*2-1:PL>;
```

|   size | <T>   |
|--------|-------|
|     01 | H     |
|     10 | S     |
|     11 | D     |