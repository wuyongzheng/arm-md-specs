## F5.1.98 LDRSHT

Load Register Signed Halfword Unprivileged loads a halfword from memory, sign-extends it to form a 32-bit word, and writes it to a register. For information about memory accesses see Memory accesses.

The memory access is restricted as if the PE were running in User mode. This makes no difference if the PE is actually running in User mode.

LDRSHT is UNPREDICTABLE in Hyp mode.

The T32 instruction uses an offset addressing mode, that calculates the address used for the memory access from a base register value and an immediate offset, and leaves the base register unchanged.

The A32 instruction uses a post-indexed addressing mode, that uses a base register value as the address for the memory access, and calculates a new address from a base register value and an offset and writes it back to the base register. The offset can be an immediate value or a register value.

It has encodings from the following instruction sets: A32 (A1 and A2) and T32 (T1).

A1

<!-- image -->

## Encoding

```
LDRSHT{<c>}{<q>} <Rt>, [<Rn>] {, #{+/-}<imm>}
```

## Decode for this encoding

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant boolean postindex = TRUE; constant boolean add = (U == '1'); constant boolean register_form = FALSE; constant bits(32) imm32 = ZeroExtend(imm4H:imm4L, 32); constant integer m = integer UNKNOWN; if t == 15 || n == 15 || n == t then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If n == 15 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction uses post-indexed addressing with the base register as PC. This is handled as described in Using R15.
- The instruction is treated as if bit[24] == '1' and bit[21] == '0'. The instruction uses immediate offset addressing with the base register as PC, without writeback.

If n == t &amp;&amp; n != 15 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction performs all of the loads using the specified addressing mode and the content of the register that is written back is UNKNOWN. In addition, if an exception occurs during such as instruction, the base address might be corrupted so that the instruction cannot be repeated.

A2

<!-- image -->

## Encoding

```
LDRSHT{<c>}{<q>} <Rt>, [<Rn>], {+/-}<Rm>
```

## Decode for this encoding

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean postindex = TRUE; constant boolean add = (U == '1'); constant boolean register_form = TRUE; constant bits(32) imm32 = bits(32) UNKNOWN; if t == 15 || n == 15 || n == t || m == 15 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If n == t &amp;&amp; n != 15 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction performs all of the loads using the specified addressing mode and the content of the register that is written back is UNKNOWN. In addition, if an exception occurs during such as instruction, the base address might be corrupted so that the instruction cannot be repeated.

T1

<!-- image -->

## Encoding

```
LDRSHT{<c>}{<q>} <Rt>, [<Rn> {, #{+}<imm>}]
```

## Decode for this encoding

```
if Rn == '1111' then SEE "LDRSH (literal)"; constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant boolean postindex = FALSE; constant boolean add = TRUE; constant boolean register_form = FALSE; constant bits(32) imm32 = ZeroExtend(imm8, 32); constant integer m = integer UNKNOWN; // Armv8-A removes UNPREDICTABLE for R13 if t == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the general-purpose register to be transferred, encoded in the 'Rt' field.

Is the general-purpose base register, encoded in the 'Rn' field.

For the 'A1' variant: specifies the offset is added to or subtracted from the base register, defaulting to + if omitted and encoded in 'U':

|   U | +/-   |
|-----|-------|
|   0 | -     |
|   1 | +     |

For the 'A2' variant: specifies the index register is added to or subtracted from the base register, defaulting to + if omitted and encoded in 'U':

|   U | +/-   |
|-----|-------|
|   0 | -     |
|   1 | +     |

&lt;q&gt;

&lt;Rt&gt;

## &lt;Rn&gt;

+/-

## &lt;imm&gt;

For the 'A1' variant: is the 8-bit unsigned immediate byte offset, in the range 0 to 255, defaulting to 0 if omitted, and encoded in the 'imm4H:imm4L' field.

For the 'T1' variant: is an optional 8-bit unsigned immediate byte offset, in the range 0 to 255, defaulting to 0 and encoded in the 'imm8' field.

## &lt;Rm&gt;

Is the general-purpose index register, encoded in the 'Rm' field.

+ Specifies the offset is added to the base register.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); if PSTATE.EL == EL2 then UNPREDICTABLE; // Hyp mode constant bits(32) offset = if register_form then R[m] else imm32;
```

```
constant bits(32) offset_addr = if add then (R[n] + offset) else (R[n] offset); constant bits(32) address = if postindex then R[n] else offset_addr; constant bits(16) data = MemU_unpriv[address,2]; if postindex then R[n] = offset_addr; R[t] = SignExtend(data, 32);
```

## CONSTRAINED UNPREDICTABLE behavior

If PSTATE.EL == EL2 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes as LDRSH (immediate).

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.