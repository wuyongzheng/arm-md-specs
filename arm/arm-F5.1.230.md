## F5.1.230 STR (immediate)

Store Register (immediate) calculates an address from a base register value and an immediate offset, and stores a word from a register to memory. It can use offset, post-indexed, or pre-indexed addressing. For information about memory accesses see Memory accesses.

This instruction is used by the alias PUSH (single register).

It has encodings from the following instruction sets: A32 (A1) and T32 (T1, T2, T3, and T4).

## A1

<!-- image -->

## Encoding for the Offset variant

```
Applies when (P == 1 && W == 0) STR{<c>}{<q>} <Rt>, [<Rn>
```

```
{, #{+/-}<imm>}]
```

## Encoding for the Post-indexed variant

```
Applies when (P == 0 && W == 0) STR{<c>}{<q>}
```

```
<Rt>, [<Rn>], #{+/-}<imm>
```

## Encoding for the Pre-indexed variant

```
Applies when (P == 1 && W == 1) STR{<c>}{<q>}
```

```
<Rt>, [<Rn>, #{+/-}<imm>]!
```

## Decode for all variants of this encoding

```
if P == '0' && W == '1' then SEE "STRT"; constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant bits(32) imm32 = ZeroExtend(imm12, 32); constant boolean index = (P == '1'); constant boolean add = (U == '1'); constant boolean wback = (P == '0') || (W == '1'); if wback && (n == 15 || n == t) then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If wback &amp;&amp; n == t , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The store instruction executes but the value stored is UNKNOWN.

If wback &amp;&amp; n == 15 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes without writeback of the base address.
- The instruction uses the addressing mode described in the equivalent immediate offset instruction.

T1

## Encoding

```
STR{<c>}{<q>} <Rt>, [<Rn> {, #{+}<imm>}]
```

## Decode for this encoding

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant bits(32) imm32 = ZeroExtend(imm5:'00', 32); constant boolean index = TRUE; constant boolean add = TRUE; constant boolean wback = FALSE;
```

T2

## Encoding

```
STR{<c>}{<q>} <Rt>, [SP{, #{+}<imm>}]
```

## Decode for this encoding

```
constant integer t = UInt(Rt); constant integer n = 13; constant bits(32) imm32 = ZeroExtend(imm8:'00', 32); constant boolean index = TRUE; constant boolean add = TRUE; constant boolean wback = FALSE;
```

T3

<!-- image -->

## Encoding

```
STR{<c>}{<q>} <Rt>, [<Rn> {, #{+}<imm>}]
```

```
STR{<c>}.W <Rt>, [<Rn> {, #{+}<imm>}] // (<Rt>, <Rn>, <imm> can be represented in T1 or T2)
```

<!-- image -->

<!-- image -->

## Decode for this encoding

```
ZeroExtend(imm12, 32);
```

```
if Rn == '1111' then UNDEFINED; constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant bits(32) imm32 = constant boolean index = TRUE; constant boolean add = TRUE; constant boolean wback = FALSE; if t == 15 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If t == 15 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The store instruction performs the store using the specified addressing mode but the value corresponding to R15 is UNKNOWN.

T4

<!-- image -->

## Encoding for the Offset variant

```
Applies when (P == 1 && U == 0 && W == 0) STR{<c>}{<q>} <Rt>, [<Rn> {, #-<imm>}]
```

## Encoding for the Post-indexed variant

```
Applies when (P == 0 && W == 1) STR{<c>}{<q>} <Rt>, [<Rn>], #{+/-}<imm>
```

## Encoding for the Pre-indexed variant

```
Applies when (P == 1 && W == 1) STR{<c>}{<q>}
```

```
<Rt>, [<Rn>, #{+/-}<imm>]!
```

## Decode for all variants of this encoding

```
UNDEFINED;
```

```
if P == '1' && U == '1' && W == '0' then SEE "STRT"; if Rn == '1111' || (P == '0' && W == '0') then constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant bits(32) imm32 = ZeroExtend(imm8, 32); constant boolean index = (P == '1'); constant boolean add = (U == '1'); constant boolean wback = (W == '1'); if t == 15 || (wback && n == t) then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If wback &amp;&amp; n == t , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The store instruction executes but the value stored is UNKNOWN.

If t == 15 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The store instruction performs the store using the specified addressing mode but the value corresponding to R15 is UNKNOWN.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

&lt;q&gt;

See Standard assembler syntax fields.

## &lt;Rt&gt;

## &lt;Rn&gt;

+/-

For the 'A1 Offset', 'A1 Post-indexed', and 'A1 Pre-indexed' variants: is the general-purpose register to be transferred, encoded in the 'Rt' field. The PC can be used, but this is deprecated.

For the 'T1', 'T2', 'T3', 'T4 Offset', 'T4 Post-indexed', and 'T4 Pre-indexed' variants: is the general-purpose register to be transferred, encoded in the 'Rt' field.

For the 'A1 Offset', 'A1 Post-indexed', and 'A1 Pre-indexed' variants: is the general-purpose base register, encoded in the 'Rn' field. The PC can be used in the offset variant, but this is deprecated.

For the 'T1', 'T3', 'T4 Offset', 'T4 Post-indexed', and 'T4 Pre-indexed' variants: is the general-purpose base register, encoded in the 'Rn' field.

Specifies the offset is added to or subtracted from the base register, defaulting to + if omitted and encoded in 'U':

|   U | +/-   |
|-----|-------|
|   0 | -     |
|   1 | +     |

## &lt;imm&gt;

For the 'A1 Offset', 'A1 Post-indexed', and 'A1 Pre-indexed' variants: is the 12-bit unsigned immediate byte offset, in the range 0 to 4095, defaulting to 0 if omitted, and encoded in the 'imm12' field.

For the 'T1' variant: is the optional positive unsigned immediate byte offset, a multiple of 4, in the range 0 to 124, defaulting to 0 and encoded in the 'imm5' field as &lt;imm&gt;/4.

+

For the 'T2' variant: is the optional positive unsigned immediate byte offset, a multiple of 4, in the range 0 to 1020, defaulting to 0 and encoded in the 'imm8' field as &lt;imm&gt;/4.

For the 'T3' variant: is an optional 12-bit unsigned immediate byte offset, in the range 0 to 4095, defaulting to 0 and encoded in the 'imm12' field.

For the 'T4 Offset', 'T4 Post-indexed', and 'T4 Pre-indexed' variants: is an 8-bit unsigned immediate byte offset, in the range 0 to 255, defaulting to 0 if omitted, and encoded in the 'imm8' field.

Specifies the offset is added to the base register.

## Alias Conditions

| Alias                  | Of variant     | Is preferred when                                                           |
|------------------------|----------------|-----------------------------------------------------------------------------|
| PUSH (single register) | A1 Pre-indexed | P == '1' && U == '0' && W == '1' && Rn == '1101' && imm12 == '000000000100' |
| PUSH (single register) | T4 Pre-indexed | Rn == '1101' && P == '1' && U == '0' && W == '1' && imm8 == '00000100'      |

## Operation

```
if CurrentInstrSet() == InstrSet_A32 then if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) offset_addr = if add then (R[n] + imm32) else (R[n] imm32); constant bits(32) address = if index then offset_addr else R[n]; MemU[address,4] = if t == 15 then PCStoreValue() else R[t]; if wback then R[n] = offset_addr; else if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) offset_addr = if add then (R[n] + imm32) else (R[n] imm32); constant bits(32) address = if index then offset_addr else R[n]; MemU[address,4] = R[t]; if wback then R[n] = offset_addr;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.