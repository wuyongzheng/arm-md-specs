## F5.1.134 PLD, PLDW (immediate)

Preload Data (immediate) signals the memory system that data memory accesses from a specified address are likely in the near future. The memory system can respond by taking actions that are expected to speed up the memory accesses when they do occur, such as preloading the cache line containing the specified address into the data cache.

The PLD instruction signals that the likely memory access is a read, and the PLDW instruction signals that it is a write.

The effect of a PLD or PLDW instruction is IMPLEMENTATION DEFINED. For more information, see Preloading caches.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding for the Preload read variant

```
Applies when (R == 1) PLD{<c>}{<q>} [<Rn> {, #{+/-}<imm>}]
```

## Encoding for the Preload write variant

Applies when

```
(R == 0) PLDW{<c>}{<q>} [<Rn> {, #{+/-}<imm>}]
```

## Decode for all variants of this encoding

```
ZeroExtend(imm12, 32);
```

```
if Rn == '1111' then SEE "PLD (literal)"; constant integer n = UInt(Rn); constant bits(32) imm32 = constant boolean add = (U == '1'); constant boolean is_pldw = (R == '0');
```

T1

<!-- image -->

## Encoding for the Preload read variant

Applies when

(W == 0)

PLD{&lt;c&gt;}{&lt;q&gt;}

[&lt;Rn&gt;

{, #{+}&lt;imm&gt;}]

## Encoding for the Preload write variant

```
Applies when (W == 1) PLDW{<c>}{<q>} [<Rn> {, #{+}<imm>}]
```

## Decode for all variants of this encoding

```
ZeroExtend(imm12, 32);
```

```
if Rn == '1111' then SEE "PLD (literal)"; constant integer n = UInt(Rn); constant bits(32) imm32 = constant boolean add = TRUE; constant boolean is_pldw = (W == '1');
```

T2

<!-- image -->

## Encoding for the Preload read variant

```
Applies when (W == 0) PLD{<c>}{<q>} [<Rn> {, #-<imm>}]
```

## Encoding for the Preload write variant

```
Applies when (W == 1) PLDW{<c>}{<q>} [<Rn> {, #-<imm>}]
```

## Decode for all variants of this encoding

```
ZeroExtend(imm8, 32);
```

```
if Rn == '1111' then SEE "PLD (literal)"; constant integer n = UInt(Rn); constant bits(32) imm32 = constant boolean add = FALSE; constant boolean is_pldw = (W == '1');
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

For the 'A1 Preload read' and 'A1 Preload write' variants: see Standard assembler syntax fields. Must be AL or omitted.

For the 'T1 Preload read', 'T1 Preload write', 'T2 Preload read', and 'T2 Preload write' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the general-purpose base register, encoded in the 'Rn' field. If the PC is used, see PLD (literal).

<!-- image -->

&lt;Rn&gt;

+/-

Specifies the offset is added to or subtracted from the base register, defaulting to + if omitted and encoded in 'U':

|   U | +/-   |
|-----|-------|
|   0 | -     |
|   1 | +     |

## &lt;imm&gt;

For the 'A1 Preload read' and 'A1 Preload write' variants: is the optional 12-bit unsigned immediate byte offset, in the range 0 to 4095, defaulting to 0 and encoded in the 'imm12' field.

For the 'T1 Preload read' and 'T1 Preload write' variants: is an optional 12-bit unsigned immediate byte offset, in the range 0 to 4095, defaulting to 0 and encoded in the 'imm12' field.

For the 'T2 Preload read' and 'T2 Preload write' variants: is an 8-bit unsigned immediate byte offset, in the range 0 to 255, defaulting to 0 if omitted, and encoded in the 'imm8' field.

Specifies the offset is added to the base register.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) address = if add then (R[n] + imm32) else (R[n] imm32); if is_pldw then Hint_PreloadDataForWrite(address); else Hint_PreloadData(address);
```

+