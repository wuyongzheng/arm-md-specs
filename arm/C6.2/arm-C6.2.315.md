## C6.2.315 PRFM (literal)

## Prefetch memory (literal)

This instruction signals the memory system that data memory accesses from a specified address are likely to occur in the near future. The address for data memory accesses is calculated from the PC value and an immediate offset. The memory system can respond by taking actions that are expected to speed up the memory accesses when they do occur, such as making the cache line containing the specified address available at the level of cache specified by the instruction.

The &lt;prfop&gt; operand specifies the prefetch hint as follows:

- Access type:
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
PRFM (<prfop>|#<imm5>), <label>
```

## Decode for this encoding

```
constant integer t = UInt(Rt); constant bits(64) offset = SignExtend(imm19:'00', 64);
```

## Assembler Symbols

## &lt;prfop&gt;

Is the prefetch operation, encoded in 'Rt':

|    Rt | <prfop>   | Architectural Feature   |
|-------|-----------|-------------------------|
| 00000 | PLDL1KEEP | -                       |
| 00001 | PLDL1STRM | -                       |
| 00010 | PLDL2KEEP | -                       |
| 00011 | PLDL2STRM | -                       |

|    Rt | <prfop>    | Architectural Feature   |
|-------|------------|-------------------------|
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

For other encodings of the 'Rt' field, use &lt;imm5&gt;.

## &lt;imm5&gt;

Is the prefetch operation encoding as an immediate, in the range 0 to 31, encoded in the 'Rt' field.

This syntax is only for encodings that are not accessible using &lt;prfop&gt; .

## &lt;label&gt;

Is the program label from which the data is to be loaded. Its offset from the address of this instruction, in the range +/-1MB, is encoded as 'imm19' times 4.

## Operation

```
constant bits(64) address = PC64 Prefetch(address, t<4:0>);
```

```
+ offset;
```
