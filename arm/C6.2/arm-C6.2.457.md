## C6.2.457 SUB (shifted register)

Subtract optionally-shifted register

This instruction subtracts an optionally-shifted register value from a register value, and writes the result to the destination register.

This instruction is used by the alias NEG (shifted register).

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (sf == 0) SUB <Wd>, <Wn>, <Wm>{, <shift> #<amount>}
```

## Encoding for the 64-bit variant

Applies when (sf ==

```
SUB <Xd>, <Xn>, <Xm>{, <shift>
```

```
1) #<amount>}
```

## Decode for all variants of this encoding

```
EndOfDecode(Decode_UNDEF);
```

```
if shift == '11' then EndOfDecode(Decode_UNDEF); if sf == '0' && imm6<5> == '1' then constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer datasize = 32 << UInt(sf); constant ShiftType shift_type = DecodeShift(shift); constant integer shift_amount = UInt(imm6);
```

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Wn&gt;

Is the 32-bit name of the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Wm&gt;

Is the 32-bit name of the second general-purpose source register, encoded in the 'Rm' field.

## &lt;shift&gt;

Is the optional shift type to be applied to the second source operand, defaulting to LSL and encoded in 'shift':

## &lt;amount&gt;

For the '32-bit' variant: is the shift amount, in the range 0 to 31, defaulting to 0 and encoded in the 'imm6' field. For the '64-bit' variant: is the shift amount, in the range 0 to 63, defaulting to 0 and encoded in the 'imm6' field.

## &lt;Xd&gt;

## &lt;Xn&gt;

Is the 64-bit name of the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Xm&gt;

Is the 64-bit name of the second general-purpose source register, encoded in the 'Rm' field.

## Alias Conditions

## Operation

```
constant bits(datasize) operand1 = X[n, datasize]; constant bits(datasize) operand2 = NOT(ShiftReg(m, shift_type, shift_amount, datasize)); bits(datasize) result; (result, -) = AddWithCarry(operand1, operand2, '1'); X[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

|   shift | <shift>   |
|---------|-----------|
|      00 | LSL       |
|      01 | LSR       |
|      10 | ASR       |
|      11 | RESERVED  |

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

| Alias                  | Is preferred when   |
|------------------------|---------------------|
| NEG (shifted register) | Rn == '11111'       |
