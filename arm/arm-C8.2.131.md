## C8.2.131 DUPM

Broadcast logical bitmask immediate to vector (unpredicated)

This instruction unconditionally broadcasts the logical bitmask immediate into each element of the destination vector. This instruction is unpredicated. The immediate is a 64-bit value consisting of a single run of ones or zeros repeating every 2, 4, 8, 16, 32 or 64 bits.

This instruction is used by the alias MOV.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

| 31   | 29 28 25 24 23 22 21 20 19   | 18 17 5 4   |
|------|------------------------------|-------------|
| 0 0  | 0 0 0 1 0 1 1 1 0 0 0 0      | imm13 Zd    |

## Encoding

```
DUPM <Zd>.<T>, #<const>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer d = UInt(Zd); bits(esize) imm; (imm, -) = DecodeBitMasks(imm13<12>, imm13<5:0>, imm13<11:6>, TRUE, esize);
```

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'imm13':

## &lt;const&gt;

Is a 64, 32, 16 or 8-bit bitmask consisting of replicated 2, 4, 8, 16, 32 or 64 bit fields, each field containing a rotated run of non-zero bits, encoded in the 'imm13' field.

<!-- image -->

| imm13         | <T>      |
|---------------|----------|
| 0xxxxxx0xxxxx | S        |
| 0xxxxxx10xxxx | H        |
| 0xxxxxx110xxx | B        |
| 0xxxxxx1110xx | B        |
| 0xxxxxx11110x | B        |
| 0xxxxxx11111x | RESERVED |
| 1xxxxxxxxxxxx | D        |

## Alias Conditions

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant bits(VL) result = Replicate(imm, VL DIV esize); Z[d, VL] = result;
```

| Alias   | Is preferred when           |
|---------|-----------------------------|
| MOV     | SVEMoveMaskPreferred(imm13) |