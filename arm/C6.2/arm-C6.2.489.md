## C6.2.489 UDIV

## Unsigned divide

This instruction divides the first unsigned source register value by the second unsigned source register value, and writes the result to the destination register. Dividing by zero writes the value zero to the destination register. The condition flags are not affected.

<!-- image -->

## Encoding for the 32-bit variant

0)

```
Applies when (sf == UDIV <Wd>, <Wn>, <Wm>
```

## Encoding for the 64-bit variant

```
1)
```

```
Applies when (sf == UDIV <Xd>, <Xn>, <Xm>
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
constant bits(datasize) operand1 = constant bits(datasize) operand2 = constant integer dividend = UInt(operand1); constant integer divisor = UInt(operand2); integer result; if divisor == 0 then result = 0; else result = dividend DIV divisor; X[d, datasize] = result<datasize-1:0>;
```

```
X[n, datasize]; X[m, datasize];
```
