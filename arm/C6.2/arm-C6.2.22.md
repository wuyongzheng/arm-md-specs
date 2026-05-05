## C6.2.22 AT

## Address translate

For more information, see op0== 0b01 , cache maintenance, TLB maintenance, and address translation instructions.

This is an alias of SYS. This means:

- The encodings in this description are named to match the encodings of SYS.
- The description of SYS gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding

AT

&lt;at\_op&gt;,

&lt;Xt&gt;

## is equivalent to

```
SYS #<op1>, C7, <Cm>, #<op2>, <Xt>
```

and is the preferred disassembly when SysOp(op1, '0111', CRm, op2) == Sys\_AT .

## Assembler Symbols

## &lt;at\_op&gt;

Is an AT operation name, as listed for the AT system instruction group, encoded in 'op1:CRm:op2':

|   op1 |   CRm |   op2 | <at_op>   | Architectural Feature   |
|-------|-------|-------|-----------|-------------------------|
|   000 |  1000 |   000 | S1E1R     | -                       |
|   000 |  1000 |   001 | S1E1W     | -                       |
|   000 |  1000 |   010 | S1E0R     | -                       |
|   000 |  1000 |   011 | S1E0W     | -                       |
|   000 |  1001 |   000 | S1E1RP    | FEAT_PAN2               |
|   000 |  1001 |   001 | S1E1WP    | FEAT_PAN2               |
|   000 |  1001 |   010 | S1E1A     | FEAT_ATS1A              |
|   100 |  1000 |   000 | S1E2R     | -                       |
|   100 |  1000 |   001 | S1E2W     | -                       |
|   100 |  1000 |   100 | S12E1R    | -                       |
|   100 |  1000 |   101 | S12E1W    | -                       |
|   100 |  1000 |   110 | S12E0R    | -                       |
|   100 |  1000 |   111 | S12E0W    | -                       |
|   100 |  1001 |   010 | S1E2A     | FEAT_ATS1A              |
|   110 |  1000 |   000 | S1E3R     | -                       |

|   op1 |   CRm |   op2 | <at_op>   | Architectural Feature   |
|-------|-------|-------|-----------|-------------------------|
|   110 |  1000 |   001 | S1E3W     | -                       |
|   110 |  1001 |   010 | S1E3A     | FEAT_ATS1A              |

<!-- image -->

&lt;Xt&gt;

Is the 64-bit name of the general-purpose source register, encoded in the 'Rt' field.

## Operation

The description of SYS gives the operational pseudocode for this instruction.
