## C7.2.304 SM3PARTW2

## SM3PARTW2

This instruction takes three 128-bit vectors from three source SIMD&amp;FP registers and returns a 128-bit result in the destination SIMD&amp;FP register. The result is obtained by a three-way exclusive-OR of the elements within the input vectors with some fixed rotations, see the Operation pseudocode for more information.

## Advanced SIMD

(FEAT\_SM3)

<!-- image -->

## Encoding

```
SM3PARTW2 <Vd>.4S, <Vn>.4S, <Vm>.4S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SM3) then EndOfDecode(Decode_UNDEF);
```

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm);
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
AArch64.CheckFPAdvSIMDEnabled(); constant bits(128) Vm = V[m, 128]; constant bits(128) Vn = V[n, 128]; constant bits(128) Vd = V[d, 128]; bits(128) result; bits(128) tmp; bits(32) tmp2; tmp<127:0> = Vn EOR (ROL(Vm<127:96>, 7) : ROL(Vm<95:64>, 7) : ROL(Vm<63:32>, 7) : ROL(Vm<31:0>, 7)); result<127:0> = Vd<127:0> EOR tmp<127:0>; tmp2 = ROL(tmp<31:0>, 15); tmp2 = tmp2 EOR ROL(tmp2, 15) EOR ROL(tmp2, 23); result<127:96> = result<127:96> EOR tmp2; V[d, 128] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
