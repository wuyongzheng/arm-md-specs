## C9.2.7 ADDSVL

Add multiple of Streaming SVE vector register size to scalar register

This instruction adds the Streaming SVE vector register size in bytes multiplied by an immediate in the range -32 to 31 to the 64-bit source general-purpose register or current stack pointer, and places the result in the 64-bit destination general-purpose register or current stack pointer.

This instruction does not require the PE to be in Streaming SVE mode.

## SME

(FEAT\_SME)

<!-- image -->

## Encoding

```
ADDSVL <Xd|SP>, <Xn|SP>, #<imm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF);
```

```
constant integer n = UInt(Rn); constant integer d = UInt(Rd); constant integer imm = SInt(imm6);
```

## Assembler Symbols

## &lt;Xd|SP&gt;

Is the 64-bit name of the destination general-purpose register or stack pointer, encoded in the 'Rd' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the source general-purpose register or stack pointer, encoded in the 'Rn' field.

## &lt;imm&gt;

Is the signed immediate operand, in the range -32 to 31, encoded in the 'imm6' field.

## Operation

```
CheckSMEEnabled(); constant integer SVL = CurrentSVL; constant integer len = imm * (SVL DIV 8); constant bits(64) operand1 = if n == 31 then SP[64] else X[n, 64]; constant bits(64) result = operand1 + len; if d == 31 then SP[64] = result; else X[d, 64] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.