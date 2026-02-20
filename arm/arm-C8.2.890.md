## C8.2.890 USDOT (vectors)

Unsigned by signed 8-bit integer dot product to 32-bit integer

This instruction computes the dot product of a group of four unsigned 8-bit integer values held in each 32-bit element of the first source vector multiplied by a group of four signed 8-bit integer values in the corresponding 32-bit element of the second source vector, and then destructively adds the widened dot product to the corresponding 32-bit element of the destination vector.

This instruction is unpredicated.

ID\_AA64ZFR0\_EL1.I8MM indicates whether this instruction is implemented.

## SVE

((FEAT\_SVE || FEAT\_SME) &amp;&amp; FEAT\_I8MM)

<!-- image -->

## Encoding

```
USDOT <Zda>.S, <Zn>.B, <Zm>.B
```

## Decode for this encoding

```
if ((!IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME)) || !IsFeatureImplemented(FEAT_I8MM)) then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda);
```

## Assembler Symbols

## &lt;Zda&gt;

Is the name of the third source and destination scalable vector register, encoded in the 'Zda' field.

## &lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; constant bits(VL) operand3 = Z[da, VL]; bits(VL) result; for e = 0 to elements-1 bits(esize) res = Elem[operand3, e, esize]; for i = 0 to 3 constant integer element1 = UInt(Elem[operand1, 4 * e + i, esize DIV 4]);
```

```
constant integer element2 = SInt(Elem[operand2, 4 * e + i, esize DIV 4]); res = res + element1 * element2; Elem[result, e, esize] = res; Z[da, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.