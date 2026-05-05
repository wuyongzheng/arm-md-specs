## C7.2.292 SHA256SU1

SHA256 schedule update 1.

## Advanced SIMD

(FEAT\_SHA256)

<!-- image -->

## Encoding

```
SHA256SU1 <Vd>.4S, <Vn>.4S, <Vm>.4S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SHA256) then constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm);
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
AArch64.CheckFPAdvSIMDEnabled(); constant bits(128) operand1 = V[d, 128]; constant bits(128) operand2 = V[n, 128]; constant bits(128) operand3 = V[m, 128]; constant bits(128) T0 = operand3<31:0> : operand2<127:32>; bits(64) T1; bits(32) elt; bits(128) result; T1 = operand3<127:64>; for e = 0 to 1 elt = Elem[T1, e, 32]; elt = ROR(elt, 17) EOR ROR(elt, 19) EOR LSR(elt, 10); elt = elt + Elem[operand1, e, 32] + Elem[T0, e, 32]; Elem[result, e, 32] = elt; T1 = result<63:0>; for e = 2 to 3 elt = Elem[T1, e - 2, 32]; elt = ROR(elt, 17) EOR ROR(elt, 19) EOR LSR(elt, 10);
```

```
EndOfDecode(Decode_UNDEF);
```

```
elt = elt + Elem[operand1, e, 32] + Elem[result, e, 32] = elt; V[d, 128] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
Elem[T0, e, 32];
```
