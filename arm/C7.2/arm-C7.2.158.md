## C7.2.158 FMOV (scalar, immediate)

Floating-point move immediate (scalar)

This instruction copies a floating-point immediate constant into the SIMD&amp;FP destination register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

<!-- image -->

## Encoding for the Half-precision variant

```
(FEAT_FP16) Applies when (ftype == 11)
```

```
FMOV <Hd>, #<imm>
```

## Encoding for the Single-precision variant

```
(FEAT_FP) Applies when (ftype == 00)
```

```
FMOV <Sd>, #<imm>
```

## Encoding for the Double-precision variant

```
(FEAT_FP) Applies when (ftype == 01)
```

```
FMOV <Dd>, #<imm>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_FP) then EndOfDecode(Decode_UNDEF); if ftype == '10' then EndOfDecode(Decode_UNDEF); if ftype == '11' && !IsFeatureImplemented(FEAT_FP16) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer datasize = 8 << UInt(ftype EOR '10'); constant bits(datasize) imm = VFPExpandImm(imm8, datasize);
```

## Assembler Symbols

## &lt;Hd&gt;

Is the 16-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

## &lt;imm&gt;

Is a signed floating-point constant with 3-bit exponent and normalized 4 bits of precision, encoded in the 'imm8' field. For details of the range of constants available and the encoding of &lt;imm&gt; , see Modified immediate constants in A64 floating-point instructions.

<!-- image -->

## &lt;Dd&gt;

Is the 32-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

<!-- image -->
