## C7.2.396 SXTL, SXTL2

Signed extend long

This instruction duplicates each vector element in the lower or upper half of the source SIMD&amp;FP register into a vector, and writes the vector to the destination SIMD&amp;FP register. The destination vector elements are twice as long as the source vector elements. All the values in this instruction are signed integer values.

The SXTL instruction extracts the source vector from the lower half of the source register. The SXTL2 instruction extracts the source vector from the upper half of the source register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

This is an alias of SSHLL, SSHLL2. This means:

- The encodings in this description are named to match the encodings of SSHLL, SSHLL2.
- The description of SSHLL, SSHLL2 gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## Vector

## (FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
SXTL{2} <Vd>.<Ta>, <Vn>.<Tb>
```

## is equivalent to

```
SSHLL{2} <Vd>.<Ta>, <Vn>.<Tb>, #0
```

and is the preferred disassembly when BitCount(immh) == 1 .

## Assembler Symbols

2

Is the second and upper half specifier. If present it causes the operation to be performed on the upper 64 bits of the registers holding the narrower elements, and is encoded in 'Q':

|   Q | 2         |
|-----|-----------|
|   0 | [absent]  |
|   1 | [present] |

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

&lt;Vd&gt;

&lt;Ta&gt;

## &lt;Vn&gt;

## &lt;Tb&gt;

Is an arrangement specifier, encoded in 'immh':

| immh   | <Ta>     |
|--------|----------|
| 0001   | 8H       |
| 001x   | 4S       |
| 01xx   | 2D       |
| 1xxx   | RESERVED |

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

Is an arrangement specifier, encoded in 'immh:Q':

| immh   | Q   | <Tb>     |
|--------|-----|----------|
| 0001   | 0   | 8B       |
| 0001   | 1   | 16B      |
| 001x   | 0   | 4H       |
| 001x   | 1   | 8H       |
| 01xx   | 0   | 2S       |
| 01xx   | 1   | 4S       |
| 1xxx   | x   | RESERVED |

## Operation

The description of SSHLL, SSHLL2 gives the operational pseudocode for this instruction.

## Operational Information

The description of SSHLL, SSHLL2 gives the operational information for this instruction.
