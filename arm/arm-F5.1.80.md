## F5.1.80 LDRD (immediate)

Load Register Dual (immediate) calculates an address from a base register value and an immediate offset, loads two words from memory, and writes them to two registers. It can use offset, post-indexed, or pre-indexed addressing. For information about memory accesses see Memory accesses.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the Offset variant

```
Applies when (P == 1 && W == 0) LDRD{<c>}{<q>} <Rt>, <Rt2>, [<Rn> {, #{+/-}<imm>}]
```

## Encoding for the Post-indexed variant

```
Applies when (P == 0 && W == 0) LDRD{<c>}{<q>} <Rt>, <Rt2>, [<Rn>], #{+/-}<imm>
```

## Encoding for the Pre-indexed variant

```
Applies when (P == 1 && W == 1) LDRD{<c>}{<q>}
```

```
<Rt>, <Rt2>, [<Rn>, #{+/-}<imm>]!
```

## Decode for all variants of this encoding

```
if Rn == '1111' then SEE "LDRD (literal)"; if Rt<0> == '1' then UNPREDICTABLE; constant integer t = UInt(Rt); constant integer t2 = t + 1; constant integer n = UInt(Rn); constant bits(32) imm32 = ZeroExtend(imm4H:imm4L, 32); constant boolean index = (P == '1'); constant boolean add = (U == '1'); constant boolean wback = (P == '0') || (W == '1'); if P == '0' && W == '1' then UNPREDICTABLE; if wback && (n == t || n == t2) then UNPREDICTABLE; if t2 == 15 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If wback &amp;&amp; (n == t || n == t2) , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction performs all of the loads using the specified addressing mode and the content of the register that is written back is UNKNOWN. In addition, if an exception occurs during such an instruction, the base address might be corrupted so that the instruction cannot be repeated.

If P == '0' &amp;&amp; W == '1' , then one of the following behaviors must occur:

T1

<!-- image -->

## Encoding for the Offset variant

```
Applies when (P == 1 && W == 0) LDRD{<c>}{<q>} <Rt>, <Rt2>, [<Rn> {, #{+/-}<imm>}]
```

## Encoding for the Post-indexed variant

```
Applies when (P == 0 && W == 1) LDRD{<c>}{<q>}
```

```
<Rt>, <Rt2>, [<Rn>], #{+/-}<imm>
```

## Encoding for the Pre-indexed variant

Applies when

```
<Rt>, <Rt2>, [<Rn>, #{+/-}<imm>]!
```

```
(P == 1 && W == 1) LDRD{<c>}{<q>}
```

## Decode for all variants of this encoding

```
if P == '0' && W == '0' then SEE "Related encodings"; if Rn == '1111' then SEE "LDRD (literal)"; constant integer t = UInt(Rt); constant integer t2 = UInt(Rt2); constant integer n = UInt(Rn); constant bits(32) imm32 = ZeroExtend(imm8:'00', 32); constant boolean index = (P == '1'); constant boolean add = (U == '1'); constant boolean wback = (W == '1'); if wback && (n == t || n == t2) then UNPREDICTABLE; // Armv8-A removes UNPREDICTABLE for R13 if t == 15 || t2 == 15 || t == t2 then UNPREDICTABLE;
```

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes as an LDRD using one of offset, post-indexed, or pre-indexed addressing.

If Rt&lt;0&gt; == '1' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes with the additional decode: t&lt;0&gt; = '0'.
- The instruction executes with the additional decode: t2 = t.
- The instruction executes as described, with no change to its behavior and no additional side-effects. This does not apply when Rt == '1111'.

## CONSTRAINED UNPREDICTABLE behavior

If wback &amp;&amp; (n == t || n == t2) , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction performs all of the loads using the specified addressing mode and the content of the register that is written back is UNKNOWN. In addition, if an exception occurs during such an instruction, the base address might be corrupted so that the instruction cannot be repeated.

If t == t2 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The load instruction executes but the destination register takes an UNKNOWN value.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

Related encodings: Load/store dual, load/store exclusive, table branch.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

For the 'A1 Offset', 'A1 Post-indexed', and 'A1 Pre-indexed' variants: is the first general-purpose register to be transferred, encoded in the 'Rt' field. This register must be even-numbered and not R14.

For the 'T1 Offset', 'T1 Post-indexed', and 'T1 Pre-indexed' variants: is the first general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Rt2&gt;

For the 'A1 Offset', 'A1 Post-indexed', and 'A1 Pre-indexed' variants: is the second general-purpose register to be transferred. This register must be &lt;R(t+1)&gt; .

For the 'T1 Offset', 'T1 Post-indexed', and 'T1 Pre-indexed' variants: is the second general-purpose register to be transferred, encoded in the 'Rt2' field.

Is the general-purpose base register, encoded in the 'Rn' field. For PC use see LDRD (literal).

Specifies the offset is added to or subtracted from the base register, defaulting to + if omitted and encoded in 'U':

|   U | +/-   |
|-----|-------|
|   0 | -     |
|   1 | +     |

<!-- image -->

## &lt;Rt&gt;

## &lt;Rn&gt;

+/-

## &lt;imm&gt;

For the 'A1 Offset', 'A1 Post-indexed', and 'A1 Pre-indexed' variants: is the 8-bit unsigned immediate byte offset, in the range 0 to 255, defaulting to 0 if omitted, and encoded in the 'imm4H:imm4L' field.

For the 'T1 Offset', 'T1 Post-indexed', and 'T1 Pre-indexed' variants: is the unsigned immediate byte offset, a multiple of 4, in the range 0 to 1020, defaulting to 0 if omitted, and encoded in the 'imm8' field as &lt;imm&gt;/4.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) offset_addr = if add then (R[n] + imm32) else (R[n] imm32); constant bits(32) address = if index then offset_addr else R[n]; if IsAligned(address, 8) then constant bits(64) data = MemA[address,8]; if BigEndian(AccessType_GPR) then R[t] = data<63:32>; R[t2] = data<31:0>; else R[t] = data<31:0>; R[t2] = data<63:32>; else constant bits(32) data1 = MemA[address,4]; constant bits(32) data2 = MemA[address+4,4]; R[t] = data1; R[t2] = data2; if wback then R[n] = offset_addr;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.