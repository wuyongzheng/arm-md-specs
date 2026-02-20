## F3.2 About the T32 Advanced SIMD and floating-point instructions and their encoding

The Advanced SIMD and floating-point instructions are common to the T32 and A32 instruction sets. These instructions perform Advanced SIMD and floating-point operations on a common register file, the SIMD&amp;FP register file. This means:

- In general, the instructions that load or store registers in this file, or move data between general-purpose registers and this register file, are common to the Advanced SIMD and floating-point instructions.
- There are distinct Advanced SIMD data-processing instructions and floating-point data-processing instructions.

All T32 Advanced SIMD and floating-point instructions have 32-bit encodings. Different groups of these instructions are decoded from different points in the 32-bit T32 instruction decode structure. Table F3-106 shows these instruction groups, and where each group is decoded from the overall T32 decode structure:

## Table F3-106 Advanced SIMD and floating-point instructions in the T32 decode structure

| Advanced SIMD and floating-point instruction group           | T32 decode is from                                        |
|--------------------------------------------------------------|-----------------------------------------------------------|
| Advanced SIMD and System register load/store and 64-bit move | System register access, Advanced SIMD, and floating-point |
| Floating-point data-processing                               | System register access, Advanced SIMD, and floating-point |
| Advanced SIMD and System register 32-bit move                | System register access, Advanced SIMD, and floating-point |
| Advanced SIMD data-processing                                | System register access, Advanced SIMD, and floating-point |
| Advanced SIMD element or structure load/store                | 32-bit                                                    |

## Chapter F4 A32 Instruction Set Encoding

This chapter describes the encoding of the A32 instruction set. It contains the following sections:

- A32 instruction set encoding.
- About the A32 Advanced SIMD and floating-point instructions and their encoding.

## In this chapter:

- In the decode tables, an entry of x for a field value means the value of the field does not affect the decoding.
- In the decode diagrams, a shaded field indicates that the bits in that field are not used in that level of decode.