## C9.2.193 MOVT (vector to table)

Move vector register to ZT0

This instruction copies the source vector register to ZT0 at the vector length offset specified by the immediate index. When the index is zero, the instruction writes zeroes to the most significant (512-VL) bits of the ZT0 register. When the index is not zero, the unindexed portions of ZT0 remain unchanged.

This instruction is unpredicated.

## SME2

(FEAT\_SME\_LUTv2)

<!-- image -->

## Encoding

```
MOVT ZT0{[<offs>, MUL VL]},
```

```
<Zt>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME_LUTv2) then constant integer t = UInt(Zt); constant integer imm = UInt(off2);
```

## Assembler Symbols

&lt;offs&gt;

Is the vector length offset, in the range 0 to 3, defaulting to 0 when omitted, encoded in the 'off2' field.

&lt;Zt&gt;

Is the name of the scalable vector register to be transferred, encoded in the 'Zt' field.

## Operation

```
CheckStreamingSVEEnabled(); CheckSMEZT0Enabled(); constant integer VL = CurrentVL; constant integer tsize = if VL <= 512 then VL else 512; constant integer offset = imm MOD (512 DIV tsize); bits(512) result = if imm == 0 then Zeros(512) else ZT0[512]; Elem[result, offset, tsize] = Z[t, VL]<tsize-1:0>; ZT0[512] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
EndOfDecode(Decode_UNDEF);
```