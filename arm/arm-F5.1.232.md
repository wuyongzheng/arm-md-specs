## F5.1.232 STRB (immediate)

Store Register Byte (immediate) calculates an address from a base register value and an immediate offset, and stores a byte from a register to memory. It can use offset, post-indexed, or pre-indexed addressing. For information about memory accesses see Memory accesses.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1, T2, and T3).

A1

<!-- image -->

## Encoding for the Offset variant

```
Applies when (P == 1 && W == 0) STRB{<c>}{<q>} <Rt>, [<Rn> {, #{+/-}<imm>}]
```

## Encoding for the Post-indexed variant

```
Applies when (P == 0 && W == 0) STRB{<c>}{<q>}
```

```
<Rt>, [<Rn>], #{+/-}<imm>
```

## Encoding for the Pre-indexed variant

```
Applies when (P == 1 && W == 1) STRB{<c>}{<q>} <Rt>, [<Rn>, #{+/-}<imm>]!
```

## Decode for all variants of this encoding

```
if P == '0' && W == '1' then SEE "STRBT"; constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant bits(32) imm32 = ZeroExtend(imm12, 32); constant boolean index = (P == '1'); constant boolean add = (U == '1'); constant boolean wback = (P == '0') || (W == '1'); if t == 15 then UNPREDICTABLE; if wback && (n == 15 || n == t) then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If t == 15 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The store instruction performs the store using the specified addressing mode but the value corresponding to R15 is UNKNOWN.

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
STRB{<c>}{<q>} <Rt>, [<Rn> {, #{+}<imm>}]
```

## Decode for this encoding

```
ZeroExtend(imm5, 32);
```

L

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant bits(32) imm32 = constant boolean index = TRUE; constant boolean add = TRUE; constant boolean wback = FALSE;
```

T2

<!-- image -->

## Encoding

```
STRB{<c>}{<q>} <Rt>, [<Rn> {, #{+}<imm>}] STRB{<c>}.W <Rt>, [<Rn> {, #{+}<imm>}] // (<Rt>, <Rn>, <imm> can be represented in T1)
```

## Decode for this encoding

```
if Rn == '1111' then UNDEFINED; constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant bits(32) imm32 = constant boolean index = TRUE; constant boolean add = TRUE; constant boolean wback = FALSE; // Armv8-A removes UNPREDICTABLE for R13 if t == 15 then UNPREDICTABLE;
```

<!-- image -->

```
ZeroExtend(imm12, 32);
```

## CONSTRAINED UNPREDICTABLE behavior

If t == 15 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The store instruction performs the store using the specified addressing mode but the value corresponding to R15 is UNKNOWN.

T3

<!-- image -->

## Encoding for the Offset variant

Applies when (P == 1 &amp;&amp; U == 0 &amp;&amp; W ==

```
STRB{<c>}{<q>} <Rt>, [<Rn>
```

```
0) {, #-<imm>}]
```

## Encoding for the Post-indexed variant

```
Applies when (P == 0 && W == 1) STRB{<c>}{<q>} <Rt>, [<Rn>], #{+/-}<imm>
```

## Encoding for the Pre-indexed variant

```
Applies when (P == 1 && W == 1) STRB{<c>}{<q>}
```

```
<Rt>, [<Rn>, #{+/-}<imm>]!
```

## Decode for all variants of this encoding

```
UNDEFINED;
```

```
if P == '1' && U == '1' && W == '0' then SEE "STRBT"; if Rn == '1111' || (P == '0' && W == '0') then constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant bits(32) imm32 = ZeroExtend(imm8, 32); constant boolean index = (P == '1'); constant boolean add = (U == '1'); constant boolean wback = (W == '1'); // Armv8-A removes UNPREDICTABLE for R13 if t == 15 || (wback && n == t) then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If t == 15 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The store instruction performs the store using the specified addressing mode but the value corresponding to R15 is UNKNOWN.

If wback &amp;&amp; n == t , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The store instruction executes but the value stored is UNKNOWN.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the general-purpose register to be transferred, encoded in the 'Rt' field.

For the 'A1 Offset', 'A1 Post-indexed', and 'A1 Pre-indexed' variants: is the general-purpose base register, encoded in the 'Rn' field. The PC can be used in the offset variant, but this is deprecated.

For the 'T1', 'T2', 'T3 Offset', 'T3 Post-indexed', and 'T3 Pre-indexed' variants: is the general-purpose base register, encoded in the 'Rn' field.

Specifies the offset is added to or subtracted from the base register, defaulting to + if omitted and encoded in 'U':

|   U | +/-   |
|-----|-------|
|   0 | -     |
|   1 | +     |

&lt;q&gt;

## &lt;Rt&gt;

## &lt;Rn&gt;

+/-

## &lt;imm&gt;

For the 'A1 Offset', 'A1 Post-indexed', and 'A1 Pre-indexed' variants: is the 12-bit unsigned immediate byte offset, in the range 0 to 4095, defaulting to 0 if omitted, and encoded in the 'imm12' field.

For the 'T1' variant: is an optional 5-bit unsigned immediate byte offset, in the range 0 to 31, defaulting to 0 and encoded in the 'imm5' field.

For the 'T2' variant: is an optional 12-bit unsigned immediate byte offset, in the range 0 to 4095, defaulting to 0 and encoded in the 'imm12' field.

For the 'T3 Offset', 'T3 Post-indexed', and 'T3 Pre-indexed' variants: is an 8-bit unsigned immediate byte offset, in the range 0 to 255, defaulting to 0 if omitted, and encoded in the 'imm8' field.

Specifies the offset is added to the base register.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) offset_addr = if add then (R[n] + imm32) else (R[n] imm32); constant bits(32) address = if index then offset_addr else R[n];
```

+

```
MemU[address,1] = R[t]<7:0>; if wback then R[n] = offset_addr;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.