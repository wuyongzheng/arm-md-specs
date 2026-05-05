## C6.2.162 GCSPOPCX

Guarded Control Stack pop and compare exception return record

This instruction loads an exception return record from the location indicated by the current Guarded control stack pointer register, compares the loaded values with the current ELR\_ELx, SPSR\_ELx, and LR, and increments the pointer by the size of a Guarded Control Stack exception return record.

This is an alias of SYS. This means:

- The encodings in this description are named to match the encodings of SYS.
- The description of SYS gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## System

(FEAT\_GCS)

<!-- image -->

## Encoding

GCSPOPCX

## is equivalent to

SYS

#&lt;op1&gt;, &lt;Cn&gt;, &lt;Cm&gt;, #&lt;op2&gt;{, &lt;Xt&gt;}

and is always the preferred disassembly.

## Operation

The description of SYS gives the operational pseudocode for this instruction.
