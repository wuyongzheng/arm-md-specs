## C9.2.347 ZERO (tiles)

Zero a list of 64-bit element ZA tiles

This instruction zeroes all bytes within each of the up to eight listed 64-bit element tiles named ZA0.D to ZA7.D , leaving the other 64-bit element tiles unmodified.

This instruction does not require the PE to be in Streaming SVE mode, and it is expected that this instruction will not experience a significant slowdown due to contention with other PEs that are executing in Streaming SVE mode.

For programmer convenience an assembler must also accept the names of 32-bit, 16-bit, and 8-bit element tiles that are converted into the corresponding set of 64-bit element tiles.

In accordance with the architecturally defined mapping between different element size tiles:

- Zeroing the 8-bit element tile name ZA0.B , or the entire array name ZA , is equivalent to zeroing all eight 64-bit element tiles named ZA0.D to ZA7.D .
- Zeroing the 16-bit element tile name ZA0.H is equivalent to zeroing 64-bit element tiles named ZA0.D , ZA2.D , ZA4.D , and ZA6.D .
- Zeroing the 16-bit element tile name ZA1.H is equivalent to zeroing 64-bit element tiles named ZA1.D , ZA3.D , ZA5.D , and ZA7.D .
- Zeroing the 32-bit element tile name ZA0.S is equivalent to zeroing 64-bit element tiles named ZA0.D and ZA4.D .
- Zeroing the 32-bit element tile name ZA1.S is equivalent to zeroing 64-bit element tiles named ZA1.D and ZA5.D .
- Zeroing the 32-bit element tile name ZA2.S is equivalent to zeroing 64-bit element tiles named ZA2.D and ZA6.D .
- Zeroing the 32-bit element tile name ZA3.S is equivalent to zeroing 64-bit element tiles named ZA3.D and ZA7.D .

The preferred disassembly of this instruction uses the shortest list of tile names that represent the encoded immediate mask.

For example:

- An immediate that encodes 64-bit element tiles ZA0.D , ZA1.D , ZA4.D , and ZA5.D is disassembled as { ZA0.S , ZA1.S }.
- An immediate that encodes 64-bit element tiles ZA0.D , ZA2.D , ZA4.D , and ZA6.D is disassembled as { ZA0.H }.
- An all-ones immediate is disassembled as { ZA }.
- An all-zeros immediate is disassembled as an empty list { }.

## SME

(FEAT\_SME)

<!-- image -->

## Encoding

```
ZERO { {<mask>} }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF);
```

```
constant bits(8) mask = imm8; constant integer esize = 64;
```

## Assembler Symbols

&lt;mask&gt;

Is the optional list of up to eight 64-bit element tile names separated by commas, encoded in the 'imm8' field.

## Operation

```
CheckSMEAndZAEnabled(); constant integer SVL = CurrentSVL; constant integer dim = SVL DIV esize; constant bits(dim*dim*esize) result = Zeros(dim*dim*esize); for i = 0 to 7 if mask<i> == '1' then ZAtile[i, esize, dim*dim*esize] =
```

```
result;
```