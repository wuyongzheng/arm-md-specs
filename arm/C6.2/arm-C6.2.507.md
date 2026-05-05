## C6.2.507 YIELD

## Yield

This instruction is a hint instruction. Software with a multithreading capability can use a YIELD instruction to indicate to the PE that it is performing a task, for example a spin-lock, that could be swapped out to improve overall system performance. The PE can use this hint to suspend and resume multiple software threads if it supports the capability.

For more information about the recommended use of this instruction, see The YIELD instruction.

<!-- image -->

## Encoding

YIELD

## Decode for this encoding

// Empty.

## Operation

Hint\_Yield();

## Chapter C7 A64 Advanced SIMD and Floating-point Descriptions

## Instruction

This chapter describes the A64 Advanced SIMD and floating-point instructions.

It contains the following sections:

- About the A64 Advanced SIMD and floating-point instructions.
- Alphabetical list of A64 Advanced SIMD and floating-point instructions.
