## C6.2.138 CSEL

## Conditional select

This instruction writes the value of the first source register to the destination register if the condition is TRUE. If the condition is FALSE, it writes the value of the second source register to the destination register.

<!-- image -->

## Encoding for the 32-bit variant

Applies when (sf ==

```
<cond>
```

```
0) CSEL <Wd>, <Wn>, <Wm>,
```

## Encoding for the 64-bit variant

Applies when (sf ==

```
1)
```

```
CSEL <Xd>, <Xn>, <Xm>, <cond>
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer datasize = 32 << UInt(sf); constant bits(4) condition = cond;
```

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Wn&gt;

Is the 32-bit name of the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Wm&gt;

Is the 32-bit name of the second general-purpose source register, encoded in the 'Rm' field.

## &lt;cond&gt;

Is one of the standard conditions, encoded in the standard way, and encoded in 'cond':

|   cond | <cond>   |
|--------|----------|
|   0000 | EQ       |
|   0001 | NE       |
|   0010 | CS       |
|   0011 | CC       |

## &lt;Xd&gt;

## &lt;Xn&gt;

Is the 64-bit name of the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Xm&gt;

Is the 64-bit name of the second general-purpose source register, encoded in the 'Rm' field.

## Operation

```
bits(datasize) result; if ConditionHolds(condition) then result = X[n, datasize]; else result = X[m, datasize]; X[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

|   cond | <cond>   |
|--------|----------|
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

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.
