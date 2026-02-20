## C8.2.278 HISTCNT

Count matching elements in vector

This instruction compares each active 32 or 64-bit element of the first source vector with all Active elements with an element number less than or equal to its own in the second source vector, and places the count of matching elements in the corresponding element of the destination vector. Inactive elements in the destination vector are set to zero.

This instruction is illegal when executed in Streaming SVE mode, unless FEAT\_SME\_FA64 is implemented and enabled.

## SVE2

(FEAT\_SVE2)

<!-- image -->

## Encoding

```
HISTCNT <Zd>.<T>, <Pg>/Z, <Zn>.<T>, <Zm>.<T>
```

## Decode for this encoding

```
EndOfDecode(Decode_UNDEF);
```

```
if !IsFeatureImplemented(FEAT_SVE2) then if size IN {'0x'} then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer d = UInt(Zd); constant integer n = UInt(Zn); constant integer m = UInt(Zm);
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size&lt;0&gt;':

&lt;T&gt;

&lt;Pg&gt;

&lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

&lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

|   size<0> | <T>   |
|-----------|-------|
|         0 | S     |
|         1 | D     |

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

## Operation

```
CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand1 = if AnyActiveElement(mask, esize) then Z[n, VL] else Zeros(VL); constant bits(VL) operand2 = if AnyActiveElement(mask, esize) then Z[m, VL] else Zeros(VL); bits(VL) result; for e = 0 to elements-1 integer count = 0; if ActivePredicateElement(mask, e, esize) then constant bits(esize) element1 = Elem[operand1, e, esize]; for i = 0 to e if ActivePredicateElement(mask, i, esize) then constant bits(esize) element2 = Elem[operand2, i, esize]; if element1 == element2 then count = count + 1; Elem[result, e, esize] = count<esize-1:0>; Z[d, VL] = result;
```