## C8.2.129 DUP (scalar)

Broadcast general-purpose register to vector elements (unpredicated)

This instruction unconditionally broadcasts the general-purpose scalar source register into each element of the destination vector. This instruction is unpredicated.

This instruction is used by the alias MOV (scalar, unpredicated).

```
SVE
```

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
DUP <Zd>.<T>, <R><n|SP>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Rn); constant integer d = UInt(Zd);
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

Is a width specifier, encoded in 'size':

&lt;T&gt;

<!-- image -->

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

|   size | <R>   |
|--------|-------|
|     00 | W     |

## &lt;n|SP&gt;

Is the number [0-30] of the general-purpose source register or the name SP (31), encoded in the 'Rn' field.

## Alias Conditions

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; bits(64) operand; if n == 31 then operand = SP[64]; else operand = X[n, 64]; bits(VL) result; for e = 0 to elements-1 Elem[result, e, esize] = operand<esize-1:0>; Z[d, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

|   size | <R>   |
|--------|-------|
|     01 | W     |
|     10 | W     |
|     11 | X     |

| Alias                      | Is preferred when   |
|----------------------------|---------------------|
| MOV (scalar, unpredicated) | Unconditionally     |