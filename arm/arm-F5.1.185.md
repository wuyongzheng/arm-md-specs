## F5.1.185 SEV

Send Event is a hint instruction. It causes an event to be signaled to all PEs in the multiprocessor system. For more information, see Wait For Event and Send Event.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding

SEV{&lt;c&gt;}{&lt;q&gt;}

## Decode for this encoding

// No additional decoding required

T1

## Encoding

SEV{&lt;c&gt;}{&lt;q&gt;}

## Decode for this encoding

// No additional decoding required

T2

<!-- image -->

## Encoding

SEV{&lt;c&gt;}.W

Listing F5-69

<!-- image -->

Listing F5-70

## Decode for this encoding

// No additional decoding required

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

<!-- image -->

See Standard assembler syntax fields.

<!-- image -->

See Standard assembler syntax fields.

## Operation

EncodingSpecificOperations();

if ConditionPassed() then SendEvent();

end

Listing F5-72