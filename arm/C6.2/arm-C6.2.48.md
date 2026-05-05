## C6.2.48 BRB

Branch record buffer

For more information, see op0== 0b01 , cache maintenance, TLB maintenance, and address translation instructions.

This is an alias of SYS. This means:

- The encodings in this description are named to match the encodings of SYS.
- The description of SYS gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## System

## (FEAT\_BRBE)

<!-- image -->

## Encoding

BRB

&lt;brb\_op&gt;

## is equivalent to

```
SYS #<op1>, <Cn>, <Cm>, #<op2>{, <Xt>}
```

and is the preferred disassembly when SysOp('001', '0111', '0010', op2) == Sys\_BRB .

## Assembler Symbols

## &lt;brb\_op&gt;

Is a BRB operation name, as listed for the BRB system instruction group, encoded in 'op2':

|   op2 | <brb_op>   | Architectural Feature   |
|-------|------------|-------------------------|
|   100 | IALL       | FEAT_BRBE               |
|   101 | INJ        | FEAT_BRBE               |

## Operation

The description of SYS gives the operational pseudocode for this instruction.
