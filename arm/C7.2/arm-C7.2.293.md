## C7.2.293 SHA512H2

SHA512 hash update part 2

This instruction takes the values from the three 128-bit source SIMD&amp;FP registers and produces a 128-bit output value that combines the sigma0 and majority functions of two iterations of the SHA512 computation. It returns this value to the destination SIMD&amp;FP register.

## Advanced SIMD

(FEAT\_SHA512)

<!-- image -->

## Encoding

```
SHA512H2 <Qd>, <Qn>, <Vm>.2D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SHA512) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm);
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
AArch64.CheckFPAdvSIMDEnabled(); bits(128) Vtmp; bits(64) NSigma0; constant bits(128) x = V[n, 128]; constant bits(128) y = V[m, 128]; constant bits(128) w = V[d, 128]; NSigma0 = ROR(y<63:0>, 28) EOR ROR(y<63:0>, 34) EOR ROR(y<63:0>, 39); Vtmp<127:64> = SHAmajority(x<63:0>, y<127:64>, y<63:0>); Vtmp<127:64> = (Vtmp<127:64> + NSigma0 + w<127:64>); NSigma0 = ROR(Vtmp<127:64>, 28) EOR ROR(Vtmp<127:64>, 34) EOR ROR(Vtmp<127:64>, 39); Vtmp<63:0> = SHAmajority(Vtmp<127:64>, y<63:0>, y<127:64>); Vtmp<63:0> = (Vtmp<63:0> + NSigma0 + w<63:0>); V[d, 128] = Vtmp;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
