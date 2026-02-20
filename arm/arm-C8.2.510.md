## C8.2.510 PMULL

Multi-vector polynomial multiply long

This instruction performs a polynomial multiplication over [0, 1] of the corresponding even-numbered elements of the first and second source vectors, and places the results in the overlapping double-width elements of the first destination vector. The same operation is performed with odd-numbered elements of the source vectors, writing to the second destination vector. This instruction is unpredicated.

This instruction is legal when executed in Streaming SVE mode if both FEAT\_SSVE\_AES and FEAT\_SVE\_AES2 are implemented.

## SVE2

(FEAT\_SVE\_AES2)

<!-- image -->

## Encoding

```
PMULL { <Zd1>.Q-<Zd2>.Q }, <Zn>.D, <Zm>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE_AES2) then EndOfDecode(Decode_UNDEF);
```

```
constant integer esize = 128; constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd:'0');
```

## Assembler Symbols

## &lt;Zd1&gt;

Is the name of the first scalable vector register of the destination multi-vector group, encoded as 'Zd' times 2.

## &lt;Zd2&gt;

Is the name of the second scalable vector register of the destination multi-vector group, encoded as 'Zd' times 2 plus 1.

## &lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
if IsFeatureImplemented(FEAT_SSVE_AES) then CheckSVEEnabled(); else CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result_lo;
```

```
bits(VL) result_hi; for e = 0 to elements-1 constant bits(esize DIV 2) element1_lo = Elem[operand1, 2*e + 0, esize constant bits(esize DIV 2) element2_lo = Elem[operand2, 2*e + 0, esize constant bits(esize DIV 2) element1_hi = Elem[operand1, 2*e + 1, esize constant bits(esize DIV 2) element2_hi = Elem[operand2, 2*e + 1, esize Elem[result_lo, e, esize] = PolynomialMult(element1_lo, element2_lo); Elem[result_hi, e, esize] = PolynomialMult(element1_hi, element2_hi); Z[d + 0, VL] = result_lo; Z[d + 1, VL] = result_hi;
```

```
DIV 2]; DIV 2]; DIV 2]; DIV 2];
```