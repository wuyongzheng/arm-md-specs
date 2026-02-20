## F5.1.42 CSDB

Consumption of Speculative Data Barrier is a memory barrier that controls speculative execution arising from data value prediction. For more information and details of the semantics, see Consumption of Speculative Data Barrier (CSDB).

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

CSDB{&lt;c&gt;}{&lt;q&gt;}

## Decode for this encoding

if cond != '1110' then UNPREDICTABLE; end

// CSDB must be encoded with AL condition

## CONSTRAINED UNPREDICTABLE behavior

If cond != '1110' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes unconditionally.
- The instruction executes conditionally.

T1

<!-- image -->

## Encoding

CSDB{&lt;c&gt;}{&lt;q&gt;}

## Decode for this encoding

if InITBlock() then UNPREDICTABLE; end

Listing F5-22

Listing F5-23

## CONSTRAINED UNPREDICTABLE behavior

If InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes unconditionally.
- The instruction executes conditionally.

For more information about the CONSTRAINED UNPREDICTABLE behavior, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

<!-- image -->

&lt;c&gt;

See Standard assembler syntax fields.

<!-- image -->

See Standard assembler syntax fields.

## Operation

if ConditionPassed() then

EncodingSpecificOperations();

ConsumptionOfSpeculativeDataBarrier();

end

Listing F5-24