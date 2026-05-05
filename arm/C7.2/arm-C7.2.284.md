## C7.2.284 SHA1H

SHA1 fixed rotate.

## Advanced SIMD

(FEAT\_SHA1)

<!-- image -->

## Encoding

```
SHA1H <Sd>, <Sn>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SHA1) then constant integer d = UInt(Rd); constant integer n = UInt(Rn);
```

## Assembler Symbols

&lt;Sd&gt;

Is the 32-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

<!-- image -->

&lt;Sn&gt;

Is the 32-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(32) operand = V[d, 32] = ROL(operand, 30);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
EndOfDecode(Decode_UNDEF);
```

```
V[n, 32]; // read element [0] only, [1-3] zeroed
```
