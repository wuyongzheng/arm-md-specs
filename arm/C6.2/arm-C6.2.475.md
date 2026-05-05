## C6.2.475 SYSL

System instruction with result

For more information, see Op0 equals 0b01 , cache maintenance, TLB maintenance, and address translation instructions for the encodings of System instructions.

This instruction is used by the aliases GCSPOPM and GCSSS2.

<!-- image -->

## Encoding

```
SYSL <Xt>, #<op1>, <Cn>, <Cm>, #<op2>
```

## Decode for this encoding

```
= UInt(Rt);
```

```
constant integer t constant bits(1) sys_L = L; constant bits(2) sys_op0 = '01'; constant bits(3) sys_op1 = op1; constant bits(3) sys_op2 = op2; constant bits(4) sys_crn = CRn; constant bits(4) sys_crm = CRm;
```

## Assembler Symbols

## &lt;Xt&gt;

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rt' field.

## &lt;op1&gt;

Is a 3-bit unsigned immediate, in the range 0 to 7, encoded in the 'op1' field.

## &lt;Cn&gt;

Is a name 'Cn', with 'n' in the range 0 to 15, encoded in the 'CRn' field.

## &lt;Cm&gt;

Is a name 'Cm', with 'm' in the range 0 to 15, encoded in the 'CRm' field.

## &lt;op2&gt;

Is a 3-bit unsigned immediate, in the range 0 to 7, encoded in the 'op2' field.

## Alias Conditions

| Alias   | Is preferred when                                              |
|---------|----------------------------------------------------------------|
| GCSPOPM | op1 == '011' && CRn == '0111' && CRm == '0111' && op2 == '001' |
| GCSSS2  | op1 == '011' && CRn == '0111' && CRm == '0111' && op2 == '011' |

## Operation

AArch64.SysInstrWithResult(sys\_op0, sys\_op1, sys\_crn, sys\_crm, sys\_op2, t);
