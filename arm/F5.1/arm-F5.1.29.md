## F5.1.29 CBNZ, CBZ

Compare and Branch on Nonzero or Zero

Compare and Branch on Nonzero and Compare and Branch on Zero compare the value in a register with zero, and conditionally branch forward a constant value. They do not affect the condition flags.

| 15   | 12 11   |    | 10   | 9   |   8 |      | 2   | 0   |
|------|---------|----|------|-----|-----|------|-----|-----|
| 1 0  | 1 1 op  |  0 | i    |     |   1 | imm5 |     | Rn  |

Listing F5-8

## Encoding for the CBNZ variant

```
Applies when (op == 1) CBNZ{<q>} <Rn>, <label>
```

## Encoding for the CBZ variant

```
Applies when (op == 0) CBZ{<q>} <Rn>, <label>
```

## Decode for all variants of this encoding

```
= ZeroExtend(i:imm5:'0', 32);
```

```
constant integer n = UInt(Rn); constant bits(32) imm32 constant boolean nonzero = (op == '1'); if InITBlock() then UNPREDICTABLE; end
```

For more information about the CONSTRAINED UNPREDICTABLE behavior, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;q&gt;

See Standard assembler syntax fields.

## &lt;Rn&gt;

Is the general-purpose register to be tested, encoded in the 'Rn' field.

## &lt;label&gt;

Is the program label to be conditionally branched to. Its offset from the PC, a multiple of 2 and in the range 0 to 126, is encoded as 'i:imm5' times 2.

## Operation

```
EncodingSpecificOperations(); if nonzero != IsZero(R[n]) then CBWritePC(PC32 + imm32); end
```

Listing F5-9