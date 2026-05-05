## C6.2.228 LDRSW (literal)

Load register signed word (literal)

This instruction calculates an address from the PC value and an immediate offset, loads a word from memory, and writes it to a register. For information about addressing modes, see Load/Store addressing modes.

<!-- image -->

## Encoding

```
LDRSW <Xt>, <label>
```

## Decode for this encoding

```
constant integer t = UInt(Rt); constant boolean nontemporal = FALSE; constant boolean tagchecked = FALSE; constant bits(64) offset
```

```
= SignExtend(imm19:'00', 64);
```

## Assembler Symbols

## &lt;Xt&gt;

Is the 64-bit name of the general-purpose register to be loaded, encoded in the 'Rt' field.

## &lt;label&gt;

Is the program label from which the data is to be loaded. Its offset from the address of this instruction, in the range +/-1MB, is encoded as 'imm19' times 4.

## Operation

```
constant bits(64) address = PC64 + offset; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescGPR(MemOp_LOAD, nontemporal, privileged, tagchecked, t); constant bits(32) data = Mem[address, 4, accdesc]; X[t, 64] = SignExtend(data, 64);
```
