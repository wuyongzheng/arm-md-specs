## C6.2.282 MOVK

## Move wide with keep

This instruction moves an optionally-shifted 16-bit immediate value into a register, keeping other bits unchanged.

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (sf == 0 && hw == 0x) MOVK <Wd>, #<imm>{, LSL #<shift>}
```

## Encoding for the 64-bit variant

```
Applies when (sf == 1) MOVK <Xd>, #<imm>{,
```

```
LSL #<shift>}
```

## Decode for all variants of this encoding

```
'1' then EndOfDecode(Decode_UNDEF);
```

```
if sf == '0' && hw<1> == constant integer d = UInt(Rd); constant integer datasize = 32 << UInt(sf); constant bits(16) imm = imm16; constant integer pos = UInt(hw) << 4;
```

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;imm&gt;

Is the 16-bit unsigned immediate, in the range 0 to 65535, encoded in the 'imm16' field.

## &lt;shift&gt;

For the '32-bit' variant: is the amount by which to shift the immediate left, either 0 (the default) or 16, encoded in the 'hw' field as &lt;shift&gt;/16.

For the '64-bit' variant: is the amount by which to shift the immediate left, either 0 (the default), 16, 32 or 48, encoded in the 'hw' field as &lt;shift&gt;/16.

## &lt;Xd&gt;

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## Operation

```
bits(datasize) result = result<pos+15:pos> = imm; X[d, datasize] = result;
```

```
X[d, datasize];
```
