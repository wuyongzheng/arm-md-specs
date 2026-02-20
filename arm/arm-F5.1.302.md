## F5.1.302 YIELD

## Yield hint

YIELD is a hint instruction. Software with a multithreading capability can use a YIELD instruction to indicate to the PE that it is performing a task, for example a spin-lock, that could be swapped out to improve overall system performance. The PE can use this hint to suspend and resume multiple software threads if it supports the capability.

For more information about the recommended use of this instruction see The Yield instruction.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding

YIELD{&lt;c&gt;}{&lt;q&gt;}

## Decode for this encoding

// No additional decoding required

T1

## Encoding

YIELD{&lt;c&gt;}{&lt;q&gt;}

## Decode for this encoding

// No additional decoding required

Listing F5-97

<!-- image -->

Listing F5-98

T2

<!-- image -->

## Encoding

YIELD{&lt;c&gt;}.W

## Decode for this encoding

// No additional decoding required

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

<!-- image -->

See Standard assembler syntax fields.

<!-- image -->

See Standard assembler syntax fields.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); Hint_Yield();
```

end

Listing F5-99

Listing F5-100