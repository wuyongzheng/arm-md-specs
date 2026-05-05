## C6.2.354 SBFM

Signed bitfield move

This instruction is usually accessed via one of its aliases, which are always preferred for disassembly.

If &lt;imms&gt; is greater than or equal to &lt;immr&gt; , this copies a bitfield of ( &lt;imms&gt; -&lt;immr&gt; +1) bits starting from bit position &lt;immr&gt; in the source register to the least significant bits of the destination register.

If &lt;imms&gt; is less than &lt;immr&gt; , this copies a bitfield of ( &lt;imms&gt; +1) bits from the least significant bits of the source register to bit position (regsize&lt;immr&gt; ) of the destination register, where regsize is the destination register size of 32 or 64 bits.

In both cases, the destination bits below the bitfield are set to zero, and the bits above the bitfield are set to a copy of the most significant bit of the bitfield.

This instruction is used by the aliases ASR (immediate), SBFIZ, SBFX, SXTB, SXTH, and SXTW.

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (sf == 0 && N == SBFM <Wd>, <Wn>, #<immr>, #<imms>
```

0)

## Encoding for the 64-bit variant

1)

```
Applies when (sf == 1 && N == SBFM <Xd>, <Xn>, #<immr>, #<imms>
```

## Decode for all variants of this encoding

```
if sf == '1' && N != '1' then EndOfDecode(Decode_UNDEF); if sf == '0' && (N != '0' || immr<5> != '0' || imms<5> != '0') then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer datasize = 32 << UInt(sf); constant integer s = UInt(imms); constant integer r = UInt(immr); bits(datasize) wmask; bits(datasize) tmask; (wmask, tmask) = DecodeBitMasks(N, imms, immr, FALSE, datasize);
```

## Assembler Symbols

&lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Wn&gt;

Is the 32-bit name of the general-purpose source register, encoded in the 'Rn' field.

## &lt;immr&gt;

For the '32-bit' variant: is the right rotate amount, in the range 0 to 31, encoded in the 'immr' field.

For the '64-bit' variant: is the right rotate amount, in the range 0 to 63, encoded in the 'immr' field.

## &lt;imms&gt;

For the '32-bit' variant: is the leftmost bit number to be moved from the source, in the range 0 to 31, encoded in the 'imms' field.

For the '64-bit' variant: is the leftmost bit number to be moved from the source, in the range 0 to 63, encoded in the 'imms' field.

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Xd&gt;

## &lt;Xn&gt;

Is the 64-bit name of the general-purpose source register, encoded in the 'Rn' field.

## Alias Conditions

| Alias           | Of variant   | Is preferred when                    |
|-----------------|--------------|--------------------------------------|
| ASR (immediate) | 32-bit       | imms == '011111'                     |
| ASR (immediate) | 64-bit       | imms == '111111'                     |
| SBFIZ           |              | UInt(imms) < UInt(immr)              |
| SBFX            |              | BFXPreferred(sf, opc<1>, imms, immr) |
| SXTB            |              | immr == '000000' && imms == '000111' |
| SXTH            |              | immr == '000000' && imms == '001111' |
| SXTW            |              | immr == '000000' && imms == '011111' |

## Operation

```
constant bits(datasize) src = X[n, datasize]; // Perform bitfield move on low bits constant bits(datasize) bot = ROR(src, r) AND wmask; constant bits(datasize) top = Replicate(src<s>, datasize); // Combine extension bits and result bits X[d, datasize] = (top AND NOT(tmask)) OR (bot AND tmask);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
