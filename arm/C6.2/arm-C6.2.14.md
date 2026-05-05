## C6.2.14 AND (immediate)

Bitwise AND (immediate)

This instruction performs a bitwise AND of a register value and an immediate value, and writes the result to the destination register.

<!-- image -->

## Encoding for the 32-bit variant

Applies when (sf == 0 &amp;&amp; N == 0)

```
AND <Wd|WSP>, <Wn>, #<imm>
```

## Encoding for the 64-bit variant

Applies when (sf ==

```
1)
```

```
AND <Xd|SP>, <Xn>, #<imm>
```

## Decode for all variants of this encoding

```
if sf == '0' && N != '0' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer datasize = 32 << UInt(sf); bits(datasize) imm; (imm, -) = DecodeBitMasks(N, imms, immr, TRUE, datasize);
```

## Assembler Symbols

## &lt;Wd|WSP&gt;

Is the 32-bit name of the destination general-purpose register or stack pointer, encoded in the 'Rd' field.

## &lt;Wn&gt;

Is the 32-bit name of the general-purpose source register, encoded in the 'Rn' field.

## &lt;imm&gt;

For the '32-bit' variant: is the bitmask immediate, encoded in 'imms:immr'.

For the '64-bit' variant: is the bitmask immediate, encoded in 'N:imms:immr'.

## &lt;Xd|SP&gt;

Is the 64-bit name of the destination general-purpose register or stack pointer, encoded in the 'Rd' field.

## &lt;Xn&gt;

Is the 64-bit name of the general-purpose source register, encoded in the 'Rn' field.

## Operation

```
constant bits(datasize) operand1 = X[n, datasize]; constant bits(datasize) operand2 = imm; constant bits(datasize) result = operand1 AND if d == 31 then SP[64] = ZeroExtend(result, 64); else X[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
operand2;
```
