## C6.2.78 CBZ

## Compare and branch on zero

This instruction compares the value in a register with zero, and conditionally branches to a label at a PC-relative offset if the comparison is equal. This instruction provides a hint that this is not a subroutine call or return. This instruction does not affect condition flags.

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (sf == 0) CBZ <Wt>, <label>
```

## Encoding for the 64-bit variant

```
Applies when (sf == 1) CBZ <Xt>, <label>
```

## Decode for all variants of this encoding

```
constant integer t = UInt(Rt); constant integer datasize = 32 << UInt(sf); constant bits(64) offset
```

## Assembler Symbols

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be tested, encoded in the 'Rt' field.

## &lt;label&gt;

Is the program label to be conditionally branched to. Its offset from the address of this instruction, in the range +/-1MB, is encoded as 'imm19' times 4.

## &lt;Xt&gt;

Is the 64-bit name of the general-purpose register to be tested, encoded in the 'Rt' field.

## Operation

```
constant boolean branch_conditional = TRUE; constant bits(datasize) operand1 = X[t, datasize]; if IsZero(operand1) then BranchTo(PC64 + offset, BranchType_DIR, branch_conditional); else BranchNotTaken(BranchType_DIR, branch_conditional);
```

```
= SignExtend(imm19:'00', 64);
```
