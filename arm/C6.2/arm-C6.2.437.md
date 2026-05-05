## C6.2.437 STTSET, STTSETL

Atomic bit set unprivileged, without return

This instruction atomically loads a 32-bit word or 64-bit doubleword from memory, performs a bitwise OR with the value held in a register on it, and stores the result back to memory.

- STTSET does not have release semantics.
- STTSETL stores to memory with release semantics, as described in Load-Acquire, Store-Release.

For information about addressing modes, see Load/Store addressing modes.

This is an alias of LDTSET, LDTSETA, LDTSETAL, LDTSETL. This means:

- The encodings in this description are named to match the encodings of LDTSET, LDTSETA, LDTSETAL, LDTSETL.
- The description of LDTSET, LDTSETA, LDTSETAL, LDTSETL gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## Integer

(FEAT\_LSUI)

<!-- image -->

## Encoding for the 32-bit no memory ordering variant

Applies when

(sz

STTSET

==

0

&lt;Ws&gt;, [&lt;Xn|SP&gt;]

is equivalent to

LDTSET

&lt;Ws&gt;, &lt;Wt&gt;, [&lt;Xn|SP&gt;]

and is always the preferred disassembly.

## Encoding for the 32-bit release variant

```
Applies when (sz == 0 && R == 1) STTSETL <Ws>, [<Xn|SP>]
```

is equivalent to

LDTSETL

&lt;Ws&gt;, &lt;Wt&gt;, [&lt;Xn|SP&gt;]

and is always the preferred disassembly.

## Encoding for the 64-bit no memory ordering variant

```
Applies when (sz == 1 && R == 0) STTSET <Xs>, [<Xn|SP>]
```

is equivalent to

```
LDTSET <Xs>, <Xt>, [<Xn|SP>]
```

and is always the preferred disassembly.

&amp;&amp;

R

==

0)

## Encoding for the 64-bit release variant

```
Applies when (sz == 1 && R == 1) STTSETL <Xs>, [<Xn|SP>] is equivalent to LDTSETL <Xs>, <Xt>, [<Xn|SP>]
```

and is always the preferred disassembly.

## Assembler Symbols

## &lt;Ws&gt;

Is the 32-bit name of the general-purpose register holding the data value to be operated on with the contents of the memory location, encoded in the 'Rs' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;Xs&gt;

Is the 64-bit name of the general-purpose register holding the data value to be operated on with the contents of the memory location, encoded in the 'Rs' field.

## Operation

The description of LDTSET, LDTSETA, LDTSETAL, LDTSETL gives the operational pseudocode for this instruction.

## Operational Information

The description of LDTSET, LDTSETA, LDTSETAL, LDTSETL gives the operational information for this instruction.
