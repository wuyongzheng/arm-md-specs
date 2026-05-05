## C6.2.142 CSINV

## Conditional select invert

This instruction returns, in the destination register, the value of the first source register if the condition is TRUE, and otherwise returns the bitwise inversion value of the second source register.

This instruction is used by the aliases CINV and CSETM.

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (sf == 0) CSINV <Wd>, <Wn>, <Wm>,
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
CSINV <Xd>, <Xn>, <Xm>, <cond>
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

## &lt;Xd&gt;

## &lt;Xn&gt;

Is the 64-bit name of the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Xm&gt;

Is the 64-bit name of the second general-purpose source register, encoded in the 'Rm' field.

## Alias Conditions

| Alias   | Is preferred when                                                 |
|---------|-------------------------------------------------------------------|
| CINV    | Rm != '11111' && Rn != '11111' && !(cond IN {'111x'}) && Rn == Rm |
| CSETM   | Rm == '11111' && Rn == '11111' && !(cond IN {'111x'})             |

## Operation

```
bits(datasize) result; if ConditionHolds(condition) then result = X[n, datasize]; else result = NOT(X[m, datasize]); X[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

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

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.
