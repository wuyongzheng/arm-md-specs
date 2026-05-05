## C6.2.378 SMULH

Signed multiply high

This instruction multiplies two 64-bit register values, and writes bits[127:64] of the 128-bit result to the 64-bit destination register.

<!-- image -->

## Encoding

```
SMULH <Xd>, <Xn>, <Xm>
```

## Decode for this encoding

```
constant integer d = constant integer n = constant integer m =
```

```
UInt(Rd); UInt(Rn); UInt(Rm);
```

## Assembler Symbols

&lt;Xd&gt;

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

&lt;Xn&gt;

Is the 64-bit name of the first general-purpose source register holding the multiplicand, encoded in the 'Rn' field.

<!-- image -->

&lt;Xm&gt;

Is the 64-bit name of the second general-purpose source register holding the multiplier, encoded in the 'Rm' field.

## Operation

```
constant bits(64) operand1 = X[n, 64]; constant bits(64) operand2 = X[m, 64]; constant integer result = SInt(operand1) * X[d, 64] = result<127:64>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
SInt(operand2);
```
