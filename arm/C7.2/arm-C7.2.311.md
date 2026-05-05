## C7.2.311 SM4EKEY

SM4 key

This instruction takes an input as a 128-bit vector from the first source SIMD&amp;FP register and a 128-bit constant from the second SIMD&amp;FP register. It derives four iterations of the output key, in accordance with the SM4 standard, returning the 128-bit result to the destination SIMD&amp;FP register.

## Advanced SIMD

(FEAT\_SM4)

<!-- image -->

## Encoding

```
SM4EKEY <Vd>.4S, <Vn>.4S, <Vm>.4S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SM4) then EndOfDecode(Decode_UNDEF);
```

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm);
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

&lt;Vn&gt;

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

&lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(128) Vm = V[m, 128]; bits(32) intval; bits(32) const; bits(128) roundresult; roundresult = V[n, 128]; for index = 0 to 3 const = Elem[Vm, index, 32]; intval = roundresult<127:96> EOR roundresult<95:64> EOR roundresult<63:32> EOR const; for i = 0 to 3 Elem[intval, i, 8] = Sbox(Elem[intval, i, 8]); intval = intval EOR ROL(intval, 13) EOR ROL(intval, 23); intval = intval EOR roundresult<31:0>;
```

```
roundresult<31:0> = roundresult<63:32>; roundresult<63:32> = roundresult<95:64>; roundresult<95:64> = roundresult<127:96>; roundresult<127:96> = intval; V[d, 128] = roundresult;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
