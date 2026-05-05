## C6.2.348 RORV

Rotate right variable

This instruction provides the value of the contents of a register rotated by a variable number of bits. The bits that are rotated off the right end are inserted into the vacated bit positions on the left. The value of the second source register modulo the register size in bits gives the number of bits by which the first source register is right-shifted.

This instruction is used by the alias ROR (register).

<!-- image -->

## Encoding for the 32-bit variant

Applies when (sf == 0)

```
RORV <Wd>, <Wn>, <Wm>
```

## Encoding for the 64-bit variant

Applies when 1)

```
(sf == RORV <Xd>, <Xn>, <Xm>
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer datasize = 32 << UInt(sf); constant ShiftType shift_type =
```

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Wn&gt;

Is the 32-bit name of the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Wm&gt;

Is the 32-bit name of the second general-purpose source register holding a shift amount from 0 to 31 in its bottom 5 bits, encoded in the 'Rm' field.

## &lt;Xd&gt;

## &lt;Xn&gt;

Is the 64-bit name of the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Xm&gt;

Is the 64-bit name of the second general-purpose source register holding a shift amount from 0 to 63 in its bottom 6 bits, encoded in the 'Rm' field.

```
DecodeShift(op2);
```

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## Alias Conditions

## Operation

```
constant bits(datasize) operand2 = X[m, datasize]; X[d, datasize] = ShiftReg(n, shift_type, UInt(operand2) MOD datasize, datasize);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

| Alias   | Is preferred when   |
|---------|---------------------|
| ROR     | Unconditionally     |
