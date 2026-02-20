## C8.2.903 UZP1, UZP2 (predicates)

Concatenate even or odd elements from two predicates

This instruction concatenates adjacent even or odd-numbered elements from the first and second source predicates and places in elements of the destination predicate. This instruction is unpredicated.

It has encodings from 2 classes: Even and Odd

## Even

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
UZP1 <Pd>.<T>, <Pn>.<T>, <Pm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Pn); constant integer m = UInt(Pm); constant integer d = UInt(Pd); constant integer part = 0;
```

## Odd

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
UZP2 <Pd>.<T>, <Pn>.<T>, <Pm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Pn); constant integer m = UInt(Pm); constant integer d = UInt(Pd); constant integer part = 1;
```

## Assembler Symbols

## &lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

Is the size specifier, encoded in 'size':

&lt;T&gt;

## &lt;Pn&gt;

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

Is the name of the first source scalable predicate register, encoded in the 'Pn' field.

## &lt;Pm&gt;

Is the name of the second source scalable predicate register, encoded in the 'Pm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer pairs = VL DIV (esize * 2); constant bits(PL) operand1 = P[n, PL]; constant bits(PL) operand2 = P[m, PL]; bits(PL) result; for p = 0 to pairs - 1 Elem[result, p, esize DIV 8] = Elem[operand1, 2*p+part, esize DIV 8]; for p = 0 to pairs - 1 Elem[result, pairs+p, esize DIV 8] = Elem[operand2, 2*p+part, esize DIV 8]; P[d, PL] = result;
```