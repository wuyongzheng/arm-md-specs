## C8.2.509 PMUL

Polynomial multiply (unpredicated)

This instruction performs a polynomial multiplication over [0, 1] of all elements of the second source vector to the corresponding elements of the first source vector and places the results in the corresponding elements of the destination vector. This instruction is unpredicated.

## SVE2

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
PMUL <Zd>.B, <Zn>.B, <Zm>.B
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8; constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd);
```

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

## &lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result; for e = 0 to elements-1 constant bits(esize) element1 = Elem[operand1, e, esize]; constant bits(esize) element2 = Elem[operand2, e, esize]; Elem[result, e, esize] = PolynomialMult(element1, element2)<esize-1:0>; Z[d, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.