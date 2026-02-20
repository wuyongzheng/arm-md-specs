## F6.1.13 SHA256H

SHA256 hash update part 1.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

## A1

(FEAT\_SHA256)

<!-- image -->

## Encoding

```
SHA256H.32 <Qd>, <Qn>, <Qm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SHA256) then UNDEFINED; if Q != '1' then UNDEFINED; if Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1' then constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm);
```

T1

(FEAT\_SHA256)

<!-- image -->

## Encoding

```
SHA256H.32 <Qd>, <Qn>, <Qm>
```

## Decode for this encoding

```
if InITBlock() then UNPREDICTABLE; if !IsFeatureImplemented(FEAT_SHA256) then UNDEFINED; if Q != '1' then UNDEFINED; if Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1' then constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm);
```

```
UNDEFINED;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

```
UNDEFINED;
```

## Assembler Symbols

&lt;Qd&gt;

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

&lt;Qn&gt;

Is the 128-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field as &lt;Qn&gt;*2.

&lt;Qm&gt;

Is the 128-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckCryptoEnabled32(); constant bits(128) X = Q[d>>1]; constant bits(128) Y = Q[n>>1]; constant bits(128) W = Q[m>>1]; constant boolean part1 = TRUE; Q[d>>1] = SHA256hash(X, Y, W, part1);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.