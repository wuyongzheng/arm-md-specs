## C6.2.46 BR

## Branch to register

This instruction branches unconditionally to an address in a register. This instruction provides a hint that this is not a subroutine call or return.

<!-- image -->

## Encoding

BR

&lt;Xn&gt;

## Decode for this encoding

```
constant integer n = UInt(Rn);
```

## Assembler Symbols

<!-- image -->

Is the 64-bit name of the general-purpose register holding the address to be branched to, encoded in the 'Rn' field.

## Operation

```
constant bits(64) target = X[n, 64]; // Value in BTypeNext will be used to set PSTATE.BTYPE if InGuardedPage then if n == 16 || n == 17 then BTypeNext = '01'; else BTypeNext = '11'; else BTypeNext = '01'; constant boolean branch_conditional = FALSE; BranchTo(target, BranchType_INDIR, branch_conditional);
```
