## C6.2.13 ADRP

Form PC-relative address to 4KB page

This instruction adds an immediate value that is shifted left by 12 bits, to the PC value to form a PC-relative address, with the bottom 12 bits masked out, and writes the result to the destination register.

<!-- image -->

## Encoding

```
ADRP <Xd>, <label>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant bits(64) imm =
```

```
SignExtend(immhi:immlo:Zeros(12), 64);
```

## Assembler Symbols

&lt;Xd&gt;

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;label&gt;

Is the program label whose 4KB page address is to be calculated. Its offset from the page address of this instruction, in the range +/-4GB, is encoded as 'immhi:immlo' times 4096.

## Operation

```
constant bits(64) base X[d, 64] = base + imm;
```

```
= PC64<63:12>:Zeros(12);
```
