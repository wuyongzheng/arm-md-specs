## C2.1 Understanding the A64 instruction descriptions

Each instruction description in A64 Base Instruction Descriptions, A64 Advanced SIMD and Floating-point Instruction Descriptions, SVE Instruction Descriptions, and SME Instruction Descriptions has the following content:

1. Atitle.
2. An introduction to the instruction.
3. The instruction encoding or encodings.
4. Any alias conditions.
5. Alist of the assembler symbols for the instruction.
6. Pseudocode describing how the instruction operates.
7. Notes, if applicable.

The following sections describe each of these.

The title of an instruction description includes the base mnemonic for the instruction.

If different forms of an instruction use the same base mnemonic, each form has its own description. In this case, the title is the mnemonic followed by a short description of the instruction form in parentheses. This is most often used when an operand is an immediate value in one instruction form, but is a register in another form.

For example, in A64 Base Instruction Descriptions there are the following titles for different forms of the ADD instruction:

- ADD(extended register).
- ADD(immediate).
- ADD(shifted register).

## C2.1.2 An introduction to the instruction

This briefly describes the function of the instruction. The introduction is not a complete description of the instruction, and it is not definitive. If there is any conflict between it and the more detailed information that follows it, the more detailed information takes priority.

## C2.1.3 The instruction encoding or encodings

This shows the instruction encoding diagram, or if the instruction has more than one encoding, shows all of the encoding diagrams. Each diagram has a subheading.

For example, for load and store instructions, the subheadings might be:

- Post-index.
- Pre-index.
- Unsigned offset.

Each diagram numbers the bits from 31 to 0. The diagram for an instruction at address A shows, from left to right, the bytes at addresses A +3, A +2, A +1, and A .

There might be variants of an encoding, if the assembler syntax prototype differs depending on the value in one or more of the encoding fields. In this case, each variant has a subheading that describes the variant and shows the distinguishing field value or values in parentheses. For example, in A64 Base Instruction Descriptions there are the following subheadings for variants of the ADC instruction encoding:

- 32-bit variant (sf = 0).
- 64-bit variant (sf = 1).

## C2.1.1 The title

The assembler syntax prototype for an encoding or variant of an encoding shows how to form a complete assembler source code instruction that assembles to the encoding. Unless otherwise stated, the prototype is also the preferred syntax for a disassembler to disassemble the encoding to. Disassemblers are permitted to omit optional symbols that represent the default value of a field or set of fields, to produce more readable disassembled code, provided that the output re-assembles to the same encoding.

Each encoding diagram, and its associated assembler syntax prototypes, is followed by encoding-specific pseudocode that translates the fields of that encoding into inputs for the encoding-independent pseudocode that describes the operation of the instruction. See Pseudocode describing how the instruction operates.

## C2.1.4 Any alias conditions, if applicable

This is an optional part of an instruction description. If included, it describes the set of conditions for which an alternative mnemonic and its associated assembler syntax prototypes are preferred for disassembly by a disassembler. It includes a link to the alias instruction description that defines the alternative syntax. The alias syntax and the original syntax can be used interchangeably in the assembler source code.

Arm recommends that if a disassembler outputs the alias syntax, it consistently outputs the alias syntax.

## C2.1.5 A list of the assembler symbols for the instruction

The Assembler symbols subsection of the instruction description contains a list of the symbols that the assembler syntax prototype or prototypes use, if any.

In assembler syntax prototypes, the following conventions are used:

| < >   | Angle brackets. Any symbol enclosed by these is a name or a value that the user supplies. For each symbol, there is a description of what the symbol represents. The description usually also specifies which encoding field or fields encodes the symbol.                                                                                                                                                                  |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| { }   | Brace brackets. Any symbols enclosed by these are optional. For each optional symbol, there is a description of what the symbol represents and how its presence or absence is encoded. In some assembler syntax prototypes, some brace brackets are mandatory, for example if they surround a register list. When the use of brace brackets is mandatory, they are separated from other syntax items by one or more spaces. |
| #     | This usually precedes a numeric constant. All uses of # are optional in A64 assembler source code. Arm recommends that disassemblers output the # where the assembler syntax prototype includes it.                                                                                                                                                                                                                         |
| +/-   | This indicates an optional + or - sign. If neither is coded, + is assumed.                                                                                                                                                                                                                                                                                                                                                  |

Single spaces are used for clarity, to separate syntax items. Where a space is mandatory, the assembler syntax prototype shows two or more consecutive spaces.

Any characters not shown in this conventions list must be coded exactly as shown in the assembler syntax prototype. Apart from brace brackets, the characters shown are used as part of a meta-language to define the architectural assembler syntax for an instruction encoding or alias, but have no architecturally defined significance in the input to an assembler or in the output from a disassembler.

The following symbol conventions are used:

| <Xn>          | The 64-bit name of a general-purpose register (X0-X30) or the zero register (XZR).                                                             |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| <Wn>          | The 32-bit name of a general-purpose register (W0-W30) or the zero register (WZR).                                                             |
| <Xn&#124;SP>  | The 64-bit name of a general-purpose register (X0-X30) or the current stack pointer (SP).                                                      |
| <Wn&#124;WSP> | The 32-bit name of a general-purpose register (W0-W30) or the current stack pointer (WSP).                                                     |
| <Bn>, <Hn>,   | <Sn>, <Dn>, <Qn> The 8, 16, 32, 64, or 128-bit name of a SIMD and floating-point register in a scalar context, as described in Register names. |
| <Vn>          | The name of a SIMD and floating-point register in a vector context, as described in Register names.                                            |

&lt;Zn&gt;

&lt;Pn&gt;

The name of an SVE scalable vector register, as described in Treatment of SVE scalable vector registers.

The name of an SVE scalable predicate register, as described in Vector predication.

If the description of a symbol specifies that the symbol is a register, the description might also specify that the range of permitted registers is extended or restricted. It also specifies any differences from the default rules for such fields.

For information about SME conventions, see ZA storage.

Note

Register names provides the A64 register names.

## C2.1.6 Pseudocode describing how the instruction operates

The Operation subsection of the instruction description contains this pseudocode.

It is encoding-independent pseudocode that provides a precise description of what the instruction does.

Note

For a description of Arm pseudocode, see Arm Pseudocode Definition. This appendix also describes the execution model for an instruction.

## C2.1.7 Notes, if applicable

If applicable, other notes about the instruction appear under additional subheadings.