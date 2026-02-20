## F5.1.31 CLREX

Clear-Exclusive clears the local monitor of the executing PE.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

CLREX{&lt;c&gt;}{&lt;q&gt;}

## Decode for this encoding

// No additional decoding required

T1

<!-- image -->

## Encoding

CLREX{&lt;c&gt;}{&lt;q&gt;}

## Decode for this encoding

// No additional decoding required

For more information about the CONSTRAINED UNPREDICTABLE behavior, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

For the 'A1' variant: see Standard assembler syntax fields. Must be AL or omitted.

For the 'T1' variant: see Standard assembler syntax fields.

See Standard assembler syntax fields.

<!-- image -->

Listing F5-13

Listing F5-14

## Operation

if ConditionPassed() then EncodingSpecificOperations(); ClearExclusiveLocal(ProcessorID());

end