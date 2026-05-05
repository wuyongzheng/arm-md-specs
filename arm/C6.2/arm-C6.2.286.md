## C6.2.286 MRS

Move System register to general-purpose register

This instruction allows the PE to read an AArch64 System register into a general-purpose register.

<!-- image -->

## Encoding

MRS &lt;Xt&gt;, (&lt;systemreg&gt;|S&lt;op0&gt;\_&lt;op1&gt;\_&lt;Cn&gt;\_&lt;Cm&gt;\_&lt;op2&gt;)

## Decode for this encoding

```
constant integer t constant bits(1) sys_L = L; constant bits(2) sys_op0 = '1' : constant bits(3) sys_op1 = op1; constant bits(3) sys_op2 = op2; constant bits(4) sys_crn = CRn; constant bits(4) sys_crm = CRm;
```

```
= UInt(Rt); o0;
```

## Assembler Symbols

## &lt;Xt&gt;

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rt' field.

## &lt;systemreg&gt;

Is a System register name, encoded in 'o0:op1:CRn:CRm:op2'.

The System register names are defined in AArch64 System Register Descriptions.

## &lt;op0&gt;

Is an unsigned immediate, encoded in 'o0':

## &lt;op1&gt;

Is a 3-bit unsigned immediate, in the range 0 to 7, encoded in the 'op1' field.

## &lt;Cn&gt;

Is a name 'Cn', with 'n' in the range 0 to 15, encoded in the 'CRn' field.

## &lt;Cm&gt;

Is a name 'Cm', with 'm' in the range 0 to 15, encoded in the 'CRm' field.

L

|   o0 |   <op0> |
|------|---------|
|    0 |       2 |
|    1 |       3 |

&lt;op2&gt;

Is a 3-bit unsigned immediate, in the range 0 to 7, encoded in the 'op2' field.

## Operation

AArch64.SysRegRead(sys\_op0, sys\_op1, sys\_crn, sys\_crm, sys\_op2, t);
