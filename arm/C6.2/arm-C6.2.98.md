## C6.2.98 CMPP

Compare with tag

This instruction subtracts the 56-bit address held in the second source register from the 56-bit address held in the first source register, updates the condition flags based on the result of the subtraction, and discards the result.

This is an alias of SUBPS. This means:

- The encodings in this description are named to match the encodings of SUBPS.
- The description of SUBPS gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## Integer

(FEAT\_MTE)

<!-- image -->

## Encoding

```
CMPP <Xn|SP>, <Xm|SP>
```

## is equivalent to

```
SUBPS <Xd>, <Xn|SP>, <Xm|SP>
```

and is always the preferred disassembly.

## Assembler Symbols

## &lt;Xn|SP&gt;

Is the 64-bit name of the first source general-purpose register or stack pointer, encoded in the 'Rn' field.

## &lt;Xm|SP&gt;

Is the 64-bit name of the second general-purpose source register or stack pointer, encoded in the 'Rm' field.

## Operation

The description of SUBPS gives the operational pseudocode for this instruction.
