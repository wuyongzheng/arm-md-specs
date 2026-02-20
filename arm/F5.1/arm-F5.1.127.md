## F5.1.127 NOP

No Operation does nothing. This instruction can be used for instruction alignment purposes.

Note

The timing effects of including a NOP instruction in a program are not guaranteed. It can increase execution time, leave it unchanged, or even reduce it. Therefore, NOP instructions are not suitable for timing loops.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding

<!-- image -->

## Decode for this encoding

// No additional decoding required

T1

## Encoding

NOP{&lt;c&gt;}{&lt;q&gt;}

## Decode for this encoding

// No additional decoding required

T2

<!-- image -->

## Encoding

NOP{&lt;c&gt;}.W

Listing F5-55

<!-- image -->

Listing F5-56

## Decode for this encoding

```
// No additional decoding required
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

<!-- image -->

See Standard assembler syntax fields.

## Operation

```
EncodingSpecificOperations();
```

```
if ConditionPassed() then // Do nothing end
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

Listing F5-58