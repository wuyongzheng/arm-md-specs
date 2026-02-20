## C8.2.277 FTSSEL

Floating-point trigonometric select coefficient

This instruction selects either the element of the first source vector or the value 1.0, based on bit&lt;0&gt; of the corresponding element of the second source element, negates the result if bit&lt;1&gt; of the corresponding element of the second source element is set, and places the results in the destination vector. This instruction is unpredicated.

FTSSEL can be combined with FTSMUL and FTMAD to compute values for sin(k) and cos(k). For more information, see FTSMUL . The use of the second operand is consistent with it holding an integer corresponding to the desired sine-wave quadrant.

This instruction is illegal when executed in Streaming SVE mode, unless FEAT\_SME\_FA64 is implemented and enabled.

## SVE

(FEAT\_SVE)

<!-- image -->

## Encoding

```
FTSSEL <Zd>.<T>, <Zn>.<T>, <Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) then EndOfDecode(Decode_UNDEF);
```

```
if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd);
```

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

<!-- image -->

<!-- image -->

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
CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result; for e = 0 to elements-1 constant bits(esize) element1 = Elem[operand1, e, esize]; constant bits(esize) element2 = Elem[operand2, e, esize]; Elem[result, e, esize] = FPTrigSSel(element1, element2); Z[d, VL] = result;
```