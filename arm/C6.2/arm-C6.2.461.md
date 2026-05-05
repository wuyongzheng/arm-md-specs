## C6.2.461 SUBPT

Subtract checked pointer

This instruction subtracts an optionally-shifted register value from a base address register value, and writes the result to the destination register. The optionally-shifted register value is treated as the offset.

If the operation would have generated a result where the most significant 8 bits of the result register differ from the most significant 8 bits of the base register, then the result is modified such that it is likely to be non-canonical when used as an address.

## Integer

(FEAT\_CPA)

<!-- image -->

## Encoding

```
SUBPT <Xd|SP>, <Xn|SP>, <Xm>{, LSL #<amount>}
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_CPA) then EndOfDecode(Decode_UNDEF);
```

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer shift = UInt(imm3);
```

## Assembler Symbols

## &lt;Xd|SP&gt;

Is the 64-bit name of the general-purpose destination register or stack pointer, encoded in the 'Rd' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the first general-purpose source register or stack pointer, encoded in the 'Rn' field.

## &lt;Xm&gt;

Is the 64-bit name of the second general-purpose source register, encoded in the 'Rm' field.

## &lt;amount&gt;

Is the left shift amount, in the range 0 to 7, defaulting to 0, encoded in the 'imm3' field.

## Operation

```
bits(64) result; constant bits(64) base = if n == 31 then SP[64] else X[n, 64]; constant bits(64) offset = LSL(X[m, 64], shift); result = base -offset; result = PointerAddCheck(result, base); if d == 31 then SP[64] = result; else X[d, 64] = result;
```
