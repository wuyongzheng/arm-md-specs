## C6.2.280 MOV (bitmask immediate)

Move bitmask immediate value

This instruction writes a bitmask immediate value to a register.

This is an alias of ORR (immediate). This means:

- The encodings in this description are named to match the encodings of ORR (immediate).
- The description of ORR (immediate) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (sf == 0 && N == 0) MOV <Wd|WSP>, #<imm>
```

## is equivalent to

```
ORR <Wd|WSP>, WZR, #<imm>
```

and is the preferred disassembly when !MoveWidePreferred(sf, N, imms, immr) .

## Encoding for the 64-bit variant

```
Applies when (sf == 1) MOV <Xd|SP>, #<imm>
```

## is equivalent to

```
ORR <Xd|SP>, XZR, #<imm>
```

and is the preferred disassembly when !MoveWidePreferred(sf, N, imms, immr) .

## Assembler Symbols

## &lt;Wd|WSP&gt;

Is the 32-bit name of the destination general-purpose register or stack pointer, encoded in the 'Rd' field.

## &lt;imm&gt;

For the '32-bit' variant: is the bitmask immediate, encoded in 'imms:immr', but excluding values which could be encoded by MOVZ or MOVN.

For the '64-bit' variant: is the bitmask immediate, encoded in 'N:imms:immr', but excluding values which could be encoded by MOVZ or MOVN.

## &lt;Xd|SP&gt;

Is the 64-bit name of the destination general-purpose register or stack pointer, encoded in the 'Rd' field.

## Operation

The description of ORR (immediate) gives the operational pseudocode for this instruction.

## Operational Information

The description of ORR (immediate) gives the operational information for this instruction.
