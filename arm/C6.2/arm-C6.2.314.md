## C6.2.314 PRFM (immediate)

Prefetch memory (immediate)

This instruction signals the memory system that data memory accesses from a specified address are likely to occur in the near future. The address for data memory accesses is calculated from a base register value and an immediate offset. The memory system can respond by taking actions that are expected to speed up the memory accesses when they do occur, such as making the cache line containing the specified address available at the level of cache specified by the instruction.

The &lt;prfop&gt; operand specifies the prefetch hint as follows:

- Access type:
- When FEAT\_PCDPHINT is implemented, IR for intent to read on update.
- PLD for prefetch for load.
- PLI for prefetch for execute.
- PST for prefetch for store.
- Target cache level:
- L1 for Level 1 cache.
- L2 for Level 2 cache.
- L3 for Level 3 cache.
- When FEAT\_PRFMSLC is implemented, SLC for system level cache.
- Policy:
- KEEP for retained or temporal prefetch, allocated in the cache normally.
- STRMfor streaming or non-temporal prefetch, for data that is used only once.

The effect of a PRFM instruction is IMPLEMENTATION DEFINED. For more information, see Prefetch memory.

For information about addressing modes, see Load/Store addressing modes.

<!-- image -->

## Encoding

```
PRFM
```

```
(<prfop>|#<imm5>), [<Xn|SP>{, #<pimm>}]
```

## Decode for this encoding

```
= LSL(ZeroExtend(imm12, 64), 3);
```

```
constant bits(64) offset constant integer n = UInt(Rn); constant integer t = UInt(Rt); constant boolean nontemporal = FALSE; constant boolean tagchecked = FALSE;
```

## Assembler Symbols

## &lt;prfop&gt;

Is the prefetch operation, encoded in 'Rt':

|    Rt | <prfop>   | Architectural Feature   |
|-------|-----------|-------------------------|
| 00000 | PLDL1KEEP | -                       |
| 00001 | PLDL1STRM | -                       |

|    Rt | <prfop>    | Architectural Feature   |
|-------|------------|-------------------------|
| 00010 | PLDL2KEEP  | -                       |
| 00011 | PLDL2STRM  | -                       |
| 00100 | PLDL3KEEP  | -                       |
| 00101 | PLDL3STRM  | -                       |
| 00110 | PLDSLCKEEP | FEAT_PRFMSLC            |
| 00111 | PLDSLCSTRM | FEAT_PRFMSLC            |
| 01000 | PLIL1KEEP  | -                       |
| 01001 | PLIL1STRM  | -                       |
| 01010 | PLIL2KEEP  | -                       |
| 01011 | PLIL2STRM  | -                       |
| 01100 | PLIL3KEEP  | -                       |
| 01101 | PLIL3STRM  | -                       |
| 01110 | PLISLCKEEP | FEAT_PRFMSLC            |
| 01111 | PLISLCSTRM | FEAT_PRFMSLC            |
| 10000 | PSTL1KEEP  | -                       |
| 10001 | PSTL1STRM  | -                       |
| 10010 | PSTL2KEEP  | -                       |
| 10011 | PSTL2STRM  | -                       |
| 10100 | PSTL3KEEP  | -                       |
| 10101 | PSTL3STRM  | -                       |
| 10110 | PSTSLCKEEP | FEAT_PRFMSLC            |
| 10111 | PSTSLCSTRM | FEAT_PRFMSLC            |
| 11000 | IR         | FEAT_PCDPHINT           |

For other encodings of the 'Rt' field, use &lt;imm5&gt;.

## &lt;imm5&gt;

Is the prefetch operation encoding as an immediate, in the range 0 to 31, encoded in the 'Rt' field.

This syntax is only for encodings that are not accessible using &lt;prfop&gt; .

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;pimm&gt;

Is the optional positive immediate byte offset, a multiple of 8 in the range 0 to 32760, defaulting to 0 and encoded in the 'imm12' field as &lt;pimm&gt;/8.

## Operation

```
bits(64) address; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescGPR(MemOp_PREFETCH, nontemporal, privileged, tagchecked, t); if n == 31 then
```

```
address = SP[64]; else address = X[n, 64]; address = AddressAdd(address, offset, accdesc); Prefetch(address, t<4:0>);
```
