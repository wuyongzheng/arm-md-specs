## C6.2.89 CLREX

## Clear exclusive

This instruction clears the local monitor of the executing PE.

<!-- image -->

## Encoding

<!-- image -->

## Decode for this encoding

// CRm field

is ignored

## Assembler Symbols

&lt;imm&gt;

Is an optional 4-bit unsigned immediate, in the range 0 to 15, defaulting to 15 and encoded in the 'CRm' field.

## Operation

ClearExclusiveLocal(ProcessorID());
