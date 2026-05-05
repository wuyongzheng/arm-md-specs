## C6.2.101 COSP

Clear other speculative prediction restriction by context

This instruction prevents predictions, other than Cache prefetch, Control flow, and Data Value predictions, that predict execution addresses based on information gathered from earlier execution within a particular execution context. Predictions, other than Cache prefetch, Control flow, and Data Value predictions, determined by the actions of code in the target execution context or contexts appearing in program order before the instruction cannot exploitatively control any speculative access occurring after the instruction is complete and synchronized.

This is an alias of SYS. This means:

- The encodings in this description are named to match the encodings of SYS.
- The description of SYS gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## System

(FEAT\_SPECRES2)

<!-- image -->

## Encoding

<!-- image -->

and is always the preferred disassembly.

## Assembler Symbols

&lt;Xt&gt;

Is the 64-bit name of the general-purpose source register, encoded in the 'Rt' field.

## Operation

The description of SYS gives the operational pseudocode for this instruction.
