## C6.2.64 CBGE (immediate)

Compare signed greater than or equal to immediate and branch

This instruction compares the signed value in a register with an immediate, and conditionally branches to a label at a PC-relative offset if the register value is greater than or equal to the immediate. This instruction provides a hint that this is not a subroutine call or return. This instruction does not affect the condition flags.

This is a pseudo-instruction of CB&lt;cc&gt; (immediate). This means:

- The encodings in this description are named to match the encodings of CB&lt;cc&gt; (immediate).
- The assembler syntax is used only for assembly, and is not used on disassembly.
- The description of CB&lt;cc&gt; (immediate) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## Branch

(FEAT\_CMPBR)

<!-- image -->

## Encoding for the 32-bit greater than variant

Applies when (sf ==

```
<Wt>, #<immp1>, <label> is equivalent to CBGT <Wt>, #<imm>, <label>
```

```
0) CBGE
```

## Encoding for the 64-bit greater than variant

Applies when (sf ==

```
<Xt>, #<immp1>, <label> is equivalent to CBGT <Xt>, #<imm>, <label>
```

```
1) CBGE
```

## Assembler Symbols

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be tested, encoded in the 'Rt' field.

## &lt;immp1&gt;

Is an unsigned immediate, in the range 1 to 64, encoded as 'imm6' plus 1.

## &lt;label&gt;

Is the program label to be conditionally branched to. Its offset from the address of this instruction, in the range -1024 to 1020, is encoded as 'imm9' times 4.

## &lt;Xt&gt;

Is the 64-bit name of the general-purpose register to be tested, encoded in the 'Rt' field.

## Operation

The description of CB&lt;cc&gt; (immediate) gives the operational pseudocode for this instruction.
