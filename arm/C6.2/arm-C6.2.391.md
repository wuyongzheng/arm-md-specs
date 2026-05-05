## C6.2.391 STEOR, STEORL

Atomic exclusive-OR on word or doubleword, without return

This instruction atomically loads a 32-bit word or 64-bit doubleword from memory, performs an exclusive-OR with the value held in a register on it, and stores the result back to memory.

- STEOR does not have release semantics.
- STEORL stores to memory with release semantics, as described in Load-Acquire, Store-Release.

For information about addressing modes, see Load/Store addressing modes.

This is an alias of LDEOR, LDEORA, LDEORAL, LDEORL. This means:

- The encodings in this description are named to match the encodings of LDEOR, LDEORA, LDEORAL, LDEORL.
- The description of LDEOR, LDEORA, LDEORAL, LDEORL gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## Integer

(FEAT\_LSE)

<!-- image -->

## Encoding for the 32-bit no memory ordering variant

Applies when

(size ==

STEOR

&lt;Ws&gt;, [&lt;Xn|SP&gt;]

is equivalent to

```
LDEOR <Ws>, <Wt>, [<Xn|SP>]
```

and is always the preferred disassembly.

## Encoding for the 32-bit release variant

Applies when

(size ==

```
STEORL <Ws>, [<Xn|SP>]
```

is equivalent to

```
LDEORL <Ws>, <Wt>, [<Xn|SP>]
```

and is always the preferred disassembly.

## Encoding for the 64-bit no memory ordering variant

Applies when

(size ==

```
STEOR <Xs>, [<Xn|SP>]
```

is equivalent to

```
LDEOR <Xs>, <Xt>, [<Xn|SP>]
```

and is always the preferred disassembly.

11

&amp;&amp;

R

==

0)

10

&amp;&amp;

R

==

1)

10

&amp;&amp;

R

==

0)

## Encoding for the 64-bit release variant

```
Applies when (size == 11 && R == 1) STEORL <Xs>, [<Xn|SP>] is equivalent to LDEORL <Xs>, <Xt>, [<Xn|SP>]
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

The description of LDEOR, LDEORA, LDEORAL, LDEORL gives the operational pseudocode for this instruction.

## Operational Information

The description of LDEOR, LDEORA, LDEORAL, LDEORL gives the operational information for this instruction.
