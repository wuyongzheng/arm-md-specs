## C7.2.260 RAX1

Rotate and exclusive-OR

This instruction rotates each 64-bit element of the 128-bit vector in a source SIMD&amp;FP register left by 1, performs a bitwise exclusive-OR of the resulting 128-bit vector and the vector in another source SIMD&amp;FP register, and writes the result to the destination SIMD&amp;FP register.

## Advanced SIMD

(FEAT\_SHA3)

<!-- image -->

## Encoding

```
RAX1 <Vd>.2D, <Vn>.2D, <Vm>.2D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SHA3) then constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm);
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

&lt;Vn&gt;

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

&lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(128) Vm = V[m, 128]; constant bits(128) Vn = V[n, 128]; V[d, 128] = Vn
```

```
EOR (ROL(Vm<127:64>, 1):ROL(Vm<63:0>, 1));
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
EndOfDecode(Decode_UNDEF);
```
