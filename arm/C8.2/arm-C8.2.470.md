## C8.2.470 MOV (vector, unpredicated)

Move vector register (unpredicated)

This instruction copies the contents of the source vector register to the destination vector register. This instruction is unpredicated.

This is an alias of ORR (vectors, unpredicated). This means:

- The encodings in this description are named to match the encodings of ORR (vectors, unpredicated).
- The description of ORR (vectors, unpredicated) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
MOV <Zd>.D, <Zn>.D
```

## is equivalent to

```
ORR <Zd>.D, <Zn>.D, <Zn>.D
```

and is the preferred disassembly when Zn == Zm .

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

## &lt;Zn&gt;

Is the name of the source scalable vector register, encoded in the 'Zn' field.

## Operation

The description of ORR (vectors, unpredicated) gives the operational pseudocode for this instruction.

## Operational Information

The description of ORR (vectors, unpredicated) gives the operational information for this instruction.