## C6.2.490 UMADDL

Unsigned multiply-add long

This instruction multiplies two 32-bit register values, adds a 64-bit register value, and writes the result to the 64-bit destination register.

This instruction is used by the alias UMULL.

<!-- image -->

## Encoding

UMADDL

&lt;Xd&gt;,

&lt;Wn&gt;, &lt;Wm&gt;, &lt;Xa&gt;

## Decode for this encoding

```
constant integer d = constant integer n = constant integer m = constant integer a =
```

```
UInt(Rd); UInt(Rn); UInt(Rm); UInt(Ra);
```

## Assembler Symbols

## &lt;Xd&gt;

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Wn&gt;

Is the 32-bit name of the first general-purpose source register holding the multiplicand, encoded in the 'Rn' field.

## &lt;Wm&gt;

Is the 32-bit name of the second general-purpose source register holding the multiplier, encoded in the 'Rm' field.

## &lt;Xa&gt;

Is the 64-bit name of the third general-purpose source register holding the addend, encoded in the 'Ra' field.

## Alias Conditions

## Operation

```
constant bits(32) operand1 = X[n, 32]; constant bits(32) operand2 = X[m, 32]; constant bits(64) operand3 = X[a, 64]; constant integer result = UInt(operand3) + (UInt(operand1) * UInt(operand2)); X[d, 64] = result<63:0>;
```

<!-- image -->

| Alias   | Is preferred when   |
|---------|---------------------|
| UMULL   | Ra == '11111'       |

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
