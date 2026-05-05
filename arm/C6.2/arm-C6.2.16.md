## C6.2.16 ANDS (immediate)

Bitwise AND (immediate), setting flags

This instruction performs a bitwise AND of a register value and an immediate value, and writes the result to the destination register. It updates the condition flags based on the result.

This instruction is used by the alias TST (immediate).

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (sf == 0 && N ==
```

```
ANDS
```

```
0) <Wd>, <Wn>, #<imm>
```

## Encoding for the 64-bit variant

Applies when (sf ==

```
1)
```

```
ANDS <Xd>, <Xn>, #<imm>
```

## Decode for all variants of this encoding

```
if sf == '0' && N != '0' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer datasize = 32 << UInt(sf); bits(datasize) imm; (imm, -) = DecodeBitMasks(N, imms, immr, TRUE, datasize);
```

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Wn&gt;

Is the 32-bit name of the general-purpose source register, encoded in the 'Rn' field.

## &lt;imm&gt;

For the '32-bit' variant: is the bitmask immediate, encoded in 'imms:immr'.

For the '64-bit' variant: is the bitmask immediate, encoded in 'N:imms:immr'.

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

Is the 64-bit name of the general-purpose source register, encoded in the 'Rn' field.

## &lt;Xd&gt;

## &lt;Xn&gt;

## Alias Conditions

## Operation

```
constant bits(datasize) operand1 = X[n, datasize]; constant bits(datasize) operand2 = imm; constant bits(datasize) result = operand1 AND operand2; X[d, datasize] = result; PSTATE.<N,Z,C,V> = result<datasize-1>:IsZeroBit(result):'00';
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

## Alias

TST (immediate)

## Is preferred when

Rd

==

'11111'
