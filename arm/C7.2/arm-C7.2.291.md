## C7.2.291 SHA256SU0

SHA256 schedule update 0.

## Advanced SIMD

(FEAT\_SHA256)

<!-- image -->

## Encoding

```
SHA256SU0 <Vd>.4S, <Vn>.4S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SHA256) then constant integer d = UInt(Rd); constant integer n = UInt(Rn);
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP source and destination register, encoded in the 'Rd' field.

&lt;Vn&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(128) operand1 = V[d, 128]; constant bits(128) operand2 = V[n, 128]; constant bits(128) T = operand2<31:0> : operand1<127:32>; bits(128) result; bits(32) elt; for e = 0 to 3 elt = Elem[T, e, 32]; elt = ROR(elt, 7) EOR ROR(elt, 18) EOR LSR(elt, 3); Elem[result, e, 32] = elt + Elem[operand1, e, 32]; V[d, 128] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
EndOfDecode(Decode_UNDEF);
```
