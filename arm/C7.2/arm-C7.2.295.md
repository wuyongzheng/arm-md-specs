## C7.2.295 SHA512SU0

SHA512 schedule update 0

This instruction takes the values from the two 128-bit source SIMD&amp;FP registers and produces a 128-bit output value that combines the gamma0 functions of two iterations of the SHA512 schedule update that are performed after the first 16 iterations within a block. It returns this value to the destination SIMD&amp;FP register.

## Advanced SIMD

(FEAT\_SHA512)

<!-- image -->

## Encoding

```
SHA512SU0 <Vd>.2D, <Vn>.2D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SHA512) then constant integer d = UInt(Rd); constant integer n = UInt(Rn);
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP source and destination register, encoded in the 'Rd' field.

&lt;Vn&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); bits(64) sig0; bits(128) Vtmp; constant bits(128) x = V[n, 128]; constant bits(128) w = V[d, 128]; sig0 = ROR(w<127:64>, 1) EOR ROR(w<127:64>, 8) EOR ('0000000':w<127:71>); Vtmp<63:0> = w<63:0> + sig0; sig0 = ROR(x<63:0>, 1) EOR ROR(x<63:0>, 8) EOR ('0000000':x<63:7>); Vtmp<127:64> = w<127:64> + sig0; V[d, 128] = Vtmp;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
EndOfDecode(Decode_UNDEF);
```
