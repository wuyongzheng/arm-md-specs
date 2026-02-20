## F5.1.170 RSC, RSCS (immediate)

Reverse Subtract with Carry (immediate) subtracts a register value and the value of NOT (Carry flag) from an immediate value, and writes the result to the destination register.

If the destination register is not the PC, the RSCS variant of the instruction updates the condition flags based on the result.

The field descriptions for &lt;Rd&gt; identify the encodings where the PC is permitted as the destination register. ARM deprecates any use of these encodings. However, when the destination register is the PC:

- The RSC variant of the instruction is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.
- The RSCS variant of the instruction performs an exception return without the use of the stack. In this case:
- The PE branches to the address written to the PC, and restores PSTATE from SPSR\_&lt;current\_mode&gt;.
- The PE checks SPSR\_&lt;current\_mode&gt; for an illegal return event. See Illegal return events from AArch32 state.
- The instruction is UNDEFINED in Hyp mode.
- The instruction is CONSTRAINED UNPREDICTABLE in User mode and System mode.

<!-- image -->

## Encoding for the RSC variant

```
Applies when (S == 0) RSC{<c>}{<q>}
```

```
{<Rd>, }<Rn>, #<const>
```

## Encoding for the RSCS variant

Applies when

```
{<Rd>, }<Rn>, #<const>
```

```
(S == 1) RSCS{<c>}{<q>}
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant boolean setflags = (S == '1'); constant bits(32) imm32 =
```

```
A32ExpandImm(imm12);
```

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the general-purpose destination register, encoded in the 'Rd' field. If omitted, this register is the same as &lt;Rn&gt; . Arm deprecates using the PC as the destination register, but if the PC is used:

- For the RSC variant, the instruction is a branch to the address calculated by the operation. This is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.

&lt;q&gt;

## &lt;Rd&gt;

## &lt;Rn&gt;

Is the general-purpose source register, encoded in the 'Rn' field. The PC can be used, but this is deprecated.

## &lt;const&gt;

An immediate value. See Modified immediate constants in A32 instructions for the range of values.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); bits(32) result; bits(4) nzcv; (result, nzcv) = AddWithCarry(NOT(R[n]), imm32, PSTATE.C); if d == 15 then if setflags then ALUExceptionReturn(result); else ALUWritePC(result); else R[d] = result; if setflags then PSTATE.<N,Z,C,V> = nzcv;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

- For the RSCS variant, the instruction performs an exception return, that restores PSTATE from SPSR\_&lt;current\_mode&gt;.