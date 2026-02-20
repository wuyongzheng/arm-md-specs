## C8.2.646 SQINCD (vector)

Signed saturating increment vector by multiple of 64-bit predicate constraint element count

This instruction determines the number of active 64-bit elements implied by the named predicate constraint, multiplies that by an immediate in the range 1 to 16 inclusive, and then uses the result to increment all destination vector elements. The results are saturated to the 64-bit signed integer range.

The named predicate constraint limits the number of active elements in a single predicate to:

- Afixed number (VL1 to VL256)
- The largest power of two (POW2)
- The largest multiple of three or four (MUL3 or MUL4)
- All available, implicitly a multiple of two (ALL).

Unspecified or out of range constraint encodings generate an empty predicate or zero element count rather than Undefined Instruction exception.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
SQINCD <Zdn>.D{, <pattern>{, MUL
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer dn = UInt(Zdn); constant bits(5) pat = pattern; constant integer imm = UInt(imm4) + 1; constant boolean unsigned = FALSE;
```

## Assembler Symbols

## &lt;Zdn&gt;

Is the name of the source and destination scalable vector register, encoded in the 'Zdn' field.

## &lt;pattern&gt;

Is the optional pattern specifier, defaulting to ALL, encoded in 'pattern':

|   pattern | <pattern>   |
|-----------|-------------|
|     00000 | POW2        |
|     00001 | VL1         |

```
#<imm>}}
```

## &lt;imm&gt;

Is the immediate multiplier, in the range 1 to 16, defaulting to 1, encoded in the 'imm4' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant integer count = DecodePredCount(pat, esize); constant bits(VL) operand1 = Z[dn, VL]; bits(VL) result; for e = 0 to elements-1 constant bits(esize) op1elt = Elem[operand1, e, esize]; if unsigned then (Elem[result, e, esize], -) = UnsignedSatQ(UInt(op1elt) + (count * imm), esize); else (Elem[result, e, esize], -) = SignedSatQ(SInt(op1elt) + (count * imm), esize); Z[dn, VL] = result;
```

## Operational Information

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.

| pattern   | <pattern>   |
|-----------|-------------|
| 00010     | VL2         |
| 00011     | VL3         |
| 00100     | VL4         |
| 00101     | VL5         |
| 00110     | VL6         |
| 00111     | VL7         |
| 01000     | VL8         |
| 01001     | VL16        |
| 01010     | VL32        |
| 01011     | VL64        |
| 01100     | VL128       |
| 01101     | VL256       |
| 0111x     | #uimm5      |
| 101x1     | #uimm5      |
| 10110     | #uimm5      |
| 1x0x1     | #uimm5      |
| 1x010     | #uimm5      |
| 1xx00     | #uimm5      |
| 11101     | MUL4        |
| 11110     | MUL3        |
| 11111     | ALL         |

- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.