## C8.2.279 HISTSEG

Count matching elements in vector segments

This instruction compares each 8-bit byte element of the first source vector with all of the elements in the corresponding 128-bit segment of the second source vector and places the count of matching elements in the corresponding element of the destination vector. This instruction is unpredicated.

This instruction is illegal when executed in Streaming SVE mode, unless FEAT\_SME\_FA64 is implemented and enabled.

```
SVE2 (FEAT_SVE2)
```

<!-- image -->

## Encoding

```
HISTSEG <Zd>.B, <Zn>.B, <Zm>.B
```

## Decode for this encoding

```
EndOfDecode(Decode_UNDEF);
```

```
if !IsFeatureImplemented(FEAT_SVE2) then if size != '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8; constant integer d = UInt(Zd); constant integer n = UInt(Zn); constant integer m = UInt(Zm);
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

&lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer segments = VL DIV 128; constant integer eltspersegment = 128 DIV esize; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result; for b = 0 to segments-1 for s = 0 to eltspersegment-1 integer count = 0; constant integer e = eltspersegment * b + s; constant bits(esize) element1 = Elem[operand1, e, for i = 0 to eltspersegment-1 constant integer e2 = eltspersegment * b + i;
```

```
esize];
```

```
constant bits(esize) element2 = Elem[operand2, e2, esize]; if element1 == element2 then count = count + 1; Elem[result, e, esize] = count<esize-1:0>; Z[d, VL] = result;
```