## C6.2.90 CLS

Count leading sign bits

This instruction counts the number of leading bits of the source register that have the same value as the most significant bit of the register, and writes the result to the destination register. This count does not include the most significant bit of the source register.

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (sf == 0) CLS <Wd>, <Wn>
```

## Encoding for the 64-bit variant

```
Applies when (sf == 1) CLS <Xd>, <Xn>
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer datasize = 32 <<
```

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Wn&gt;

Is the 32-bit name of the general-purpose source register, encoded in the 'Rn' field.

## &lt;Xd&gt;

<!-- image -->

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
CountLeadingSignBits(operand1);
```
