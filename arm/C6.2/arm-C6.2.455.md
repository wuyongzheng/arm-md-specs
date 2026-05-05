## C6.2.455 SUB (extended register)

Subtract extended and scaled register

This instruction subtracts a sign or zero-extended register value, followed by an optional left shift amount, from a register value, and writes the result to the destination register. The argument that is extended from the &lt;Rm&gt; register can be a byte, halfword, word, or doubleword.

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (sf == 0) SUB <Wd|WSP>, <Wn|WSP>, <Wm>{, <extend>
```

```
{#<amount>}}
```

## Encoding for the 64-bit variant

```
Applies when (sf == 1) SUB <Xd|SP>, <Xn|SP>, <R><m>{, <extend> {#<amount>}}
```

## Decode for all variants of this encoding

```
if imm3 IN {'101', '110', '111'} then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer shift = UInt(imm3); constant integer datasize = 32 << UInt(sf); constant ExtendType extend_type = DecodeRegExtend(option);
```

## Assembler Symbols

## &lt;Wd|WSP&gt;

Is the 32-bit name of the destination general-purpose register or stack pointer, encoded in the 'Rd' field.

## &lt;Wn|WSP&gt;

Is the 32-bit name of the first source general-purpose register or stack pointer, encoded in the 'Rn' field.

## &lt;Wm&gt;

Is the 32-bit name of the second general-purpose source register, encoded in the 'Rm' field.

## &lt;extend&gt;

For the '32-bit' variant: is the extension to be applied to the second source operand, encoded in 'option':

|   option | <extend>   |
|----------|------------|
|      000 | UXTB       |
|      001 | UXTH       |

Is a width specifier, encoded in 'option':

|   option | <extend>      |
|----------|---------------|
|      010 | LSL&#124;UXTW |
|      011 | UXTX          |
|      100 | SXTB          |
|      101 | SXTH          |
|      110 | SXTW          |
|      111 | SXTX          |

If 'Rd' or 'Rn' is '11111' (WSP) and 'option' is '010' then LSL is preferred, but may be omitted when 'imm3' is '000'. In all other cases &lt;extend&gt; is required and must be UXTW when 'option' is '010'.

For the '64-bit' variant: is the extension to be applied to the second source operand, encoded in 'option':

|   option | <extend>      |
|----------|---------------|
|      000 | UXTB          |
|      001 | UXTH          |
|      010 | UXTW          |
|      011 | LSL&#124;UXTX |
|      100 | SXTB          |
|      101 | SXTH          |
|      110 | SXTW          |
|      111 | SXTX          |

If 'Rd' or 'Rn' is '11111' (SP) and 'option' is '011' then LSL is preferred, but may be omitted when 'imm3' is '000'. In all other cases &lt;extend&gt; is required and must be UXTX when 'option' is '011'.

## &lt;amount&gt;

Is the left shift amount to be applied after extension in the range 0 to 4, defaulting to 0, encoded in the 'imm3' field. It must be absent when &lt;extend&gt; is absent, is required when &lt;extend&gt; is LSL, and is optional when &lt;extend&gt; is present but not LSL.

## &lt;Xd|SP&gt;

Is the 64-bit name of the destination general-purpose register or stack pointer, encoded in the 'Rd' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the first source general-purpose register or stack pointer, encoded in the 'Rn' field.

<!-- image -->

| option   | <R>   |
|----------|-------|
| 00x      | W     |

&lt;m&gt;

Is the number [0-30] of the second general-purpose source register or the name ZR (31), encoded in the 'Rm' field.

## Operation

```
constant bits(datasize) operand1 = if n == 31 then SP[datasize] else X[n, datasize]; constant bits(datasize) operand2 = NOT(ExtendReg(m, extend_type, shift, datasize)); bits(datasize) result; (result, -) = AddWithCarry(operand1, operand2, '1'); if d == 31 then SP[64] = ZeroExtend(result, 64); else X[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

| option   | <R>   |
|----------|-------|
| 010      | W     |
| x11      | X     |
| 10x      | W     |
| 110      | W     |
