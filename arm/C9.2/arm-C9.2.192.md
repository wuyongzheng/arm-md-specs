## C9.2.192 MOVT (scalar to table)

Move 8 bytes from general-purpose register to ZT0

This instruction moves 8 bytes to the ZT0 register at the byte offset specified by the immediate index from a general-purpose register. This instruction is UNDEFINED in Non-debug state.

## SME2

(FEAT\_SME2)

<!-- image -->

## Encoding

```
MOVT ZT0[<offs>],
```

```
<Xt>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) || !Halted() then EndOfDecode(Decode_UNDEF); constant integer t = UInt(Rt); constant integer offset = UInt(off3);
```

## Assembler Symbols

&lt;offs&gt;

Is the immediate byte offset, a multiple of 8 in the range of 0 to 56, encoded in the 'off3' field as &lt;offs&gt;/8.

&lt;Xt&gt;

Is the 64-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## Operation

```
CheckSMEEnabled(); CheckSMEZT0Enabled(); bits(512) result = ZT0[512]; Elem[result, offset, 64] = ZT0[512] = result;
```

```
X[t, 64];
```