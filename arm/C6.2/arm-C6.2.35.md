## C6.2.35 B

## Branch

This instruction branches unconditionally to a label at a PC-relative offset. This instruction provides a hint that this is not a subroutine call or return.

<!-- image -->

## Encoding

B

&lt;label&gt;

## Decode for this encoding

constant bits(64) offset = SignExtend(imm26:'00', 64);

## Assembler Symbols

## &lt;label&gt;

Is the program label to be unconditionally branched to. Its offset from the address of this instruction, in the range +/-128MB, is encoded as 'imm26' times 4.

## Operation

constant boolean branch\_conditional

BranchTo(PC64 + offset,

```
= FALSE; BranchType_DIR, branch_conditional);
```
