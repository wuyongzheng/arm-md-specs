## C6.2.479 TLBI

TLB invalidate operation

For more information, see op0== 0b01 , cache maintenance, TLB maintenance, and address translation instructions.

This is an alias of SYS. This means:

- The encodings in this description are named to match the encodings of SYS.
- The description of SYS gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding

```
TLBI <tlbi_op>{, <Xt>}
```

## is equivalent to

```
SYS #<op1>, <Cn>, <Cm>, #<op2>{, <Xt>}
```

and is the preferred disassembly when SysOp(op1, CRn, CRm, op2) == Sys\_TLBI .

## Assembler Symbols

## &lt;tlbi\_op&gt;

Is a TLBI operation name, as listed for the TLBI system instruction group, encoded in 'op1:CRn:CRm:op2':

|   op1 |   CRn |   CRm |   op2 | <tlbi_op>   | Architectural Feature   |
|-------|-------|-------|-------|-------------|-------------------------|
|   000 |  1000 |  0001 |   000 | VMALLE1OS   | FEAT_TLBIOS             |
|   000 |  1000 |  0001 |   001 | VAE1OS      | FEAT_TLBIOS             |
|   000 |  1000 |  0001 |   010 | ASIDE1OS    | FEAT_TLBIOS             |
|   000 |  1000 |  0001 |   011 | VAAE1OS     | FEAT_TLBIOS             |
|   000 |  1000 |  0001 |   101 | VALE1OS     | FEAT_TLBIOS             |
|   000 |  1000 |  0001 |   111 | VAALE1OS    | FEAT_TLBIOS             |
|   000 |  1000 |  0010 |   001 | RVAE1IS     | FEAT_TLBIRANGE          |
|   000 |  1000 |  0010 |   011 | RVAAE1IS    | FEAT_TLBIRANGE          |
|   000 |  1000 |  0010 |   101 | RVALE1IS    | FEAT_TLBIRANGE          |
|   000 |  1000 |  0010 |   111 | RVAALE1IS   | FEAT_TLBIRANGE          |
|   000 |  1000 |  0011 |   000 | VMALLE1IS   | -                       |
|   000 |  1000 |  0011 |   001 | VAE1IS      | -                       |
|   000 |  1000 |  0011 |   010 | ASIDE1IS    | -                       |
|   000 |  1000 |  0011 |   011 | VAAE1IS     | -                       |
|   000 |  1000 |  0011 |   101 | VALE1IS     | -                       |

| op1     | CRn       | CRm       |   op2 | <tlbi_op>    | Architectural Feature   |
|---------|-----------|-----------|-------|--------------|-------------------------|
| 000     | 1000      | 0011      |   111 | VAALE1IS     | -                       |
| 000     | 1000      | 0101      |   001 | RVAE1OS      | FEAT_TLBIRANGE          |
| 000     | 1000      | 0101      |   011 | RVAAE1OS     | FEAT_TLBIRANGE          |
| 000     | 1000      | 0101      |   101 | RVALE1OS     | FEAT_TLBIRANGE          |
| 000     | 1000      | 0101      |   111 | RVAALE1OS    | FEAT_TLBIRANGE          |
| 000     | 1000      | 0110      |   001 | RVAE1        | FEAT_TLBIRANGE          |
| 000     | 1000      | 0110      |   011 | RVAAE1       | FEAT_TLBIRANGE          |
| 000     | 1000      | 0110      |   101 | RVALE1       | FEAT_TLBIRANGE          |
| 000     | 1000      | 0110      |   111 | RVAALE1      | FEAT_TLBIRANGE          |
| 000     | 1000      | 0111      |   000 | VMALLE1      | -                       |
| 000     | 1000      | 0111      |   001 | VAE1         | -                       |
| 000     | 1000      | 0111      |   010 | ASIDE1       | -                       |
| 000     | 1000      | 0111      |   011 | VAAE1        | -                       |
| 000     | 1000      | 0111      |   101 | VALE1        | -                       |
| 000     | 1000      | 0111      |   111 | VAALE1       | -                       |
| 000     | 1001      | 0001      |   000 | VMALLE1OSNXS | FEAT_XS                 |
| 000     | 1001      | 0001      |   001 | VAE1OSNXS    | FEAT_XS                 |
| 000     | 1001      | 0001      |   010 | ASIDE1OSNXS  | FEAT_XS                 |
| 000     | 1001      | 0001      |   011 | VAAE1OSNXS   | FEAT_XS                 |
| 000     | 1001      | 0001      |   101 | VALE1OSNXS   | FEAT_XS                 |
| 000     | 1001      | 0001      |   111 | VAALE1OSNXS  | FEAT_XS                 |
| 000     | 1001      | 0010      |   001 | RVAE1ISNXS   | FEAT_XS                 |
| 000     | 1001      | 0010      |   011 | RVAAE1ISNXS  | FEAT_XS                 |
| 000     | 1001      | 0010      |   101 | RVALE1ISNXS  | FEAT_XS                 |
| 000     | 1001      | 0010      |   111 | RVAALE1ISNXS | FEAT_XS                 |
| 000     | 1001      | 0011      |   000 | VMALLE1ISNXS | FEAT_XS                 |
| 000     | 1001      | 0011      |   001 | VAE1ISNXS    | FEAT_XS                 |
| 000     | 1001      | 0011      |   010 | ASIDE1ISNXS  | FEAT_XS                 |
| 000     | 1001      | 0011      |   011 | VAAE1ISNXS   | FEAT_XS                 |
| 000     | 1001      | 0011      |   101 | VALE1ISNXS   | FEAT_XS                 |
| 000 000 | 1001 1001 | 0011 0101 |   111 | VAALE1ISNXS  | FEAT_XS FEAT_XS         |
|         |           |           |   001 | RVAE1OSNXS   |                         |
| 000     | 1001      | 0101      |   011 | RVAAE1OSNXS  | FEAT_XS                 |
| 000     | 1001      | 0101      |   111 | RVAALE1OSNXS | FEAT_XS                 |
| 000     | 1001      | 0110      |   001 | RVAE1NXS     | FEAT_XS                 |
| 000     | 1001      | 0110      |   011 | RVAAE1NXS    | FEAT_XS                 |
| 000     | 1001      | 0110      |   101 | RVALE1NXS    | FEAT_XS                 |
| 000     | 1001      | 0110      |   111 | RVAALE1NXS   | FEAT_XS                 |
| 000     | 1001      | 0111      |   000 | VMALLE1NXS   | FEAT_XS                 |

|   op1 |   CRn |   CRm |   op2 | <tlbi_op>    | Architectural Feature   |
|-------|-------|-------|-------|--------------|-------------------------|
|   000 |  1001 |  0111 |   001 | VAE1NXS      | FEAT_XS                 |
|   000 |  1001 |  0111 |   010 | ASIDE1NXS    | FEAT_XS                 |
|   000 |  1001 |  0111 |   011 | VAAE1NXS     | FEAT_XS                 |
|   000 |  1001 |  0111 |   101 | VALE1NXS     | FEAT_XS                 |
|   000 |  1001 |  0111 |   111 | VAALE1NXS    | FEAT_XS                 |
|   100 |  1000 |  0000 |   001 | IPAS2E1IS    | -                       |
|   100 |  1000 |  0000 |   010 | RIPAS2E1IS   | FEAT_TLBIRANGE          |
|   100 |  1000 |  0000 |   101 | IPAS2LE1IS   | -                       |
|   100 |  1000 |  0000 |   110 | RIPAS2LE1IS  | FEAT_TLBIRANGE          |
|   100 |  1000 |  0001 |   000 | ALLE2OS      | FEAT_TLBIOS             |
|   100 |  1000 |  0001 |   001 | VAE2OS       | FEAT_TLBIOS             |
|   100 |  1000 |  0001 |   100 | ALLE1OS      | FEAT_TLBIOS             |
|   100 |  1000 |  0001 |   101 | VALE2OS      | FEAT_TLBIOS             |
|   100 |  1000 |  0001 |   110 | VMALLS12E1OS | FEAT_TLBIOS             |
|   100 |  1000 |  0010 |   001 | RVAE2IS      | FEAT_TLBIRANGE          |
|   100 |  1000 |  0010 |   010 | VMALLWS2E1IS | FEAT_TLBIW              |
|   100 |  1000 |  0010 |   101 | RVALE2IS     | FEAT_TLBIRANGE          |
|   100 |  1000 |  0011 |   000 | ALLE2IS      | -                       |
|   100 |  1000 |  0011 |   001 | VAE2IS       | -                       |
|   100 |  1000 |  0011 |   100 | ALLE1IS      | -                       |
|   100 |  1000 |  0011 |   101 | VALE2IS      | -                       |
|   100 |  1000 |  0011 |   110 | VMALLS12E1IS | -                       |
|   100 |  1000 |  0100 |   000 | IPAS2E1OS    | FEAT_TLBIOS             |
|   100 |  1000 |  0100 |   001 | IPAS2E1      | -                       |
|   100 |  1000 |  0100 |   010 | RIPAS2E1     | FEAT_TLBIRANGE          |
|   100 |  1000 |  0100 |   011 | RIPAS2E1OS   | FEAT_TLBIRANGE          |
|   100 |  1000 |  0100 |   100 | IPAS2LE1OS   | FEAT_TLBIOS             |
|   100 |  1000 |  0100 |   101 | IPAS2LE1     | -                       |
|   100 |  1000 |  0100 |   110 | RIPAS2LE1    | FEAT_TLBIRANGE          |
|   100 |  1000 |  0100 |   111 | RIPAS2LE1OS  | FEAT_TLBIRANGE          |
|   100 |  1000 |  0101 |   001 | RVAE2OS      | FEAT_TLBIRANGE          |
|   100 |  1000 |  0101 |   010 | VMALLWS2E1OS | FEAT_TLBIW              |
|   100 |  1000 |  0101 |   101 | RVALE2OS     | FEAT_TLBIRANGE          |
|   100 |  1000 |  0110 |   001 | RVAE2        | FEAT_TLBIRANGE          |
|   100 |  1000 |  0110 |   010 | VMALLWS2E1   | FEAT_TLBIW              |
|   100 |  1000 |  0110 |   101 | RVALE2       | FEAT_TLBIRANGE          |
|   100 |  1000 |  0111 |   000 | ALLE2        | -                       |
|   100 |  1000 |  0111 |   001 | VAE2         | -                       |
|   100 |  1000 |  0111 |   100 | ALLE1        | -                       |
|   100 |  1000 |  0111 |   101 | VALE2        | -                       |

| op1   | CRn   | CRm   | op2     | <tlbi_op>                    | Architectural Feature   |
|-------|-------|-------|---------|------------------------------|-------------------------|
| 100   | 1000  | 0111  | 110     | VMALLS12E1                   | -                       |
| 100   | 1001  | 0000  | 001     | IPAS2E1ISNXS                 | FEAT_XS                 |
| 100   | 1001  | 0000  | 010     | RIPAS2E1ISNXS                | FEAT_XS                 |
| 100   | 1001  | 0000  | 101     | IPAS2LE1ISNXS                | FEAT_XS                 |
| 100   | 1001  | 0000  | 110     | RIPAS2LE1ISNXS               | FEAT_XS                 |
| 100   | 1001  | 0001  | 000     | ALLE2OSNXS                   | FEAT_XS                 |
| 100   | 1001  | 0001  | 001     | VAE2OSNXS                    | FEAT_XS                 |
| 100   | 1001  | 0001  | 100     | ALLE1OSNXS                   | FEAT_XS                 |
| 100   | 1001  | 0001  | 101     | VALE2OSNXS                   | FEAT_XS                 |
| 100   | 1001  | 0001  | 110     | VMALLS12E1OSNXS              | FEAT_XS                 |
| 100   | 1001  | 0010  | 001     | RVAE2ISNXS                   | FEAT_XS                 |
| 100   | 1001  | 0010  | 010     | VMALLWS2E1ISNXS              | FEAT_TLBIW              |
| 100   | 1001  | 0010  | 101     | RVALE2ISNXS                  | FEAT_XS                 |
| 100   | 1001  | 0011  | 000     | ALLE2ISNXS                   | FEAT_XS                 |
| 100   | 1001  | 0011  | 001     | VAE2ISNXS                    | FEAT_XS                 |
| 100   | 1001  | 0011  | 100     | ALLE1ISNXS                   | FEAT_XS                 |
| 100   | 1001  | 0011  | 101     | VALE2ISNXS                   | FEAT_XS                 |
| 100   | 1001  | 0011  | 110 000 | VMALLS12E1ISNXS IPAS2E1OSNXS | FEAT_XS FEAT_XS         |
| 100   | 1001  | 0100  | 001     | IPAS2E1NXS                   |                         |
| 100   | 1001  | 0100  |         |                              | FEAT_XS                 |
| 100   | 1001  | 0100  |         | RIPAS2E1OSNXS                | FEAT_XS                 |
|       |       |       | 011 100 | IPAS2LE1OSNXS                |                         |
| 100   | 1001  | 0100  | 101     | IPAS2LE1NXS                  | FEAT_XS                 |
| 100   | 1001  | 0100  |         |                              | FEAT_XS                 |
| 100   | 1001  | 0100  | 110     | RIPAS2LE1NXS                 | FEAT_XS                 |
| 100   | 1001  | 0101  | 001     | RVAE2OSNXS                   | FEAT_XS                 |
| 100   | 1001  | 0101  | 010     | VMALLWS2E1OSNXS              | FEAT_TLBIW              |
| 100   | 1001  | 0101  | 101     | RVALE2OSNXS                  | FEAT_XS                 |
| 100   | 1001  | 0110  | 001     | RVAE2NXS                     | FEAT_XS                 |
| 100   | 1001  | 0110  | 010     | VMALLWS2E1NXS                | FEAT_TLBIW              |
| 100   | 1001  | 0110  | 101     | RVALE2NXS                    | FEAT_XS                 |
| 100   | 1001  | 0111  | 000     | ALLE2NXS                     | FEAT_XS                 |
| 100   | 1001  | 0111  | 001     | VAE2NXS                      | FEAT_XS                 |
| 100   | 1001  | 0111  | 100     | ALLE1NXS                     | FEAT_XS                 |
| 100   | 1001  | 0111  |         |                              | FEAT_XS                 |
| 100   | 1001  | 0111  | 101 110 | VALE2NXS VMALLS12E1NXS       | FEAT_XS                 |
| 110   | 1000  | 0001  | 000     | ALLE3OS                      | FEAT_TLBIOS             |
| 110   | 1000  | 0001  | 001     | VAE3OS                       | FEAT_TLBIOS             |

|   op1 |   CRn |   CRm |   op2 | <tlbi_op>   | Architectural Feature   |
|-------|-------|-------|-------|-------------|-------------------------|
|   110 |  1000 |  0001 |   101 | VALE3OS     | FEAT_TLBIOS             |
|   110 |  1000 |  0010 |   001 | RVAE3IS     | FEAT_TLBIRANGE          |
|   110 |  1000 |  0010 |   101 | RVALE3IS    | FEAT_TLBIRANGE          |
|   110 |  1000 |  0011 |   000 | ALLE3IS     | -                       |
|   110 |  1000 |  0011 |   001 | VAE3IS      | -                       |
|   110 |  1000 |  0011 |   101 | VALE3IS     | -                       |
|   110 |  1000 |  0100 |   011 | RPAOS       | FEAT_RME                |
|   110 |  1000 |  0100 |   111 | RPALOS      | FEAT_RME                |
|   110 |  1000 |  0101 |   001 | RVAE3OS     | FEAT_TLBIRANGE          |
|   110 |  1000 |  0101 |   101 | RVALE3OS    | FEAT_TLBIRANGE          |
|   110 |  1000 |  0110 |   001 | RVAE3       | FEAT_TLBIRANGE          |
|   110 |  1000 |  0110 |   101 | RVALE3      | FEAT_TLBIRANGE          |
|   110 |  1000 |  0111 |   000 | ALLE3       | -                       |
|   110 |  1000 |  0111 |   001 | VAE3        | -                       |
|   110 |  1000 |  0111 |   100 | PAALL       | FEAT_RME                |
|   110 |  1000 |  0111 |   101 | VALE3       | -                       |
|   110 |  1001 |  0001 |   000 | ALLE3OSNXS  | FEAT_XS                 |
|   110 |  1001 |  0001 |   001 | VAE3OSNXS   | FEAT_XS                 |
|   110 |  1001 |  0001 |   101 | VALE3OSNXS  | FEAT_XS                 |
|   110 |  1001 |  0010 |   001 | RVAE3ISNXS  | FEAT_XS                 |
|   110 |  1001 |  0010 |   101 | RVALE3ISNXS | FEAT_XS                 |
|   110 |  1001 |  0011 |   000 | ALLE3ISNXS  | FEAT_XS                 |
|   110 |  1001 |  0011 |   001 | VAE3ISNXS   | FEAT_XS                 |
|   110 |  1001 |  0011 |   101 | VALE3ISNXS  | FEAT_XS                 |
|   110 |  1001 |  0101 |   001 | RVAE3OSNXS  | FEAT_XS                 |
|   110 |  1001 |  0101 |   101 | RVALE3OSNXS | FEAT_XS                 |
|   110 |  1001 |  0110 |   001 | RVAE3NXS    | FEAT_XS                 |
|   110 |  1001 |  0110 |   101 | RVALE3NXS   | FEAT_XS                 |
|   110 |  1001 |  0111 |   000 | ALLE3NXS    | FEAT_XS                 |
|   110 |  1001 |  0111 |   001 | VAE3NXS     | FEAT_XS                 |
|   110 |  1001 |  0111 |   101 | VALE3NXS    | FEAT_XS                 |

## &lt;Xt&gt;

Is the 64-bit name of the optional general-purpose source register, defaulting to '11111', encoded in the 'Rt' field.

## Operation

The description of SYS gives the operational pseudocode for this instruction.
