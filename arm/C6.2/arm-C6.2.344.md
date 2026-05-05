## C6.2.344 REV64

## Reverse bytes

This instruction reverses the byte order in a 64-bit general-purpose register.

When assembling for Armv8.2, an assembler must support this pseudo-instruction. It is OPTIONAL whether an assembler supports this pseudo-instruction when assembling for an architecture earlier than Armv8.2.

This is a pseudo-instruction of REV. This means:

- The encodings in this description are named to match the encodings of REV.
- The assembler syntax is used only for assembly, and is not used on disassembly.
- The description of REV gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding

REV64

&lt;Xd&gt;,

&lt;Xn&gt;

## is equivalent to

REV

&lt;Xd&gt;, &lt;Xn&gt;

## Assembler Symbols

## &lt;Xd&gt;

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Xn&gt;

Is the 64-bit name of the general-purpose source register, encoded in the 'Rn' field.

## Operation

The description of REV gives the operational pseudocode for this instruction.

## Operational Information

The description of REV gives the operational information for this instruction.
