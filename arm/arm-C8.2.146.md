## C8.2.146 EXTQ

Extract vector segment from each pair of quadword vector segments

This instruction copies, for each 128-bit vector segment of the result, the indexed byte up to and including the last byte of the corresponding first source vector segment to the bottom of the result segment, and then fills the remainder of the result segment starting from the first byte of the corresponding second source vector segment. The result segments are destructively placed in the corresponding first source vector segment. This instruction is unpredicated.

## SVE2

(FEAT\_SVE2p1 || FEAT\_SME2p1)

<!-- image -->

## Encoding

```
EXTQ <Zdn>.B, <Zdn>.B, <Zm>.B, #<imm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p1) && !IsFeatureImplemented(FEAT_SME2p1) then EndOfDecode(Decode_UNDEF); constant integer dn = UInt(Zdn); constant integer m = UInt(Zm); constant integer position = UInt(imm4) << 3;
```

## Assembler Symbols

## &lt;Zdn&gt;

Is the name of the first source and destination scalable vector register, encoded in the 'Zdn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## &lt;imm&gt;

Is the unsigned immediate operand, in the range 0 to 15, encoded in the 'imm4' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer segments = VL DIV 128; constant bits(VL) operand1 = Z[dn, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result; for s = 0 to segments-1 constant bits(256) concat = Elem[operand2, s, 128] : Elem[operand1, s, 128]; Elem[result, s, 128] = concat<position+127:position>; Z[dn, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.