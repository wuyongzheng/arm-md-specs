## C6.2.421 STSETB, STSETLB

Atomic bit set on byte, without return

This instruction atomically loads an 8-bit byte from memory, performs a bitwise OR with the value held in a register on it, and stores the result back to memory.

- STSETB does not have release semantics.
- STSETLB stores to memory with release semantics, as described in Load-Acquire, Store-Release.

For information about addressing modes, see Load/Store addressing modes.

This is an alias of LDSETB, LDSETAB, LDSETALB, LDSETLB. This means:

- The encodings in this description are named to match the encodings of LDSETB, LDSETAB, LDSETALB, LDSETLB.
- The description of LDSETB, LDSETAB, LDSETALB, LDSETLB gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## Integer

(FEAT\_LSE)

<!-- image -->

## Encoding for the No memory ordering variant

```
Applies when (R == 0) STSETB <Ws>, [<Xn|SP>] is equivalent to LDSETB <Ws>, <Wt>, [<Xn|SP>]
```

and is always the preferred disassembly.

## Encoding for the Release variant

```
Applies when (R == 1) STSETLB <Ws>, [<Xn|SP>] is equivalent to LDSETLB <Ws>, <Wt>, [<Xn|SP>]
```

and is always the preferred disassembly.

## Assembler Symbols

## &lt;Ws&gt;

Is the 32-bit name of the general-purpose register holding the data value to be operated on with the contents of the memory location, encoded in the 'Rs' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## Operation

The description of LDSETB, LDSETAB, LDSETALB, LDSETLB gives the operational pseudocode for this instruction.

## Operational Information

The description of LDSETB, LDSETAB, LDSETALB, LDSETLB gives the operational information for this instruction.
