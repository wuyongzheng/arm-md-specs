## F5.1.10 ADR

Form PC-relative address adds an immediate value to the PC value to form a PC-relative address, and writes the result to the destination register.

This instruction is used by the alias SUB (immediate, from PC).

This instruction is used by the pseudo-instruction ADD (immediate, to PC).

It has encodings from the following instruction sets: A32 (A1 and A2) and T32 (T1, T2, and T3).

A1

<!-- image -->

## Encoding

ADR{&lt;c&gt;}{&lt;q&gt;} &lt;Rd&gt;, &lt;label&gt;

## Decode for this encoding

```
= A32ExpandImm(imm12);
```

```
constant integer d = UInt(Rd); constant bits(32) imm32 constant boolean add = TRUE;
```

## A2

<!-- image -->

## Encoding

ADR{&lt;c&gt;}{&lt;q&gt;} &lt;Rd&gt;, &lt;label&gt;

## Decode for this encoding

```
constant integer d = UInt(Rd); constant bits(32) imm32 = A32ExpandImm(imm12); constant boolean add = FALSE;
```

Listing F5-1

Listing F5-2

T1

## Encoding

```
ADR{<c>}{<q>} <Rd>, <label>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant bits(32) imm32 = ZeroExtend(imm8:'00', 32); constant boolean add = TRUE;
```

T2

<!-- image -->

## Encoding

```
ADR{<c>}{<q>} <Rd>, <label>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant bits(32) imm32 = ZeroExtend(i:imm3:imm8, 32); constant boolean add = FALSE; // Armv8-A removes UNPREDICTABLE for R13 if d == 15 then UNPREDICTABLE; end
```

T3

<!-- image -->

## Encoding

ADR{&lt;c&gt;}{&lt;q&gt;} &lt;Rd&gt;, &lt;label&gt;

```
ADR{<c>}.W <Rd>, <label> // (<Rd>, <label> can be presented in T1)
```

<!-- image -->

Listing F5-3

Listing F5-4

## Decode for this encoding

```
constant integer d = UInt(Rd); constant bits(32) imm32 = ZeroExtend(i:imm3:imm8, 32); constant boolean add = TRUE; // Armv8-A removes UNPREDICTABLE for R13 if d == 15 then UNPREDICTABLE; end
```

For more information about the CONSTRAINED UNPREDICTABLE behavior, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

For the 'A1' and 'A2' variants: is the general-purpose destination register, encoded in the 'Rd' field. If the PC is used, the instruction is a branch to the address calculated by the operation. This is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.

For the 'T1', 'T2', and 'T3' variants: is the general-purpose destination register, encoded in the 'Rd' field.

## &lt;label&gt;

For the 'A1' and 'A2' variants: the label of an instruction or literal data item whose address is to be loaded into &lt;Rd&gt; . The assembler calculates the required value of the offset from the Align(PC, 4) value of the ADR instruction to this label.

If the offset is zero or positive, encoding A1 is used, with imm32 equal to the offset.

If the offset is negative, encoding A2 is used, with imm32 equal to the size of the offset. That is, the use of encoding A2 indicates that the required offset is minus the value of imm32 .

Permitted values of the size of the offset are any of the constants described in Modified immediate constants in A32 instructions.

For the 'T1' variant: the label of an instruction or literal data item whose address is to be loaded into &lt;Rd&gt; . The assembler calculates the required value of the offset from the Align(PC, 4) value of the ADR instruction to this label. Permitted values of the size of the offset are multiples of 4 in the range 0 to 1020.

For the 'T2' and 'T3' variants: the label of an instruction or literal data item whose address is to be loaded into &lt;Rd&gt; . The assembler calculates the required value of the offset from the Align(PC, 4) value of the ADR instruction to this label.

If the offset is zero or positive, encoding T3 is used, with imm32 equal to the offset.

If the offset is negative, encoding T2 is used, with imm32 equal to the size of the offset. That is, the use of encoding T2 indicates that the required offset is minus the value of imm32 .

Permitted values of the size of the offset are 0-4095.

The instruction aliases permit the addition or subtraction of the offset and the immediate offset to be specified separately, including permitting a subtraction of 0 that cannot be specified using the normal syntax. For more information, see Use of labels in UAL instruction syntax.

## Alias Conditions

&lt;q&gt;

## &lt;Rd&gt;

| Alias                    | Of variant   | Is preferred when                 |
|--------------------------|--------------|-----------------------------------|
| ADD (immediate, to PC)   |              | Never                             |
| SUB (immediate, from PC) | A2           | imm12 == '000000000000'           |
| SUB (immediate, from PC) | T2           | i : imm3 : imm8 == '000000000000' |

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) result = (if add then (Align(PC32,4) + imm32) else (Align(PC32,4) imm32)); if d == 15 then // Can only occur for A32 encodings ALUWritePC(result); else R[d] = result; end end
```

Listing F5-6