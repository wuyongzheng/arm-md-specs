## C7.2.303 SM3PARTW1

## SM3PARTW1

This instruction takes three 128-bit vectors from the three source SIMD&amp;FP registers and returns a 128-bit result in the destination SIMD&amp;FP register. The result is obtained by a three-way exclusive-OR of the elements within the input vectors with some fixed rotations, see the Operation pseudocode for more information.

## Advanced SIMD

(FEAT\_SM3)

<!-- image -->

## Encoding

```
SM3PARTW1 <Vd>.4S, <Vn>.4S, <Vm>.4S
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

## &lt;Vn&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Vm&gt;

Is the name of the third SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(128) Vm = V[m, 128]; constant bits(128) Vn = V[n, 128]; constant bits(128) Vd = V[d, 128]; bits(128) result; result<95:0> = (Vd EOR Vn)<95:0> EOR (ROL(Vm<127:96>, 15):ROL(Vm<95:64>, 15):ROL(Vm<63:32>, 15)); for i = 0 to 3 if i == 3 then result<127:96> = (Vd EOR Vn)<127:96> EOR (ROL(result<31:0>, 15)); result<(32*i)+31:(32*i)> = (result<(32*i)+31:(32*i)> EOR ROL(result<(32*i)+31:(32*i)>, 15) EOR ROL(result<(32*i)+31:(32*i)>, 23)); V[d, 128] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
