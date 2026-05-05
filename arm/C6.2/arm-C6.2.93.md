## C6.2.93 CMN (immediate)

Compare negative (immediate)

This instruction adds a register value and an optionally-shifted immediate value. It updates the condition flags based on the result, and discards the result.

This is an alias of ADDS (immediate). This means:

- The encodings in this description are named to match the encodings of ADDS (immediate).
- The description of ADDS (immediate) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding for the 32-bit variant

Applies when (sf ==

```
0)
```

```
CMN <Wn|WSP>, #<imm>{, <shift>} is equivalent to ADDS WZR, <Wn|WSP>, #<imm>{, <shift>}
```

and is always the preferred disassembly.

## Encoding for the 64-bit variant

```
Applies when (sf == 1) CMN <Xn|SP>, #<imm>{, <shift>} is equivalent to ADDS XZR, <Xn|SP>, #<imm>{, <shift>}
```

and is always the preferred disassembly.

## Assembler Symbols

## &lt;Wn|WSP&gt;

Is the 32-bit name of the source general-purpose register or stack pointer, encoded in the 'Rn' field.

## &lt;imm&gt;

Is an unsigned immediate, in the range 0 to 4095, encoded in the 'imm12' field.

## &lt;shift&gt;

Is the optional left shift to apply to the immediate, defaulting to LSL #0 and encoded in 'sh':

## &lt;Xn|SP&gt;

Is the 64-bit name of the source general-purpose register or stack pointer, encoded in the 'Rn' field.

## Operation

The description of ADDS (immediate) gives the operational pseudocode for this instruction.

## Operational Information

The description of ADDS (immediate) gives the operational information for this instruction.

|   sh | <shift>   |
|------|-----------|
|    0 | LSL #0    |
|    1 | LSL #12   |
