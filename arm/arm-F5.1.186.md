## F5.1.186 SEVL

Send Event Local is a hint instruction that causes an event to be signaled locally without requiring the event to be signaled to other PEs in the multiprocessor system. It can prime a wait-loop which starts with a WFE instruction.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding

SEVL{&lt;c&gt;}{&lt;q&gt;}

## Decode for this encoding

// No additional decoding required

T1

## Encoding

SEVL{&lt;c&gt;}{&lt;q&gt;}

## Decode for this encoding

// No additional decoding required

T2

<!-- image -->

## Encoding

SEVL{&lt;c&gt;}.W

Listing F5-73

<!-- image -->

Listing F5-74

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
if ConditionPassed() then EncodingSpecificOperations(); SendEventLocal(); end
```

Listing F5-76