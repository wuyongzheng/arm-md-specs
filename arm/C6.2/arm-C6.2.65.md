## C6.2.65 CBH&lt;cc&gt;

## Compare halfwords and branch

This instruction compares the halfword values in two registers, and conditionally branches to a label at a PC-relative offset if the condition is true. This instruction provides a hint that this is not a subroutine call or return. This instruction does not affect the condition flags.

This instruction is used by the pseudo-instructions CBHLE, CBHLO, CBHLS, and CBHLT.

## Branch

(FEAT\_CMPBR)

<!-- image -->

## Encoding for the Greater than variant

```
Applies when (cc == 000) CBHGT <Wt>, <Wm>, <label>
```

## Encoding for the Greater than or equal variant

```
Applies when (cc == 001) CBHGE <Wt>, <Wm>, <label>
```

## Encoding for the Higher variant

```
Applies when (cc == 010) CBHHI <Wt>, <Wm>, <label>
```

## Encoding for the Higher or same variant

```
Applies when (cc == 011) CBHHS <Wt>, <Wm>, <label>
```

## Encoding for the Equal variant

```
Applies when (cc == 110) CBHEQ <Wt>, <Wm>, <label>
```

## Encoding for the Not equal variant

```
Applies when (cc == 111) CBHNE <Wt>, <Wm>, <label>
```

## Decode for all variants of this encoding

```
EndOfDecode(Decode_UNDEF);
```

```
if !IsFeatureImplemented(FEAT_CMPBR) then constant integer datasize = 8 << UInt(H); constant integer t = UInt(Rt); constant integer m = UInt(Rm); constant bits(64) offset = SignExtend(imm9:'00', 64); CmpOp op; boolean unsigned; case cc of when '000' op = Cmp_GT; unsigned = FALSE; when '001' op = Cmp_GE; unsigned = FALSE; when '010' op = Cmp_GT; unsigned = TRUE; when '011' op = Cmp_GE; unsigned = TRUE; when '110' op = Cmp_EQ; unsigned = TRUE; when '111' op = Cmp_NE; unsigned = TRUE; otherwise EndOfDecode(Decode_UNDEF);
```

## Assembler Symbols

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be tested, encoded in the 'Rt' field.

## &lt;Wm&gt;

Is the 32-bit name of the second general-purpose source register, encoded in the 'Rm' field.

## &lt;label&gt;

Is the program label to be conditionally branched to. Its offset from the address of this instruction, in the range -1024 to 1020, is encoded as 'imm9' times 4.

## Operation

```
constant bits(datasize) operand1 = X[t, datasize]; constant bits(datasize) operand2 = X[m, datasize]; constant boolean branch_conditional = TRUE; constant integer value1 = if unsigned then UInt(operand1) else SInt(operand1); constant integer value2 = if unsigned then UInt(operand2) else SInt(operand2); boolean cond; case op of when Cmp_EQ cond = value1 == value2; when Cmp_NE cond = value1 != value2; when Cmp_GE cond = value1 >= value2; when Cmp_GT cond = value1 > value2; if cond then BranchTo(PC64 + offset, BranchType_DIR, branch_conditional); else BranchNotTaken(BranchType_DIR, branch_conditional);
```
