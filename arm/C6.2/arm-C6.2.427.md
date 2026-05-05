## C6.2.427 STSMIN, STSMINL

Atomic signed minimum on word or doubleword, without return

This instruction atomically loads a 32-bit word or 64-bit doubleword from memory, compares it against the value held in a register, and stores the smaller value back to memory, treating the values as signed numbers.

- STSMIN does not have release semantics.
- STSMINL stores to memory with release semantics, as described in Load-Acquire, Store-Release.

For information about addressing modes, see Load/Store addressing modes.

This is an alias of LDSMIN, LDSMINA, LDSMINAL, LDSMINL. This means:

- The encodings in this description are named to match the encodings of LDSMIN, LDSMINA, LDSMINAL, LDSMINL.
- The description of LDSMIN, LDSMINA, LDSMINAL, LDSMINL gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## Integer

(FEAT\_LSE)

<!-- image -->

## Encoding for the 32-bit no memory ordering variant

Applies when

(size ==

STSMIN

&lt;Ws&gt;, [&lt;Xn|SP&gt;]

is equivalent to

```
LDSMIN <Ws>, <Wt>, [<Xn|SP>]
```

and is always the preferred disassembly.

## Encoding for the 32-bit release variant

Applies when

(size ==

STSMINL

10

&lt;Ws&gt;, [&lt;Xn|SP&gt;]

is equivalent to

```
LDSMINL <Ws>, <Wt>, [<Xn|SP>]
```

and is always the preferred disassembly.

## Encoding for the 64-bit no memory ordering variant

Applies when

(size ==

```
STSMIN <Xs>, [<Xn|SP>]
```

is equivalent to

```
LDSMIN <Xs>, <Xt>, [<Xn|SP>]
```

and is always the preferred disassembly.

11

&amp;&amp;

R

==

0)

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
Applies when (size == 11 && R == 1) STSMINL <Xs>, [<Xn|SP>] is equivalent to LDSMINL <Xs>, <Xt>, [<Xn|SP>]
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

The description of LDSMIN, LDSMINA, LDSMINAL, LDSMINL gives the operational pseudocode for this instruction.

## Operational Information

The description of LDSMIN, LDSMINA, LDSMINAL, LDSMINL gives the operational information for this instruction.
