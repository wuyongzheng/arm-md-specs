## C7.2.305 SM3SS1

## SM3SS1

This instruction rotates the top 32 bits of the 128-bit vector in the first source SIMD&amp;FP register by 12, and adds that 32-bit value to the two other 32-bit values held in the top 32 bits of each of the 128-bit vectors in the second and third source SIMD&amp;FP registers, rotating this result left by 7 and writing the final result into the top 32 bits of the vector in the destination SIMD&amp;FP register, with the bottom 96 bits of the vector being written to 0.

## Advanced SIMD

(FEAT\_SM3)

<!-- image -->

## Encoding

```
SM3SS1 <Vd>.4S, <Vn>.4S, <Vm>.4S, <Va>.4S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SM3) then EndOfDecode(Decode_UNDEF);
```

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer a = UInt(Ra);
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

## &lt;Vn&gt;

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## &lt;Va&gt;

Is the name of the third SIMD&amp;FP source register, encoded in the 'Ra' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(128) Vm = V[m, 128]; constant bits(128) Vn = V[n, 128]; constant bits(128) Va = V[a, 128]; bits(128) result; result<127:96> = ROL((ROL(Vn<127:96>, 12) + Vm<127:96> + Va<127:96>), 7); result<95:0> = Zeros(96); V[d, 128] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
