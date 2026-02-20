## F5.1.30 CLRBHB

Clear Branch History clears the branch history for the current context to the extent that branch history information created before the CLRBHB instruction cannot be used by code before the CLRBHB instruction to exploitatively control the execution of any indirect branches in code in the current context that appear in program order after the instruction.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

## A1

(FEAT\_CLRBHB)

<!-- image -->

## Encoding

CLRBHB{&lt;c&gt;}{&lt;q&gt;}

## Decode for this encoding

if !IsFeatureImplemented(FEAT\_CLRBHB) then ExecuteAsNOP(); end

T1

(FEAT\_CLRBHB)

<!-- image -->

## Encoding

CLRBHB{&lt;c&gt;}{&lt;q&gt;}

## Decode for this encoding

if !IsFeatureImplemented(FEAT\_CLRBHB) then ExecuteAsNOP(); end

## Assembler Symbols

<!-- image -->

See Standard assembler syntax fields.

See Standard assembler syntax fields.

<!-- image -->

Listing F5-10

Listing F5-11

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); Hint_CLRBHB(); end
```