## C6.2.175 IC

Instruction cache operation

For more information, see op0== 0b01 , cache maintenance, TLB maintenance, and address translation instructions.

This is an alias of SYS. This means:

- The encodings in this description are named to match the encodings of SYS.
- The description of SYS gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding

```
IC <ic_op>{, <Xt>}
```

## is equivalent to

```
SYS #<op1>, C7, <Cm>, #<op2>{, <Xt>}
```

and is the preferred disassembly when SysOp(op1, '0111', CRm, op2) == Sys\_IC .

## Assembler Symbols

## &lt;ic\_op&gt;

Is an IC operation name, as listed for the IC system instruction pages, encoded in 'op1:CRm:op2':

|   op1 |   CRm |   op2 | <ic_op>   |
|-------|-------|-------|-----------|
|   000 |  0001 |   000 | IALLUIS   |
|   000 |  0101 |   000 | IALLU     |
|   011 |  0101 |   001 | IVAU      |

<!-- image -->

Is the 64-bit name of the optional general-purpose source register, defaulting to '11111', encoded in the 'Rt' field.

## Operation

The description of SYS gives the operational pseudocode for this instruction.
