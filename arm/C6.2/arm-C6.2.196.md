## C6.2.196 LDAXR

Load-acquire exclusive register

This instruction derives an address from a base register value, loads a 32-bit word or 64-bit doubleword from memory, and writes it to a register. The memory access is atomic. The PE marks the physical address being accessed as an exclusive access. This exclusive access mark is checked by Store Exclusive instructions. See Synchronization and semaphores.

If the destination register is not one of WZR or XZR , LDAXR loads from memory with Acquire semantics.

For more information about memory ordering semantics, see Load-Acquire, Load-AcquirePC, and Store-Release.

For information about addressing modes, see Load/Store addressing modes.

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (size == 10) LDAXR <Wt>, [<Xn|SP>{, #0}]
```

## Encoding for the 64-bit variant

```
Applies when (size == 11) LDAXR <Xt>, [<Xn|SP>{, #0}]
```

## Decode for all variants of this encoding

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer elsize = 8 << UInt(size); constant integer regsize = if elsize == 64 then 64 else constant boolean acqrel = t != 31; constant boolean tagchecked = n != 31;
```

## Assembler Symbols

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;Xt&gt;

```
32;
```

Is the 64-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## Operation

```
bits(64) address; bits(elsize) data; constant integer dbytes = elsize DIV 8; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescExLDST(MemOp_LOAD, acqrel, tagchecked, privileged, t); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; AArch64.SetExclusiveMonitors(address, dbytes, accdesc); data = Mem[address, dbytes, accdesc]; X[t, regsize] = ZeroExtend(data, regsize);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
