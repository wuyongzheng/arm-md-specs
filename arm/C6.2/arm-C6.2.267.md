## C6.2.267 LDXRH

## Load exclusive register halfword

This instruction derives an address from a base register value, loads a halfword from memory, zero-extends it and writes it to a register. The memory access is atomic. The PE marks the physical address being accessed as an exclusive access. This exclusive access mark is checked by Store Exclusive instructions. See Synchronization and semaphores. For information about addressing modes, see Load/Store addressing modes.

<!-- image -->

## Encoding

```
LDXRH <Wt>, [<Xn|SP>{, #0}]
```

## Decode for this encoding

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant boolean acqrel = FALSE; constant boolean tagchecked =
```

```
n != 31;
```

## Assembler Symbols

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## Operation

```
bits(64) address; bits(16) data; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescExLDST(MemOp_LOAD, acqrel, tagchecked, privileged, t); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; AArch64.SetExclusiveMonitors(address, 2, accdesc); data = Mem[address, 2, accdesc]; X[t, 32] = ZeroExtend(data, 32);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
