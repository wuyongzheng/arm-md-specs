## F5.1.82 LDRD (register)

Load Register Dual (register) calculates an address from a base register value and a register offset, loads two words from memory, and writes them to two registers. It can use offset, post-indexed, or pre-indexed addressing. For information about memory accesses see Memory accesses.

<!-- image -->

## Encoding for the Offset variant

```
Applies when (P == 1 && W == 0) LDRD{<c>}{<q>} <Rt>, <Rt2>, [<Rn>, {+/-}<Rm>]
```

## Encoding for the Post-indexed variant

```
Applies when (P == 0 && W == 0) LDRD{<c>}{<q>} <Rt>, <Rt2>, [<Rn>], {+/-}<Rm>
```

## Encoding for the Pre-indexed variant

```
Applies when (P == 1 && W == 1) LDRD{<c>}{<q>} <Rt>, <Rt2>, [<Rn>, {+/-}<Rm>]!
```

## Decode for all variants of this encoding

```
if Rt<0> == '1' then UNPREDICTABLE; constant integer t = UInt(Rt); constant integer t2 = t + 1; constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean index = (P == '1'); constant boolean add = (U == '1'); constant boolean wback = (P == '0') || (W == '1'); if P == '0' && W == '1' then UNPREDICTABLE; if t2 == 15 || m == 15 || m == t || m == t2 then UNPREDICTABLE; if wback && (n == 15 || n == t || n == t2) then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If wback &amp;&amp; (n == t || n == t2) , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction performs all of the loads using the specified addressing mode and the content of the register that is written back is UNKNOWN. In addition, if an exception occurs during such as instruction, the base address might be corrupted so that the instruction cannot be repeated.

If P == '0' &amp;&amp; W == '1' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes as an LDRD using one of offset, post-indexed, or pre-indexed addressing.

If m == t || m == t2 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction loads register Rm with an UNKNOWN value.

If Rt&lt;0&gt; == '1' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes with the additional decode: t&lt;0&gt; = '0'.
- The instruction executes with the additional decode: t2 = t.
- The instruction executes as described, with no change to its behavior and no additional side-effects. This does not apply when Rt == '1111'.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

&lt;q&gt;

&lt;Rt&gt;

Is the first general-purpose register to be transferred, encoded in the 'Rt' field. This register must be even-numbered and not R14.

&lt;Rt2&gt;

Is the second general-purpose register to be transferred. This register must be &lt;R(t+1)&gt; .

&lt;Rn&gt;

+/-

Is the general-purpose base register, encoded in the 'Rn' field. The PC can be used in the offset variant.

Specifies the index register is added to or subtracted from the base register, defaulting to + if omitted and encoded in 'U':

|   U | +/-   |
|-----|-------|
|   0 | -     |
|   1 | +     |

&lt;Rm&gt;

Is the general-purpose index register, encoded in the 'Rm' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) offset_addr = if add then (R[n] + R[m]) else (R[n] R[m]); constant bits(32) address = if index then offset_addr else R[n]; if IsAligned(address, 8) then constant bits(64) data = MemA[address,8]; if BigEndian(AccessType_GPR) then R[t] = data<63:32>; R[t2] = data<31:0>; else R[t] = data<31:0>; R[t2] = data<63:32>; else constant bits(32) data1 = MemA[address,4]; constant bits(32) data2 = MemA[address+4,4]; R[t] = data1; R[t2] = data2; if wback then R[n] = offset_addr;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.