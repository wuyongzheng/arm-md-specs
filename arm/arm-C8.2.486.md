## C8.2.486 NMATCH

Detect no matching elements, setting the condition flags

This instruction compares each active 8-bit or 16-bit character in the first source vector with all of the characters in the corresponding 128-bit segment of the second source vector. Where the first source element detects no matching characters in the second segment it places true in the corresponding element of the destination predicate, otherwise false. Inactive elements in the destination predicate register are set to zero. This instruction sets the First (N), None (Z), and !Last (C) condition flags based on the predicate result, and sets the V flag to zero.

This instruction is illegal when executed in Streaming SVE mode, unless FEAT\_SME\_FA64 is implemented and enabled.

## SVE2

(FEAT\_SVE2)

<!-- image -->

## Encoding

```
NMATCH <Pd>.<T>, <Pg>/Z, <Zn>.<T>, <Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) then EndOfDecode(Decode_UNDEF); if size IN {'1x'} then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer d = UInt(Pd); constant integer n = UInt(Zn); constant integer m = UInt(Zm);
```

## Assembler Symbols

&lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

Is the size specifier, encoded in 'size&lt;0&gt;':

<!-- image -->

&lt;Pg&gt;

&lt;Zn&gt;

|   size<0> | <T>   |
|-----------|-------|
|         0 | B     |
|         1 | H     |

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant integer eltspersegment = 128 DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand1 = if AnyActiveElement(mask, esize) then Z[n, VL] else Zeros(VL); constant bits(VL) operand2 = if AnyActiveElement(mask, esize) then Z[m, VL] else Zeros(VL); bits(PL) result; constant integer psize = esize DIV 8; for e = 0 to elements-1 if ActivePredicateElement(mask, e, esize) then constant integer segmentbase = e - (e MOD eltspersegment); Elem[result, e, psize] = ZeroExtend('1', psize); constant bits(esize) element1 = Elem[operand1, e, esize]; for i = segmentbase to (segmentbase + eltspersegment) 1 constant bits(esize) element2 = Elem[operand2, i, esize]; if element1 == element2 then Elem[result, e, psize] = ZeroExtend('0', psize); else Elem[result, e, psize] = ZeroExtend('0', psize); PSTATE.<N,Z,C,V> = PredTest(mask, result, esize); P[d, PL] = result;
```