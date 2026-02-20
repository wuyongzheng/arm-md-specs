## F5.1.43 DBG

## Debug hint

DBG executes as a NOP . Arm deprecates any use of the DBG instruction.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

DBG{&lt;c&gt;}{&lt;q&gt;} #&lt;option&gt;

## Decode for this encoding

// DBG executes as a NOP. The 'option' field is ignored

T1

<!-- image -->

## Encoding

DBG{&lt;c&gt;}{&lt;q&gt;} #&lt;option&gt;

## Decode for this encoding

// DBG executes as a NOP. The 'option' field is ignored

For more information about the CONSTRAINED UNPREDICTABLE behavior, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

<!-- image -->

See Standard assembler syntax fields.

<!-- image -->

See Standard assembler syntax fields.

## &lt;option&gt;

Is a 4-bit unsigned immediate, in the range 0 to 15, encoded in the 'option' field.

## Operation

if ConditionPassed() then

```
EncodingSpecificOperations();
```

hint