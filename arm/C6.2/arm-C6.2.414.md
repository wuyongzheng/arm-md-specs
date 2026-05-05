## C6.2.414 STR (immediate)

Store register (immediate)

This instruction stores a word or a doubleword from a register to memory. The address that is used for the store is calculated from a base register and an immediate offset. For information about addressing modes, see Load/Store addressing modes.

It has encodings from 3 classes: Post-index, Pre-index, and Unsigned offset

## Post-index

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (size == 10) STR <Wt>, [<Xn|SP>], #<simm>
```

## Encoding for the 64-bit variant

```
Applies when (size == 11) STR <Xt>, [<Xn|SP>], #<simm>
```

## Decode for all variants of this encoding

```
constant boolean wback = TRUE; constant boolean postindex = TRUE; constant integer scale = UInt(size); constant bits(64) offset
```

## Pre-index

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (size == 10) STR <Wt>, [<Xn|SP>, #<simm>]!
```

## Encoding for the 64-bit variant

```
Applies when (size == 11) STR <Xt>, [<Xn|SP>, #<simm>]!
```

```
= SignExtend(imm9, 64);
```

## Decode for all variants of this encoding

```
constant boolean wback = TRUE; constant boolean postindex = FALSE; constant integer scale = UInt(size); constant bits(64) offset
```

## Unsigned offset

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (size == 10) STR <Wt>, [<Xn|SP>{, #<pimm>}]
```

## Encoding for the 64-bit variant

```
Applies when (size == 11) STR <Xt>, [<Xn|SP>{, #<pimm>}]
```

## Decode for all variants of this encoding

```
constant boolean wback = FALSE; constant boolean postindex = FALSE; constant integer scale = UInt(size); constant bits(64) offset = LSL(ZeroExtend(imm12, 64),
```

## Assembler Symbols

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;simm&gt;

Is the signed immediate byte offset, in the range -256 to 255, encoded in the 'imm9' field.

## &lt;Xt&gt;

Is the 64-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;pimm&gt;

For the '32-bit' variant: is the optional positive immediate byte offset, a multiple of 4 in the range 0 to 16380, defaulting to 0 and encoded in the 'imm12' field as &lt;pimm&gt;/4.

For the '64-bit' variant: is the optional positive immediate byte offset, a multiple of 8 in the range 0 to 32760, defaulting to 0 and encoded in the 'imm12' field as &lt;pimm&gt;/8.

```
= SignExtend(imm9, 64);
```

```
scale);
```

## Shared Decode

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer{} datasize = 8 << scale; constant boolean nontemporal = FALSE; constant boolean tagchecked = wback || n != 31; Constraint c; boolean rt_unknown = FALSE; if wback && n == t && n != 31 then c = ConstrainUnpredictable(Unpredictable_WBOVERLAPST); assert c IN {Constraint_NONE, Constraint_UNKNOWN, Constraint_UNDEF, Constraint_NOP}; case c of when Constraint_NONE rt_unknown = FALSE; // Value stored is original value when Constraint_UNKNOWN rt_unknown = TRUE; // Value stored is UNKNOWN when Constraint_UNDEF EndOfDecode(Decode_UNDEF); when Constraint_NOP EndOfDecode(Decode_NOP); end end
```

## Operation

```
bits(64) address; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescGPR(MemOp_STORE, nontemporal, privileged, tagchecked, t); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; if !postindex then address = AddressAdd(address, offset, accdesc); bits(datasize) data; if rt_unknown then data = bits(datasize) UNKNOWN; else data = X[t, datasize]; Mem[address, datasize DIV 8, accdesc] = data; if wback then if postindex then address = AddressAdd(address, offset, accdesc); if n == 31 then SP[64] = address; else X[n, 64] = address;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
