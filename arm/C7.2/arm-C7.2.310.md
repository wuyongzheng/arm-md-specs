## C7.2.310 SM4E

## SM4 encode

This instruction takes input data as a 128-bit vector from the first source SIMD&amp;FP register, and four iterations of the round key held as the elements of the 128-bit vector in the second source SIMD&amp;FP register. It encrypts the data by four rounds, in accordance with the SM4 standard, returning the 128-bit result to the destination SIMD&amp;FP register.

## Advanced SIMD

(FEAT\_SM4)

<!-- image -->

## Encoding

```
SM4E <Vd>.4S, <Vn>.4S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SM4) then EndOfDecode(Decode_UNDEF);
```

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn);
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP source and destination register, encoded in the 'Rd' field.

&lt;Vn&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(128) Vn = V[n, 128]; bits(32) intval; bits(128) roundresult; bits(32) roundkey; roundresult = V[d, 128]; for index = 0 to 3 roundkey = Elem[Vn, index, 32]; intval = roundresult<127:96> EOR roundresult<95:64> EOR roundresult<63:32> EOR roundkey; for i = 0 to 3 Elem[intval, i, 8] = Sbox(Elem[intval, i, 8]); intval = intval EOR ROL(intval, 2) EOR ROL(intval, 10) EOR ROL(intval, 18) EOR ROL(intval, 24); intval = intval EOR roundresult<31:0>; roundresult<31:0> = roundresult<63:32>; roundresult<63:32> = roundresult<95:64>; roundresult<95:64> = roundresult<127:96>; roundresult<127:96> = intval;
```

V[d, 128] = roundresult;

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
