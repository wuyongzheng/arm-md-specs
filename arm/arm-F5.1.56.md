## F5.1.56 ISB

Instruction Synchronization Barrier flushes the pipeline in the PE and is a context synchronization event. For more information, see Instruction Synchronization Barrier (ISB).

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

ISB{&lt;c&gt;}{&lt;q&gt;} {&lt;option&gt;}

## Decode for this encoding

// No additional decoding required

T1

<!-- image -->

## Encoding

ISB{&lt;c&gt;}{&lt;q&gt;} {&lt;option&gt;}

## Decode for this encoding

// No additional decoding required

For more information about the CONSTRAINED UNPREDICTABLE behavior, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

For the 'A1' variant: see Standard assembler syntax fields. Must be AL or omitted.

For the 'T1' variant: see Standard assembler syntax fields.

See Standard assembler syntax fields.

<!-- image -->

Listing F5-49

Listing F5-50

## &lt;option&gt;

Specifies an optional limitation on the barrier operation. Values are:

SY Full system barrier operation, encoded as option = 0b1111 . Can be omitted.

All other encodings of option are reserved. The corresponding instructions execute as full system barrier operations, but must not be relied upon by software.

## Operation

if ConditionPassed() then EncodingSpecificOperations(); InstructionSynchronizationBarrier();

end

Listing F5-51