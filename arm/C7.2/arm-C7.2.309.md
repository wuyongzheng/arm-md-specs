## C7.2.309 SM3TT2B

## SM3TT2B

This instruction takes three 128-bit vectors from three source SIMD&amp;FP registers, and a 2-bit immediate index value, and returns a 128-bit result in the destination SIMD&amp;FP register. It performs a 32-bit majority function between the three 32-bit fields held in the upper three elements of the first source vector, and adds the resulting 32-bit value and the following three other 32-bit values:

- The bottom 32-bit element of the first source vector, Vd, that was used for the 32-bit majority function.
- The 32-bit element held in the top 32 bits of the second source vector, Vn.
- A32-bit element indexed out of the third source vector, Vm.

Athree-way exclusive-OR is performed of the result of this addition, the result of the addition rotated left by 9, and the result of the addition rotated left by 17. The result of this exclusive-OR is returned as the top element of the returned result. The other elements of this result are taken from elements of the first source vector, with the element returned in bits&lt;63:32&gt; being rotated left by 19.

## Advanced SIMD

(FEAT\_SM3)

<!-- image -->

## Encoding

```
SM3TT2B <Vd>.4S, <Vn>.4S, <Vm>.S[<imm2>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SM3) then EndOfDecode(Decode_UNDEF);
```

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer i = UInt(imm2);
```

## Assembler Symbols

## &lt;Vd&gt;

Is the name of the SIMD&amp;FP source and destination register, encoded in the 'Rd' field.

## &lt;Vn&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Vm&gt;

Is the name of the third SIMD&amp;FP source register, encoded in the 'Rm' field.

## &lt;imm2&gt;

Is a 32-bit element indexed out of &lt;Vm&gt;, encoded in 'imm2'.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(128) Vm = V[m, 128]; constant bits(128) Vn = V[n, 128]; constant bits(128) Vd = V[d, 128]; bits(32) Wj; bits(128) result; bits(32) TT2; Wj = Elem[Vm, i, 32]; TT2 = (Vd<127:96> AND Vd<95:64>) OR (NOT(Vd<127:96>) AND Vd<63:32>); TT2 = (TT2 + Vd<31:0> + Vn<127:96> + Wj)<31:0>; result<31:0> = Vd<63:32>; result<63:32> = ROL(Vd<95:64>, 19); result<95:64> = Vd<127:96>; result<127:96> = TT2 EOR ROL(TT2, 9) EOR ROL(TT2, 17); V[d, 128] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
