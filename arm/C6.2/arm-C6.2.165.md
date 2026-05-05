## C6.2.165 GCSPUSHM

Guarded Control Stack push

This instruction decrements the current Guarded Control Stack pointer register by the size of a Guarded control procedure return record and stores an entry to the Guarded Control Stack.

This is an alias of SYS. This means:

- The encodings in this description are named to match the encodings of SYS.
- The description of SYS gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## System

(FEAT\_GCS)

<!-- image -->

## Encoding

<!-- image -->

and is always the preferred disassembly.

## Assembler Symbols

&lt;Xt&gt;

Is the 64-bit name of the general-purpose source register, encoded in the 'Rt' field.

## Operation

The description of SYS gives the operational pseudocode for this instruction.
