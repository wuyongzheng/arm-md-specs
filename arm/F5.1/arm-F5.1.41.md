## F5.1.41 CRC32C

## CRC32C

CRC32C performs a cyclic redundancy check (CRC) calculation on a value held in a general-purpose register. It takes an input CRC value in the first source operand, performs a CRC on the input value in the second source operand, and returns the output CRC value. The second source operand can be 8, 16, or 32 bits. To align with common usage, the bit order of the values is reversed as part of the operation, and the polynomial 0x1EDC6F41 is used for the CRC calculation.

In an Armv8.0 implementation, this is an OPTIONAL instruction. From Armv8.1, it is mandatory for all implementations to implement this instruction.

Note

ID\_ISAR5.CRC32 indicates whether this instruction is supported in the T32 and A32 instruction sets.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

(FEAT\_CRC32)

<!-- image -->

## Encoding for the CRC32CB variant

```
Applies when (sz == 00) CRC32CB{<q>} <Rd>,
```

```
<Rn>, <Rm>
```

## Encoding for the CRC32CH variant

Applies when

```
<Rn>, <Rm>
```

```
(sz == 01) CRC32CH{<q>} <Rd>,
```

## Encoding for the CRC32CW variant

```
Applies when (sz == 10)
```

```
CRC32CW{<q>} <Rd>, <Rn>, <Rm>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_CRC32) then UNDEFINED; end constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer{} size = 8 << UInt(sz); constant boolean crc32c = (C == '1'); if d == 15 || n == 15 || m == 15 then UNPREDICTABLE; end if size == 64 then UNPREDICTABLE; end if cond != '1110' then UNPREDICTABLE; end
```

Listing F5-19

## CONSTRAINED UNPREDICTABLE behavior

If size == 64 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes with the additional decode: size = 32;.

If cond != '1110' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes unconditionally.
- The instruction executes conditionally.

T1

## (FEAT\_CRC32)

<!-- image -->

## Encoding for the CRC32CB variant

```
Applies when (sz == 00) CRC32CB{<q>} <Rd>, <Rn>, <Rm>
```

## Encoding for the CRC32CH variant

Applies when

```
<Rn>, <Rm>
```

```
(sz == 01) CRC32CH{<q>} <Rd>,
```

## Encoding for the CRC32CW variant

```
Applies when (sz == 10) CRC32CW{<q>} <Rd>,
```

```
<Rn>, <Rm>
```

## Decode for all variants of this encoding

```
if InITBlock() then UNPREDICTABLE; end if !IsFeatureImplemented(FEAT_CRC32) then UNDEFINED; end constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer{} size = 8 << UInt(sz); constant boolean crc32c = (C == '1'); if d == 15 || n == 15 || m == 15 then UNPREDICTABLE; end if size == 64 then UNPREDICTABLE; end
```

Listing F5-20

## CONSTRAINED UNPREDICTABLE behavior

If size == 64 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes with the additional decode: size = 32;.

For more information about the CONSTRAINED UNPREDICTABLE behavior, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

<!-- image -->

See Standard assembler syntax fields. A CRC32C instruction must be unconditional.

Is the general-purpose accumulator output register, encoded in the 'Rd' field.

## &lt;Rd&gt;

&lt;Rn&gt;

Is the general-purpose accumulator input register, encoded in the 'Rn' field.

## &lt;Rm&gt;

Is the general-purpose data source register, encoded in the 'Rm' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) acc = R[n]; // accumulator constant bits(size) val = R[m]<size-1:0>; // input value constant bits(32) poly = (if crc32c then 0x1EDC6F41 else 0x04C11DB7)<31:0>; constant bits(32+size) tempacc = BitReverse(acc):Zeros(size); constant bits(32+size) tempval = BitReverse(val):Zeros(32); // Poly32Mod2 on a bitstring does a polynomial Modulus over {0,1} operation R[d] = BitReverse(Poly32Mod2(tempacc EOR tempval, poly)); end
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

Listing F5-21