## F5.1.214 SSBB

Speculative Store Bypass Barrier is a memory barrier that prevents speculative loads from bypassing earlier stores to the same virtual address under certain conditions. For more information and details of the semantics, see Speculative Store Bypass Barrier (SSBB).

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

SSBB{&lt;q&gt;}

## Decode for this encoding

// No additional decoding required

T1

<!-- image -->

## Encoding

SSBB{&lt;q&gt;}

## Decode for this encoding

if InITBlock() then UNPREDICTABLE;

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

<!-- image -->

See Standard assembler syntax fields.

## Operation

EncodingSpecificOperations();

SpeculativeStoreBypassBarrierToVA();