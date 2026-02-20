## F5.1.235 STRD (immediate)

Store Register Dual (immediate) calculates an address from a base register value and an immediate offset, and stores two words from two registers to memory. It can use offset, post-indexed, or pre-indexed addressing. For information about memory accesses see Memory accesses.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the Offset variant

```
Applies when (P == 1 && W == 0) STRD{<c>}{<q>} <Rt>, <Rt2>, [<Rn>
```

```
{, #{+/-}<imm>}]
```

## Encoding for the Post-indexed variant

```
Applies when (P == 0 && W == 0) STRD{<c>}{<q>}
```

```
<Rt>, <Rt2>, [<Rn>], #{+/-}<imm>
```

## Encoding for the Pre-indexed variant

```
Applies when (P == 1 && W == 1) STRD{<c>}{<q>}
```

```
<Rt>, <Rt2>, [<Rn>, #{+/-}<imm>]!
```

## Decode for all variants of this encoding

```
UNPREDICTABLE;
```

```
if Rt<0> == '1' then UNPREDICTABLE; constant integer t = UInt(Rt); constant integer t2 = t + 1; constant integer n = UInt(Rn); constant bits(32) imm32 = ZeroExtend(imm4H:imm4L, 32); constant boolean index = (P == '1'); constant boolean add = (U == '1'); constant boolean wback = (P == '0') || (W == '1'); if P == '0' && W == '1' then UNPREDICTABLE; if wback && (n == 15 || n == t || n == t2) then if t2 == 15 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If t == 15 || t2 == 15 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The store instruction performs the store using the specified addressing mode but the value corresponding to R15 is UNKNOWN.

If wback &amp;&amp; (n == t || n == t2) , then one of the following behaviors must occur:

- The instruction is UNDEFINED.

T1

<!-- image -->

## Encoding for the Offset variant

<!-- image -->

## Encoding for the Post-indexed variant

```
Applies when (P == 0 && W == 1) STRD{<c>}{<q>}
```

```
<Rt>, <Rt2>, [<Rn>], #{+/-}<imm>
```

## Encoding for the Pre-indexed variant

Applies when

```
(P == 1 && W == 1) STRD{<c>}{<q>} <Rt>, <Rt2>, [<Rn>, #{+/-}<imm>]!
```

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
- The instruction executes as an LDRD using one of offset, post-indexed, or pre-indexed addressing.

## Decode for all variants of this encoding

```
if P == '0' && W == '0' then SEE "Related encodings"; constant integer t = UInt(Rt); constant integer t2 = UInt(Rt2); constant integer n = UInt(Rn); constant bits(32) imm32 = ZeroExtend(imm8:'00', 32); constant boolean index = (P == '1'); constant boolean add = (U == '1'); constant boolean wback = (W == '1'); if wback && (n == t || n == t2) then UNPREDICTABLE; // Armv8-A removes UNPREDICTABLE for R13 if n == 15 || t == 15 || t2 == 15 then UNPREDICTABLE;
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

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

Related encodings: Load/store dual, load/store exclusive, table branch.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

For the 'A1 Offset', 'A1 Post-indexed', and 'A1 Pre-indexed' variants: is the first general-purpose register to be transferred, encoded in the 'Rt' field. This register must be even-numbered and not R14.

For the 'T1 Offset', 'T1 Post-indexed', and 'T1 Pre-indexed' variants: is the first general-purpose register to be transferred, encoded in the 'Rt' field.

&lt;q&gt;

&lt;Rt&gt;

## &lt;Rt2&gt;

For the 'A1 Offset', 'A1 Post-indexed', and 'A1 Pre-indexed' variants: is the second general-purpose register to be transferred. This register must be &lt;R(t+1)&gt; .

For the 'T1 Offset', 'T1 Post-indexed', and 'T1 Pre-indexed' variants: is the second general-purpose register to be transferred, encoded in the 'Rt2' field.

For the 'A1 Offset', 'A1 Post-indexed', and 'A1 Pre-indexed' variants: is the general-purpose base register, encoded in the 'Rn' field. The PC can be used in the offset variant, but this is deprecated.

For the 'T1 Offset', 'T1 Post-indexed', and 'T1 Pre-indexed' variants: is the general-purpose base register, encoded in the 'Rn' field.

Specifies the offset is added to or subtracted from the base register, defaulting to + if omitted and encoded in 'U':

|   U | +/-   |
|-----|-------|
|   0 | -     |
|   1 | +     |

## &lt;Rn&gt;

+/-

## &lt;imm&gt;

For the 'A1 Offset', 'A1 Post-indexed', and 'A1 Pre-indexed' variants: is the 8-bit unsigned immediate byte offset, in the range 0 to 255, defaulting to 0 if omitted, and encoded in the 'imm4H:imm4L' field.

For the 'T1 Offset', 'T1 Post-indexed', and 'T1 Pre-indexed' variants: is the unsigned immediate byte offset, a multiple of 4, in the range 0 to 1020, defaulting to 0 if omitted, and encoded in the 'imm8' field as &lt;imm&gt;/4.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) offset_addr = if add then (R[n] + imm32) else (R[n] constant bits(32) address = if index then offset_addr else R[n]; if IsAligned(address, 8) then bits(64) data; if BigEndian(AccessType_GPR) then data<63:32> = R[t]; data<31:0> = R[t2]; else data<31:0> = R[t]; data<63:32> = R[t2]; MemA[address,8] = data; else MemA[address,4] = R[t]; MemA[address+4,4] = R[t2]; if wback then R[n] = offset_addr;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

```
imm32);
```