## C9.2.195 SCLAMP

Multi-vector signed clamp to minimum/maximum

This instruction clamps each signed element in the two or four destination vectors to between the signed minimum value in the corresponding element of the first source vector and the signed maximum value in the corresponding element of the second source vector and destructively places the clamped results in the corresponding elements of the two or four destination vectors.

This instruction is unpredicated.

It has encodings from 2 classes: Two registers and Four registers

```
Two registers (FEAT_SME2)
```

<!-- image -->

## Encoding

```
SCLAMP { <Zd1>.<T>-<Zd2>.<T> }, <Zn>.<T>, <Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd:'0'); constant integer nreg = 2;
```

## Four registers

(FEAT\_SME2)

<!-- image -->

## Encoding

```
SCLAMP { <Zd1>.<T>-<Zd4>.<T> }, <Zn>.<T>, <Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd:'00'); constant integer nreg = 4;
```

```
EndOfDecode(Decode_UNDEF);
```

U

U

## Assembler Symbols

## &lt;Zd1&gt;

For the 'Two registers' variant: is the name of the first scalable vector register of the destination multi-vector group, encoded as 'Zd' times 2.

For the 'Four registers' variant: is the name of the first scalable vector register of the destination multi-vector group, encoded as 'Zd' times 4.

Is the size specifier, encoded in 'size':

## &lt;Zd2&gt;

Is the name of the second scalable vector register of the destination multi-vector group, encoded as 'Zd' times 2 plus 1.

## &lt;Zn&gt;

## &lt;T&gt;

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## &lt;Zd4&gt;

Is the name of the fourth scalable vector register of the destination multi-vector group, encoded as 'Zd' times 4 plus 3.

## Operation

```
CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; array [0..3] of bits(VL) results; for r = 0 to nreg-1 constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; constant bits(VL) operand3 = Z[d+r, VL]; for e = 0 to elements-1 constant integer element1 = SInt(Elem[operand1, e, esize]); constant integer element2 = SInt(Elem[operand2, e, esize]); constant integer element3 = SInt(Elem[operand3, e, esize]); constant integer res = Min(Max(element1, element3), element2); Elem[results[r], e, esize] = res<esize-1:0>; for r = 0 to nreg-1 Z[d+r, VL] = results[r];
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.