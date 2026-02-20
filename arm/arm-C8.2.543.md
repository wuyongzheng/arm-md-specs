## C8.2.543 RDVL

Read multiple of vector register size to scalar register

This instruction multiplies the current vector register size in bytes by an immediate in the range -32 to 31 and places the result in the 64-bit destination general-purpose register.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
RDVL <Xd>, #<imm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer imm = SInt(imm6);
```

## Assembler Symbols

## &lt;Xd&gt;

Is the 64-bit name of the destination general-purpose register, encoded in the 'Rd' field.

## &lt;imm&gt;

Is the signed immediate operand, in the range -32 to 31, encoded in the 'imm6' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer len = X[d, 64] = len<63:0>;
```

```
imm * (VL DIV 8);
```