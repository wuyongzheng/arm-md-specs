## C8.2.507 PMOV (to predicate)

Move predicate from vector

This instruction copies a packed bitmap, where bit value 0b1 represents TRUE and bit value 0b0 represents FALSE, from a portion of the source vector register to elements of the destination SVE predicate register.

Because the number of bits in an SVE predicate element scales with the vector element size, the behavior varies according to the specified element size.

- When the predicate element specifier is B, each bit [N] from the least-significant VL/8 bits in the source vector register is copied to bit [N] of the destination predicate register. The portion index, if specified, must be 0.
- When the predicate element specifier is H, each bit [N] within the indexed block of VL/16 bits in the source vector register is copied to bit [N*2] of the destination predicate register, and the other bits in the predicate are set to zero. The portion index is in the range 0 to 1, inclusive.
- When the predicate element specifier is S, each bit [N] within the indexed block of VL/32 bits in the source vector register is copied to bit [N*4] of the destination predicate register, and the other bits in the predicate are set to zero. The portion index is in the range 0 to 3, inclusive.
- When the predicate element specifier is D, each bit [N] within the indexed block of VL/64 bits in the source vector register is copied to bit [N*8] of the destination predicate register, and the other bits in the predicate are set to zero. The portion index is in the range 0 to 7, inclusive.

The portion index is optional, defaulting to 0 if omitted.

It has encodings from 4 classes: Byte, Doubleword, Halfword, and Word

## Byte

(FEAT\_SVE2p1 || FEAT\_SME2p1)

<!-- image -->

## Encoding

```
PMOV <Pd>.B, <Zn>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p1) && !IsFeatureImplemented(FEAT_SME2p1) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Zn); constant integer d = UInt(Pd); constant integer esize = 8; constant integer imm = 0;
```

## Doubleword

(FEAT\_SVE2p1 || FEAT\_SME2p1)

<!-- image -->

## Encoding

<!-- image -->

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p1) && !IsFeatureImplemented(FEAT_SME2p1) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Zn); constant integer d = UInt(Pd); constant integer esize = 64; constant integer imm = UInt(i3h:i3l);
```

## Halfword

(FEAT\_SVE2p1 || FEAT\_SME2p1)

<!-- image -->

## Encoding

```
PMOV <Pd>.H, <Zn>{[<imm>]}
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p1) && !IsFeatureImplemented(FEAT_SME2p1) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Zn); constant integer d = UInt(Pd); constant integer esize = 16; constant integer imm = UInt(i1);
```

## Word

(FEAT\_SVE2p1 || FEAT\_SME2p1)

<!-- image -->

## Encoding

```
PMOV <Pd>.S, <Zn>{[<imm>]}
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p1) && !IsFeatureImplemented(FEAT_SME2p1) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Zn); constant integer d = UInt(Pd); constant integer esize = 32; constant integer imm = UInt(i2);
```

## Assembler Symbols

## &lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

## &lt;Zn&gt;

Is the name of the source scalable vector register, encoded in the 'Zn' field.

## &lt;imm&gt;

For the 'Doubleword' variant: is the optional portion index, in the range 0 to 7, defaulting to 0, encoded in the 'i3h:i3l' fields.

For the 'Halfword' variant: is the optional portion index, in the range 0 to 1, defaulting to 0, encoded in the 'i1' field.

For the 'Word' variant: is the optional portion index, in the range 0 to 3, defaulting to 0, encoded in the 'i2' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(VL) operand = Z[n, VL]; bits(PL) result; constant integer psize = esize DIV 8; for e = 0 to elements-1 Elem[result, e, psize] = ZeroExtend(operand<(elements * imm) + e>, psize); P[d, PL] = result;
```