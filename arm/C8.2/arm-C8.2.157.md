## C8.2.157 FADDA

Floating-point add strictly-ordered reduction, accumulating in scalar

This instruction adds the floating-point values in a SIMD&amp;FP scalar source and all active lanes of the vector source and destructively places the result in the SIMD&amp;FP scalar source register. Vector elements are processed strictly in order from low to high, with the scalar source providing the initial value. Inactive elements in the source vector are ignored.

This instruction is illegal when executed in Streaming SVE mode, unless FEAT\_SME\_FA64 is implemented and enabled.

## SVE

(FEAT\_SVE)

<!-- image -->

## Encoding

```
FADDA <V><dn>, <Pg>, <V><dn>, <Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) then EndOfDecode(Decode_UNDEF);
```

```
if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer dn = UInt(Vdn); constant integer m = UInt(Zm);
```

## Assembler Symbols

&lt;V&gt;

Is a width specifier, encoded in 'size':

<!-- image -->

&lt;dn&gt;

<!-- image -->

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

&lt;Zm&gt;

Is the name of the source scalable vector register, encoded in the 'Zm' field.

|   size | <V>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |

Is the number [0-31] of the source and destination SIMD&amp;FP register, encoded in the 'Vdn' field.

&lt;T&gt;

Is the size specifier, encoded in 'size':

## Operation

```
CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(esize) operand1 = V[dn, esize]; constant bits(VL) operand2 = if AnyActiveElement(mask, esize) then Z[m, VL] else Zeros(VL); bits(esize) result = operand1; for e = 0 to elements-1 if ActivePredicateElement(mask, e, esize) then constant bits(esize) element = Elem[operand2, e, esize]; result = FPAdd(result, element, FPCR); V[dn, esize] = result;
```

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |