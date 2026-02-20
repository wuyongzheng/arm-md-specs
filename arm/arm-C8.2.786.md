## C8.2.786 SUBR (immediate)

Reversed subtract from immediate (unpredicated)

This instruction performs a reversed subtraction from an unsigned immediate each element of the source vector, and destructively places the results in the corresponding elements of the source vector. This instruction is unpredicated.

The immediate is an unsigned value in the range 0 to 255, and for element widths of 16 bits or higher it may also be a positive multiple of 256 in the range 256 to 65280.

The immediate is encoded in 8 bits with an optional left shift by 8. The preferred disassembly when the shift option is specified is ' #&lt;uimm8&gt;, LSL #8 '. However an assembler and disassembler may also allow use of the shifted 16-bit value unless the immediate is 0 and the shift amount is 8, which must be unambiguously described as ' #0, LSL #8 '.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
SUBR <Zdn>.<T>, <Zdn>.<T>, #<imm>{,
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size:sh == '001' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer dn = UInt(Zdn); integer imm = UInt(imm8); if sh == '1' then imm = imm << 8;
```

## Assembler Symbols

## &lt;Zdn&gt;

Is the name of the source and destination scalable vector register, encoded in the 'Zdn' field.

<!-- image -->

```
<shift>}
```

Is the size specifier, encoded in 'size':

## &lt;imm&gt;

Is an unsigned immediate in the range 0 to 255, encoded in the 'imm8' field.

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

## &lt;shift&gt;

Is the optional left shift to apply to the immediate, defaulting to LSL #0 and encoded in 'sh':

|   sh | <shift>   |
|------|-----------|
|    0 | LSL #0    |
|    1 | LSL #8    |

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) operand1 = Z[dn, VL]; bits(VL) result; for e = 0 to elements-1 constant integer element1 = UInt(Elem[operand1, e, esize]); Elem[result, e, esize] = (imm - element1)<esize-1:0>; Z[dn, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.