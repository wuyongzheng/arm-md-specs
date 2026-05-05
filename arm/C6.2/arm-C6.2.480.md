## C6.2.480 TLBIP

TLB invalidate pair operation.

This is an alias of SYSP. This means:

- The encodings in this description are named to match the encodings of SYSP.
- The description of SYSP gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## System

## (FEAT\_SYSINSTR128)

<!-- image -->

## Encoding

```
TLBIP <tlbip_op>{, <Xt1>, <Xt2>}
```

## is equivalent to

```
SYSP #<op1>, <Cn>, <Cm>, #<op2>{, <Xt1>, <Xt2>}
```

and is the preferred disassembly when SysOp128(op1, CRn, CRm, op2) == Sys\_TLBIP .

## Assembler Symbols

## &lt;tlbip\_op&gt;

Is a TLBIP operation name, as listed for the TLBIP system pair instruction group, encoded in 'op1:CRn:CRm:op2':

|   op1 |   CRn |   CRm |   op2 | <tlbip_op>   | Architectural Feature   |
|-------|-------|-------|-------|--------------|-------------------------|
|   000 |  1000 |  0001 |   001 | VAE1OS       | FEAT_D128               |
|   000 |  1000 |  0001 |   011 | VAAE1OS      | FEAT_D128               |
|   000 |  1000 |  0001 |   101 | VALE1OS      | FEAT_D128               |
|   000 |  1000 |  0001 |   111 | VAALE1OS     | FEAT_D128               |
|   000 |  1000 |  0010 |   001 | RVAE1IS      | FEAT_D128               |
|   000 |  1000 |  0010 |   011 | RVAAE1IS     | FEAT_D128               |
|   000 |  1000 |  0010 |   101 | RVALE1IS     | FEAT_D128               |
|   000 |  1000 |  0010 |   111 | RVAALE1IS    | FEAT_D128               |
|   000 |  1000 |  0011 |   001 | VAE1IS       | FEAT_D128               |
|   000 |  1000 |  0011 |   011 | VAAE1IS      | FEAT_D128               |
|   000 |  1000 |  0011 |   101 | VALE1IS      | FEAT_D128               |
|   000 |  1000 |  0011 |   111 | VAALE1IS     | FEAT_D128               |
|   000 |  1000 |  0101 |   001 | RVAE1OS      | FEAT_D128               |

|   op1 | CRn       |   CRm |   op2 | <tlbip_op>   | Architectural Feature   |
|-------|-----------|-------|-------|--------------|-------------------------|
|   000 | 1000      |  0101 |   011 | RVAAE1OS     | FEAT_D128               |
|   000 | 1000      |  0101 |   101 | RVALE1OS     | FEAT_D128               |
|   000 | 1000      |  0101 |   111 | RVAALE1OS    | FEAT_D128               |
|   000 | 1000      |  0110 |   001 | RVAE1        | FEAT_D128               |
|   000 | 1000      |  0110 |   011 | RVAAE1       | FEAT_D128               |
|   000 | 1000      |  0110 |   101 | RVALE1       | FEAT_D128               |
|   000 | 1000      |  0110 |   111 | RVAALE1      | FEAT_D128               |
|   000 | 1000      |  0111 |   001 | VAE1         | FEAT_D128               |
|   000 | 1000      |  0111 |   011 | VAAE1        | FEAT_D128               |
|   000 | 1000      |  0111 |   101 | VALE1        | FEAT_D128               |
|   000 | 1000      |  0111 |   111 | VAALE1       | FEAT_D128               |
|   000 | 1001      |  0001 |   001 | VAE1OSNXS    | FEAT_D128               |
|   000 | 1001      |  0001 |   011 | VAAE1OSNXS   | FEAT_D128               |
|   000 | 1001      |  0001 |   101 | VALE1OSNXS   | FEAT_D128               |
|   000 | 1001      |  0001 |   111 | VAALE1OSNXS  | FEAT_D128               |
|   000 | 1001      |  0010 |   011 | RVAAE1ISNXS  | FEAT_D128               |
|   000 | 1001      |  0010 |   101 | RVALE1ISNXS  | FEAT_D128               |
|   000 | 1001      |  0010 |   111 | RVAALE1ISNXS | FEAT_D128               |
|   000 | 1001      |  0011 |   001 | VAE1ISNXS    | FEAT_D128               |
|   000 | 1001      |  0011 |   011 | VAAE1ISNXS   | FEAT_D128               |
|   000 | 1001      |  0011 |   101 | VALE1ISNXS   | FEAT_D128               |
|   000 | 1001      |  0011 |   111 | VAALE1ISNXS  | FEAT_D128               |
|   000 | 1001      |  0101 |   001 | RVAE1OSNXS   | FEAT_D128               |
|   000 | 1001      |  0101 |   011 | RVAAE1OSNXS  | FEAT_D128               |
|   000 | 1001      |  0101 |   101 | RVALE1OSNXS  | FEAT_D128               |
|   000 | 1001      |  0101 |   111 | RVAALE1OSNXS | FEAT_D128               |
|   000 | 1001      |  0110 |   001 | RVAE1NXS     | FEAT_D128               |
|   000 | 1001      |  0110 |   011 | RVAAE1NXS    | FEAT_D128               |
|   000 | 1001      |  0110 |   101 | RVALE1NXS    | FEAT_D128               |
|   000 | 1001      |  0110 |   111 | RVAALE1NXS   | FEAT_D128               |
|   000 | 1001      |  0111 |   001 | VAE1NXS      | FEAT_D128               |
|   000 | 1001      |  0111 |   011 | VAAE1NXS     | FEAT_D128               |
|   000 | 1001 1001 |  0111 |   101 | VALE1NXS     | FEAT_D128               |
|   000 |           |  0111 |   111 | VAALE1NXS    | FEAT_D128               |
|   100 | 1000      |  0000 |   001 | IPAS2E1IS    | FEAT_D128               |
|   100 | 1000      |  0000 |   010 | RIPAS2E1IS   | FEAT_D128               |
|   100 | 1000      |  0000 |   101 | IPAS2LE1IS   | FEAT_D128               |
|   100 | 1000      |  0000 |   110 | RIPAS2LE1IS  | FEAT_D128               |

|   op1 |   CRn |   CRm |   op2 | <tlbip_op>     | Architectural Feature   |
|-------|-------|-------|-------|----------------|-------------------------|
|   100 |  1000 |  0001 |   101 | VALE2OS        | FEAT_D128               |
|   100 |  1000 |  0010 |   001 | RVAE2IS        | FEAT_D128               |
|   100 |  1000 |  0010 |   101 | RVALE2IS       | FEAT_D128               |
|   100 |  1000 |  0011 |   001 | VAE2IS         | FEAT_D128               |
|   100 |  1000 |  0011 |   101 | VALE2IS        | FEAT_D128               |
|   100 |  1000 |  0100 |   000 | IPAS2E1OS      | FEAT_D128               |
|   100 |  1000 |  0100 |   001 | IPAS2E1        | FEAT_D128               |
|   100 |  1000 |  0100 |   010 | RIPAS2E1       | FEAT_D128               |
|   100 |  1000 |  0100 |   011 | RIPAS2E1OS     | FEAT_D128               |
|   100 |  1000 |  0100 |   100 | IPAS2LE1OS     | FEAT_D128               |
|   100 |  1000 |  0100 |   101 | IPAS2LE1       | FEAT_D128               |
|   100 |  1000 |  0100 |   110 | RIPAS2LE1      | FEAT_D128               |
|   100 |  1000 |  0100 |   111 | RIPAS2LE1OS    | FEAT_D128               |
|   100 |  1000 |  0101 |   001 | RVAE2OS        | FEAT_D128               |
|   100 |  1000 |  0101 |   101 | RVALE2OS       | FEAT_D128               |
|   100 |  1000 |  0110 |   001 | RVAE2          | FEAT_D128               |
|   100 |  1000 |  0110 |   101 | RVALE2         | FEAT_D128               |
|   100 |  1000 |  0111 |   001 | VAE2           | FEAT_D128               |
|   100 |  1000 |  0111 |   101 | VALE2          | FEAT_D128               |
|   100 |  1001 |  0000 |   001 | IPAS2E1ISNXS   | FEAT_D128               |
|   100 |  1001 |  0000 |   010 | RIPAS2E1ISNXS  | FEAT_D128               |
|   100 |  1001 |  0000 |   101 | IPAS2LE1ISNXS  | FEAT_D128               |
|   100 |  1001 |  0000 |   110 | RIPAS2LE1ISNXS | FEAT_D128               |
|   100 |  1001 |  0001 |   001 | VAE2OSNXS      | FEAT_D128               |
|   100 |  1001 |  0001 |   101 | VALE2OSNXS     | FEAT_D128               |
|   100 |  1001 |  0010 |   001 | RVAE2ISNXS     | FEAT_D128               |
|   100 |  1001 |  0010 |   101 | RVALE2ISNXS    | FEAT_D128               |
|   100 |  1001 |  0011 |   001 | VAE2ISNXS      | FEAT_D128               |
|   100 |  1001 |  0011 |   101 | VALE2ISNXS     | FEAT_D128               |
|   100 |  1001 |  0100 |   000 | IPAS2E1OSNXS   | FEAT_D128               |
|   100 |  1001 |  0100 |   001 | IPAS2E1NXS     | FEAT_D128               |
|   100 |  1001 |  0100 |   010 | RIPAS2E1NXS    | FEAT_D128               |
|   100 |  1001 |  0100 |   011 | RIPAS2E1OSNXS  | FEAT_D128               |
|   100 |  1001 |  0100 |   100 | IPAS2LE1OSNXS  | FEAT_D128               |
|   100 |  1001 |  0100 |   101 | IPAS2LE1NXS    | FEAT_D128               |
|   100 |  1001 |  0100 |   110 | RIPAS2LE1NXS   | FEAT_D128               |
|   100 |  1001 |  0100 |   111 | RIPAS2LE1OSNXS | FEAT_D128               |
|   100 |  1001 |  0101 |   001 | RVAE2OSNXS     | FEAT_D128               |
|   100 |  1001 |  0101 |   101 | RVALE2OSNXS    | FEAT_D128 FEAT_D128     |
|   100 |  1001 |  0110 |   001 | RVAE2NXS       |                         |

|   op1 |   CRn |   CRm |   op2 | <tlbip_op>   | Architectural Feature   |
|-------|-------|-------|-------|--------------|-------------------------|
|   100 |  1001 |  0110 |   101 | RVALE2NXS    | FEAT_D128               |
|   100 |  1001 |  0111 |   001 | VAE2NXS      | FEAT_D128               |
|   100 |  1001 |  0111 |   101 | VALE2NXS     | FEAT_D128               |
|   110 |  1000 |  0001 |   001 | VAE3OS       | FEAT_D128               |
|   110 |  1000 |  0001 |   101 | VALE3OS      | FEAT_D128               |
|   110 |  1000 |  0010 |   001 | RVAE3IS      | FEAT_D128               |
|   110 |  1000 |  0010 |   101 | RVALE3IS     | FEAT_D128               |
|   110 |  1000 |  0011 |   001 | VAE3IS       | FEAT_D128               |
|   110 |  1000 |  0011 |   101 | VALE3IS      | FEAT_D128               |
|   110 |  1000 |  0101 |   001 | RVAE3OS      | FEAT_D128               |
|   110 |  1000 |  0101 |   101 | RVALE3OS     | FEAT_D128               |
|   110 |  1000 |  0110 |   001 | RVAE3        | FEAT_D128               |
|   110 |  1000 |  0110 |   101 | RVALE3       | FEAT_D128               |
|   110 |  1000 |  0111 |   001 | VAE3         | FEAT_D128               |
|   110 |  1000 |  0111 |   101 | VALE3        | FEAT_D128               |
|   110 |  1001 |  0001 |   001 | VAE3OSNXS    | FEAT_D128               |
|   110 |  1001 |  0001 |   101 | VALE3OSNXS   | FEAT_D128               |
|   110 |  1001 |  0010 |   001 | RVAE3ISNXS   | FEAT_D128               |
|   110 |  1001 |  0010 |   101 | RVALE3ISNXS  | FEAT_D128               |
|   110 |  1001 |  0011 |   001 | VAE3ISNXS    | FEAT_D128               |
|   110 |  1001 |  0011 |   101 | VALE3ISNXS   | FEAT_D128               |
|   110 |  1001 |  0101 |   001 | RVAE3OSNXS   | FEAT_D128               |
|   110 |  1001 |  0101 |   101 | RVALE3OSNXS  | FEAT_D128               |
|   110 |  1001 |  0110 |   001 | RVAE3NXS     | FEAT_D128               |
|   110 |  1001 |  0110 |   101 | RVALE3NXS    | FEAT_D128               |
|   110 |  1001 |  0111 |   001 | VAE3NXS      | FEAT_D128               |
|   110 |  1001 |  0111 |   101 | VALE3NXS     | FEAT_D128               |

## &lt;Xt1&gt;

Is the 64-bit name of the first optional general-purpose source register, defaulting to '11111', encoded in the 'Rt' field.

## &lt;Xt2&gt;

Is the 64-bit name of the second optional general-purpose source register, defaulting to '11111', encoded as 'Rt' +1. Defaults to '11111' if 'Rt' = '11111'.

## Operation

The description of SYSP gives the operational pseudocode for this instruction.
