## F6.1.107 VLD3 (single 3-element structure to all lanes)

Load single 3-element structure and replicate to all lanes of three registers

Load single 3-element structure and replicate to all lanes of three registers loads one 3-element structure from memory into all lanes of three registers. For details of the addressing mode, see Advanced SIMD addressing mode.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information, see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

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
Applies when (Rm == 1101) VLD3{<c>}{<q>}.<size> <list>, [<Rn>]!
```

## Encoding for the Post-indexed variant

```
Applies when (Rm != 11x1) VLD3{<c>}{<q>}.<size> <list>, [<Rn>],
```

```
<Rm>
```

## Decode for all variants of this encoding

```
m != 13);
```

```
if size == '11' || a == '1' then UNDEFINED; constant integer ebytes = 1 << UInt(size); constant integer inc = if T == '0' then 1 else 2; constant integer d = UInt(D:Vd); constant integer d2 = d + inc; constant integer d3 = d2 + inc; constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && if n == 15 || d3 > 31 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If d3 &gt; 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- One or more of the SIMD and floating-point registers are UNKNOWN. If the instruction specifies writeback, the base register becomes UNKNOWN. This behavior does not affect any general-purpose registers.

T1

<!-- image -->

## Encoding for the Offset variant

Applies when (Rm ==

```
1111) VLD3{<c>}{<q>}.<size> <list>, [<Rn>]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VLD3{<c>}{<q>}.<size>
```

```
<list>, [<Rn>]!
```

## Encoding for the Post-indexed variant

Applies when (Rm !=

```
11x1) VLD3{<c>}{<q>}.<size> <list>, [<Rn>],
```

```
<Rm>
```

## Decode for all variants of this encoding

```
m != 13);
```

```
if size == '11' || a == '1' then UNDEFINED; constant integer ebytes = 1 << UInt(size); constant integer inc = if T == '0' then 1 else 2; constant integer d = UInt(D:Vd); constant integer d2 = d + inc; constant integer d3 = d2 + inc; constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && if n == 15 || d3 > 31 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If d3 &gt; 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- One or more of the SIMD and floating-point registers are UNKNOWN. If the instruction specifies writeback, the base register becomes UNKNOWN. This behavior does not affect any general-purpose registers.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors, and particularly VLD3 (single 3-element structure to all lanes).

## Assembler Symbols

For the 'A1 Offset' and 'A1 Post-indexed' variants: see Standard assembler syntax fields. This encoding must be

```
<c> unconditional. For the 'T1 Offset' and 'T1 Post-indexed' variants: see Standard assembler syntax fields. <q> See Standard assembler syntax fields. <size> Is the data size, encoded in 'size':
```

|   size |   <size> |
|--------|----------|
|     00 |        8 |
|     01 |       16 |
|     10 |       32 |

Is a list containing the 64-bit names of three SIMD&amp;FP registers.

The list must be one of:

```
{ <Dd>[], <Dd+1>[], <Dd+2>[] } Single-spaced registers, encoded in the 'T' field as 0. { <Dd>[], <Dd+2>[], <Dd+4>[] } Double-spaced registers, encoded in the 'T' field as 1.
```

The register &lt;Dd&gt; is encoded in the 'D:Vd' field.

## &lt;list&gt;

## &lt;Rn&gt;

Is the general-purpose base register, encoded in the 'Rn' field.

## &lt;Rm&gt;

Is the general-purpose index register containing an offset applied after the access, encoded in the 'Rm' field.

For more information about the variants of this instruction, see Advanced SIMD addressing mode.

Alignment

Standard alignment rules apply, see Alignment support.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); constant bits(32) address = R[n]; constant integer esize = ebytes * 8; constant bits(esize) element1 = MemU[address, ebytes]; constant bits(esize) element2 = MemU[address+ebytes,ebytes]; constant bits(esize) element3 = MemU[address+2*ebytes,ebytes]; D[d] = Replicate(element1, 64 DIV esize); D[d2] = Replicate(element2, 64 DIV esize); D[d3] = Replicate(element3, 64 DIV esize); if wback then if register_index then
```

```
R[n] = R[n] + R[m]; else R[n] = R[n] + 3*ebytes;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.