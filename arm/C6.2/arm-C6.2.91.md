## C6.2.91 CLZ

## Count leading zeros

This instruction counts the number of consecutive binary zero bits, starting from the most significant bit in the source register, and places the count in the destination register.

<!-- image -->

## Encoding for the 32-bit variant

Applies when (sf ==

```
0) CLZ <Wd>, <Wn>
```

## Encoding for the 64-bit variant

```
Applies when (sf == 1) CLZ <Xd>, <Xn>
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer datasize = 32 <<
```

## Assembler Symbols

&lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Wn&gt;

Is the 32-bit name of the general-purpose source register, encoded in the 'Rn' field.

## &lt;Xd&gt;

## &lt;Xn&gt;

Is the 64-bit name of the general-purpose source register, encoded in the 'Rn' field.

## Operation

```
constant bits(datasize) operand1 = X[n, datasize]; constant integer result = X[d, datasize] = result<datasize-1:0>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
UInt(sf);
```

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

```
CountLeadingZeroBits(operand1);
```
