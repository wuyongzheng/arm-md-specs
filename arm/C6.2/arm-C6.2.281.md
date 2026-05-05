## C6.2.281 MOV (register)

Move register value

This instruction copies the value in a source register to the destination register.

This is an alias of ORR (shifted register). This means:

- The encodings in this description are named to match the encodings of ORR (shifted register).
- The description of ORR (shifted register) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding for the 32-bit variant

Applies when (sf ==

```
0) MOV <Wd>, <Wm> is equivalent to ORR <Wd>, WZR, <Wm>
```

and is always the preferred disassembly.

## Encoding for the 64-bit variant

Applies when (sf ==

```
1) MOV <Xd>, <Xm>
```

## is equivalent to

```
ORR <Xd>, XZR, <Xm>
```

and is always the preferred disassembly.

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Wm&gt;

Is the 32-bit name of the general-purpose source register, encoded in the 'Rm' field.

## &lt;Xd&gt;

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Xm&gt;

Is the 64-bit name of the general-purpose source register, encoded in the 'Rm' field.

## Operation

The description of ORR (shifted register) gives the operational pseudocode for this instruction.

## Operational Information

The description of ORR (shifted register) gives the operational information for this instruction.
