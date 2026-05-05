## C6.2.79 CCMN (immediate)

Conditional compare negative (immediate)

This instruction sets the value of the condition flags to the result of the comparison of a register value and a negated immediate value if the condition is TRUE, and an immediate value otherwise.

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (sf == 0) CCMN <Wn>, #<imm>, #<nzcv>,
```

```
<cond>
```

## Encoding for the 64-bit variant

Applies when (sf ==

```
1)
```

```
CCMN <Xn>, #<imm>, #<nzcv>, <cond>
```

## Decode for all variants of this encoding

```
constant integer n = UInt(Rn); constant integer datasize = 32 << UInt(sf); constant bits(4) condition = cond; bits(4) flags = nzcv; constant bits(datasize) imm = ZeroExtend(imm5,
```

## Assembler Symbols

## &lt;Wn&gt;

Is the 32-bit name of the general-purpose source register, encoded in the 'Rn' field.

## &lt;imm&gt;

Is a five bit unsigned (positive) immediate encoded in the 'imm5' field.

## &lt;nzcv&gt;

Is the flag bit specifier, an immediate in the range 0 to 15, giving the alternative state for the 4-bit NZCV condition flags, encoded in the 'nzcv' field.

## &lt;cond&gt;

Is one of the standard conditions, encoded in the standard way, and encoded in 'cond':

|   cond | <cond>   |
|--------|----------|
|   0000 | EQ       |
|   0001 | NE       |
|   0010 | CS       |

```
datasize);
```

<!-- image -->

## &lt;Xn&gt;

|   cond | <cond>   |
|--------|----------|
|   0011 | CC       |
|   0100 | MI       |
|   0101 | PL       |
|   0110 | VS       |
|   0111 | VC       |
|   1000 | HI       |
|   1001 | LS       |
|   1010 | GE       |
|   1011 | LT       |
|   1100 | GT       |
|   1101 | LE       |
|   1110 | AL       |
|   1111 | NV       |

Is the 64-bit name of the general-purpose source register, encoded in the 'Rn' field.

## Operation

```
if ConditionHolds(condition) then constant bits(datasize) operand1 = X[n, datasize]; constant bits(datasize) operand2 = imm; (-, flags) = AddWithCarry(operand1, operand2, '0'); PSTATE.<N,Z,C,V> = flags;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
