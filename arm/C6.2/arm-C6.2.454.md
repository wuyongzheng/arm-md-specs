## C6.2.454 STZGM

Store Allocation Tag and zero multiple

This instruction writes a naturally aligned block of N Allocation Tags and stores zero to the associated data locations, where the size of N is identified in DCZID\_EL0.BS, and the Allocation Tag is taken from the source register bits&lt;3:0&gt;.

This instruction is UNDEFINED at EL0.

This instruction generates an Unchecked access.

## Integer

(FEAT\_MTE2)

<!-- image -->

## Encoding

```
STZGM <Xt>, [<Xn|SP>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_MTE2) then constant integer t = UInt(Rt); constant integer n = UInt(Rn);
```

## Assembler Symbols

&lt;Xt&gt;

Is the 64-bit name of the general-purpose source register, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## Operation

```
if PSTATE.EL == EL0 then UNDEFINED; constant bits(64) data = X[t, 64]; constant bits(4) tag = data<3:0>; bits(64) address; if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; constant integer size = 4 * (2 ^ (UInt(DCZID_EL0.BS))); address = Align(address, size); constant integer count = size >> LOG2_TAG_GRANULE; constant boolean stzgm = TRUE; constant AccessDescriptor accdesc = CreateAccDescLDGSTG(MemOp_STORE, stzgm, t); for i = 0 to count-1 AArch64.MemTag[address, accdesc] = tag; Mem[address, TAG_GRANULE, accdesc] = Zeros(8*TAG_GRANULE); address = AddressIncrement(address, TAG_GRANULE, accdesc);
```

```
EndOfDecode(Decode_UNDEF);
```
