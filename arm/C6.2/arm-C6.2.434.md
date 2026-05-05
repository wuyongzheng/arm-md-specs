## C6.2.434 STTR

Store register (unprivileged)

This instruction stores a word or doubleword from a register to memory. The address that is used for the store is calculated from a base register and an immediate offset.

Explicit Memory effects produced by the instruction behave as if the instruction was executed at EL0 if the Effective value of PSTATE.UAO is 0 and either:

- The instruction is executed at EL1.
- The instruction is executed at EL2 when the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}.

Otherwise, the Explicit Memory effects operate with the restrictions determined by the Exception level at which the instruction is executed.

For information about addressing modes, see Load/Store addressing modes.

<!-- image -->

## Encoding for the 32-bit variant

Applies when (size ==

```
10) STTR <Wt>, [<Xn|SP>{, #<simm>}]
```

## Encoding for the 64-bit variant

Applies when (size ==

```
11) STTR <Xt>, [<Xn|SP>{, #<simm>}]
```

## Decode for all variants of this encoding

```
constant integer scale = UInt(size); constant bits(64) offset = SignExtend(imm9, 64);
```

## Assembler Symbols

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;simm&gt;

Is the optional signed immediate byte offset, in the range -256 to 255, defaulting to 0 and encoded in the 'imm9' field.

## &lt;Xt&gt;

Is the 64-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## Shared Decode

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer{} datasize = 8 << constant boolean nontemporal = FALSE; constant boolean tagchecked = n != 31;
```

## Operation

```
bits(64) address; constant boolean privileged = AArch64.IsUnprivAccessPriv(); constant AccessDescriptor accdesc = CreateAccDescGPR(MemOp_STORE, nontemporal, privileged, tagchecked, t); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; address = AddressAdd(address, offset, accdesc); Mem[address, datasize DIV 8, accdesc] = X[t, datasize];
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
scale;
```
