## F6.1.15 SHA256SU0

SHA256 schedule update 0.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

## A1

(FEAT\_SHA256)

<!-- image -->

## Encoding

```
SHA256SU0.32 <Qd>, <Qm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SHA256) then UNDEFINED; if size != '10' then UNDEFINED; if Vd<0> == '1' || Vm<0> == '1' then UNDEFINED; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm);
```

T1

(FEAT\_SHA256)

<!-- image -->

## Encoding

```
SHA256SU0.32 <Qd>, <Qm>
```

## Decode for this encoding

```
if InITBlock() then UNPREDICTABLE; if !IsFeatureImplemented(FEAT_SHA256) then if size != '10' then UNDEFINED; if Vd<0> == '1' || Vm<0> == '1' then UNDEFINED; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm);
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
if ConditionPassed() then bits(128) result; EncodingSpecificOperations(); CheckCryptoEnabled32(); constant bits(128) x = Q[d>>1]; constant bits(128) y = Q[m>>1]; constant bits(128) t = y<31:0> : x<127:32>; for e = 0 to 3 bits(32) elt = Elem[t, e, 32]; elt = ROR(elt, 7) EOR ROR(elt, 18) EOR LSR(elt, 3); Elem[result, e, 32] = elt + Elem[x, e, 32]; Q[d>>1] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.