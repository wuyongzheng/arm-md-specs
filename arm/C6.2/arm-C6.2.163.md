## C6.2.163 GCSPOPM

## Guarded Control Stack pop

This instruction loads the 64-bit doubleword that is pointed to by the current Guarded Control Stack pointer, writes it to the destination register, and increments the current Guarded Control Stack pointer register by the size of a Guarded Control Stack procedure return record.

This is an alias of SYSL. This means:

- The encodings in this description are named to match the encodings of SYSL.
- The description of SYSL gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## System

(FEAT\_GCS)

<!-- image -->

## Encoding

GCSPOPM

{&lt;Xt&gt;}

## is equivalent to

SYSL

&lt;Xt&gt;, #&lt;op1&gt;, &lt;Cn&gt;, &lt;Cm&gt;, #&lt;op2&gt;

and is always the preferred disassembly.

## Assembler Symbols

<!-- image -->

&lt;Xt&gt;

Is the 64-bit name of the optional general-purpose destination register, encoded in the 'Rt' field. Defaults to XZR if absent.

## Operation

The description of SYSL gives the operational pseudocode for this instruction.
