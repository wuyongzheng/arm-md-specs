## C6.2.207 LDGM

## Load tag multiple

This instruction reads a naturally aligned block of N Allocation Tags, where the size of N is identified in GMID\_EL1.BS, and writes the Allocation Tag read from address A to the destination register at 4*A&lt;7:4&gt;+3:4*A&lt;7:4&gt;. Bits of the destination register not written with an Allocation Tag are set to 0.

This instruction is UNDEFINED at EL0.

This instruction generates an Unchecked access.

## Integer

(FEAT\_MTE2)

<!-- image -->

## Encoding

```
LDGM <Xt>, [<Xn|SP>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_MTE2) then constant integer t = UInt(Rt); constant integer n = UInt(Rn);
```

## Assembler Symbols

<!-- image -->

&lt;Xt&gt;

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## Operation

```
if PSTATE.EL == EL0 then UNDEFINED; bits(64) data = Zeros(64); bits(64) address; if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; constant integer size = 4 * (2 ^ (UInt(GMID_EL1.BS))); address = Align(address, size); constant integer count = size >> LOG2_TAG_GRANULE; integer index = UInt(address<LOG2_TAG_GRANULE+3:LOG2_TAG_GRANULE>); constant boolean stzgm = FALSE; constant AccessDescriptor accdesc for i = 0 to count-1 constant bits(4) tag = AArch64.MemTag[address, accdesc];
```

```
EndOfDecode(Decode_UNDEF);
```

```
= CreateAccDescLDGSTG(MemOp_LOAD, stzgm, t);
```

```
Elem[data, index, 4] = tag; address = AddressIncrement(address, TAG_GRANULE, accdesc); index = index + 1; X[t, 64] = data;
```
