## C8.2.508 PMOV (to vector)

Move predicate to vector

This instruction copies the source SVE predicate register elements into the destination vector register as a packed bitmap with one bit per predicate element, where bit value 0b1 represents a TRUE predicate element, and bit value 0b0 represents a FALSE predicate element.

Because the number of bits in an SVE predicate element scales with the vector element size, the behavior varies according to the specified element size.

- When the predicate element specifier is B, every bit in the predicate register is copied to the least-significant VL/8 bits of the destination vector register. The portion index, if specified, must be 0.
- When the predicate element specifier is H, every second bit in the predicate register is copied to the indexed block of VL/16 bits in the destination vector register, where the portion index is in the range 0 to 1, inclusive.
- When the predicate element specifier is S, every fourth bit in the predicate register is copied to the indexed block of VL/32 bits in the destination vector register, where the portion index is in the range 0 to 3, inclusive.
- When the predicate element specifier is D, every eighth bit in the predicate register is copied to the indexed block of VL/64 bits in the destination vector register, where the portion index is in the range 0 to 7, inclusive.

The portion index is optional, defaulting to 0 if omitted. When the index is zero, the instruction writes zeroes to the most significant VL-(VL/esize) bits of the destination vector register. When a non-zero index is specified, the packed bitmap is inserted into the destination vector register, and the unindexed blocks remain unchanged.

It has encodings from 4 classes: Byte, Doubleword, Halfword, and Word

## Byte

(FEAT\_SVE2p1 || FEAT\_SME2p1)

<!-- image -->

## Encoding

PMOV

&lt;Zd&gt;, &lt;Pn&gt;.B

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p1) && !IsFeatureImplemented(FEAT_SME2p1) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Pn); constant integer d = UInt(Zd); constant integer esize = 8; constant integer imm = 0;
```

## Doubleword

(FEAT\_SVE2p1 || FEAT\_SME2p1)

<!-- image -->

## Encoding

```
PMOV <Zd>{[<imm>]}, <Pn>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p1) && !IsFeatureImplemented(FEAT_SME2p1) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Pn); constant integer d = UInt(Zd); constant integer esize = 64; constant integer imm = UInt(i3h:i3l);
```

## Halfword

(FEAT\_SVE2p1 || FEAT\_SME2p1)

<!-- image -->

## Encoding

```
PMOV <Zd>{[<imm>]}, <Pn>.H
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p1) && !IsFeatureImplemented(FEAT_SME2p1) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Pn); constant integer d = UInt(Zd); constant integer esize = 16; constant integer imm = UInt(i1);
```

## Word

(FEAT\_SVE2p1 || FEAT\_SME2p1)

<!-- image -->

## Encoding

```
PMOV <Zd>{[<imm>]}, <Pn>.S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p1) && !IsFeatureImplemented(FEAT_SME2p1) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Pn); constant integer d = UInt(Zd); constant integer esize = 32; constant integer imm = UInt(i2);
```

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

## &lt;Pn&gt;

Is the name of the source scalable predicate register, encoded in the 'Pn' field.

## &lt;imm&gt;

For the 'Doubleword' variant: is the optional portion index, in the range 0 to 7, defaulting to 0, encoded in the 'i3h:i3l' fields.

For the 'Halfword' variant: is the optional portion index, in the range 0 to 1, defaulting to 0, encoded in the 'i1' field.

For the 'Word' variant: is the optional portion index, in the range 0 to 3, defaulting to 0, encoded in the 'i2' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) operand = P[n, PL]; bits(VL) result; if imm == 0 then result = Zeros(VL); else result = Z[d, VL]; for e = 0 to elements-1 result<(elements * imm) + e> = PredicateElement(operand, e, esize); Z[d, VL] = result;
```