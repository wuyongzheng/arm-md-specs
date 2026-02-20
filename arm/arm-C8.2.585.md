## C8.2.585 SM4EKEY

## SM4 key updates

This instruction reads four rounds of 32-bit input key values from each 128-bit segment of the first source vector, along with four rounds of 32-bit constants from the corresponding 128-bit segment of the second source vector. The four rounds of output key values are derived in accordance with the SM4 standard, and placed in the corresponding segments of the destination vector. This instruction is unpredicated.

ID\_AA64ZFR0\_EL1.SM4 indicates whether this instruction is implemented.

This instruction is illegal when executed in Streaming SVE mode, unless FEAT\_SME\_FA64 is implemented and enabled.

## SVE2

(FEAT\_SVE\_SM4)

<!-- image -->

## Encoding

```
SM4EKEY <Zd>.S, <Zn>.S, <Zm>.S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE_SM4) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd);
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

## &lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

<!-- image -->

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer segments = VL DIV 128; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result; for s = 0 to segments-1 constant bits(128) source = Elem[operand2, bits(32) intval; bits(32) const; bits(128) roundresult = Elem[operand1, s, 128];
```

```
s, 128];
```

```
for index = 0 to 3 const = Elem[source, index, 32]; intval = roundresult<127:96> EOR roundresult<95:64> EOR roundresult<63:32> EOR const; for i = 0 to 3 Elem[intval, i, 8] = Sbox(Elem[intval, i, 8]); intval = intval EOR ROL(intval, 13) EOR ROL(intval, 23); intval = intval EOR roundresult<31:0>; roundresult<31:0> = roundresult<63:32>; roundresult<63:32> = roundresult<95:64>; roundresult<95:64> = roundresult<127:96>; roundresult<127:96> = intval; Elem[result, s, 128] = roundresult; Z[d, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.