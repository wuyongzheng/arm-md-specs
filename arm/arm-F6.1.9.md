## F6.1.9 SHA1M

SHA1 hash update (majority).

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

## A1

(FEAT\_SHA1)

<!-- image -->

## Encoding

```
SHA1M.32 <Qd>, <Qn>, <Qm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SHA1) then UNDEFINED; if Q != '1' then UNDEFINED; if Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1' then constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm);
```

T1

(FEAT\_SHA1)

<!-- image -->

## Encoding

```
SHA1M.32 <Qd>, <Qn>, <Qm>
```

## Decode for this encoding

```
if InITBlock() then UNPREDICTABLE; if !IsFeatureImplemented(FEAT_SHA1) then UNDEFINED; if Q != '1' then UNDEFINED; if Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1' then constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm);
```

```
UNDEFINED;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

```
UNDEFINED;
```

## Assembler Symbols

## &lt;Qd&gt;

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

&lt;Qn&gt;

Is the 128-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field as &lt;Qn&gt;*2.

## &lt;Qm&gt;

Is the 128-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckCryptoEnabled32(); bits(128) x = Q[d>>1]; bits(32) y = Q[n>>1]<31:0>; // Note: 32 bits wide constant bits(128) w = Q[m>>1]; for e = 0 to 3 constant bits(32) t = SHAmajority(x<63:32>, x<95:64>, x<127:96>); y = y + ROL(x<31:0>, 5) + t + Elem[w, e, 32]; x<63:32> = ROL(x<63:32>, 30); constant bits(160) yx = ROL(y:x, 32); (y, x) = (yx<128+:32>, yx<0+:128>); Q[d>>1] = x;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.