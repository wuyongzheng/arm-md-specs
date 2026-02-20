## C8.2.806 UADDV

Unsigned add reduction to scalar

This instruction performs an unsigned add horizontally across all lanes of a vector, and places the result in the SIMD&amp;FP scalar destination register. Narrow elements are first zero-extended to 64 bits. Inactive elements in the source vector are treated as zero.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
UADDV <Dd>, <Pg>, <Zn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Vd);
```

## Assembler Symbols

&lt;Dd&gt;

Is the 64-bit name of the destination SIMD&amp;FP register, encoded in the 'Vd' field.

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

Is the name of the source scalable vector register, encoded in the 'Zn' field.

Is the size specifier, encoded in 'size':

<!-- image -->

&lt;Zn&gt;

<!-- image -->

&lt;T&gt;

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand = if AnyActiveElement(mask, esize) then Z[n, VL] else Zeros(VL); integer sum = 0; for e = 0 to elements-1 if ActivePredicateElement(mask, e, esize) then constant integer element = UInt(Elem[operand, e, esize]); sum = sum + element; V[d, 64] = sum<63:0>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.