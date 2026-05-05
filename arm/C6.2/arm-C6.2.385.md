## C6.2.385 STADD, STADDL

Atomic add on word or doubleword, without return

This instruction atomically loads a 32-bit word or 64-bit doubleword from memory, adds the value held in a register to it, and stores the result back to memory.

- STADD does not have release semantics.
- STADDL stores to memory with release semantics, as described in Load-Acquire, Store-Release.

For information about addressing modes, see Load/Store addressing modes.

This is an alias of LDADD, LDADDA, LDADDAL, LDADDL. This means:

- The encodings in this description are named to match the encodings of LDADD, LDADDA, LDADDAL, LDADDL.
- The description of LDADD, LDADDA, LDADDAL, LDADDL gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## Integer

(FEAT\_LSE)

<!-- image -->

## Encoding for the 32-bit no memory ordering variant

Applies when

(size ==

STADD

&lt;Ws&gt;, [&lt;Xn|SP&gt;]

is equivalent to

LDADD

&lt;Ws&gt;, &lt;Wt&gt;, [&lt;Xn|SP&gt;]

and is always the preferred disassembly.

## Encoding for the 32-bit release variant

Applies when

(size ==

```
STADDL <Ws>, [<Xn|SP>]
```

is equivalent to

```
LDADDL <Ws>, <Wt>, [<Xn|SP>]
```

and is always the preferred disassembly.

## Encoding for the 64-bit no memory ordering variant

Applies when

(size ==

```
STADD <Xs>, [<Xn|SP>]
```

is equivalent to

```
LDADD <Xs>, <Xt>, [<Xn|SP>]
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
Applies when (size == 11 && R == 1) STADDL <Xs>, [<Xn|SP>] is equivalent to LDADDL <Xs>, <Xt>, [<Xn|SP>]
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

The description of LDADD, LDADDA, LDADDAL, LDADDL gives the operational pseudocode for this instruction.

## Operational Information

The description of LDADD, LDADDA, LDADDAL, LDADDL gives the operational information for this instruction.
