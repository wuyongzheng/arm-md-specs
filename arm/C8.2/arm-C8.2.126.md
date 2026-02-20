## C8.2.126 DECP (scalar)

Decrement scalar by count of true predicate elements

This instruction counts the number of true elements in the source predicate and then uses the result to decrement the scalar destination.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
DECP <Xdn>, <Pm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer m = UInt(Pm); constant integer dn = UInt(Rdn);
```

## Assembler Symbols

## &lt;Xdn&gt;

Is the 64-bit name of the source and destination general-purpose register, encoded in the 'Rdn' field.

## &lt;Pm&gt;

Is the name of the source scalable predicate register, encoded in the 'Pm' field.

<!-- image -->

Is the size specifier, encoded in 'size':

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(64) operand1 = X[dn, 64]; constant bits(PL) operand2 = P[m, PL]; integer count = 0; for e = 0 to elements-1 if ActivePredicateElement(operand2, e, esize) count = count + 1; X[dn, 64] = operand1 - count;
```

## Operational Information

If FEAT\_SME is implemented and the PE is in Streaming SVE mode, then any subsequent instruction which is dependent on the general-purpose register written by this instruction might be significantly delayed.

```
then
```