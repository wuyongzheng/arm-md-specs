## F6.1.11 SHA1SU0

SHA1 schedule update 0.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

## A1

(FEAT\_SHA1)

<!-- image -->

## Encoding

```
SHA1SU0.32 <Qd>, <Qn>, <Qm>
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
SHA1SU0.32 <Qd>, <Qn>, <Qm>
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
if ConditionPassed() then EncodingSpecificOperations(); CheckCryptoEnabled32(); constant bits(128) op1 = bits(128) op2 = Q[n>>1]; constant bits(128) op3 = op2 = op2<63:0> : op1<127:64>; Q[d>>1] = op1 EOR op2 EOR op3;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

```
Q[d>>1]; Q[m>>1];
```