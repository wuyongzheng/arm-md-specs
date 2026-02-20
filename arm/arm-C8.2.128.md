## C8.2.128 DUP (immediate)

Broadcast signed immediate to vector elements (unpredicated)

This instruction unconditionally broadcasts the signed integer immediate into each element of the destination vector. This instruction is unpredicated.

The immediate operand is a signed value in the range -128 to +127, and for element widths of 16 bits or higher it may also be a signed multiple of 256 in the range -32768 to +32512 (excluding 0).

The immediate is encoded in 8 bits with an optional left shift by 8. The preferred disassembly when the shift option is specified is ' #&lt;simm8&gt;, LSL #8 '. However an assembler and disassembler may also allow use of the shifted 16-bit value unless the immediate is 0 and the shift amount is 8, which must be unambiguously described as ' #0, LSL #8 '.

This instruction is used by the alias MOV (immediate, unpredicated).

This instruction is used by the pseudo-instruction FMOV (zero, unpredicated).

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
DUP <Zd>.<T>, #<imm>{, <shift>}
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size:sh == '001' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer d = UInt(Zd); integer imm = SInt(imm8); if sh == '1' then imm = imm << 8;
```

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

<!-- image -->

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

## &lt;imm&gt;

Is a signed immediate in the range -128 to 127, encoded in the 'imm8' field.

## &lt;shift&gt;

Is the optional left shift to apply to the immediate, defaulting to LSL #0 and encoded in 'sh':

|   sh | <shift>   |
|------|-----------|
|    0 | LSL #0    |
|    1 | LSL #8    |

| Alias                         | Is preferred when   |
|-------------------------------|---------------------|
| FMOV (zero, unpredicated)     | Never               |
| MOV (immediate, unpredicated) | Unconditionally     |

```
esize);
```

## Alias Conditions

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant bits(VL) result = Replicate(imm<esize-1:0>, VL DIV Z[d, VL] = result;
```