## C6.2.420 STSET, STSETL

Atomic bit set on word or doubleword, without return

This instruction atomically loads a 32-bit word or 64-bit doubleword from memory, performs a bitwise OR with the value held in a register on it, and stores the result back to memory.

- STSET does not have release semantics.
- STSETL stores to memory with release semantics, as described in Load-Acquire, Store-Release.

For information about addressing modes, see Load/Store addressing modes.

This is an alias of LDSET, LDSETA, LDSETAL, LDSETL. This means:

- The encodings in this description are named to match the encodings of LDSET, LDSETA, LDSETAL, LDSETL.
- The description of LDSET, LDSETA, LDSETAL, LDSETL gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## Integer

(FEAT\_LSE)

<!-- image -->

## Encoding for the 32-bit no memory ordering variant

Applies when

(size ==

STSET

&lt;Ws&gt;, [&lt;Xn|SP&gt;]

## is equivalent to

```
LDSET <Ws>, <Wt>, [<Xn|SP>]
```

and is always the preferred disassembly.

## Encoding for the 32-bit release variant

```
Applies when (size == 10 && R == 1) STSETL <Ws>, [<Xn|SP>]
```

## is equivalent to

```
LDSETL <Ws>, <Wt>, [<Xn|SP>]
```

and is always the preferred disassembly.

## Encoding for the 64-bit no memory ordering variant

Applies when

(size ==

```
STSET <Xs>, [<Xn|SP>]
```

is equivalent to

```
LDSET <Xs>, <Xt>, [<Xn|SP>]
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

0)

## Encoding for the 64-bit release variant

```
Applies when (size == 11 && R == 1) STSETL <Xs>, [<Xn|SP>] is equivalent to LDSETL <Xs>, <Xt>, [<Xn|SP>]
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

The description of LDSET, LDSETA, LDSETAL, LDSETL gives the operational pseudocode for this instruction.

## Operational Information

The description of LDSET, LDSETA, LDSETAL, LDSETL gives the operational information for this instruction.
