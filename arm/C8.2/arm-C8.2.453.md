## C8.2.453 MADPT

Multiply-add checked pointer vectors to multiplicand

This instruction multiplies, with overflow check, the elements of the first and second source vectors and adds the results of multiplication, with pointer check, to elements of the third (addend) vector. The final results are destructively placed in the destination and first source (multiplicand) vector.

This instruction is illegal when executed in Streaming SVE mode, unless FEAT\_SME\_FA64 is implemented and enabled.

## SVE2

(FEAT\_SVE &amp;&amp; FEAT\_CPA)

<!-- image -->

## Encoding

```
MADPT <Zdn>.D, <Zm>.D, <Za>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) || !IsFeatureImplemented(FEAT_CPA) then EndOfDecode(Decode_UNDEF); constant integer dn = UInt(Zdn); constant integer m = UInt(Zm); constant integer a = UInt(Za);
```

## Assembler Symbols

## &lt;Zdn&gt;

Is the name of the first source and destination scalable vector register, encoded in the 'Zdn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

<!-- image -->

## &lt;Za&gt;

Is the name of the third source scalable vector register, encoded in the 'Za' field.

## Operation

```
CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV 64; constant bits(VL) operand1 = Z[dn, VL]; constant bits(VL) operand2 = Z[m, VL]; constant bits(VL) operand3 = Z[a, VL]; bits(VL) result; for e = 0 to elements-1 constant integer element1 = SInt(Elem[operand1, e, 64]); constant integer element2 = SInt(Elem[operand2, e, 64]); constant integer product = element1 * element2; constant boolean overflow = (product != SInt(product<63:0>)); constant bits(64) addend = Elem[operand3, e, 64]; Elem[result, e, 64] = PointerMultiplyAddCheck(addend + product, addend, overflow);
```

Z[dn, VL] = result;

## Operational Information

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.