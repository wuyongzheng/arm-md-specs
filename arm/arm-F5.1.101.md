## F5.1.101 LSL (register)

Logical Shift Left (register) shifts a register value left by a variable number of bits, shifting in zeros, and writes the result to the destination register. The variable number of bits is read from the bottom byte of a register.

This is an alias of MOV , MOVS (register-shifted register). This means:

- The encodings in this description are named to match the encodings of MOV , MOVS (register-shifted register).
- The description of MOV, MOVS (register-shifted register) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding for the Not flag setting variant

```
LSL{<c>}{<q>} {<Rd>, }<Rm>, <Rs>
```

## is equivalent to

```
MOV{<c>}{<q>} <Rd>, <Rm>, LSL <Rs>
```

and is always the preferred disassembly.

T1

## Encoding for the Logical shift left variant

```
LSL<c>{<q>} {<Rdm>, }<Rdm>, <Rs>
```

is equivalent to

```
MOV<c>{<q>} <Rdm>, <Rdm>, LSL <Rs>
```

and is the preferred disassembly when InITBlock() .

T2

<!-- image -->

<!-- image -->

## Encoding for the Not flag setting variant

```
LSL{<c>}{<q>} {<Rd>, }<Rm>, <Rs>
```

```
LSL<c>.W {<Rd>, }<Rm>, <Rs> // (InITBlock() && (UInt(Rd) < 8 && Rd == Rm && UInt(Rs) < 8))
```

## is equivalent to

```
MOV{<c>}{<q>} <Rd>, <Rm>, LSL <Rs>
```

and is always the preferred disassembly.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

&lt;q&gt;

## &lt;Rd&gt;

Is the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Rm&gt;

Is the first general-purpose source register, encoded in the 'Rm' field.

## &lt;Rs&gt;

Is the second general-purpose source register holding a shift amount in its bottom 8 bits, encoded in the 'Rs' field.

## &lt;Rdm&gt;

Is the first general-purpose source register and the destination register, encoded in the 'Rdm' field.

## Operation

The description of MOV, MOVS (register-shifted register) gives the operational pseudocode for this instruction.

## Operational Information

The description of MOV, MOVS (register-shifted register) gives the operational information for this instruction.