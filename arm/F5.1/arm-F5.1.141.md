## F5.1.141 POP (single register)

Pop Single Register from Stack loads a single general-purpose register from the stack, loading from the address in SP, and updates SP to point just above the loaded data.

This is an alias of LDR (immediate). This means:

- The encodings in this description are named to match the encodings of LDR (immediate).
- The description of LDR (immediate) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

It has encodings from the following instruction sets: A32 (A1) and T32 (T4).

A1

<!-- image -->

## Encoding for the Post-indexed variant

```
POP{<c>}{<q>} <single_register_list>
```

is equivalent to

```
LDR{<c>}{<q>} <Rt>, [SP], #4
```

and is always the preferred disassembly.

T4

<!-- image -->

## Encoding for the Post-indexed variant

```
POP{<c>}{<q>} <single_register_list>
```

## is equivalent to

```
LDR{<c>}{<q>} <Rt>, [SP], #4
```

and is always the preferred disassembly.

## Assembler Symbols

<!-- image -->

See Standard assembler syntax fields.

<!-- image -->

See Standard assembler syntax fields.

## &lt;single\_register\_list&gt;

Is the general-purpose register &lt;Rt&gt; to be loaded surrounded by { and }.

## Operation

The description of LDR (immediate) gives the operational pseudocode for this instruction.

## Operational Information

The description of LDR (immediate) gives the operational information for this instruction.