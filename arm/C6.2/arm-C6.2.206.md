## C6.2.206 LDG

## Load Allocation Tag

This instruction loads an Allocation Tag from a memory address, generates a Logical Address Tag from the Allocation Tag and merges it into the destination register. The address used for the load is calculated from the base register and an immediate signed offset scaled by the Tag Granule.

## Integer

(FEAT\_MTE)

<!-- image -->

## Encoding

```
LDG
```

```
<Xt>, [<Xn|SP>{, #<simm>}]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_MTE) then EndOfDecode(Decode_UNDEF); constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant bits(64) offset = LSL(SignExtend(imm9, 64), LOG2_TAG_GRANULE);
```

## Assembler Symbols

## &lt;Xt&gt;

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;simm&gt;

Is the optional signed immediate offset, a multiple of 16 in the range -4096 to 4080, defaulting to 0 and encoded in the 'imm9' field.

## Operation

```
bits(64) address; bits(4) tag; if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; constant boolean stzgm = FALSE; constant AccessDescriptor accdesc address = AddressAdd(address, offset, accdesc); address = Align(address, TAG_GRANULE); tag = AArch64.MemTag[address, accdesc]; X[t, 64] = AArch64.AddressWithAllocationTag(X[t, 64], tag);
```

```
= CreateAccDescLDGSTG(MemOp_LOAD, stzgm, t);
```
