## C6.2.476 SYSP

128-bit system instruction.

This instruction is used by the alias TLBIP.

## System

(FEAT\_SYSINSTR128)

<!-- image -->

## Encoding

```
SYSP #<op1>, <Cn>, <Cm>, #<op2>{, <Xt1>, <Xt2>}
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SYSINSTR128) then if Rt<0> == '1' && Rt != '11111' then EndOfDecode(Decode_UNDEF); constant integer t = UInt(Rt); constant integer t2 = if t == 31 then 31 else t + 1; constant bits(1) sys_L = L; constant bits(2) sys_op0 = '01'; constant bits(3) sys_op1 = op1; constant bits(3) sys_op2 = op2; constant bits(4) sys_crn = CRn; constant bits(4) sys_crm = CRm;
```

## Assembler Symbols

## &lt;op1&gt;

Is a 3-bit unsigned immediate, in the range 0 to 6, encoded in the 'op1' field.

## &lt;Cn&gt;

Is a name 'Cn', with 'n' in the range 8 to 9, encoded in the 'CRn' field.

## &lt;Cm&gt;

Is a name 'Cm', with 'm' in the range 0 to 7, encoded in the 'CRm' field.

## &lt;op2&gt;

Is a 3-bit unsigned immediate, in the range 0 to 7, encoded in the 'op2' field.

## &lt;Xt1&gt;

Is the 64-bit name of the first optional general-purpose source register, defaulting to '11111', encoded in the 'Rt' field.

## &lt;Xt2&gt;

Is the 64-bit name of the second optional general-purpose source register, defaulting to '11111', encoded as 'Rt' +1. Defaults to '11111' if 'Rt' = '11111'.

```
EndOfDecode(Decode_UNDEF);
```

## Alias Conditions

| Alias   | Is preferred when                                            |
|---------|--------------------------------------------------------------|
| TLBIP   | CRn IN {'100x'} && SysOp128(op1, CRn, CRm, op2) == Sys_TLBIP |

## Operation

AArch64.SysInstr128(sys\_op0, sys\_op1, sys\_crn, sys\_crm, sys\_op2, t, t2);
