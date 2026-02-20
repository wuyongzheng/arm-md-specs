## C8.2.796 TRN1, TRN2 (vectors)

Interleave even or odd elements from two vectors

This instruction interleaves alternating even or odd-numbered elements from the first and second source vectors and places in elements of the destination vector. This instruction is unpredicated.

The 128-bit element variant requires that the Effective SVE vector length is at least 256 bits. ID\_AA64ZFR0\_EL1.F64MM indicates whether the 128-bit element variant is implemented. The 128-bit element variant is illegal when executed in Streaming SVE mode, unless FEAT\_SME\_FA64 is implemented and enabled.

It has encodings from 4 classes: Even, Even (quadwords), Odd, and Odd (quadwords)

## Even

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
TRN1 <Zd>.<T>, <Zn>.<T>, <Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd); constant integer part = 0;
```

## Even (quadwords)

(FEAT\_F64MM)

<!-- image -->

## Encoding

```
TRN1 <Zd>.Q, <Zn>.Q, <Zm>.Q
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_F64MM) then constant integer esize = 128; constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd); constant integer part = 0;
```

```
EndOfDecode(Decode_UNDEF);
```

## Odd

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
TRN2 <Zd>.<T>, <Zn>.<T>, <Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd); constant integer part = 1;
```

## Odd (quadwords)

(FEAT\_F64MM)

<!-- image -->

## Encoding

```
TRN2 <Zd>.Q, <Zn>.Q, <Zm>.Q
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_F64MM) then EndOfDecode(Decode_UNDEF); constant integer esize = 128; constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd); constant integer part = 1;
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
if esize < 128 then CheckSVEEnabled(); else CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; if VL < esize * 2 then EndOfDecode(Decode_UNDEF); constant integer pairs = VL DIV (esize * 2); constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result = Zeros(VL); for p = 0 to pairs-1 Elem[result, 2*p+0, esize] = Elem[operand1, 2*p+part, esize]; Elem[result, 2*p+1, esize] = Elem[operand2, 2*p+part, esize]; Z[d, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.