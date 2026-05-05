## C6.2.375 SMSTART

Enables access to Streaming SVE mode and SME architectural state

This instruction enables access to Streaming SVE mode and SME architectural state.

SMSTART enters Streaming SVE mode, and enables the SME ZA storage.

SMSTART SM enters Streaming SVE mode, but does not enable the SME ZA storage.

SMSTART ZA enables the SME ZA storage, but does not cause an entry to Streaming SVE mode.

This is an alias of MSR (immediate). This means:

- The encodings in this description are named to match the encodings of MSR (immediate).
- The description of MSR (immediate) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## System

(FEAT\_SME)

<!-- image -->

## Encoding

| SMSTART          | {<option>}        |
|------------------|-------------------|
| is equivalent to | is equivalent to  |
| MSR              | <pstatefield>, #1 |

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
