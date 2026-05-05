## C6.2.212 LDNP

Load pair of registers, with non-temporal hint

This instruction calculates an address from a base register value and an immediate offset, loads two 32-bit words or two 64-bit doublewords from memory, and writes them to two registers.

For information about addressing modes, see Load/Store addressing modes. For information about non-temporal pair instructions, see Load/Store non-temporal pair.

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (opc == 00) LDNP
```

```
<Wt1>, <Wt2>, [<Xn|SP>{, #<imm>}]
```

## Encoding for the 64-bit variant

```
Applies when (opc == 10) LDNP
```

```
<Xt1>, <Xt2>, [<Xn|SP>{, #<imm>}]
```

## Decode for all variants of this encoding

```
constant integer t = UInt(Rt); constant integer t2 = UInt(Rt2); constant integer n = UInt(Rn); constant boolean nontemporal = TRUE; constant integer scale = 2 + UInt(opc<1>); constant integer datasize = 8 << scale; constant bits(64) offset = LSL(SignExtend(imm7, 64), scale); constant boolean tagchecked = n != 31; boolean rt_unknown = FALSE; if t == t2 then constant Constraint c = ConstrainUnpredictable(Unpredictable_LDPOVERLAP); assert c IN {Constraint_UNKNOWN, Constraint_UNDEF, Constraint_NOP}; case c of when Constraint_UNKNOWN rt_unknown = TRUE; // Result is UNKNOWN when Constraint_UNDEF EndOfDecode(Decode_UNDEF); when Constraint_NOP EndOfDecode(Decode_NOP);
```

For information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors, and particularly LDNP.

## Assembler Symbols

&lt;Wt1&gt;

Is the 32-bit name of the first general-purpose register to be transferred, encoded in the 'Rt' field.

&lt;Wt2&gt;

Is the 32-bit name of the second general-purpose register to be transferred, encoded in the 'Rt2' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;imm&gt;

For the '32-bit' variant: is the optional signed immediate byte offset, a multiple of 4 in the range -256 to 252, defaulting to 0 and encoded in the 'imm7' field as &lt;imm&gt;/4.

For the '64-bit' variant: is the optional signed immediate byte offset, a multiple of 8 in the range -512 to 504, defaulting to 0 and encoded in the 'imm7' field as &lt;imm&gt;/8.

## &lt;Xt1&gt;

Is the 64-bit name of the first general-purpose register to be transferred, encoded in the 'Rt' field.

&lt;Xt2&gt;

Is the 64-bit name of the second general-purpose register to be transferred, encoded in the 'Rt2' field.

## Operation

```
bits(64) address; constant integer dbytes = datasize DIV 8; constant boolean privileged = PSTATE.EL != EL0; constant boolean ispair = TRUE; constant AccessDescriptor accdesc = CreateAccDescGPR(MemOp_LOAD, nontemporal, privileged, tagchecked, ispair, t, t2); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; address = AddressAdd(address, offset, accdesc); constant bits(2*datasize) data = Mem[address, 2 * dbytes, accdesc]; if rt_unknown then X[t, datasize] = bits(datasize) UNKNOWN; elsif BigEndian(accdesc.acctype) then X[t2, datasize] = data<(datasize-1):0>; X[t, datasize] = data<(2*datasize-1):datasize>; else X[t, datasize] = data<(datasize-1):0>; X[t2, datasize] = data<(2*datasize-1):datasize>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
