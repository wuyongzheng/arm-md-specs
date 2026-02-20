## F6.1.106 VLD3 (single 3-element structure to one lane)

Load single 3-element structure to one lane of three registers loads one 3-element structure from memory into corresponding elements of three registers. Elements of the registers that are not loaded are unchanged. For details of the addressing mode, see Advanced SIMD addressing mode.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information, see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1, A2, and A3) and T32 (T1, T2, and T3).

## A1

<!-- image -->

## Encoding for the Offset variant

```
Applies when (Rm == 1111) VLD3{<c>}{<q>}.<size> <list>, [<Rn>]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VLD3{<c>}{<q>}.<size> <list>, [<Rn>]!
```

## Encoding for the Post-indexed variant

```
Applies when (Rm != 11x1) VLD3{<c>}{<q>}.<size> <list>, [<Rn>], <Rm>
```

## Decode for all variants of this encoding

```
if size == '11' then SEE "VLD3 (single 3-element structure to if index_align<0> != '0' then UNDEFINED; constant integer ebytes = 1; constant integer index = UInt(index_align<3:1>); constant integer inc = 1; constant integer d = UInt(D:Vd); constant integer d2 = d + inc; constant integer d3 = d2 + inc; constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 || d3 > 31 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If d3 &gt; 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- One or more of the SIMD and floating-point registers are UNKNOWN. If the instruction specifies writeback, the base register becomes UNKNOWN. This behavior does not affect any general-purpose registers.

```
all lanes)";
```

## A2

<!-- image -->

## Encoding for the Offset variant

```
Applies when (Rm == 1111) VLD3{<c>}{<q>}.<size>
```

```
<list>, [<Rn>]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VLD3{<c>}{<q>}.<size>
```

```
<list>, [<Rn>]!
```

## Encoding for the Post-indexed variant

Applies when

```
(Rm != 11x1) VLD3{<c>}{<q>}.<size> <list>, [<Rn>], <Rm>
```

## Decode for all variants of this encoding

```
if size == '11' then SEE "VLD3 (single 3-element structure to if index_align<0> != '0' then UNDEFINED; constant integer ebytes = 2; constant integer index = UInt(index_align<3:2>); constant integer inc = if index_align<1> == '0' then 1 else 2; constant integer d = UInt(D:Vd); constant integer d2 = d + inc; constant integer d3 = d2 + inc; constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 || d3 > 31 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If d3 &gt; 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- One or more of the SIMD and floating-point registers are UNKNOWN. If the instruction specifies writeback, the base register becomes UNKNOWN. This behavior does not affect any general-purpose registers.

```
all lanes)";
```

A3

<!-- image -->

## Encoding for the Offset variant

```
Applies when (Rm == 1111) VLD3{<c>}{<q>}.<size>
```

```
<list>, [<Rn>]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VLD3{<c>}{<q>}.<size>
```

```
<list>, [<Rn>]!
```

## Encoding for the Post-indexed variant

Applies when

```
(Rm != 11x1) VLD3{<c>}{<q>}.<size> <list>, [<Rn>], <Rm>
```

## Decode for all variants of this encoding

```
if size == '11' then SEE "VLD3 (single 3-element structure to if index_align<1:0> != '00' then UNDEFINED; constant integer ebytes = 4; constant integer index = UInt(index_align<3>); constant integer inc = if index_align<2> == '0' then 1 else 2; constant integer d = UInt(D:Vd); constant integer d2 = d + inc; constant integer d3 = d2 + inc; constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 || d3 > 31 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If d3 &gt; 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- One or more of the SIMD and floating-point registers are UNKNOWN. If the instruction specifies writeback, the base register becomes UNKNOWN. This behavior does not affect any general-purpose registers.

```
all lanes)";
```

T1

<!-- image -->

## Encoding for the Offset variant

```
Applies when (Rm == 1111) VLD3{<c>}{<q>}.<size>
```

```
<list>, [<Rn>]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VLD3{<c>}{<q>}.<size>
```

```
<list>, [<Rn>]!
```

## Encoding for the Post-indexed variant

Applies when

```
(Rm != 11x1) VLD3{<c>}{<q>}.<size> <list>, [<Rn>], <Rm>
```

## Decode for all variants of this encoding

```
if size == '11' then SEE "VLD3 (single 3-element structure to if index_align<0> != '0' then UNDEFINED; constant integer ebytes = 1; constant integer index = UInt(index_align<3:1>); constant integer inc = 1; constant integer d = UInt(D:Vd); constant integer d2 = d + inc; constant integer d3 = d2 + inc; constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 || d3 > 31 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If d3 &gt; 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- One or more of the SIMD and floating-point registers are UNKNOWN. If the instruction specifies writeback, the base register becomes UNKNOWN. This behavior does not affect any general-purpose registers.

```
all lanes)";
```

T2

<!-- image -->

## Encoding for the Offset variant

```
Applies when (Rm == 1111) VLD3{<c>}{<q>}.<size>
```

```
<list>, [<Rn>]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VLD3{<c>}{<q>}.<size>
```

```
<list>, [<Rn>]!
```

## Encoding for the Post-indexed variant

Applies when

```
(Rm != 11x1) VLD3{<c>}{<q>}.<size> <list>, [<Rn>], <Rm>
```

## Decode for all variants of this encoding

```
if size == '11' then SEE "VLD3 (single 3-element structure to if index_align<0> != '0' then UNDEFINED; constant integer ebytes = 2; constant integer index = UInt(index_align<3:2>); constant integer inc = if index_align<1> == '0' then 1 else 2; constant integer d = UInt(D:Vd); constant integer d2 = d + inc; constant integer d3 = d2 + inc; constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 || d3 > 31 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If d3 &gt; 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- One or more of the SIMD and floating-point registers are UNKNOWN. If the instruction specifies writeback, the base register becomes UNKNOWN. This behavior does not affect any general-purpose registers.

```
all lanes)";
```

T3

<!-- image -->

## Encoding for the Offset variant

```
Applies when (Rm == 1111) VLD3{<c>}{<q>}.<size>
```

```
<list>, [<Rn>]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VLD3{<c>}{<q>}.<size>
```

```
<list>, [<Rn>]!
```

## Encoding for the Post-indexed variant

Applies when

```
(Rm != 11x1) VLD3{<c>}{<q>}.<size> <list>, [<Rn>], <Rm>
```

## Decode for all variants of this encoding

```
if size == '11' then SEE "VLD3 (single 3-element structure to if index_align<1:0> != '00' then UNDEFINED; constant integer ebytes = 4; constant integer index = UInt(index_align<3>); constant integer inc = if index_align<2> == '0' then 1 else 2; constant integer d = UInt(D:Vd); constant integer d2 = d + inc; constant integer d3 = d2 + inc; constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 || d3 > 31 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If d3 &gt; 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- One or more of the SIMD and floating-point registers are UNKNOWN. If the instruction specifies writeback, the base register becomes UNKNOWN. This behavior does not affect any general-purpose registers.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors, and particularly VLD3 (single 3-element structure to one lane).

```
all lanes)";
```

## Assembler Symbols

&lt;c&gt;

For the 'A1 Offset', 'A1 Post-indexed', 'A2 Offset', 'A2 Post-indexed', 'A3 Offset', and 'A3 Post-indexed' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 Offset', 'T1 Post-indexed', 'T2 Offset', 'T2 Post-indexed', 'T3 Offset', and 'T3 Post-indexed' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

## &lt;size&gt;

Is the data size, encoded in 'size':

## &lt;list&gt;

## &lt;Rn&gt;

&lt;q&gt;

|   size |   <size> |
|--------|----------|
|     00 |        8 |
|     01 |       16 |
|     10 |       32 |

Is a list containing the 64-bit names of the three SIMD&amp;FP registers holding the element.

The list must be one of:

```
{ <Dd>[<index>], <Dd+1>[<index>], <Dd+2>[<index>] } Single-spaced registers, encoded as 'spacing' = 0. { <Dd>[<index>], <Dd+2>[<index>], <Dd+4>[<index>] } Double-spaced registers, encoded as 'spacing' = 1. Not permitted when <size> == 8. The encoding of 'spacing' depends on <size> : <size> == 8 'spacing' is encoded in the 'index_align<0>' field. <size> == 16 'spacing' is encoded in the 'index_align<1>' field, and 'index_align<0>' is set to 0. <size> == 32 'spacing' is encoded in the 'index_align<2>' field, and 'index_align<1:0>' is set to 0b00 . The register <Dd> is encoded in the 'D:Vd' field. The permitted values and encoding of <index> depend on <size> : <size> == 8 <index> is in the range 0 to 7, encoded in the 'index_align<3:1>' field. <size> == 16 <index> is in the range 0 to 3, encoded in the 'index_align<3:2>' field. <size> == 32 <index> is 0 or 1, encoded in the 'index_align<3>' field.
```

Is the general-purpose base register, encoded in the 'Rn' field.

## &lt;Rm&gt;

Is the general-purpose index register containing an offset applied after the access, encoded in the 'Rm' field.

For more information about the variants of this instruction, see Advanced SIMD addressing mode.

Alignment

Standard alignment rules apply, see Alignment support.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); constant bits(32) address = R[n]; Elem[D[d], index,8*ebytes] = MemU[address,ebytes]; Elem[D[d2],index,8*ebytes] = MemU[address+ebytes,ebytes]; Elem[D[d3],index,8*ebytes] = MemU[address+2*ebytes,ebytes]; if wback then if register_index then R[n] = R[n] + R[m]; else R[n] = R[n] + 3*ebytes;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.