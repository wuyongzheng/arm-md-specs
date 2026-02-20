## C8.2.165 FCM&lt;cc&gt; (zero)

Floating-point compare with zero

This instruction compares active floating-point elements in the source vector with zero, and places the boolean results of the specified comparison in the corresponding elements of the destination predicate. Inactive elements in the destination predicate register are set to zero. This instruction does not set the condition flags.

| <cc>   | Comparison            |
|--------|-----------------------|
| EQ     | equal                 |
| GE     | greater than or equal |
| GT     | greater than          |
| LE     | less than or equal    |
| LT     | less than             |
| NE     | not equal             |
| UO     | unordered             |

It has encodings from 6 classes: Equal, Greater than, Greater than or equal, Less than, Less than or equal, and Not equal

## Equal

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FCMEQ <Pd>.<T>, <Pg>/Z, <Zn>.<T>, #0.0
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Pd); constant CmpOp op = Cmp_EQ;
```

## Greater than

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FCMGT <Pd>.<T>, <Pg>/Z, <Zn>.<T>, #0.0
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Pd); constant CmpOp op = Cmp_GT;
```

## Greater than or equal

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FCMGE <Pd>.<T>, <Pg>/Z, <Zn>.<T>, #0.0
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Pd); constant CmpOp op = Cmp_GE;
```

## Less than

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FCMLT <Pd>.<T>, <Pg>/Z, <Zn>.<T>, #0.0
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Pd); constant CmpOp op = Cmp_LT;
```

<!-- image -->

<!-- image -->

```
Less than or equal (FEAT_SVE || FEAT_SME) 0 1 1 31 29 0 0 1 0 28 25 1 24 size 23 22 0 1 0 21 19 0 18 0 17 1 16 0 0 1 15 13 Pg 12 10 Zn 9 5 1 4 Pd 3 0 eq lt ne Encoding FCMLE <Pd>.<T>, <Pg>/Z, <Zn>.<T>, #0.0 Decode for this encoding if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Pd); constant CmpOp op = Cmp_LE; Not equal (FEAT_SVE || FEAT_SME) 0 1 1 31 29 0 0 1 0 28 25 1 24 size 23 22 0 1 0 21 19 0 18 1 17 1 16 0 0 1 15 13 Pg 12 10 Zn 9 5 0 4 Pd 3 0 eq lt ne Encoding FCMNE <Pd>.<T>, <Pg>/Z, <Zn>.<T>, #0.0 Decode for this encoding
```

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Pd); constant CmpOp op = Cmp_NE;
```

## Assembler Symbols

&lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

Is the size specifier, encoded in 'size':

&lt;T&gt;

&lt;Pg&gt;

&lt;Zn&gt;

Is the name of the source scalable vector register, encoded in the 'Zn' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand = if AnyActiveElement(mask, esize) then Z[n, VL] else Zeros(VL); bits(PL) result; constant integer psize = esize DIV 8; for e = 0 to elements-1 if ActivePredicateElement(mask, e, esize) then constant bits(esize) element = Elem[operand, e, esize]; boolean res; case op of when Cmp_EQ res = FPCompareEQ(element, 0<esize-1:0>, FPCR); when Cmp_GE res = FPCompareGE(element, 0<esize-1:0>, FPCR); when Cmp_GT res = FPCompareGT(element, 0<esize-1:0>, FPCR); when Cmp_NE res = FPCompareNE(element, 0<esize-1:0>, FPCR); when Cmp_LT res = FPCompareGT(0<esize-1:0>, element, FPCR); when Cmp_LE res = FPCompareGE(0<esize-1:0>, element, FPCR); constant bit pbit = if res then '1' else '0'; Elem[result, e, psize] = ZeroExtend(pbit, psize); else Elem[result, e, psize] = ZeroExtend('0', psize); P[d, PL] = result;
```

## Operational Information

If FEAT\_SME is implemented and the PE is in Streaming SVE mode, then any subsequent instruction which is dependent on the predicate register written by this instruction might be significantly delayed.

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.