## F5.1.81 LDRD (literal)

Load Register Dual (literal) calculates an address from the PC value and an immediate offset, loads two words from memory, and writes them to two registers. For information about memory accesses see Memory accesses.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
LDRD{<c>}{<q>} <Rt>, <Rt2>, <label> // (Normal form) LDRD{<c>}{<q>} <Rt>, <Rt2>, [PC, #{+/-}<imm>] // (Alternative form)
```

## Decode for this encoding

```
if Rt<0> == '1' then UNPREDICTABLE; constant integer t = UInt(Rt); constant integer t2 = t + 1; constant bits(32) imm32 = ZeroExtend(imm4H:imm4L, 32); constant boolean add = (U == '1'); if t2 == 15 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If Rt&lt;0&gt; == '1' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes with the additional decode: t&lt;0&gt; = '0';.
- The instruction executes with the additional decode: t2 = t;.
- The instruction executes as described, with no change to its behavior and no additional side-effects. This does not apply when Rt == '1111'.

If P == '0' || W == '1' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes as if P == 1 and W == 0.'

T1

<!-- image -->

## Encoding

```
Applies when (!(P == '0' && W == '0')) LDRD{<c>}{<q>} <Rt>, <Rt2>, <label> // (Normal form) LDRD{<c>}{<q>} <Rt>, <Rt2>, [PC, #{+/-}<imm>] // (Alternative form)
```

## Decode for this encoding

```
if P == '0' && W == '0' then SEE "Related encodings"; constant integer t = UInt(Rt); constant integer t2 = UInt(Rt2); constant bits(32) imm32 = ZeroExtend(imm8:'00', 32); constant boolean add = (U == '1'); // Armv8-A removes UNPREDICTABLE for R13 if t == 15 || t2 == 15 || t == t2 then UNPREDICTABLE; if W == '1' then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If t == t2 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The load instruction executes but the destination register takes an UNKNOWN value.

If W == '1' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes without writeback of the base address.
- The instruction uses post-indexed addressing when P == '0' and uses pre-indexed addressing otherwise. The instruction is handled as described in Using R15.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

Related encodings: Load/Store dual, Load/Store-Exclusive, Load-Acquire/Store-Release, table branch.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

For the 'A1' variant: is the first general-purpose register to be transferred, encoded in the 'Rt' field. This register must be even-numbered and not R14.

For the 'T1' variant: is the first general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Rt2&gt;

For the 'A1' variant: is the second general-purpose register to be transferred. This register must be &lt;R(t+1)&gt; .

For the 'T1' variant: is the second general-purpose register to be transferred, encoded in the 'Rt2' field.

&lt;q&gt;

## &lt;Rt&gt;

## &lt;label&gt;

For the 'A1' variant: the label of the literal data item that is to be loaded into &lt;Rt&gt; . The assembler calculates the required value of the offset from the Align(PC, 4) value of the instruction to this label. Any value in the range -255 to 255 is permitted. If the offset is zero or positive, imm32 is equal to the offset and add == TRUE , encoded as U==1. If the offset is negative, imm32 is equal to minus the offset and add == FALSE , encoded as U == 0.

For the 'T1' variant: the label of the literal data item that is to be loaded into &lt;Rt&gt; . The assembler calculates the required value of the offset from the Align(PC, 4) value of the instruction to this label. Permitted values of the offset are multiples of 4 in the range -1020 to 1020.

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

For the 'T1' variant: is the optional 8-bit unsigned immediate byte offset, in the range 0 to 255, defaulting to 0 and encoded in the 'imm8' field.

The alternative syntax permits the addition or subtraction of the offset and the immediate offset to be specified separately, including permitting a subtraction of 0 that cannot be specified using the normal syntax. For more information, see Use of labels in UAL instruction syntax.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) address = (if add then (Align(PC32,4) + imm32) else (Align(PC32,4) imm32)); if IsAligned(address, 8) then constant bits(64) data = MemA[address,8]; if BigEndian(AccessType_GPR) then R[t] = data<63:32>; R[t2] = data<31:0>; else R[t] = data<31:0>; R[t2] = data<63:32>; else constant bits(32) data1 = MemA[address,4]; constant bits(32) data2 = MemA[address+4,4]; R[t] = data1; R[t2] = data2;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.