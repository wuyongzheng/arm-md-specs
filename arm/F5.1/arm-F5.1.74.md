## F5.1.74 LDR (literal)

Load Register (literal) calculates an address from the PC value and an immediate offset, loads a word from memory, and writes it to a register. For information about memory accesses see Memory accesses.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding

```
Applies when (!(P == '0' && W == '1')) LDR{<c>}{<q>} <Rt>, <label> // (Normal form) LDR{<c>}{<q>} <Rt>, [PC, #{+/-}<imm>] // (Alternative form)
```

## Decode for this encoding

```
if P == '0' && W == '1' then SEE "LDRT"; constant integer t = UInt(Rt); constant bits(32) imm32 = ZeroExtend(imm12, 32); constant boolean add = (U == '1'); constant boolean wback = (P == '0') || (W == '1'); if wback then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If wback , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes with the additional decode: wback = FALSE;.
- The instruction treats bit[24] as the P bit, and bit[21] as the writeback (W) bit, and uses the same addressing mode as described in LDR (immediate). The instruction uses post-indexed addressing when P == '0' and uses pre-indexed addressing otherwise. The instruction is handled as described in Using R15.

T1

## Encoding

```
LDR{<c>}{<q>} <Rt>, <label> // (Normal form)
```

<!-- image -->

## Decode for this encoding

```
constant integer t = UInt(Rt); constant bits(32) imm32 = ZeroExtend(imm8:'00', 32); constant boolean add = TRUE;
```

T2

<!-- image -->

## Encoding

```
LDR{<c>}.W <Rt>, <label> // (Preferred syntax) LDR{<c>}{<q>} <Rt>, <label> // (Preferred syntax, and <Rt>, <label> can be represented in T1) LDR{<c>}{<q>} <Rt>, [PC, #{+/-}<imm>] // (Alternative syntax)
```

## Decode for this encoding

```
constant integer t = UInt(Rt); constant bits(32) imm32 = ZeroExtend(imm12, 32); constant boolean add = (U == '1'); if t == 15 && InITBlock() && !LastInITBlock() then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

For the 'A1' variant: is the general-purpose register to be transferred, encoded in the 'Rt' field. The PC can be used. If the PC is used, the instruction branches to the address (data) loaded to the PC. This is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.

For the 'T1' variant: is the general-purpose register to be transferred, encoded in the 'Rt' field.

For the 'T2' variant: is the general-purpose register to be transferred, encoded in the 'Rt' field. The SP can be used. The PC can be used, provided the instruction is either outside an IT block or the last instruction of an IT block. If the PC is used, the instruction branches to the address (data) loaded to the PC. This is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.

## &lt;label&gt;

For the 'A1' and 'T2' variants: the label of the literal data item that is to be loaded into &lt;Rt&gt; . The assembler calculates the required value of the offset from the Align(PC, 4) value of the instruction to this label. Permitted values of the offset are -4095 to 4095.

If the offset is zero or positive, imm32 is equal to the offset and add == TRUE , encoded as U == 1.

&lt;q&gt;

## &lt;Rt&gt;

+/-

If the offset is negative, imm32 is equal to minus the offset and add == FALSE , encoded as U == 0.

For the 'T1' variant: the label of the literal data item that is to be loaded into &lt;Rt&gt; . The assembler calculates the required value of the offset from the Align(PC, 4) value of the instruction to this label. Permitted values of the offset are Multiples of four in the range 0 to 1020.

Specifies the offset is added to or subtracted from the base register, defaulting to + if omitted and encoded in 'U':

|   U | +/-   |
|-----|-------|
|   0 | -     |
|   1 | +     |

## &lt;imm&gt;

For the 'A1' variant: is the 12-bit unsigned immediate byte offset, in the range 0 to 4095, defaulting to 0 if omitted, and encoded in the 'imm12' field.

For the 'T2' variant: is a 12-bit unsigned immediate byte offset, in the range 0 to 4095, encoded in the 'imm12' field.

The alternative syntax permits the addition or subtraction of the offset and the immediate offset to be specified separately, including permitting a subtraction of 0 that cannot be specified using the normal syntax. For more information, see Use of labels in UAL instruction syntax.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) base = Align(PC32,4); constant bits(32) address = if add then (base + imm32) else (base -imm32); constant bits(32) data = MemU[address,4]; if t == 15 then if address<1:0> == '00' then LoadWritePC(data); else UNPREDICTABLE; else R[t] = data;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.