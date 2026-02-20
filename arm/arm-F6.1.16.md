## F6.1.16 SHA256SU1

SHA256 schedule update 1.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

## A1

(FEAT\_SHA256)

<!-- image -->

## Encoding

```
SHA256SU1.32 <Qd>, <Qn>, <Qm>
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
SHA256SU1.32 <Qd>, <Qn>, <Qm>
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

## &lt;Qd&gt;

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

&lt;Qn&gt;

Is the 128-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field as &lt;Qn&gt;*2.

## &lt;Qm&gt;

Is the 128-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckCryptoEnabled32(); bits(32) elt; bits(128) result; constant bits(128) x = Q[d>>1]; constant bits(128) y = Q[n>>1]; constant bits(128) z = Q[m>>1]; constant bits(128) T0 = z<31:0> : y<127:32>; bits(64) T1 = z<127:64>; for e = 0 to 1 elt = Elem[T1, e, 32]; elt = ROR(elt, 17) EOR ROR(elt, 19) EOR LSR(elt, 10); elt = elt + Elem[x, e, 32] + Elem[T0, e, 32]; Elem[result, e, 32] = elt; T1 = result<63:0>; for e = 2 to 3 elt = Elem[T1, e - 2, 32]; elt = ROR(elt, 17) EOR ROR(elt, 19) EOR LSR(elt, 10); elt = elt + Elem[x, e, 32] + Elem[T0, e, 32]; Elem[result, e, 32] = elt; Q[d>>1] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.