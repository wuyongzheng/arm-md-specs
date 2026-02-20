## C8.2.576 SEL (vectors)

Conditionally select elements from two vectors

This instruction selects elements from the first source vector where the corresponding vector select predicate element is true, and from the second source vector where the predicate element is false, and places them in the corresponding elements of the destination vector.

This instruction is used by the alias MOV (vector, predicated).

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

|   31 | 29 28   | 25 24 23 22   | 21     |    | 16 15 14 13   | 10 9   | 5 4   | 0   |
|------|---------|---------------|--------|----|---------------|--------|-------|-----|
|    0 | 0 0     | 0 0 1 0 1     | size 1 | Zm | 1 1           | Pv     | Zn    | Zd  |

## Encoding

```
SEL <Zd>.<T>, <Pv>, <Zn>.<T>, <Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer v = UInt(Pv); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd);
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

<!-- image -->

&lt;T&gt;

&lt;Pv&gt;

&lt;Zn&gt;

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

Is the name of the vector select predicate register, encoded in the 'Pv' field.

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Alias Conditions

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[v, PL]; constant bits(VL) operand1 = if AnyActiveElement(mask, esize) then Z[n, VL] else Zeros(VL); constant bits(VL) operand2 = if AnyActiveElement(NOT(mask), esize) then Z[m, VL] else Zeros(VL); bits(VL) result; for e = 0 to elements-1 if ActivePredicateElement(mask, e, esize) then Elem[result, e, esize] = Elem[operand1, e, esize]; else Elem[result, e, esize] = Elem[operand2, e, esize]; Z[d, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

| Alias                    | Is preferred when   |
|--------------------------|---------------------|
| MOV (vector, predicated) | Zd == Zm            |