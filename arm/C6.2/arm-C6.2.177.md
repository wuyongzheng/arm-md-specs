## C6.2.177 ISB

Instruction synchronization barrier

This instruction flushes the pipeline in the PE and is a context synchronization event. For more information, see Instruction Synchronization Barrier (ISB).

<!-- image -->

## Encoding

ISB {&lt;option&gt;|#&lt;imm&gt;}

## Decode for this encoding

// no additional decoding required

## Assembler Symbols

## &lt;option&gt;

Specifies an optional limitation on the barrier operation. Values are:

SY Full system barrier operation, encoded as CRm = 0b1111 . Can be omitted.

All other encodings of 'CRm' are reserved. The corresponding instructions execute as full system barrier operations, but must not be relied upon by software.

## &lt;imm&gt;

Is an optional 4-bit unsigned immediate, in the range 0 to 15, defaulting to 15 and encoded in the 'CRm' field.

## Operation

```
InstructionSynchronizationBarrier(); if IsFeatureImplemented(FEAT_BRBE) && BRBEBranchOnISB() then BRBEISB();
```
