## F4.2 About the A32 Advanced SIMD and floating-point instructions and their encoding

The Advanced SIMD and floating-point instructions are common to the T32 and A32 instruction sets. These instructions perform Advanced SIMD and floating-point operations on a common register file, the SIMD&amp;FP register file. This means:

- In general, the instructions that load or store registers in this file, or move data between general-purpose registers and this register file, are common to the Advanced SIMD and floating-point instructions.
- There are distinct Advanced SIMD data-processing instructions and floating-point data-processing instructions.

All A32 Advanced SIMD and floating-point instructions have 32-bit encodings. Different groups of these instructions are decoded from different points in the 32-bit A32 instruction decode structure. Table F4-90 shows these instruction groups, and where each group is decoded from the overall A32 decode structure:

Table F4-90 Advanced SIMD and floating-point instructions in the A32 decode structure

| Advanced SIMD and floating-point instruction group           | A32 decode is from                                                         |
|--------------------------------------------------------------|----------------------------------------------------------------------------|
| Advanced SIMD and System register load/store and 64-bit move | System register access, Advanced SIMD, floating-point, and Supervisor call |
| Floating-point data-processing                               | System register access, Advanced SIMD, floating-point, and Supervisor call |
| Advanced SIMD and System register 32-bit move                | System register access, Advanced SIMD, floating-point, and Supervisor call |
| Advanced SIMD data-processing                                | Unconditional instructions                                                 |
| Advanced SIMD element or structure load/store                | Unconditional instructions                                                 |

## Chapter F5 T32 and A32 Base Instruction Set Instruction Descriptions

This chapter describes each instruction. It contains the following sections:

- Alphabetical list of T32 and A32 base instruction set instructions.
- Encoding and use of banked register transfer instructions.