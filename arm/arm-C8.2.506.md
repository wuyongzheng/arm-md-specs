## C8.2.506 PMLAL

Multi-vector polynomial multiply long and accumulate

This instruction performs a polynomial multiplication over [0, 1] of the corresponding even-numbered elements of the first and second source vectors, and a bitwise exclusive-OR on the result with the overlapping double-width elements of the first destination vector. The same operation is performed with odd-numbered elements of the source vectors, writing to the second destination vector. This instruction is unpredicated.

This instruction is legal when executed in Streaming SVE mode if both FEAT\_SSVE\_AES and FEAT\_SVE\_AES2 are implemented.

## SVE2

(FEAT\_SVE\_AES2)

<!-- image -->

## Encoding

```
PMLAL { <Zda1>.Q-<Zda2>.Q }, <Zn>.D, <Zm>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE_AES2) then EndOfDecode(Decode_UNDEF);
```

```
constant integer esize = 128; constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda:'0');
```

## Assembler Symbols

## &lt;Zda1&gt;

Is the name of the first scalable vector register of the destination multi-vector group, encoded as 'Zda' times 2.

## &lt;Zda2&gt;

Is the name of the second scalable vector register of the destination multi-vector group, encoded as 'Zda' times 2 plus 1.

## &lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
if IsFeatureImplemented(FEAT_SSVE_AES) then CheckSVEEnabled(); else CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result_lo = Z[da + 0, VL];
```

```
bits(VL) result_hi = Z[da + 1, VL]; for e = 0 to elements-1 constant bits(esize DIV 2) element1_lo = Elem[operand1, 2*e + 0, esize DIV 2]; constant bits(esize DIV 2) element2_lo = Elem[operand2, 2*e + 0, esize DIV 2]; constant bits(esize DIV 2) element1_hi = Elem[operand1, 2*e + 1, esize DIV 2]; constant bits(esize DIV 2) element2_hi = Elem[operand2, 2*e + 1, esize DIV 2]; constant bits(esize) product_lo = PolynomialMult(element1_lo, element2_lo); constant bits(esize) product_hi = PolynomialMult(element1_hi, element2_hi); Elem[result_lo, e, esize] = Elem[result_lo, e, esize] EOR product_lo; Elem[result_hi, e, esize] = Elem[result_hi, e, esize] EOR product_hi; Z[da + 0, VL] = result_lo; Z[da + 1, VL] = result_hi;
```