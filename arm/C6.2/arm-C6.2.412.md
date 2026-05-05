## C6.2.412 STNP

Store pair of registers, with non-temporal hint

This instruction calculates an address from a base register value and an immediate offset, and stores two 32-bit words or two 64-bit doublewords to the calculated address, from two registers. For information about addressing modes, see Load/Store addressing modes. For information about non-temporal pair instructions, see Load/Store non-temporal pair.

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (opc == 00) STNP
```

```
<Wt1>, <Wt2>, [<Xn|SP>{, #<imm>}]
```

## Encoding for the 64-bit variant

```
Applies when (opc == 10) STNP
```

```
<Xt1>, <Xt2>, [<Xn|SP>{, #<imm>}]
```

## Decode for all variants of this encoding

```
constant integer t = UInt(Rt); constant integer t2 = UInt(Rt2); constant integer n = UInt(Rn); constant boolean nontemporal = TRUE; constant integer scale = 2 + UInt(opc<1>); constant integer datasize = 8 << scale; constant bits(64) offset = LSL(SignExtend(imm7, 64), scale); constant boolean tagchecked = n != 31;
```

## Assembler Symbols

## &lt;Wt1&gt;

Is the 32-bit name of the first general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Wt2&gt;

Is the 32-bit name of the second general-purpose register to be transferred, encoded in the 'Rt2' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;imm&gt;

For the '32-bit' variant: is the optional signed immediate byte offset, a multiple of 4 in the range -256 to 252, defaulting to 0 and encoded in the 'imm7' field as &lt;imm&gt;/4.

For the '64-bit' variant: is the optional signed immediate byte offset, a multiple of 8 in the range -512 to 504, defaulting to 0 and encoded in the 'imm7' field as &lt;imm&gt;/8.

## &lt;Xt1&gt;

Is the 64-bit name of the first general-purpose register to be transferred, encoded in the 'Rt' field.

<!-- image -->

Is the 64-bit name of the second general-purpose register to be transferred, encoded in the 'Rt2' field.

## Operation

```
bits(64) address; constant integer dbytes = datasize DIV 8; constant boolean privileged = PSTATE.EL != EL0; constant boolean ispair = TRUE; constant AccessDescriptor accdesc = CreateAccDescGPR(MemOp_STORE, nontemporal, privileged, tagchecked, ispair, t, t2); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; address = AddressAdd(address, offset, accdesc); constant bits(2*datasize) data = (if BigEndian(accdesc.acctype) then X[t, datasize]:X[t2, datasize] else X[t2, datasize]:X[t, datasize]); Mem[address, 2 * dbytes, accdesc] = data;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
