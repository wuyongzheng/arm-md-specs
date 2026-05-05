## C6.2.82 CCMP (register)

## Conditional compare (register)

This instruction sets the value of the condition flags to the result of the comparison of two registers if the condition is TRUE, and an immediate value otherwise.

<!-- image -->

## Encoding for the 32-bit variant

Applies when (sf ==

```
<cond>
```

```
0) CCMP <Wn>, <Wm>, #<nzcv>,
```

## Encoding for the 64-bit variant

Applies when (sf ==

```
1)
```

```
CCMP <Xn>, <Xm>, #<nzcv>, <cond>
```

## Decode for all variants of this encoding

```
constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer datasize = 32 << constant bits(4) condition = cond; bits(4) flags = nzcv;
```

## Assembler Symbols

## &lt;Wn&gt;

Is the 32-bit name of the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Wm&gt;

Is the 32-bit name of the second general-purpose source register, encoded in the 'Rm' field.

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
UInt(sf);
```

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

Is the 64-bit name of the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Xm&gt;

Is the 64-bit name of the second general-purpose source register, encoded in the 'Rm' field.

## Operation

```
if ConditionHolds(condition) then constant bits(datasize) operand1 = X[n, datasize]; constant bits(datasize) operand2 = X[m, datasize]; (-, flags) = AddWithCarry(operand1, NOT(operand2), PSTATE.<N,Z,C,V> = flags;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
'1');
```
