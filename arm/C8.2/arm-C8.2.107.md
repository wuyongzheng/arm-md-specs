## C8.2.107 CMP&lt;cc&gt; (wide elements)

Compare vector to 64-bit wide elements

This instruction compares active integer elements in the first source vector with overlapping 64-bit doubleword elements in the second source vector, and places the boolean results of the specified comparison in the corresponding elements of the destination predicate. Inactive elements in the destination predicate register are set to zero. This instruction sets the First (N), None (Z), and !Last (C) condition flags based on the predicate result, and sets the V flag to zero.

| <cc>   | Comparison                   |
|--------|------------------------------|
| EQ     | equal                        |
| GE     | signed greater than or equal |
| GT     | signed greater than          |
| HI     | unsigned higher than         |
| HS     | unsigned higher than or same |
| LE     | signed less than or equal    |
| LO     | unsigned lower than          |
| LS     | unsigned lower than or same  |
| LT     | signed less than             |
| NE     | not equal                    |

It has encodings from 10 classes: Equal, Greater than, Greater than or equal, Higher, Higher or same, Less than, Less than or equal, Lower, Lower or same, and Not equal

## Equal

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
CMPEQ <Pd>.<T>, <Pg>/Z, <Zn>.<T>, <Zm>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '11' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Pd); constant CmpOp cmp_op = Cmp_EQ; constant boolean unsigned = FALSE;
```

## Greater than

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
CMPGT <Pd>.<T>, <Pg>/Z, <Zn>.<T>, <Zm>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '11' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Pd); constant CmpOp cmp_op = Cmp_GT; constant boolean unsigned = FALSE;
```

## Greater than or equal

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
CMPGE <Pd>.<T>, <Pg>/Z, <Zn>.<T>, <Zm>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '11' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Pd); constant CmpOp cmp_op = Cmp_GE; constant boolean unsigned = FALSE;
```

## Higher

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
CMPHI <Pd>.<T>, <Pg>/Z, <Zn>.<T>, <Zm>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '11' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Pd); constant CmpOp cmp_op = Cmp_GT; constant boolean unsigned = TRUE;
```

## Higher or same

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
CMPHS <Pd>.<T>, <Pg>/Z, <Zn>.<T>, <Zm>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '11' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Pd); constant CmpOp cmp_op = Cmp_GE; constant boolean unsigned = TRUE;
```

## Less than

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
CMPLT <Pd>.<T>, <Pg>/Z, <Zn>.<T>, <Zm>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '11' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Pd); constant CmpOp cmp_op = Cmp_LT; constant boolean unsigned = FALSE;
```

## Less than or equal

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
CMPLE <Pd>.<T>, <Pg>/Z, <Zn>.<T>, <Zm>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '11' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Pd); constant CmpOp cmp_op = Cmp_LE; constant boolean unsigned = FALSE;
```

## Lower

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
CMPLO <Pd>.<T>, <Pg>/Z, <Zn>.<T>, <Zm>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '11' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Pd); constant CmpOp cmp_op = Cmp_LT; constant boolean unsigned = TRUE;
```

## Lower or same

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
CMPLS <Pd>.<T>, <Pg>/Z, <Zn>.<T>, <Zm>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '11' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Pd); constant CmpOp cmp_op = Cmp_LE; constant boolean unsigned = TRUE;
```

## Not equal

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
CMPNE <Pd>.<T>, <Pg>/Z, <Zn>.<T>, <Zm>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '11' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Pd); constant CmpOp cmp_op = Cmp_NE; constant boolean unsigned = FALSE;
```

## Assembler Symbols

&lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

Is the size specifier, encoded in 'size':

<!-- image -->

&lt;Pg&gt;

&lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

&lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

|   size | <T>      |
|--------|----------|
|     00 | B        |
|     01 | H        |
|     10 | S        |
|     11 | RESERVED |

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand1 = if AnyActiveElement(mask, esize) then Z[n, VL] else Zeros(VL); constant bits(VL) operand2 = if AnyActiveElement(mask, esize) then Z[m, VL] else Zeros(VL); bits(PL) result; constant integer psize = esize DIV 8; for e = 0 to elements-1 constant bits(esize) op1elt = Elem[operand1, e, esize]; constant integer element1 = if unsigned then UInt(op1elt) else SInt(op1elt); if ActivePredicateElement(mask, e, esize) then boolean cond; constant bits(64) op2elt = Elem[operand2, (e * esize) DIV 64, 64]; constant integer element2 = if unsigned then UInt(op2elt) else SInt(op2elt); case cmp_op of when Cmp_EQ cond = element1 == element2; when Cmp_NE cond = element1 != element2; when Cmp_GE cond = element1 >= element2; when Cmp_LT cond = element1 < element2; when Cmp_GT cond = element1 > element2; when Cmp_LE cond = element1 <= element2; constant bit pbit = if cond then '1' else '0'; Elem[result, e, psize] = ZeroExtend(pbit, psize); else Elem[result, e, psize] = ZeroExtend('0', psize); PSTATE.<N,Z,C,V> = PredTest(mask, result, esize); P[d, PL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

If FEAT\_SME is implemented and the PE is in Streaming SVE mode, then any subsequent instruction which is dependent on the predicate register or NZCV condition flags written by this instruction might be significantly delayed.