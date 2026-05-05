## C6.2.262 LDURSH

Load register signed halfword (unscaled)

This instruction calculates an address from a base register and an immediate offset, loads a signed halfword from memory, sign-extends it, and writes it to a register. For information about addressing modes, see Load/Store addressing modes.

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (opc == 11) LDURSH
```

```
<Wt>, [<Xn|SP>{, #<simm>}]
```

## Encoding for the 64-bit variant

```
Applies when (opc == 10) LDURSH
```

```
<Xt>, [<Xn|SP>{, #<simm>}]
```

## Decode for all variants of this encoding

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

## &lt;Xt&gt;

Is the 64-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## Shared Decode

```
constant integer n = UInt(Rn); constant integer t = UInt(Rt); constant integer{} datasize = 16; constant integer{} regsize = 64 >> UInt(opc<0>); constant boolean nontemporal = FALSE; constant boolean tagchecked = n != 31;
```

## Operation

```
bits(64) address; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescGPR(MemOp_LOAD, nontemporal, privileged, tagchecked, t); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; address = AddressAdd(address, offset, accdesc); constant bits(datasize) data = Mem[address, datasize DIV 8, accdesc]; X[t, regsize] = SignExtend(data, regsize);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
