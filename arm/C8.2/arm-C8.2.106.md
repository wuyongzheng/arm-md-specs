## C8.2.106 CMP&lt;cc&gt; (immediate)

Compare vector to immediate

This instruction compares active integer elements in the source vector with an immediate, and places the boolean results of the specified comparison in the corresponding elements of the destination predicate. Inactive elements in the destination predicate register are set to zero. This instruction sets the First (N), None (Z), and !Last (C) condition flags based on the predicate result, and sets the V flag to zero.

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
CMPEQ <Pd>.<T>, <Pg>/Z, <Zn>.<T>, #<imm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Pd); constant CmpOp cmp_op = Cmp_EQ; constant integer imm = SInt(imm5); constant boolean unsigned = FALSE;
```

## Greater than

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
CMPGT <Pd>.<T>, <Pg>/Z, <Zn>.<T>, #<imm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Pd); constant CmpOp cmp_op = Cmp_GT; constant integer imm = SInt(imm5); constant boolean unsigned = FALSE;
```

## Greater than or equal

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
CMPGE <Pd>.<T>, <Pg>/Z, <Zn>.<T>, #<imm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Pd); constant CmpOp cmp_op = Cmp_GE; constant integer imm = SInt(imm5); constant boolean unsigned = FALSE;
```

## Higher

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
CMPHI <Pd>.<T>, <Pg>/Z, <Zn>.<T>, #<imm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Pd); constant CmpOp cmp_op = Cmp_GT; constant integer imm = UInt(imm7); constant boolean unsigned = TRUE;
```

## Higher or same

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
CMPHS <Pd>.<T>, <Pg>/Z, <Zn>.<T>, #<imm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Pd); constant CmpOp cmp_op = Cmp_GE; constant integer imm = UInt(imm7); constant boolean unsigned = TRUE;
```

## Less than

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
CMPLT <Pd>.<T>, <Pg>/Z, <Zn>.<T>, #<imm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Pd); constant CmpOp cmp_op = Cmp_LT; constant integer imm = SInt(imm5); constant boolean unsigned = FALSE;
```

## Less than or equal

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
CMPLE <Pd>.<T>, <Pg>/Z, <Zn>.<T>, #<imm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Pd); constant CmpOp cmp_op = Cmp_LE; constant integer imm = SInt(imm5); constant boolean unsigned = FALSE;
```

## Lower

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
CMPLO <Pd>.<T>, <Pg>/Z, <Zn>.<T>, #<imm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Pd); constant CmpOp cmp_op = Cmp_LT; constant integer imm = UInt(imm7); constant boolean unsigned = TRUE;
```

## Lower or same

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
CMPLS <Pd>.<T>, <Pg>/Z, <Zn>.<T>, #<imm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Pd); constant CmpOp cmp_op = Cmp_LE; constant integer imm = UInt(imm7); constant boolean unsigned = TRUE;
```

## Not equal

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
CMPNE <Pd>.<T>, <Pg>/Z, <Zn>.<T>, #<imm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Pd); constant CmpOp cmp_op = Cmp_NE; constant integer imm = SInt(imm5); constant boolean unsigned = FALSE;
```

## Assembler Symbols

## &lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

Is the size specifier, encoded in 'size':

<!-- image -->

<!-- image -->

## &lt;Zn&gt;

Is the name of the source scalable vector register, encoded in the 'Zn' field.

## &lt;imm&gt;

For the 'Equal', 'Greater than', 'Greater than or equal', 'Less than', 'Less than or equal', and 'Not equal' variants: is the signed immediate operand, in the range -16 to 15, encoded in the 'imm5' field.

For the 'Higher', 'Higher or same', 'Lower', and 'Lower or same' variants: is the unsigned immediate operand, in the range 0 to 127, encoded in the 'imm7' field.

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand1 = if AnyActiveElement(mask, esize) then Z[n, VL] else Zeros(VL); bits(PL) result; constant integer psize = esize DIV 8; for e = 0 to elements-1 constant bits(esize) op1elt = Elem[operand1, e, esize]; constant integer element1 = if unsigned then UInt(op1elt) else SInt(op1elt); if ActivePredicateElement(mask, e, esize) then boolean cond; case cmp_op of when Cmp_EQ cond = element1 == imm; when Cmp_NE cond = element1 != imm; when Cmp_GE cond = element1 >= imm; when Cmp_LT cond = element1 < imm; when Cmp_GT cond = element1 > imm; when Cmp_LE cond = element1 <= imm; constant bit pbit = if cond then '1' else '0'; Elem[result, e, psize] = ZeroExtend(pbit, psize); else Elem[result, e, psize] = ZeroExtend('0', psize); PSTATE.<N,Z,C,V> = PredTest(mask, result, esize); P[d, PL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

If FEAT\_SME is implemented and the PE is in Streaming SVE mode, then any subsequent instruction which is dependent on the predicate register or NZCV condition flags written by this instruction might be significantly delayed.