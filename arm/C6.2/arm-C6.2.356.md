## C6.2.356 SDIV

## Signed divide

This instruction divides the first signed source register value by the second signed source register value, and writes the result to the destination register. Dividing by zero writes the value zero to the destination register. The condition flags are not affected.

<!-- image -->

## Encoding for the 32-bit variant

0)

```
Applies when (sf == SDIV <Wd>, <Wn>, <Wm>
```

## Encoding for the 64-bit variant

```
1)
```

```
Applies when (sf == SDIV <Xd>, <Xn>, <Xm>
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer datasize = 32 <<
```

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Wn&gt;

Is the 32-bit name of the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Wm&gt;

Is the 32-bit name of the second general-purpose source register, encoded in the 'Rm' field.

## &lt;Xd&gt;

## &lt;Xn&gt;

Is the 64-bit name of the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Xm&gt;

Is the 64-bit name of the second general-purpose source register, encoded in the 'Rm' field.

```
UInt(sf);
```

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## Operation

```
constant bits(datasize) operand1 = X[n, datasize]; constant bits(datasize) operand2 = X[m, datasize]; constant integer dividend = SInt(operand1); constant integer divisor = SInt(operand2); integer result; if divisor == 0 then result = 0; elsif (dividend < 0) == (divisor < 0) then result = Abs(dividend) DIV Abs(divisor); // same signs - positive result else result = -(Abs(dividend) DIV Abs(divisor)); // different signs - negative X[d, datasize] = result<datasize-1:0>;
```

```
result
```
