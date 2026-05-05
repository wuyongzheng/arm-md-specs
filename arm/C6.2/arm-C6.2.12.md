## C6.2.12 ADR

Form PC-relative address

This instruction adds an immediate value to the PC value to form a PC-relative address, and writes the result to the destination register.

<!-- image -->

## Encoding

```
ADR <Xd>, <label>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant bits(64) imm = SignExtend(immhi:immlo, 64);
```

## Assembler Symbols

## &lt;Xd&gt;

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;label&gt;

Is the program label whose address is to be calculated. Its offset from the address of this instruction, in the range +/-1MB, is encoded in 'immhi:immlo'.

## Operation

```
X[d, 64] = PC64 + imm;
```
