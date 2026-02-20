## C1.1 About the A64 instruction set

The A64 instruction set is the instruction set supported in the AArch64 Execution state. All A64 instructions have a width of 32 bits.

The following chapters contain alphabetical lists of A64 instructions:

- A64 Base Instruction Descriptions lists all of:
- -Branch instructions, exception generating instructions, system instructions.
- -Load, store, and data-processing instructions associated with the general-purpose registers.
- A64 Advanced SIMD and Floating-point Instruction Descriptions lists the load, store, and data-processing instructions associated with Advanced SIMD and floating-point support.
- SVE Instruction Descriptions lists the load, store, and data-processing instructions associated with SVE support.
- SMEInstruction Descriptions lists the load, store, and data-processing instructions associated with SME support.

When an instruction supports more than one syntax, each syntax is an instruction variant . Instruction variants can occur because of differences in:

- The size or format of the operands.
- The register file used for the operands.
- The addressing mode used for load/load/store memory operands.

Instruction variants might also arise as the result of other factors.

Instruction variants are described in the instruction description for the individual instructions.

A64 instruction set encoding describes the A64 encoding structure. A64 instructions have a regular bit encoding structure:

- 5-bit register operand fields at fixed positions within the instruction. For general-purpose register operands, the values 0-30 select one of 31 registers. The value 31 is used as a special case that can:
- -Indicate use of the current stack pointer, when identifying a load/store base register or in a limited set of data-processing instructions. See The stack pointer registers.
- -Indicate the value zero when used as a source register operand.
- -Indicate discarding the result when used as a destination register operand.
- For Advanced SIMD and floating-point register access and SVE scalable vector register access, a 5-bit register operand field selects one of 32 registers of the appropriate type.
- Certain Advanced SIMD, SVE, and SME instructions have a register operand field smaller than 5 bits when specifying an indexed vector element or multi-vector operand, which restricts the number of vector registers that can be accessed by those operands.
- For SME instructions that access ZA tiles, ZA tile slices, or ZA array vectors, see ZA storage.
- Immediate bits that provide constant data-processing values or address offsets are placed in contiguous bitfields. Some computed values in instruction variants use one or more immediate bitfields together with the secondary encoding bitfields.

All encodings that are not fully defined are described as unallocated. An attempt to execute an unallocated instruction is UNDEFINED, unless the behavior is otherwise defined in this Manual.