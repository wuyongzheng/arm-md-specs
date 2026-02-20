## F5.1.236 STRD (register)

Store Register Dual (register) calculates an address from a base register value and a register offset, and stores two words from two registers to memory. It can use offset, post-indexed, or pre-indexed addressing. For information about memory accesses see Memory accesses.

<!-- image -->

## Encoding for the Offset variant

Applies when

```
(P == 1 && W == 0) STRD{<c>}{<q>} <Rt>, <Rt2>, [<Rn>, {+/-}<Rm>]
```

## Encoding for the Post-indexed variant

```
Applies when (P == 0 && W == 0) STRD{<c>}{<q>} <Rt>, <Rt2>, [<Rn>], {+/-}<Rm>
```

## Encoding for the Pre-indexed variant

```
Applies when (P == 1 && W == 1) STRD{<c>}{<q>} <Rt>, <Rt2>, [<Rn>, {+/-}<Rm>]!
```

## Decode for all variants of this encoding

```
if Rt<0> == '1' then UNPREDICTABLE; constant integer t = UInt(Rt); constant integer t2 = t + 1; constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean index = (P == '1'); constant boolean add = (U == '1'); constant boolean wback = (P == '0') || (W == '1'); if P == '0' && W == '1' then UNPREDICTABLE; if t2 == 15 || m == 15 then UNPREDICTABLE; if wback && (n == 15 || n == t || n == t2) then
```

```
UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If t == 15 || t2 == 15 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The store instruction performs the store using the specified addressing mode but the value corresponding to R15 is UNKNOWN.

If wback &amp;&amp; (n == t || n == t2) , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The store instruction executes but the value stored is UNKNOWN.

If wback &amp;&amp; n == 15 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes without writeback of the base address.
- The instruction uses the addressing mode described in the equivalent immediate offset instruction.

If Rt&lt;0&gt; == '1' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes with the additional decode: t&lt;0&gt; = '0'.
- The instruction executes with the additional decode: t2 = t.
- The instruction executes as described, with no change to its behavior and no additional side-effects. This does not apply when Rt == '1111'.

If P == '0' &amp;&amp; W == '1' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes with the additional decode: P = '1'; W = '0'.
- The instruction executes with the additional decode: P = '1'; W = '1'.
- The instruction executes with the additional decode: P = '0'; W = '0'.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

<!-- image -->

## &lt;Rt&gt;

Is the first general-purpose register to be transferred, encoded in the 'Rt' field. This register must be even-numbered and not R14.

&lt;Rt2&gt;

Is the second general-purpose register to be transferred. This register must be &lt;R(t+1)&gt; .

## &lt;Rn&gt;

+/-

Is the general-purpose base register, encoded in the 'Rn' field. The PC can be used in the offset variant, but this is deprecated.

Specifies the index register is added to or subtracted from the base register, defaulting to + if omitted and encoded in 'U':

## &lt;Rm&gt;

Is the general-purpose index register, encoded in the 'Rm' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) offset_addr = if add then (R[n] + R[m]) else (R[n] R[m]); constant bits(32) address = if index then offset_addr else R[n]; if IsAligned(address, 8) then bits(64) data; if BigEndian(AccessType_GPR) then data<63:32> = R[t]; data<31:0> = R[t2]; else data<31:0> = R[t]; data<63:32> = R[t2]; MemA[address,8] = data; else MemA[address,4] = R[t]; MemA[address+4,4] = R[t2]; if wback then R[n] = offset_addr;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

|   U | +/-   |
|-----|-------|
|   0 | -     |
|   1 | +     |