## F5.1.135 PLD (literal)

Preload Data (literal) signals the memory system that data memory accesses from a specified address are likely in the near future. The memory system can respond by taking actions that are expected to speed up the memory accesses when they do occur, such as preloading the cache line containing the specified address into the data cache.

The effect of a PLD instruction is IMPLEMENTATION DEFINED. For more information, see Preloading caches.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
PLD{<c>}{<q>} <label> // (Normal form) PLD{<c>}{<q>} [PC, #{+/-}<imm>] // (Alternative form)
```

## Decode for this encoding

```
constant bits(32) imm32 = constant boolean add = (U == '1');
```

T1

<!-- image -->

## Encoding

```
PLD{<c>}{<q>} <label> // (Preferred syntax) PLD{<c>}{<q>} [PC, #{+/-}<imm>] // (Alternative syntax)
```

## Decode for this encoding

```
constant bits(32) imm32 = constant boolean add = (U == '1');
```

```
ZeroExtend(imm12, 32);
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

```
ZeroExtend(imm12, 32);
```

## Assembler Symbols

&lt;c&gt;

For the 'A1' variant: see Standard assembler syntax fields. Must be AL or omitted.

For the 'T1' variant: see Standard assembler syntax fields.

&lt;q&gt;

See Standard assembler syntax fields.

## &lt;label&gt;

The label of the literal data item that is likely to be accessed in the near future. The assembler calculates the required value of the offset from the Align(PC, 4) value of the instruction to this label. The offset must be in the range -4095 to 4095.

If the offset is zero or positive, imm32 is equal to the offset and add == TRUE .

If the offset is negative, imm32 is equal to minus the offset and add == FALSE .

Specifies the offset is added to or subtracted from the base register, defaulting to + if omitted and encoded in 'U':

|   U | +/-   |
|-----|-------|
|   0 | -     |
|   1 | +     |

+/-

## &lt;imm&gt;

For the 'A1' variant: is the 12-bit unsigned immediate byte offset, in the range 0 to 4095, encoded in the 'imm12' field.

For the 'T1' variant: is a 12-bit unsigned immediate byte offset, in the range 0 to 4095, encoded in the 'imm12' field.

The alternative syntax permits the addition or subtraction of the offset and the immediate offset to be specified separately, including permitting a subtraction of 0 that cannot be specified using the normal syntax. For more information, see Use of labels in UAL instruction syntax.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) address = (if add then (Align(PC32,4) + imm32) else (Align(PC32,4) imm32)); Hint_PreloadData(address);
```