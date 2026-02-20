## C8.2.190 FDUP

Broadcast floating-point immediate to vector elements (unpredicated)

This instruction unconditionally broadcasts the floating-point immediate into each element of the destination vector. This instruction is unpredicated.

This instruction is used by the alias FMOV (immediate, unpredicated).

```
SVE (FEAT_SVE || FEAT_SME)
```

<!-- image -->

## Encoding

```
FDUP <Zd>.<T>, #<const>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer d = UInt(Zd); constant bits(esize) imm = VFPExpandImm(imm8, esize);
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

## &lt;const&gt;

Is a floating-point immediate value expressible as ±n÷16 × 2^r, where n and r are integers such that 16 ≤ n ≤ 31 and -3 ≤ r ≤ 4, i.e. a normalized binary floating-point encoding with 1 sign bit, 3-bit exponent, and 4-bit fractional part, encoded in the 'imm8' field.

<!-- image -->

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |

## Alias Conditions

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; bits(VL) result; for e = 0 to elements-1 Elem[result, e, esize] = imm; Z[d, VL] = result;
```

## Alias

FMOV (immediate, unpredicated)

## Is preferred when

Unconditionally