## F6.1.114 VLDR (literal)

Load SIMD&amp;FP register (literal) loads a single register from the Advanced SIMD and floating-point register file, using an address from the PC value and an immediate offset.

Depending on settings in the CPACR, NSACR, HCPTR, and FPEXC registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information, see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the Half-precision scalar variant

```
(FEAT_FP16) Applies when (size == 01) VLDR{<c>}{<q>}.16 <Sd>, <label> // (Preferred syntax) VLDR{<c>}{<q>}.16 <Sd>, [PC, #{+/-}<imm>]
```

## Encoding for the Single-precision scalar variant

```
Applies when (size == 10) VLDR{<c>}{<q>}{.32} <Sd>, <label> // (Preferred syntax) VLDR{<c>}{<q>}{.32} <Sd>, [PC, #{+/-}<imm>]
```

## Encoding for the Double-precision scalar variant

```
Applies when (size == 11) VLDR{<c>}{<q>}{.64} <Dd>, <label> // (Preferred syntax) VLDR{<c>}{<q>}{.64} <Dd>, [PC, #{+/-}<imm>]
```

## Decode for all variants of this encoding

```
if size == '00' || (size == '01' && !IsFeatureImplemented(FEAT_FP16)) then UNDEFINED; if size == '01' && cond != '1110' then UNPREDICTABLE; constant boolean add = (U == '1'); constant integer esize = 8 << UInt(size); constant integer imm32 = UInt(imm8) << (if size == '01' then 1 else 2); constant integer d = if size == '11' then UInt(D:Vd) else UInt(Vd:D); constant integer n = UInt(Rn);
```

## CONSTRAINED UNPREDICTABLE behavior

If size == '01' &amp;&amp; cond != '1110' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

T1

<!-- image -->

L

## Encoding for the Half-precision scalar variant

```
(FEAT_FP16) Applies when (size == 01) VLDR{<c>}{<q>}.16 <Sd>, <label> // (Preferred syntax) VLDR{<c>}{<q>}.16 <Sd>, [PC, #{+/-}<imm>]
```

## Encoding for the Single-precision scalar variant

```
Applies when (size == 10) VLDR{<c>}{<q>}{.32} <Sd>, <label> // (Preferred syntax) VLDR{<c>}{<q>}{.32} <Sd>, [PC, #{+/-}<imm>]
```

## Encoding for the Double-precision scalar variant

Applies when (size ==

```
11)
```

```
VLDR{<c>}{<q>}{.64} <Dd>, <label> // (Preferred syntax) VLDR{<c>}{<q>}{.64} <Dd>, [PC, #{+/-}<imm>]
```

## Decode for all variants of this encoding

```
if size == '00' || (size == '01' && !IsFeatureImplemented(FEAT_FP16)) then UNDEFINED; if size == '01' && InITBlock() then UNPREDICTABLE; constant boolean add = (U == '1'); constant integer esize = 8 << UInt(size); constant integer imm32 = UInt(imm8) << (if size == '01' then 1 else 2); constant integer d = if size == '11' then UInt(D:Vd) else UInt(Vd:D); constant integer n = UInt(Rn);
```

## CONSTRAINED UNPREDICTABLE behavior

If size == '01' &amp;&amp; InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

&lt;q&gt;

## &lt;Sd&gt;

Is the 32-bit name of the SIMD&amp;FP destination register, encoded in the 'Vd:D' field.

## &lt;label&gt;

The label of the literal data item to be loaded.

For the single-precision scalar or double-precision scalar variants: the assembler calculates the required value of the offset from the Align(PC, 4) value of the instruction to this label. Permitted values are multiples of 4 in the range -1020 to 1020.

For the half-precision scalar variant: the assembler calculates the required value of the offset from the Align(PC, 4) value of the instruction to this label. Permitted values are multiples of 2 in the range -510 to 510.

If the offset is zero or positive, imm32 is equal to the offset and add == TRUE .

If the offset is negative, imm32 is equal to minus the offset and add == FALSE .

Specifies the offset is added to or subtracted from the base register, defaulting to + if omitted and encoded in 'U':

|   U | +/-   |
|-----|-------|
|   0 | -     |
|   1 | +     |

+/-

## &lt;imm&gt;

For the 'A1 Half-precision scalar' and 'T1 Half-precision scalar' variants: is the optional unsigned immediate byte offset, a multiple of 2, in the range 0 to 510, defaulting to 0, and encoded in the 'imm8' field as &lt;imm&gt;/2.

For the 'A1 Double-precision scalar', 'A1 Single-precision scalar', 'T1 Double-precision scalar', and 'T1 Single-precision scalar' variants: is the optional unsigned immediate byte offset, a multiple of 4, in the range 0 to 1020, defaulting to 0, and encoded in the 'imm8' field as &lt;imm&gt;/4.

Is an optional data size specifier for 32-bit memory accesses that can be used in the assembler source code, but is otherwise ignored.

Is an optional data size specifier for 64-bit memory accesses that can be used in the assembler source code, but is otherwise ignored.

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

The alternative syntax permits the addition or subtraction of the offset and the immediate offset to be specified separately, including permitting a subtraction of 0 that cannot be specified using the normal syntax. For more information, see Use of labels in UAL instruction syntax.

## .32

## .64

## &lt;Dd&gt;

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckVFPEnabled(TRUE); constant bits(32) base = if n == 15 then Align(PC32,4) else R[n]; constant bits(32) address = if add then (base + imm32) else (base -imm32); case esize of when 16 H[d] = MemA[address,2]; when 32 S[d] = MemA[address,4]; when 64 constant bits(32) word1 = MemA[address,4]; constant bits(32) word2 = MemA[address+4,4]; // Combine the word-aligned words in the correct order for current endianness. D[d] = if BigEndian(AccessType_ASIMD) then word1:word2 else word2:word1;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.