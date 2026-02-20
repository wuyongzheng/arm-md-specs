## C8.2.828 UMINQV

Unsigned minimum reduction of quadword vector segments

This instruction performs an unsigned minimum of the same element numbers from each 128-bit source vector segment, and places each result into the corresponding element number of the 128-bit SIMD&amp;FP destination register. Inactive elements in the source vector are treated as the maximum unsigned integer for the element size.

## SVE2

(FEAT\_SVE2p1 || FEAT\_SME2p1)

<!-- image -->

## Encoding

```
UMINQV <Vd>.<T>, <Pg>, <Zn>.<Tb>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p1) && !IsFeatureImplemented(FEAT_SME2p1) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Vd); constant boolean unsigned = TRUE;
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the destination SIMD&amp;FP register, encoded in the 'Vd' field.

Is an arrangement specifier, encoded in 'size':

<!-- image -->

## &lt;Pg&gt;

<!-- image -->

&lt;Zn&gt;

|   size | <T>   |
|--------|-------|
|     00 | 16B   |
|     01 | 8H    |
|     10 | 4S    |
|     11 | 2D    |

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

Is the name of the source scalable vector register, encoded in the 'Zn' field.

## &lt;Tb&gt;

Is the size specifier, encoded in 'size':

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer segments = VL DIV 128; constant integer elempersegment = 128 DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand = if AnyActiveElement(mask, esize) then Z[n, VL] else Zeros(VL); bits(128) result = Zeros(128); bits(128) stmp = Zeros(128); integer dtmp; for e = 0 to elempersegment-1 dtmp = if unsigned then (2^esize - 1) else (2^(esize-1) 1); for s = 0 to segments-1 if ActivePredicateElement(mask, s * elempersegment + e, esize) then stmp = Elem[operand, s, 128]; dtmp = Min(dtmp, UInt(Elem[stmp, e, esize])); Elem[result, e, esize] = dtmp<esize-1:0>; V[d, 128] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

|   size | <Tb>   |
|--------|--------|
|     00 | B      |
|     01 | H      |
|     10 | S      |
|     11 | D      |