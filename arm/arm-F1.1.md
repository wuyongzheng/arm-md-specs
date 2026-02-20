## F1.1 Format of instruction descriptions

The instruction descriptions in T32 and A32 Base Instruction Set Instruction Descriptions and T32 and A32 Advanced SIMD and Floating-point Instruction Descriptions normally use the following format:

- Instruction section title.
- Introduction to the instruction.
- Adescription of each encoding of the instruction.
- Assembler syntax.
- Pseudocode describing how the instruction operates.
- Notes, if applicable.

Each of these items is described in more detail in the following subsections.

## F1.1.1 Instruction section title

The instruction section title gives the base mnemonic for the instruction or instructions described in the section. When one mnemonic has multiple forms described in separate instruction sections, this is followed by a short description of the form in parentheses. The most common use of this is to distinguish between forms of an instruction in which one of the operands is an immediate value and forms in which it is a register.

## F1.1.2 Introduction to the instruction

The introduction to the instruction briefly describes the main features of the instruction. This description is not necessarily complete and is not definitive. If there is any conflict between it and the more detailed information that follows, the latter takes priority.

## F1.1.3 Instruction encodings

This is a list of one or more instruction encodings. Each instruction encoding is labeled as:

- A1, A2, A3 . . . for the first, second, third, and any additional A32 encodings.
- T1, T2, T3 . . . for the first, second, third, and any additional T32 encodings.

Each instruction encoding description consists of:

- An assembly syntax that ensures that the assembler selects the encoding in preference to any other encoding. Sometimes, multiple syntax variants are given. These are written in a typewriter font using the conventions described in Assembler syntax prototype line conventions. The correct one to use can be indicated by:
- -Asubheading that identifies the encodings that correspond to the syntax. See, for example, the subheading Flag setting, rotate right with extend variant in the description of the A1 encoding of the ADC , ADCS (register) instructions in A1.
- -An annotation to the syntax, such as Inside IT block or Outside IT block . See, for example, the syntax descriptions of the T1 encoding of the ADC , ADCS (register) instructions in T1.

In other cases, the correct one to use can be determined by looking at the assembler syntax description and using it to determine which syntax corresponds to the instruction being disassembled.

There is usually more than one syntax variant that ensures re-assembly to any particular encoding, and the exact set of syntaxes that do so usually depends on the register numbers, immediate constants, and other operands to the instruction. For example, when assembling to the T32 instruction set, the syntax AND R0, R0, R8 ensures selection of a 32-bit encoding but AND R0, R0, R1 selects a 16-bit encoding.

For each instruction encoding belonging to a target instruction set, an assembler can use this information to determine whether it can use that encoding to encode the instruction requested by the UAL source. If multiple encodings can encode the instruction, then:

- -If both a 16-bit encoding and a 32-bit encoding can encode the instruction, the architecture prefers the 16-bit encoding. This means the assembler must use the 16-bit encoding rather than the 32-bit encoding. Software can use the .W and .N qualifiers to specify the required encoding width, see Standard assembler syntax fields.

- -If multiple encodings of the same length can encode the instruction, the Assembler syntax subsection says which encoding is preferred, and how software can, instead, select the other encodings. Each encoding also documents UAL syntax that selects it in preference to any other encoding.

If no encodings of the target instruction set can encode the instruction requested by the UAL source, normally the assembler generates an error saying that the instruction is not available in that instruction set.

Note

In some cases, an instruction is available in one instruction set but not in another. The Assembler syntax subsection identifies many of these cases. For example, the A32 instructions with bits&lt;31:28&gt; == 0b1111 described in Branch, branch with link, and block data transfer, System register access, Advanced SIMD, floating-point, and Supervisor call, and Unconditional instructions cannot have a Condition code, but the equivalent T32 instructions often can, and this usually appears in the Assembler syntax subsection as a statement that the A32 instruction cannot be conditional.

However, some such cases are too complex to describe in the available space, so the definitive test of whether an instruction is available in a given instruction set is whether there is an available encoding for it in that instruction set.

The assembly syntax given for an encoding is therefore a suitable one for a disassembler to disassemble that encoding to. However, disassemblers might use simpler syntaxes when they are suitable for the operand combination, to produce more readable disassembled code.

- An encoding diagram, where:
- -For a 32-bit A32 encoding diagram, the bits are numbered from 31-0.
- -For a 16-bit T32 encoding diagram, the bits are numbered from 15-0. This halfword can be described as hw1 of the instruction.
- -For a 32-bit T32 encoding diagram, the bits are numbered from 15-0 for each halfword, as a reminder that a 32-bit T32 instruction consists of two consecutive halfwords rather than a word. In this case, the left-hand halfword in the diagram is identified as hw1 , and the right-hand halfword is identified as hw2 .

Where instructions are stored using the standard little-endian instruction endianness:

- -The encoding diagram for an A32 instruction at address A shows, from left to right, the bytes at addresses A+3, A+2, A+1, A.
- -The encoding diagram for a 32-bit T32 instruction shows bytes in the order A+1, A for hw1 , followed by bytes A+3, A+2 for hw2 .
- Encoding-specific pseudocode. This is pseudocode that translates the encoding-specific instruction fields into inputs to the encoding-independent pseudocode in the Operation subsection, and that picks out any special cases in the encoding. For a detailed description of the pseudocode used and of the relationship between the encoding diagram, the encoding-specific pseudocode and the encoding-independent pseudocode, see Arm Pseudocode Definition.

## F1.1.4 Assembler symbols

The Assembly symbols describe the standard UAL syntax for the instruction.

Each syntax description consists of the following elements:

- Descriptions of all variable or optional fields of the syntax.

Some syntax fields are standardized across all or most instructions. Standard assembler syntax fields describes these fields.

By default, syntax fields that specify registers, such as &lt;Rd&gt; , &lt;Rn&gt; , or &lt;Rt&gt; , can be any of R0-R12 or LR in T32 instructions, and any of R0-R12, SP, or LR in A32 instructions. These require that the encoding-specific pseudocode set the corresponding integer variable (such as d , n , or t ) to the corresponding register number, using 0-12 for R0-R12, 13 for SP, or 14 for LR:

- -Normally, software can do this by setting the corresponding field in the instruction, typically named Rd, Rn, Rt, to the binary encoding of that number.
- -In the case of 16-bit T32 encodings, the field is normally of length 3, and so the encoding is available only when the assembler syntax specifies one of R0-R7. Such encodings often use a register field name like Rdn. This indicates that the encoding is available only if &lt;Rd&gt; and &lt;Rn&gt; specify the same register, and that the register number of that register is encoded in the field if they do.

spaces

- +/-

The description of a syntax field that specifies a register sometimes extends or restricts the permitted range of registers or documents other differences from the default rules for such fields. Examples of extensions are permitting the use of the SP in a T32 instruction, or permitting the use of the PC, identified using register number 15.

- Where appropriate, text that briefly describes changes from the pre-UAL assembler syntax. Where present, this usually consists of an alternative pre-UAL form of the assembler mnemonic. The pre-UAL assembler syntax does not conflict with UAL. Arm recommends that it is supported, as an optional extension to UAL, so that pre-UAL assembler source files can be assembled.

## F1.1.4.1 Assembler syntax prototype line conventions

The following conventions are used in assembler syntax prototype lines and their subfields:

- &lt; &gt; Any item bracketed by &lt; and &gt; is a short description of a type of value to be supplied by the user in that position. A longer description of the item is normally supplied by subsequent text. Such items often correspond to a similarly named field in an encoding diagram for an instruction. When the correspondence requires only the binary encoding of an integer value or register number to be substituted into the instruction encoding, it is not described explicitly. For example, if the assembler syntax for an instruction contains an item &lt;Rn&gt; and the instruction encoding diagram contains a 4-bit field named Rn, the number of the register specified in the assembler syntax is encoded in binary in the instruction field.

If the correspondence between the assembler syntax item and the instruction encoding is more complex than simple binary encoding of an integer or register number, the item description indicates how it is encoded. This is often done by specifying a required output from the encoding-specific pseudocode, such as add = TRUE . The assembler must use only encodings that produce that output.

- { } Any item bracketed by { and } is optional. A description of the item and of how its presence or absence is encoded in the instruction is normally supplied by subsequent text.

Many instructions have an optional destination register. Unless otherwise stated, if such a destination register is omitted, it is the same as the immediately following source register in the instruction syntax.

- # In the assembler syntax, numeric constants are normally preceded by a # . Some UAL instruction syntax descriptions explicitly show this # as optional. Any UAL assembler:
- Must treat the # as optional where an instruction syntax description shows it as optional.
- Can treat the # either as mandatory or as optional where an instruction syntax description does not show it as optional.

Note

Arm recommends that UAL assemblers treat all uses of # shown in this manual as optional.

Single spaces are used for clarity, to separate items. When a space is obligatory in the assembler syntax, two or more consecutive spaces are used.

This indicates an optional + or -sign. If neither is coded, + is assumed.

All other characters must be encoded precisely as they appear in the assembler syntax. Apart from { and } , the special characters described above do not appear in the basic forms of assembler instructions documented in this manual. In a few places, the { and } characters must be encoded as part of a variable item. When this happens, the long description of the variable item indicates how they must be used.

## F1.1.5 Pseudocode describing how the instruction operates

The Operation for all classes subsection contains encoding-independent pseudocode that describes the main operation of the instruction. For a detailed description of the pseudocode used and of the relationship between the encoding diagram, the encoding-specific pseudocode and the encoding-independent pseudocode, see Arm Pseudocode Definition.