## C8.2.145 EXT

Extract vector from pair of vectors

This instruction copies the indexed byte up to the last byte of the first source vector to the bottom of the result vector, then fills the remainder of the result starting from the first byte of the second source vector. The result is destructively placed in the destination and first source vector, or constructively placed in the destination vector. This instruction is unpredicated.

An index that is greater than or equal to the vector length in bytes is treated as zero, resulting in the first source vector being copied to the result unchanged.

It has encodings from 2 classes: Constructive and Destructive

## Constructive

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

|   31 | 29 28   | 25 24 23 22 21 20   | 16 15 13 12   | 10 9   | 5 4   |    |
|------|---------|---------------------|---------------|--------|-------|----|
|    0 | 0 0     | 0 0 1 0 1 0 1       | 1 imm8h 0 0 0 | imm8l  | Zn    | Zd |

## Encoding

```
EXT <Zd>.B, { <Zn1>.B, <Zn2>.B }, #<imm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8; constant integer dst = UInt(Zd); constant integer s1 = UInt(Zn); constant integer s2 = (s1 + 1) MOD 32; constant integer position = UInt(imm8h:imm8l) * 8;
```

## Destructive

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
EXT <Zdn>.B, <Zdn>.B, <Zm>.B, #<imm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8; constant integer dst = UInt(Zdn); constant integer s1 = dst; constant integer s2 = UInt(Zm); constant integer position = UInt(imm8h:imm8l) * 8;
```

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

## &lt;Zn1&gt;

Is the name of the first scalable vector register of the source multi-vector group, encoded in the 'Zn' field.

## &lt;Zn2&gt;

Is the name of the second scalable vector register of the source multi-vector group, encoded in the 'Zn' field.

## &lt;imm&gt;

Is the unsigned immediate operand, in the range 0 to 255, encoded in the 'imm8h:imm8l' fields.

## &lt;Zdn&gt;

Is the name of the first source and destination scalable vector register, encoded in the 'Zdn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) operand1 = Z[s1, VL]; constant bits(VL) operand2 = Z[s2, VL]; bits(VL) result; constant bits(VL*2) concat = operand2 : operand1; if position >= VL then result = concat<VL-1:0>; else result = concat<(position+VL)-1:position>; Z[dst, VL] = result;
```

## Operational Information

For the Constructive variant:

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

For the Destructive variant:

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

The destructive variant of this instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and the destructive variant of this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.