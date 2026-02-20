## C9.2.194 RDSVL

Read multiple of Streaming SVE vector register size to scalar register

This instruction multiplies the Streaming SVE vector register size in bytes by an immediate in the range -32 to 31 and places the result in the 64-bit destination general-purpose register.

This instruction does not require the PE to be in Streaming SVE mode.

## SME

(FEAT\_SME)

<!-- image -->

## Encoding

```
RDSVL <Xd>, #<imm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF);
```

```
constant integer d = UInt(Rd); constant integer imm = SInt(imm6);
```

## Assembler Symbols

&lt;Xd&gt;

Is the 64-bit name of the destination general-purpose register, encoded in the 'Rd' field.

## &lt;imm&gt;

Is the signed immediate operand, in the range -32 to 31, encoded in the 'imm6' field.

## Operation

```
CheckSMEEnabled(); constant integer SVL = CurrentSVL; constant integer len = imm * (SVL X[d, 64] = len<63:0>;
```

```
DIV 8);
```