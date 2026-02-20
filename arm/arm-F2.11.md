## F2.11 Advanced SIMD and floating-point load/store instructions

Table F2-17 summarizes the SIMD and floating-point register file load/store instructions in the Advanced SIMD and floating-point instruction sets.

Advanced SIMD also provides instructions for loading and storing multiple elements, or structures of elements, see Element and structure load/store instructions.

Table F2-17 SIMD and floating-point register file load/store instructions

| Instruction           | See                           | Operation                                                                                                                                |
|-----------------------|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Vector Load Multiple  | VLDM,VLDMDB,VLDMIA            | Load 1-16 consecutive 64-bit registers, Advanced SIMD and floating-point. Load 1-32 consecutive 32-bit registers, floating-point only.   |
| Vector Load Register  | VLDR(immediate) VLDR(literal) | Load one 64-bit register, Advanced SIMD and floating-point. Load one 32-bit register, floating-point only.                               |
| Vector Store Multiple | VSTM, VSTMDB, VSTMIA          | Store 1-16 consecutive 64-bit registers, Advanced SIMD and floating-point. Store 1-32 consecutive 32-bit registers, floating-point only. |
| Vector Store Register | VSTR                          | Store one 64-bit register, Advanced SIMD and floating-point. Store one 32-bit register, floating-point only.                             |

## F2.11.1 Element and structure load/store instructions

Table F2-18 shows the element and structure load/store instructions available in the Advanced SIMD instruction set. Loading and storing structures of more than one element automatically de-interleaves or interleaves the elements, see Figure F2-1 for an example of de-interleaving. Interleaving is the inverse process.

Table F2-18 Element and structure load/store instructions

| Instruction              | See                                            |
|--------------------------|------------------------------------------------|
| Load single element      |                                                |
| Multiple elements        | VLD1 (multiple single elements)                |
| To one lane              | VLD1 (single element to one lane)              |
| To all lanes             | VLD1 (single element to all lanes)             |
| Load 2-element structure |                                                |
| Multiple structures      | VLD2 (multiple 2-element structures)           |
| To one lane              | VLD2 (single 2-element structure to one lane)  |
| To all lanes             | VLD2 (single 2-element structure to all lanes) |
| Load 3-element structure |                                                |
| Multiple structures      | VLD3 (multiple 3-element structures)           |
| To one lane              | VLD3 (single 3-element structure to one lane)  |
| To all lanes             | VLD3 (single 3-element structure to all lanes) |

Figure F2-1 shows the de-interleaving of a VLD3.16 (multiple 3-element structures) instruction:

| Instruction               | See                                             |
|---------------------------|-------------------------------------------------|
| Load 4-element structure  |                                                 |
| Multiple structures       | VLD4 (multiple 4-element structures)            |
| To one lane               | VLD4 (single 4-element structure to one lane)   |
| To all lanes              | VLD4 (single 4-element structure to all lanes)  |
| Store single element      |                                                 |
| Multiple elements         | VST1 (multiple single elements)                 |
| From one lane             | VST1 (single element from one lane)             |
| Store 2-element structure |                                                 |
| Multiple structures       | VST2 (multiple 2-element structures)            |
| From one lane             | VST2 (single 2-element structure from one lane) |
| Store 3-element structure |                                                 |
| Multiple structures       | VST3 (multiple 3-element structures)            |
| From one lane             | VST3 (single 3-element structure from one lane) |
| Store 4-element structure |                                                 |
| Multiple structures       | VST4 (multiple 4-element structures)            |
| From one lane             | VST4 (single 4-element structure from one lane) |

Figure F2-1 shows the VLD3.16 instruction operating to three 64-bit registers that comprise four 16-bit elements:

<!-- image -->

- Different instructions in this group would produce similar figures, but operate on different numbers of registers. For example, VLD4 and VST4 instructions operate on four registers.
- Different element sizes would produce similar figures but with 8-bit or 32-bit elements.
- These instructions operate only on doubleword (64-bit) registers.