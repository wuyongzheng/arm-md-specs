## F6.1.239 VST2 (multiple 2-element structures)

Store multiple 2-element structures from two or four registers stores multiple 2-element structures from two or four registers to memory, with interleaving. For more information, see Element and structure load/store instructions. Every element of each register is saved. For details of the addressing mode, see Advanced SIMD addressing mode.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information, see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1 and A2) and T32 (T1 and T2).

## A1

<!-- image -->

## Encoding for the Offset variant

Applies when (Rm ==

```
1111)
```

```
VST2{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VST2{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}]!
```

## Encoding for the Post-indexed variant

```
Applies when (Rm != 11x1) VST2{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}],
```

```
<Rm>
```

## Decode for all variants of this encoding

```
if align == '11' then UNDEFINED; if size == '11' then UNDEFINED; constant integer pairs = 1; constant integer inc = if itype == '1001' then 2 else 1; constant integer alignment = if align == '00' then 1 else 4 << constant integer ebytes = 1 << UInt(size); constant integer elements = 8 DIV ebytes; constant integer d = UInt(D:Vd); constant integer d2 = d + inc; constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 || d2+pairs > 32 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If d2+pairs &gt; 32 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The memory locations specified by the instruction and the number of registers specified by the instruction become UNKNOWN. If the instruction specifies writeback, then that register becomes UNKNOWN. This behavior does not affect any other memory locations.

```
UInt(align);
```

## A2

<!-- image -->

## Encoding for the Offset variant

```
Applies when (Rm == 1111) VST2{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VST2{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]!
```

## Encoding for the Post-indexed variant

Applies when

```
(Rm != 11x1) VST2{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}],
```

## Decode for all variants of this encoding

```
if size == '11' then UNDEFINED; constant integer pairs = 2; constant integer inc = 2; constant integer alignment = if align == '00' then 1 else 4 << constant integer ebytes = 1 << UInt(size); constant integer elements = 8 DIV ebytes; constant integer d = UInt(D:Vd); constant integer d2 = d + inc; constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 || d2+pairs > 32 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If d2+pairs &gt; 32 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The memory locations specified by the instruction and the number of registers specified by the instruction become UNKNOWN. If the instruction specifies writeback, then that register becomes UNKNOWN. This behavior does not affect any other memory locations.

```
<Rm>
```

```
UInt(align);
```

T1

<!-- image -->

## Encoding for the Offset variant

```
Applies when (Rm == 1111) VST2{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VST2{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]!
```

## Encoding for the Post-indexed variant

Applies when

```
(Rm != 11x1) VST2{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}],
```

## Decode for all variants of this encoding

```
if align == '11' then UNDEFINED; if size == '11' then UNDEFINED; constant integer pairs = 1; constant integer inc = if itype == '1001' then 2 else 1; constant integer alignment = if align == '00' then 1 else 4 << UInt(align); constant integer ebytes = 1 << UInt(size); constant integer elements = 8 DIV ebytes; constant integer d = UInt(D:Vd); constant integer d2 = d + inc; constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 || d2+pairs > 32 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If d2+pairs &gt; 32 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The memory locations specified by the instruction and the number of registers specified by the instruction become UNKNOWN. If the instruction specifies writeback, then that register becomes UNKNOWN. This behavior does not affect any other memory locations.

```
<Rm>
```

T2

<!-- image -->

## Encoding for the Offset variant

```
Applies when (Rm == 1111) VST2{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VST2{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]!
```

## Encoding for the Post-indexed variant

Applies when

```
(Rm != 11x1) VST2{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}],
```

## Decode for all variants of this encoding

```
if size == '11' then UNDEFINED; constant integer pairs = 2; constant integer inc = 2; constant integer alignment = if align == '00' then 1 else 4 << UInt(align); constant integer ebytes = 1 << UInt(size); constant integer elements = 8 DIV ebytes; constant integer d = UInt(D:Vd); constant integer d2 = d + inc; constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 || d2+pairs > 32 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If d2+pairs &gt; 32 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The memory locations specified by the instruction and the number of registers specified by the instruction become UNKNOWN. If the instruction specifies writeback, then that register becomes UNKNOWN. This behavior does not affect any other memory locations.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors, and particularly VST2 (multiple 2-element structures).

Related encodings: See Advanced SIMD element or structure load/store for the T32 instruction set, or Advanced SIMD element or structure load/store for the A32 instruction set.

```
<Rm>
```

## Assembler Symbols

## &lt;c&gt;

For the 'A1 Offset', 'A1 Post-indexed', 'A2 Offset', and 'A2 Post-indexed' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 Offset', 'T1 Post-indexed', 'T2 Offset', and 'T2 Post-indexed' variants: see Standard assembler syntax fields.

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

64 64-bit alignment, encoded in the 'align' field as 0b01 . 128 128-bit alignment, encoded in the 'align' field as 0b10 . 256 256-bit alignment, encoded in the 'align' field as 0b11 . Available only if &lt;list&gt; contains four registers.

: is the preferred separator before the &lt;align&gt; value, but the alignment can be specified as @&lt;align&gt; , see Advanced SIMD addressing mode.

## &lt;Rm&gt;

Is the general-purpose index register containing an offset applied after the access, encoded in the 'Rm' field.

For more information about the variants of this instruction, see Advanced SIMD addressing mode.

## &lt;q&gt;

|   size |   <size> |
|--------|----------|
|     00 |        8 |
|     01 |       16 |
|     10 |       32 |

Is a list containing the 64-bit names of the SIMD&amp;FP registers.

The list must be one of:

```
{ <Dd>, <Dd+1> } Two single-spaced registers. Selects the A1 and T1 encodings of the instruction, and encoded in the 'itype' field as 0b1000 . { <Dd>, <Dd+2> } Two double-spaced registers. Selects the A1 and T1 encodings of the instruction, and encoded in the 'itype' field as 0b1001 . { <Dd>, <Dd+1>, <Dd+2>, <Dd+3> } Three single-spaced registers. Selects the A2 and T2 encodings of the instruction.
```

The register &lt;Dd&gt; is encoded in the 'D:Vd' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); bits(32) address = R[n]; constant boolean nontemporal = FALSE; constant boolean privileged = PSTATE.EL != EL0; constant boolean tagchecked = FALSE; constant AccessDescriptor accdesc = CreateAccDescASIMD(MemOp_STORE, nontemporal, tagchecked, privileged); if !IsAligned(address, alignment) then constant FaultRecord fault = AlignmentFault(accdesc, ZeroExtend(address, 64)); AArch32.Abort(fault); for r = 0 to pairs-1 for e = 0 to elements-1 MemU[address, ebytes] = Elem[D[d+r], e,8*ebytes]; MemU[address+ebytes,ebytes] = Elem[D[d2+r],e,8*ebytes]; address = address + 2*ebytes; if wback then if register_index then R[n] = R[n] + R[m]; else R[n] = R[n] + 16*pairs;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.