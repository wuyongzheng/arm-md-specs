## F2.2 Unified Assembler Language

This manual uses the Arm Unified Assembler Language (UAL). This assembly language syntax provides a canonical form for all T32 and A32 instructions.

UALdescribes the syntax for the mnemonic and the operands of each instruction. In addition, it assumes that instructions and data items can be given labels. It does not specify the syntax to be used for labels, nor what assembler directives and options are available. See your assembler documentation for these details.

Most earlier Arm assembly language mnemonics are still supported as synonyms, as described in the instruction details.

Note

Most earlier T32 assembly language mnemonics are not supported.

UALincludes instruction selection rules that specify which instruction encoding is selected when more than one can provide the required functionality. For example, both 16-bit and 32-bit encodings exist for an ADD R0, R1, R2 instruction. The most common instruction selection rule is that when both a 16-bit encoding and a 32-bit encoding are available, the 16-bit encoding is selected, to optimize code density.

Syntax options exist to override the normal instruction selection rules and ensure that a particular encoding is selected. These are useful when disassembling code, to ensure that subsequent assembly produces the original code, and in some other situations.

## F2.2.1 Conditional instructions

For maximum portability of UAL assembly language between the T32 and A32 instruction sets, Arm recommends that:

- IT instructions are written before conditional instructions in the correct way for the T32 instruction set.
- When assembling to the A32 instruction set, assemblers check that any IT instructions are correct, but do not generate any code for them.

Although other T32 instructions are unconditional, all instructions that are made conditional by an IT instruction must be written with a condition. These conditions must match the conditions imposed by the IT instruction. For example, an ITTEE EQ instruction imposes the EQ condition on the first two following instructions, and the NE condition on the next two. Those four instructions must be written with EQ , EQ , NE and NE conditions respectively.

Some instructions cannot be made conditional by an IT instruction. Some instructions can be conditional if they are the last instruction in the IT block, but not otherwise.

The branch instruction encodings that include a condition code field cannot be made conditional by an IT instruction. If the assembler syntax indicates a conditional branch that correctly matches a preceding IT instruction, it is assembled using a branch instruction encoding that does not include a condition code field.

## F2.2.2 Use of labels in UAL instruction syntax

The UAL syntax for some instructions includes the label of an instruction or a literal data item that is at a fixed offset from the instruction being specified. The assembler must:

1. Calculate the PC or Align(PC, 4) value of the instruction. The PC value of an instruction is its address plus 4 for a T32 instruction, or plus 8 for an A32 instruction. The Align(PC, 4) value of an instruction is its PC value ANDed with 0xFFFFFFFC to force it to be word-aligned. There is no difference between the PC and Align(PC, 4) values for an A32 instruction, but there can be for a T32 instruction.
2. Calculate the offset from the PC or Align(PC, 4) value of the instruction to the address of the labeled instruction or literal data item.

3. Assemble a PC-relative encoding of the instruction, that is, one that reads its PC or Align(PC, 4) value and adds the calculated offset to form the required address.

Note

For instructions that can encode a subtraction operation, if the instruction cannot encode the calculated offset but can encode minus the calculated offset, the instruction encoding specifies a subtraction of minus the calculated offset.

The syntax of the following instructions includes a label:

- B , BL , and BLX (immediate). The assembler syntax for these instructions always specifies the label of the instruction that they branch to. Their encodings specify a sign-extended immediate offset that is added to the PC value of the instruction to form the target address of the branch.
- CBNZ and CBZ . The assembler syntax for these instructions always specifies the label of the instruction that they branch to. Their encodings specify a zero-extended immediate offset that is added to the PC value of the instruction to form the target address of the branch. They do not support backward branches.
- LDR , LDRB , LDRD , LDRH , LDRSB , LDRSH , PLD , PLDW , PLI , and VLDR . The normal assembler syntax of these load instructions can specify the label of a literal data item that is to be loaded. The encodings of these instructions specify a zero-extended immediate offset that is either added to or subtracted from the Align(PC, 4) value of the instruction to form the address of the data item. A few such encodings perform a fixed addition or a fixed subtraction and must only be used when that operation is required, but most contain a bit that specifies whether the offset is to be added or subtracted.

When the assembler calculates an offset of 0 for the normal syntax of these instructions, it must assemble an encoding that adds 0 to the Align(PC, 4) value of the instruction. Encodings that subtract 0 from the Align(PC, 4) value cannot be specified by the normal syntax.

There is an alternative syntax for these instructions that specifies the addition or subtraction and the immediate offset explicitly. In this syntax, the label is replaced by [PC, #+/-&lt;imm&gt;] , where:

- +/-

Is + or omitted to specify that the immediate offset is to be added to the Align(PC, 4) value, or -if it is to be subtracted.

&lt;imm&gt;

Is the immediate offset.

This alternative syntax makes it possible to assemble the encodings that subtract 0 from the Align(PC, 4) value, and to disassemble them to a syntax that can be re-assembled correctly.

- ADR . The normal assembler syntax for this instruction can specify the label of an instruction or literal data item whose address is to be calculated. Its encoding specifies a zero-extended immediate offset that is either added to or subtracted from the Align(PC, 4) value of the instruction to form the address of the data item, and some opcode bits that determine whether it is an addition or subtraction.

When the assembler calculates an offset of 0 for the normal syntax of this instruction, it must assemble the encoding that adds 0 to the Align(PC, 4) value of the instruction. The encoding that subtracts 0 from the Align(PC, 4) value cannot be specified by the normal syntax.

There is an alternative syntax for this instruction that specifies the addition or subtraction and the immediate value explicitly, by writing them as additions ADD &lt;Rd&gt;, PC, #&lt;imm&gt; or subtractions SUB &lt;Rd&gt;, PC, #&lt;imm&gt; . This alternative syntax makes it possible to assemble the encoding that subtracts 0 from the Align(PC, 4) value, and to disassemble it to a syntax that can be re-assembled correctly.

Note

Arm recommends that where possible, software avoids using:

- The alternative syntax for the ADR , LDC , LDR , LDRB , LDRD , LDRH , LDRSB , LDRSH , PLD , PLI , PLDW , and VLDR instructions.
- The encodings of these instructions that subtract 0 from the Align(PC, 4) value.