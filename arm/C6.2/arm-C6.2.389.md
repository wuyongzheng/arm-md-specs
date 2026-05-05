## C6.2.389 STCLRB, STCLRLB

Atomic bit clear on byte, without return

This instruction atomically loads an 8-bit byte from memory, performs a bitwise AND with the complement of the value held in a register on it, and stores the result back to memory.

- STCLRB does not have release semantics.
- STCLRLB stores to memory with release semantics, as described in Load-Acquire, Store-Release.

For information about addressing modes, see Load/Store addressing modes.

This is an alias of LDCLRB, LDCLRAB, LDCLRALB, LDCLRLB. This means:

- The encodings in this description are named to match the encodings of LDCLRB, LDCLRAB, LDCLRALB, LDCLRLB.
- The description of LDCLRB, LDCLRAB, LDCLRALB, LDCLRLB gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## Integer

(FEAT\_LSE)

<!-- image -->

## Encoding for the No memory ordering variant

```
Applies when (R == 0) STCLRB <Ws>, [<Xn|SP>] is equivalent to LDCLRB <Ws>, <Wt>, [<Xn|SP>]
```

and is always the preferred disassembly.

## Encoding for the Release variant

```
Applies when (R == 1) STCLRLB <Ws>, [<Xn|SP>] is equivalent to LDCLRLB <Ws>, <Wt>, [<Xn|SP>]
```

and is always the preferred disassembly.

## Assembler Symbols

## &lt;Ws&gt;

Is the 32-bit name of the general-purpose register holding the data value to be operated on with the contents of the memory location, encoded in the 'Rs' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## Operation

The description of LDCLRB, LDCLRAB, LDCLRALB, LDCLRLB gives the operational pseudocode for this instruction.

## Operational Information

The description of LDCLRB, LDCLRAB, LDCLRALB, LDCLRLB gives the operational information for this instruction.
