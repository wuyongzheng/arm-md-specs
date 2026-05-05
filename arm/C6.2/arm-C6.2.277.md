## C6.2.277 MOV (to/from SP)

Move register value to or from SP

This instruction copies the value of a register to or from the stack pointer.

This is an alias of ADD (immediate). This means:

- The encodings in this description are named to match the encodings of ADD (immediate).
- The description of ADD (immediate) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding for the 32-bit variant

Applies when (sf ==

```
0) MOV <Wd|WSP>, <Wn|WSP>
```

## is equivalent to

```
ADD <Wd|WSP>, <Wn|WSP>, #0
```

and is the preferred disassembly when Rd == '11111' || Rn == '11111' .

## Encoding for the 64-bit variant

Applies when (sf ==

```
1) MOV <Xd|SP>, <Xn|SP>
```

## is equivalent to

```
ADD <Xd|SP>, <Xn|SP>, #0
```

and is the preferred disassembly when Rd == '11111' || Rn == '11111' .

## Assembler Symbols

## &lt;Wd|WSP&gt;

Is the 32-bit name of the destination general-purpose register or stack pointer, encoded in the 'Rd' field.

## &lt;Wn|WSP&gt;

Is the 32-bit name of the source general-purpose register or stack pointer, encoded in the 'Rn' field.

## &lt;Xd|SP&gt;

Is the 64-bit name of the destination general-purpose register or stack pointer, encoded in the 'Rd' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the source general-purpose register or stack pointer, encoded in the 'Rn' field.

## Operation

The description of ADD (immediate) gives the operational pseudocode for this instruction.

## Operational Information

The description of ADD (immediate) gives the operational information for this instruction.
