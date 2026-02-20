## C8.2.584 SM4E

SM4 encryption and decryption

This instruction reads 16 bytes of input data from each 128-bit segment of the first source vector, together with four iterations of 32-bit round keys from the corresponding 128-bit segments of the second source vector. Each block of data is encrypted by four rounds in accordance with the SM4 standard, and destructively placed in the corresponding segments of the first source vector. This instruction is unpredicated.

ID\_AA64ZFR0\_EL1.SM4 indicates whether this instruction is implemented.

This instruction is illegal when executed in Streaming SVE mode, unless FEAT\_SME\_FA64 is implemented and enabled.

## SVE2

(FEAT\_SVE\_SM4)

<!-- image -->

## Encoding

```
SM4E <Zdn>.S,
```

```
<Zdn>.S, <Zm>.S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE_SM4) then EndOfDecode(Decode_UNDEF);
```

```
constant integer m = UInt(Zm); constant integer dn = UInt(Zdn);
```

## Assembler Symbols

## &lt;Zdn&gt;

Is the name of the first source and destination scalable vector register, encoded in the 'Zdn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer segments = VL DIV 128; constant bits(VL) operand1 = Z[dn, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result; for s = 0 to segments-1 constant bits(128) key = Elem[operand2, s, 128]; bits(32) intval; bits(128) roundresult = Elem[operand1, s, 128]; bits(32) roundkey; for index = 0 to 3 roundkey = Elem[key, index, 32]; intval = roundresult<127:96> EOR roundresult<95:64> EOR roundresult<63:32> EOR roundkey; for i = 0 to 3
```

```
Elem[intval, i,8] = Sbox(Elem[intval,i,8]); intval = (intval EOR ROL(intval, 2) EOR ROL(intval, 10) EOR ROL(intval, 18) EOR ROL(intval, 24)); intval = intval EOR roundresult<31:0>; roundresult<31:0> = roundresult<63:32>; roundresult<63:32> = roundresult<95:64>; roundresult<95:64> = roundresult<127:96>; roundresult<127:96> = intval; Elem[result, s, 128] = roundresult; Z[dn, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.