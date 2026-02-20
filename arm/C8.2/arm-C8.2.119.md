## C8.2.119 CPY (immediate, zeroing)

Copy signed integer immediate to vector elements (zeroing)

This instruction copies a signed integer immediate to each Active element in the destination vector. Inactive elements in the destination vector register are set to zero.

The immediate operand is a signed value in the range -128 to +127, and for element widths of 16 bits or higher it may also be a signed multiple of 256 in the range -32768 to +32512 (excluding 0).

The immediate is encoded in 8 bits with an optional left shift by 8. The preferred disassembly when the shift option is specified is ' #&lt;simm8&gt;, LSL #8 '. However an assembler and disassembler may also allow use of the shifted 16-bit value unless the immediate is 0 and the shift amount is 8, which must be unambiguously described as ' #0, LSL #8 '.

This instruction is used by the alias MOV (immediate, zeroing).

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
CPY <Zd>.<T>, <Pg>/Z, #<imm>{, <shift>}
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size:sh == '001' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer d = UInt(Zd); constant boolean merging = FALSE; integer imm = SInt(imm8); if sh == '1' then imm = imm << 8;
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

<!-- image -->

M

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

## &lt;Pg&gt;

Is the name of the governing scalable predicate register, encoded in the 'Pg' field.

## &lt;imm&gt;

Is a signed immediate in the range -128 to 127, encoded in the 'imm8' field.

## &lt;shift&gt;

Is the optional left shift to apply to the immediate, defaulting to LSL #0 and encoded in 'sh':

|   sh | <shift>   |
|------|-----------|
|    0 | LSL #0    |
|    1 | LSL #8    |

| Alias                    | Is preferred when   |
|--------------------------|---------------------|
| MOV (immediate, zeroing) | Unconditionally     |

## Alias Conditions

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(VL) dest = if merging then Z[d, VL] else Zeros(VL); bits(VL) result; for e = 0 to elements-1 if ActivePredicateElement(mask, e, esize) then Elem[result, e, esize] = imm<esize-1:0>; else Elem[result, e, esize] = Elem[dest, e, esize]; Z[d, VL] = result;
```