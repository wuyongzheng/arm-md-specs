## C6.2.5 ADD (immediate)

Add immediate value

This instruction adds a register value and an optionally-shifted immediate value, and writes the result to the destination register.

This instruction is used by the alias MOV (to/from SP).

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (sf == 0)
```

```
ADD
```

```
<Wd|WSP>, <Wn|WSP>, #<imm>{, <shift>}
```

## Encoding for the 64-bit variant

Applies when (sf ==

```
ADD <Xd|SP>, <Xn|SP>, #<imm>{,
```

```
1) <shift>}
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer datasize = 32 << UInt(sf); constant bits(24) imm = if sh == '0' then Zeros(12):imm12
```

## Assembler Symbols

## &lt;Wd|WSP&gt;

Is the 32-bit name of the destination general-purpose register or stack pointer, encoded in the 'Rd' field.

## &lt;Wn|WSP&gt;

Is the 32-bit name of the source general-purpose register or stack pointer, encoded in the 'Rn' field.

## &lt;imm&gt;

Is an unsigned immediate, in the range 0 to 4095, encoded in the 'imm12' field.

## &lt;shift&gt;

Is the optional left shift to apply to the immediate, defaulting to LSL #0 and encoded in 'sh':

|   sh | <shift>   |
|------|-----------|
|    0 | LSL #0    |
|    1 | LSL #12   |

```
else imm12:Zeros(12);
```

## &lt;Xd|SP&gt;

Is the 64-bit name of the destination general-purpose register or stack pointer, encoded in the 'Rd' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the source general-purpose register or stack pointer, encoded in the 'Rn' field.

## Alias Conditions

```
Alias Is preferred when
```

```
MOV (to/from SP) sh == '0' && imm12 == '000000000000' && (Rd == '11111' || Rn == '11111')
```

## Operation

```
constant bits(datasize) operand1 = if n == 31 then SP[datasize] else X[n, datasize]; constant bits(datasize) operand2 = ZeroExtend(imm, datasize); bits(datasize) result; (result, -) = AddWithCarry(operand1, operand2, '0'); if d == 31 then SP[64] = ZeroExtend(result, 64); else X[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
