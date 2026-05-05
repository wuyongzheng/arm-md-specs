## C6.2.160 EXTR

## Extract register

This instruction extracts a register from a pair of registers.

This instruction is used by the alias ROR (immediate).

<!-- image -->

## Encoding for the 32-bit variant

Applies when (sf == 0 &amp;&amp; N == 0 &amp;&amp; imms == 0xxxxx)

```
EXTR <Wd>, <Wn>, <Wm>, #<lsb>
```

## Encoding for the 64-bit variant

Applies when (sf == 1 &amp;&amp; N == 1)

```
EXTR <Xd>, <Xn>, <Xm>, #<lsb>
```

## Decode for all variants of this encoding

```
EndOfDecode(Decode_UNDEF);
```

```
if N != sf then EndOfDecode(Decode_UNDEF); if sf == '0' && imms<5> == '1' then constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer datasize = 32 << UInt(sf); constant integer lsb = UInt(imms);
```

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Wn&gt;

Is the 32-bit name of the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Wm&gt;

Is the 32-bit name of the second general-purpose source register, encoded in the 'Rm' field.

## &lt;lsb&gt;

## &lt;Xd&gt;

For the '32-bit' variant: is the least significant bit position from which to extract, in the range 0 to 31, encoded in the 'imms' field.

For the '64-bit' variant: is the least significant bit position from which to extract, in the range 0 to 63, encoded in the 'imms' field.

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Xn&gt;

Is the 64-bit name of the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Xm&gt;

Is the 64-bit name of the second general-purpose source register, encoded in the 'Rm' field.

## Alias Conditions

## Operation

```
bits(datasize) result; constant bits(datasize) operand1 = X[n, datasize]; constant bits(datasize) operand2 = X[m, datasize]; constant bits(2*datasize) concat = operand1:operand2; result = concat<(lsb+datasize)-1:lsb>; X[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

## Alias

ROR (immediate)

## Is preferred when

Rn == Rm
