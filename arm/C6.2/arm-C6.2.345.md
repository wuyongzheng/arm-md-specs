## C6.2.345 RMIF

Rotate, mask insert flags

This instruction performs a rotation right of a value held in a general-purpose register by an immediate value, and then inserts a selection of the bottom four bits of the result of the rotation into the PSTATE flags, under the control of a second immediate mask.

## Integer

(FEAT\_FlagM)

<!-- image -->

## Encoding

```
RMIF <Xn>, #<shift>, #<mask>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_FlagM) then EndOfDecode(Decode_UNDEF); constant integer imm = UInt(imm6); constant bits(4) flagmask = mask; constant integer n = UInt(Rn);
```

## Assembler Symbols

## &lt;Xn&gt;

Is the 64-bit name of the general-purpose source register, encoded in the 'Rn' field.

## &lt;shift&gt;

Is the shift amount, in the range 0 to 63, defaulting to 0 and encoded in the 'imm6' field.

## &lt;mask&gt;

Is the flag bit mask, an immediate in the range 0 to 15, which selects the bits that are inserted into the NZCV condition flags, encoded in the 'mask' field.

## Operation

```
constant bits(64) reg = X[n, 64]; constant bits(4) flags = (reg:reg)<imm+3:imm>; if flagmask<3> == '1' then PSTATE.N = flags<3>; if flagmask<2> == '1' then PSTATE.Z = flags<2>; if flagmask<1> == '1' then PSTATE.C = flags<1>; if flagmask<0> == '1' then PSTATE.V = flags<0>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
