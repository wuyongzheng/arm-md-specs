## C8.2.191 FEXPA

Floating-point exponential accelerator

This instruction computes an exponentiation acceleration operation on each floating-point element in the source vector, where the result sign is zero, the result exponent field is copied from a set of significant bits of the input fraction, and the result fraction is inserted from a lookup table indexed by the least-significant input fraction bits, and returns each result in the corresponding element of the destination vector.

This instruction is fully defined by its bit-manipulation semantics, does not generate floating-point exceptions, and does not guarantee NaN propagation.

For double-precision variants, the result element exponent is copied from the source element bits&lt;16:6&gt;, and the result fraction is set based on the source element to the rounded value of 2 52 × (2 bits&lt;5:0&gt;/64 - 1).

For single-precision variants, the result element exponent is copied from the source element bits&lt;13:6&gt;, and the result fraction is set based on the source element to the rounded value of 2 23 × (2 bits&lt;5:0&gt;/64 - 1).

For half-precision variants, the result element exponent is copied from the source element bits&lt;9:5&gt;, and the result fraction is set based on the source element to the rounded value of 2 10 × (2 bits&lt;4:0&gt;/32 - 1).

This instruction is unpredicated.

This instruction is illegal when executed in Streaming SVE mode, unless FEAT\_SME\_FA64 is implemented and enabled, or FEAT\_SSVE\_FEXPA is implemented.

Note

For a double-precision input value x in the range 70,368,744,177,655 &lt;= x &lt; 70,368,744,179,711, the operation performed by this instruction is equivalent to computing 2 x-70,368,744,178,687 .

For a single-precision input value x in the range 131,073 &lt;= x &lt; 131,327, the operation performed by this instruction is equivalent to computing 2 x-131,199 .

For a half-precision input value x in the range 33 &lt;= x &lt; 63, the operation performed by this instruction is equivalent to computing 2 x-47 .

## SVE

(FEAT\_SVE || FEAT\_SSVE\_FEXPA)

<!-- image -->

## Encoding

```
FEXPA <Zd>.<T>, <Zn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SSVE_FEXPA) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn); constant integer d = UInt(Zd);
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

<!-- image -->

<!-- image -->

&lt;Zn&gt;

Is the size specifier, encoded in 'size':

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |

Is the name of the source scalable vector register, encoded in the 'Zn' field.

## Operation

```
if IsFeatureImplemented(FEAT_SSVE_FEXPA) then CheckSVEEnabled(); else CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) operand = Z[n, VL]; bits(VL) result; for e = 0 to elements-1 constant bits(esize) element = Elem[operand, e, esize]; Elem[result, e, esize] = FPExpA(element); Z[d, VL] = result;
```