## C7.2.157 FMOV (general)

Floating-point move to or from general-purpose register without conversion

This instruction transfers the contents of a SIMD&amp;FP register to a general-purpose register, or the contents of a general-purpose register to a SIMD&amp;FP register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

<!-- image -->

## Encoding for the Half-precision to 32-bit variant

```
(FEAT_FP16) Applies when (sf == 0 && ftype == 11 && rmode == 00 && opcode == 110)
```

```
FMOV <Wd>, <Hn>
```

## Encoding for the Half-precision to 64-bit variant

```
(FEAT_FP16) Applies when (sf == 1 && ftype == 11 && rmode == 00 && opcode == 110)
```

```
FMOV <Xd>, <Hn>
```

## Encoding for the 32-bit to half-precision variant

```
(FEAT_FP16) Applies when (sf == 0 && ftype == 11 && rmode == 00 && opcode == 111)
```

```
FMOV <Hd>, <Wn>
```

## Encoding for the 32-bit to single-precision variant

```
(FEAT_FP) Applies when (sf == 0 && ftype == 00 && rmode == 00 && opcode == 111)
```

```
FMOV <Sd>, <Wn>
```

## Encoding for the Single-precision to 32-bit variant

```
(FEAT_FP) Applies when (sf == 0 && ftype == 00 && rmode == 00 && opcode == 110)
```

```
FMOV <Wd>, <Sn>
```

## Encoding for the 64-bit to half-precision variant

```
(FEAT_FP16) Applies when (sf == 1 && ftype == 11 && rmode == 00 && opcode == 111)
```

```
FMOV <Hd>, <Xn>
```

## Encoding for the 64-bit to double-precision variant

```
(FEAT_FP) Applies when (sf == 1 && ftype == 01 && rmode == 00 && opcode == 111)
```

```
FMOV <Dd>, <Xn>
```

## Encoding for the 64-bit to top half of 128-bit variant

```
(FEAT_FP) Applies when (sf == 1 && ftype == 10 && rmode == 01 && opcode == 111)
```

```
FMOV <Vd>.D[1], <Xn>
```

## Encoding for the Double-precision to 64-bit variant

```
(FEAT_FP) Applies when (sf == 1 && ftype == 01 && rmode == 00 && opcode == 110)
```

```
FMOV <Xd>, <Dn>
```

## Encoding for the Top half of 128-bit to 64-bit variant

```
(FEAT_FP) Applies when (sf == 1 && ftype == 10 && rmode == 01 && opcode == 110)
```

```
FMOV <Xd>, <Vn>.D[1]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_FP) then EndOfDecode(Decode_UNDEF); if ftype == '10' && opcode<2:1>:rmode != '11 01' then EndOfDecode(Decode_UNDEF); if ftype == '11' && !IsFeatureImplemented(FEAT_FP16) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer intsize = 32 << UInt(sf); constant integer fltsize = if ftype == '10' then 64 else (8 << UInt(ftype EOR '10')); constant integer part = UInt(rmode<0>); FPConvOp op; case opcode<2:1>:rmode of when '11 00' // FMOV if fltsize != 16 && fltsize != intsize then EndOfDecode(Decode_UNDEF); op = if opcode<0> == '1' then FPConvOp_MOV_ItoF else FPConvOp_MOV_FtoI; when '11 01' // FMOV D[1] if intsize != 64 || ftype != '10' then EndOfDecode(Decode_UNDEF); op = if opcode<0> == '1' then FPConvOp_MOV_ItoF else FPConvOp_MOV_FtoI; otherwise Unreachable();
```

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Hn&gt;

- &lt;Xd&gt;
- &lt;Hd&gt;

Is the 16-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

## &lt;Wn&gt;

Is the 32-bit name of the general-purpose source register, encoded in the 'Rn' field.

Is the 16-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Sd&gt;

&lt;Sn&gt;

&lt;Xn&gt;

&lt;Dd&gt;

&lt;Vd&gt;

## &lt;Dn&gt;

&lt;Vn&gt;

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPEnabled(); bits(fltsize) fltval; bits(intsize) intval; case op of when FPConvOp_MOV_FtoI fltval = Vpart[n, part, fltsize]; X[d, intsize] = ZeroExtend(fltval, intsize); when FPConvOp_MOV_ItoF intval = X[n, intsize]; Vpart[d, part, fltsize] = intval<fltsize-1:0>; otherwise Unreachable();
```

## Operational Information

If FEAT\_SME is implemented and the PE is in Streaming SVE mode, then any subsequent instruction which is dependent on the general-purpose register written by this instruction might be significantly delayed.

Is the 32-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the 32-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

Is the 64-bit name of the general-purpose source register, encoded in the 'Rn' field.

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.
