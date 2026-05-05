## C6.2.208 LDIAPP

Load-Acquire RCpc ordered pair of registers

This instruction calculates an address from a base register value and an optional offset, loads two 32-bit words or two 64-bit doublewords from memory, and writes them to two registers. For information on single-copy atomicity and alignment requirements, see Requirements for single-copy atomicity and Alignment of data accesses. The instruction also has memory ordering semantics, as described in Load-Acquire, Load-AcquirePC, and Store-Release, except that:

- The Memory effects associated with Xt1/Wt1 are Ordered-before the Memory effects associated with Xt2/Wt2.
- If the destination registers are not both WZR or not both XZR , LDIAPP loads from memory with Acquire semantics.
- There is no ordering requirement, separate from the requirements of a Load-AcquirePC or a Store-Release, created by having a Store-Release followed by a Load-AcquirePC instruction.
- The reading of a value written by a Store-Release by a Load-AcquirePC instruction by the same observer does not make the write of the Store-Release globally observed.

For information about addressing modes, see Load/Store addressing modes.

## Integer

(FEAT\_LRCPC3)

<!-- image -->

## Encoding for the 32-bit post-index variant

```
Applies when
```

```
(size == 10 && opc2 == 0000) LDIAPP <Wt1>, <Wt2>, [<Xn|SP>], #8
```

## Encoding for the 32-bit variant

```
Applies when (size == 10 && opc2 == 0001) LDIAPP <Wt1>, <Wt2>, [<Xn|SP>]
```

## Encoding for the 64-bit post-index variant

```
Applies when (size == 11 && opc2 == 0000) LDIAPP <Xt1>, <Xt2>, [<Xn|SP>], #16
```

## Encoding for the 64-bit variant

```
Applies when (size == 11 && opc2 == 0001) LDIAPP <Xt1>, <Xt2>, [<Xn|SP>]
```

## Decode for all variants of this encoding

```
EndOfDecode(Decode_UNDEF);
```

```
if !IsFeatureImplemented(FEAT_LRCPC3) then constant boolean ispair = TRUE; constant boolean postindex = opc2<0> == '0'; boolean wback = opc2<0> == '0';
```

LDIAPP has the same CONSTRAINED UNPREDICTABLE behavior as LDP . For information about this CONSTRAINED UNPREDICTABLE behavior, see Architectural Constraints on UNPREDICTABLE behaviors, and particularly LDP and LDIAPP.

## Assembler Symbols

## &lt;Wt1&gt;

Is the 32-bit name of the first general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Wt2&gt;

Is the 32-bit name of the second general-purpose register to be transferred, encoded in the 'Rt2' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;Xt1&gt;

Is the 64-bit name of the first general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Xt2&gt;

Is the 64-bit name of the second general-purpose register to be transferred, encoded in the 'Rt2' field.

## Shared Decode

```
constant integer t = UInt(Rt); constant integer t2 = UInt(Rt2); constant integer n = UInt(Rn); constant integer{} scale = 2 + UInt(size<0>); constant integer{} datasize = 8 << scale; constant integer offset = if opc2<0> == '0' then (2 << scale) else 0; constant boolean acqrel = t != 31 && t2 != 31; constant boolean tagchecked = wback || n != 31; boolean rt_unknown = FALSE; boolean wb_unknown = FALSE; if wback && (t == n || t2 == n) && n != 31 then constant Constraint c = ConstrainUnpredictable(Unpredictable_WBOVERLAPLD); assert c IN {Constraint_WBSUPPRESS, Constraint_UNKNOWN, Constraint_UNDEF, Constraint_NOP}; case c of when Constraint_WBSUPPRESS wback = FALSE; // writeback is suppressed when Constraint_UNKNOWN wb_unknown = TRUE; // writeback is UNKNOWN when Constraint_UNDEF EndOfDecode(Decode_UNDEF); when Constraint_NOP EndOfDecode(Decode_NOP); end end if t == t2 then constant Constraint c = ConstrainUnpredictable(Unpredictable_LDPOVERLAP); assert c IN {Constraint_UNKNOWN, Constraint_UNDEF, Constraint_NOP}; case c of when Constraint_UNKNOWN rt_unknown = TRUE; // result is UNKNOWN when Constraint_UNDEF EndOfDecode(Decode_UNDEF); when Constraint_NOP EndOfDecode(Decode_NOP); end end
```

## Operation

```
bits(64) address; bits(datasize) data1; bits(datasize) data2; constant integer dbytes = datasize DIV 8; constant AccessDescriptor accdesc = CreateAccDescLDAcqPC(tagchecked, ispair, acqrel, t, t2); if n == 31 then
```

```
CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; if !postindex then address = AddressAdd(address, offset, accdesc); bits(2*datasize) full_data; full_data = Mem[address, 2*dbytes, accdesc]; if BigEndian(accdesc.acctype) then data2 = full_data<(datasize-1):0>; data1 = full_data<(2*datasize-1):datasize>; else data1 = full_data<(datasize-1):0>; data2 = full_data<(2*datasize-1):datasize>; if rt_unknown then data1 = bits(datasize) UNKNOWN; data2 = bits(datasize) UNKNOWN; X[t, datasize] = data1; X[t2, datasize] = data2; if wback then if wb_unknown then address = bits(64) UNKNOWN; elsif postindex then address = AddressAdd(address, offset, accdesc); if n == 31 then SP[64] = address; else X[n, 64] = address;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
