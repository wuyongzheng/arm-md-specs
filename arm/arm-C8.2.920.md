## C8.2.920 WHILELE (predicate as counter)

While incrementing signed scalar less than or equal to scalar (predicate-as-counter)

This instruction generates a predicate for a group of two or four vectors that starting from the lowest numbered element of the group is true while the incrementing value of the first, signed scalar operand is less than or equal to the second scalar operand and false thereafter up to the highest numbered element of the group.

If the second scalar operand is equal to the maximum signed integer value, then a condition that includes an equality test can never fail and the result will be an all-true predicate.

The full width of the scalar operands is significant for the purposes of comparison, and the full width first operand is incremented by one for each destination predicate element, irrespective of the predicate result element size.

The predicate result is placed in the predicate destination register using the predicate-as-counter encoding. This instruction sets the First (N), None (Z), and !Last (C) condition flags based on the predicate result, and sets the V flag to zero.

## SVE2

(FEAT\_SME2 || FEAT\_SVE2p1)

<!-- image -->

## Encoding

```
WHILELE <PNd>.<T>, <Xn>, <Xm>, <vl>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) && !IsFeatureImplemented(FEAT_SVE2p1) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer rsize = 64; constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer d = UInt('1':PNd); constant boolean unsigned = FALSE; constant boolean invert = FALSE; constant CmpOp op = Cmp_LE; constant integer width = 2 << UInt(vl);
```

## Assembler Symbols

## &lt;PNd&gt;

Is the name of the destination scalable predicate register PN8-PN15, with predicate-as-counter encoding, encoded in the 'PNd' field.

&lt;T&gt;

Is the size specifier, encoded in 'size':

&lt;Xn&gt;

Is the vl specifier, encoded in 'vl':

## Operation

```
if IsFeatureImplemented(FEAT_SVE2p1) then CheckSVEEnabled(); else CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = width * (VL DIV esize); bits(rsize) operand1 = X[n, rsize]; constant bits(rsize) operand2 = X[m, rsize]; bits(PL) result; boolean last = TRUE; integer count = 0; constant integer op2val = if unsigned then UInt(operand2) else SInt(operand2); for e = 0 to elements-1 constant integer op1val = if unsigned then UInt(operand1) else SInt(operand1); boolean cond; case op of when Cmp_LT cond = (op1val < op2val); when Cmp_LE cond = (op1val <= op2val); last = last && cond; if last then count = count + 1; operand1 = operand1 + 1; result = EncodePredCount(esize, elements, count, invert, PL); PSTATE.<N,Z,C,V> = PredCountTest(elements, count, invert); P[d, PL] = result;
```

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

Is the 64-bit name of the first source general-purpose register, encoded in the 'Rn' field.

&lt;Xm&gt;

Is the 64-bit name of the second source general-purpose register, encoded in the 'Rm' field.

&lt;vl&gt;

|   vl | <vl>   |
|------|--------|
|    0 | VLx2   |
|    1 | VLx4   |