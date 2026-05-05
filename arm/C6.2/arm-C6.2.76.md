## C6.2.76 CBLT (register)

Compare signed less than register and branch

This instruction compares the signed values in two registers, and conditionally branches to a label at a PC-relative offset if the second value is less than the first. This instruction provides a hint that this is not a subroutine call or return. This instruction does not affect the condition flags.

This is a pseudo-instruction of CB&lt;cc&gt; (register). This means:

- The encodings in this description are named to match the encodings of CB&lt;cc&gt; (register).
- The assembler syntax is used only for assembly, and is not used on disassembly.
- The description of CB&lt;cc&gt; (register) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## Branch

(FEAT\_CMPBR)

<!-- image -->

## Encoding for the 32-bit greater than variant

Applies when (sf ==

```
0) CBLT <Wm>, <Wt>, <label>
```

## is equivalent to

```
CBGT <Wt>, <Wm>, <label>
```

## Encoding for the 64-bit greater than variant

Applies when (sf ==

```
1) CBLT <Xm>, <Xt>, <label>
```

## is equivalent to

```
CBGT <Xt>, <Xm>, <label>
```

## Assembler Symbols

## &lt;Wm&gt;

Is the 32-bit name of the second general-purpose source register, encoded in the 'Rm' field.

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be tested, encoded in the 'Rt' field.

## &lt;label&gt;

Is the program label to be conditionally branched to. Its offset from the address of this instruction, in the range -1024 to 1020, is encoded as 'imm9' times 4.

## &lt;Xm&gt;

Is the 64-bit name of the second general-purpose source register, encoded in the 'Rm' field.

<!-- image -->

Is the 64-bit name of the general-purpose register to be tested, encoded in the 'Rt' field.

## Operation

The description of CB&lt;cc&gt; (register) gives the operational pseudocode for this instruction.
