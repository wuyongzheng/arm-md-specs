## F6.1.111 VLD4 (multiple 4-element structures)

Load multiple 4-element structures to four registers loads multiple 4-element structures from memory into four registers, with de-interleaving. For more information, see Element and structure load/store instructions. Every element of each register is loaded. For details of the addressing mode, see Advanced SIMD addressing mode.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information, see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the Offset variant

```
Applies when (Rm == 1111) VLD4{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VLD4{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]!
```

## Encoding for the Post-indexed variant

```
Applies when (Rm != 11x1) VLD4{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}], <Rm>
```

## Decode for all variants of this encoding

```
if itype != '000x' then SEE "Related encodings"; if size == '11' then UNDEFINED; constant integer inc = if itype<0> == '0' then 1 else 2; constant integer alignment = if align == '00' then 1 else 4 << UInt(align); constant integer ebytes = 1 << UInt(size); constant integer elements = 8 DIV ebytes; constant integer d = UInt(D:Vd); constant integer d2 = d + inc; constant integer d3 = d2 + inc; constant integer d4 = d3 + inc; constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 || d4 > 31 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If d4 &gt; 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- One or more of the SIMD and floating-point registers are UNKNOWN. If the instruction specifies writeback, the base register becomes UNKNOWN. This behavior does not affect any general-purpose registers.

T1

<!-- image -->

## Encoding for the Offset variant

```
Applies when (Rm == 1111) VLD4{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VLD4{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]!
```

## Encoding for the Post-indexed variant

Applies when

```
(Rm != 11x1) VLD4{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}],
```

## Decode for all variants of this encoding

```
if itype != '000x' then SEE "Related encodings"; if size == '11' then UNDEFINED; constant integer inc = if itype<0> == '0' then 1 else 2; constant integer alignment = if align == '00' then 1 else 4 << constant integer ebytes = 1 << UInt(size); constant integer elements = 8 DIV ebytes; constant integer d = UInt(D:Vd); constant integer d2 = d + inc; constant integer d3 = d2 + inc; constant integer d4 = d3 + inc; constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 || d4 > 31 then UNPREDICTABLE;
```

```
<Rm>
```

```
UInt(align);
```

## CONSTRAINED UNPREDICTABLE behavior

If d4 &gt; 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- One or more of the SIMD and floating-point registers are UNKNOWN. If the instruction specifies writeback, the base register becomes UNKNOWN. This behavior does not affect any general-purpose registers.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors, and particularly VLD4 (multiple 4-element structures).

Related encodings: See Advanced SIMD element or structure load/store for the T32 instruction set, or Advanced SIMD element or structure load/store for the A32 instruction set.

## Assembler Symbols

&lt;c&gt;

For the 'A1 Offset' and 'A1 Post-indexed' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 Offset' and 'T1 Post-indexed' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

## &lt;size&gt;

Is the data size, encoded in 'size':

## &lt;list&gt;

## &lt;Rn&gt;

Is the general-purpose base register, encoded in the 'Rn' field.

## &lt;align&gt;

Is the optional alignment.

Whenever &lt;align&gt; is omitted, the standard alignment is used, see Unaligned data access, and is encoded in the 'align' field as 0b00 .

Whenever &lt;align&gt; is present, the permitted values are:

&lt;q&gt;

|   size |   <size> |
|--------|----------|
|     00 |        8 |
|     01 |       16 |
|     10 |       32 |

Is a list containing the 64-bit names of the SIMD&amp;FP registers.

The list must be one of:

```
{ <Dd>, <Dd+1>, <Dd+2>, <Dd+3> } Single-spaced registers, encoded in the 'itype' field as 0b0000 . { <Dd>, <Dd+2>, <Dd+4>, <Dd+6> } Double-spaced registers, encoded in the 'itype' field as 0b0001 .
```

The register &lt;Dd&gt; is encoded in the 'D:Vd' field.

```
64 64-bit alignment, encoded in the 'align' field as 0b01 . 128 128-bit alignment, encoded in the 'align' field as 0b10 . 256 256-bit alignment, encoded in the 'align' field as 0b11 .
```

: is the preferred separator before the &lt;align&gt; value, but the alignment can be specified as @&lt;align&gt; , see Advanced SIMD addressing mode.

## &lt;Rm&gt;

Is the general-purpose index register containing an offset applied after the access, encoded in the 'Rm' field.

For more information about the variants of this instruction, see Advanced SIMD addressing mode.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); bits(32) address = R[n]; constant boolean nontemporal = FALSE; constant boolean privileged = PSTATE.EL != EL0; constant boolean tagchecked = FALSE; constant AccessDescriptor accdesc = CreateAccDescASIMD(MemOp_LOAD, nontemporal, tagchecked, privileged); if !IsAligned(address, alignment) then constant FaultRecord fault = AlignmentFault(accdesc, ZeroExtend(address, 64)); AArch32.Abort(fault); for e = 0 to elements-1 Elem[D[d], e,8*ebytes] = MemU[address,ebytes]; Elem[D[d2],e,8*ebytes] = MemU[address+ebytes,ebytes]; Elem[D[d3],e,8*ebytes] = MemU[address+2*ebytes,ebytes]; Elem[D[d4],e,8*ebytes] = MemU[address+3*ebytes,ebytes]; address = address + 4*ebytes; if wback then if register_index then R[n] = R[n] + R[m]; else R[n] = R[n] + 32;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.