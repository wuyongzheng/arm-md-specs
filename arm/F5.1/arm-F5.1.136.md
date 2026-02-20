## F5.1.136 PLD, PLDW (register)

Preload Data (register) signals the memory system that data memory accesses from a specified address are likely in the near future. The memory system can respond by taking actions that are expected to speed up the memory accesses when they do occur, such as preloading the cache line containing the specified address into the data cache.

The PLD instruction signals that the likely memory access is a read, and the PLDW instruction signals that it is a write.

The effect of a PLD or PLDW instruction is IMPLEMENTATION DEFINED. For more information, see Preloading caches.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the Preload read, optional shift or rotate variant

```
Applies when
```

```
(R == 1 && !(imm5 == 00000 && stype == 11)) PLD{<c>}{<q>} [<Rn>, {+/-}<Rm> {, <shift> #<amount>}]
```

## Encoding for the Preload read, rotate right with extend variant

```
Applies when (R == 1 && imm5 == 00000 && stype ==
```

```
PLD{<c>}{<q>} [<Rn>, {+/-}<Rm>
```

```
11) , RRX]
```

## Encoding for the Preload write, optional shift or rotate variant

```
Applies when (R == 0 && !(imm5 == 00000 && stype == 11)) PLDW{<c>}{<q>} [<Rn>, {+/-}<Rm> {, <shift> #<amount>}]
```

## Encoding for the Preload write, rotate right with extend variant

```
Applies when (R == 0 && imm5 == 00000 && stype == 11) PLDW{<c>}{<q>} [<Rn>, {+/-}<Rm> , RRX]
```

## Decode for all variants of this encoding

```
constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean add = (U == '1'); constant boolean is_pldw = (R == '0'); SRType shift_t; integer shift_n; (shift_t, shift_n) = DecodeImmShift(stype, imm5); if m == 15 || (n == 15 && is_pldw) then
```

```
UNPREDICTABLE;
```

T1

<!-- image -->

## Encoding for the Preload read variant

```
Applies when (W == 0)
```

```
PLD{<c>}{<q>} [<Rn>, {+}<Rm> {, LSL
```

## Encoding for the Preload write variant

Applies when (W == 1)

```
PLDW{<c>}{<q>} [<Rn>, {+}<Rm> {, LSL #<amount>}]
```

## Decode for all variants of this encoding

```
if Rn == '1111' then SEE "PLD (literal)"; constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean add = TRUE; constant boolean is_pldw = (W == '1'); constant SRType shift_t = SRType_LSL; constant integer shift_n = UInt(imm2); // Armv8-A removes UNPREDICTABLE for R13 if m == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

For the 'Preload read, optional shift or rotate', 'Preload read, rotate right with extend', 'Preload write, optional shift or rotate', and 'Preload write, rotate right with extend' variants: see Standard assembler syntax fields. &lt;c&gt; must be AL or omitted.

For the 'Preload read' and 'Preload write' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

For the 'Preload read, optional shift or rotate', 'Preload read, rotate right with extend', 'Preload write, optional shift or rotate', and 'Preload write, rotate right with extend' variants: is the general-purpose base register, encoded in the 'Rn' field. The PC can be used.

For the 'Preload read' and 'Preload write' variants: is the general-purpose base register, encoded in the 'Rn' field.

Specifies the index register is added to or subtracted from the base register, defaulting to + if omitted and encoded in 'U':

&lt;q&gt;

## &lt;Rn&gt;

+/-

```
#<amount>}]
```

## &lt;Rm&gt;

Is the general-purpose index register, encoded in the 'Rm' field.

## &lt;shift&gt;

Is the type of shift to be applied to the index register, encoded in 'stype':

|   stype | <shift>   |
|---------|-----------|
|      00 | LSL       |
|      01 | LSR       |
|      10 | ASR       |
|      11 | ROR       |

## &lt;amount&gt;

For the 'Preload read, optional shift or rotate' and 'Preload write, optional shift or rotate' variants: is the shift amount, in the range 1 to 31 (when &lt;shift&gt; = LSL or ROR) or 1 to 32 (when &lt;shift&gt; = LSR or ASR) encoded in the 'imm5' field as &lt;amount&gt; modulo 32.

For the 'Preload read' and 'Preload write' variants: is the shift amount, in the range 0 to 3, defaulting to 0 and encoded in the 'imm2' field.

Specifies the index register is added to the base register.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) offset = Shift(R[m], shift_t, shift_n, PSTATE.C); constant bits(32) address = if add then (R[n] + offset) else (R[n] offset); if is_pldw then Hint_PreloadDataForWrite(address); else Hint_PreloadData(address);
```

+

|   U | +/-   |
|-----|-------|
|   0 | -     |
|   1 | +     |