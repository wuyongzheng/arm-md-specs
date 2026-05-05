## C7.2.245 MOV (vector)

Move vector

This instruction copies the vector in the source SIMD&amp;FP register into the destination SIMD&amp;FP register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

This is an alias of ORR (vector, register). This means:

- The encodings in this description are named to match the encodings of ORR (vector, register).
- The description of ORR (vector, register) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## Three registers of the same type

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
MOV <Vd>.<T>, <Vn>.<T>
```

## is equivalent to

```
ORR <Vd>.<T>, <Vn>.<T>, <Vn>.<T>
```

and is the preferred disassembly when Rm == Rn .

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'Q':

&lt;T&gt;

## &lt;Vn&gt;

|   Q | <T>   |
|-----|-------|
|   0 | 8B    |
|   1 | 16B   |

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

The description of ORR (vector, register) gives the operational pseudocode for this instruction.

## Operational Information

The description of ORR (vector, register) gives the operational information for this instruction.
