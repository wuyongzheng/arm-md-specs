## C9.2.191 MOVT (table to scalar)

Move 8 bytes from ZT0 to general-purpose register

This instruction moves 8 bytes to a general-purpose register from the ZT0 register at the byte offset specified by the immediate index. This instruction is UNDEFINED in Non-debug state.

## SME2

(FEAT\_SME2)

<!-- image -->

## Encoding

```
MOVT
```

```
<Xt>, ZT0[<offs>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) || !Halted() then EndOfDecode(Decode_UNDEF); constant integer t = UInt(Rt); constant integer offset = UInt(off3);
```

## Assembler Symbols

&lt;Xt&gt;

Is the 64-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;offs&gt;

Is the immediate byte offset, a multiple of 8 in the range of 0 to 56, encoded in the 'off3' field as &lt;offs&gt;/8.

## Operation

```
CheckSMEEnabled(); CheckSMEZT0Enabled(); constant bits(512) operand = ZT0[512]; X[t, 64] = Elem[operand, offset, 64];
```