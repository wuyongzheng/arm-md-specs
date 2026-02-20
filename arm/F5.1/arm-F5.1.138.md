## F5.1.138 PLI (register)

Preload Instruction (register)

Preload Instruction signals the memory system that instruction memory accesses from a specified address are likely in the near future. The memory system can respond by taking actions that are expected to speed up the memory accesses when they do occur, such as pre-loading the cache line containing the specified address into the instruction cache.

The effect of a PLI instruction is IMPLEMENTATION DEFINED. For more information, see Preloading caches.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the Rotate right with extend variant

```
Applies when (imm5 == 00000 && stype == 11) PLI{<c>}{<q>} [<Rn>, {+/-}<Rm> , RRX]
```

## Encoding for the Shift or rotate by value variant

```
Applies when (!(imm5 == 00000 && stype == 11)) PLI{<c>}{<q>} [<Rn>, {+/-}<Rm> {, <shift>
```

```
#<amount>}]
```

## Decode for all variants of this encoding

```
constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean add = (U == '1'); SRType shift_t; integer shift_n; (shift_t, shift_n) = DecodeImmShift(stype, if m == 15 then UNPREDICTABLE;
```

T1

<!-- image -->

## Encoding

```
PLI{<c>}{<q>} [<Rn>, {+}<Rm> {, LSL #<amount>}]
```

```
imm5);
```

## Decode for this encoding

```
(immediate, literal)";
```

```
if Rn == '1111' then SEE "PLI constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean add = TRUE; constant SRType shift_t = SRType_LSL; constant integer shift_n = UInt(imm2); // Armv8-A removes UNPREDICTABLE for R13 if m == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

For the 'Rotate right with extend' and 'Shift or rotate by value' variants: see Standard assembler syntax fields. &lt;c&gt; must be AL or omitted.

For the 'T1' variant: see Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the general-purpose base register, encoded in the 'Rn' field.

Specifies the index register is added to or subtracted from the base register, defaulting to + if omitted and encoded in 'U':

|   U | +/-   |
|-----|-------|
|   0 | -     |
|   1 | +     |

&lt;q&gt;

## &lt;Rn&gt;

+/-

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

For the 'Shift or rotate by value' variant: is the shift amount, in the range 1 to 31 (when &lt;shift&gt; = LSL or ROR) or 1 to 32 (when &lt;shift&gt; = LSR or ASR) encoded in the 'imm5' field as &lt;amount&gt; modulo 32.

For the 'T1' variant: is the shift amount, in the range 0 to 3, defaulting to 0 and encoded in the 'imm2' field.

Specifies the index register is added to the base register.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) offset = Shift(R[m], shift_t, shift_n, PSTATE.C); constant bits(32) address = if add then (R[n] + offset) else (R[n] offset); Hint_PreloadInstr(address);
```

+