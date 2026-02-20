## F5.1.231 STR (register)

Store Register (register) calculates an address from a base register value and an offset register value, stores a word from a register to memory. The offset register value can optionally be shifted. For information about memory accesses see Memory accesses.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1 and T2).

## A1

<!-- image -->

## Encoding for the Offset variant

```
Applies when (P == 1 && W == 0) STR{<c>}{<q>} <Rt>, [<Rn>, {+/-}<Rm>{, <shift>}]
```

## Encoding for the Post-indexed variant

```
Applies when (P == 0 && W == 0) STR{<c>}{<q>} <Rt>, [<Rn>], {+/-}<Rm>{, <shift>}
```

## Encoding for the Pre-indexed variant

```
Applies when (P == 1 && W == 1) STR{<c>}{<q>}
```

```
<Rt>, [<Rn>, {+/-}<Rm>{, <shift>}]!
```

## Decode for all variants of this encoding

```
if P == '0' && W == '1' then SEE "STRT"; constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean index = (P == '1'); constant boolean add = (U == '1'); constant boolean wback = (P == '0') || (W == '1'); SRType shift_t; integer shift_n; (shift_t, shift_n) = DecodeImmShift(stype, imm5); if m == 15 then UNPREDICTABLE; if wback && (n == 15 || n == t) then UNPREDICTABLE;
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
STR{<c>}{<q>} <Rt>, [<Rn>, {+}<Rm>]
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
STR{<c>}{<q>} <Rt>, [<Rn>, {+}<Rm>{, LSL #<imm>}] STR{<c>}.W <Rt>, [<Rn>, {+}<Rm>] // (<Rt>, <Rn>, <Rm> can be represented in T1)
```

## Decode for this encoding

```
if Rn == '1111' then UNDEFINED; constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean index = TRUE; constant boolean add = TRUE; constant boolean wback = FALSE; constant SRType shift_t = SRType_LSL; constant integer shift_n = UInt(imm2); // Armv8-A removes UNPREDICTABLE for R13 if t == 15 || m == 15 then UNPREDICTABLE;
```

L

<!-- image -->

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

For the 'Offset', 'Post-indexed', and 'Pre-indexed' variants: is the general-purpose register to be transferred, encoded in the 'Rt' field. The PC can be used, but this is deprecated.

For the 'T1' and 'T2' variants: is the general-purpose register to be transferred, encoded in the 'Rt' field.

For the 'Offset', 'Post-indexed', and 'Pre-indexed' variants: is the general-purpose base register, encoded in the 'Rn' field. The PC can be used in the offset variant, but this is deprecated.

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

## &lt;shift&gt;

The shift to apply to the value read from &lt;Rm&gt; . If absent, no shift is applied. Otherwise, see Shifts applied to a register.

+

Specifies the index register is added to the base register.

## &lt;imm&gt;

If present, the size of the left shift to apply to the value from &lt;Rm&gt; , in the range 1-3. &lt;imm&gt; is encoded in imm2. If absent, no shift is specified and imm2 is encoded as 0b00 .

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) offset = Shift(R[m], shift_t, shift_n, PSTATE.C); constant bits(32) offset_addr = if add then (R[n] + offset) else (R[n] offset); constant bits(32) address = if index then offset_addr else R[n]; bits(32) data; if t == 15 then // Only possible for encoding A1 data = PCStoreValue(); else data = R[t]; MemU[address,4] = data; if wback then R[n] = offset_addr;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.