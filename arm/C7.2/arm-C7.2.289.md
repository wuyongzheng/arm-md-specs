## C7.2.289 SHA256H2

SHA256 hash update (part 2).

## Advanced SIMD

(FEAT\_SHA256)

<!-- image -->

## Encoding

```
SHA256H2 <Qd>, <Qn>, <Vm>.4S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SHA256) then constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm);
```

## Assembler Symbols

&lt;Qd&gt;

Is the 128-bit name of the SIMD&amp;FP source and destination, encoded in the 'Rd' field.

&lt;Qn&gt;

Is the 128-bit name of the second SIMD&amp;FP source register, encoded in the 'Rn' field.

&lt;Vm&gt;

Is the name of the third SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant boolean part1 = FALSE; V[d, 128] = SHA256hash(V[n, 128], V[d, 128], V[m, 128],
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
EndOfDecode(Decode_UNDEF);
```

```
part1);
```
