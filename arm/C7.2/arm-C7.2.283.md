## C7.2.283 SHA1C

SHA1 hash update (choose).

## Advanced SIMD

(FEAT\_SHA1)

<!-- image -->

## Encoding

```
SHA1C <Qd>, <Sn>, <Vm>.4S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SHA1) then constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm);
```

## Assembler Symbols

&lt;Qd&gt;

Is the 128-bit name of the SIMD&amp;FP source and destination, encoded in the 'Rd' field.

&lt;Sn&gt;

Is the 32-bit name of the second SIMD&amp;FP source register, encoded in the 'Rn' field.

&lt;Vm&gt;

Is the name of the third SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); bits(128) x = V[d, 128]; bits(32) y = V[n, 32]; // Note: 32 not 128 bits wide constant bits(128) w = V[m, 128]; for e = 0 to 3 constant bits(32) t = SHAchoose(x<63:32>, x<95:64>, y = y + ROL(x<31:0>, 5) + t + Elem[w, e, 32]; x<63:32> = ROL(x<63:32>, 30); constant bits(160) yx = ROL(y:x, 32); (y, x) = (yx<159:128>, yx<127:0>); V[d, 128] = x;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
EndOfDecode(Decode_UNDEF);
```

```
x<127:96>);
```
