## C6.2.145 DC

Data cache operation

For more information, see op0== 0b01 , cache maintenance, TLB maintenance, and address translation instructions.

This is an alias of SYS. This means:

- The encodings in this description are named to match the encodings of SYS.
- The description of SYS gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding

<!-- image -->

## is equivalent to

```
SYS #<op1>, C7, <Cm>, #<op2>, <Xt>
```

and is the preferred disassembly when SysOp(op1, '0111', CRm, op2) == Sys\_DC .

## Assembler Symbols

## &lt;dc\_op&gt;

Is a DC operation name, as listed for the DC system instruction group, encoded in 'op1:CRm:op2':

|   op1 |   CRm |   op2 | <dc_op>   | Architectural Feature   |
|-------|-------|-------|-----------|-------------------------|
|   000 |  0110 |   001 | IVAC      | -                       |
|   000 |  0110 |   010 | ISW       | -                       |
|   000 |  0110 |   011 | IGVAC     | FEAT_MTE2               |
|   000 |  0110 |   100 | IGSW      | FEAT_MTE2               |
|   000 |  0110 |   101 | IGDVAC    | FEAT_MTE2               |
|   000 |  0110 |   110 | IGDSW     | FEAT_MTE2               |
|   000 |  1010 |   010 | CSW       | -                       |
|   000 |  1010 |   100 | CGSW      | FEAT_MTE2               |
|   000 |  1010 |   110 | CGDSW     | FEAT_MTE2               |
|   000 |  1110 |   010 | CISW      | -                       |
|   000 |  1110 |   100 | CIGSW     | FEAT_MTE2               |
|   000 |  1110 |   110 | CIGDSW    | FEAT_MTE2               |
|   000 |  1111 |   001 | CIVAPS    | FEAT_PoPS               |
|   000 |  1111 |   101 | CIGDVAPS  | FEAT_PoPS && FEAT_MTE2  |
|   011 |  0100 |   001 | ZVA       | -                       |

|   op1 |   CRm |   op2 | <dc_op>   | Architectural Feature   |
|-------|-------|-------|-----------|-------------------------|
|   011 |  0100 |   011 | GVA       | FEAT_MTE                |
|   011 |  0100 |   100 | GZVA      | FEAT_MTE                |
|   011 |  1010 |   001 | CVAC      | -                       |
|   011 |  1010 |   011 | CGVAC     | FEAT_MTE                |
|   011 |  1010 |   101 | CGDVAC    | FEAT_MTE                |
|   011 |  1011 |   000 | CVAOC     | FEAT_OCCMO              |
|   011 |  1011 |   001 | CVAU      | -                       |
|   011 |  1011 |   111 | CGDVAOC   | FEAT_OCCMO && FEAT_MTE  |
|   011 |  1100 |   001 | CVAP      | FEAT_DPB                |
|   011 |  1100 |   011 | CGVAP     | FEAT_MTE                |
|   011 |  1100 |   101 | CGDVAP    | FEAT_MTE                |
|   011 |  1101 |   001 | CVADP     | FEAT_DPB2               |
|   011 |  1101 |   011 | CGVADP    | FEAT_MTE                |
|   011 |  1101 |   101 | CGDVADP   | FEAT_MTE                |
|   011 |  1110 |   001 | CIVAC     | -                       |
|   011 |  1110 |   011 | CIGVAC    | FEAT_MTE                |
|   011 |  1110 |   101 | CIGDVAC   | FEAT_MTE                |
|   011 |  1111 |   000 | CIVAOC    | FEAT_OCCMO              |
|   011 |  1111 |   111 | CIGDVAOC  | FEAT_OCCMO && FEAT_MTE  |
|   100 |  1110 |   000 | CIPAE     | FEAT_MEC                |
|   100 |  1110 |   111 | CIGDPAE   | FEAT_MEC && FEAT_MTE2   |
|   110 |  1110 |   001 | CIPAPA    | FEAT_RME                |
|   110 |  1110 |   101 | CIGDPAPA  | FEAT_RME && FEAT_MTE2   |

<!-- image -->

Is the 64-bit name of the general-purpose source register, encoded in the 'Rt' field.

## Operation

The description of SYS gives the operational pseudocode for this instruction.
