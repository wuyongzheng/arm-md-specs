## C6.2.401 STLR

## Store-release register

This instruction stores a 32-bit word or a 64-bit doubleword to a memory location, from a register. The instruction also has memory ordering semantics as described in Load-Acquire, Store-Release. For information about addressing modes, see Load/Store addressing modes.

It has encodings from 2 classes: No offset and Pre-index

## No offset

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (size == 10) STLR <Wt>, [<Xn|SP>{, #0}]
```

## Encoding for the 64-bit variant

```
Applies when (size == 11) STLR <Xt>, [<Xn|SP>{, #0}]
```

## Decode for all variants of this encoding

```
UInt(size);
```

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant boolean wback = FALSE; constant integer offset = 0; constant boolean rt_unknown = FALSE; constant integer elsize = 8 << constant integer datasize = elsize; constant boolean acquire = FALSE; constant boolean tagchecked = n != 31;
```

## Pre-index

## (FEAT\_LRCPC3)

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (size == 10) STLR <Wt>, [<Xn|SP>, #-4]!
```

## Encoding for the 64-bit variant

```
Applies when (size == STLR
```

```
11) <Xt>, [<Xn|SP>, #-8]!
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_LRCPC3) then EndOfDecode(Decode_UNDEF); constant boolean wback = TRUE; constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer datasize = 8 << UInt(size); constant integer offset = -1 * (1 << UInt(size)); constant boolean acquire = FALSE; constant boolean tagchecked = TRUE; boolean rt_unknown = FALSE; if n == t && n != 31 then constant Constraint c = ConstrainUnpredictable(Unpredictable_WBOVERLAPST); assert c IN {Constraint_NONE, Constraint_UNKNOWN, Constraint_UNDEF, Constraint_NOP}; case c of when Constraint_NONE rt_unknown = FALSE; // value stored is original value when Constraint_UNKNOWN rt_unknown = TRUE; // value stored is UNKNOWN when Constraint_UNDEF EndOfDecode(Decode_UNDEF); when Constraint_NOP EndOfDecode(Decode_NOP);
```

## Assembler Symbols

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

<!-- image -->

Is the 64-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## Operation

```
bits(64) address; constant integer dbytes = datasize DIV 8; constant AccessDescriptor accdesc = CreateAccDescAcqRel(MemOp_STORE, tagchecked, acquire, t); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; address = AddressAdd(address, offset, accdesc); bits(datasize) data; if rt_unknown then data = bits(datasize) UNKNOWN; else data = X[t, datasize]; Mem[address, dbytes, accdesc] = data; if wback then if n == 31 then
```

```
SP[64] = address; else X[n, 64] = address;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
