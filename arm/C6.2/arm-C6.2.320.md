## C6.2.320 RBIT

## Reverse bits

This instruction reverses the bit order in a register.

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (sf == 0) RBIT <Wd>, <Wn>
```

## Encoding for the 64-bit variant

```
Applies when (sf == 1) RBIT <Xd>, <Xn>
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

## &lt;Xn&gt;

Is the 64-bit name of the general-purpose source register, encoded in the 'Rn' field.

## Operation

```
constant bits(datasize) operand = bits(datasize) result; for i = 0 to datasize-1 result<(datasize-1)-i> = operand<i>; X[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
UInt(sf);
```

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

```
X[n, datasize];
```
