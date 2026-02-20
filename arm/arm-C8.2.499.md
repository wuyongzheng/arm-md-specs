## C8.2.499 ORR (vectors, unpredicated)

Bitwise inclusive OR (unpredicated)

This instruction performs a bitwise inclusive OR on all elements of the second source vector with the corresponding elements of the first source vector and places the first in the corresponding elements of the destination vector. This instruction is unpredicated.

This instruction is used by the alias MOV (vector, unpredicated).

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
ORR <Zd>.D, <Zn>.D, <Zm>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd);
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

<!-- image -->

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

&lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Alias Conditions

## Operation

```
Z[n, VL]; Z[m, VL];
```

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant bits(VL) operand1 = constant bits(VL) operand2 = Z[d, VL] = operand1 OR operand2;
```

| Alias                      | Is preferred when   |
|----------------------------|---------------------|
| MOV (vector, unpredicated) | Zn == Zm            |

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.