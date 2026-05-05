## C6.2.36 BC.cond

Branch consistent conditionally

This instruction branches conditionally to a label at a PC-relative offset, with a hint that this branch is very unlikely to change direction. This instruction provides a hint that this is not a subroutine call or return.

19-bit signed PC-relative branch offset (FEAT\_HBC)

<!-- image -->

## Encoding

```
BC.<cond> <label>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_HBC) then EndOfDecode(Decode_UNDEF);
```

```
constant bits(64) offset = SignExtend(imm19:'00', 64); constant bits(4) condition = cond;
```

## Assembler Symbols

## &lt;cond&gt;

Is one of the standard conditions, encoded in the standard way, and encoded in 'cond':

|   cond | <cond>   |
|--------|----------|
|   0000 | EQ       |
|   0001 | NE       |
|   0010 | CS       |
|   0011 | CC       |
|   0100 | MI       |
|   0101 | PL       |
|   0110 | VS       |
|   0111 | VC       |
|   1000 | HI       |
|   1001 | LS       |
|   1010 | GE       |
|   1011 | LT       |
|   1100 | GT       |
|   1101 | LE       |
|   1110 | AL       |
|   1111 | NV       |

## &lt;label&gt;

Is the program label to be conditionally branched to. Its offset from the address of this instruction, in the range +/-1MB, is encoded as 'imm19' times 4.

## Operation

```
constant boolean branch_conditional = TRUE; if ConditionHolds(condition) then BranchTo(PC64 + offset, else BranchNotTaken(BranchType_DIR, branch_conditional);
```

```
BranchType_DIR, branch_conditional);
```
