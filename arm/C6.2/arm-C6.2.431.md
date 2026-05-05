## C6.2.431 STTCLR, STTCLRL

Atomic bit clear unprivileged, without return

This instruction atomically loads a 32-bit word or 64-bit doubleword from memory, performs a bitwise AND with the complement of the value held in a register on it, and stores the result back to memory.

- STTCLR does not have release semantics.
- STTCLRL stores to memory with release semantics, as described in Load-Acquire, Store-Release.

For information about addressing modes, see Load/Store addressing modes.

This is an alias of LDTCLR, LDTCLRA, LDTCLRAL, LDTCLRL. This means:

- The encodings in this description are named to match the encodings of LDTCLR, LDTCLRA, LDTCLRAL, LDTCLRL.
- The description of LDTCLR, LDTCLRA, LDTCLRAL, LDTCLRL gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## Integer

(FEAT\_LSUI)

<!-- image -->

## Encoding for the 32-bit no memory ordering variant

Applies when

(sz

STTCLR

==

0

&lt;Ws&gt;, [&lt;Xn|SP&gt;]

is equivalent to

LDTCLR

&lt;Ws&gt;, &lt;Wt&gt;, [&lt;Xn|SP&gt;]

and is always the preferred disassembly.

## Encoding for the 32-bit release variant

```
Applies when (sz == 0 && R == 1) STTCLRL <Ws>, [<Xn|SP>]
```

is equivalent to

```
LDTCLRL <Ws>, <Wt>, [<Xn|SP>]
```

and is always the preferred disassembly.

## Encoding for the 64-bit no memory ordering variant

```
Applies when (sz == 1 && R == 0) STTCLR <Xs>, [<Xn|SP>]
```

is equivalent to

```
LDTCLR <Xs>, <Xt>, [<Xn|SP>]
```

and is always the preferred disassembly.

&amp;&amp;

R

==

0)

## Encoding for the 64-bit release variant

```
Applies when (sz == 1 && R == 1) STTCLRL <Xs>, [<Xn|SP>] is equivalent to LDTCLRL <Xs>, <Xt>, [<Xn|SP>]
```

and is always the preferred disassembly.

## Assembler Symbols

## &lt;Ws&gt;

Is the 32-bit name of the general-purpose register holding the data value to be operated on with the contents of the memory location, encoded in the 'Rs' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

<!-- image -->

Is the 64-bit name of the general-purpose register holding the data value to be operated on with the contents of the memory location, encoded in the 'Rs' field.

## Operation

The description of LDTCLR, LDTCLRA, LDTCLRAL, LDTCLRL gives the operational pseudocode for this instruction.

## Operational Information

The description of LDTCLR, LDTCLRA, LDTCLRAL, LDTCLRL gives the operational information for this instruction.
