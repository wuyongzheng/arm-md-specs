## F5.1.92 LDRSB (literal)

Load Register Signed Byte (literal) calculates an address from the PC value and an immediate offset, loads a byte from memory, sign-extends it to form a 32-bit word, and writes it to a register. For information about memory accesses see Memory accesses.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
Applies when (!(P == '0' && W == '1')) LDRSB{<c>}{<q>} <Rt>, <label> // (Normal form) LDRSB{<c>}{<q>} <Rt>, [PC, #{+/-}<imm>] // (Alternative form)
```

## Decode for this encoding

```
if P == '0' && W == '1' then SEE "LDRSBT"; constant integer t = UInt(Rt); constant bits(32) imm32 = ZeroExtend(imm4H:imm4L, 32); constant boolean add = (U == '1'); constant boolean wback = (P == '0') || (W == '1'); if t == 15 || wback then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If wback , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes with the additional decode: wback = FALSE;.
- The instruction treats bit[24] as the P bit, and bit[21] as the writeback (W) bit, and uses the same addressing mode as described in LDRSB (immediate). The instruction uses post-indexed addressing when P == '0' and uses pre-indexed addressing otherwise. The instruction is handled as described in Using R15.

T1

<!-- image -->

## Encoding

```
LDRSB{<c>}{<q>} <Rt>, <label> // (Preferred syntax) LDRSB{<c>}{<q>} <Rt>, [PC, #{+/-}<imm>] // (Alternative syntax)
```

## Decode for this encoding

```
ZeroExtend(imm12, 32);
```

```
if Rt == '1111' then SEE "PLI"; constant integer t = UInt(Rt); constant bits(32) imm32 = constant boolean add = (U == '1'); // Armv8-A removes UNPREDICTABLE for R13
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

&lt;q&gt;

## &lt;Rt&gt;

Is the general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;label&gt;

For the 'A1' variant: the label of the literal data item that is to be loaded into &lt;Rt&gt; . The assembler calculates the required value of the offset from the Align(PC, 4) value of the instruction to this label. Any value in the range -255 to 255 is permitted. If the offset is zero or positive, imm32 is equal to the offset and add == TRUE , encoded as U==1. If the offset is negative, imm32 is equal to minus the offset and add == FALSE , encoded as U == 0.

For the 'T1' variant: the label of the literal data item that is to be loaded into &lt;Rt&gt; . The assembler calculates the required value of the offset from the Align(PC, 4) value of the instruction to this label. Permitted values of the offset are -4095 to 4095.

If the offset is zero or positive, imm32 is equal to the offset and add == TRUE , encoded as U == 1.

If the offset is negative, imm32 is equal to minus the offset and add == FALSE , encoded as U == 0.

Specifies the offset is added to or subtracted from the base register, defaulting to + if omitted and encoded in 'U':

|   U | +/-   |
|-----|-------|
|   0 | -     |
|   1 | +     |

+/-

## &lt;imm&gt;

For the 'A1' variant: is the 8-bit unsigned immediate byte offset, in the range 0 to 255, defaulting to 0 if omitted, and encoded in the 'imm4H:imm4L' field.

For the 'T1' variant: is a 12-bit unsigned immediate byte offset, in the range 0 to 4095, encoded in the 'imm12' field.

The alternative syntax permits the addition or subtraction of the offset and the immediate offset to be specified separately, including permitting a subtraction of 0 that cannot be specified using the normal syntax. For more information, see Use of labels in UAL instruction syntax.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) base = Align(PC32,4); constant bits(32) address = if add then (base + imm32) else (base -imm32); R[t] = SignExtend(MemU[address,1], 32);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.