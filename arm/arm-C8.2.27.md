## C8.2.27 AND (vectors, unpredicated)

Bitwise AND (unpredicated)

This instruction performs a bitwise AND on all elements of the second source vector with the corresponding elements of the first source vector and places the results in the corresponding elements of the destination vector. This instruction is unpredicated.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
AND <Zd>.D, <Zn>.D, <Zm>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd);
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

## &lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; Z[d, VL] = operand1 AND operand2;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.