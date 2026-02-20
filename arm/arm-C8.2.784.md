## C8.2.784 SUBPT (unpredicated)

Subtract checked pointer vectors (unpredicated)

This instruction subtracts, with pointer check, all elements of the second source vector from corresponding elements of the first source vector and places the results in the corresponding elements of the destination vector. This instruction is unpredicated.

This instruction is illegal when executed in Streaming SVE mode, unless FEAT\_SME\_FA64 is implemented and enabled.

## SVE2

(FEAT\_SVE &amp;&amp; FEAT\_CPA)

<!-- image -->

## Encoding

```
SUBPT <Zd>.D, <Zn>.D, <Zm>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) || !IsFeatureImplemented(FEAT_CPA) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd);
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
CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV 64; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result; for e = 0 to elements-1 constant bits(64) element1 = Elem[operand1, e, 64]; constant bits(64) element2 = Elem[operand2, e, 64]; constant bits(64) res = element1 -element2; Elem[result, e, 64] = PointerAddCheck(res, element1); Z[d, VL] = result;
```