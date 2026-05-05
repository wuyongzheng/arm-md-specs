## C7.2.460 XAR

Exclusive-OR and rotate

This instruction performs a bitwise exclusive-OR of the 128-bit vectors in the two source SIMD&amp;FP registers, rotates each 64-bit element of the resulting 128-bit vector right by the value specified by a 6-bit immediate value, and writes the result to the destination SIMD&amp;FP register.

## Advanced SIMD

(FEAT\_SHA3)

<!-- image -->

| 31 28 27 25 24 23   | 22 21 20   | 10   | 5 4   | 0   |
|---------------------|------------|------|-------|-----|
| 1 1 0 0 1 1 1 0 1   | 0 0 Rm     | imm6 | Rn    | Rd  |

## Encoding

```
XAR <Vd>.2D, <Vn>.2D, <Vm>.2D, #<imm6>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SHA3) then constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm);
```

## Assembler Symbols

## &lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

## &lt;Vn&gt;

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## &lt;imm6&gt;

Is a rotation right, encoded in 'imm6'.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(128) Vm = V[m, 128]; constant bits(128) Vn = V[n, 128]; constant bits(128) tmp = Vn EOR Vm; V[d, 128] = ROR(tmp<127:64>, UInt(imm6)):ROR(tmp<63:0>, UInt(imm6));
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
EndOfDecode(Decode_UNDEF);
```
