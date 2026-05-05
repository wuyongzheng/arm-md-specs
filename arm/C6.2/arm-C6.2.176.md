## C6.2.176 IRG

Insert random tag

This instruction inserts a random Logical Address Tag into the address in the first source register, and writes the result to the destination register. Any tags specified in the optional second source register or in GCR\_EL1.Exclude are excluded from the selection of the random Logical Address Tag.

## Integer

(FEAT\_MTE)

<!-- image -->

## Encoding

```
IRG <Xd|SP>, <Xn|SP>{, <Xm>}
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_MTE) then EndOfDecode(Decode_UNDEF);
```

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm);
```

## Assembler Symbols

## &lt;Xd|SP&gt;

Is the 64-bit name of the destination general-purpose register or stack pointer, encoded in the 'Rd' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the first source general-purpose register or stack pointer, encoded in the 'Rn' field.

## &lt;Xm&gt;

Is the 64-bit name of the second general-purpose source register, encoded in the 'Rm' field. Defaults to XZR if absent.

## Operation

```
constant bits(64) operand = if n == 31 then SP[64] else X[n, 64]; constant bits(64) exclude_reg = X[m, 64]; constant bits(16) exclude = exclude_reg<15:0> OR GCR_EL1.Exclude; constant bits(4) rtag = AArch64.ChooseTagOrZero(exclude); constant bits(64) result = AArch64.AddressWithAllocationTag(operand, rtag); if d == 31 then SP[64] = result; else X[d, 64] = result;
```
