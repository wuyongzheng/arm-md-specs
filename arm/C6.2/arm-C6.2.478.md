## C6.2.478 TBZ

Test bit and branch if zero

This instruction compares the value of a test bit with zero, and conditionally branches to a label at a PC-relative offset if the comparison is equal. This instruction provides a hint that this is not a subroutine call or return. This instruction does not affect condition flags.

<!-- image -->

## Encoding

```
TBZ
```

```
<R><t>, #<imm>, <label>
```

## Decode for this encoding

```
constant integer t = UInt(Rt); constant integer datasize = 32 << UInt(b5); constant integer bit_pos = UInt(b5:b40); constant bits(64) offset
```

## Assembler Symbols

&lt;R&gt;

Is a width specifier, encoded in 'b5':

```
= SignExtend(imm14:'00', 64);
```

<!-- image -->

Is the number [0-30] of the general-purpose register to be tested or the name ZR (31), encoded in the 'Rt' field.

## &lt;imm&gt;

Is the bit number to be tested, in the range 0 to 63, encoded in 'b5:b40'.

## &lt;label&gt;

Is the program label to be conditionally branched to. Its offset from the address of this instruction, in the range +/-32KB, is encoded as 'imm14' times 4.

|   b5 | <R>   |
|------|-------|
|    0 | W     |
|    1 | X     |

In assembler source code an 'X' specifier is always permitted, but a 'W' specifier is only permitted when the bit number is less than 32.

## Operation

```
constant bits(datasize) operand = X[t, datasize]; constant boolean branch_conditional = TRUE; if operand<bit_pos> == '0' then BranchTo(PC64 + offset, else BranchNotTaken(BranchType_DIR, branch_conditional);
```

```
BranchType_DIR, branch_conditional);
```
