## C7.2.296 SHA512SU1

SHA512 schedule update 1

This instruction takes the values from the three source SIMD&amp;FP registers and produces a 128-bit output value that combines the gamma1 functions of two iterations of the SHA512 schedule update that are performed after the first 16 iterations within a block. It returns this value to the destination SIMD&amp;FP register.

## Advanced SIMD

(FEAT\_SHA512)

<!-- image -->

## Encoding

```
SHA512SU1 <Vd>.2D, <Vn>.2D, <Vm>.2D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SHA512) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm);
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP source and destination register, encoded in the 'Rd' field.

&lt;Vn&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rn' field.

&lt;Vm&gt;

Is the name of the third SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); bits(64) sig1; bits(128) Vtmp; constant bits(128) x = V[n, 128]; constant bits(128) y = V[m, 128]; constant bits(128) w = V[d, 128]; sig1 = ROR(x<127:64>, 19) EOR ROR(x<127:64>, 61) EOR ('000000':x<127:70>); Vtmp<127:64> = w<127:64> + sig1 + y<127:64>; sig1 = ROR(x<63:0>, 19) EOR ROR(x<63:0>, 61) EOR ('000000':x<63:6>); Vtmp<63:0> = w<63:0> + sig1 + y<63:0>; V[d, 128] = Vtmp;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
