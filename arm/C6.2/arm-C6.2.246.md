## C6.2.246 LDTRH

Load register halfword (unprivileged)

This instruction loads a halfword from memory, zero-extends it, and writes the result to a register. The address that is used for the load is calculated from a base register and an immediate offset.

Explicit Memory effects produced by the instruction behave as if the instruction was executed at EL0 if the Effective value of PSTATE.UAO is 0 and either:

- The instruction is executed at EL1.
- The instruction is executed at EL2 when the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}.

Otherwise, the Explicit Memory effects operate with the restrictions determined by the Exception level at which the instruction is executed.

For information about addressing modes, see Load/Store addressing modes.

<!-- image -->

## Encoding

```
LDTRH <Wt>, [<Xn|SP>{, #<simm>}]
```

## Decode for this encoding

```
constant bits(64) offset = SignExtend(imm9, 64);
```

## Assembler Symbols

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;simm&gt;

Is the optional signed immediate byte offset, in the range -256 to 255, defaulting to 0 and encoded in the 'imm9' field.

## Shared Decode

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer{} datasize = 16; constant boolean nontemporal = FALSE; constant boolean tagchecked = n != 31;
```

## Operation

```
bits(64) address; constant boolean privileged = AArch64.IsUnprivAccessPriv(); constant AccessDescriptor accdesc = CreateAccDescGPR(MemOp_LOAD, nontemporal, privileged, tagchecked, t); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; address = AddressAdd(address, offset, accdesc); constant bits(datasize) data = Mem[address, datasize DIV 8, accdesc]; X[t, 32] = ZeroExtend(data, 32);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
