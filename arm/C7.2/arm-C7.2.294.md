## C7.2.294 SHA512H

SHA512 hash update part 1

This instruction takes the values from the three 128-bit source SIMD&amp;FP registers and produces a 128-bit output value that combines the sigma1 and chi functions of two iterations of the SHA512 computation. It returns this value to the destination SIMD&amp;FP register.

## Advanced SIMD

(FEAT\_SHA512)

<!-- image -->

## Encoding

```
SHA512H <Qd>, <Qn>, <Vm>.2D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SHA512) then constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm);
```

## Assembler Symbols

&lt;Qd&gt;

Is the 128-bit name of the SIMD&amp;FP source and destination register, encoded in the 'Rd' field.

&lt;Qn&gt;

Is the 128-bit name of the second SIMD&amp;FP source register, encoded in the 'Rn' field.

&lt;Vm&gt;

Is the name of the third SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); bits(128) Vtmp; bits(64) MSigma1; bits(64) tmp; constant bits(128) x = V[n, 128]; constant bits(128) y = V[m, 128]; constant bits(128) w = V[d, 128]; MSigma1 = ROR(y<127:64>, 14) EOR ROR(y<127:64>, 18) EOR ROR(y<127:64>, 41); Vtmp<127:64> = (y<127:64> AND x<63:0>) EOR (NOT(y<127:64>) AND x<127:64>); Vtmp<127:64> = (Vtmp<127:64> + MSigma1 + w<127:64>); tmp = Vtmp<127:64> + y<63:0>; MSigma1 = ROR(tmp, 14) EOR ROR(tmp, 18) EOR ROR(tmp, 41); Vtmp<63:0> = (tmp AND y<127:64>) EOR (NOT(tmp) AND x<63:0>); Vtmp<63:0> = (Vtmp<63:0> + MSigma1 + w<63:0>); V[d, 128] = Vtmp;
```

```
EndOfDecode(Decode_UNDEF);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
