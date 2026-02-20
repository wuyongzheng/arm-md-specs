## F5.1.145 PUSH (single register)

Push Single Register to Stack stores a single general-purpose register to the stack, storing to the 32-bit word below the address in SP, and updates SP to point to the start of the stored data.

This is an alias of STR (immediate). This means:

- The encodings in this description are named to match the encodings of STR (immediate).
- The description of STR (immediate) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

It has encodings from the following instruction sets: A32 (A1) and T32 (T4).

A1

<!-- image -->

## Encoding for the Pre-indexed variant

```
PUSH{<c>}{<q>} <single_register_list>
```

is equivalent to

```
STR{<c>}{<q>} <Rt>, [SP, #-4]!
```

and is always the preferred disassembly.

T4

<!-- image -->

## Encoding for the Pre-indexed variant

```
PUSH{<c>}{<q>} <single_register_list> // (Standard syntax)
```

## is equivalent to

```
STR{<c>}{<q>} <Rt>, [SP, #-4]!
```

and is always the preferred disassembly.

## Assembler Symbols

<!-- image -->

See Standard assembler syntax fields.

<!-- image -->

See Standard assembler syntax fields.

## &lt;single\_register\_list&gt;

Is the general-purpose register &lt;Rt&gt; to be stored surrounded by { and }.

## Operation

The description of STR (immediate) gives the operational pseudocode for this instruction.

## Operational Information

The description of STR (immediate) gives the operational information for this instruction.