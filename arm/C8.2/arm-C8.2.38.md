## C8.2.38 BCAX

Bitwise clear and exclusive-OR

This instruction performs a bitwise AND on elements of the second source vector with the corresponding inverted elements of the third source vector, then an exclusive-OR on the results with corresponding elements of the first source vector. The final results are destructively placed in the corresponding elements of the destination and first source vector. This instruction is unpredicated.

## SVE2

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
BCAX <Zdn>.D, <Zdn>.D,
```

```
<Zm>.D, <Zk>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer m = UInt(Zm); constant integer k = UInt(Zk); constant integer dn = UInt(Zdn);
```

## Assembler Symbols

## &lt;Zdn&gt;

Is the name of the first source and destination scalable vector register, encoded in the 'Zdn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

<!-- image -->

Is the name of the third source scalable vector register, encoded in the 'Zk' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant bits(VL) operand1 = Z[dn, VL]; constant bits(VL) operand2 = Z[m, VL]; constant bits(VL) operand3 = Z[k, VL]; Z[dn, VL] = operand1 EOR (operand2 AND NOT(operand3));
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.