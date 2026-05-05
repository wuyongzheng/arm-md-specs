## C6.2.301 ORR (shifted register)

Bitwise OR (shifted register)

This instruction performs a bitwise (inclusive) OR of a register value and an optionally-shifted register value, and writes the result to the destination register.

This instruction is used by the alias MOV (register).

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (sf == 0) ORR <Wd>, <Wn>, <Wm>{, <shift>
```

## Encoding for the 64-bit variant

```
Applies when (sf == 1) ORR <Xd>, <Xn>, <Xm>{, <shift>
```

```
#<amount>}
```

```
#<amount>}
```

## Decode for all variants of this encoding

```
EndOfDecode(Decode_UNDEF);
```

```
if sf == '0' && imm6<5> == '1' then constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer datasize = 32 << UInt(sf); constant ShiftType shift_type = DecodeShift(shift); constant integer shift_amount = UInt(imm6);
```

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Wn&gt;

Is the 32-bit name of the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Wm&gt;

Is the 32-bit name of the second general-purpose source register, encoded in the 'Rm' field.

## &lt;shift&gt;

Is the optional shift to be applied to the final source, defaulting to LSL and encoded in 'shift':

|   shift | <shift>   |
|---------|-----------|
|      00 | LSL       |
|      01 | LSR       |

## &lt;amount&gt;

For the '32-bit' variant: is the shift amount, in the range 0 to 31, defaulting to 0 and encoded in the 'imm6' field. For the '64-bit' variant: is the shift amount, in the range 0 to 63, defaulting to 0 and encoded in the 'imm6' field.

## &lt;Xd&gt;

## &lt;Xn&gt;

Is the 64-bit name of the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Xm&gt;

Is the 64-bit name of the second general-purpose source register, encoded in the 'Rm' field.

## Alias Conditions

```
Alias Is preferred when MOV (register) shift == '00' && imm6 == '000000' && Rn == '11111'
```

## Operation

```
constant bits(datasize) operand1 = X[n, datasize]; constant bits(datasize) operand2 = ShiftReg(m, shift_type, shift_amount, datasize); X[d, datasize] = operand1 OR operand2;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

|   shift | <shift>   |
|---------|-----------|
|      10 | ASR       |
|      11 | ROR       |

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.
