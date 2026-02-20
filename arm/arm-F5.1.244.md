## F5.1.244 STRT

Store Register Unprivileged stores a word from a register to memory. For information about memory accesses see Memory accesses.

The memory access is restricted as if the PE were running in User mode. This makes no difference if the PE is actually running in User mode.

STRT is UNPREDICTABLE in Hyp mode.

The T32 instruction uses an offset addressing mode, that calculates the address used for the memory access from a base register value and an immediate offset, and leaves the base register unchanged.

The A32 instruction uses a post-indexed addressing mode, that uses a base register value as the address for the memory access, and calculates a new address from a base register value and an offset and writes it back to the base register. The offset can be an immediate value or an optionally-shifted register value.

It has encodings from the following instruction sets: A32 (A1 and A2) and T32 (T1).

A1

<!-- image -->

## Encoding

```
STRT{<c>}{<q>} <Rt>, [<Rn>] {, #{+/-}<imm>}
```

## Decode for this encoding

```
ZeroExtend(imm12, 32);
```

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant boolean postindex = TRUE; constant boolean add = (U == '1'); constant boolean register_form = FALSE; constant bits(32) imm32 = constant integer m = integer UNKNOWN; constant integer shift_n = integer UNKNOWN; constant SRType shift_t = SRType UNKNOWN; if n == 15 || n == t then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If n == t , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The store instruction executes but the value stored is UNKNOWN.

If n == 15 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction uses post-indexed addressing with the base register as PC. This is handled as described in Using R15.
- The instruction is treated as if bit[24] == 1 and bit[21] == 0. The instruction uses immediate offset addressing with the base register as PC, without writeback.

A2

<!-- image -->

## Encoding

```
STRT{<c>}{<q>} <Rt>, [<Rn>], {+/-}<Rm>{, <shift>}
```

## Decode for this encoding

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean postindex = TRUE; constant boolean add = (U == '1'); constant boolean register_form = TRUE; SRType shift_t; integer shift_n; (shift_t, shift_n) = DecodeImmShift(stype, imm5); constant bits(32) imm32 = bits(32) UNKNOWN; if n == 15 || n == t || m == 15 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If n == t , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The store instruction executes but the value stored is UNKNOWN.

If n == 15 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction uses post-indexed addressing with the base register as PC. This is handled as described in Using R15.
- The instruction is treated as if bit[24] == 1 and bit[21] == 0. The instruction uses immediate offset addressing with the base register as PC, without writeback.

L

T1

<!-- image -->

## Encoding

```
STRT{<c>}{<q>} <Rt>, [<Rn> {, #{+}<imm>}]
```

## Decode for this encoding

```
if Rn == '1111' then UNDEFINED; constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant boolean postindex = FALSE; constant boolean add = TRUE; constant boolean register_form = FALSE; constant bits(32) imm32 = ZeroExtend(imm8, 32); constant integer m = integer UNKNOWN; constant integer shift_n = integer UNKNOWN; constant SRType shift_t = SRType UNKNOWN; // Armv8-A removes UNPREDICTABLE for R13 if t == 15 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If t == 15 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The store instruction performs the store using the specified addressing mode but the value corresponding to R15 is UNKNOWN.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

For the 'A1' and 'A2' variants: is the general-purpose register to be transferred, encoded in the 'Rt' field. The PC can be used, but this is deprecated.

For the 'T1' variant: is the general-purpose register to be transferred, encoded in the 'Rt' field.

Is the general-purpose base register, encoded in the 'Rn' field.

For the 'A1' variant: specifies the offset is added to or subtracted from the base register, defaulting to + if omitted and encoded in 'U':

|   U | +/-   |
|-----|-------|
|   0 | -     |
|   1 | +     |

For the 'A2' variant: specifies the index register is added to or subtracted from the base register, defaulting to + if omitted and encoded in 'U':

&lt;q&gt;

&lt;Rt&gt;

## &lt;Rn&gt;

+/-

## &lt;imm&gt;

For the 'A1' variant: is the 12-bit unsigned immediate byte offset, in the range 0 to 4095, defaulting to 0 if omitted, and encoded in the 'imm12' field.

For the 'T1' variant: is an optional 8-bit unsigned immediate byte offset, in the range 0 to 255, defaulting to 0 and encoded in the 'imm8' field.

## &lt;Rm&gt;

Is the general-purpose index register, encoded in the 'Rm' field.

## &lt;shift&gt;

The shift to apply to the value read from &lt;Rm&gt; . If absent, no shift is applied. Otherwise, see Shifts applied to a register.

+

Specifies the offset is added to the base register.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); if PSTATE.EL == EL2 then UNPREDICTABLE; // Hyp mode constant bits(32) offset = (if register_form then Shift(R[m], shift_t, shift_n, PSTATE.C) else imm32); constant bits(32) offset_addr = if add then (R[n] + offset) else (R[n] offset); constant bits(32) address = if postindex then R[n] else offset_addr; bits(32) data; if t == 15 then // Only possible for encodings A1 and A2 data = PCStoreValue(); else data = R[t]; MemU_unpriv[address,4] = data; if postindex then R[n] = offset_addr;
```

## CONSTRAINED UNPREDICTABLE behavior

If PSTATE.EL == EL2 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes as STR (immediate).

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

|   U | +/-   |
|-----|-------|
|   0 | -     |
|   1 | +     |