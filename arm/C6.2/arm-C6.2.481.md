## C6.2.481 TRCIT

Trace instrumentation

This instruction generates an instrumentation trace packet that contains the value of the provided register.

This is an alias of SYS. This means:

- The encodings in this description are named to match the encodings of SYS.
- The description of SYS gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## System

(FEAT\_ITE)

<!-- image -->

## Encoding

TRCIT

&lt;Xt&gt;

## is equivalent to

<!-- formula-not-decoded -->

and is always the preferred disassembly.

## Assembler Symbols

<!-- image -->

Is the 64-bit name of the general-purpose source register, encoded in the 'Rt' field.

## Operation

The description of SYS gives the operational pseudocode for this instruction.
