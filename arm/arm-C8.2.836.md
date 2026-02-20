## C8.2.836 UMLSLT (vectors)

Unsigned multiply-subtract long (top)

This instruction multiplies the corresponding odd-numbered unsigned elements of the first and second source vectors, and destructively subtracts from the overlapping double-width elements of the addend vector. This instruction is unpredicated.

## SVE2

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
UMLSLT <Zda>.<T>, <Zn>.<Tb>, <Zm>.<Tb>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda);
```

## Assembler Symbols

&lt;Zda&gt;

Is the name of the third source and destination scalable vector register, encoded in the 'Zda' field.

<!-- image -->

<!-- image -->

Is the size specifier, encoded in 'size':

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Tb&gt;

Is the size specifier, encoded in 'size':

<!-- image -->

&lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result = Z[da, VL]; for e = 0 to elements-1 constant integer element1 = UInt(Elem[operand1, 2*e + 1, esize DIV 2]); constant integer element2 = UInt(Elem[operand2, 2*e + 1, esize DIV 2]); constant bits(esize) product = (element1 * element2)<esize-1:0>; Elem[result, e, esize] = Elem[result, e, esize] product; Z[da, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

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