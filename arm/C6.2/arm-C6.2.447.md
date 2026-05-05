## C6.2.447 STURH

Store register halfword (unscaled)

This instruction calculates an address from a base register value and an immediate offset, and stores a halfword to the calculated address, from a 32-bit register. For information about addressing modes, see Load/Store addressing modes.

<!-- image -->

## Encoding

```
STURH <Wt>, [<Xn|SP>{, #<simm>}]
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
constant integer n = UInt(Rn); constant integer t = UInt(Rt); constant integer{} datasize = 16; constant boolean nontemporal = FALSE; constant boolean tagchecked = n != 31;
```

## Operation

```
bits(64) address; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescGPR(MemOp_STORE, nontemporal, privileged, tagchecked, t); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; address = AddressAdd(address, offset, accdesc); Mem[address, datasize DIV 8, accdesc] = X[t, datasize];
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
