## C8.2.936 ZIP1, ZIP2 (vectors)

Interleave elements from two half vectors

This instruction interleaves alternating elements from the lowest or highest halves of the first and second source vectors and places in elements of the destination vector. This instruction is unpredicated.

The 128-bit element variant requires that the Effective SVE vector length is at least 256 bits. ID\_AA64ZFR0\_EL1.F64MM indicates whether the 128-bit element variant is implemented. The 128-bit element variant is illegal when executed in Streaming SVE mode, unless FEAT\_SME\_FA64 is implemented and enabled.

It has encodings from 4 classes: High halves, High halves (quadwords), Low halves, and Low halves (quadwords)

## High halves

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
ZIP2 <Zd>.<T>, <Zn>.<T>, <Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd); constant integer part = 1;
```

## High halves (quadwords)

(FEAT\_F64MM)

<!-- image -->

## Encoding

```
ZIP2 <Zd>.Q, <Zn>.Q, <Zm>.Q
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_F64MM) then constant integer esize = 128; constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd); constant integer part = 1;
```

```
EndOfDecode(Decode_UNDEF);
```

## Low halves

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
ZIP1 <Zd>.<T>, <Zn>.<T>, <Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd); constant integer part = 0;
```

## Low halves (quadwords)

(FEAT\_F64MM)

<!-- image -->

## Encoding

```
ZIP1 <Zd>.Q, <Zn>.Q, <Zm>.Q
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_F64MM) then EndOfDecode(Decode_UNDEF); constant integer esize = 128; constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd); constant integer part = 0;
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

## &lt;T&gt;

## &lt;Zn&gt;

Is the size specifier, encoded in 'size':

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
if esize < 128 then CheckSVEEnabled(); else CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; if VL < esize * 2 then EndOfDecode(Decode_UNDEF); constant integer pairs = VL DIV (esize * 2); constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result = Zeros(VL); constant integer base = part * pairs; for p = 0 to pairs-1 Elem[result, 2*p+0, esize] = Elem[operand1, base+p, esize]; Elem[result, 2*p+1, esize] = Elem[operand2, base+p, esize]; Z[d, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.