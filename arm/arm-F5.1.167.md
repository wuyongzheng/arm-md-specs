## F5.1.167 RSB, RSBS (immediate)

Reverse Subtract (immediate) subtracts a register value from an immediate value, and writes the result to the destination register.

If the destination register is not the PC, the RSBS variant of the instruction updates the condition flags based on the result.

The field descriptions for &lt;Rd&gt; identify the encodings where the PC is permitted as the destination register. ARM deprecates any use of these encodings. However, when the destination register is the PC:

- The RSB variant of the instruction is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.
- The RSBS variant of the instruction performs an exception return without the use of the stack. In this case:
- The PE branches to the address written to the PC, and restores PSTATE from SPSR\_&lt;current\_mode&gt;.
- The PE checks SPSR\_&lt;current\_mode&gt; for an illegal return event. See Illegal return events from AArch32 state.
- The instruction is UNDEFINED in Hyp mode.
- The instruction is CONSTRAINED UNPREDICTABLE in User mode and System mode.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding for the RSB variant

```
Applies when (S == 0) RSB{<c>}{<q>} {<Rd>, }<Rn>, #<const>
```

## Encoding for the RSBS variant

```
Applies when (S == 1) RSBS{<c>}{<q>} {<Rd>, }<Rn>, #<const>
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant boolean setflags = (S == '1'); constant bits(32) imm32 =
```

T1

## Encoding

```
A32ExpandImm(imm12);
```

<!-- image -->

```
RSB<c>{<q>} {<Rd>, }<Rn>, #0 // (InITBlock()) RSBS{<q>} {<Rd>, }<Rn>, #0 // (Outside IT block)
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant boolean setflags = !InITBlock(); constant bits(32) imm32 = Zeros(32); // immediate =
```

T2

<!-- image -->

## Encoding for the RSB variant

```
Applies when (S == 0) RSB{<c>}{<q>} {<Rd>, }<Rn>, #<const> RSB<c>.W {<Rd>, }<Rn>, #0 // (Inside IT block)
```

## Encoding for the RSBS variant

```
Applies when (S == 1) RSBS{<c>}{<q>} {<Rd>, }<Rn>, #<const> RSBS.W {<Rd>, }<Rn>, #0 // (Outside IT block)
```

## Decode for all variants of this encoding

```
T32ExpandImm(i:imm3:imm8);
```

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant boolean setflags = (S == '1'); constant bits(32) imm32 = // Armv8-A removes UNPREDICTABLE for R13 if d == 15 || n == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

<!-- image -->

```
<c> See Standard assembler syntax fields. <q> See Standard assembler syntax fields.
```

```
#0
```

## &lt;Rd&gt;

## &lt;Rn&gt;

For the 'A1 RSB' and 'A1 RSBS' variants: is the general-purpose destination register, encoded in the 'Rd' field. If omitted, this register is the same as &lt;Rn&gt; . Arm deprecates using the PC as the destination register, but if the PC is used:

- For the RSB variant, the instruction is a branch to the address calculated by the operation. This is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.
- For the RSBS variant, the instruction performs an exception return, that restores PSTATE from SPSR\_&lt;current\_mode&gt;.

For the 'T1', 'T2 RSB', and 'T2 RSBS' variants: is the general-purpose destination register, encoded in the 'Rd' field. If omitted, this register is the same as &lt;Rn&gt; .

For the 'A1 RSB' and 'A1 RSBS' variants: is the general-purpose source register, encoded in the 'Rn' field. The PC can be used, but this is deprecated.

For the 'T1', 'T2 RSB', and 'T2 RSBS' variants: is the general-purpose source register, encoded in the 'Rn' field.

## &lt;const&gt;

For the 'A1 RSB' and 'A1 RSBS' variants: an immediate value. See Modified immediate constants in A32 instructions for the range of values.

For the 'T2 RSB' and 'T2 RSBS' variants: an immediate value. See Modified immediate constants in T32 instructions for the range of values.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); bits(32) result; bits(4) nzcv; (result, nzcv) = AddWithCarry(NOT(R[n]), imm32, '1'); if d == 15 then // Can only occur for A32 encoding if setflags then ALUExceptionReturn(result); else ALUWritePC(result); else R[d] = result; if setflags then PSTATE.<N,Z,C,V> = nzcv;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.