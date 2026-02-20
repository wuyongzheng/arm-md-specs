## F5.1.97 LDRSH (register)

Load Register Signed Halfword (register) calculates an address from a base register value and an offset register value, loads a halfword from memory, sign-extends it to form a 32-bit word, and writes it to a register. The offset register value can be shifted left by 0, 1, 2, or 3 bits. For information about memory accesses see Memory accesses.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding for the Offset variant

```
Applies when (P == 1 && W == 0) LDRSH{<c>}{<q>}
```

```
<Rt>, [<Rn>, {+/-}<Rm>]
```

## Encoding for the Post-indexed variant

```
Applies when (P == 0 && W == 0) LDRSH{<c>}{<q>} <Rt>, [<Rn>], {+/-}<Rm>
```

## Encoding for the Pre-indexed variant

```
Applies when (P == 1 && W == 1) LDRSH{<c>}{<q>}
```

```
<Rt>, [<Rn>, {+/-}<Rm>]!
```

## Decode for all variants of this encoding

```
if P == '0' && W == '1' then SEE "LDRSHT"; constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean index = (P == '1'); constant boolean add = (U == '1'); constant boolean wback = (P == '0') || (W == '1'); constant SRType shift_t = SRType_LSL; constant integer shift_n = 0; if t == 15 || m == 15 then UNPREDICTABLE; if wback && (n == 15 || n == t) then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If wback &amp;&amp; n == t , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction performs all of the loads using the specified addressing mode and the content of the register that is written back is UNKNOWN. In addition, if an exception occurs during such as instruction, the base address might be corrupted so that the instruction cannot be repeated.

T1

## Encoding

```
LDRSH{<c>}{<q>} <Rt>, [<Rn>, {+}<Rm>]
```

## Decode for this encoding

```
shift_t = SRType_LSL;
```

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean index = TRUE; constant boolean add = TRUE; constant boolean wback = FALSE; constant SRType constant integer shift_n = 0;
```

T2

<!-- image -->

## Encoding

```
LDRSH{<c>}{<q>} <Rt>, [<Rn>, {+}<Rm>{,
```

```
LDRSH{<c>}.W <Rt>, [<Rn>, {+}<Rm>] // (<Rt>, <Rn>, <Rm> can be represented in
```

## Decode for this encoding

```
if Rn == '1111' then SEE "LDRSH (literal)"; if Rt == '1111' then SEE "Related constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean index = TRUE; constant boolean add = TRUE; constant boolean wback = FALSE; constant SRType shift_t = SRType_LSL; constant integer shift_n = UInt(imm2); // Armv8-A removes UNPREDICTABLE for R13 if m == 15 then UNPREDICTABLE;
```

```
LSL #<imm>}] T1)
```

```
instructions";
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

Related instructions: Load/store, signed (register offset).

<!-- image -->

B

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the general-purpose register to be transferred, encoded in the 'Rt' field.

For the 'Offset', 'Post-indexed', and 'Pre-indexed' variants: is the general-purpose base register, encoded in the 'Rn' field. The PC can be used in the offset variant.

For the 'T1' and 'T2' variants: is the general-purpose base register, encoded in the 'Rn' field.

Specifies the index register is added to or subtracted from the base register, defaulting to + if omitted and encoded in 'U':

|   U | +/-   |
|-----|-------|
|   0 | -     |
|   1 | +     |

&lt;q&gt;

## &lt;Rt&gt;

## &lt;Rn&gt;

+/-

## &lt;Rm&gt;

Is the general-purpose index register, encoded in the 'Rm' field.

+

Specifies the index register is added to the base register.

## &lt;imm&gt;

If present, the size of the left shift to apply to the value from &lt;Rm&gt; , in the range 1-3. &lt;imm&gt; is encoded in imm2. If absent, no shift is specified and imm2 is encoded as 0b00 .

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) offset = Shift(R[m], shift_t, shift_n, PSTATE.C); constant bits(32) offset_addr = if add then (R[n] + offset) else (R[n] offset); constant bits(32) address = if index then offset_addr else R[n]; constant bits(16) data = MemU[address,2]; if wback then R[n] = offset_addr; R[t] = SignExtend(data, 32);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.