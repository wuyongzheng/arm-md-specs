## C6.2.168 GCSSS2

Guarded Control Stack switch stack 2

This instruction validates that the most recent entry of the Guarded Control Stack being switched to contains an In-progress cap entry, stores a Valid cap entry to the Guarded Control Stack that is being switched from, and sets Xt to the Guarded Control Stack pointer that is being switched from.

This is an alias of SYSL. This means:

- The encodings in this description are named to match the encodings of SYSL.
- The description of SYSL gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## System

(FEAT\_GCS)

<!-- image -->

## Encoding

GCSSS2

&lt;Xt&gt;

## is equivalent to

```
SYSL <Xt>, #<op1>, <Cn>, <Cm>, #<op2>
```

and is always the preferred disassembly.

## Assembler Symbols

<!-- image -->

&lt;Xt&gt;

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rt' field.

## Operation

The description of SYSL gives the operational pseudocode for this instruction.
