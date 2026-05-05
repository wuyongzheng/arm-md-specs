## C7.2.288 SHA1SU1

SHA1 schedule update 1.

## Advanced SIMD

(FEAT\_SHA1)

<!-- image -->

## Encoding

```
SHA1SU1 <Vd>.4S, <Vn>.4S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SHA1) then constant integer d = UInt(Rd); constant integer n = UInt(Rn);
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP source and destination register, encoded in the 'Rd' field.

&lt;Vn&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(128) operand1 = V[d, 128]; constant bits(128) operand2 = V[n, 128]; constant bits(128) T = operand1 EOR LSR(operand2, 32); bits(128) result; result<31:0> = ROL(T<31:0>, 1); result<63:32> = ROL(T<63:32>, 1); result<95:64> = ROL(T<95:64>, 1); result<127:96> = ROL(T<127:96>, 1) EOR ROL(T<31:0>, 2); V[d, 128] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
EndOfDecode(Decode_UNDEF);
```
