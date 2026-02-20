## C8.2.865 UQINCW (scalar)

Unsigned saturating increment scalar by multiple of 32-bit predicate constraint element count

This instruction determines the number of active 32-bit elements implied by the named predicate constraint, multiplies that by an immediate in the range 1 to 16 inclusive, and then uses the result to increment the scalar destination. The result is saturated to the general-purpose register's unsigned integer range.

The named predicate constraint limits the number of active elements in a single predicate to:

- Afixed number (VL1 to VL256)
- The largest power of two (POW2)
- The largest multiple of three or four (MUL3 or MUL4)
- All available, implicitly a multiple of two (ALL).

Unspecified or out of range constraint encodings generate an empty predicate or zero element count rather than Undefined Instruction exception.

It has encodings from 2 classes: 32-bit and 64-bit

## 32-bit

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
UQINCW <Wdn>{, <pattern>{,
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer dn = UInt(Rdn); constant bits(5) pat = pattern; constant integer imm = UInt(imm4) + 1; constant boolean unsigned = TRUE; constant integer ssize = 32;
```

## 64-bit

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
UQINCW <Xdn>{, <pattern>{, MUL #<imm>}}
```

```
MUL #<imm>}}
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer dn = UInt(Rdn); constant bits(5) pat = pattern; constant integer imm = UInt(imm4) + 1; constant boolean unsigned = TRUE; constant integer ssize = 64;
```

## Assembler Symbols

## &lt;Wdn&gt;

Is the 32-bit name of the source and destination general-purpose register, encoded in the 'Rdn' field.

## &lt;pattern&gt;

Is the optional pattern specifier, defaulting to ALL, encoded in 'pattern':

| pattern   | <pattern>   |
|-----------|-------------|
| 00000     | POW2        |
| 00001     | VL1         |
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

## &lt;imm&gt;

Is the immediate multiplier, in the range 1 to 16, defaulting to 1, encoded in the 'imm4' field.

## &lt;Xdn&gt;

Is the 64-bit name of the source and destination general-purpose register, encoded in the 'Rdn' field.

## Operation

```
CheckSVEEnabled(); constant integer count = DecodePredCount(pat, esize); constant bits(ssize) operand1 = X[dn, ssize]; bits(ssize) result; if unsigned then (result, -) = UnsignedSatQ(UInt(operand1) + (count * imm), ssize); else (result, -) = SignedSatQ(SInt(operand1) + (count * imm), ssize); X[dn, 64] = Extend(result, 64, unsigned);
```