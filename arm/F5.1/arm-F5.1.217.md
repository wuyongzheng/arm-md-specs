## F5.1.217 STC

Store data to System register calculates an address from a base register value and an immediate offset, and stores a word from the DBGDTRRXint System register to memory. It can use offset, post-indexed, pre-indexed, or unindexed addressing. For information about memory accesses, see Memory accesses.

In an implementation that includes EL2, the permitted STC access to DBGDTRRXint can be trapped to Hyp mode, meaning that an attempt to execute an STC instruction in a Non-secure mode other than Hyp mode, that would be permitted in the absence of the Hyp trap controls, generates a Hyp Trap exception. For more information, see HDCR.TDA.

For simplicity, the STC pseudocode does not show this possible trap to Hyp mode.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the Offset variant

```
Applies when (P == 1 && W == 0) STC{<c>}{<q>} p14, c5, [<Rn>{, #{+/-}<imm>}]
```

## Encoding for the Post-indexed variant

```
Applies when (P == 0 && W == 1) STC{<c>}{<q>}
```

```
p14, c5, [<Rn>], #{+/-}<imm>
```

## Encoding for the Pre-indexed variant

```
Applies when (P == 1 && W == 1) STC{<c>}{<q>} p14, c5, [<Rn>, #{+/-}<imm>]!
```

## Encoding for the Unindexed variant

```
Applies when (P == 0 && U == 1 && W == 0) STC{<c>}{<q>} p14, c5, [<Rn>], <option>
```

## Decode for all variants of this encoding

```
if P == '0' && U == '0' && W == '0' then UNDEFINED; constant integer n = UInt(Rn); constant integer cp = 14; constant bits(32) imm32 = ZeroExtend(imm8:'00', 32); constant boolean index = (P == '1'); constant boolean add = (U == '1'); constant boolean wback = (W == '1'); if n == 15 && (wback || CurrentInstrSet() != InstrSet_A32) then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If n == 15 &amp;&amp; wback , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes without writeback of the base address.
- The instruction executes with writeback to the PC. The instruction is handled as described in Using R15.

T1

<!-- image -->

## Encoding for the Offset variant

```
Applies when (P == 1 && W == 0)
```

```
STC{<c>}{<q>} p14, c5, [<Rn>{, #{+/-}<imm>}]
```

## Encoding for the Post-indexed variant

Applies when

```
p14, c5, [<Rn>], #{+/-}<imm>
```

```
(P == 0 && W == 1) STC{<c>}{<q>}
```

## Encoding for the Pre-indexed variant

```
Applies when (P == 1 && W == 1) STC{<c>}{<q>} p14, c5, [<Rn>, #{+/-}<imm>]!
```

## Encoding for the Unindexed variant

Applies when (P == 0 &amp;&amp; U == 1 &amp;&amp; W ==

```
0) STC{<c>}{<q>} p14, c5, [<Rn>], <option>
```

## Decode for all variants of this encoding

```
if P == '0' && U == '0' && W == '0' then UNDEFINED; constant integer n = UInt(Rn); constant integer cp = 14; constant bits(32) imm32 = ZeroExtend(imm8:'00', 32); constant boolean index = (P == '1'); constant boolean add = (U == '1'); constant boolean wback = (W == '1'); if n == 15 && (wback || CurrentInstrSet() !=
```

```
InstrSet_A32) then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If n == 15 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes without writeback of the base address.
- The instruction executes with writeback to the PC. The instruction is handled as described in Using R15.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

For the 'A1 Offset' and 'A1 Unindexed' variants: is the general-purpose base register, encoded in the 'Rn' field. The PC can be used, but this is deprecated.

For the 'A1 Post-indexed', 'A1 Pre-indexed', 'T1 Offset', 'T1 Post-indexed', 'T1 Pre-indexed', and 'T1 Unindexed' variants: is the general-purpose base register, encoded in the 'Rn' field.

Specifies the offset is added to or subtracted from the base register, defaulting to + if omitted and encoded in 'U':

|   U | +/-   |
|-----|-------|
|   0 | -     |
|   1 | +     |

&lt;q&gt;

## &lt;Rn&gt;

+/-

## &lt;imm&gt;

Is the immediate offset used for forming the address, a multiple of 4 in the range 0-1020, defaulting to 0 and encoded in the 'imm8' field, as &lt;imm&gt;/4.

## &lt;option&gt;

Is an 8-bit immediate, in the range 0 to 255 enclosed in { }, encoded in the 'imm8' field. The value of this field is ignored when executing this instruction.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) offset_addr = if add then (R[n] + imm32) else (R[n] imm32); constant bits(32) address = if index then offset_addr else R[n]; // System register read from DBGDTRRXint. AArch32.SysRegRead(cp, ThisInstr(), address<31:0>); if wback then R[n] = offset_addr;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.