## F5.1.73 LDR (immediate)

Load Register (immediate) calculates an address from a base register value and an immediate offset, loads a word from memory, and writes it to a register. It can use offset, post-indexed, or pre-indexed addressing. For information about memory accesses see Memory accesses.

This instruction is used by the alias POP (single register).

It has encodings from the following instruction sets: A32 (A1) and T32 (T1, T2, T3, and T4).

## A1

<!-- image -->

## Encoding for the Offset variant

```
Applies when (P == 1 && W == 0) LDR{<c>}{<q>} <Rt>, [<Rn>
```

```
{, #{+/-}<imm>}]
```

## Encoding for the Post-indexed variant

```
Applies when (P == 0 && W == 0) LDR{<c>}{<q>}
```

```
<Rt>, [<Rn>], #{+/-}<imm>
```

## Encoding for the Pre-indexed variant

```
Applies when (P == 1 && W == 1) LDR{<c>}{<q>}
```

```
<Rt>, [<Rn>, #{+/-}<imm>]!
```

## Decode for all variants of this encoding

```
if Rn == '1111' then SEE "LDR (literal)"; if P == '0' && W == '1' then SEE "LDRT"; constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant bits(32) imm32 = ZeroExtend(imm12, 32); constant boolean index = (P == '1'); constant boolean add = (U == '1'); constant boolean wback = (P == '0') || (W == '1'); if wback && n == t then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If wback &amp;&amp; n == t , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction performs all of the loads using the specified addressing mode and the content of the register that is written back is UNKNOWN. In addition, if an exception occurs during such an instruction, the base address might be corrupted so that the instruction cannot be repeated.

T1

## Encoding

```
LDR{<c>}{<q>} <Rt>, [<Rn> {, #{+}<imm>}]
```

## Decode for this encoding

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant bits(32) imm32 = ZeroExtend(imm5:'00', 32); constant boolean index = TRUE; constant boolean add = TRUE; constant boolean wback = FALSE;
```

T2

## Encoding

```
LDR{<c>}{<q>} <Rt>, [SP{, #{+}<imm>}]
```

## Decode for this encoding

```
constant integer t = UInt(Rt); constant integer n = 13; constant bits(32) imm32 = ZeroExtend(imm8:'00', 32); constant boolean index = TRUE; constant boolean add = TRUE; constant boolean wback = FALSE;
```

T3

<!-- image -->

## Encoding

```
LDR{<c>}{<q>} <Rt>, [<Rn> {, #{+}<imm>}]
```

```
LDR{<c>}.W <Rt>, [<Rn> {, #{+}<imm>}] // (<Rt>, <Rn>, <imm> can be represented in T1 or T2)
```

<!-- image -->

<!-- image -->

## Decode for this encoding

```
if Rn == '1111' then SEE "LDR (literal)"; constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant bits(32) imm32 = ZeroExtend(imm12, 32); constant boolean index = TRUE; constant boolean add = TRUE; constant boolean wback = FALSE; if t == 15 &&
```

```
InITBlock() && !LastInITBlock() then UNPREDICTABLE;
```

T4

<!-- image -->

## Encoding for the Offset variant

```
Applies when (P == 1 && U == 0 && W ==
```

```
LDR{<c>}{<q>} <Rt>, [<Rn>
```

```
0) {, #-<imm>}]
```

## Encoding for the Post-indexed variant

```
Applies when (P == 0 && W == 1) LDR{<c>}{<q>}
```

```
<Rt>, [<Rn>], #{+/-}<imm>
```

## Encoding for the Pre-indexed variant

Applies when

```
(P == 1 && W == 1)
```

```
LDR{<c>}{<q>} <Rt>, [<Rn>, #{+/-}<imm>]!
```

## Decode for all variants of this encoding

```
if Rn == '1111' then SEE "LDR (literal)"; if P == '1' && U == '1' && W == '0' then SEE "LDRT"; if P == '0' && W == '0' then UNDEFINED; constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant bits(32) imm32 = ZeroExtend(imm8, 32); constant boolean index = (P == '1'); constant boolean add = (U == '1'); constant boolean wback = (W == '1'); if (wback && n == t) || (t == 15 && InITBlock() && !LastInITBlock()) then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If wback &amp;&amp; n == t , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction performs all of the loads using the specified addressing mode and the content of the register that is written back is UNKNOWN. In addition, if an exception occurs during such an instruction, the base address might be corrupted so that the instruction cannot be repeated.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

For the 'A1 Offset', 'A1 Post-indexed', and 'A1 Pre-indexed' variants: is the general-purpose register to be transferred, encoded in the 'Rt' field. The PC can be used. If the PC is used, the instruction branches to the address (data) loaded to the PC. This is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.

For the 'T1' and 'T2' variants: is the general-purpose register to be transferred, encoded in the 'Rt' field.

For the 'T3', 'T4 Offset', 'T4 Post-indexed', and 'T4 Pre-indexed' variants: is the general-purpose register to be transferred, encoded in the 'Rt' field. The PC can be used, provided the instruction is either outside an IT block or the last instruction of an IT block. If the PC is used, the instruction branches to the address (data) loaded to the PC. This is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.

For the 'A1 Offset', 'A1 Post-indexed', 'A1 Pre-indexed', 'T3', 'T4 Offset', 'T4 Post-indexed', and 'T4 Pre-indexed' variants: is the general-purpose base register, encoded in the 'Rn' field. For PC use see LDR (literal).

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

For the 'A1 Offset', 'A1 Post-indexed', and 'A1 Pre-indexed' variants: is the 12-bit unsigned immediate byte offset, in the range 0 to 4095, defaulting to 0 if omitted, and encoded in the 'imm12' field.

For the 'T1' variant: is the optional positive unsigned immediate byte offset, a multiple of 4, in the range 0 to 124, defaulting to 0 and encoded in the 'imm5' field as &lt;imm&gt;/4.

For the 'T2' variant: is the optional positive unsigned immediate byte offset, a multiple of 4, in the range 0 to 1020, defaulting to 0 and encoded in the 'imm8' field as &lt;imm&gt;/4.

For the 'T3' variant: is an optional 12-bit unsigned immediate byte offset, in the range 0 to 4095, defaulting to 0 and encoded in the 'imm12' field.

For the 'T4 Offset', 'T4 Post-indexed', and 'T4 Pre-indexed' variants: is an 8-bit unsigned immediate byte offset, in the range 0 to 255, defaulting to 0 if omitted, and encoded in the 'imm8' field.

Specifies the offset is added to the base register.

+

## Alias Conditions

| Alias                 | Of variant      | Is preferred when                                                           |
|-----------------------|-----------------|-----------------------------------------------------------------------------|
| POP (single register) | A1 Post-indexed | P == '0' && U == '1' && W == '0' && Rn == '1101' && imm12 == '000000000100' |
| POP (single register) | T4 Post-indexed | Rn == '1101' && P == '0' && U == '1' && W == '1' && imm8 == '00000100'      |

## Operation

```
if CurrentInstrSet() == InstrSet_A32 then if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) offset_addr = if add then (R[n] + imm32) else (R[n] imm32); constant bits(32) address = if index then offset_addr else R[n]; constant bits(32) data = MemU[address,4]; if wback then R[n] = offset_addr; if t == 15 then if address<1:0> == '00' then LoadWritePC(data); else UNPREDICTABLE; else R[t] = data; else if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) offset_addr = if add then (R[n] + imm32) else (R[n] imm32); constant bits(32) address = if index then offset_addr else R[n]; constant bits(32) data = MemU[address,4]; if wback then R[n] = offset_addr; if t == 15 then if address<1:0> == '00' then LoadWritePC(data); else UNPREDICTABLE; else R[t] = data;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.