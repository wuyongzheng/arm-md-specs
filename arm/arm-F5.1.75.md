## F5.1.75 LDR (register)

Load Register (register) calculates an address from a base register value and an offset register value, loads a word from memory, and writes it to a register. The offset register value can optionally be shifted. For information about memory accesses, see Memory accesses.

The T32 form of LDR (register) does not support register writeback.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding for the Offset variant

```
Applies when (P == 1 && W == 0) LDR{<c>}{<q>}
```

```
<Rt>, [<Rn>, {+/-}<Rm>{, <shift>}]
```

## Encoding for the Post-indexed variant

```
Applies when (P == 0 && W == 0) LDR{<c>}{<q>} <Rt>, [<Rn>], {+/-}<Rm>{,
```

## Encoding for the Pre-indexed variant

Applies when

```
<Rt>, [<Rn>, {+/-}<Rm>{, <shift>}]!
```

```
(P == 1 && W == 1) LDR{<c>}{<q>}
```

## Decode for all variants of this encoding

```
if P == '0' && W == '1' then SEE "LDRT"; constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean index = (P == '1'); constant boolean add = (U == '1'); constant boolean wback = (P == '0') || (W == '1'); SRType shift_t; integer shift_n; (shift_t, shift_n) = DecodeImmShift(stype, imm5); if m == 15 then UNPREDICTABLE; if wback && (n == 15 || n == t) then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If wback &amp;&amp; n == t , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction performs all of the loads using the specified addressing mode and the content of the register that is written back is UNKNOWN. In addition, if an exception occurs during such as instruction, the base address might be corrupted so that the instruction cannot be repeated.

```
<shift>}
```

T1

## Encoding

```
LDR{<c>}{<q>} <Rt>, [<Rn>, {+}<Rm>]
```

## Decode for this encoding

```
= SRType_LSL;
```

L

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant SRType shift_t constant integer shift_n = 0; constant boolean index = TRUE; constant boolean add = TRUE; constant boolean wback = FALSE;
```

T2

<!-- image -->

## Encoding

```
LDR{<c>}{<q>} <Rt>, [<Rn>, {+}<Rm>{, LSL #<imm>}] LDR{<c>}.W <Rt>, [<Rn>, {+}<Rm>] // (<Rt>, <Rn>, <Rm> can be represented in T1)
```

## Decode for this encoding

```
if Rn == '1111' then SEE "LDR (literal)"; constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant SRType shift_t = SRType_LSL; constant integer shift_n = UInt(imm2); // Armv8-A removes UNPREDICTABLE for R13 if m == 15 then UNPREDICTABLE; if t == 15 && InITBlock() && !LastInITBlock() then UNPREDICTABLE; constant boolean index = TRUE; constant boolean add = TRUE; constant boolean wback = FALSE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

<!-- image -->

B

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

&lt;q&gt;

See Standard assembler syntax fields.

## &lt;Rt&gt;

## &lt;Rn&gt;

For the 'Offset', 'Post-indexed', and 'Pre-indexed' variants: is the general-purpose register to be transferred, encoded in the 'Rt' field. The PC can be used. If the PC is used, the instruction branches to the address (data) loaded to the PC. This branch is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.

For the 'T1' variant: is the general-purpose register to be transferred, encoded in the 'Rt' field.

For the 'T2' variant: is the general-purpose register to be transferred, encoded in the 'Rt' field. The PC can be used, provided the instruction is either outside an IT block or the last instruction of an IT block. If the PC is used, the instruction branches to the address (data) loaded to the PC. This is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.

For the 'Offset', 'Post-indexed', and 'Pre-indexed' variants: is the general-purpose base register, encoded in the 'Rn' field. The PC can be used in the offset variant.

For the 'T1' and 'T2' variants: is the general-purpose base register, encoded in the 'Rn' field.

- +/-Specifies the index register is added to or subtracted from the base register, defaulting to + if omitted and encoded in 'U':

|   U | +/-   |
|-----|-------|
|   0 | -     |
|   1 | +     |

## &lt;Rm&gt;

Is the general-purpose index register, encoded in the 'Rm' field.

## &lt;shift&gt;

The shift to apply to the value read from &lt;Rm&gt; . If absent, no shift is applied. Otherwise, see Shifts applied to a register.

+

Specifies the index register is added to the base register.

## &lt;imm&gt;

If present, the size of the left shift to apply to the value from &lt;Rm&gt; , in the range 1-3. &lt;imm&gt; is encoded in imm2. If absent, no shift is specified and imm2 is encoded as 0b00 .

## Operation

```
if CurrentInstrSet() == InstrSet_A32 then if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) offset = Shift(R[m], shift_t, shift_n, PSTATE.C); constant bits(32) offset_addr = if add then (R[n] + offset) else (R[n] offset); constant bits(32) address = if index then offset_addr else R[n]; constant bits(32) data = MemU[address,4]; if wback then R[n] = offset_addr; if t == 15 then if address<1:0> == '00' then LoadWritePC(data); else UNPREDICTABLE; else R[t] = data; else if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) offset = Shift(R[m], shift_t, shift_n, PSTATE.C); constant bits(32) offset_addr = (R[n] + offset); constant bits(32) address = offset_addr; constant bits(32) data = MemU[address,4]; if t == 15 then if address<1:0> == '00' then LoadWritePC(data); else UNPREDICTABLE; else R[t] = data;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.