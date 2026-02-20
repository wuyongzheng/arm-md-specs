## C8.2.26 AND (immediate)

Bitwise AND with immediate (unpredicated)

This instruction performs a bitwise AND on an immediate with each 64-bit element of the source vector, and destructively places the results in the corresponding elements of the source vector. The immediate is a 64-bit value consisting of a single run of ones or zeros repeating every 2, 4, 8, 16, 32 or 64 bits. This instruction is unpredicated.

This instruction is used by the pseudo-instruction BIC (immediate).

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
AND <Zdn>.<T>, <Zdn>.<T>, #<const>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then
```

```
EndOfDecode(Decode_UNDEF); constant integer dn = UInt(Zdn); bits(64) imm; (imm, -) = DecodeBitMasks(imm13<12>, imm13<5:0>, imm13<11:6>, TRUE, 64);
```

## Assembler Symbols

## &lt;Zdn&gt;

Is the name of the source and destination scalable vector register, encoded in the 'Zdn' field.

<!-- image -->

Is the size specifier, encoded in 'imm13':

## &lt;const&gt;

Is a 64, 32, 16 or 8-bit bitmask consisting of replicated 2, 4, 8, 16, 32 or 64 bit fields, each field containing a rotated run of non-zero bits, encoded in the 'imm13' field.

| imm13         | <T>      |
|---------------|----------|
| 0xxxxxx0xxxxx | S        |
| 0xxxxxx10xxxx | H        |
| 0xxxxxx110xxx | B        |
| 0xxxxxx1110xx | B        |
| 0xxxxxx11110x | B        |
| 0xxxxxx11111x | RESERVED |
| 1xxxxxxxxxxxx | D        |

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV 64; constant bits(VL) operand = Z[dn, VL]; bits(VL) result; for e = 0 to elements-1 constant bits(64) element1 = Elem[operand, Elem[result, e, 64] = element1 AND imm; Z[dn, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.

```
e, 64];
```