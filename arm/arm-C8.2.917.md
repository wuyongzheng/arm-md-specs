## C8.2.917 WHILEHS (predicate as counter)

While decrementing unsigned scalar higher than or same as scalar (predicate-as-counter)

This instruction generates a predicate for a group of two or four vectors that starting from the highest numbered element of the group is true while the decrementing value of the first, unsigned scalar operand is higher than or the same as the second scalar operand and false thereafter down to the lowest numbered element of the group.

If the second scalar operand is equal to the minimum unsigned integer value, then a condition that includes an equality test can never fail and the result will be an all-true predicate.

The full width of the scalar operands is significant for the purposes of comparison, and the full width first operand is decremented by one for each destination predicate element, irrespective of the predicate result element size.

The predicate result is placed in the predicate destination register using the predicate-as-counter encoding. This instruction sets the First (N), None (Z), and !Last (C) condition flags based on the predicate result, and sets the V flag to zero.

## SVE2

(FEAT\_SME2 || FEAT\_SVE2p1)

<!-- image -->

## Encoding

```
WHILEHS <PNd>.<T>, <Xn>, <Xm>, <vl>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) && !IsFeatureImplemented(FEAT_SVE2p1) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer rsize = 64; constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer d = UInt('1':PNd); constant boolean unsigned = TRUE; constant boolean invert = TRUE; constant CmpOp op = Cmp_GE; constant integer width = 2 << UInt(vl);
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
if IsFeatureImplemented(FEAT_SVE2p1) then CheckSVEEnabled(); else CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = width * (VL DIV esize); bits(rsize) operand1 = X[n, rsize]; constant bits(rsize) operand2 = X[m, rsize]; bits(PL) result; boolean last = TRUE; integer count = 0; constant integer element2 = if unsigned then UInt(operand2) else SInt(operand2); for e = elements-1 downto 0 boolean cond; constant integer element1 = if unsigned then UInt(operand1) else SInt(operand1); case op of when Cmp_GT cond = (element1 > element2); when Cmp_GE cond = (element1 >= element2); last = last && cond; if last then count = count + 1; operand1 = operand1 - 1; result = EncodePredCount(esize, elements, count, invert, PL); PSTATE.<N,Z,C,V> = PredCountTest(elements, count, invert); P[d, PL] = result;
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