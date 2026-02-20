## F5.1.137 PLI (immediate, literal)

Preload Instruction (immediate, literal)

Preload Instruction signals the memory system that instruction memory accesses from a specified address are likely in the near future. The memory system can respond by taking actions that are expected to speed up the memory accesses when they do occur, such as pre-loading the cache line containing the specified address into the instruction cache.

The effect of a PLI instruction is IMPLEMENTATION DEFINED. For more information, see Preloading caches.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1, T2, and T3).

A1

<!-- image -->

## Encoding

```
PLI{<c>}{<q>} [<Rn> {, #{+/-}<imm>}] // (Preferred syntax) PLI{<c>}{<q>} <label> // (Normal form) PLI{<c>}{<q>} [PC, #{+/-}<imm>] // (Alternative form)
```

## Decode for this encoding

```
constant integer n = UInt(Rn); constant bits(32) imm32 = constant boolean add = (U == '1');
```

T1

<!-- image -->

## Encoding

```
PLI{<c>}{<q>} [<Rn> {, #{+}<imm>}]
```

## Decode for this encoding

```
ZeroExtend(imm12, 32);
```

```
if Rn == '1111' then SEE "encoding T3"; constant integer n = UInt(Rn); constant bits(32) imm32 = constant boolean add = TRUE;
```

```
ZeroExtend(imm12, 32);
```

T2

<!-- image -->

## Encoding

```
PLI{<c>}{<q>} [<Rn> {, #-<imm>}]
```

## Decode for this encoding

```
ZeroExtend(imm8, 32);
```

```
if Rn == '1111' then SEE "encoding T3"; constant integer n = UInt(Rn); constant bits(32) imm32 = constant boolean add = FALSE;
```

T3

<!-- image -->

## Encoding

```
PLI{<c>}{<q>} <label> // (Preferred syntax) PLI{<c>}{<q>} [PC, #{+/-}<imm>] // (Alternative syntax)
```

## Decode for this encoding

```
constant integer n = 15; constant bits(32) imm32 = constant boolean add = (U == '1');
```

```
ZeroExtend(imm12, 32);
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

<!-- image -->

&lt;c&gt;

For the 'A1' variant: see Standard assembler syntax fields. Must be AL or omitted.

For the 'T1', 'T2', and 'T3' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the general-purpose base register, encoded in the 'Rn' field.

<!-- image -->

&lt;Rn&gt;

+/-

Specifies the offset is added to or subtracted from the base register, defaulting to + if omitted and encoded in 'U':

|   U | +/-   |
|-----|-------|
|   0 | -     |
|   1 | +     |

## &lt;imm&gt;

For the 'A1' variant: is the optional 12-bit unsigned immediate byte offset, in the range 0 to 4095, defaulting to 0 and encoded in the 'imm12' field.

For the 'T1' variant: is an optional 12-bit unsigned immediate byte offset, in the range 0 to 4095, defaulting to 0 and encoded in the 'imm12' field.

For the 'T2' variant: is an 8-bit unsigned immediate byte offset, in the range 0 to 255, defaulting to 0 if omitted, and encoded in the 'imm8' field.

For the 'T3' variant: is a 12-bit unsigned immediate byte offset, in the range 0 to 4095, encoded in the 'imm12' field.

## &lt;label&gt;

The label of the instruction that is likely to be accessed in the near future. The assembler calculates the required value of the offset from the Align(PC, 4) value of the instruction to this label. The offset must be in the range -4095 to 4095.

If the offset is zero or positive, imm32 is equal to the offset and add == TRUE .

If the offset is negative, imm32 is equal to minus the offset and add == FALSE .

Specifies the offset is added to the base register.

For the literal forms of the instruction, encoding T3 is used, or Rn is encoded as 0b1111 in encoding A1, to indicate that the PC is the base register.

The alternative literal syntax permits the addition or subtraction of the offset and the immediate offset to be specified separately, including permitting a subtraction of 0 that cannot be specified using the normal syntax. For more information, see Use of labels in UAL instruction syntax.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) base = if n == 15 then Align(PC32,4) else R[n]; constant bits(32) address = if add then (base + imm32) else (base -imm32); Hint_PreloadInstr(address);
```

+