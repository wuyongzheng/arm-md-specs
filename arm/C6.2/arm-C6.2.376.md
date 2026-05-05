## C6.2.376 SMSTOP

Disables access to Streaming SVE mode and SME architectural state

This instruction disables access to Streaming SVE mode and SME architectural state.

SMSTOP exits Streaming SVE mode, and disables the SME ZA storage.

SMSTOP SM exits Streaming SVE mode, but does not disable the SME ZA storage.

SMSTOP ZA disables the SME ZA storage, but does not cause an exit from Streaming SVE mode.

This is an alias of MSR (immediate). This means:

- The encodings in this description are named to match the encodings of MSR (immediate).
- The description of MSR (immediate) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## System

(FEAT\_SME)

<!-- image -->

## Encoding

| SMSTOP           | {<option>}        |
|------------------|-------------------|
| is equivalent to | is equivalent to  |
| MSR              | <pstatefield>, #0 |

and is always the preferred disassembly.

## Assembler Symbols

## &lt;option&gt;

Is an optional mode, encoded in 'CRm&lt;2:1&gt;':

|   CRm<2:1> | <option>   | Description                     |
|------------|------------|---------------------------------|
|         00 | RESERVED   | •                               |
|         01 | SM         | Maps to <pstatefield> SVCRSM.   |
|         10 | ZA         | Maps to <pstatefield> SVCRZA.   |
|         11 | [absent]   | Maps to <pstatefield> SVCRSMZA. |

## Operation

The description of MSR (immediate) gives the operational pseudocode for this instruction.
