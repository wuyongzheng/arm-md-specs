## F6.1.237 VST1 (multiple single elements)

Store multiple single elements from one, two, three, or four registers

Store multiple single elements from one, two, three, or four registers stores elements to memory from one, two, three, or four registers, without interleaving. Every element of each register is stored. For details of the addressing mode, see Advanced SIMD addressing mode.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information, see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1, A2, A3, and A4) and T32 (T1, T2, T3, and T4).

## A1

<!-- image -->

## Encoding for the Offset variant

```
Applies when (Rm == 1111) VST1{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VST1{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}]!
```

## Encoding for the Post-indexed variant

```
Applies when (Rm != 11x1) VST1{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}], <Rm>
```

## Decode for all variants of this encoding

```
if align<1> == '1' then UNDEFINED; constant integer alignment = if align == '00' then 1 else 4 << constant integer regs = 1; constant integer ebytes = 1 << UInt(size); constant integer elements = 8 DIV ebytes; constant integer d = UInt(D:Vd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 then UNPREDICTABLE;
```

```
UInt(align);
```

## A2

<!-- image -->

## Encoding for the Offset variant

Applies when (Rm ==

```
<list>, [<Rn>{:<align>}]
```

```
1111) VST1{<c>}{<q>}.<size>
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VST1{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]!
```

## Encoding for the Post-indexed variant

Applies when (Rm !=

```
11x1)
```

```
VST1{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}], <Rm>
```

## Decode for all variants of this encoding

```
if align == '11' then UNDEFINED; constant integer alignment = if align == '00' then 1 else 4 << constant integer regs = 2; constant integer ebytes = 1 << UInt(size); constant integer elements = 8 DIV ebytes; constant integer d = UInt(D:Vd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 || d+regs > 32 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If d+regs &gt; 32 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The memory locations specified by the instruction and the number of registers specified by the instruction become UNKNOWN. If the instruction specifies writeback, then that register becomes UNKNOWN. This behavior does not affect any other memory locations.

```
UInt(align);
```

A3

<!-- image -->

## Encoding for the Offset variant

Applies when (Rm == 1111)

```
VST1{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VST1{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]!
```

## Encoding for the Post-indexed variant

Applies when (Rm !=

```
VST1{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}],
```

```
11x1) <Rm>
```

## Decode for all variants of this encoding

```
if align<1> == '1' then UNDEFINED; constant integer alignment = if align == '00' then 1 else 4 << constant integer regs = 3; constant integer ebytes = 1 << UInt(size); constant integer elements = 8 DIV ebytes; constant integer d = UInt(D:Vd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 || d+regs > 32 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If d+regs &gt; 32 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The memory locations specified by the instruction and the number of registers specified by the instruction become UNKNOWN. If the instruction specifies writeback, then that register becomes UNKNOWN. This behavior does not affect any other memory locations.

```
UInt(align);
```

## A4

<!-- image -->

## Encoding for the Offset variant

```
Applies when (Rm == 1111) VST1{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VST1{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]!
```

## Encoding for the Post-indexed variant

Applies when

```
(Rm != 11x1) VST1{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}],
```

## Decode for all variants of this encoding

```
constant integer regs = 4; constant integer alignment = if align == '00' then 1 else 4 << UInt(align); constant integer ebytes = 1 << UInt(size); constant integer elements = 8 DIV ebytes; constant integer d = UInt(D:Vd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 || d+regs > 32 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If d+regs &gt; 32 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The memory locations specified by the instruction and the number of registers specified by the instruction become UNKNOWN. If the instruction specifies writeback, then that register becomes UNKNOWN. This behavior does not affect any other memory locations.

```
<Rm>
```

T1

<!-- image -->

## Encoding for the Offset variant

Applies when (Rm ==

```
VST1{<c>}{<q>}.<size>
```

```
1111) <list>, [<Rn>{:<align>}]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VST1{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}]!
```

## Encoding for the Post-indexed variant

```
Applies when (Rm != 11x1) VST1{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}], <Rm>
```

## Decode for all variants of this encoding

```
if align<1> == '1' then UNDEFINED; constant integer alignment = if align == '00' then 1 else 4 << constant integer regs = 1; constant integer ebytes = 1 << UInt(size); constant integer elements = 8 DIV ebytes; constant integer d = UInt(D:Vd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 then UNPREDICTABLE;
```

T2

<!-- image -->

## Encoding for the Offset variant

```
Applies when (Rm == 1111) VST1{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VST1{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}]!
```

```
UInt(align);
```

## Encoding for the Post-indexed variant

Applies when (Rm !=

```
VST1{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}],
```

```
11x1) <Rm>
```

## Decode for all variants of this encoding

```
if align == '11' then UNDEFINED; constant integer alignment = if align == '00' then 1 else 4 << constant integer regs = 2; constant integer ebytes = 1 << UInt(size); constant integer elements = 8 DIV ebytes; constant integer d = UInt(D:Vd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 || d+regs > 32 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If d+regs &gt; 32 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The memory locations specified by the instruction and the number of registers specified by the instruction become UNKNOWN. If the instruction specifies writeback, then that register becomes UNKNOWN. This behavior does not affect any other memory locations.

T3

<!-- image -->

## Encoding for the Offset variant

```
Applies when (Rm == 1111) VST1{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VST1{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]!
```

## Encoding for the Post-indexed variant

```
Applies when (Rm != 11x1) VST1{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}],
```

```
<Rm>
```

```
UInt(align);
```

## Decode for all variants of this encoding

```
if align<1> == '1' then UNDEFINED; constant integer alignment = if align == '00' then 1 else 4 << constant integer regs = 3; constant integer ebytes = 1 << UInt(size); constant integer elements = 8 DIV ebytes; constant integer d = UInt(D:Vd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 || d+regs > 32 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If d+regs &gt; 32 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The memory locations specified by the instruction and the number of registers specified by the instruction become UNKNOWN. If the instruction specifies writeback, then that register becomes UNKNOWN. This behavior does not affect any other memory locations.

T4

<!-- image -->

## Encoding for the Offset variant

```
Applies when (Rm == 1111) VST1{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VST1{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]!
```

## Encoding for the Post-indexed variant

```
Applies when (Rm != 11x1) VST1{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}], <Rm>
```

## Decode for all variants of this encoding

```
constant integer regs = 4; constant integer alignment = if align == '00' then 1 else 4 << UInt(align); constant integer ebytes = 1 << UInt(size); constant integer elements = 8 DIV ebytes; constant integer d = UInt(D:Vd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 || d+regs > 32 then UNPREDICTABLE;
```

```
UInt(align);
```

## CONSTRAINED UNPREDICTABLE behavior

If d+regs &gt; 32 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The memory locations specified by the instruction and the number of registers specified by the instruction become UNKNOWN. If the instruction specifies writeback, then that register becomes UNKNOWN. This behavior does not affect any other memory locations.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors, and particularly VST1 (multiple single elements).

Related encodings: See Advanced SIMD element or structure load/store for the T32 instruction set, or Advanced SIMD element or structure load/store for the A32 instruction set.

## Assembler Symbols

&lt;c&gt;

For the 'A1 Offset', 'A1 Post-indexed', 'A2 Offset', 'A2 Post-indexed', 'A3 Offset', 'A3 Post-indexed', 'A4 Offset', and 'A4 Post-indexed' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 Offset', 'T1 Post-indexed', 'T2 Offset', 'T2 Post-indexed', 'T3 Offset', 'T3 Post-indexed', 'T4 Offset', and 'T4 Post-indexed' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

## &lt;size&gt;

Is the data size, encoded in 'size':

## &lt;list&gt;

<!-- image -->

<!-- image -->

|   size |   <size> |
|--------|----------|
|     00 |        8 |
|     01 |       16 |
|     10 |       32 |
|     11 |       64 |

Is a list containing the 64-bit names of the SIMD&amp;FP registers.

The list must be one of:

```
{ <Dd> } Single register. Selects the A1 and T1 encodings of the instruction. { <Dd>, <Dd+1> } Two single-spaced registers. Selects the A2 and T2 encodings of the instruction. { <Dd>, <Dd+1>, <Dd+2> } Three single-spaced registers. Selects the A3 and T3 encodings of the instruction. { <Dd>, <Dd+1>, <Dd+2>, <Dd+3> } Four single-spaced registers. Selects the A4 and T4 encodings of the instruction.
```

The register &lt;Dd&gt; is encoded in the 'D:Vd' field.

Is the general-purpose base register, encoded in the 'Rn' field.

## &lt;align&gt;

Is the optional alignment.

Whenever &lt;align&gt; is omitted, the standard alignment is used, see Unaligned data access, and is encoded in the 'align' field as 0b00 .

Whenever &lt;align&gt; is present, the permitted values are:

- 64 64-bit alignment, encoded in the 'align' field as 0b01 .
- 128 128-bit alignment, encoded in the 'align' field as 0b10 . Available only if &lt;list&gt; contains two or four registers.
- 256 256-bit alignment, encoded in the 'align' field as 0b11 . Available only if &lt;list&gt; contains four registers.
- : is the preferred separator before the &lt;align&gt; value, but the alignment can be specified as @&lt;align&gt; , see Advanced SIMD addressing mode.

## &lt;Rm&gt;

Is the general-purpose index register containing an offset applied after the access, encoded in the 'Rm' field.

For more information about &lt;Rn&gt; , ! , and &lt;Rm&gt; , see Advanced SIMD addressing mode.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); bits(32) address = R[n]; constant boolean nontemporal = FALSE; constant boolean privileged = PSTATE.EL != EL0; constant boolean tagchecked = FALSE; constant AccessDescriptor accdesc = CreateAccDescASIMD(MemOp_STORE, nontemporal, tagchecked, privileged); if !IsAligned(address, alignment) then constant FaultRecord fault = AlignmentFault(accdesc, ZeroExtend(address, 64)); AArch32.Abort(fault); for r = 0 to regs-1 for e = 0 to elements-1 if ebytes != 8 then MemU[address,ebytes] = Elem[D[d+r],e,8*ebytes]; else if !IsAligned(address, ebytes) && AlignmentEnforced() then constant FaultRecord fault = AlignmentFault(accdesc, ZeroExtend(address, 64)); AArch32.Abort(fault); constant bits(64) data = Elem[D[d+r],e,64]; if BigEndian(AccessType_ASIMD) then MemU[address,4] = data<63:32>; MemU[address+4,4] = data<31:0>; else MemU[address,4] = data<31:0>; MemU[address+4,4] = data<63:32>; address = address + ebytes; if wback then if register_index then R[n] = R[n] + R[m]; else R[n] = R[n] + 8*regs;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.