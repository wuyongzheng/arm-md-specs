## C6.2.7 ADDG

Add with tag

This instruction adds an immediate value scaled by the Tag Granule to the address in the source register, modifies the Logical Address Tag of the address using an immediate value, and writes the result to the destination register. Tags specified in GCR\_EL1.Exclude are excluded from the possible outputs when modifying the Logical Address Tag.

## Integer

(FEAT\_MTE)

<!-- image -->

## Encoding

```
ADDG <Xd|SP>, <Xn|SP>, #<uimm6>, #<uimm4>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_MTE) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant bits(4) tag_offset = imm4; constant bits(64) offset = LSL(ZeroExtend(imm6, 64),
```

## Assembler Symbols

## &lt;Xd|SP&gt;

Is the 64-bit name of the destination general-purpose register or stack pointer, encoded in the 'Rd' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the source general-purpose register or stack pointer, encoded in the 'Rn' field.

## &lt;uimm6&gt;

Is an unsigned immediate, a multiple of 16 in the range 0 to 1008, encoded in the 'imm6' field.

## &lt;uimm4&gt;

Is an unsigned immediate, in the range 0 to 15, encoded in the 'imm4' field.

## Operation

```
constant bits(64) operand1 = if n == 31 then SP[64] else X[n, 64]; constant bits(4) start_tag = AArch64.AllocationTagFromAddress(operand1); constant bits(16) exclude = GCR_EL1.Exclude; constant bits(4) rtag = AArch64.ChooseNonExcludedTagOrZero(start_tag, tag_offset, exclude); bits(64) result; (result, -) = AddWithCarry(operand1, offset, '0'); result = AArch64.AddressWithAllocationTag(result, rtag); if d == 31 then SP[64] = result; else X[d, 64] = result;
```

```
LOG2_TAG_GRANULE);
```
