## F6.1.12 SHA1SU1

SHA1 schedule update 1.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

## A1

(FEAT\_SHA1)

<!-- image -->

## Encoding

```
SHA1SU1.32 <Qd>, <Qm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SHA1) then UNDEFINED; if size != '10' then UNDEFINED; if Vd<0> == '1' || Vm<0> == '1' then UNDEFINED; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm);
```

T1

(FEAT\_SHA1)

<!-- image -->

## Encoding

```
SHA1SU1.32 <Qd>, <Qm>
```

## Decode for this encoding

```
if InITBlock() then UNPREDICTABLE; if !IsFeatureImplemented(FEAT_SHA1) then if size != '10' then UNDEFINED; if Vd<0> == '1' || Vm<0> == '1' then UNDEFINED; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm);
```

```
UNDEFINED;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;Qd&gt;

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

&lt;Qm&gt;

Is the 128-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckCryptoEnabled32(); constant bits(128) X = Q[d>>1]; constant bits(128) Y = Q[m>>1]; constant bits(128) T = X EOR LSR(Y, 32); constant bits(32) W0 = ROL(T<31:0>, 1); constant bits(32) W1 = ROL(T<63:32>, 1); constant bits(32) W2 = ROL(T<95:64>, 1); constant bits(32) W3 = ROL(T<127:96>, 1) EOR ROL(T<31:0>, 2); Q[d>>1] = W3:W2:W1:W0;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.