## C7.2.12 BCAX

Bit clear and exclusive-OR

This instruction performs a bitwise AND of the 128-bit vector in a source SIMD&amp;FP register and the complement of the vector in another source SIMD&amp;FP register, then performs a bitwise exclusive-OR of the resulting vector and the vector in a third source SIMD&amp;FP register, and writes the result to the destination SIMD&amp;FP register.

## Advanced SIMD

(FEAT\_SHA3)

<!-- image -->

## Encoding

```
BCAX <Vd>.16B, <Vn>.16B, <Vm>.16B, <Va>.16B
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SHA3) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer a = UInt(Ra);
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

## &lt;Vn&gt;

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

&lt;Va&gt;

Is the name of the third SIMD&amp;FP source register, encoded in the 'Ra' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(128) operand1 = V[m, 128]; constant bits(128) operand2 = V[n, 128]; constant bits(128) operand3 = V[a, 128]; V[d, 128] = operand2 EOR (operand1 AND NOT(operand3));
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
