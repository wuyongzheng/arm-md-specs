## C7.2.246 MOV (to general)

Move vector element to general-purpose register

This instruction reads the unsigned integer from the source SIMD&amp;FP register, zero-extends it to form a 32-bit or 64-bit value, and writes the result to the destination general-purpose register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

This is an alias of UMOV. This means:

- The encodings in this description are named to match the encodings of UMOV.
- The description of UMOV gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## Advanced SIMD

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding for the 32-bit variant

Applies when (Q == 0 &amp;&amp; imm5 == xx100)

```
MOV
```

```
<Wd>, <Vn>.S[<index>]
```

## is equivalent to

```
UMOV <Wd>, <Vn>.S[<index>]
```

and is always the preferred disassembly.

## Encoding for the 64-bit variant

```
Applies when (Q == 1 && imm5 == x1000) MOV <Xd>, <Vn>.D[<index>]
```

## is equivalent to

```
UMOV <Xd>, <Vn>.D[<index>]
```

and is always the preferred disassembly.

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Vn&gt;

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;index&gt;

For the '32-bit' variant: is the element index encoded in 'imm5&lt;4:3&gt;'.

For the '64-bit' variant: is the element index encoded in 'imm5&lt;4&gt;'.

<!-- image -->

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## Operation

The description of UMOV gives the operational pseudocode for this instruction.

## Operational Information

The description of UMOV gives the operational information for this instruction.
