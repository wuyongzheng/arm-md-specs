## C8.2.236 FMLSLB (indexed)

Half-precision multiply-subtract by indexed element from single-precision (bottom)

This instruction widens the even-numbered half-precision elements in the first source vector and the indexed element from the corresponding 128-bit segment in the second source vector to single-precision format and then destructively multiplies and subtracts these values without intermediate rounding from the single-precision elements of the destination vector that overlap with the corresponding half-precision elements in the first source vector. This instruction is unpredicated.

## Single-precision

## (FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
FMLSLB <Zda>.S, <Zn>.H, <Zm>.H[<imm>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda); constant integer index = UInt(i3h:i3l); constant boolean op1_neg = TRUE;
```

## Assembler Symbols

## &lt;Zda&gt;

Is the name of the third source and destination scalable vector register, encoded in the 'Zda' field.

## &lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register Z0-Z7, encoded in the 'Zm' field.

## &lt;imm&gt;

Is the immediate index, in the range 0 to 7, encoded in the 'i3h:i3l' fields.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant integer eltspersegment = 128 constant bits(VL) op1 = Z[n, VL]; constant bits(VL) op2 = Z[m, VL]; constant bits(VL) op3 = Z[da, VL];
```

```
DIV esize; bits(VL) result;
```

```
for e = 0 to elements-1 constant integer segmentbase = e - (e MOD eltspersegment); constant integer s = 2 * segmentbase + index; constant bits(esize DIV 2) elem1 = (if op1_neg then FPNeg(Elem[op1, 2*e + 0, esize DIV 2], FPCR) else Elem[op1, 2*e + 0, esize DIV 2]); constant bits(esize DIV 2) elem2 = Elem[op2, s, esize DIV 2]; constant bits(esize) elem3 = Elem[op3, e, esize]; Elem[result, e, esize] = FPMulAddH(elem3, elem1, elem2, FPCR); Z[da, VL] = result;
```

## Operational Information

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.