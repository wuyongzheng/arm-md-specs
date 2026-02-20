## F6.1.8 SHA1H

SHA1 fixed rotate.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

## A1

(FEAT\_SHA1)

<!-- image -->

## Encoding

```
SHA1H.32 <Qd>, <Qm>
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
SHA1H.32 <Qd>, <Qm>
```

## Decode for this encoding

```
if InITBlock() then UNPREDICTABLE; if !IsFeatureImplemented(FEAT_SHA1) then UNDEFINED; if size != '10' then UNDEFINED; if Vd<0> == '1' || Vm<0> == '1' then UNDEFINED; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm);
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

## &lt;Qd&gt;

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

## &lt;Qm&gt;

Is the 128-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckCryptoEnabled32(); Q[d>>1] = ZeroExtend(ROL(Q[m>>1]<31:0>, 30),
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

```
128);
```