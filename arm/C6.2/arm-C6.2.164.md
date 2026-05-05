## C6.2.164 GCSPOPX

Guarded Control Stack pop exception return record

This instruction loads an exception return record from the location indicated by the current Guarded Control Stack pointer register, checks that the record is an exception return record, and increments the pointer by the size of a Guarded Control Stack exception return record.

This is an alias of SYS. This means:

- The encodings in this description are named to match the encodings of SYS.
- The description of SYS gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## System

(FEAT\_GCS)

<!-- image -->

| Encoding                               |
|----------------------------------------|
| GCSPOPX                                |
| is equivalent to                       |
| SYS #<op1>, <Cn>, <Cm>, #<op2>{, <Xt>} |

and is always the preferred disassembly.

## Operation

The description of SYS gives the operational pseudocode for this instruction.
