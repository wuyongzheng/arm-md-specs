## C6.2.216 LDR (literal)

## Load register (literal)

This instruction calculates an address from the PC value and an immediate offset, loads a word from memory, and writes it to a register. For information about addressing modes, see Load/Store addressing modes.

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (opc ==
```

```
00)
```

```
LDR <Wt>, <label>
```

## Encoding for the 64-bit variant

Applies when (opc ==

```
LDR
```

```
01) <Xt>, <label>
```

## Decode for all variants of this encoding

```
constant integer t = UInt(Rt); constant integer size = 4 << UInt(opc<0>); constant boolean nontemporal = FALSE; constant boolean tagchecked = FALSE; constant bits(64) offset
```

## Assembler Symbols

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be loaded, encoded in the 'Rt' field.

## &lt;label&gt;

Is the program label from which the data is to be loaded. Its offset from the address of this instruction, in the range +/-1MB, is encoded as 'imm19' times 4.

<!-- image -->

```
= SignExtend(imm19:'00', 64);
```

Is the 64-bit name of the general-purpose register to be loaded, encoded in the 'Rt' field.

## Operation

```
constant bits(64) address = PC64 + offset; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescGPR(MemOp_LOAD, nontemporal, privileged, tagchecked, t); X[t, size * 8] = Mem[address, size, accdesc];
```
