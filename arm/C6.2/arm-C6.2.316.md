## C6.2.316 PRFM (register)

Prefetch memory (register)

This instruction signals the memory system that data memory accesses from a specified address are likely to occur in the near future. The address for data memory accesses is calculated from a base register value and an offset register value. The offset register value can optionally be shifted and extended. The memory system can respond by taking actions that are expected to speed up the memory accesses when they do occur, such as making the cache line containing the specified address available at the level of cache specified by the instruction.

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
PRFM (<prfop>|#<imm5>), [<Xn|SP>, (<Wm>|<Xm>){, <extend> {<amount>}}]
```

## Decode for this encoding

```
if option<1> == '0' then EndOfDecode(Decode_UNDEF); // sub-word index constant ExtendType extend_type = DecodeRegExtend(option); constant integer shift = if S == '1' then 3 else 0; constant integer n = UInt(Rn); constant integer t = UInt(Rt); constant integer m = UInt(Rm); constant boolean nontemporal = FALSE; constant boolean tagchecked = FALSE;
```

## Assembler Symbols

## &lt;prfop&gt;

Is the prefetch operation, encoded in 'Rt':

|    Rt | <prfop>    | Architectural Feature   |
|-------|------------|-------------------------|
| 00000 | PLDL1KEEP  | -                       |
| 00001 | PLDL1STRM  | -                       |
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

For other encodings of the 'Rt' field, use &lt;imm5&gt;.

## &lt;imm5&gt;

Is the prefetch operation encoding as an immediate, in the range 0 to 31, encoded in the 'Rt' field.

This syntax is only for encodings that are not accessible using &lt;prfop&gt; .

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;Wm&gt;

When option&lt;0&gt; is set to 0, is the 32-bit name of the general-purpose index register, encoded in the 'Rm' field.

## &lt;Xm&gt;

When option&lt;0&gt; is set to 1, is the 64-bit name of the general-purpose index register, encoded in the 'Rm' field.

## &lt;extend&gt;

Is the index extend/shift specifier, defaulting to LSL, and which must be omitted for the LSL option when &lt;amount&gt; is omitted, encoded in 'option':

## &lt;amount&gt;

Is the index shift amount, optional only when &lt;extend&gt; is not LSL. Where it is permitted to be optional, it defaults to #0. It is encoded in 'S':

|   S | <amount>   |
|-----|------------|
|   0 | #0         |
|   1 | #3         |

## Operation

```
bits(64) address; constant bits(64) offset = ExtendReg(m, extend_type, shift, 64); constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescGPR(MemOp_PREFETCH, nontemporal, privileged, tagchecked, t); if n == 31 then address = SP[64]; else address = X[n, 64]; address = AddressAdd(address, offset, accdesc); Prefetch(address, t<4:0>);
```

|   option | <extend>   |
|----------|------------|
|      010 | UXTW       |
|      011 | LSL        |
|      110 | SXTW       |
|      111 | SXTX       |
