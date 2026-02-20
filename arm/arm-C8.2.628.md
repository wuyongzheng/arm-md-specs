## C8.2.628 SQDMLALB (vectors)

Signed saturating doubling multiply-add (bottom)

This instruction multiples the corresponding even-numbered signed elements of the first and second source vectors, and then doubles the result of the multiplication. Each intermediate value is saturated to the double-width N-bit value's signed integer range -2 (N-1) to (2 (N-1) )-1 and is then destructively added to the overlapping double-width elements of the addend and destination vector. Each destination element is saturated to the double-width N-bit element's signed integer range -2 (N-1) to (2 (N-1) )-1. This instruction is unpredicated.

## SVE2

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
SQDMLALB <Zda>.<T>, <Zn>.<Tb>, <Zm>.<Tb>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda); constant integer sel1 = 0; constant integer sel2 = 0;
```

## Assembler Symbols

## &lt;Zda&gt;

Is the name of the third source and destination scalable vector register, encoded in the 'Zda' field.

&lt;T&gt;

<!-- image -->

Is the size specifier, encoded in 'size':

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

&lt;Tb&gt;

Is the size specifier, encoded in 'size':

<!-- image -->

&lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result = Z[da, VL]; for e = 0 to elements-1 constant integer element1 = SInt(Elem[operand1, 2 * e + sel1, esize DIV 2]); constant integer element2 = SInt(Elem[operand2, 2 * e + sel2, esize DIV 2]); constant integer element3 = SInt(Elem[result, e, esize]); constant integer product = SInt(SignedSat(2 * element1 * element2, esize)); Elem[result, e, esize] = SignedSat(element3 + product, esize); Z[da, VL] = result;
```

## Operational Information

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.

|   size | <Tb>     |
|--------|----------|
|     00 | RESERVED |
|     01 | B        |
|     10 | H        |
|     11 | S        |