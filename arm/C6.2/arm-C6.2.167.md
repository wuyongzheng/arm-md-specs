## C6.2.167 GCSSS1

Guarded Control Stack switch stack 1

This instruction validates that the stack being switched to contains a Valid cap entry, stores an In-progress cap entry to the stack that is being switched to, and sets the current Guarded control stack pointer to the stack that is being switched to.

If the instruction generates a synchronous Data Abort exception, Watchpoint exception, GPC exception, or GCS Data Check exception, the value of GCSPR\_ELx for the current Exception level is restored to the value held in the register before the instruction was executed.

This is an alias of SYS. This means:

- The encodings in this description are named to match the encodings of SYS.
- The description of SYS gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## System

(FEAT\_GCS)

<!-- image -->

## Encoding

GCSSS1

&lt;Xt&gt;

## is equivalent to

SYS

#3, C7,

C7, #2, &lt;Xt&gt;

and is always the preferred disassembly.

## Assembler Symbols

&lt;Xt&gt;

Is the 64-bit name of the general-purpose source register, encoded in the 'Rt' field.

## Operation

The description of SYS gives the operational pseudocode for this instruction.
