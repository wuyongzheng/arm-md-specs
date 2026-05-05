## C6.2.285 MRRS

Move System register to two adjacent general-purpose registers

This instruction allows the PE to read an AArch64 128-bit System register into two adjacent 64-bit general-purpose registers.

## System

(FEAT\_SYSREG128)

<!-- image -->

## Encoding

```
MRRS <Xt>, <Xt+1>, (<systemreg>|S<op0>_<op1>_<Cn>_<Cm>_<op2>)
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SYSREG128) then EndOfDecode(Decode_UNDEF); if Rt<0> == '1' then EndOfDecode(Decode_UNDEF); constant integer t = UInt(Rt); constant integer t2 = UInt(Rt+1); constant bits(1) sys_L = L; constant bits(2) sys_op0 = '1' : o0; constant bits(3) sys_op1 = op1; constant bits(3) sys_op2 = op2; constant bits(4) sys_crn = CRn; constant bits(4) sys_crm = CRm;
```

## Assembler Symbols

&lt;Xt&gt;

Is the 64-bit name of the first general-purpose destination register, encoded in the 'Rt' field.

## &lt;Xt+1&gt;

Is the 64-bit name of the second general-purpose destination register, encoded as 'Rt' +1.

## &lt;systemreg&gt;

Is a System register name, encoded in 'o0:op1:CRn:CRm:op2'.

## &lt;op0&gt;

Is an unsigned immediate, encoded in 'o0':

|   o0 |   <op0> |
|------|---------|
|    0 |       2 |
|    1 |       3 |

## &lt;op1&gt;

## Is a 3-bit unsigned immediate, in the range 0 to 7, encoded in the 'op1' field. &lt;Cn&gt; Is a name 'Cn', with 'n' in the range 0 to 15, encoded in the 'CRn' field. &lt;Cm&gt; Is a name 'Cm', with 'm' in the range 0 to 15, encoded in the 'CRm' field. &lt;op2&gt; Is a 3-bit unsigned immediate, in the range 0 to 7, encoded in the 'op2' field.

## Operation

AArch64.SysRegRead128(sys\_op0, sys\_op1, sys\_crn, sys\_crm, sys\_op2, t, t2);
