## C8.2.573 SDOT (4-way, vectors)

Signed integer dot product (four-way)

This instruction computes the dot product of a group of four signed 8-bit or 16-bit integer values held in each 32-bit or 64-bit element of the first source vector multiplied by a group of four signed 8-bit or 16-bit integer values in the corresponding 32-bit or 64-bit element of the second source vector, and then destructively adds the widened dot product to the corresponding 32-bit or 64-bit element of the destination vector.

This instruction is unpredicated.

```
SVE
```

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
SDOT <Zda>.<T>, <Zn>.<Tb>, <Zm>.<Tb>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size IN {'0x'} then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda);
```

## Assembler Symbols

## &lt;Zda&gt;

Is the name of the third source and destination scalable vector register, encoded in the 'Zda' field.

&lt;T&gt;

## &lt;Zn&gt;

<!-- image -->

Is the size specifier, encoded in 'size&lt;0&gt;':

|   size<0> | <T>   |
|-----------|-------|
|         0 | S     |
|         1 | D     |

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

Is the size specifier, encoded in 'size&lt;0&gt;':

<!-- image -->

&lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; constant bits(VL) operand3 = Z[da, VL]; bits(VL) result; for e = 0 to elements-1 bits(esize) res = Elem[operand3, e, esize]; for i = 0 to 3 constant integer element1 = SInt(Elem[operand1, 4 * e + i, esize DIV 4]); constant integer element2 = SInt(Elem[operand2, 4 * e + i, esize DIV 4]); res = res + element1 * element2; Elem[result, e, esize] = res; Z[da, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.

|   size<0> | <Tb>   |
|-----------|--------|
|         0 | B      |
|         1 | H      |