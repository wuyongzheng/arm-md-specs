## C6.2.396 STGP

Store Allocation Tag and pair of registers

This instruction stores an Allocation Tag and two 64-bit doublewords to memory, from two registers. The address used for the store is calculated from the base register and an immediate signed offset scaled by the Tag Granule. The Allocation Tag is calculated from the Logical Address Tag in the base register.

This instruction generates an Unchecked access.

It has encodings from 3 classes: Post-index, Pre-index, and Signed offset

## Post-index

(FEAT\_MTE)

<!-- image -->

## Encoding

```
STGP <Xt1>, <Xt2>, [<Xn|SP>], #<imm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_MTE) then EndOfDecode(Decode_UNDEF); constant integer t = UInt(Rt); constant integer t2 = UInt(Rt2); constant integer n = UInt(Rn); constant bits(64) offset = LSL(SignExtend(simm7, 64), LOG2_TAG_GRANULE); constant boolean writeback = TRUE; constant boolean postindex = TRUE;
```

## Pre-index

(FEAT\_MTE)

<!-- image -->

## Encoding

```
STGP <Xt1>, <Xt2>, [<Xn|SP>, #<imm>]!
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_MTE) then EndOfDecode(Decode_UNDEF); constant integer t = UInt(Rt); constant integer t2 = UInt(Rt2); constant integer n = UInt(Rn); constant bits(64) offset = LSL(SignExtend(simm7, 64), constant boolean writeback = TRUE; constant boolean postindex = FALSE;
```

```
LOG2_TAG_GRANULE);
```

## Signed offset

(FEAT\_MTE)

<!-- image -->

## Encoding

```
STGP <Xt1>, <Xt2>, [<Xn|SP>{, #<imm>}]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_MTE) then EndOfDecode(Decode_UNDEF); constant integer t = UInt(Rt); constant integer t2 = UInt(Rt2); constant integer n = UInt(Rn); constant bits(64) offset = LSL(SignExtend(simm7, 64), LOG2_TAG_GRANULE); constant boolean writeback = FALSE; constant boolean postindex = FALSE;
```

## Assembler Symbols

## &lt;Xt1&gt;

Is the 64-bit name of the first general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Xt2&gt;

Is the 64-bit name of the second general-purpose register to be transferred, encoded in the 'Rt2' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;imm&gt;

For the 'Post-index' and 'Pre-index' variants: is the signed immediate offset, a multiple of 16 in the range -1024 to 1008, encoded in the 'simm7' field.

For the 'Signed offset' variant: is the optional signed immediate offset, a multiple of 16 in the range -1024 to 1008, defaulting to 0 and encoded in the 'simm7' field.

## Operation

```
bits(64) address; if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; constant boolean stzgm = FALSE; constant boolean ispair = TRUE; constant AccessDescriptor accdesc = CreateAccDescLDGSTG(MemOp_STORE, stzgm, ispair, t, t2); if !postindex then address = AddressAdd(address, offset, accdesc);
```

```
if !IsAligned(address, TAG_GRANULE) then constant FaultRecord fault = AlignmentFault(accdesc, address); AArch64.Abort(fault); constant bits(128) data = (if BigEndian(accdesc.acctype) then X[t, 64]:X[t2, 64] else X[t2, 64]:X[t, 64]); Mem[address, 16, accdesc] = data; AArch64.MemTag[address, accdesc] = AArch64.AllocationTagFromAddress(address); if writeback then if postindex then address = AddressAdd(address, offset, accdesc); if n == 31 then SP[64] = address; else X[n, 64] = address;
```
