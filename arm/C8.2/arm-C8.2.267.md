## C8.2.267 FRSQRTS

Floating-point reciprocal square root step (unpredicated)

This instruction multiplies corresponding floating-point elements of the first and second source vectors, subtracts the products from 3.0 and divides the results by 2.0 without any intermediate rounding, and places the results in the corresponding elements of the destination vector. This instruction is unpredicated.

This instruction can be used to perform a single Newton-Raphson iteration for calculating the reciprocal square root of a vector of floating-point values.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FRSQRTS <Zd>.<T>, <Zn>.<T>, <Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd);
```

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

&lt;T&gt;

## &lt;Zn&gt;

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result; for e = 0 to elements-1 constant bits(esize) element1 = Elem[operand1, e, esize]; constant bits(esize) element2 = Elem[operand2, e, esize]; Elem[result, e, esize] = Z[d, VL] = result;
```

```
FPRSqrtStepFused(element1, element2, FPCR);
```