## C6.2.274 MADD

## Multiply-add

This instruction multiplies two register values, adds a third register value, and writes the result to the destination register.

This instruction is used by the alias MUL.

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (sf == 0) MADD <Wd>, <Wn>, <Wm>, <Wa>
```

## Encoding for the 64-bit variant

Applies when

```
(sf == 1) MADD <Xd>, <Xn>, <Xm>, <Xa>
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer a = UInt(Ra); constant integer datasize = 32 << UInt(sf);
```

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Wn&gt;

Is the 32-bit name of the first general-purpose source register holding the multiplicand, encoded in the 'Rn' field.

## &lt;Wm&gt;

Is the 32-bit name of the second general-purpose source register holding the multiplier, encoded in the 'Rm' field.

## &lt;Wa&gt;

Is the 32-bit name of the third general-purpose source register holding the addend, encoded in the 'Ra' field.

## &lt;Xd&gt;

## &lt;Xn&gt;

Is the 64-bit name of the first general-purpose source register holding the multiplicand, encoded in the 'Rn' field.

## &lt;Xm&gt;

Is the 64-bit name of the second general-purpose source register holding the multiplier, encoded in the 'Rm' field.

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

<!-- image -->

Is the 64-bit name of the third general-purpose source register holding the addend, encoded in the 'Ra' field.

## Alias Conditions

## Operation

```
constant bits(datasize) operand1 = X[n, datasize]; constant bits(datasize) operand2 = X[m, datasize]; constant bits(datasize) operand3 = X[a, datasize]; constant integer result = UInt(operand3) + (UInt(operand1) * UInt(operand2)); X[d, datasize] = result<datasize-1:0>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

| Alias   | Is preferred when   |
|---------|---------------------|
| MUL     | Ra == '11111'       |
