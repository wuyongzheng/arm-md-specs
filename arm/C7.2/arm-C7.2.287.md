## C7.2.287 SHA1SU0

SHA1 schedule update 0.

## Advanced SIMD

(FEAT\_SHA1)

<!-- image -->

## Encoding

```
SHA1SU0 <Vd>.4S, <Vn>.4S, <Vm>.4S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SHA1) then constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm);
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
AArch64.CheckFPAdvSIMDEnabled(); constant bits(128) operand1 = V[d, 128]; constant bits(128) operand2 = V[n, 128]; constant bits(128) operand3 = V[m, 128]; bits(128) result = operand2<63:0> : operand1<127:64>; result = result EOR operand1 EOR operand3; V[d, 128] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
EndOfDecode(Decode_UNDEF);
```
