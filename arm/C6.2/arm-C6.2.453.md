## C6.2.453 STZG

Store Allocation Tag, zeroing

This instruction stores an Allocation Tag to memory, zeroing the associated data location. The address used for the store is calculated from the base register and an immediate signed offset scaled by the Tag Granule. The Allocation Tag is calculated from the Logical Address Tag in the source register.

This instruction generates an Unchecked access.

It has encodings from 3 classes: Post-index, Pre-index, and Signed offset

## Post-index

(FEAT\_MTE)

<!-- image -->

## Encoding

```
STZG <Xt|SP>, [<Xn|SP>], #<simm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_MTE) then EndOfDecode(Decode_UNDEF); constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant bits(64) offset = LSL(SignExtend(imm9, 64), LOG2_TAG_GRANULE); constant boolean writeback = TRUE; constant boolean postindex = TRUE;
```

## Pre-index

(FEAT\_MTE)

<!-- image -->

## Encoding

```
STZG <Xt|SP>, [<Xn|SP>, #<simm>]!
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_MTE) then EndOfDecode(Decode_UNDEF); constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant bits(64) offset = LSL(SignExtend(imm9, 64), LOG2_TAG_GRANULE); constant boolean writeback = TRUE; constant boolean postindex = FALSE;
```

## Signed offset

(FEAT\_MTE)

<!-- image -->

## Encoding

```
STZG <Xt|SP>, [<Xn|SP>{, #<simm>}]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_MTE) then EndOfDecode(Decode_UNDEF); constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant bits(64) offset = LSL(SignExtend(imm9, 64), LOG2_TAG_GRANULE); constant boolean writeback = FALSE; constant boolean postindex = FALSE;
```

## Assembler Symbols

## &lt;Xt|SP&gt;

Is the 64-bit name of the general-purpose source register or stack pointer, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;simm&gt;

Is the optional signed immediate offset, a multiple of 16 in the range -4096 to 4080, defaulting to 0 and encoded in the 'imm9' field.

## Operation

```
bits(64) address; if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; constant boolean stzgm = FALSE; constant AccessDescriptor accdesc = CreateAccDescLDGSTG(MemOp_STORE, stzgm, t); if !postindex then address = AddressAdd(address, offset, accdesc); if !IsAligned(address, TAG_GRANULE) then constant FaultRecord fault = AlignmentFault(accdesc, address); AArch64.Abort(fault); Mem[address, TAG_GRANULE, accdesc] = Zeros(TAG_GRANULE * 8); constant bits(64) data = if t == 31 then SP[64] else X[t, 64]; constant bits(4) tag = AArch64.AllocationTagFromAddress(data); AArch64.MemTag[address, accdesc] = tag;
```

```
if writeback then if postindex then address = AddressAdd(address, offset, accdesc); if n == 31 then SP[64] = address; else X[n, 64] = address;
```
