## C8.2.151 FAC&lt;cc&gt;

Floating-point absolute compare

This instruction compares active absolute values of floating-point elements in the first source vector with the corresponding absolute values of elements in the second source vector, and places the boolean results of the specified comparison in the corresponding elements of the destination predicate. Inactive elements in the destination predicate register are set to zero. This instruction does not set the condition flags.

| <cc>   | Comparison            |
|--------|-----------------------|
| GE     | greater than or equal |
| GT     | greater than          |
| LE     | less than or equal    |
| LT     | less than             |

This instruction is used by the pseudo-instructions FACLE and FACLT.

It has encodings from 2 classes: Greater than and Greater than or equal

## Greater than

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FACGT <Pd>.<T>, <Pg>/Z, <Zn>.<T>, <Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Pd); constant CmpOp cmp_op = Cmp_GT;
```

## Greater than or equal

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FACGE <Pd>.<T>, <Pg>/Z, <Zn>.<T>, <Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Pd); constant CmpOp cmp_op = Cmp_GE;
```

## Assembler Symbols

## &lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

Is the size specifier, encoded in 'size':

&lt;T&gt;

## &lt;Pg&gt;

&lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand1 = if AnyActiveElement(mask, esize) then Z[n, VL] else Zeros(VL); constant bits(VL) operand2 = if AnyActiveElement(mask, esize) then Z[m, VL] else Zeros(VL); bits(PL) result; constant integer psize = esize DIV 8; for e = 0 to elements-1 if ActivePredicateElement(mask, e, esize) then constant bits(esize) element1 = FPAbs(Elem[operand1, e, esize], FPCR);
```

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

```
constant bits(esize) element2 = FPAbs(Elem[operand2, e, esize], FPCR); boolean res; case cmp_op of when Cmp_GE res = FPCompareGE(element1, element2, FPCR); when Cmp_GT res = FPCompareGT(element1, element2, FPCR); constant bit pbit = if res then '1' else '0'; Elem[result, e, psize] = ZeroExtend(pbit, psize); else Elem[result, e, psize] = ZeroExtend('0', psize); P[d, PL] = result;
```

## Operational Information

If FEAT\_SME is implemented and the PE is in Streaming SVE mode, then any subsequent instruction which is dependent on the predicate register written by this instruction might be significantly delayed.