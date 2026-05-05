## C6.2.102 CPP

Cache prefetch prediction restriction by context

This instruction prevents cache allocation predictions that predict execution addresses based on information gathered from earlier execution within a particular execution context. The actions of code in the target execution context or contexts appearing in program order before the instruction cannot exploitatively control cache prefetch predictions occurring after the instruction is complete and synchronized.

For more information, see CPP RCTX, Cache Prefetch Prediction Restriction by Context.

This is an alias of SYS. This means:

- The encodings in this description are named to match the encodings of SYS.
- The description of SYS gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## System

(FEAT\_SPECRES)

<!-- image -->

## Encoding

<!-- image -->

and is always the preferred disassembly.

## Assembler Symbols

<!-- image -->

Is the 64-bit name of the general-purpose source register, encoded in the 'Rt' field.

## Operation

The description of SYS gives the operational pseudocode for this instruction.
