## F5.1.87 LDRH (immediate)

Load Register Halfword (immediate) calculates an address from a base register value and an immediate offset, loads a halfword from memory, zero-extends it to form a 32-bit word, and writes it to a register. It can use offset, post-indexed, or pre-indexed addressing. For information about memory accesses see Memory accesses.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1, T2, and T3).

A1

<!-- image -->

## Encoding for the Offset variant

```
Applies when (P == 1 && W == 0) LDRH{<c>}{<q>} <Rt>, [<Rn>
```

```
{, #{+/-}<imm>}]
```

## Encoding for the Post-indexed variant

```
Applies when (P == 0 && W == 0) LDRH{<c>}{<q>}
```

```
<Rt>, [<Rn>], #{+/-}<imm>
```

## Encoding for the Pre-indexed variant

```
Applies when (P == 1 && W == 1) LDRH{<c>}{<q>}
```

```
<Rt>, [<Rn>, #{+/-}<imm>]!
```

## Decode for all variants of this encoding

```
if Rn == '1111' then SEE "LDRH (literal)"; if P == '0' && W == '1' then SEE "LDRHT"; constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant bits(32) imm32 = ZeroExtend(imm4H:imm4L, 32); constant boolean index = (P == '1'); constant boolean add = (U == '1'); constant boolean wback = (P == '0') || (W == '1'); if t == 15 || (wback && n == t) then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If wback &amp;&amp; n == t , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction performs all of the loads using the specified addressing mode and the content of the register that is written back is UNKNOWN. In addition, if an exception occurs during such an instruction, the base address might be corrupted so that the instruction cannot be repeated.

T1

## Encoding

<!-- image -->

## Decode for this encoding

```
ZeroExtend(imm5:'0', 32);
```

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant bits(32) imm32 = constant boolean index = TRUE; constant boolean add = TRUE; constant boolean wback = FALSE;
```

T2

<!-- image -->

## Encoding

```
LDRH{<c>}{<q>} <Rt>, [<Rn>
```

```
LDRH{<c>}.W <Rt>, [<Rn> {, #{+}<imm>}] // (<Rt>, <Rn>, <imm> can be represented
```

## Decode for this encoding

```
if Rt == '1111' then SEE "PLD (immediate)"; if Rn == '1111' then SEE "LDRH (literal)"; constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant bits(32) imm32 = constant boolean index = TRUE; constant boolean add = TRUE; constant boolean wback = FALSE; // Armv8-A removes UNPREDICTABLE for R13
```

<!-- image -->

```
{, #{+}<imm>}] in T1)
```

```
ZeroExtend(imm12, 32);
```

T3

<!-- image -->

L

## Encoding for the Offset variant

```
Applies when (Rt != 1111 && P == 1 && U == 0 && W ==
```

```
LDRH{<c>}{<q>} <Rt>, [<Rn>
```

```
0) {, #-<imm>}]
```

## Encoding for the Post-indexed variant

Applies when

```
<Rt>, [<Rn>], #{+/-}<imm>
```

```
(P == 0 && W == 1) LDRH{<c>}{<q>}
```

## Encoding for the Pre-indexed variant

```
Applies when (P == 1 && W == 1) LDRH{<c>}{<q>} <Rt>, [<Rn>, #{+/-}<imm>]!
```

## Decode for all variants of this encoding

```
if Rn == '1111' then SEE "LDRH (literal)"; if Rt == '1111' && P == '1' && U == '0' && W == '0' then SEE "PLDW if P == '1' && U == '1' && W == '0' then SEE "LDRHT"; if P == '0' && W == '0' then UNDEFINED; constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant bits(32) imm32 = ZeroExtend(imm8, 32); constant boolean index = (P == '1'); constant boolean add = (U == '1'); constant boolean wback = (W == '1'); if (t == 15 && W == '1') || (wback && n == t) then UNPREDICTABLE; // Armv8-A removes UNPREDICTABLE for R13
```

## CONSTRAINED UNPREDICTABLE behavior

If wback &amp;&amp; n == t , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction performs all of the loads using the specified addressing mode and the content of the register that is written back is UNKNOWN. In addition, if an exception occurs during such an instruction, the base address might be corrupted so that the instruction cannot be repeated.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

```
(immediate)";
```

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the general-purpose register to be transferred, encoded in the 'Rt' field.

For the 'A1 Offset', 'A1 Post-indexed', 'A1 Pre-indexed', 'T2', 'T3 Offset', 'T3 Post-indexed', and 'T3 Pre-indexed' variants: is the general-purpose base register, encoded in the 'Rn' field. For PC use see LDRH (literal).

For the 'T1' variant: is the general-purpose base register, encoded in the 'Rn' field.

Specifies the offset is added to or subtracted from the base register, defaulting to + if omitted and encoded in 'U':

|   U | +/-   |
|-----|-------|
|   0 | -     |
|   1 | +     |

&lt;q&gt;

## &lt;Rt&gt;

## &lt;Rn&gt;

+/-

## &lt;imm&gt;

For the 'A1 Offset', 'A1 Post-indexed', and 'A1 Pre-indexed' variants: is the 8-bit unsigned immediate byte offset, in the range 0 to 255, defaulting to 0 if omitted, and encoded in the 'imm4H:imm4L' field.

For the 'T1' variant: is the optional positive unsigned immediate byte offset, a multiple of 2, in the range 0 to 62, defaulting to 0 and encoded in the 'imm5' field as &lt;imm&gt;/2.

For the 'T2' variant: is an optional 12-bit unsigned immediate byte offset, in the range 0 to 4095, defaulting to 0 and encoded in the 'imm12' field.

For the 'T3 Offset', 'T3 Post-indexed', and 'T3 Pre-indexed' variants: is an 8-bit unsigned immediate byte offset, in the range 0 to 255, defaulting to 0 if omitted, and encoded in the 'imm8' field.

Specifies the offset is added to the base register.

## Operation

```
if CurrentInstrSet() == InstrSet_A32 then if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) offset_addr = if add then (R[n] + imm32) else (R[n] constant bits(32) address = if index then offset_addr else R[n]; constant bits(16) data = MemU[address,2]; if wback then R[n] = offset_addr; R[t] = ZeroExtend(data, 32); else if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) offset_addr = if add then (R[n] + imm32) else (R[n] constant bits(32) address = if index then offset_addr else R[n];
```

+

```
imm32); imm32);
```

```
constant bits(16) data = MemU[address,2]; if wback then R[n] = offset_addr; R[t] = ZeroExtend(data, 32);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.