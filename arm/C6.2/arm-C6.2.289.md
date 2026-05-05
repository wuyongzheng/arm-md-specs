## C6.2.289 MSRR

Move two adjacent general-purpose registers to System register

This instruction allows the PE to write an AArch64 128-bit System register from two adjacent 64-bit general-purpose registers.

## System

(FEAT\_SYSREG128)

<!-- image -->

## Encoding

MSRR (&lt;systemreg&gt;|S&lt;op0&gt;\_&lt;op1&gt;\_&lt;Cn&gt;\_&lt;Cm&gt;\_&lt;op2&gt;), &lt;Xt&gt;, &lt;Xt+1&gt;

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SYSREG128) then EndOfDecode(Decode_UNDEF); if Rt<0> == '1' then EndOfDecode(Decode_UNDEF); constant integer t = UInt(Rt); constant integer t2 = UInt(Rt+1); constant bits(1) sys_L = L; constant bits(2) sys_op0 = '1' : o0; constant bits(3) sys_op1 = op1; constant bits(3) sys_op2 = op2; constant bits(4) sys_crn = CRn; constant bits(4) sys_crm = CRm;
```

## Assembler Symbols

&lt;systemreg&gt;

Is a System register name, encoded in 'o0:op1:CRn:CRm:op2'.

&lt;op0&gt;

Is an unsigned immediate, encoded in 'o0':

|   o0 |   <op0> |
|------|---------|
|    0 |       2 |
|    1 |       3 |

```
<op1> Is a 3-bit unsigned immediate, in the range 0 to 7, encoded in the 'op1' field. <Cn>
```

Is a name 'Cn', with 'n' in the range 0 to 15, encoded in the 'CRn' field.

## &lt;Cm&gt;

Is a name 'Cm', with 'm' in the range 0 to 15, encoded in the 'CRm' field.

&lt;op2&gt;

Is a 3-bit unsigned immediate, in the range 0 to 7, encoded in the 'op2' field.

## &lt;Xt&gt;

Is the 64-bit name of the first general-purpose source register, encoded in the 'Rt' field.

## &lt;Xt+1&gt;

Is the 64-bit name of the second general-purpose source register, encoded as 'Rt' +1.

## Operation

AArch64.SysRegWrite128(sys\_op0, sys\_op1, sys\_crn, sys\_crm, sys\_op2, t, t2);
