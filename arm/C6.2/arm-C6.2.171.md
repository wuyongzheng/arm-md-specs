## C6.2.171 GMI

Tag mask insert

This instruction inserts the tag in the first source register into the excluded set specified in the second source register, writing the new excluded set to the destination register.

## Integer

(FEAT\_MTE)

<!-- image -->

## Encoding

```
GMI <Xd>, <Xn|SP>, <Xm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_MTE) then EndOfDecode(Decode_UNDEF);
```

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm);
```

## Assembler Symbols

## &lt;Xd&gt;

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the first source general-purpose register or stack pointer, encoded in the 'Rn' field.

## &lt;Xm&gt;

Is the 64-bit name of the second general-purpose source register, encoded in the 'Rm' field.

## Operation

```
constant bits(64) address = if n == 31 then SP[64] else X[n, 64]; bits(64) mask = X[m, 64]; constant bits(4) tag = AArch64.AllocationTagFromAddress(address); mask<UInt(tag)> = '1'; X[d, 64] = mask;
```
