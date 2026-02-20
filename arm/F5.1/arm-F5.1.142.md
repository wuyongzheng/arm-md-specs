## F5.1.142 PSSBB

Physical Speculative Store Bypass Barrier is a memory barrier that prevents speculative loads from bypassing earlier stores to the same physical address under certain conditions. For more information and details of the semantics, see Physical Speculative Store Bypass Barrier (PSSBB).

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

<!-- image -->

## Decode for this encoding

// No additional decoding required

T1

<!-- image -->

## Encoding

PSSBB{&lt;q&gt;}

## Decode for this encoding

if InITBlock() then UNPREDICTABLE;

## Assembler Symbols

<!-- image -->

See Standard assembler syntax fields.

## Operation

EncodingSpecificOperations();

SpeculativeStoreBypassBarrierToPA();