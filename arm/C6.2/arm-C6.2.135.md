## C6.2.135 CRC32B, CRC32H, CRC32W, CRC32X

## CRC32 checksum

This instruction performs a cyclic redundancy check (CRC) calculation on a value held in a general-purpose register. It takes an input CRC value in the first source operand, performs a CRC on the input value in the second source operand, and returns the output CRC value. The second source operand can be 8, 16, 32, or 64 bits. To align with common usage, the bit order of the values is reversed as part of the operation, and the polynomial 0x04C11DB7 is used for the CRC calculation.

In an Armv8.0 implementation, this is an OPTIONAL instruction. From Armv8.1, it is mandatory for all implementations to implement this instruction.

## Note

ID\_AA64ISAR0\_EL1.CRC32 indicates whether this instruction is supported.

## CRC

(FEAT\_CRC32)

<!-- image -->

## Encoding for the CRC32B variant

```
Applies when (sf == 0 && sz == 00)
```

```
CRC32B <Wd>, <Wn>, <Wm>
```

## Encoding for the CRC32H variant

Applies when (sf

```
CRC32H <Wd>,
```

```
== 0 && sz == 01) <Wn>, <Wm>
```

## Encoding for the CRC32W variant

```
Applies when (sf
```

```
== 0 && sz == 10) CRC32W <Wd>, <Wn>, <Wm>
```

## Encoding for the CRC32X variant

Applies when (sf == 1 &amp;&amp; sz == 11)

```
CRC32X <Wd>, <Wn>, <Xm>
```

## Decode for all variants of this encoding

```
EndOfDecode(Decode_UNDEF);
```

```
if !IsFeatureImplemented(FEAT_CRC32) then constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); if sf == '1' && sz != '11' then EndOfDecode(Decode_UNDEF); if sf == '0' && sz == '11' then EndOfDecode(Decode_UNDEF); constant integer size = 8 << UInt(sz);
```

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose accumulator output register, encoded in the 'Rd' field.

## &lt;Wn&gt;

Is the 32-bit name of the general-purpose accumulator input register, encoded in the 'Rn' field.

## &lt;Wm&gt;

Is the 32-bit name of the general-purpose data source register, encoded in the 'Rm' field.

## &lt;Xm&gt;

Is the 64-bit name of the general-purpose data source register, encoded in the 'Rm' field.

## Operation

```
constant bits(32) acc = X[n, 32]; // accumulator constant bits(size) val = X[m, size]; // input value constant bits(32) poly = \texttt{0x04C11DB7}<31:0>; constant bits(32+size) tempacc = BitReverse(acc):Zeros(size); constant bits(size+32) tempval = BitReverse(val):Zeros(32); // Poly32Mod2 on a bitstring does a polynomial Modulus over {0,1} operation X[d, 32] = BitReverse(Poly32Mod2(tempacc EOR tempval, poly));
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
