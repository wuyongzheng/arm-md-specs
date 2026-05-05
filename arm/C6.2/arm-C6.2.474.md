## C6.2.474 SYS

System instruction

For more information, see Op0 equals 0b01 , cache maintenance, TLB maintenance, and address translation instructions for the encodings of System instructions.

This instruction is used by the aliases APAS, AT, BRB, CFP, COSP, CPP, DC, DVP, GCSPOPCX, GCSPOPX, GCSPUSHM, GCSPUSHX, GCSSS1, IC, TLBI, and TRCIT.

<!-- image -->

## Encoding

```
SYS #<op1>, <Cn>, <Cm>, #<op2>{, <Xt>}
```

## Decode for this encoding

```
= UInt(Rt);
```

```
constant integer t constant bits(1) sys_L = L; constant bits(2) sys_op0 = '01'; constant bits(3) sys_op1 = op1; constant bits(3) sys_op2 = op2; constant bits(4) sys_crn = CRn; constant bits(4) sys_crm = CRm;
```

## Assembler Symbols

## &lt;op1&gt;

Is a 3-bit unsigned immediate, in the range 0 to 7, encoded in the 'op1' field.

## &lt;Cn&gt;

Is a name 'Cn', with 'n' in the range 0 to 15, encoded in the 'CRn' field.

## &lt;Cm&gt;

Is a name 'Cm', with 'm' in the range 0 to 15, encoded in the 'CRm' field.

## &lt;op2&gt;

Is a 3-bit unsigned immediate, in the range 0 to 7, encoded in the 'op2' field.

## &lt;Xt&gt;

Is the 64-bit name of the optional general-purpose source register, defaulting to '11111', encoded in the 'Rt' field.

## Alias Conditions

| Alias   | Is preferred when                                              |
|---------|----------------------------------------------------------------|
| APAS    | op1 == '110' && CRn == '0111' && CRm == '0000' && op2 == '000' |

| Alias    | Is preferred when                                                                              |
|----------|------------------------------------------------------------------------------------------------|
| AT       | CRn == '0111' && CRm IN {'100x'} && SysOp(op1, '0111', CRm, op2) == Sys_AT                     |
| BRB      | op1 == '001' && CRn == '0111' && CRm == '0010' && SysOp('001', '0111', '0010', op2) == Sys_BRB |
| CFP      | op1 == '011' && CRn == '0111' && CRm == '0011' && op2 == '100'                                 |
| COSP     | op1 == '011' && CRn == '0111' && CRm == '0011' && op2 == '110'                                 |
| CPP      | op1 == '011' && CRn == '0111' && CRm == '0011' && op2 == '111'                                 |
| DC       | CRn == '0111' && SysOp(op1, '0111', CRm, op2) == Sys_DC                                        |
| DVP      | op1 == '011' && CRn == '0111' && CRm == '0011' && op2 == '101'                                 |
| GCSPOPCX | op1 == '000' && CRn == '0111' && CRm == '0111' && op2 == '101'                                 |
| GCSPOPX  | op1 == '000' && CRn == '0111' && CRm == '0111' && op2 == '110'                                 |
| GCSPUSHM | op1 == '011' && CRn == '0111' && CRm == '0111' && op2 == '000'                                 |
| GCSPUSHX | op1 == '000' && CRn == '0111' && CRm == '0111' && op2 == '100'                                 |
| GCSSS1   | op1 == '011' && CRn == '0111' && CRm == '0111' && op2 == '010'                                 |
| IC       | CRn == '0111' && SysOp(op1, '0111', CRm, op2) == Sys_IC                                        |
| TLBI     | CRn IN {'100x'} && SysOp(op1, CRn, CRm, op2) == Sys_TLBI                                       |
| TRCIT    | op1 == '011' && CRn == '0111' && CRm == '0010' && op2 == '111'                                 |

## Operation

AArch64.SysInstr(sys\_op0, sys\_op1, sys\_crn, sys\_crm, sys\_op2, t);
