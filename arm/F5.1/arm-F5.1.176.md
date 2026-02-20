## F5.1.176 SB

Speculation Barrier is a barrier that controls speculation. For more information and details of the semantics, see Speculation Barrier (SB).

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

(FEAT\_SB)

<!-- image -->

## Encoding

<!-- image -->

## Decode for this encoding

// No additional decoding required

T1

(FEAT\_SB)

<!-- image -->

## Encoding

<!-- image -->

## Decode for this encoding

if InITBlock() then UNPREDICTABLE; end

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

<!-- image -->

See Standard assembler syntax fields.

Listing F5-63

Listing F5-64

## Operation

if ConditionPassed() then EncodingSpecificOperations(); SpeculationBarrier();

end