## C6.2.182 LDAPR

Load-acquire RCpc register

This instruction derives an address from a base register value, loads a 32-bit word or 64-bit doubleword from the derived address in memory, and writes it to a register.

If the destination register is not one of WZR or XZR , LDAPR loads from memory with AcquirePC semantics.

For more information about memory ordering semantics, see Load-Acquire, Load-AcquirePC, and Store-Release.

For information about addressing modes, see Load/Store addressing modes.

It has encodings from 2 classes: Post-index and No offset

## Post-index

(FEAT\_LRCPC3)

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when 10)
```

```
(size == LDAPR <Wt>, [<Xn|SP>], #4
```

## Encoding for the 64-bit variant

```
Applies when 11)
```

```
(size == LDAPR <Xt>, [<Xn|SP>], #8
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_LRCPC3) then EndOfDecode(Decode_UNDEF); constant integer t = UInt(Rt); constant integer n = UInt(Rn); boolean wback = TRUE; constant boolean acquirepc = t != 31; constant integer regsize = if size == '11' then 64 else 32; constant integer datasize = 8 << UInt(size); constant integer offset = 1 << UInt(size); constant boolean tagchecked = TRUE; boolean wb_unknown = FALSE; if n == t && n != 31 then constant Constraint c = ConstrainUnpredictable(Unpredictable_WBOVERLAPLD); assert c IN {Constraint_WBSUPPRESS, Constraint_UNKNOWN, Constraint_UNDEF, Constraint_NOP}; case c of when Constraint_WBSUPPRESS wback = FALSE; // writeback is suppressed when Constraint_UNKNOWN wb_unknown = TRUE; // writeback is UNKNOWN when Constraint_UNDEF EndOfDecode(Decode_UNDEF); when Constraint_NOP EndOfDecode(Decode_NOP);
```

## No offset

(FEAT\_LRCPC)

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (size == 10) LDAPR <Wt>, [<Xn|SP>
```

```
{, #0}]
```

## Encoding for the 64-bit variant

```
Applies when (size == 11) LDAPR <Xt>, [<Xn|SP> {, #0}]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_LRCPC) then EndOfDecode(Decode_UNDEF); constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant boolean wback = FALSE; constant integer offset = 0; constant boolean wb_unknown = FALSE; constant integer elsize = 8 << UInt(size); constant integer regsize = if elsize == 64 then 64 else 32; constant integer datasize = elsize; constant boolean acquirepc = t != 31; constant boolean tagchecked = n != 31;
```

## Assembler Symbols

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be loaded, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;Xt&gt;

Is the 64-bit name of the general-purpose register to be loaded, encoded in the 'Rt' field.

## Operation

```
bits(64) address; bits(datasize) data; constant integer dbytes = datasize DIV 8; constant AccessDescriptor accdesc = CreateAccDescLDAcqPC(tagchecked, acquirepc, t); if n == 31 then CheckSPAlignment(); address = SP[64]; else
```

```
address = X[n, 64]; data = Mem[address, dbytes, accdesc]; X[t, regsize] = ZeroExtend(data, regsize); if wback then if wb_unknown then address = bits(64) UNKNOWN; else address = AddressAdd(address, offset, accdesc); if n == 31 then SP[64] = address; else X[n, 64] = address;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
