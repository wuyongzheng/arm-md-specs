## C6.2.397 STILP

Store-release ordered pair of registers

This instruction calculates an address from a base register value and an optional offset, and stores two 32-bit words or two 64-bit doublewords to the calculated address, from two registers. For information on single-copy atomicity and alignment requirements, see Requirements for single-copy atomicity and Alignment of data accesses. The instruction also has memory ordering semantics, as described in Load-Acquire, Load-AcquirePC, and Store-Release, with the additional requirement that:

- When using the pre-index addressing mode, the Memory effects associated with Xt2/Wt2 are Ordered-before the Memory effects associated with Xt1/Wt1.
- For all other addressing modes, the Memory effects associated with Xt1/Wt1 are Ordered-before the Memory effects associated with Xt2/Wt2.

For information about addressing modes, see Load/Store addressing modes.

## Integer

(FEAT\_LRCPC3)

<!-- image -->

## Encoding for the 32-bit pre-index variant

```
Applies when (size == 10 && opc2 == 0000) STILP <Wt1>, <Wt2>, [<Xn|SP>, #-8]!
```

## Encoding for the 32-bit variant

```
Applies when (size == 10 && opc2 == 0001) STILP <Wt1>, <Wt2>, [<Xn|SP>]
```

## Encoding for the 64-bit pre-index variant

```
== 0000)
```

```
Applies when (size == 11 && opc2 STILP <Xt1>, <Xt2>, [<Xn|SP>, #-16]!
```

## Encoding for the 64-bit variant

```
Applies when (size == 11 && opc2 == 0001) STILP <Xt1>, <Xt2>, [<Xn|SP>]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_LRCPC3) then constant boolean ispair = TRUE; constant boolean wback = opc2<0> == '0';
```

```
EndOfDecode(Decode_UNDEF);
```

STILP has the same CONSTRAINED UNPREDICTABLE behavior as STP . For information about this CONSTRAINED UNPREDICTABLE behavior, see Architectural Constraints on UNPREDICTABLE behaviors, and particularly STP and STILP.

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
constant integer t = UInt(Rt); constant integer t2 = UInt(Rt2); constant integer n = UInt(Rn); constant integer{} scale = 2 + UInt(size<0>); constant integer{} datasize = 8 << scale; constant integer offset = if opc2<0> == '0' then -1 * (2 << scale) else 0; constant boolean acqrel = FALSE; constant boolean tagchecked = wback || n != 31; boolean rt_unknown = FALSE; if wback && (t == n || t2 == n) && n != 31 then constant Constraint c = ConstrainUnpredictable(Unpredictable_WBOVERLAPST); assert c IN {Constraint_NONE, Constraint_UNKNOWN, Constraint_UNDEF, Constraint_NOP}; case c of when Constraint_NONE rt_unknown = FALSE; // value stored is pre-writeback when Constraint_UNKNOWN rt_unknown = TRUE; // value stored is UNKNOWN when Constraint_UNDEF EndOfDecode(Decode_UNDEF); when Constraint_NOP EndOfDecode(Decode_NOP); end end
```

## Operation

```
bits(64) address; bits(datasize) data1; bits(datasize) data2; constant integer dbytes = datasize DIV 8; AccessDescriptor accdesc = CreateAccDescAcqRel(MemOp_STORE, tagchecked, ispair, acqrel, t, t2); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; address = AddressAdd(address, offset, accdesc); if rt_unknown && t == n then data1 = bits(datasize) UNKNOWN; else data1 = X[t, datasize];
```

```
if rt_unknown && t2 == n then data2 = bits(datasize) UNKNOWN; else data2 = X[t2, datasize]; bits(2*datasize) full_data; if BigEndian(accdesc.acctype) then full_data = data1:data2; else full_data = data2:data1; accdesc.highestaddressfirst = offset < 0; Mem[address, 2*dbytes, accdesc] = full_data; if wback then if n == 31 then SP[64] = address; else X[n, 64] = address;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
