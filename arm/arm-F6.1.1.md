## F6.1.1 AESD

AES single round decryption.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

(FEAT\_AES)

<!-- image -->

## Encoding

<!-- image -->

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AES) then UNDEFINED; if size != '00' then UNDEFINED; if Vd<0> == '1' || Vm<0> == '1' then UNDEFINED; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm);
```

T1

(FEAT\_AES)

<!-- image -->

## Encoding

```
AESD.<dt> <Qd>, <Qm>
```

## Decode for this encoding

```
if InITBlock() then UNPREDICTABLE; if !IsFeatureImplemented(FEAT_AES) then if size != '00' then UNDEFINED; if Vd<0> == '1' || Vm<0> == '1' then UNDEFINED; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm);
```

```
UNDEFINED;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;dt&gt;

Is the data type, encoded in 'size':

## &lt;Qd&gt;

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

## &lt;Qm&gt;

Is the 128-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckCryptoEnabled32(); constant bits(128) operand1 = Q[d>>1]; constant bits(128) operand2 = Q[m>>1]; Q[d>>1] = AESInvSubBytes(AESInvShiftRows(operand1 EOR operand2));
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

| size   | <dt>     |
|--------|----------|
| 00     | 8        |
| 01     | RESERVED |
| 1x     | RESERVED |