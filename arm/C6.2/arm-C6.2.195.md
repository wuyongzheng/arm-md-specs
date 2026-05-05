## C6.2.195 LDAXP

Load-acquire exclusive pair of registers

This instruction derives an address from a base register value, loads two 32-bit words or two 64-bit doublewords from memory, and writes them to two registers. For information on single-copy atomicity and alignment requirements, see Requirements for single-copy atomicity and Alignment of data accesses. The PE marks the physical address being accessed as an exclusive access. This exclusive access mark is checked by Store Exclusive instructions. See Synchronization and semaphores.

If the destination registers are not both WZR or not both XZR , LDAXP loads from memory with Acquire semantics.

For more information about memory ordering semantics, see Load-Acquire, Load-AcquirePC, and Store-Release.

For information about addressing modes, see Load/Store addressing modes.

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (sz == 0) LDAXP
```

```
<Wt1>, <Wt2>, [<Xn|SP>{, #0}]
```

## Encoding for the 64-bit variant

```
Applies when (sz == 1) LDAXP
```

```
<Xt1>, <Xt2>, [<Xn|SP>{, #0}]
```

## Decode for all variants of this encoding

```
constant integer t = UInt(Rt); constant integer t2 = UInt(Rt2); constant integer n = UInt(Rn); constant integer elsize = 32 << UInt(sz); constant integer datasize = elsize * 2; constant boolean acqrel = t != 31 && t2 != 31; constant boolean tagchecked = n != 31; boolean rt_unknown = FALSE; if t == t2 then constant Constraint c = ConstrainUnpredictable(Unpredictable_LDPOVERLAP); assert c IN {Constraint_UNKNOWN, Constraint_UNDEF, Constraint_NOP}; case c of when Constraint_UNKNOWN rt_unknown = TRUE; // result is UNKNOWN when Constraint_UNDEF EndOfDecode(Decode_UNDEF); when Constraint_NOP EndOfDecode(Decode_NOP);
```

For information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors, and particularly LDAXP.

## Assembler Symbols

&lt;Wt1&gt;

Is the 32-bit name of the first general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Wt2&gt;

Is the 32-bit name of the second general-purpose register to be transferred, encoded in the 'Rt2' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;Xt1&gt;

Is the 64-bit name of the first general-purpose register to be transferred, encoded in the 'Rt' field.

&lt;Xt2&gt;

Is the 64-bit name of the second general-purpose register to be transferred, encoded in the 'Rt2' field.

## Operation

```
bits(64) address; bits(datasize) data; constant integer dbytes = datasize DIV 8; constant boolean privileged = PSTATE.EL != EL0; constant boolean ispair = elsize == 64; // When elsize is 32, the access is single-copy atomic constant AccessDescriptor accdesc = CreateAccDescExLDST(MemOp_LOAD, acqrel, tagchecked, privileged, ispair, t, t2); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; AArch64.SetExclusiveMonitors(address, dbytes, accdesc); data = Mem[address, dbytes, accdesc]; if rt_unknown then // ConstrainedUNPREDICTABLE case X[t, datasize] = bits(datasize) UNKNOWN; // In this case t = t2 elsif BigEndian(accdesc.acctype) then X[t, elsize] = data<elsize +: elsize>; X[t2, elsize] = data<0 +: elsize>; else X[t, elsize] = data<0 +: elsize>; X[t2, elsize] = data<elsize +: elsize>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
