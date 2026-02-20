## C8.2.276 FTSMUL

Floating-point trigonometric starting value

This instruction multiplies each element of the first source vector by itself, replaces the sign-bit of each product with the least-significant bit of the corresponding element of the second source vector, and places the results in the destination vector. This instruction is unpredicated.

FTSMUL can be combined with FTMAD and FTSSEL to compute values for sin(x) and cos(x). The use of the second operand is consistent with it holding an integer corresponding to the desired sine-wave quadrant when used in conjunction with FTMAD .

Note: FTSMUL , FTMAD , and FTSSEL can be used to compute values for sin(k) and correspondingly cos(kπ /2) via an intermediate value x, in the range π /4 &lt; x ≤ π /4, and a quadrant q where k = q π /2 + x, using a Taylor Series approximation. FTSMUL can be used to compute x 2 , and to insert q&lt;0&gt; into the most-significant bit, indicating the desired odd versus even Taylor Series to be used in FTMAD . Repeated uses of FTMAD can be performed on this value with decreasing immediate index operands, to produce a single accumulated value approximating the Taylor Series result with a single outstanding factor. FTSSEL can be used to apply the final factor of x, 1.0, -x, or -1.0, dependent on the corresponding sine-wave quadrant q&lt;1:0&gt;, to produce a final sin() or cos() value.

This instruction is illegal when executed in Streaming SVE mode, unless FEAT\_SME\_FA64 is implemented and enabled.

## SVE

(FEAT\_SVE)

<!-- image -->

## Encoding

```
FTSMUL <Zd>.<T>, <Zn>.<T>, <Zm>.<T>
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

&lt;T&gt;

<!-- image -->

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |

## &lt;Zn&gt;

|   size | <T>   |
|--------|-------|
|     01 | H     |
|     10 | S     |
|     11 | D     |

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

<!-- image -->

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result; for e = 0 to elements-1 constant bits(esize) element1 = Elem[operand1, e, esize]; constant bits(esize) element2 = Elem[operand2, e, esize]; Elem[result, e, esize] = FPTrigSMul(element1, element2, FPCR); Z[d, VL] = result;
```